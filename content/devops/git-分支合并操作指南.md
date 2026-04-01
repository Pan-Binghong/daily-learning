---
title: Git 分支合并操作指南
date: '2026-03-31T13:57:00.000Z'
lastmod: '2026-03-31T14:02:00.000Z'
draft: false
tags:
- Git
categories:
- DevOps
---

> 💡 本文以 moodoor-agent-tools 项目为背景，系统梳理 Git 分支合并的完整工作流，涵盖日常开发、冲突解决、受保护分支等核心场景，适合团队协作开发时参考。

# 一、基本概念

在 Git 多人协作开发中，分支管理是保证代码质量和发布稳定性的关键机制。以下是常见的分支角色与术语说明：

标准分支合并流程：

```plain text
feature/xxx  →  (MR)  →  dev  →  (MR)  →  main
```

---

# 二、日常开发流程（从头到尾）

## 第一步：从 dev 切出功能分支

每次开发新功能前，先同步 dev 的最新代码，再切出独立的功能分支，避免与他人工作产生干扰。

```shell
# 切换到 dev 并拉取最新代码
git checkout dev
git pull origin dev

# 创建并切换到新功能分支
git checkout -b feature/htp-workflow
```

## 第二步：开发并提交代码

在功能分支上自由提交，遵循语义化提交信息规范（feat / fix / refactor / docs 等），方便后续代码审查和历史追溯。

```shell
# 暂存所有修改并提交
git add .
git commit -m "feat: 新增HTP房树人绘画测验(htp) workflow"

# 推送到远程仓库
git push origin feature/htp-workflow
```

## 第三步：在 GitLab 创建 Merge Request

功能开发完成后，通过 MR 流程申请将代码合入 dev，触发代码审查，确保代码质量。

1. 打开 GitLab 项目页面
1. 左侧菜单 → Merge Requests → New merge request
1. Source branch 选 feature/htp-workflow，Target branch 选 dev
1. 填写标题和描述，点击 Create merge request
## 第四步：审查与合并

持有 Maintainer 权限的团队成员完成代码审查后点击 Merge 按钮，合并动作将自动触发 CI/CD 流水线，完成构建与部署。

---

# 三、遇到冲突怎么办

冲突发生在两个分支同时修改了同一文件的同一区域，Git 无法自动决定保留哪一方，需要开发者手动介入解决。这是团队协作中最常见的问题之一。

## 冲突标记的含义

冲突发生时，Git 会在文件中插入冲突标记，结构如下：

```python
<<<<<<< HEAD
# 这是当前分支（dev）的内容
from api import api_mandala, api_dreamwork
=======
# 这是要合进来的分支（feature）的内容
from api import api_mandala, api_dreamwork, api_htp
>>>>>>> feature/htp-workflow
```

- <<<<<<< HEAD 到 ======= 之间：当前分支（HEAD）的内容
- ======= 到 >>>>>>> 之间：对方分支（feature）的内容
## 解决冲突的步骤

手动编辑冲突文件，将两段内容合并为正确的最终版本，删除所有冲突标记符号：

```python
# 合并后正确的结果
from api import api_mandala, api_dreamwork, api_htp
```

编辑完成后，执行以下命令标记冲突已解决并继续合并流程：

```shell
git add main.py          # 标记冲突文件已解决
git rebase --continue    # 继续 rebase（若使用 merge 则执行 git merge --continue）
```

## 实际案例：main.py 冲突分析

在 moodoor-agent-tools 项目中，main.py 出现冲突的根本原因是模块加载顺序的问题：

- dev 分支：要求 load_dotenv() 必须在所有业务模块 import 之前执行，否则环境变量无法被正确读取
- feature 分支：新增 import 时错误地将其插入到了 load_dotenv() 调用之前，导致顺序错误
修复后的正确结构：

```python
from dotenv import load_dotenv
import os

# 必须先加载环境变量，再导入依赖环境变量的业务模块
env = os.getenv("ENV", "dev")
load_dotenv(f".env.{env}")

# 环境变量加载完毕后，再 import 业务模块
from api import api_mandala, api_dreamwork, api_familyconstellation, api_htp
```

> 💡 凡是在模块初始化时依赖环境变量的代码，务必确保 load_dotenv() 在 import 之前执行。这是 Python 项目中最常见的启动顺序陷阱之一。

---

# 四、常用命令速查

以下命令在日常分支管理中高频使用，建议熟记：

```shell
# 查看所有分支（含远程）
git branch -a

# 查看某功能分支比 dev 多了哪些提交
git log --oneline dev..feature/htp-workflow

# 拉取远程最新代码（不修改本地工作区）
git fetch origin

# 将某分支合并到当前分支
git merge feature/htp-workflow

# 使用 rebase 方式整合（提交历史更线性整洁）
git rebase dev

# 查看当前存在冲突的文件列表
git diff --name-only --diff-filter=U

# 放弃当前 rebase 操作，回到操作前状态
git rebase --abort
```

> 💡 merge vs rebase：merge 保留完整的分支历史，适合需要追溯合并节点的场景；rebase 将提交历史变为线性，适合保持 dev/main 历史整洁。团队应统一选择，不要混用。

---

# 五、dev 分支受保护怎么办

GitLab 中 dev、main 这类核心分支通常被设为受保护分支（Protected Branch），禁止直接 push，所有变更必须通过 Merge Request 流程进行。这是保障代码安全和审查质量的重要机制。

## 如何判断分支是否受保护

直接 push 时收到以下报错，说明该分支已受保护：
You are not allowed to push code to protected branches

## 正确处理方式

1. 将代码推送到 feature/xxx 功能分支（不受保护）
1. 在 GitLab 上创建 Merge Request，申请合入 dev
1. 由持有 Maintainer 权限的成员审核并执行合并操作
---

# 六、完整操作回顾

以 moodoor-agent-tools 项目为例，完整的分支操作链路如下：

```plain text
origin/dev (e4403c5)
    ↑ pull
本地 dev
    ↑ rebase
feature/familyconstellation-workflow  ── 解决 main.py 冲突 ──┐
feature/htp-workflow                  ── 解决 main.py 冲突 ──┤
                                                              ↓
                                          在 GitLab 创建 MR !1 和 MR !2
                                          等待有权限的人 Merge → dev
                                          CI/CD 自动部署到 k3s
```

最终结果：

- MR !1：feature/familyconstellation-workflow → dev
- MR !2：feature/htp-workflow → dev
---

> 💡 记住一条原则：功能分支随意提交，dev / main 走 Merge Request。

