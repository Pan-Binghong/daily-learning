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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWJL7SFS%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDiyr00K0Rxuju9e2tUBAR%2Bl3I%2F0n2ZyizZK3wumm8k%2BgIhAMOba5XsDhJ5MJQB7yIS26MPc80E%2F2Ho0x1T%2BUCInbmzKv8DCDIQABoMNjM3NDIzMTgzODA1IgyYt%2FJtGp71Bg54cOkq3AOuDGFTBR98TYnB0Ik7W33g5ezq25Rk3RYA6WAAhlmvLSUznOxbcOxlTzQcZDt4VVDmcMT6q8z79j58K5EBEhdP8NYE4HwnYeH38tDQvNI%2FkBSeqk46stxRw5bwUcABESnM5m5T51323kwuDEULoPfzmRj4NR2CEs8Z2Nm3gSHBrY5dunvLF%2B2i0ef%2BLSSmYszPLnEMMtKvk9ySoU58q9gPgO3w3WhqWmDrG7vcgJkf5rFv1jGRaedUwdzD89G%2FN%2BTLfI7BvFpL4%2BZMEJktt7h3NR8XxwgtqFDOa%2BImgjbykBMv%2FlKczPxYrXVvQBsJbzbh0hY1h%2BP58mAf57fi6%2FMAszrIBOKF%2BmibGbbb5FjOxhhoVLaR6mrmxlcdzxvD5X1zO24MxeM1qJHOIS%2BvS%2BLeprz%2FI4yq5hjyTzIbGSRlnWLCmAcDPSfHDwi9Z9t5eYthAXP9UhxdaK04Erf%2BtMSiuTZQ4KqZ6zHYkCkSFMYm2fPO11iO9pSnMKGdjko5njSQi%2Br%2BRspK8%2B4fo%2FGlq7ZMxiFlWxtOKj%2BsKzumNfdxhWAAb00f7jH8IJNfrav8XknALm8KIiGMZyzVNdQZ15bTgqjoD%2BOd78rs1GIbmXw9NQjjota6PiMxDr9KwjDHoLLKBjqkAYeAuYEdjuQzFXhGmDLc00guGPVK%2FwrfUcL6XR93337pUv8c9WFvS%2FICzzeS1zR%2FbKcBQn5F%2Boi9PIIF%2BQtcqY7iImYVf8cJlUx8E2ebKV7lX5HTxTb5Icse9HmQrkunG6vRc%2FSEBT6D2GfzSQajN0qU1iBetmhkXBJzbkUq06HioAHKx5vIGHzivHTNCnSBRqk7H9KTxAN1uZjCjebVxqiS3quK&X-Amz-Signature=dd8cbd3a9fac6ed8ef7d8f199657b68417aa5b1423d8c50b7d001acf1d1a66e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

