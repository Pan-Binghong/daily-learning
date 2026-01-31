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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RFZGRYS%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfZfEZKKc%2FnF4%2BZq3hgef4o6NS2JMLSzoau%2FixHKCL3wIhAOJRIJ%2BesKMvEImY1fm8IUDEunhIBVhWXA3x5Df0KVoRKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxk9i2WIupEYb4Ydhwq3APEKPqasBUC3Rk%2Bsed3lH3FsGac4Yx3PSy4vlIcbKxrn4P2r4z%2BcY2QnZKv%2B0XMoRgjtgQn8gO%2F9GA2KuKo9eydk9fw6%2FY9oi3ra7QERhXMJCjX9uyu9uD6EBwXfKoiIN%2BLHbyLUBX4Cs7ONaPvVEuyMnYS6lS2OtXpN0daRVHgUuDCY5gYCQELjzH3OipqZX9ZD6nl1Tpb%2B33Nsd%2FsURuKtP1uIPVLDRKBy%2B7tCT%2FoC1wkWhUDPZEeaijv6RdSvEaxXZUy%2FAuhZInqaeJp19rPUdZsp0hg%2FYy9wluR%2FlnA2AznRLWXuI4IySW6b0vUjQmc88BLGQsBp0XFEKbkVJtfJFmUAbb6kzqByQXVlhsr12EpejJvkp2ZsZikgWp23zFnfRChMVLNf0y9l2LLHHr0ZGKlocXWq8jKAXP%2Btcnld5xaeXFUzgxC9m9TwxV5oNsGlkvDHkNeC7bBOZqyhyop5%2B06OCOrFoiJ1IzkpucKkDvde0lG7RwnJQAPxf%2B8pcMc8tneEN9JPiBmrU888uIRhI8OwP9pT2NMHQ3VtW5ERQQTJB%2FGsn6c67UbW9fSjm2ISjQtljzQ0ZwD88dbwupJNibg6bzxpiF3LzGTRX2pdW9mWASW0Iezy90HVzDazPXLBjqkAVrllyMZOL%2FHrKtU3O%2FMYQPfMuFyYbhdd6aZ6miyeeKJF0W%2F%2FNH%2BxOzFKurBxo5iMRWWkJrsT51eY20ZlU97q5AZifTSvLXowOLZhDICmguy68wDYxGkjRRvSL3ATMjP2u2o%2B%2FTHrAiaojCYZ6WE4fycAYB4v6xmcOr9eXl6uJsQ2lYEtD1jY0oxxHeN7A2qR0doVmTesxCV4H06cHPGxtgUsvwI&X-Amz-Signature=3f79dcbb648592150f0691849ff3d18c46a65a3a7d157707a2378f06a992f991&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

