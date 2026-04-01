---
title: Git 分支合并完全指南：从功能分支到 Merge Request
date: '2026-03-31T14:30:00.000Z'
lastmod: '2026-03-31T15:00:00.000Z'
draft: false
tags:
- Git
categories:
- DevOps
---

> 💡 本文以 moodoor-agent-tools 项目为实战案例，系统讲解 Git 分支合并的完整工作流，涵盖从功能分支创建、Merge Request 提交，到冲突解决的全过程。

# 一、基本概念

在多人协作项目中，分支管理是日常开发的核心。以下是几个关键概念：

标准合并流程：

```plain text
feature/xxx  →  (MR)  →  dev  →  (MR)  →  main
```

![](https://git-scm.com/book/en/v2/images/basic-merging-2.png)

Git 分支工作流示意图

# 二、日常开发流程（从头到尾）

## 第一步：从 dev 切出功能分支

开始新功能开发前，先确保本地 dev 与远端同步，再切出专属功能分支：

```shell
git checkout dev
git pull origin dev
git checkout -b feature/htp-workflow
```

## 第二步：开发、提交代码

在功能分支上自由开发，提交时建议遵循 Conventional Commits 规范（feat / fix / chore 等前缀）：

```shell
git add .
git commit -m "feat: 新增HTP房树人绘画测验(htp) workflow"
git push origin feature/htp-workflow
```

## 第三步：在 GitLab 创建 Merge Request

1. 打开 GitLab 项目页面
1. 左侧菜单 → Merge Requests → New merge request
1. Source branch 选 feature/htp-workflow，Target branch 选 dev
1. 填写标题和描述（简要说明本次改动的目的和影响），点击 Create merge request
![](https://git-scm.com/book/en/v2/images/basic-merging-1.png)

GitLab Merge Request 审查界面示意

## 第四步：审核与合并

拥有 Maintainer 权限的成员审查代码后点击 Merge 即可完成合并。合并后 CI/CD Pipeline 会自动触发，执行测试和部署流程。

> 💡 如果 CI/CD 检查失败，MR 会被标记为不可合并，需先修复流水线错误再提交。

# 三、遇到冲突怎么办

当两个分支修改了同一文件的同一区域时，合并就会产生冲突。冲突不可怕，关键是要理解冲突标记的含义并正确解决。

## 冲突长什么样

Git 会在冲突文件中插入冲突标记，将两个版本的内容都保留下来供你选择：

```python
<<<<<<< HEAD
from api import api_mandala, api_dreamwork
=======
from api import api_mandala, api_dreamwork, api_htp
>>>>>>> feature/htp-workflow
```

- <<<<<<< HEAD 到 ======= 之间是当前分支（HEAD）的内容
- ======= 到 >>>>>>> 之间是待合并分支的内容
![](https://about.gitlab.com/images/blogimages/gitlab-flow-duo/The-GitLab-Flow-2023-mr-pushing-code-portion.png)

代码冲突标记示意（需手动选择保留哪一版本）

## 解决冲突的步骤

1. 手动编辑冲突文件，删除所有冲突标记（<<<, ===, >>>），保留正确的代码内容
1. 将解决后的文件标记为已解决，然后继续 rebase 或合并：
```shell
git add main.py
git rebase --continue
```

## 实际案例：load_dotenv() 引发的冲突

moodoor-agent-tools 项目中 main.py 曾出现冲突，根本原因在于：load_dotenv() 必须在所有业务 import 之前执行，但 feature 分支误将 import 语句写到了环境加载之前。

正确的文件结构应如下所示：

```python
# 第一步：加载环境变量（必须最先执行）
from dotenv import load_dotenv
import os

env = os.getenv("ENV", "dev")
load_dotenv(f".env.{env}")

# 第二步：加载业务模块（依赖环境变量）
from api import api_mandala, api_dreamwork, api_familyconstellation, api_htp
```

> 💡 环境变量加载顺序问题是 Python 项目中最常见的冲突根源之一。建议在项目规范中明确约定 load_dotenv() 的调用位置。

# 四、常用命令速查

以下命令覆盖了日常分支管理的常见场景，建议收藏备用：

```shell
# 查看所有分支（本地 + 远端）
git branch -a

# 查看功能分支相对 dev 的提交差异
git log --oneline dev..feature/htp-workflow

# 拉取远端最新状态（不自动合并）
git fetch origin

# 本地直接合并（适合本地测试）
git merge feature/htp-workflow

# 将当前分支变基到 dev（保持提交历史整洁）
git rebase dev

# 查看有冲突的文件列表
git diff --name-only --diff-filter=U

# 放弃当前 rebase，恢复到 rebase 前状态
git rebase --abort
```

# 五、dev 分支受保护怎么办

当直接 push 到 dev 时，会遇到如下报错：

```plain text
You are not allowed to push code to protected branches
```

这是 GitLab 的分支保护机制，正确做法是走 MR 流程：

1. 将代码 push 到 feature 分支（git push origin feature/xxx）
1. 在 GitLab 上创建 Merge Request，目标分支设为 dev
1. 等待拥有 Maintainer 权限的成员审核并点击 Merge
> 💡 如果团队只有你一人，可在 GitLab 项目设置中将自己添加为 Maintainer，或临时解除分支保护（不推荐长期使用）。

# 六、完整流程回顾

一图看懂完整的 Git 工作流：

```plain text
origin/dev
  │
  ▼ git pull
本地 dev
  │
  ▼ git checkout -b feature/xxx
feature 分支（自由开发、提交）
  │
  ▼ git rebase dev（同步最新代码）
解决冲突（如有）
  │
  ▼ git push origin feature/xxx
GitLab Merge Request
  │
  ▼ Maintainer 审核 & Merge
dev 分支
  │
  ▼ CI/CD Pipeline
自动测试 → 自动部署
```

> 💡 记住一句话：功能分支随意提交，dev/main 走 Merge Request。

---

## References

1. Git 官方文档 - 分支与合并 (https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6)
1. GitLab 文档 - Merge Requests (https://docs.gitlab.com/ee/user/project/merge_requests/)
1. Conventional Commits 规范 (https://www.conventionalcommits.org/zh-hans/)
[https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6](https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6)

[https://docs.gitlab.com/ee/user/project/merge_requests/](https://docs.gitlab.com/ee/user/project/merge_requests/)

[https://www.conventionalcommits.org/zh-hans/](https://www.conventionalcommits.org/zh-hans/)

