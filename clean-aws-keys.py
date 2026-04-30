#!/usr/bin/env python3
"""
清理内容文件中的 AWS 临时密钥
移除 Notion 图片 URL 中的签名参数
"""

import os
import re
from pathlib import Path

def clean_aws_credentials_in_file(filepath):
    """清理单个文件中的 AWS 凭证"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 匹配模式1: ?X-Amz-Credential=... 到 行尾或 )
    # 移除 AWS 签名相关的所有查询参数
    patterns = [
        # 移除从 ?X-Amz-Algorithm 开始到 URL 结束的所有 AWS 参数
        (r'\?X-Amz-Algorithm=[^\s\)\"\']+', ''),
        # 移除 &X-Amz-... 参数
        (r'&X-Amz-[^\s\)\"\']+', ''),
        # 移除 x-amz-... 参数
        (r'&x-amz-[^\s\)\"\']+', ''),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # 清理残留的 ? 和 & 在 URL 结尾
    content = re.sub(r'https://[^\s\)\"\']+\?["\'\)]', lambda m: m.group(0).rstrip('?'), content)
    content = re.sub(r'https://[^\s\)\"\']+&["\'\)]', lambda m: m.group(0).rstrip('&'), content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    content_dir = Path('content')
    cleaned_files = []
    
    for md_file in content_dir.rglob('*.md'):
        try:
            if clean_aws_credentials_in_file(md_file):
                cleaned_files.append(str(md_file))
                print(f"[OK] Cleaned: {md_file}")
        except Exception as e:
            print(f"[ERROR] Failed {md_file}: {e}")
    
    print(f"\n{'='*60}")
    print(f"[DONE] Cleaned {len(cleaned_files)} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
