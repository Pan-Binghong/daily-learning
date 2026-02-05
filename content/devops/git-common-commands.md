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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URZOYFSS%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIBQM7qCcNCmzyp35cRgEvpmdrsWoyg84Zs9dlrihF8wxAiAs6NHV%2BFBthrVQuMx7tC3%2BFcdNRadn55GtYHqtSiEQECr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMHN3hlX4En7Ng8PAtKtwDXFqytVDJnBRpyIfJ%2FTaolUXaI98R5Pked1AVv8spBbZsrD6irldaQs2NCjAfbYO4ghmbRiIdAyhiu5D38kG5P%2BGtSMdVwodpVjLnzw%2BPCax%2FcGZkTeRiziWe%2FYPGHGrIosduxp%2FI9aP6AaN8vi1MKp5L1usYxUG1aD%2FqEVIcXAjwkrChbuiyumCBnGTGY0IJOy4uh8UAawOeQ4vsXUpOgOuasHPs3niBWuuuw00gGNothDdcHSkBpd0HbtbXgXie1qaula6Y5EI0hFUsTEzXSH5UkH%2FHw%2B8UgLZ4ViTHV0cg5hj3PPHY48gqCMywaZ07DiQrxs8IAVKL%2B0suUGrtWi%2BLotv0kn2xgx9LDpa4O8QopF5gplD1QSoVaABiqL5ZHa9V1X5%2B98Ju%2F4VYtnPnJeJ%2BwxqjlI0j5CAjfS6p%2Fixjmt4JElQgBBuDrkr49yjl6mN9pkpMrG7b9AMdSswNTQmZLci%2BS80npEURSW5uykA%2FN8FCfEfeUoSia6hVdS4sCx0FNk4lSanL9UXllwy50RcdmJQleAJUDaGJjA7yjQBd%2FEKce1GShLkYEj5kbmklukoBA4rTQ9CDmQvS33nrMUSAk1B13m3CoZi9WJF6DdRsWBZxDUNM2jzHGaIw7pKQzAY6pgHSItNVzJxFTJ3Jap3VHV9P5M6TQWC8sXqCUc8%2B0E%2BcQ0u0gwpk6bMcR3rIM4mmTeuIe28SifhkcQG36udzWCAY9pbva4k%2FfVyhmyMHTKbBLgZ4RlNiqjU6pyXVslvbNhBtTfCN1ggUbUmj7sffxKdNDTl3pHyOVSzN2352Cw3MuTj9vA479%2FGcs%2FZohhDYRKKy%2B7WEnvC6RCrDXf3dHgQFZCzOzN17&X-Amz-Signature=b8b0df4f7f0ed52a6f819fb4325ae8b8cc42906168caaa046f8d6ec791a0273c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

