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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVCQTZUA%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2Bn7PTptImF3keymRvRL3CK%2F2mBqNB3JExzlMDV93d4gIhAKPeT95s4xtJUGCHMm4NdJPmEGuHdogiOGmuke%2FNKUUXKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxkBKd6xYWnqMjiLMgq3AMTCOwewBEpsAwqFDQUEP36O5RHKJS4VbQRNKUjjsbDmAbyMAMW3KxV%2B6CFWNFIfp6OsFq%2BJY8MG9rX7OKlfQpmSBriKzNXvbhepqhL5V2TxxhgD%2BiL8ToCAnjM%2FF3h7StRWAwEEggZsLR4da7rCwWchK3yH4U9L3ieyYVma12o3uCFu6qnPvEoocncyebWBnkgppnbAAiFZgdxRSnLW3dDYDQi0gXDCFlT2g0gT2w1uxEYsoS%2FmbkgbJzYsDlayLothilwNzKSC4NiWpo0ugIqQdsolRMMW79cszSDBBaKCXdcXuJ9XOPVziTZ54Gg9lF%2FyuesHNiCVmhhEiPG%2F3lLbKmrWeloE0jIaTVD4Zj2x1rHihWPOMronkl10ajcsiPQkF1HEjULyI8emh1fiYop0bcMiKWpXhMDEuSkRkhTey280WeaNlysKTqI2dBNU9vDX9l7cnrY4ixuLwrmvvYJWpNjhSpZxosmRLpq%2BZO50H%2F62iCnwaE9r3l5IpmJ2dQ2lV9JFHduBHZzoSyrkbnK0vqGUOX0egSemSsaio2gT5T9u%2FqtB4Km75vm9NS%2Bw14aeA9bBVKcyTr5P9sog4b16LjJF59UeVAY4PDje%2FEAJDvhxBNDr04mg3VXozCy3%2FbOBjqkAVz3qrIxoVAesJgtpmKk69RfB%2BvXXpPFTli4Y6oi8A%2BBsxomJ%2BwhkMyfH4K1S6a1xc15HUjMlnTi%2B3wuW6socqClDKlI3yXeNwcJhsDGQWjRyWWN5lqYQXy%2BiRbHboqS1WwXok87Zh0l1rlq5%2BPD6rcobI8jSaymeXrRZu9v8FqYVQ%2F3fLX%2F8WYXA%2F0LuaFJGV1eZk9mdideDMjeOW8oB%2Fd1FcoX&X-Amz-Signature=f64a29f62460cddbe54b1004210c7cf643b1bb915806bde76e874b5bbd5f1b43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

