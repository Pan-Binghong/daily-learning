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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBC6NLLL%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDtp1IGnuGNM7kOOYeP50QExmRoYBNMQ4kC7Toz9wueIwIhAPp3wn0sBRiZJ0JSXtWY3j%2FnonWsm2NxA6V%2BJVuvdjOSKv8DCDkQABoMNjM3NDIzMTgzODA1IgwDEoWfPSuaKczvtuIq3ANdeAS6aNrlQjXXVC7f8wDGSQL1Bq9%2BSgQnIuaOVRXptQzoyBnIWfutdRJmDm1mOsDjU7Ab6s8lfi1lQNWThj6zjX3e1jH83tK2B7pNFC4jRds%2FA5n%2FlVPo%2BLL4VW6XmpCSDLMmTLMPMksdJe6lVnvIiD29S986E3hedv33NDtNT0rImHkhgae48U33pEPdAiZzClLEy%2Bye7%2FovEzYI%2B5KchfVpbmsJFrjl7y%2Flbrxveuf8pqOToFybMat2hTvax4VUy%2FQ%2BHSAeDjWSzaXwJ%2B%2BxRiCZDpPBKvqebnLyWSH8NPQ2LasDpxhkxRH0sBk8Ou8%2Bi7RGmYMtdJ33qrInQuBIy7poZqtfCkFgNT4EXlDqQ5hxnyS3xi4DyXYd%2B2wQqtiG%2BKzPkg2AsTzj0mwLWzFnWiEPH7tiDyh7M7b96KVYp599np8xjb7rC0tXkHAg5JqRqPoIP4%2BDT6XbQQUVbwPgotzK73vVlKH7xNXEA%2FoPoMsV4WIP7uNnPnoPqruS80WdgF5vxej8GjR2u6VKqPdcOGrfjdn7w5FOomEIdIO%2BcfMrrYqwjVXIsceM5U19D0Rq4nYNlqzlg5KMmf3Pnw1hVy5Xit0y0FdMDzJnlI9ch7PpDXWZXndXEfkdczC57%2BvKBjqkAa7SDJmYZsw%2BBqR%2BcGVLZJf4o%2BMdxkLJmvqfeqCZp4AUtWYODe8HJ5RPP6ough111y9usY%2FBa%2BnfVoaepiySRJy84frDEVXFOCOHG7geJJUt3AApg3g7n3FugdROkiE0t91IHYG8QG%2BWSnBJVbflFWn7IbD3Ktv3GVlr%2BoQHJMdMY%2BAjBXH3pRsxjKPUnvUO6akk1VW0dHwgUy0Q%2B6m3bm4Qqkl6&X-Amz-Signature=8e51a5c677c9b837d5b593b1a17787d106887b5d790eb016f57ad9fd774103b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

