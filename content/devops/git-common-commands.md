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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677IEOHOC%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIF%2BgE3QOw4rbLScGNmMQN6K6nhuX8ZO2rat7LM7I6DbZAiEAhTTKi2jNUQaUYAPkMTBvxUSsyYOIMERxq2Ug%2FY91jhkq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDHUVOg%2BiRrciYp%2BQSCrcA2P0g0LBt2eocJbnv%2FcHeAx%2FktzH1EbQ60nTjemKjDKYu5YONKcxnozG%2BgV%2Fg7p1VrTK035s5fTM4ej3jg540zSy9godOKKzbW87vpL6v8bKFjRBbx9u6dgMwvFefqmiPva2qunRarg9UrhvITDBa83IWBtsF7f%2BvG%2FvzPN82ZUajBXr7GNkMik9nmQf995jP5HOT6zEBFdrP9ESs2HTyKvdY27lFNh0PISdosoGQ0ItyQs0gxpWCwNnkK%2BSjhXj5NKwpLHnrecJYaG%2FhQHEjdas9FHnXpPkLNsJZ53u5d%2Fe382o%2FcidJnnBYrNprMuIS0u9VY%2F9P5sl00YQROQSZwOTWKUJNWq14Z1T%2BbTrDaVDB1lW%2F5Xyy6E5rndGFzUgMnEeyXrjbeUaf8zyJjCv9DqlBdmXvtfQzObMkG%2Fk5WQDchSNWJ99Q%2BegjW%2FFttLixpcxXUu7vAdtO4aaPXc7%2BYMi4nR%2BkZE1qe7xFDJs3rnQRftkvMoRoBATtczoBJf9YFRZ78yeSnV68fqTr1FYAJY%2BBgH%2BYczFbpeX7ALJNfzyEIc9pOZ%2BCdyD6sGsrdrNL%2By9YR0QQ4wOxxecKyC%2B1T8fBotS5w1gUljQD%2F5Ypm%2FwRJc9yj3jDTvKvf%2BgMPyv%2BMkGOqUB25ulhcy1sNJ0EKkTF6DcdWhNPAw7iMsg13ymuDdHiGAn%2FN43SpSlqhUW%2F8DHaNYLtlw8lYfUYFPpfRnytqYnopA7tClL%2BmCPReRDYWAfCvDtg9GlMccMkws9syDJGesdjjfpUu%2B9MmN3KQHu%2F3B22BNiKaX%2BC6Sdpy6UC0xgiFh49te767tXCCD7Rz%2B6rL4X0UuIXsbtd6g%2FmwMynnaNYQOh0yH9&X-Amz-Signature=e400df3eda8192d1b2c8fcea663ec196d6f5be5f3ac423aae0d4f995d8139232&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

