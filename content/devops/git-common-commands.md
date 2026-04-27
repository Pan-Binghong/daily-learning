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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXK2JFFI%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCU7vkIJre85zSk41cj004rbhVTolfutWTdRpLFxjGAgIhALAkl7ss7IGu%2Ba%2FQ5N7TsqoI%2BOLC3m6uRpNmEgK75NU8KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMlGB7OomfiiTYY24q3APnPkeksT00%2BfibH2RfY7zqm9y%2BIYHcql8iw%2F0iArTf%2FvmNIV8hPkf382CAGISpJ7inEHuGhdIVAg4VmAUiy2AVji0Ne0vhU1G%2BtpJWcZyfJ4kEC%2FR%2BZ5p3V1DUmfDS1UO8hy3dfMLM98gAxkZjyNSKNBFk4fcAI1U9achIVb1nvVAMa00ElMYVVUtGeYmT1i9eDELq5YQf2wEBpesx1v1CFe64FOOGBBB37Xfgd7z6XT8GMAlieWHsdGiaJUX3T1hptIN%2Fb01g81OkrDAs3YASALOZwnbw9CpVOHr%2BwmxQ%2Fc%2FlLnqzMZt4%2FWfnHUHJjh%2Fm2XtdW8OUYx8vRmik3Soqj4ewxbASMzKVzBISpn0zaui97mtZLAbedmbXtGp%2BdcfC%2BJWK%2Fmbw6XXljShtLza%2FKnyA3SaS%2BBbHFVL3XadhQbd3k0hDco4M2o8PeHeOCkuv5tbPki0mAEz2Ue6qgXqmoiwVdvPrL70oMcGU3UMyX6SAqeZYbwwIDQ7%2FLoe%2Fe6FjUOWdiodAya9H9YRoihCR5Pm7tGi5Ul7YlHBH2EMVrw72wd6yONsllYrcz%2BIenhE30m0o9Z6Jck7KNwYwkA3HBmn98zc%2BeVRD60p3kx7Qeawnjm9UKJ1EPG%2B0VjDntrvPBjqkAUVkGfl%2F6gsYkzL7m2oxI0dROAP1tJti93QD%2BfBlYRO3O%2FEpK12uhVkG74gs31XmnncIiJickGJr0jUGzexFmlhi3EOBcPnqgqgrla8yIZWt5UjpMxNoYiVgZcPuEzGDuvit6d1Km2ZHZhOApGLddwnbhb38nLZ4mKKfYB2Sqqm4vgMR4idwYQRJ6%2BCvkJcOHUKQtVgLTA%2B%2FtAkOoO0oopPssUCY&X-Amz-Signature=4037ad83a021d7534871e9b6c47df8551f9a4b3e8d22449c911330c63dd7fb59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

