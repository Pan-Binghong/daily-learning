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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634XZRDJG%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBOz%2FbrhL%2Bk0PbXilmL7R1RUSHkd%2FNnYxAoSfNiMn2kCAiAFF5iSqfo5X7iIL0LZxYG8QxfWn%2Bj5KDOuut5XKkCaPir%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMv5NaycXh%2F32mJLiqKtwDdLz7LFwCCeWVsS4PvCRLtwBBxXZbst%2B9lpoU%2FI1bylWKfZ5j4VFd%2B%2Bh22hneDZ0p7h2YcmDpAz4GQTiuYdqoQF%2Fv7XPogFQNfOXZEmAKlBpLD887jiKq2gt9%2BqlTFhLqBPIiHKU%2BK4%2FubnEw81waa9OQWm3QEx%2BqyWRCKRpIxejMDePjcPr3lIqnwkcC%2FfHNL8JK%2Bc8PQZ1jAn6xvejRPLNcw0OcOlx1K3IR0%2BbkFRugiu9DEuTEnBlDFYkxaF5yXnQIk%2FpnFKCfo3tMKoCBGUEzlq4s8PrC2yOjDJy454CbDTJdiPtMJ10HF0HdszELzTQO6GIO5X7rc0NJ2rlEugRUOeCl3s3KG6rd%2FspCwdmbUkzjcVElsTqeO9R8Q2Zeh49FdLfsagCL4O73wZDTNXXCg6lIKZPAWN62TfRJvOemG4e%2F5kTDyKXFFPU8uie4PMozMNqRLXvLw5bFi2cltUiR4rozC6ixqlW5J3xt2f1hvPw7a6NMuhfgRhaQGls17rI4lWkt%2FEykRuqlZtclJGY2jdCM0Tb6E79iYOewirfcbXzHD1N4DgBVhGh1tUE7SN4tBpGecKGaDV7JplcfpDOJtjAh0SJFYe8DPXIR5V4XSWSPkSu5LqAGpegwz82OzQY6pgE0Ih4yWopvET846SUIeaHqWm2gTE6VyDA0iz%2BV9M%2Bg3LNSXRw1%2Fq4kYCgnRJiw7e%2BJbtvvnY%2F1E3s9WlpPyPdZG9C8G%2FCamEJwmBUInpvTQIl2RKxNzYdzGs4%2BNtJ%2Bhkdn0e5MYS8kCypyOdKDzQMMXggGecGXUWBovBDMZYvSuevMgkewLFHe0s6AfbiZN6LxOpQipMQaVLAoKWjNUauDojCOPA82&X-Amz-Signature=4e217f82241f50caa7f3d4ffcb83cafc790a66dcf62c9446dc78102669df153b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

