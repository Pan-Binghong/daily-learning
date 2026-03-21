#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动提交随机代码到 GitHub 仓库
"""

import os
import random
import datetime
import subprocess

def generate_random_code():
    """生成随机代码内容"""
    languages = [
        "Python",
        "JavaScript", 
        "Java",
        "C++",
        "Go",
        "Rust"
    ]
    
    code_snippets = [
        """
def hello_world():
    print("Hello, World!")
    return True
""",
        """
function calculateSum(a, b) {
    return a + b;
}
""",
        """
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
""",
        """
#include <iostream>
int main() {
    std::cout << "Hello World" << std::endl;
    return 0;
}
""",
        """
package main
import "fmt"
func main() {
    fmt.Println("Hello, World!")
}
""",
        """
fn main() {
    println!("Hello, World!");
}
"""
    ]
    
    language = random.choice(languages)
    code = random.choice(code_snippets).strip()
    
    return language, code

def generate_commit_message():
    """生成随机的提交信息"""
    messages = [
        "日常代码更新",
        "优化代码结构",
        "添加新功能",
        "修复小问题",
        "代码重构",
        "性能优化",
        "更新文档",
        "日常维护",
        "代码格式化",
        "添加注释"
    ]
    
    emojis = ["✨", "🐛", "📝", "⚡", "🔧", "💡", "🎨", "🚀", "📦", "🔨"]
    
    message = random.choice(messages)
    emoji = random.choice(emojis)
    
    return f"{emoji} {message} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def commit_and_push():
    """执行 git 提交和推送"""
    try:
        # 生成随机代码
        language, code = generate_random_code()
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # 创建随机代码文件
        filename = f"random_code_{timestamp}.txt"
        filepath = os.path.join("auto_commits", filename)
        
        # 确保目录存在
        os.makedirs("auto_commits", exist_ok=True)
        
        # 写入代码
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {language} 代码片段\n")
            f.write(f"# 生成时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(code)
        
        print(f"✅ 已生成代码文件: {filepath}")
        print(f"📝 代码语言: {language}")
        
        # 配置 git（如果还没有配置）
        # 优先使用环境变量中的 git 信息，fallback 到账号真实邮箱
        git_email = os.environ.get('GIT_AUTHOR_EMAIL', 'binghongpan0222@gmail.com')
        git_name = os.environ.get('GIT_AUTHOR_NAME', 'Pan-Binghong')
        subprocess.run(['git', 'config', '--global', 'user.email', git_email], check=False)
        subprocess.run(['git', 'config', '--global', 'user.name', git_name], check=False)
        
        # 获取当前分支名
        branch_result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], 
                                     capture_output=True, text=True, check=True)
        branch_name = branch_result.stdout.strip()
        print(f"📍 当前分支: {branch_name}")
        
        # 添加文件
        subprocess.run(['git', 'add', filepath], check=True)
        print("✅ 文件已添加到暂存区")
        
        # 检查是否有变更
        status_result = subprocess.run(['git', 'status', '--porcelain'], 
                                     capture_output=True, text=True, check=True)
        if not status_result.stdout.strip():
            print("⚠️ 没有需要提交的更改")
            return True
        
        # 提交
        commit_message = generate_commit_message()
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print(f"✅ 已提交: {commit_message}")
        
        # 推送（使用 --force-with-lease 更安全，但这里直接用 push）
        subprocess.run(['git', 'push', 'origin', branch_name], check=True)
        print("✅ 代码已推送到 GitHub")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 操作失败: {e}")
        return False
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return False

def main():
    """主函数"""
    print("\n" + "="*60)
    print("🚀 开始自动提交随机代码")
    print("="*60)
    print(f"⏰ 执行时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    success = commit_and_push()
    
    print()
    if success:
        print("="*60)
        print("✨ 自动提交完成！")
        print("="*60)
    else:
        print("="*60)
        print("❌ 自动提交失败！")
        print("="*60)
    
    print()

if __name__ == "__main__":
    main()

