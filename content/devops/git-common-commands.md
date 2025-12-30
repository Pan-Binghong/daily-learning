---
title: Git Common commands
date: '2024-11-20T01:22:00.000Z'
lastmod: '2025-04-03T07:41:00.000Z'
draft: false
tags:
- Git
categories:
- DevOps
---

> 💡 Git代码管理规范说明，以及常用命令。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYOFGJX%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJlbIh65yBgV57o1ZuRlgtr8JMOvu1Azr7WvctqJQhMgIgVv21omMzXNbA%2FAjX5fb8ZS63nJcCkEeNyITTp2Hq2PcqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKFlzXbHowmo3T2SVCrcAwBFsHwvPg3I7FwkaKjuQa5ARB20xiATQ7QQc8ZIgVDncuurrXNYZNYului2aez8E%2FTE46Vi4Vrnc%2FcL82RM4cdVaOxz8v%2BVCPpRppoSt%2FqQDfy69yixmWqUztVGtg%2FrWrpF3vPg2e0DxL9okJWH4SAPcCSAFnjmsz%2BnX%2B%2BU%2BPjRCOIEWLhQf5E4hc2bEFAksOtC2FOn0xiwBwvrXNbyCkVMucN0aDJ9%2B%2BpmyE5qzwuCAt1fRxXRMSxRqgfDCgh3V9jLv38iYkiOOAX8iSq4SX71nqoz463SimAHBB5HWksw8BJbhyj4bkacYqPcIxSbb9nwWGzbRBy2gCgPYo5x4T8e1gzBDEOPDhlccefz%2FlPSK8ef4YLc4Y1K9xJSThWqpCMIAsS3ez3hrsZ6tnWT1aaFxhBTpIX7nPA1QWNJ0fR3Zk5ArPc65MGWWvAgu59HMr7Nzy7V%2FyFQLKv4yUi7eM7J7Qz7XN9B4LVcSe5jWYRJn3W3ijONGq%2BqxgI%2BIcjNbydRo0LXG716Zp2%2BsQV%2BKc9k3wtXQ7vQAqIB0ZYlkc38apzSmA%2F6amRZbX%2FJbtSuMzOfDN34y53z8BvT%2BaHd7nF6uSuem6nXnAHS58btosIyycED2bLg1pqtmcn6MMLdzMoGOqUBHCKjcANcWPuF5yZKESCEc2JmBLzsatOzM8XaBxq%2FtNx2xA1dqBiM2YMDdGVwCwaZvWqH7G1lhe%2FeuK8Iu7I6QNuCtvvOpfDhzPNxX9QQjNXKrBgRv3gi6z%2F4NruYbqv7DipRQSvzB3FHkRIEfwb7hFPCpK%2BppS4dXSg3C78ecJjQCudJxD2hoz7SeWWGx15FrDdx6o6Zyuz9hoyHFUMgRuUGW4TR&X-Amz-Signature=bff33d535ec5ecebaa42a7d50f9a29b869688677321680e16b00ecd04cb47ebc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 分支说明

最常见的三种类型分支，名称与解释。

- main
- develop
- test
开发人员经常创建的两种临时分支。

- featrue（功能）
- bugfix（Bug修复）
---

## 工作环境常用命令

### Git基础常用命令

> 💡 想多看就继续看吧。以下主要涉及：上传并提交，合并，标签等操作。

1. 添加到暂存区
1. 提交到HEAD
1. 提交到服务器内的仓库中
1. 分支操作
1. 拉取以及合并
1. 标签
1. 替换本地改动
---

### Git常用配置

- 解决win和linux换行符格式问题
- 解决旧版本初始化分支名称为master问题
---

### 实战经历

```bash
# 初始化本地仓库
git init

# 创建并切换到 main 分支
git checkout -b main

# 添加文件
git add .

# 初始提交
git commit -m "Initial commit"

# 推送代码到远程仓库
git push -u origin main
```

> References

