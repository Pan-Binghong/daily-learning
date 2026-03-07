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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PNEFFJY%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDuMEVZ%2BVLq%2BvWHXIwKSbWfKIs6qFqO5INxqFEkuIKhZQIgYZrxrxIuwBE2sS5ldfftX6DHm92Y%2BGPu0WS6cljg2lIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFGI7PAluz4o9oD6lircA9011WBYD8H56IcTRV2yaRXpqo0mvWG%2BCpoaF4MtwGRyQCmhdi9SJXdlK3xqYidoHt8vvAMSaBURs6socbhHs%2FGPM1y%2FEE%2FCDhxuY8oEEcbq%2FuMXD0XkSzW6FqIUnxrS0kYEqo0vGKoGAvvITXcpgS4%2B8UGnaaPbJ1Pixacx4q%2BoJauSXlZesF%2F1A6eX7pF2miol5Is5aahSitDGFTzj4BYAoL1umE9bdD86R2lveDQigbgwcsftozWAm9IcKP%2B5jjCRm0cWFvMOjKmvbjAQ8tPhpdNnUwTSZmwXjiEZtr3Qb%2BBZS8aWK962W8F1o3We0bSYrT8Oc3H6oballcjmrfCxIHvpacy1X1%2FSbuAv1l8RobEtVTxHHdVOJfdr%2FUWxg4k3KZRcGPziZPFLFOltddXQXedWqCBhISQTleQFC6sun2gn%2FoVMpewRfIBilW0sLS5ZxrLc5Hvg7kksFfLII7Gx98nkz6U7Gh2%2FW0jrQkE6qQdrReozmOEdeg36E0bmGF0NJ6KVXy04cKKX8ILcn3thGvHwdKh%2BEg9wGhQEGRf7dMlcylhwAVjQkp0nKqmdAyhCCRiwJlv0DvH1kD7yvM%2BD3zV2tPGTyxK6a4LYsur%2Fl7VrwMtGjsExYOsKMOeTrs0GOqUBpRxrSC2A%2FzIDO782SCbd8wy4TFJYBEZpmqgwr0b0%2BFn87ak1oMnY2rKsd8UMJXLEMY9nO3J8ueDJCpeV5XgX6dJUQJ3KmnOHSXwYcsFRi%2FDomLUtJNt0qmfS2RghzaYHLPRveCFK8UKj4SdYmJfRu3bXEmzgYfsQxob3q99OlzEiNURQK5V4QUA%2BYLrjiysVGzW1JsFYjlF7gzJm5l6FD4gvjlv9&X-Amz-Signature=d18540d219d5e5516abd8d826a92a7867c2618514db67c91e2c4fa8e95a439dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

