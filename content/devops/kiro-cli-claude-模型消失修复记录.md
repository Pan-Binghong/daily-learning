---
title: kiro-cli Claude 模型消失修复记录
date: '2026-06-16T02:13:00.000Z'
lastmod: '2026-06-16T02:28:00.000Z'
draft: false
tags:
- DevOps
- kiro
- 代理
categories:
- DevOps
---

日期：2026-06-11

## 问题现象

kiro-cli 输入 /model 后，Claude 系列模型全部消失，只剩开源模型（DeepSeek、MiniMax、Qwen3 等）。

## 根本原因

Kiro 在 2026 年 4-5 月将后端服务域名从旧的迁移到新的：

模型列表（configOptions）现在由 management.us-east-1.kiro.dev 下发。

本机 mihomo 代理配置中 amazonaws.com 有路由规则，但 kiro.dev 没有，导致新域名走"漏网之鱼"默认分组，连接异常，模型列表返回空。

## 修复方案

在 /home/pan/.config/mihomo/config.yaml 的 rules 区域添加规则：

```yaml
- 'DOMAIN-SUFFIX,kiro.dev,国外网站'
```

位置：rules 区域靠前，openai.com 规则之前。

然后通过 mihomo API 热重载配置：

```bash
curl -s -X PUT http://127.0.0.1:9090/configs \
  -H 'Content-Type: application/json' \
  -d '{"path":"/home/pan/.config/mihomo/config.yaml"}'
```

## 验证

重载后，在 kiro-cli 中输入 /model，Claude 系列模型应重新出现。

