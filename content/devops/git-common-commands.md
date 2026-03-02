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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUK27NCV%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6lMx2NPIHd4XgessX56%2BPXv0X3tN298lJ0HT%2BWWTXCAiBBglYeFMvxUf1SS8xxxZPXGFVEDtQW84%2B4%2FJfTyRIhLSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMGHcSZbqydOHFj05vKtwDwzRptym97IT46dnLWqrgGI%2BpA%2Bl1TIIOKDuDEqfoWpaimu9ftHrCpJYM%2BINtwEzos8f7LVeamTrzsM%2FYuRgY%2B7M3Tt7j6cLMdX38hLhwGBn6CToHyrawvC%2BOe6qxsDG9iCo4Gr2gmts6B6Man0%2FImoA8kVE5h5bsAEhw9L67Z5xEaRSdSiKaovMkC8%2FTeYw0fC%2BuwWieNp5uKDu8yNKnmlzhZY30Ju2%2BpdhgqLI69WU0AiH%2FqCla9mrCUMJE0navk5sYfxz%2BVuyz1WwlgSexs5a3FbZJ7D9knJdbyqMAojGHMNbETBc3Mo1qi7mhI0NUMaN%2FfnFinfUYDOE%2Bb5dvC8baGGc6zQTfn7UA5fLK86Qt0xvdWbgaFVVTLPhu%2BV3O2xrCADsHWj3qSPiOAeb2nRQ8JhNQGJUlL%2B2wDKbGj%2F5mvJ2TBOnU%2FdxgVak%2Bng31FI3CGiPcgtihjjGQcWmxXExINKwhwAqabM1XQVIWpDVygCGpe%2B%2B6TMch8oL1o%2BYqnHodBncFu8J3ifM3EokwPT7qSu%2F9G51DXzokuyYs15A6WhJKGQH4hkvNnIob5ccpFUX%2Bk%2Fzmfpbzn3lc3Hk%2FAgNO%2Fv5KM4IJAhdUxW1VlyPdGavP5vIN9NkoHf0w9fyTzQY6pgGjJgZ5PI8JqBUiz5ZRViTihHkeDUEl%2Bib5M%2FG4Ecs7Gv3LXqQf%2Ff4rjQPFIvrZkVLshF%2BUao0I1Yk8FKMmsKup52SBttMVa1mlzC3Dj%2Fb%2BtLJO4pLxv3vRNlsoe3hwsvZjxQbdjBJ4I8%2Bt0thwLKCUdJejS17nP7PFdpDyj3ABR9GkGktESDx1BtEfqh2OZbWe%2FAjC7K%2FTFGtSSwNMw7Jr2TMmDThW&X-Amz-Signature=42a11c897bca3ea262d619d81ff78989c7488d4ccc797197a8ed1af8a4d05372&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

