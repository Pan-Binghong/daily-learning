---
title: OpenClaw vs Hermes Agent：2026 年最火两大开源 AI Agent 架构深度对比
date: '2026-04-13T13:45:00.000Z'
lastmod: '2026-04-13T13:50:00.000Z'
draft: false
tags:
- LLMs
- AI Agent
categories:
- AI
---

# OpenClaw vs Hermes Agent：2026 年最火两大开源 AI Agent 架构深度对比

---

## 一、背景：两场不同的革命

2026 年，开源 AI Agent 领域出现了两颗耀眼的明星：

- OpenClaw（前身 Clawdbot）：TypeScript + Node.js，GitHub ⭐ 302k，由奥地利开发者 Peter Steinberger 创建，2026 年 2 月爆火，成为 GitHub 历史上增长最快的项目。
- Hermes Agent：Python，GitHub ⭐ 74k，由 Nous Research 团队打造，2025 年 7 月发布，主打"自我进化"，最新版 v2026.4.8（4 月 8 日）。
两者都是开源自托管 AI Agent，都支持 Telegram/Discord/WhatsApp 等多平台接入，都可以对接任意 LLM。但它们在架构哲学上走了完全不同的路。

---

## 二、技术栈：TypeScript Gateway vs Python Agent

> 💡 OpenClaw 为什么选 TypeScript？因为它的核心不是 AI 逻辑，而是消息网关基础设施。Node.js 的事件循环天然适合处理 20+ 即时通讯平台的并发 WebSocket 连接。

> 💡 Hermes 为什么选 Python？因为它的核心是机器学习研究管道。Python 生态（PyTorch、Atropos RL、HuggingFace）让 Hermes 可以直接生成训练数据、跑强化学习环境。

---

## 三、架构哲学：Gateway-First vs Agent-First

### OpenClaw：Gateway 是一切的中心

OpenClaw 的整体架构可以用一句话概括：一个消息网关，内嵌了一个 AI 大脑。

```plain text
所有即时通讯平台
    ↓ (Channel Bridge 标准化消息)
Gateway (Node.js 长驻 Daemon)
    ↓ WebSocket ws://127.0.0.1:18789
Agent Runtime (pi SDK embedded)
    ↓ (LLM 推理 + Tool 执行)
技能系统 / 记忆 / 沙箱
```

Gateway 是一个单一的长驻进程，暴露 4 种事件类型：agent、chat、presence、health。所有客户端——macOS App、Telegram Bot、浏览器——都通过同一个 WebSocket 连接。

> 💡 关键设计：OpenClaw 内嵌了 pi SDK 作为 AI 大脑（pi 与 Claude Code 同一血统），自己只负责消息路由和状态管理。

```plain text
OpenClaw 提供：channels → gateway → routing → skills → memory → security
pi SDK 提供：  LLM loop → tool execution → streaming → session management
```

目录结构（核心模块）：

```plain text
openclaw/src/
├── agents/
│   ├── pi-embedded.ts           # 核心 Agent 编排循环
│   ├── pi-embedded-subscribe.ts # Agent 事件订阅
│   ├── agent-scope.ts           # Agent 配置解析
│   └── auth-profiles.ts         # OAuth 凭据管理
├── gateway/
│   ├── server.impl.ts           # Gateway 服务器
│   ├── boot.ts                  # 启动流程
│   └── protocol/                # 自研 WebSocket 协议 v3
└── infra/
    └── heartbeat-runner.ts      # 心跳（每 30 分钟）
```

### Hermes Agent：AIAgent 是一切的中心

Hermes 的架构是一个超级 Agent 类，适配了所有平台。

```plain text
用户输入（CLI / Telegram / Discord / API）
    ↓
HermesCLI.process_input() 或 Gateway.dispatch()
    ↓
AIAgent.run_conversation()        # 核心
    ├── prompt_builder.build_system_prompt()
    ├── runtime_provider.resolve()  # 18+ 模型提供商
    ├── API call（OpenAI / Anthropic / Codex 三种模式）
    ├── handle_function_call()      # 47 个工具
    └── session_db.save()           # SQLite + FTS5
```

目录结构：

