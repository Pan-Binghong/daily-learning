#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的定时任务脚本示例
"""

import datetime
import os

def main():
    """主函数：执行定时任务"""
    current_time = datetime.datetime.now()
    print(f"定时任务执行时间: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"时区: {os.environ.get('TZ', 'UTC')}")
    print("任务执行成功！")

if __name__ == "__main__":
    main()

