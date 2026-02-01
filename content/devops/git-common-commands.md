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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627R5F7ZB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FENXwDFZrrQUJQKG1rIkt8T7Py77bg8epVfVdtEp2EgIhAK9WZhsx4TsjtrN1v2iBSEr3V5Sg3VCO9URTwxEUXLmtKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzeuBlz8C8ZN8EnLYcq3ANDuyPVG76644uWAKz5f8GoPvh9MQriWKDrhNAGz9kX8OozDs3VJyXoEsGLhcMaB%2FbTsoNDjBsvv1vun%2BgKKf%2B5oyPTfD5Zbiol7iZj4UGB%2FzvZSzWcxbdi0uG1ZjpUn5OKGveR9AmQeyYa0o17izob1Z20B8PAHJtNHI4aTtl8aIt%2FlIDfF%2FCk8x2GWiFKa17w6aCExG3GkZaCNaiQRO73pgipiJh%2BvdAxSWbT4XaYtIF%2FQz2iiVc3DOIKCNDJQTNKSDIYVUUNH4f3fK14Jx001Rv5kv6EB4yT0tknqbj0qCH%2FVNJohBDqscNtH5tSJfJagyrynOgeGyJWbbupMZKMN6QjxQ7HH2roBZ974GHfWNtguYkTXGf8tZv931gJ1G9zKg5r4tZ0D%2FJTtS6mY5stxL7GLvcO1WOCDlkCvbD9JqnIEg46By%2BWzGbhRtLwT0XZoBUge6idOTGYoSVLwTS5lDwAu%2FensqjIq6jdGeJ%2B8aL1Mfui9CVlzhdp7pSkT0BVfnk5STFsNy6UIRy0m%2Fq5bxCeqIxp7S%2BJZHIFqHYdOzOPJl6OHwX%2FK3ibXYb9ykESX1h2Ny125LrKGxkp4aUBjfn7%2BhaOu1qmj4iNguNsMK9hHoMmVrdStGDkfzCzkvvLBjqkAUuCCyZxXDcAn94pZoG9VPzoKn6xMdTYrgSB2a%2FkXP73byJ0ORbAzb0Bqo%2BajpTHW9ej0pn8uxHOMFpfmWZPHK%2F1iyBS1T55X289ATqDJiJRpQBjRVjO22Y6mxX0H4WZoYCVDFqmGU7d1AvhSmAJmtIuHqBg0%2BrqUSY8UU4HaxLpHAY9uoY9usFJdygCwM08Jvyi17gCoXVwuWUZ0Znqy5IcvCVX&X-Amz-Signature=9e388f767bf9d1cd188aefc5028d31d9964a2363b10b4f4fe7b087c83d1ed5a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

