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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q43GMJY%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6InHBLVt0CsUBAxEAV6TMJ1R7%2BpaJn4fNi2CpgfiisgIgDZSXbOK93P%2B4SRpccylnm8hvuTBmCnCMB5Dr0LTOfs4q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDMM2hcgDch2Rrxt%2BfircA51%2FvwMUgydrzAKrAtS7q%2BlfcmznmQZlfws0XDtbPD%2FKXsq%2FT8cj%2FR90KgQYCwJEZ2xy%2FXis8Dofd7IBkeVywG69K4vTqThVb6oLGNsphaAY0qUiDOs02HMsoAXf0tvSxSeD4Ej6fSOPPHmoZNA44SjIKAs8SACmNPUhUZyei0Nlbd1N4%2BC%2BoO5arC%2FjTgU9XXoqcBTNX0sLZSwH3%2F6avhSae98C8Hgmm22uXuf%2Be4wJSFy2gJg4nD2EUbTdUZTOnSYMSg62h6PzzIl30%2FkdAKZteTzA1g7o2BPLVN7FOYv5ejnryxLcjIwTndV%2FgTYQBMBkNW99ai0dlEcPOWMStZA0Vju0VTSCUpefKYCPcvXy1E22Gco0L9huVcU%2BsplM8skVdaDnbOtJFR3j3eUG%2BFr7k8PtvUYuwNCup6O5m1hrC13aj1A5Ov3fxaHord%2FQKJhsZy6kESA7timyZUDemMUx52UupdJJM2gczqzVAEis71NAmlOsKuJ%2FB5O2a3UsQlnU1qSJTNSojCCeuKTT5S5jvWBPDEjUBvOKUNFSvOnjNrNG%2F9Wr7FsBK7UpPsUHd3W%2F6zK4jpPZmAvxPuAxIFyu%2F5FHLUAwLSlqI1yjqAOxPCQuPTazg%2F35RlFAMLuJ2sgGOqUB1J7X7qiQThHPLiPj9IT%2FC8W4ZUC1XTc3dE4gTpqUr9zBykOhviD9fLuwbLLt7%2FJTLcPsXJ6lhuivmr93PG8qE6A1P1KEtnlUDOkX43F8z2eg95zuiF9qpTaj1jwviMOX5qbk1DlzqvX72VX74pSfQDYyGSUWLn4Bpx1EEBwEmKA8cnxmUMPLsB%2FW7l9PQqGFbJpwKB9GTBsI6wyKsyZ3EHYtDHc9&X-Amz-Signature=cdee98a2b21e3295a96b3b06d310a9552bd6b1f9cf103c41e6235c0fea6ae3e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

