#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Notion to Hugo Blog Sync Script
从 Notion 数据库同步笔记到 Hugo 博客
"""

import os
import sys
import json
import yaml
import requests
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class NotionToHugo:
    """Notion 到 Hugo 的同步工具"""

    def __init__(self, config_path: str = "notion-config.yml"):
        """初始化"""
        self.config = self.load_config(config_path)
        self.notion_token = os.environ.get('NOTION_TOKEN')

        if not self.notion_token:
            raise ValueError("❌ 未找到 NOTION_TOKEN 环境变量")

        self.headers = {
            "Authorization": f"Bearer {self.notion_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }

        # Hugo 内容目录
        self.content_dir = Path(self.config.get('hugo_content_dir', 'content'))
        self.content_dir.mkdir(parents=True, exist_ok=True)

    def load_config(self, config_path: str) -> Dict:
        """加载配置文件"""
        if not os.path.exists(config_path):
            print(f"⚠️  配置文件 {config_path} 不存在，使用默认配置")
            return {
                'databases': [],
                'hugo_content_dir': 'content'
            }

        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def query_database(self, database_id: str, filter_config: Dict = None) -> List[Dict]:
        """查询 Notion 数据库"""
        url = f"https://api.notion.com/v1/databases/{database_id}/query"

        payload = {}
        if filter_config:
            payload['filter'] = filter_config

        all_results = []
        has_more = True
        start_cursor = None

        while has_more:
            if start_cursor:
                payload['start_cursor'] = start_cursor

            response = requests.post(url, headers=self.headers, json=payload)

            if response.status_code != 200:
                print(f"❌ 查询数据库失败: {response.status_code}")
                print(f"   错误信息: {response.text}")
                return []

            data = response.json()
            all_results.extend(data.get('results', []))

            has_more = data.get('has_more', False)
            start_cursor = data.get('next_cursor')

        return all_results

    def get_page_content(self, page_id: str) -> List[Dict]:
        """获取页面内容块"""
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"

        all_blocks = []
        has_more = True
        start_cursor = None

        while has_more:
            params = {}
            if start_cursor:
                params['start_cursor'] = start_cursor

            response = requests.get(url, headers=self.headers, params=params)

            if response.status_code != 200:
                print(f"❌ 获取页面内容失败: {response.status_code}")
                return []

            data = response.json()
            all_blocks.extend(data.get('results', []))

            has_more = data.get('has_more', False)
            start_cursor = data.get('next_cursor')

        return all_blocks

    def extract_text(self, rich_text: List[Dict]) -> str:
        """从 Notion rich text 提取纯文本"""
        if not rich_text:
            return ""
        return "".join([text.get('plain_text', '') for text in rich_text])

    def clean_url(self, url: str) -> str:
        """清理 URL 中的 AWS 签名参数，防止密钥泄露"""
        if not url:
            return url
        # 移除 AWS 签名相关的查询参数
        # 匹配 ?X-Amz-Algorithm=... 或 &X-Amz-... 开头的参数
        url = re.sub(r'[?&]X-Amz-[^&\s\)\"\'\]]*', '', url)
        # 移除残留的 ? 或 & 在 URL 结尾
        url = re.sub(r'[?&]$', '', url)
        return url

    def get_property_value(self, property_data: Dict) -> Any:
        """获取属性值"""
        prop_type = property_data.get('type')

        if prop_type == 'title':
            return self.extract_text(property_data.get('title', []))
        elif prop_type == 'rich_text':
            return self.extract_text(property_data.get('rich_text', []))
        elif prop_type == 'number':
            return property_data.get('number')
        elif prop_type == 'select':
            select = property_data.get('select')
            return select.get('name') if select else None
        elif prop_type == 'multi_select':
            return [item.get('name') for item in property_data.get('multi_select', [])]
        elif prop_type == 'date':
            date = property_data.get('date')
            return date.get('start') if date else None
        elif prop_type == 'checkbox':
            return property_data.get('checkbox')
        elif prop_type == 'url':
            return property_data.get('url')
        elif prop_type == 'email':
            return property_data.get('email')
        elif prop_type == 'phone_number':
            return property_data.get('phone_number')
        else:
            return None

    def block_to_markdown(self, block: Dict) -> str:
        """将 Notion block 转换为 Markdown"""
        block_type = block.get('type')

        if block_type == 'paragraph':
            text = self.extract_text(block['paragraph'].get('rich_text', []))
            return f"{text}\n\n"

        elif block_type == 'heading_1':
            text = self.extract_text(block['heading_1'].get('rich_text', []))
            return f"# {text}\n\n"

        elif block_type == 'heading_2':
            text = self.extract_text(block['heading_2'].get('rich_text', []))
            return f"## {text}\n\n"

        elif block_type == 'heading_3':
            text = self.extract_text(block['heading_3'].get('rich_text', []))
            return f"### {text}\n\n"

        elif block_type == 'bulleted_list_item':
            text = self.extract_text(block['bulleted_list_item'].get('rich_text', []))
            return f"- {text}\n"

        elif block_type == 'numbered_list_item':
            text = self.extract_text(block['numbered_list_item'].get('rich_text', []))
            return f"1. {text}\n"

        elif block_type == 'to_do':
            text = self.extract_text(block['to_do'].get('rich_text', []))
            checked = block['to_do'].get('checked', False)
            checkbox = "[x]" if checked else "[ ]"
            return f"- {checkbox} {text}\n"

        elif block_type == 'toggle':
            text = self.extract_text(block['toggle'].get('rich_text', []))
            return f"<details><summary>{text}</summary>\n\n</details>\n\n"

        elif block_type == 'code':
            code_data = block['code']
            text = self.extract_text(code_data.get('rich_text', []))
            language = code_data.get('language', '')
            return f"```{language}\n{text}\n```\n\n"

        elif block_type == 'quote':
            text = self.extract_text(block['quote'].get('rich_text', []))
            return f"> {text}\n\n"

        elif block_type == 'divider':
            return "---\n\n"

        elif block_type == 'image':
            image = block['image']
            if image.get('type') == 'external':
                url = image['external'].get('url', '')
            elif image.get('type') == 'file':
                url = image['file'].get('url', '')
            else:
                url = ''
            # 清理 URL 中的 AWS 签名参数，防止密钥泄露
            url = self.clean_url(url)
            caption = self.extract_text(image.get('caption', []))
            return f"![{caption}]({url})\n\n"

        elif block_type == 'bookmark':
            url = block['bookmark'].get('url', '')
            return f"[{url}]({url})\n\n"

        elif block_type == 'callout':
            text = self.extract_text(block['callout'].get('rich_text', []))
            return f"> 💡 {text}\n\n"

        else:
            # 未支持的类型，返回空字符串
            return ""

    def create_hugo_frontmatter(self, page: Dict, db_config: Dict) -> str:
        """创建 Hugo front matter"""
        properties = page.get('properties', {})

        # 属性名映射：Notion属性名 -> Hugo字段名
        property_mapping = {
            '标签': 'tags',
            'Tags': 'tags',
            'tags': 'tags',
            '分类': 'categories',
            'Categories': 'categories',
            'categories': 'categories',
            'Status': 'status',
            'status': 'status',
        }

        # 提取标题
        title = ""
        for prop_name, prop_data in properties.items():
            if prop_data.get('type') == 'title':
                title = self.get_property_value(prop_data)
                break

        # 提取其他属性
        frontmatter = {
            'title': title or "Untitled",
            'date': page.get('created_time', datetime.now().isoformat()),
            'lastmod': page.get('last_edited_time', datetime.now().isoformat()),
            'draft': False
        }

        # 添加自定义属性
        for prop_name, prop_data in properties.items():
            prop_type = prop_data.get('type')

            # 跳过 title 类型（已处理）
            if prop_type == 'title':
                continue

            if prop_type in ['select', 'multi_select']:
                value = self.get_property_value(prop_data)
                if value:
                    # 使用映射表或转换为小写下划线
                    key = property_mapping.get(prop_name, prop_name.lower().replace(' ', '_'))

                    # 如果是 tags 但值不是列表，转换为列表
                    if key == 'tags' and not isinstance(value, list):
                        value = [value]

                    frontmatter[key] = value

        # 添加分类（从数据库配置）
        if 'category' in db_config:
            if 'categories' not in frontmatter:
                frontmatter['categories'] = []
            elif not isinstance(frontmatter['categories'], list):
                frontmatter['categories'] = [frontmatter['categories']]

            # 添加数据库分类（如果不存在）
            if db_config['category'] not in frontmatter['categories']:
                frontmatter['categories'].append(db_config['category'])

        # 生成 YAML front matter
        yaml_str = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False, default_flow_style=False)
        return f"---\n{yaml_str}---\n\n"

    def sanitize_filename(self, title: str) -> str:
        """清理文件名"""
        # 移除特殊字符
        filename = re.sub(r'[<>:"/\\|?*]', '', title)
        # 替换空格为短横线
        filename = re.sub(r'\s+', '-', filename)
        # 转换为小写
        filename = filename.lower()
        # 限制长度
        filename = filename[:100]
        return filename

    def sync_database(self, db_config: Dict) -> int:
        """同步单个数据库"""
        database_id = db_config.get('database_id')
        section = db_config.get('section', 'posts')

        print(f"\n📂 同步数据库: {db_config.get('name', database_id)}")
        print(f"   目标目录: {section}/")

        # 查询数据库
        filter_config = db_config.get('filter')
        pages = self.query_database(database_id, filter_config)

        print(f"   找到 {len(pages)} 篇文章")

        # 创建目标目录
        section_dir = self.content_dir / section
        section_dir.mkdir(parents=True, exist_ok=True)

        synced_count = 0

        for page in pages:
            try:
                # 创建 front matter
                frontmatter = self.create_hugo_frontmatter(page, db_config)

                # 获取页面内容
                blocks = self.get_page_content(page['id'])

                # 转换为 Markdown
                content = ""
                for block in blocks:
                    content += self.block_to_markdown(block)

                # 生成文件名
                properties = page.get('properties', {})
                title = ""
                for prop_data in properties.values():
                    if prop_data.get('type') == 'title':
                        title = self.get_property_value(prop_data)
                        break

                filename = self.sanitize_filename(title or page['id']) + ".md"
                filepath = section_dir / filename

                # 写入文件
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(frontmatter)
                    f.write(content)

                synced_count += 1
                print(f"   ✅ {filename}")

            except Exception as e:
                print(f"   ❌ 处理页面失败: {e}")
                continue

        return synced_count

    def sync_all(self):
        """同步所有数据库"""
        print("="*60)
        print("🚀 开始同步 Notion 到 Hugo")
        print("="*60)
        print(f"⏰ 执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        databases = self.config.get('databases', [])

        if not databases:
            print("\n⚠️  配置文件中没有数据库配置")
            print("   请在 notion-config.yml 中配置数据库")
            return

        total_synced = 0

        for db_config in databases:
            try:
                count = self.sync_database(db_config)
                total_synced += count
            except Exception as e:
                print(f"\n❌ 同步数据库失败: {e}")
                continue

        print("\n" + "="*60)
        print(f"✨ 同步完成！共同步 {total_synced} 篇文章")
        print("="*60)


def main():
    """主函数"""
    try:
        syncer = NotionToHugo()
        syncer.sync_all()
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
