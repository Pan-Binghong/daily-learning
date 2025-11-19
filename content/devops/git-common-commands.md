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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S2NCJVY%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDwJFr38fIc1Oyu%2FYrE1Cn3y9XZEeUe2SSfC%2Ftf6%2F7MBwIhAKYJ5Qr%2FAKcv9BM9O%2BLcS6i0h20uP9vlb%2BfEel0Kok91KogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxNMS3NGWWSRWEGtD8q3AP9G7Rl%2FnwpqYVtpgoRz2T44bf73P2DL5r06eCgWMl%2FQANErM6UGELyQ70s5r5uPJQwANnGVmvv%2BZMb06BIZ593j1TuMoV08rrT2dzKripQGnG8jiJ%2BP5%2FMt1s7Q6r0ID8mlLK2WQs7DO1Pf4xj0szctNGS1CKvVDshZSEi3baB7uhjQGcD5ftIp%2B97jVpLkTufvzoKCglxzurkat3nTECRbG4f%2BVbZfpJldT1zsCxWpkbHjTWIpVDq8Kr6CuYft0YpnXN%2BhtMApo6yf4Woph89xUjsoTQiKt%2FWxKjvDn%2B8tC9%2B98OVojpLGGaa6mpu3JU9HML41LnscgcROko6MBBr7XqMTcQvgTkbWaV68gS9fG4woT9qOKBPxZhlT8TY4nAQt55zr59szvf4b31mMDrnn3J07f5HZSyszTzelAFs74PdPgjLD5y1C4FDYWkY%2FsxvC1Kr8LTPdpEFY6ziDh6vNYVAZiGGXYglRG1UTypEh%2BgXV4gzHDUmkTqQrOxp%2B%2Fg2MwedcQtShXSziuoJpggxXjdmCgiR1hnH9p%2BNG5JONLwHkNXKhkJGzElweCF7aJkXQMajXNYSJ59eRk7MEsiiYuzedaignYRAoACEg43eWFewGoF8bJDGriUW6DCfyvTIBjqkARdUAu3nmYwbQ3v7TPzkOQxiixxOsBAPAAE7N13QfAbyozzuZ3T%2BBNx3tKLsdOKDoptIzAt8HRXGTzc1Muo0hRgNsfWraL0j8TTaoib1xTIx5swjqpGfWx9KQDAD9wJret%2FfEX10WGsfn%2B2SCi6QQALrbyXoIWj1T%2BbAc%2FS3ud5ywjXn82C8n3bDRRKI%2F2fkrRm%2B%2FWBz5ChcUvYWVv0OmyVruBKX&X-Amz-Signature=2973726fbb843036b2a1a89f4308bc90bd262a2495e5c625887e11d329ddc32c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

