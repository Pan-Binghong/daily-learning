---
title: Kiro 操作技巧指南
date: '2026-03-30T14:40:00.000Z'
lastmod: '2026-03-30T14:58:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

# Kiro 操作技巧指南

Kiro 是 Amazon/AWS 推出的 AI IDE，基于 VS Code 构建。其核心设计理念是「规格驱动开发」——在写代码之前，先把需求、设计和任务梳理清楚，再交由 AI 辅助实现。本文整理了围绕 Kiro 四大核心特性（Specs、Hooks、Agents、Steering files）的实用操作技巧。

> 💡 本文内容基于 Kiro 已公开的功能文档，仅描述已有据可查的特性，不包含猜测或未经验证的功能。

---

# 一、Specs（规格驱动开发）

Specs 是 Kiro 最具特色的功能，强制你在动手写代码前先完成三份文档：需求文档（requirements）、设计文档（design）、任务清单（tasks）。这种方式让 AI 拥有充分的上下文，从而减少后期返工。

## 1.1 三阶段工作流

- Requirements（需求）：用自然语言描述你要构建的功能，AI 会将其转化为结构化的需求条目（通常是 EARS 格式或类似的用户故事格式）。
- Design（设计）：基于需求，AI 生成技术设计方案，包括数据模型、组件关系、接口定义等。你可以在这一步修改设计，再进入下一阶段。
- Tasks（任务）：AI 将设计拆解为具体的编码任务列表，每个任务对应实际的代码变更。可逐条执行，也可批量执行。
## 1.2 操作技巧

> 💡 在 Requirements 阶段，描述越具体越好。包含边界条件、错误处理预期和非功能性需求（性能、安全等），可以显著提升后续 Design 和 Tasks 的质量。

- 不要跳过 Design 审查：AI 生成的设计文档需要人工确认，尤其是数据库 schema 和 API 契约，这些决策一旦进入 Tasks 阶段就难以回头。
- Tasks 可以部分执行：如果对某个任务的实现方式存疑，可以先跳过该任务，手动实现后再继续执行后续任务。
- Spec 文件存储在项目的 .kiro/specs/ 目录下，是普通的 Markdown 文件，可以用 Git 进行版本控制和团队协作。
```plain text
.kiro/
  specs/
    user-auth/
      requirements.md
      design.md
      tasks.md
    payment-system/
      requirements.md
      design.md
      tasks.md
```

---

# 二、Hooks（钩子）

Hooks 是 Kiro 的自动化机制，允许你在特定事件发生时（如文件保存、文件变更）自动触发 AI 执行预定义的操作。常见场景包括：保存代码后自动更新文档、修改 API 后自动同步测试用例、代码变更后自动检查一致性等。

## 2.1 Hook 的工作原理

Hook 配置文件存储在 .kiro/hooks/ 目录下。每个 Hook 定义了触发条件（trigger）和要执行的 prompt 或操作（action）。当触发条件满足时，Kiro 会自动调用 AI Agent 执行对应的任务。

## 2.2 常用 Hook 场景

- 文档同步：修改源代码文件后，自动更新对应的 README 或 API 文档。
- 测试生成：新增或修改函数后，自动生成或更新对应的单元测试。
- 一致性检查：修改数据模型后，提示检查相关的序列化/反序列化代码是否需要同步更新。
## 2.3 操作技巧

> 💡 Hook 的 prompt 应该聚焦且范围明确。避免写「检查整个项目是否有问题」这类模糊指令，改为「检查刚修改的文件中，函数签名是否与调用方一致」。

- 控制触发范围：通过 glob 模式限定 Hook 只对特定目录或文件类型生效，避免每次保存都触发不必要的 AI 调用。
- 保持 Hook 幂等：Hook 执行的操作应该可以安全地重复执行，不应该在每次触发时都追加内容而非替换内容。
- Hook 配置文件同样是普通文本文件，可通过 Git 管理，便于团队共享自动化规则。
```plain text
.kiro/
  hooks/
    sync-docs.md       # 代码变更后同步文档
    update-tests.md    # 函数修改后更新测试
```

---

# 三、Agents（智能体）

Kiro 的 Agents 能够执行复杂的多步骤任务，比普通的代码补全或单轮对话更强大。Agent 可以读取文件、修改代码、运行命令、调用工具，并在多个步骤之间保持上下文，直到完成目标。

## 3.1 Agent 的能力边界

- 文件操作：读取、创建、修改项目文件。
- 终端执行：运行 shell 命令（如安装依赖、执行测试、编译构建）。
- 多步推理：将复杂任务拆解为子任务，按顺序或并行执行。
- 工具调用：根据配置调用外部工具或 MCP 服务。
## 3.2 与 Specs 配合使用

Specs 的 Tasks 阶段本质上就是在调度 Agent。每个 Task 条目都是一个 Agent 任务，Kiro 会依次或按需将这些任务交给 Agent 执行。这意味着你通过 Spec 控制的是高层意图，Agent 负责具体实现。