```plain text
hermes-agent/
├── run_agent.py          # AIAgent 类 (~9,200 行)
├── cli.py                # HermesCLI (~8,500 行)
├── model_tools.py        # 工具编排 + _discover_tools()
├── hermes_state.py       # SessionDB (SQLite + FTS5)
├── agent/
│   ├── skill_commands.py # 技能斜杠命令
│   └── trajectory.py     # 轨迹保存
├── tools/
│   └── registry.py       # 工具注册表（无依赖，被所有模块导入）
├── skills/               # 内置技能
├── environments/         # RL 训练环境 (Atropos)
└── tests/                # ~3,000 个 Pytest 测试
```

---

## 四、Agent Loop 源码对比

### OpenClaw 的 Loop（TypeScript，run.ts）

```typescript
// src/agents/pi-embedded-runner/run.ts
while (true) {
  const attempt = await runEmbeddedAttempt({
    sessionId,
    sessionKey,
    prompt,
    model,
    tools,
    // ...
  });

  if (attempt.success) break;

  if (attempt.contextOverflow) {
    await compactSession();   // 上下文压缩后继续
    continue;
  }

  if (attempt.authError) {
    await rotateApiKey();     // 自动轮换 API Key
    continue;
  }

  break; // 其他错误退出
}
```

OpenClaw Loop 特点：

- 异步优先（async/await），充分利用 Node.js 事件循环
- 自动处理上下文溢出：compactSession() 压缩后继续，不中断任务
- 自动轮换 API Key，支持凭据池
- Loop 本身极简，复杂性下沉到 runEmbeddedAttempt()
### Hermes Agent 的 Loop（Python，run_agent.py）

```python
# run_agent.py - AIAgent.run_conversation()
while (api_call_count < self.max_iterations
       and self.iteration_budget.remaining > 0):

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tool_schemas
    )

    if response.tool_calls:
        for tool_call in response.tool_calls:
            result = handle_function_call(tool_call)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })
    else:
        return response.content  # 无工具调用 → 最终回复
```

Hermes Loop 特点：

- 完全同步（无 async/await），设计简洁，便于调试
- 双重退出条件：max_iterations（默认 90）+ iteration_budget
- 消息格式遵循 OpenAI 标准（role: system/user/assistant/tool）
- Reasoning 内容存入 assistant_msg["reasoning"]，保留思维链
### 核心差异总结

---

## 五、记忆系统：文件系统 vs SQLite+FTS5

### OpenClaw 的记忆系统

OpenClaw 的记忆以文件系统为基础：

- 对话历史：JSONL 文件
- 用户记忆：Markdown 文件（MEMORY.md 格式）
- 技能：目录结构（skill-name/SKILL.md + scripts/）
- 心跳驱动：heartbeat-runner.ts 每 30 分钟触发一次记忆整理
> 💡 设计哲学：一切可读、可审计、可编辑。记忆就是普通文件，用户随时可以打开 Finder/Explorer 查看和修改。

### Hermes Agent 的记忆系统

Hermes 使用 SQLite + FTS5 全文检索：

```python
# hermes_state.py - SessionDB
class SessionDB:
    # SQLite with FTS5 virtual table
    # 支持跨会话全文搜索
    # Sessions 有 lineage tracking（parent/child 关系）
    # LLM 辅助摘要：搜索结果由 LLM 自动总结
```

- FTS5 全文检索：可以搜索几个月前的对话内容
- Session Lineage：记录父子会话关系，支持分叉
- LLM 摘要：召回历史时自动用 LLM 提炼重点
- Honcho dialectic memory：用户画像随时间深化
---

## 六、技能/工具系统：声明式 vs 注册表模式

### OpenClaw 技能系统

```plain text
skill-name/
├── SKILL.md          # 元数据 + LLM 指令（必须）
├── pyproject.toml    # Python 依赖（可选）
└── scripts/          # 可执行脚本
```

- 三级加载：workspace 技能 → managed 技能 → bundled 技能（52 个内置）
- 依赖自检：技能声明依赖，若 gh 未安装则该技能不加载，不会产生"命令未找到"错误
- 沙箱执行：工具可在 Docker 容器内运行，限制爆炸半径
Hook 系统（TypeScript 事件处理器）：

