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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XURPEDFC%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIG9sL8%2BkWi2pI5bKsGfAvmEg9qNg5B9jElM7ZYAEWRetAiEAt9WTRCkE2aMpf7ShOA1%2FYBnINs9Am3heV9Ls5i868O4q%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDHKzxaSQa%2BZoJKzAFCrcA2Gl5%2BI%2BUFzz2E7R7fvjJuCbppzOjqr0WVLt0k3v8tc5ADdxPAQqSa%2BwwRi2nZdhoTZ1ZXvdZVM6phB4QVwOL8pvp4AyWxc6%2BXMsYwBSxSdKY%2BrPxBPUaorif%2BfkkqAamXUquQxkfAKf1Vh1RJpyXI4Hkod19E10SzRM8bkGsdZRPm%2BcKX%2Fj3Lzn0zLURC4V235ID%2FbJOKn2UV5ARxXM3RF%2FUjPYudbBQycW4G%2FVHFseEHitu19fl0iuMcoKSXBTL5lQ0bTE7MBdDVAUhyBHVpdviyur98EO3GqATnebCEkBJUuxwhi2cgUsLEPwjL0etDKhY4X987M7mQ8OwhNpW7QdsqEH%2BaG9ygP%2BEMQ5Ewam21SgQ0XyZzPjdFJNY%2FCvYImrnKMxLYMM9ACLPN3GZgZgsHbr8DgRhsXkMBcjuNHXHGbDn%2BgRLQIAVlGB%2F64z8amUrk8mwfSSS2QoaQ%2Bsx3hnFJT3J4RaytGUUo8tAzP7hlqiqdOrRJZ9YZ9NL2XkCG%2Fvro9fcqtwieiblLKsRmaeeckUb1g4QSClGXw9Fo4WZN9oQqP0TOrsS%2BtbffgCBu4xA9faew4fQpDPbO4oe7bCExJzYNoSq7fItRllVr4T4JmOa9jPN6EysyD6MI38p8oGOqUB%2BvaO%2Bu%2FMxKFQkDVC0dNUgmKxEyjkSW0dRJ9iVsLA2Uds8gNgQyI7%2FT7Ld2RXZvUCRV9bnLQv%2FMgaZjALc0KLPFJLoqTXCFIq%2FQ8F%2Bp3WSBkfrRQ9KonfFhVNgcVMYlrO2n7c%2Fc3mtUiEBSmtVly0ArdMTfDlraGOFtsrCh3ItREis7t7p7vbSxlpRh%2FyQu%2BqtJouhMiioRLDFKiyVrVuTIPoX01H&X-Amz-Signature=1c1f0836cd7dda19fec51670a66688fdb2ae42f50875c3b37694e20cebcd0ad6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

