---
title: Git Common commands
date: '2024-11-20T01:22:00.000Z'
lastmod: '2025-04-03T07:41:00.000Z'
draft: false
标签:
- Git
categories:
- DevOps
---

> 💡 Git代码管理规范说明，以及常用命令。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDBNJMOZ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkk1CO9IRLwtJ6Awk10zSIofoJKk57MBXY4w4L8FVwQAIgSKyiernJQ3bVwawuec79fnPk3mCes%2B4%2F0969Tuq195gqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3mYQyHFLLkTxmn2SrcA6vJG4IXBmjYbwbHKHCYzApCAyq4y2%2FrKc%2Be45q4sChEJ9usSBBE64ydraFtIySqVw7UtWo5twFYKrPOERb6iN0xEXo9l947dax5wDnfXcDDgFaCwFa6YdVyoRKRd%2FibaeOBrTpqJHo0%2FzwGEckm%2Ft8mGpr19JRyvolUELvwlmu399Qu9wgbrNnvAWnjybORD%2FJao6knxM3qwrDFiP81w%2BiyjgNQ90GKSxfXN%2B%2FcgeXXEh%2BcqQQv1dCm%2FWxB8YPjiLNVzCm%2F18HNAV8PBrPrCZvJpDzd5EnyL6fcR3wymk403GhqTMCJYbIgUXV68AHmSPqLUlRLTdEINSRWbF9J3j40bTfmwpNPmhVaCikgaqraNRikWZb2BgBeolK21epxHOrDm%2Bjph29YToYibd5clcWqNUUw6WySKAHsukWUoHcm7OgZLHktjlPErY5FeXqTBA4cKpYfDju94wZWQJR60rQOeV8fvuHE%2F2TPk9JmWLoKL%2BCS4DsDhwgFENz%2FsN%2BM%2FF1Ee1EBC%2FtHEE5w%2BzeFYMtLebop%2FlaGRPd3roo6IPdDGBdeLyigSHkGuYwx3aIRmfCQ8jaCLactglRH7W3i7%2F29vuO1wa%2BqhxkaAqZ03ZR%2B3Xst%2Bv6njecTtfCJMLmirMgGOqUBSsHXkeQ6xn5HteOths8Wg8ia%2BdCwHhH6AzGaJ07mI05JV8hgYlDmxSXt31oa8l8syAvijq8oyuOMhMk1aUEnfLLmVbyNaAKlFYGCYXo58vFAm4lCfrufSuaBaCCgZHvOE0VbCJRsmsO4wkHLX81C%2F4u2TvkwFnvumY6e9wsYZnhK6c4LOsfDjTrHlPCB1S%2FMMNEXbzjqnCRx%2F986qJp4R2KH5FeM&X-Amz-Signature=e379b443805fec5bdc454861f112cabfa5108d5f7db722878473df17ed0cc0f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

