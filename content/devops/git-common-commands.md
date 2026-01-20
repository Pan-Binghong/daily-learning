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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INXBAZ2%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDOP3%2FB8BigbXBp8KlYBkHQVa7LRfXdnck6jg81FtIEgIhAMHFXYoKkHGwSofHzJI6VNfcjY%2B1ve7brTwSMHSqMLqvKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbYSKLkgynRgQYFi4q3ANy3%2BAsAxZ4SG21V3kRN6sligfE7W%2BmVXz%2Br4ivWsJI4spdoehbnHEaZqnfAcakCLJZnDLpc8kVN3NV0E2Z9xwYDwhFcWJsIzJMRAmQxed6nzTXmPVKvmO6hOiJoP%2FkrZ%2FF9nq1VbL1%2B9Cvuc3h5eE8F5BnPdkoM36v03tIJ6n5VnaFc6iw8Squai1T8pS8LLk33J14RwLVfwqKAF1SDz%2FmByU4J4K11PClqCV4CXIcVjdzRUm65qc94BwPbWbaJAq%2FT0mJlf%2B%2BT%2BFDity3AbzWjRhZz46%2FAlkQh9d9BvvaPRlU5FTAUiby%2BGrQfZZxDLvVQz2LioaKE60bPp2ApwLIMwvYlvmFpkUR2VM0KE0wDpH8yEBp8ytf%2F9PpokuRG1o1J3TdtVPzb5AwdcGJlQ52SuasbnDpGOx2ht16BOCdLfhxCbaklX%2B2rp628DyfMb%2BQ7KdFxYDGGdE95IlOqcKM%2B3CAQ%2FmkYt3Q1KWXk3VhnW26R5%2F8RJLxGGZdoloQX9nxdwJbrZsPgPJcm7%2BRWPa8cOQ%2FYOAMfLwKGh3zFzTam0N1kJRLzu%2FQ3mdxZnGi28FuZpJEtCHSm0qEZc9yndTLJHTXjsQDQLBiuTp7%2F7gHeBAXY7ES0Um1DJW8IDCY9brLBjqkAQ6lNiXJOz5%2ByDK3U1IAGQRYHwFfbBLP8kVnhNrVmXL8%2BGbhcSWgz3a1zhCRwXLhrYaroKet%2FxhS3FmZrB0Wb6%2Fsgp6LPzog8ybTDiHbtLt%2B14vEzrP21elKE1TyLj2hPvJVLTIIrYRDv3zOlpfqMCsV6FJN7HQkN4DruHWrHPT0C9%2FCw34wF3OonGuyAP7sfm6jCF%2FUaVZUw7yKVbGXiL1ONbpl&X-Amz-Signature=2320d3549c6f5f6dddab3392f65fa26c03c5d52fa51e08756cc1c5ffcd8d5268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

