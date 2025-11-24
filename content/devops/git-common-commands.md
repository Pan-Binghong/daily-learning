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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RCUPFH7%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbnbiOv%2FSP3cJzwTjqd1DAdSdACCcOnSxm0dO1lbeejAIgTG%2FXVTkG3UL%2B0Da7mcobj3LIHhMF%2BhJcIZRgOXOg1UQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDB6lh7wpYmDhij4KQCrcA24RzO9gk%2BhFx05OX4ZmVaroEvOEBi5%2BOpLRwtKePuAiBoxwWrdCFED9gDFk7xGS1SIlEO4%2BqGA1iwIP%2BTPEVsejAsOV4jKDSfPnt%2FAN%2BM4E7JycvMoa8F4mGEJiC7%2Bg57TIUTBplxctLKvAGPu3esdXnA9cRdfCOWyw8BUXIDZNAC2oj1cNqbQS9M2HlLVDd0c8Y1%2B1iGKhpxCfZ14b2nAguTHWA%2Fv%2FiQDxXy4J%2F5Jb3961JCpZObCZzbJmvke1o9qxN7eTh2ADapTSx64midGIRr4QG20xVhNGdtof5hAp8z25yp69uWZNX0wsDM6ifmOzAe7hnc4t27Un9j6HuBjHcEqAkDXPy5%2FgDAzqKj%2FhumgDOdVFeAVSQEI%2F73hbcalUAzY2jNQXBMd49r21YVNF3EueyD%2BSEnP8AT3PMuuDIk6qG05KbmQR7H%2BiQaWd7%2BdbCmPviHxrU6YIpCjWz75KP7CwI5XfOABYFjKQP8T%2Fadp6NEOGNnCOf35bDvAA%2FDC4c6NHdeRW%2Fd1twIVJRHbE%2FbSFOJ74KxoANSvLAtzm5suUIbD7InqEzIXdfAaUOuieRVCP57%2FwkDlwwN3eGgVJQtSx4yLRwm5YX6Rk4BmA5jRp3TBMm%2FeHazfdMMTdjskGOqUBd%2FDJ031CoT5y3oToFPli4ycsXXmKJ2oi%2FrKXTDmK%2FDd5FH0TgY6EBEz5mnrcppJ60aM0giOYkXfB7NISUUyYWd%2Bl%2BEhXV1J40IhzKFG87AW6FWZV57uVegcu97X5f2IMijAFGbitXinNEzINJkg6gVJRH8ZPPLp4bDiFxg1NSoRcgN8Nn4fyhpfpUG12TnUuJDlaqv%2FBO3vgp1MmHHr7wVi%2Bqumv&X-Amz-Signature=17864bedf4a49de1a0793f76d41e431a1250475d8497e367695c93d8d42ab3a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

