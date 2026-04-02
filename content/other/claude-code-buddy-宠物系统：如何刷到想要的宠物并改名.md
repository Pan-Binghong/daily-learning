---
title: Claude Code /buddy 宠物系统：如何刷到想要的宠物并改名
date: '2026-04-01T14:01:00.000Z'
lastmod: '2026-04-01T14:04:00.000Z'
draft: false
tags:
- Claude
categories:
- 其他
---

# Claude Code /buddy 宠物系统：如何刷到想要的宠物并改名

## 背景

Claude Code 2.x 新增了 /buddy 功能，启动后可领养一只专属像素宠物。宠物的物种、稀有度、眼睛、帽子、属性完全由账号 userID 经哈希算法决定，官方没有提供重置入口——也就是说，你天生注定只能领养一种宠物。但社区已经破解了这套算法，通过 bruteforce 暴力枚举 userID，可以找到任意你想要的宠物对应的 uid，然后替换配置文件即可。本文介绍完整操作流程。

![](https://images.unsplash.com/photo-1762242298589-582f5f6c3fb1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w5MTEyNTV8MHwxfHNlYXJjaHwxfHx0ZXJtaW5hbCUyMGNvbW1hbmQlMjBsaW5lJTIwZGV2ZWxvcGVyfGVufDB8MHx8fDE3NzUwNTE4OTV8MA&ixlib=rb-4.1.0&q=80&w=1080)

## 核心原理

> 💡 算法链路：userID + SALT("friend-2026-401") → Bun.hash() → Mulberry32 PRNG → rarity / species / eye / hat / shiny(1%) / stats

宠物系统支持 18 种物种：

- duck（鸭子）
- goose（鹅）
- blob（史莱姆）
- cat（猫）
- dragon（龙）
- octopus（章鱼）
- owl（猫头鹰）
- penguin（企鹅）
- turtle（乌龟）
- snail（蜗牛）
- ghost（幽灵）
- axolotl（六角恐龙）
- capybara（水豚）
- cactus（仙人掌）
- robot（机器人）
- rabbit（兔子）
- mushroom（蘑菇）
- chonk（肥猫）
稀有度权重分布：

> 💡 native 安装（brew install bun / curl 安装）用 Bun.hash()，npm install -g bun 安装用 FNV-1a，两者结果完全不同！确认安装方式再跑脚本，否则刷出来的 uid 对应宠物会不一致。

## 操作步骤

### 第一步：安装 bun（native 方式）

必须使用 native 安装方式，npm 安装的 bun 哈希算法不同，刷出来的 uid 对应的宠物会不一致。

```bash
# macOS / Linux native 安装
curl -fsSL https://bun.sh/install | bash

# 或 Homebrew
brew install bun

# 验证
bun --version
```

### 第二步：获取 buddy-reroll.js 脚本

从 linux.do 教程获取完整脚本（见文末 References），保存到 ~/buddy-reroll.js

### 第三步：搜索目标宠物的 userID

脚本通过枚举随机 uid 并计算对应宠物，找到满足条件的第一个结果。legendary shiny rabbit 约需 10 万次迭代，约 0.3 秒。

```bash
# 搜索 legendary shiny rabbit
bun buddy-reroll.js --species rabbit --rarity legendary --shiny --count 1

# 只要 legendary（不限物种）
bun buddy-reroll.js --rarity legendary --count 3

# 验证某个 userID 对应什么宠物
bun buddy-reroll.js --check <userID>
```

### 第四步：修改 ~/.claude.json

找到脚本输出的 uid 后，编辑 ~/.claude.json，替换 userID 字段，并删除 companion 整个字段（否则不会重新孵化）：

```json
{
  "userID": "此处填入脚本输出的uid",
  "hasCompletedOnboarding": true
}
```

> 💡 删除 companion 块后，上方字段末尾不能留逗号，否则 JSON parse error 导致 Claude Code 无法启动！建议用 jq 或 VS Code 验证 JSON 格式再保存。

### 第五步：重启 Claude Code，运行 /buddy

保存 ~/.claude.json 后完全退出并重启 Claude Code。运行 /buddy 命令，系统会检测到没有 companion 字段，触发孵化流程，按提示命名宠物即可。

![](https://images.unsplash.com/photo-1593720213681-e9a8778330a7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w5MTEyNTV8MHwxfHNlYXJjaHwxfHxzZXR0aW5ncyUyMGNvbmZpZ3VyYXRpb24lMjBmaWxlJTIwY29kZXxlbnwwfDB8fHwxNzc1MDUxODk1fDA&ixlib=rb-4.1.0&q=80&w=1080)

## 改名方法

宠物孵化后可以随时改名，直接编辑 ~/.claude.json 中 companion.name 字段的值：

```json
"companion": {
  "name": "panbit",
  "personality": "...",
  "hatchedAt": 1234567890
}
```

保存文件后重启 Claude Code 即可生效。personality 和 hatchedAt 字段不要修改，只改 name 值即可。

> 💡 改名不会触发重新孵化，companion 块只要保留完整、JSON 合法，重启后宠物外观不变，仅名字更新。

---

## References

1. buddy-reroll.js 脚本完整教程 — https://linux.do/t/topic/1871870
1. Claude Code /buddy 刷宠物方法（另一篇参考）— https://linux.do/t/topic/1873901
1. Claude Code 官方文档 — https://docs.anthropic.com/en/docs/claude-code/overview
[https://linux.do/t/topic/1871870](https://linux.do/t/topic/1871870)

