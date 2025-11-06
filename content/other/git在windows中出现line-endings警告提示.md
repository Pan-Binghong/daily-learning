---
title: Git在Windows中出现Line Endings警告提示
date: '2025-10-29T03:19:00.000Z'
lastmod: '2025-10-29T03:22:00.000Z'
draft: false
tags:
- Git
categories:
- 其他
---

 这个警告的原因是 Git 在 Windows 系统上会自动将 LF（Linux/Mac 风格的换行符）转换为 CRLF（Windows 风格的换行符）。

```sql
# 禁用自动转换
git config --global core.autocrlf false

# 删除已暂存的文件
git rm -r --cached .

# 重新添加所有文件
git add .
```

