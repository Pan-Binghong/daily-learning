---
title: 强化学习中的 Rollout：从零理解这个核心概念
date: '2026-03-30T10:49:00.000Z'
lastmod: '2026-03-31T01:22:00.000Z'
draft: false
tags:
- Reinforcement Learning
- RLHF
- Training
categories:
- AI
---

# 一、先从一个比喻开始

想象你在训练一只小狗坐下。你发出指令，小狗做出反应，你给它奖励或不给。这个「发指令 → 小狗行动 → 给奖励」的过程重复很多次，小狗慢慢学会了正确行为。

强化学习（Reinforcement Learning，RL）的逻辑和这一模一样。而 Rollout，就是「让模型跑一遍、看它会怎么做」的这个过程。

# 二、强化学习的基本框架

要理解 Rollout，先要了解 RL 的五个核心概念：

- 智能体（Agent）：做决策的主体（模型、机器人等）
- 环境（Environment）：智能体所处的世界
- 状态（State，s）：当前的情况描述
- 动作（Action，a）：智能体做出的选择
- 奖励（Reward，r）：做出该动作后获得的反馈信号
智能体的目标：选择动作，最大化长期累计奖励。

# 三、什么是 Rollout？

Rollout（也叫 trajectory，轨迹）指的是智能体与环境交互的一段完整序列：

```plain text
s₀ → a₀ → r₀ → s₁ → a₁ → r₁ → s₂ → a₂ → r₂ → ... → sT
```

翻译成人话就是：从某个初始状态出发，智能体不断做决策、获得奖励、进入下一个状态，直到任务结束（或达到最大步数）。这一整条链，就是一次 Rollout。

几个例子：

- 打一局围棋（从开局到分出胜负）= 一次 Rollout
- 玩一局 Atari 游戏 = 一次 Rollout
- 让语言模型回答一个问题（从收到问题到生成完整回复）= 一次 Rollout
# 四、Rollout 在训练中起什么作用？

训练一个 RL 模型的基本流程是：

```plain text
1. 执行 Rollout（让模型跑一遍，收集数据）
      ↓
2. 计算回报（这次 Rollout 总共获得了多少奖励？）
      ↓
3. 更新模型参数（做得好的行为提高概率；做得差的降低概率）
      ↓
4. 重复
```

Rollout 是整个训练循环的数据来源。没有 Rollout，模型就没有「经验」可学。

![](https://images.pexels.com/photos/7267546/pexels-photo-7267546.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200)

## 回报（Return）的计算

一次 Rollout 中，每一步都有奖励 r₀, r₁, r₂...。总回报通常用折扣累计奖励表示：

```plain text
G = r₀ + γ·r₁ + γ²·r₂ + ...
```

其中 γ（gamma，折扣因子，通常取 0.9~0.99）表示「越近的奖励越重要」。γ 越小，模型越短视；γ 越大，模型越有长远规划。

# 五、On-Policy vs Off-Policy Rollout

这是 RL 中一个重要区别，关系到 Rollout 数据能不能被复用：

- On-Policy（同策略）：用当前版本的模型收集 Rollout，立即用于更新，更新后旧数据就过期。代表算法：PPO、TRPO。
- Off-Policy（异策略）：可以用旧版本模型收集的 Rollout 来更新，数据可以存入 Replay Buffer 复用。代表算法：DQN、SAC。
On-Policy 更稳定但数据效率低（每次都要重新采样）；Off-Policy 数据效率高但训练可能不稳定。LLM 的强化训练通常用 On-Policy 方法（如 PPO），因为稳定性更重要。

# 六、Rollout 在大语言模型训练中（RLHF）

这是近年来最热门的应用场景。训练 ChatGPT、Claude 这类模型时，都用到了强化学习，其中 Rollout 的概念稍有特殊。

## 语言模型的 Rollout 是什么样的？

在 LLM 的 RL 训练中，将文本生成过程映射到 RL 框架：

- 状态（State） = 当前的对话上下文（已经生成的 token 序列）
- 动作（Action） = 生成下一个 token
- 一次 Rollout = 从问题开始，逐 token 生成，直到输出完整回复
```plain text
问题: "帮我解释量子纠缠"
  ↓
生成 token₁: "量"
生成 token₂: "子"
生成 token₃: "纠"
...
生成 tokenN: [结束符]
  ↓
完整回复 = 一次 Rollout
```

## 奖励从哪里来？

在 RLHF（基于人类反馈的强化学习）中：

1. 人类标注员对模型的多个回答进行排名
1. 用这些排名训练一个奖励模型（Reward Model）
1. 奖励模型对每次 Rollout（即每个完整回复）打一个分数
1. 用这个分数作为奖励，通过 PPO 等算法更新语言模型
## 现代 LLM 训练（GRPO / DeepSeek-R1 等）

在推理模型的训练中，Rollout 更加关键：

![](https://images.pexels.com/photos/18069695/pexels-photo-18069695.png?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200)

- 对同一个问题，模型同时生成多个 Rollout（多条回复，通常 8~16 条）
- 对这些回复打分（比如数学题对不对、推理链是否正确）
- 用组内相对分数指导模型更新：比组内平均分高的回复概率提高，低的概率降低
这个方法叫 GRPO（Group Relative Policy Optimization），Rollout 的质量和数量直接影响训练效果。DeepSeek-R1 的推理能力正是通过大量 Rollout 的强化训练获得的。

# 七、多个并行 Rollout

实际训练中，为了效率，通常同时运行多个 Rollout（并行采样）：

```plain text
问题 1 → Rollout 1a, 1b, 1c, 1d（4个不同回复）
问题 2 → Rollout 2a, 2b, 2c, 2d
...
收集一批后，统一计算奖励、统一更新模型
```

这批批量数据叫做 Rollout Buffer（经验缓冲区）。收集满 Buffer 后，用 mini-batch 方式多轮更新模型参数，然后丢弃这批数据，重新采样新的 Rollout。

# 八、总结：Rollout 一句话定义

![](https://images.pexels.com/photos/17489150/pexels-photo-17489150.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200)

> Rollout = 让智能体（或语言模型）从头到尾执行一次完整的决策序列，收集（状态、动作、奖励）数据，用于训练。

它是强化学习训练的核心引擎：没有 Rollout，就没有经验；没有经验，就无法学习。

在 LLM 时代，Rollout 的概念从「游戏里打一局」扩展到了「模型生成一段回复」，但本质是一样的——让模型先「试一试」，再根据结果好坏来调整它的行为。

---

# 参考文献

---

[https://arxiv.org/abs/1707.06347](https://arxiv.org/abs/1707.06347)

[https://arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155)

[https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948)

[https://arxiv.org/abs/2005.07759](https://arxiv.org/abs/2005.07759)

