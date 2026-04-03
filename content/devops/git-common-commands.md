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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGCOZC3U%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAQVMJ0DBq4vAhbGhCvbo2eLaXyyrouEyDx%2FhIBWIDYQIhAJY6b6smVqdI5tV7jk4C%2B6x4BWhdA7ioMh%2FcrTqaxA1lKv8DCH8QABoMNjM3NDIzMTgzODA1IgxRDCEs7zQCqrbQMhsq3AOeUe2DoH5P%2BDpCX%2F3WSiCeCi9VU1Iymact4K68LwHtin6G%2BhqAX1ViRE1ro3BafpPYLqHt7qMs1sVGzq9oNv0UE36OWqCuzW%2Fu5Q6%2Bu8J1nLNreK5DIoKNk%2BkHxVeFYygr1%2B2gyF12tCKSLWgoDZrznDV9X43%2Fk3sGSX4TAc0JqdCSOpEthSuF18s4q9v4GS8OfY9qW5z4B2YN97hOoAdMfvAz5eCBKREByu%2BlR9UR%2B9v2runUI8VzGxVxAXC7q4iMvXHHEQddap5AovtqimuCGoYvsm%2B09NRGI1gyYUcNaxq6%2F7nIn%2BQ6jOuxeoODpdbUiTqXeyAGOvio007xY8I%2Bvbvt%2BByfFLaqIlVAOl9ax829GhXQDef3YQezy0wteXtT%2FOG4IY2Qa7IophseN%2FvnQRzxn9BahemeMDFONlCGbTQM71ffaxvCaDyMf%2FL%2FY2EPXYmm8AemMJPCbiB%2BKmhRaBN%2FgMbHiHjPOXlXACuNbdhle7a1fGTMj7ymyIJPkd0uHCmA22iWh5E7yiAjXmgMrL6dYWC8RDuzr0Z%2FlFrFn38rbelR5CYKnAAHO%2BDWXIhp%2FqiNgOELok9sjJV4mox0cLSh2YXznl9lANOp3c9scKG3HeUtS%2FrF%2F0dwijDhrr3OBjqkAaiyLzZptpaXnokQi8PTCGA4Y%2FCC7Lt9ek9VfJbhQEmIaYkVteVZaSxzHRY4ig%2FQCrfMKPzZ9pg2oQil95VqiIlkivYgtl6c2fXmUjGdff2qu9VY2lFV8Xmmx3bDRORgIBPTjtmHBgArXeDmtLe7TCmeKZQKtNupZw25nTeZPRyXbXGX%2F52Ls8xXfIwHhfwzwFYaFuP4IoiD038vzQKqBbRbB%2FX6&X-Amz-Signature=ada391dddac7bbabb2215f8b39f0905a445b420205cfd6528e03f218b92ff081&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

