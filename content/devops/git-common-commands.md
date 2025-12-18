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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPGQ46RU%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZLfYpSCQQWUaUkNYoxiTTktYflUShfgum95fA43AxFQIhANDzybaTT2GN2SZZ9t36mXVp9qpWvMj4ATgDifKVMBVtKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpG67QgVpw%2Fb%2FXxxcq3AN1yGCAF50XjLEQdKdmILb0leY2fLiFDw7V8n63dJ%2FyhXcnz8T7q7f47xz3q3haQHJbch%2BhLPIrJU3cPYOzOEmvKz1pS6RtBhipDslLENeOxCF9bv65usZUc1HkUrHHctaOOGftYkff7%2Fc3TgWt6H7POPG9jcDGZc3Fyk1w2v8b3g8p0MXQzjf8ecsfCGn1LKkzFglyS8dBhF9YfbuNKJy%2BMBPfkpb5OBJt5FhA2%2B%2FOoiXPVKT4ljCFqrUiS2EvgXEEUW2mJtE8PRx5TJDevNCMcPFLrMAJJ5%2BSY8hCeQviCvym%2B0GN22RQzVTiRNCs%2BuHC5tXM8utZ6R7ytUtFzdw3m8jjmpWyvGwZJ95jEhGS51p9JVLZcZZI8GvF2R7AsXspzYhzW%2BqmTjeT8KxjRTM4dNMBxJyNx6A9K3GfoZqnmXFUvC4pNSymOxzwQYXulgQjA9LhGVx8WhXTiSV%2FGmE%2F6Gw5tX079lGWMQ1MPg1gTU9IUCxj3bzgtrdOK5UUFVecx7iECD5Mr595QuatiL6F4xlKogT%2BFSCGZkvGbgAG4x5xD9HoiN6Gr2yjuLIO%2FZSWpPtl1gPz%2B37ek0DU%2BlPouW3fjPQk36qvLG5oNdPAXgVaX%2Fq5ESactkQEkDCTyo3KBjqkAfGOSm1fjuj8RxEajymPLSh55SN7ufvsK6%2FwH0Ie86Ow3V%2B1Je5arZ3r2UStwG3Cvv9JHdCTmIoNOEwQ71%2ByhNnkoU5TEnab3%2F82ACKvVQE0OmxOoPsI%2BZmt%2Bj95tsaxj%2BnZdvipSHIIB6%2BCEQNEiM7J%2FNR%2FRuK0aD9mE1%2Fa6pM9Rb8t0lH%2BuZwAjhpFgzqqmCgJ%2Fy1foz0CrI7lzEAbDDLTWDTY&X-Amz-Signature=f406309903a5f7dbea8f311cc45c9232dbd1bd105270fa385d52beac9fa13254&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

