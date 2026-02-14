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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S63HKBL5%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICdXqoPbAhBN0wDjkCRt6wtkkTk6Gbhi5UDzyN%2B160K%2BAiBJ9LuhHAt7vCGK4s3ne62Kzy5MIX2VcB8baQTu30M0EiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkhoMc6KIeX0XlwhLKtwD2ww4eJOuzMPs28P2ska1JtQSSWnHKT85D5sM4%2FkgDBmXMZFkvUjJ7nUT88kmj8R6mEivItVaX8fBgSW1Q55%2BdZLdmARlONPcBIWXKeV7xER8l%2F5SxToElR7qQq2BziAMTIs%2Bxn%2F3JHrIqOLVgpZ9V0wYL5zPOSjLPqxPXEdzbNgwlxMcNtEudg7%2BD10cZKJO0UW8cwQErtTKVm34O5it%2FwkwC4wHvjLTZJQvUpmfu35NU5m%2BvhZ5M29LgM04TXAqRpWeHniHQctRt%2B7wy4y3n34RctuXs0LZcKXEEZYzyuFg6fEsgpkuQZyYSge7ClC2k2U67aFxYOfLnCGqTrIKeIETmEdE22gv49V7XetLzgsNXi0PjdJj2EsluD6Cu2j4wIQxNqoBvbZ0dfxHmEt5R1pcC7kdd920Ip8NznMfULQdOC1EBrLtSTMvTc%2B0EdEJaLpFDHKMT%2B0x8Z7WHYp1278V96Nwug23jY1HhCm4npQEyCF8l5ryG%2B3Ke0ry3IEQk705QVTsc1T2pPRsuukpP6ZKr3Fmc0k%2Bd%2BJKdLeWmqfgfwYnEsy7GWRqKVg6NLaiBOahKz6DN%2FlfG%2B0947U2Br6h7E2Zk0oXKmW9kfo3Gqn5M6VayR%2FXP%2F67OXEwmsC%2FzAY6pgGUM%2F2carkwvC7tQEHnP9zMQU4Ej%2BGUs1O2babUsTkS0lSK8s5ME7LyKKE%2BrUH3V4x5BcNgu6yp3aJYzG1ac%2BBjQrNePOpRyxj1F8NiDQZx4jf6KY31qz1xIYmvQmifUrBjAUzaMlc7McGfRQs43eSsB8rg7m%2F5AkinEHIKBEDRfxv5I8ws%2B461HSCydGa7zbikCYM4hmS7Fe8gOwBfLHKHtSf6ONM0&X-Amz-Signature=05b38e65811e8ac64a9bb7af1aa188162bc4aa5e041865e9d34476f03364c1bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

