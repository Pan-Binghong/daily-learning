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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJNXEUFV%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDwVdyZSaICtECZwjp22uCySD7vBvcoRRJYnMTIC97GMAiAmWybKH%2BW639bICHfm4nri%2BzrdTXsyIBiAORnKtbpt6ir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMQXDrm2i2ppNCFsLfKtwDhUdvYVjoQeEYd1OqtwuqnEayEAQWB5WJ9NzJ0poXkwhs6bra4On0WNaag3EgL2PrPIGtVu56TPFTBtGFYRQAN5hdOE9BWLhQ%2F1T38TOETJAqErlc584lxZ1CK5Hgba2nyP8iJGKmFs126ymrTTp7iHx9E9GNicX4LalCXVzKMzzcyiqtGNAN5FtZD1ySM3s4dEiddjUBWv%2FO3CA8BxFO7niKLIYnd4Cw8T7aezfC5%2BofwI4QbEQjWvvOCwx3VmGMcoNmya2FtcMzyh1msIi7cqOA16prx7jfa6Ps4rpkqFsw781bgfmoy7LbO%2ByH0a6JJBqeVCNIHLcNG3i58CTi1WhIWc3OeyPehGH%2FtT5ulwFtQ6sGFMiq%2Byt6%2FKYhE113qasdiJcd7TXk4pRg2PvE5WOr2ekjPKw%2B7RgWsyf7bDcsn%2FQGMOa2w2ferStazlbOP7rnFRgKa%2F8pzhRXWx719hYbhsqiP1v3GlvCx%2BKAZP17WEx6oZEGmim3LG0wSyEdw3s03R0WMZ6BXP4vcGsLtMiMf6BVRgeddqk3j68II8LdNzabElkDQrF%2FeyGhdd8KYCvlGzCM%2BmE556X72dKyyJHcBFhCEu7y%2FZYQteZvBgjKf6%2BA6csqObqzIqsw56y9zgY6pgG5lfJgmuTd7ef12ihe7RavESHKsfxHV1dmvDn%2Fi77qm4PPQCo%2F5LroVEiX5DAJY6oIVfUoOwcs9qAdPqYuFSSrgqVWnlnRSbbzHDokb1ugHQahr%2B80DI4xDFt9LUYu2Bd7s3qVOV2zor6pnRYDPdLDtZL34Umbq%2FlFODVe9kkWSER87tt5odSRAxN6O0EEX8GCOE8JjYbR9kU4RjX2fkUSdFkFltV7&X-Amz-Signature=f4102f35f3f8e3f9564938dc14b13e8f95ea5f36b03548e1c80beb9e1d3275d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

