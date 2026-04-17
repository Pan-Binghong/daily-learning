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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM3DKIN7%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDc0JsxEgFbGwha9oqTwsFR0SFqDbSpgtlpsp9LlJskFgIgCXnPEmfnNoAePRpbYc3Xs7LoKjTtukf4XcjY%2B1fdgywqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDLaJTiLYHRkhsAoAyrcA%2FL1YTXw25DTPeJi%2F8tquPQiklIBQiOq%2FgUj7DmMB%2B17F1Pz32Yx9iSJX8vxeJFgAD52wZ6Dh3n67HVCPt6Mh46Cv5qcaAHG%2FeTDphIrDW7SKoWTnzUBnN5Ey9qa3Uc1Weixcnv4%2BcZva2IJPYnZK4UfCmg1IKX7uvFx4g7SQ8MeXD3TTtcAsEVdkzVrpgVr1AF5bl3Lk%2FckxitbGUJ9jXeCmYMk3AyiDnw4wziBuSGFHa%2BONxM2VXXlqb3ylnWavs5ruJZnD7nI4Vs40l3EBS2s8bV3%2Bj%2B2waeHiNTlVPFJM7YHbnWr0BZmr%2FcOP%2BEUOlhQWrcKyT1s14hbU62GA%2B99FqzTetBxxS3C71dA0qXukcdCA6JcUbnV%2F8E%2B5tf%2BF%2F6xn%2BtyLqvCh%2FEJVcoDtR77rpUyUwtSa0BEhHp66cTAflHQxdlxqd73rxWh243kmGOVPq5OWyRltQLqzzhZrX8TYixWoRh%2FPPUA6JqACoaA60yRkDk6XordDtn49soz7vHgyFM9rUkDmlKhtMquAeoxxORoDccgE0%2BNdaj%2FNjEv8SxvVi5CUeFzRBQQD4w4Dw8iHRM4ZcDIP22HNElhzEJcaTtN%2FFo9sFVNRiCgt4JDiLWl7z3FHK5GsmoaMOO7hs8GOqUBdtbOIPADvbPWu44QHWLHqynIXIB8qMA0Fcq6cgfPDbAUf%2F6Hxv3sugI9ikvEwGF5Ox%2ByVhrIUMBKi6Njw%2BzwPpoWDRNSepARiddDoTWbllEV7J2ct8wBMpm%2B%2F657vfbCG9awsHjwI32DEJP6RPsHPLiWJtXJI3LqZQ1V9K5DHPtZ%2BzDsr94Y%2F62thG81ZEY2uTdb7KORNrNj4p%2FUG28gILxF%2BRLK&X-Amz-Signature=41062f27762e67251c0dc95662d8172511e4335e305a6dae87ba402083a0b5e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

