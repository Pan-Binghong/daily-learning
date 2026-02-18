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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXI4J3Y2%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2V0G%2FZaLs4q2Hrn8lZU4ZfkZ9isG%2F8R78yv4VLLugKAIgZ5IbUsbzukn1FjIOe4tD1ALKkJZUAmAyc0ac7E4a4Ogq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDnNhzMB%2B8IIaSrsUyrcA3VU34AW6nH5CLrozGJ9fcEPRIdIcyq6meLx37qlS%2FaP%2FfmG6h63yKJJJt41sx74I%2FUCWX0Vqbn4IrzNz5DqBKYCCm4dbd1lC9IKh4b88X0Qx1J%2FigzdMUmPugVNVXc5EbomAzAByaLfti3g5khy2Lcvo%2FQLKogK%2FPGaXa4PjNbaAh6hAdxT8t3USkP8beRrSFn%2Flujj4v1sBmuxrGAytvbQ%2BS99wX2E9wslLOVIXb4SbAMJcTcjAEqDt2ev5CxTlRzarlDpA5rscRA6H%2FOhiup1AieBJz2v68cEwE3zT1gw99HAd1XTNUQsmRBR3yDfo9gxseYmQ8LWZA%2FqvkZ4%2BC%2FNPhuOzh0JTrs4ThG%2BBzpcpWHmMV%2BCPXZ51vQPBWcxK%2BdXtmULrEvteXxaE7C0VJ195E4txjHpMCieF0j6cGAiWfc39psPEnIoRvOuyoLZLU%2Bw88B4aisKwFP7HU30ceXfoJm5J4QiEtEWVefqbXwt0%2FXRtvGQnh5mG6GroKFuWiCDlGuxFTomQRHD7gRMnD2TZ0Y1hz2eDVW%2FdRtciEWofNDfdUw%2F8FMorFBha%2FZhtItRyzMdypGe34Sn2KgwVhRMwMvpQxj6JAJHLueLmxQZ6%2BpzRwD%2Buu3DV%2FkGMICf1MwGOqUBtmSu8mUhdp3mYStuvytEz44j9y5WY57fA0a2nDKG%2BwuGfhrsaLvB8bz39wwOWg6I66M9ZjwZFtz182rbyOjVfiAoCN3KYP1YaZgk8ZknzlRGLooyGqfkZN44a%2FEc00uV0y4p1cXbuCOrrKFKX3V%2FnaPXRirci9rcnBihEnk3kcpDjT%2FwAooN6FYANosMnOnYF68t%2FBSuDbiyY7KorNxnIGQ6i1%2FC&X-Amz-Signature=2a5601cc243ea6a4ec5bb099b641c9e560eefb84d8bff702f9d444dfe6c60887&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

