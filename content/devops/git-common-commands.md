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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLJAZTQR%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBjTTGYR73eWqptj9mjnGE08ddzRVsRGWgYI7zfPhEQAAiEA3yXgLF199CgGl9CXFke%2BK%2BAFaaVLF2epqqhAkj%2FoGP8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDPgj2keHeooBB3kHYyrcA09%2BKu0D%2FbMq1xqbfGzMHuo%2Fic0NPv512QigjPr3I8fEzAhwbLZfig7x6dwDyVaogEIIA5%2BuSL5NkwbGUFhB3ExX1rpf%2ByXU6lYpr8DsX1CIj0F3yKHchyHjv4HpD4lam76egwqqstnNL5uzmBnfDZIqsPWp4iahmk4p%2FqpdXNy%2B%2BR8w2DGUF%2BFe3tCZhUio6HyWbvGrGiPAah7CCbzGX9HwxthfQWCxocdkr3UBqYcV1ccja9cMAn0UjUH5a6hc4SpwXwt%2FIHxBMx%2FET8%2F1yul%2FAABycW2YJt2ZWALY20AWtC57SHxAzZqSUG0xqbGYVOJ7QoA8kQ5uYHV1d5Ni%2B7OBoKEo6IDbhiA96Fqb7mV4GuucHDXuWtwTF2fWYlcg6oozijlXmnuAh7eROYH79rRd471c0T8GhSlskL7%2BiRNsuFnYCjmoJypzgtq21%2FlONGdwIu1FVzy5yNSCrqCXQPB%2B99i04JecH0HC6momgnwlRmRQhZD1IEvGntCn4vDQJvQBkaO7QlSVnBKGX%2FBvY2pHQuFDVrfDePaeq6oMzIgoig4xeBneWcKsqBQBR3sT8xkA6jXQJTLL4dZg2EHJmB0OR9dYNqK4PCKS4Ve50W6m0fBwKD4m6Zn9z0c%2BMO7Rq8sGOqUBEKGispfPcvJ214kIMUHT40Oh27qhRoiiQBTxApoA%2BbnzxzkyVGjF2lAjL8USx9xVV910rtpVrK3CPhS9KCxPewEi6pOGMa0SjD7W4VHo2eJ%2F%2F0Q3%2BsEgtYn9%2FwxDWFnbVIYmMgAfh9N1Dt%2FqxR%2Fl0IkW10g3sJJFFT476RLgBNMVfwwK2euWeuz4HOvKgAk3zYDDQzAI2w6xJQ%2BYP82GCEiYHdFo&X-Amz-Signature=f13e5777c0bac1a164bdb3cbf4671060ad2516dc0a887aa9795a7550f656d0dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

