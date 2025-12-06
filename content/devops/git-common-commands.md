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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB3BUBLZ%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZJm7IzASK5KGQJHUIHdPyIvCnlWxLt3%2BT%2BNHZNXJhRAIhALCU2iLLLn%2BMC8RaSSqwH%2F8vUkoMKNYXW6H%2Fhhpa5MXFKv8DCGsQABoMNjM3NDIzMTgzODA1IgxWzgpq6TjYRoQgT60q3AMr1Ah31iZ45DrbM9ul60MNrJWYNYXhsHFip8jo5NVKJ%2FxvlfemFxWFS4yQ7fFY2%2F1o5GF2yNzCfv0Ut3V6Bhqb%2B3I1EF7hN0HJnu7xkTP4HaujkXRBwCwAfaR9rEHcHeMXjFwblJ4WBXt4YRpfQLSqjP%2FYS2jyqVUcR83oXmE1EqUXyufCTxTxEHLRsTT0aHmVJnRdD%2Fs61FHcEf%2BJWyxvX6GdetI4ycgyZycKWnmMWZkyr7JUip1aZvf4l1Er2eIKS7F7oDnMC%2BqKF0Rhu12ZKMcIRfgxMvoFM8vjOxewtTNrYRf4z5LbeqDi2qvrkxokIsEkV2h1Gr7q3auzzWVzDelWzTRIiVzCtNv5xQkM7rr5kFzqgUTE%2F3tScb60crY39XCTbkJP66F2dRxVxSyUYi448OwpX99fRrnfuOu%2BeW%2F78cLXY%2F5eDxlFkhGNZcKJdcZQQpCS7U%2B%2FilI5zPZSeHIqnPd680lRah3PvQJb%2BtMrIt8KR8A4ed7taZbjuEGct2mbNHFZAf1FG4YQM1%2BCZZSHyk3fcbbJUd6439UAnwIQu40NhEzOd82nqUUZE0hkrpxYoV7gFsWfQ4gx8EmkjPOzaqLCsyDhlWZvvhu4p%2F%2FsB5wscSi9geESfzChp87JBjqkARR0%2FiUfw%2F8LhKlw0RnHQufJa4rPqfoocicne6mdD5AdoULHchhZ8H7CdNLycdzUFpcZXcoiyeYsjMeJskvptw2A3zAqxkGl6vkqXCQ5epTA5y3cjB25OcK97okeI4lqQd%2FDno3vdr5vcAyzdXlRqTyCZYDwszywVdQBHaa0f5l64emFZ%2Bd9ZBREPqBzxAHCZIzzlpLoYl8QGuTaDzANMgaSMP74&X-Amz-Signature=cfa6c3f4cea8f7ac293191f2145c0b8b85117aa43232da4bb83b4c388c20369e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

