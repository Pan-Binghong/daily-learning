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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVMR3ZFR%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLsvNgMdyaieYzYsVApTvl%2FG%2FdZgt6ro8En8A9lP%2Fp1AiB42lLlO1dsM7R4TrmRwfgqTmfSgx%2BVICEAb56KDPsvSyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcE5KtQbesGEsbw7bKtwDZ3XAtHUOg9yoILiqEdljTD7JycFLDG5XOwUMVSK1sB%2FN74a0%2Bwz%2FXYvCrly0zvzBsfyYRlLx%2B4G%2BQMtjtN79HZBJLk4laL9AIB12o6ADJEnKHhVROb0lExglLQ8Aiyabfg4OODwv8tbchMNEsxUOf1Tl0taRO2Ih5HZQ2XvtSI1jpVuMtEQZCjGldJSa6D1rcy6iM7eZkWLb2gyGfEa5Du0CmB8Pv9AsuJ8mbvGlfQ4uAxAYOc1CfVIG6bnAxZ179GDZIEFsfcMjAq0DWbHcnOfpQGpIkwU6y%2FLf9HuXUGflxpv61o8XBJGUpYoAjVWogYOyWr3Qk2s3enLL7YwPhOLeErcTC50%2BsNzFL6jkgqkCfSIjFaXKC1rUGaF0ewWSi9M50lsSKXawv%2FxU4j4YT%2BlmdCgH81itwEIIGuCZNHLKN7gTiY2OCBlhDiVEq6k7FsKb7Gbd0A2inPdjxCWl%2BC0bEvgtsraD%2FnKpb1upMPBJUrOC1aNs0C6a%2BJ8IkWVVgPhx3XK%2FNT9XCL%2FjeEFmrjVtxiT1iDsiaCaIjOYcZKVWWUA57v4WQKwZIxoSeucXxcey8jroyOOhJi9UptfmY%2FPlNjY99z5VIGYA2dYq0o%2BuSOG34nhrQBnke44wxKKsyAY6pgEplaAe1808nwurQu9R5X00MOvrTc%2FXeLvvyiwiocuRuXcRobHeKg5hHaRAU2BUSRksnkHMstWK5ZlzmsK2D2NdYvVCQbUFotjT6J8MFs7sPIQlUQ7pkIrKzxYNArgjvT9gJ7JR6CTz3z7n7iQ64lyOCE6p1egQH6vaO3EfHdaQH731L60L9SI31TjHXJlJx4kgdLcVJR%2BeDAONhIeG4Nw1r9nIwLAw&X-Amz-Signature=9339bd94ca67985029b5767fe1dfd5be767d4d1ca330484753b1a790f5dae6e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