```plain text
command:new → command:reset → gateway:startup
before_agent_start → agent_end
before_tool_call → after_tool_call
```

### Hermes Agent 工具系统

```python
# tools/registry.py（无依赖，被所有模块导入）
# 每个工具文件在 import 时自动注册：

# tools/your_tool.py
from tools.registry import registry

@registry.register(name="your_tool", toolset="dev")
def your_tool(param: str) -> dict:
    ...
```

- 47 个工具，分属 20 个 Toolset，按平台/场景按需启用
> 💡 自治技能创建（Hermes 独有）：完成复杂任务后，Agent 自动分析执行轨迹，提炼成可复用技能，下次遇到类似问题自动加载。这是 OpenClaw 没有的能力。

---

## 七、多模型支持与并发

### OpenClaw

通过 pi SDK 接入模型，配置文件切换：

```json
{
  "model": "anthropic/claude-opus-4-5"
}
```

- 支持多 Agent 实例，每个绑定不同 channel 和 personality
- Lane-based 并发：chat、cron、工具执行分属不同 lane
### Hermes Agent

- Provider Resolution 层支持 18+ 模型提供商
- 三种 API 模式：chat_completions / codex_responses / anthropic_messages
- 子 Agent 并行化：可 spawn 隔离 subagent 处理并行工作流
- 6 种 Terminal Backend：local、Docker、SSH、Daytona、Singularity、Modal
---

## 八、研究向能力（Hermes 的差异化优势）

Hermes Agent 内置了一套完整的 RL 训练管道，这是 OpenClaw 完全没有的：

```plain text
environments/        # Atropos RL 环境
batch_runner.py      # 批量轨迹生成
trajectory.py        # 轨迹压缩（用于训练下一代模型）
```

> 💡 这意味着：每次 Hermes Agent 完成任务，都可以选择保存轨迹，这些数据可以直接用于微调下一版 Hermes 模型。Agent 的使用过程本身就是数据飞轮。

---

## 九、部署模型对比

---

## 十、如何选择？

```plain text
你的核心需求是什么？
│
├── 多平台消息机器人 + 跑在家庭服务器/手机上
│   → 选 OpenClaw
│   原因：Gateway 架构天然支持多通道，TypeScript 生态稳定
│
├── 个人 AI 助手 + 想让 Agent 越用越聪明
│   → 选 Hermes Agent
│   原因：自动技能创建 + FTS5 记忆，真正的闭环学习
│
├── AI 研究 / 想用 Agent 生产训练数据
│   → 选 Hermes Agent
│   原因：内置 Atropos RL 环境 + 轨迹生成管道
│
└── 两个都想要？
    → 先用 Hermes（更易上手），成熟后迁移到 OpenClaw 的 Gateway 架构
    Hermes 官方支持一键导入 OpenClaw 的设置和记忆（~/.openclaw 自动检测）
```

---

## 结语

OpenClaw 和 Hermes Agent 代表了 2026 年开源 AI Agent 的两种主流路线：

OpenClaw 是基础设施优先——它先建了一个工业级的消息网关，再把 AI 塞进去。这让它在稳定性、并发处理、多平台支持上表现出色，但学习曲线较陡，TypeScript 生态对非前端开发者不够友好。

Hermes Agent 是能力优先——它先问"一个 AI Agent 应该能做什么"，再逐步补充基础设施。自我进化的技能系统和 RL 训练管道，让它成为目前最接近"真正学习"的开源 Agent。

> 💡 两者都是 MIT/Apache 开源，都在高速迭代。如果你只能选一个，今天（2026 年 4 月）的推荐是：从 Hermes Agent 开始，因为它更易上手，上限更高。

---

## References

1. OpenClaw GitHub Repository. https://github.com/openclaw/openclaw
1. Hermes Agent GitHub Repository (Nous Research). https://github.com/NousResearch/hermes-agent
1. Nous Research Official Site. https://nousresearch.com
1. Atropos RL Framework (Nous Research). https://github.com/NousResearch/atropos
1. OpenAI Chat Completions API Reference. https://platform.openai.com/docs/api-reference/chat
1. SQLite FTS5 Full-Text Search Extension Documentation. https://www.sqlite.org/fts5.html
[https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

