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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPTYNBZM%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCICVtdIlBC09bsBhjhe94QcsbWxotO8RO%2FINoOTPL5ogMAiEAl%2BqgNyW8%2BMyZeSZ%2BW4%2FkSyWrCxMjenzfhvUf1KUF%2BG8q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDCasdb35a7o%2BSFmPZSrcA%2Bc7bBVVXB507pO6eKw3ATFYxMxyne3piwxOjdgKCARGddJ3AkSHGRVjoYbWs7GwI%2FxyP8riNIC63%2FIE%2FXuwP6OLQHpLY9DCZGWbKcWvHeGl%2FSDNzGi%2FUctf05G3CypoKMRrzevSusE0dXZNIncM2RePUwZ7ki22s4hBuLO9qzLqH6gwWU9AaoSrNXmKdVQHZseopSTTs91KMEFzVJb6R0fsJP0sVUz7df%2F1xR3WNcqvqfiQ3l6ApcIiLbmvFkVNG2Vq5BXZHp%2FbTs%2FW0IOE8nEvA2ns1Hr%2BcNGTYiPLEdItYtMkmrAcBSzzvGnw0sL8Xl5GBR1eFaaAnbGsFVJurAjfsascRBSGnuMllb63RM%2BcT5T%2B3Ht2awWmu11xeczhdd12e2Ud2BwF6cbpUQ8itGUQRaoDvlCKjAqUr1gKUWGpeEUHmtxHpwFoOnVJg%2BjNYR%2BbyOKUyAuQw%2FQyaTjAIdk1MD5PpOcJ87QnIIj8pOIs5CD%2BCXuwunvvYhCUv4grTeK5yOgnxdk7LZvh5oDDelO6OMgW3FeOUE5KN%2BzqjhCrA8MkhILsvdg%2FsIgUDviOMlstpMLNNHuMMVN5sQnAoSjWyJ2nPk4yzwYk%2FZ22hhXnh47%2B%2BZ410FGWKrLUMPPw1MgGOqUBe%2Bk%2BmImSG2LEfaBMOCgvQgfEcAdi7l%2FWPMR%2F%2F5F2TtdJGwADgdFvLPc42bz%2FibH6lXxjnQQwlT8p6lfooulUOQrQqv8qjcRGJYg%2FAZg%2Bnc3nGC%2B9rXrE9%2FZ2jI85KMhT7sP%2Ft9yLb38ULrAOoDkMXlew6J0t0jDKt7XsMvA6991gQ4KC3Rv%2FXWH3VJtqwj439X65tvCIqDboKnLErcMLW5kH3kSK&X-Amz-Signature=5c60a1ac1d7ed1c739a3ba6acc3cc38d3a3f4fa52cf2d54443ef169dff05817b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

