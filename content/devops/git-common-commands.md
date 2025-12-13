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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCPUU36T%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIC8zDa0wzFhO7%2F1VUd3C%2FjruAydpspQHZofW6kms8sEJAiBBEwceKbcvvUPmOHF%2FFD2zFlB7q7Qh8Kseel2hw0ApECr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIM3XQvSCpaSTO3mkurKtwDGeNQyt%2BGDSCKoNUXWOXEsycW26LJyJvDtUshD3nFpQz0DJw1JABbsvOUIijOIAbVp1EoRYzvb8fTpA6ozPAaKdEJlCQfrjGqS9gDF5VLRgt24t83R0ZUNEYAzH1plRrOUHlEazq%2BwMG9dDEkDQh17B0u5tU%2BeOpcrPLOXC599rZ%2FXQLS9T4yEsib18B%2BzbNaq8CN7sZ%2BcU%2F8FGW%2BmHBCRn16nGvCL9JupD1DVHhUHHNs46Ak83bYjiIIo4D%2BIgWH7P6aXOUMWokHU6%2FtrFFi9sCbnH54Hzdy80HCwDTzZC%2BiqZq9GktyPisvmd83T%2B3xJECQv1IaQpEEaOA0AExLRXkpga0tKXMgrVBCQ%2FrVUJkhpf2xKL%2FoVV3rT5jhkWlapZ3tfNP05kaCzZneGkF3Kxc9lY8GwFyWRMa%2FJMrLrU6bp3stN1aZD4dPnKdFk14A7PidlnxrgayQcbRWcWQ07ZTqeRibugLCjzmWdsK0TxuM1BHW4t70o7xliSzq%2Bzv%2FGzhz2HJRUKc5pqFqCpk0XKvWK%2BWdaHMUdYvOp9VXh%2BUtl3nWQ5RGsz5VzziTGOamNtneS3eoi%2BDnoWXo9Ozl2YRutbFnbhycItTvB3U64CrT%2BsIDDWTRQ%2FmZEvgwm43zyQY6pgEvcDrVlzIzvUbkm06VHzGu2nUv5ocJbtenzF%2FqKmeQT3eC5KDPKxxupSGc54MNTsvA3lRRQJ5%2F83%2B7ny5YaA4b3B6T1ozmvK3%2FF1kOYbEyvSgZ9QOwKoi4WnKTrfVbdlGmk3dTGK%2FsVFFV%2BrOOeATY4v0VS60fdSWtqYAeB5YFBZdHo8Ud%2B1it2f167%2BUavTI8tp85jK%2FyTgAT3L1DhDGEoMTbC9rC&X-Amz-Signature=515c44efa398cb55cdc8facee77358b977fa93e8d291f74b5ed81c76c1db08b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

