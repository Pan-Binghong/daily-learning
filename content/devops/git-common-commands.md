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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFACECSB%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrraNItDHULImNp82CQ%2Bzt3m0nyI5cs3B7eMV63LdLNQIgdmIHfv5wgQOoXOOH%2FTc61sqHvrblq6yGwuZvDvmAE20qiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhkxzpzta33SomdRSrcA%2F%2B5WmaFpJ5laEdfriWxDWcgw4h9%2BGXCjeLsNODArSn6gZ6v4Emx%2BLhaa1Q%2Bcz7RvvqFSEOq2xtTI11lVwFlZTq9%2BiLNxoO5hMopP5qW%2BpZaDkqXkt8l0q%2BZzwlxkdLwYyKwhvJcTfR%2Bp8WhhXbeco14hidPFZdVsJkuFNIcipm48XhKYk0SYo8S0g4E4X21GQdXJj0dSicJqXDhu4hsSU%2FeKOSJ81P%2F%2BCVqVbGr4s%2FOhmJ8ZPPEkVy1FElIzBtcm%2B8kVXAi286bCY%2B%2BcIvheZ7LW7Jg1Nkv5Y7f%2FskuzZzvt1K5UhLAWa4AJJNZ6e8hoUNFXZhwoFr0oFSn8LnjTGRNS0PXaIJCi58x3JnYI2HK3LVcwXcrpEDT0G9DMDAU27Yj4yNAnu4D3ud4wq338DSeVr1YpY0sna7PQL9OhxLCsSBgt1%2ByK%2BJKvpESmaW6Mc0LXKZgAJldRXEtD2nRSrt%2FxwRE5Y6HdR6dCR0g4u%2BPduPS%2BdYQOEscGiyujq86a7xIPIMhdblhbTkFcnqrYkyDkltGGBKEF1xlrHTu7si8lPnEPDR3wVPHEDXYnADCK65Ms7AuTk08fZgLKJTe5DRk6q7lYQ7XkpnTxl00UAZ2JQ%2FKkxprzPFkceSIMPiOts8GOqUBFZz1uw%2BIm%2BK03hOR%2FytvvOtbZIim2wCEIloEcvoAB7CK2tanG7bUZyJUQCEgkNDCbcy5QMqGtmD8R%2FOK09ZN%2B7XyOYREanj19AclVLw1MQZBH%2Fv2Xxozi2R3zbvF092kLLBMssqdfEXEu%2BDq%2FW2alapiv68nhSYG2jGD%2F43Avq49rU7AuK83jlhI2cn%2FQUbV5wzyExUoub%2BSOPSt1XkNZ0q3BApj&X-Amz-Signature=3d6c1e1055f908e095df13b9a8bc05bb547ea0118661ee58b851ad184e2c6444&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

