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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XIDNNVO%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg0A7w3Vj1U9nKXiiB4Z3WzB7AdgTRNLYD3odLGSiM3AiANgLgszpXrClwbw6PHzfP2OtJ4tNyvFfwrLOxoOokuXyr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMeDblcnOask44o5aXKtwDP3EJOi92XIAbZFdLv5LUZaXahfkn4bw5NmjYNMBBTo88kjpLchhopUxr8EERgxF90TlVGcRblkBGs5tXPVE0JS%2FOGk9Vc7bPPoFeneBo%2Bi7QtKebDv4efOJTHu%2BiU0y25NtqpoD4cGRB%2BWjAnEMu1rN5uBf%2BjoVdSbxFI%2BbHLLoLTwdQWxV7udQ9uGGLElXnAHxb%2BiUIObC2g6m2sMHXoTlg4acMegt4HJJ%2BY%2BebYFbilxgWG0Q1r7rQ%2BRxNNFpT37HOrgnrFJQrPcdrg0%2BC4xjrtC48zk58ubkeisanMivREec9N8ufeGLSJKYwRACxnuSh1mCkkfOoo4QQ%2Bd%2Fdn65Klxz%2FMzJCPdK51921sV7gn1nb68KpKXSRFyHb7eaxB8spGRPZ6fHqOrr9X2%2FVVhyTY1fhfW480kxDjgmdkcae0oqezgJzO2WUFk9e6C9k8d%2BUou3MTa%2F42c9%2F%2BQXWRaeEAKJdPO%2BoI4kfcDCrDei0hcwacMDENcPgK4q0UAY30isqoIK%2FAj0DcmYJp9RlSDZKPSscIRlWBJU6AmVllApsSEA7ZS%2B6LsdOp%2FYgwOdEQdBl5bNf0GqJaDp8bcr2suFMrpHz133RUSTTIJTMxoRl%2BBeWPFz%2F892f8xow4rb9zQY6pgGkW0FVfAz4p6EHj2Cd3BLCYrnoLJyltwVwLh7XvO56JvSWrmojKAkt4U57lUahimAOZWiwXMZJHXtZJpU%2FtG8tuSTVAAVmbbo9zULun%2Fp%2Bz3SUyxiITtrBsruf5T1MUzWB2gdBoQ%2F2xPWDKRKGW1pHhZH7kKnTloC5nGkFSbAuklPlNRJ1HBTcM6RGGblikZuzQRjSZL7T48%2B1u8HB0Wnlb%2Bh7RHxA&X-Amz-Signature=6d26165368a1e46cd49632ca8694186330170c4b6b889f0533d06c2b90146ddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

