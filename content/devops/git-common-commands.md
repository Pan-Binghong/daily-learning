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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGB7LAZ6%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIE3Csz1I%2FraMlyHm9Ea%2FdtienEvGFb94cW%2FsFnxJrGVfAiAnHT%2F50GUzLcv0iRasSOyehkkiagyBPW3NKqOXgNC47yqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4EDen9y8IydOS3y6KtwD7gLP11FeFDBgZ2lc07ka1J%2FBWgqmSoLigkerdP5DvIVtqxsJqQVRze8oQvAG7lyvyCkAauRFn%2F6AgFbsaLk0oa%2BPS5g8wXnw1NGqZng7i2XYsViwOoxfIfk900r0ksPSQ1%2BgZg9BFTr4yjNOElLMPmqg3CmQcmTDNrsgC4xjKd2AGSLiSf05xeLj%2Bm5W961%2F%2FvDgu5zOR3brTjAuwBsKlFRmL3F3CUTeR6DfQz2yYK4ypr502m488UTE%2FKDYZbhd8ykvcs5%2B4oqgJ2Bay%2BT234kL4PN39c1O%2F3ciaYmQdhCY3vjZjBAUMXyQwq2Y%2BGamidI8meb3VHMefSbqjgEJehFs5plt1cn%2B2MajIvjJ%2B9zUl5EgkFz8PACFanCs%2BnbikPddjbfG4aq%2BGr%2Fh%2BsxWGZAaxHszoq93iysIiWcToz8X3Jjxukxlx01dp00XEqsKZjI%2FZkaDrlb58gO7qMpHrJ1lByPqA1AfKR9ovl%2BEJrdt2a6urTyKfRAw9H7HyaMxeTzIfr2jcbK2uofmx0ic0vvNXFgz7rj1kIjOBAxRMlzNjgRJT3dIYqWiX%2F%2FmB1QsBPTJlC0kZwgabPPitcjifLtcTC9dvFuw%2FA6Eo6b5TnEtfA4SOCJS0a3REVowlt6QzwY6pgGwj7ZzVYlDuBh0KDFQ%2FcqHnk8MVZOqbE%2FpyyNVWNjfFI7MlrC41KHevBKyXVDDP9oom7fn%2BILGLe4VIPhvYkYw2varNtSp%2B1KBeSkJw7HQn9KpNkKbiu1xrG9hrg1PgtuSTklABj4VtARJoAHyN7tffGeqjGlNezKUppEi68NigetTTP5%2Fs%2BooJajrI%2BoBLuG1aWH2FlWma186eCv7zxR%2BoRU4kuiC&X-Amz-Signature=81f68a029e8d4dbfde2f6febbbb96892e8d1f3367250387135b7245d091315ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

