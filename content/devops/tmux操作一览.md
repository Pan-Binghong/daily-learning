---
title: Tmux操作一览
date: '2025-02-25T01:49:00.000Z'
lastmod: '2026-04-01T04:32:00.000Z'
draft: false
tags:
- Tmux
categories:
- DevOps
---

> 💡 Tmux 是一个非常强大的终端复用工具，它可以帮助你在一个窗口中管理多个会话，非常适合长时间运行任务或多任务处理。

---

## 安装

---

```bash
sudo apt update
sudo apt install tmux
```

## 基本操作

### 会话管理

---

- 新建会话
- 分离会话
- 列出会话
- 关闭会话
### 窗口操作

---

- 新建窗口
- 切换窗口
- 重命名窗口
- 关闭窗口
### 窗格操作

- 水平分割
- 垂直分割
- 切换窗格
- 关闭
## 使用示例

---

- 查看当前服务器内，有无tmux会话，输入命令进入。
- 进入会话后，开启2个窗格。Ctrl + b ，%
- 在model 会话内，新建窗口，并修改名称。
> References

---

# 核心概念：Server / Session / Window / Pane

tmux 的架构分为四层，从外到内依次是：

```plain text
tmux server（后台进程，自动启动）
 └── session（会话，可多个）
      └── window（窗口，类似浏览器标签页）
           └── pane（窗格，窗口内分割的终端）
```

### Server（服务进程）

tmux 启动后会在后台运行一个 server 进程，管理所有会话。通常不需要手动操作，关闭所有 session 后 server 自动退出。

### Session（会话）

一个 server 可以有多个 session。每个 session 相互独立，即使断开 SSH 连接，session 内的任务仍然在后台运行。

- 适合用途：跑训练任务、长时间部署脚本、多项目隔离
- 常见操作：新建、attach（重新连入）、detach（脱离）、rename、kill
### Window（窗口）

每个 session 内可以有多个 window，类似浏览器的多标签页，底部状态栏会显示所有窗口列表。

### Pane（窗格）

每个 window 可以分割成多个 pane，每个 pane 是一个独立的终端。常用来同时监控日志和执行命令。

> 💡 记忆口诀：一个 server 跑多个 session，一个 session 有多个 window，一个 window 分多个 pane。

---

# 开启鼠标滚轮支持

默认情况下 tmux 不支持鼠标滚轮，需要在配置文件中开启。

## 配置方法

```bash
# 编辑（或新建）配置文件
vim ~/.tmux.conf

# 添加以下内容
set -g mouse on
```

```bash
# 修改后，在 tmux 内无需重启，直接生效：
# 按 Ctrl+b 然后输入：
:source-file ~/.tmux.conf
```

## 开启鼠标后的操作说明

- 滚轮上下：直接滚动历史输出（进入 copy mode）
- 点击切换 pane：用鼠标点击不同窗格即可切换
- 拖拽调整 pane 大小：拖动窗格边框
- 点击底部状态栏：切换 window
> 💡 开启鼠标后，终端的原生选中/右键粘贴会被 tmux 接管，需要按住 Shift 再用鼠标选中文字，才能使用系统剪贴板。

## Copy Mode 内复制粘贴

进入 copy mode（滚轮滚动时自动进入，或按 Ctrl+b [ 手动进入）后：

```plain text
# 默认绑定（vi 模式）
Space 或 v     开始选中
Enter 或 y     复制选中内容到 tmux 缓冲区
q              退出 copy mode
Ctrl+b ]       粘贴 tmux 缓冲区内容
```

推荐在 ~/.tmux.conf 中开启 vi 模式，操作更顺手：

```bash
setw -g mode-keys vi
```

> 💡 tmux 的缓冲区与系统剪贴板是独立的。如需与系统剪贴板互通，可安装 xclip / xsel（Linux）或配合 tmux-yank 插件。

---

# 更多常用命令速查

## 会话管理

```bash
tmux                        # 新建匿名会话
tmux new -s mywork          # 新建并命名会话
tmux ls                     # 列出所有会话
tmux attach -t mywork       # 重新连入指定会话
tmux attach                 # 连入最近一个会话
tmux kill-session -t mywork # 删除指定会话
tmux kill-server            # 关闭所有会话和 server
```

## 窗口操作（Ctrl+b 前缀）

```plain text
Ctrl+b c        新建窗口
Ctrl+b ,        重命名当前窗口
Ctrl+b w        列出所有窗口（可上下选择）
Ctrl+b n        切换到下一个窗口
Ctrl+b p        切换到上一个窗口
Ctrl+b 0-9      按编号切换窗口
Ctrl+b &        关闭当前窗口（需确认）
```

## 窗格操作（Ctrl+b 前缀）

```plain text
Ctrl+b %        左右分割窗格
Ctrl+b "        上下分割窗格
Ctrl+b 方向键   切换窗格
Ctrl+b o        切换到下一个窗格
Ctrl+b z        当前窗格全屏 / 恢复
Ctrl+b x        关闭当前窗格（需确认）
Ctrl+b q        显示窗格编号（按数字快速跳转）
Ctrl+b !        把当前窗格拆出为独立窗口
Ctrl+b Ctrl+方向键  调整窗格大小（每次 1 格）
Ctrl+b Alt+方向键   调整窗格大小（每次 5 格）
```

## 其他实用操作

```plain text
Ctrl+b d        脱离当前会话（session 继续后台运行）
Ctrl+b s        列出所有 session（树形，可展开 window）
Ctrl+b $        重命名当前 session
Ctrl+b t        显示时钟（按 q 退出）
Ctrl+b ?        查看所有快捷键帮助
```

## 常用 ~/.tmux.conf 配置推荐

```bash
# 开启鼠标
set -g mouse on

# vi 风格 copy mode
setw -g mode-keys vi

# 状态栏刷新间隔（秒）
set -g status-interval 5

# 窗口编号从 1 开始（更直观）
set -g base-index 1
setw -g pane-base-index 1

# 修改前缀键为 Ctrl+a（可选，习惯 screen 的用户）
# unbind C-b
# set-option -g prefix C-a
# bind-key C-a send-prefix
```

> 💡 修改 ~/.tmux.conf 后，在 tmux 内执行 Ctrl+b 再输入 :source-file ~/.tmux.conf 即可立即生效，无需重启。