## 3.3 操作技巧

> 💡 对于涉及生产环境或不可逆操作的任务（如数据库迁移、删除文件），在 Agent 执行前务必进行人工确认，不要设置全自动模式。

- 任务粒度要适中：单个 Agent 任务不宜过大（如「重构整个后端」），建议控制在「修改某个模块的某个功能」级别，让 Agent 有清晰的完成标准。
- 提供足够的上下文：在任务描述中明确「需要读取哪些文件」「输出应该满足什么条件」，帮助 Agent 快速定位工作范围。
- 利用 Agent 做代码审查辅助：让 Agent 基于已有的 Steering files 和 Specs 检查新提交的代码是否符合项目规范。
> 💡 Kiro Agent 执行任务时会显示执行步骤和使用的工具，保持对 Agent 行为的可观测性，遇到异常可以随时中断。

---

# 四、Steering Files（引导文件）

Steering files 类似于其他 AI 编程工具中的 CLAUDE.md 或 .cursorrules，用于持久化地告诉 AI 关于这个项目的背景信息、编码规范和偏好。放置在 .kiro/steering/ 目录下，每次 AI 处理任务时都会自动参考这些文件。

## 4.1 Steering Files 的典型内容

- 项目概述：项目是什么、技术栈选型、主要模块划分。
- 编码规范：命名约定、代码风格、注释要求、禁止的模式。
- 架构决策：关键的设计决定及其原因（ADR，架构决策记录）。
- 外部依赖说明：使用了哪些第三方服务、它们的用途和限制。
- 禁止事项：AI 不应该修改的文件、不应该使用的库、不应该引入的模式。
## 4.2 Steering Files 结构示例

```markdown
# 项目概述
本项目是一个 FastAPI 后端服务，提供用户管理和订单处理功能。

## 技术栈
- Python 3.11+
- FastAPI + Pydantic v2
- PostgreSQL（通过 SQLAlchemy 2.0 ORM）
- Redis（用于缓存和会话）

## 编码规范
- 所有 API 路由使用 async/await
- 数据库操作必须使用 Repository 模式，禁止在路由层直接操作数据库
- 错误处理统一使用自定义 AppException 类
- 所有公共函数必须有类型注解

## 禁止事项
- 不要修改 alembic/versions/ 下的迁移文件
- 不要引入 Django 或 Flask 依赖
- 不要在代码中硬编码任何凭据
```

## 4.3 操作技巧

> 💡 Steering files 是投资回报率最高的配置。花 30 分钟写好一份详细的 steering file，可以让后续所有 AI 操作都少踩坑，特别是在多人协作项目中统一 AI 的行为。

- 可以拆分为多个文件：不必把所有内容塞进一个文件，可以按主题拆分（如 coding-style.md、architecture.md、dependencies.md），Kiro 会读取整个目录下的所有文件。
- 保持更新：项目架构演进时同步更新 steering files，过时的指导信息比没有指导信息更危险。
- 用「禁止」代替「建议」：AI 对明确的否定指令（不要做X）的遵从率高于软性建议（最好做Y）。
```plain text
.kiro/
  steering/
    product.md         # 产品背景和用户群
    tech-stack.md      # 技术栈和版本要求
    coding-style.md    # 编码规范
    architecture.md    # 架构决策记录
    dos-and-donts.md   # 明确的规定和禁止项
```

---

# 五、四大特性协作使用

Kiro 的四大特性不是孤立存在的，它们共同构成了一个完整的 AI 辅助开发工作流：

- Steering files 提供持久化的项目上下文，让 AI 始终了解项目背景和规范。
- Specs 在每个功能开发前对齐需求和设计，减少方向性错误。
- Agents 基于 Specs 的 Tasks 执行具体编码工作，遵循 Steering files 的规范约束。
- Hooks 在开发过程中保持代码和文档的自动同步，减少手动维护成本。
## 推荐的项目初始化顺序

- 第一步：创建 Steering files，记录项目背景、技术栈和核心规范。
- 第二步：为第一个功能创建 Spec，完成 Requirements → Design → Tasks 三阶段。
- 第三步：让 Agent 执行 Tasks，过程中持续审查每个步骤的输出。
- 第四步：配置 Hooks，自动化高频重复任务（如文档同步、测试更新）。
---

# 六、与其他 AI IDE 的对比

Kiro 与 Cursor、GitHub Copilot、Claude Code 等工具的最大区别在于其「规格优先」的设计哲学。其他工具更侧重于即时的代码补全和对话式编辑，而 Kiro 强制要求在编码前先完成需求和设计，更适合功能较为复杂、需要多步骤实现的场景。

> 💡 Kiro 的 Specs 机制特别适合「不知道从哪里开始」的场景：只需用自然语言描述想要的功能，Kiro 会帮你把模糊的想法转化为结构化的开发计划。

