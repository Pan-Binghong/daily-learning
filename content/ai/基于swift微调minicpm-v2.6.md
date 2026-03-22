---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVMQGQZL%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDX3pb91S9yvtRKPg2BpkNY1SJzhREXntGuFUmRN8HeRQIgZlZp6hOxA8ySewSmcZEQW4SJwLd0JE76JqyqTOZEEZEq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDHfp7g5v5op0ueVKJCrcAwF%2FX%2BMtKgGtcZ95u65URG4%2FYg9Da7Y9PmvP7C52Fp%2F%2FfcV2oG6cxBiYQtP9o%2BfawMEzELBlqAud6tQJCiutISNKuNkRMo5IRvoUGon85fA1jZa0vVPuOzhGC3cpejEddPzDSKEsem24lnOmk6KRl0nVFR4M25BB3KVlwSGIqb4cMoAK6xTxePB%2Fzm10nAVPmzd4UTsvI94kowBGmbs386pkkxYLdpjodorHblFojj4bbTymXG77%2BWSAKoEwHIz4x%2Fe1eOC1vagJhBPSQf%2BA7pUzU72TZEdaJ4FbMWivsE8cN74TanOQ5OToGVx81MElM1fdZAvPh%2BQ%2F9cx%2FJw8MUadDSa1SarBTkAXQs4m2b%2FAxo3lpqGrjBZukxtk6RVDDv6tGyPoTl%2FsQkMCFwwH8E3n9U5SHweVO4BYDZu4Hid4JGQocM66LGt856grPRaaKF%2BnTvVDfdykJF2RwGXTUsomMxLsyIBVoSHZ%2Ft%2BVsfcnFhAJ5Pt%2BxM8kE%2FHXnDqvY62uKEv781ZXWbfVGgVynk7KAcks7q1wSczGEktSYHMA3utagvhplYPYfRlBmdzVkHCBvyYBioo4i1rfjkfU1%2Fq6%2FkLqMkfDdDEqWULeIh3ilQ2iOdcgA2LVadFZlMOGs%2Fc0GOqUB1QOull7Vb4e6jE4vctnYmEjlLf8sW0hmWJWMkXy4jXJsfeVpGUK602P39RhuN0Mr8Szdo59hNMqYhyjQK6nX0QehcOM8nVj6UaCGepxOmxdc6be53%2BSQgG7ByBouLAnXE76sT%2BHpJoMrXeX%2FbrbmFWrtYCRG%2BEttzXaog3ZNTLwoF4OC7Zx7E8cI%2FytHOJe6EtkAxMaiVZNOrZ2lm%2BCTVUMgrNlw&X-Amz-Signature=c2c1f86128442ef51d009ae7bd98cac8bec5dbe1314d4bc1322dc873591d17cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVMQGQZL%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDX3pb91S9yvtRKPg2BpkNY1SJzhREXntGuFUmRN8HeRQIgZlZp6hOxA8ySewSmcZEQW4SJwLd0JE76JqyqTOZEEZEq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDHfp7g5v5op0ueVKJCrcAwF%2FX%2BMtKgGtcZ95u65URG4%2FYg9Da7Y9PmvP7C52Fp%2F%2FfcV2oG6cxBiYQtP9o%2BfawMEzELBlqAud6tQJCiutISNKuNkRMo5IRvoUGon85fA1jZa0vVPuOzhGC3cpejEddPzDSKEsem24lnOmk6KRl0nVFR4M25BB3KVlwSGIqb4cMoAK6xTxePB%2Fzm10nAVPmzd4UTsvI94kowBGmbs386pkkxYLdpjodorHblFojj4bbTymXG77%2BWSAKoEwHIz4x%2Fe1eOC1vagJhBPSQf%2BA7pUzU72TZEdaJ4FbMWivsE8cN74TanOQ5OToGVx81MElM1fdZAvPh%2BQ%2F9cx%2FJw8MUadDSa1SarBTkAXQs4m2b%2FAxo3lpqGrjBZukxtk6RVDDv6tGyPoTl%2FsQkMCFwwH8E3n9U5SHweVO4BYDZu4Hid4JGQocM66LGt856grPRaaKF%2BnTvVDfdykJF2RwGXTUsomMxLsyIBVoSHZ%2Ft%2BVsfcnFhAJ5Pt%2BxM8kE%2FHXnDqvY62uKEv781ZXWbfVGgVynk7KAcks7q1wSczGEktSYHMA3utagvhplYPYfRlBmdzVkHCBvyYBioo4i1rfjkfU1%2Fq6%2FkLqMkfDdDEqWULeIh3ilQ2iOdcgA2LVadFZlMOGs%2Fc0GOqUB1QOull7Vb4e6jE4vctnYmEjlLf8sW0hmWJWMkXy4jXJsfeVpGUK602P39RhuN0Mr8Szdo59hNMqYhyjQK6nX0QehcOM8nVj6UaCGepxOmxdc6be53%2BSQgG7ByBouLAnXE76sT%2BHpJoMrXeX%2FbrbmFWrtYCRG%2BEttzXaog3ZNTLwoF4OC7Zx7E8cI%2FytHOJe6EtkAxMaiVZNOrZ2lm%2BCTVUMgrNlw&X-Amz-Signature=e43521b3f3d1ed40c0ee2df59275d203995839dff5dbaf3f57c0cbf284339536&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVMQGQZL%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDX3pb91S9yvtRKPg2BpkNY1SJzhREXntGuFUmRN8HeRQIgZlZp6hOxA8ySewSmcZEQW4SJwLd0JE76JqyqTOZEEZEq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDHfp7g5v5op0ueVKJCrcAwF%2FX%2BMtKgGtcZ95u65URG4%2FYg9Da7Y9PmvP7C52Fp%2F%2FfcV2oG6cxBiYQtP9o%2BfawMEzELBlqAud6tQJCiutISNKuNkRMo5IRvoUGon85fA1jZa0vVPuOzhGC3cpejEddPzDSKEsem24lnOmk6KRl0nVFR4M25BB3KVlwSGIqb4cMoAK6xTxePB%2Fzm10nAVPmzd4UTsvI94kowBGmbs386pkkxYLdpjodorHblFojj4bbTymXG77%2BWSAKoEwHIz4x%2Fe1eOC1vagJhBPSQf%2BA7pUzU72TZEdaJ4FbMWivsE8cN74TanOQ5OToGVx81MElM1fdZAvPh%2BQ%2F9cx%2FJw8MUadDSa1SarBTkAXQs4m2b%2FAxo3lpqGrjBZukxtk6RVDDv6tGyPoTl%2FsQkMCFwwH8E3n9U5SHweVO4BYDZu4Hid4JGQocM66LGt856grPRaaKF%2BnTvVDfdykJF2RwGXTUsomMxLsyIBVoSHZ%2Ft%2BVsfcnFhAJ5Pt%2BxM8kE%2FHXnDqvY62uKEv781ZXWbfVGgVynk7KAcks7q1wSczGEktSYHMA3utagvhplYPYfRlBmdzVkHCBvyYBioo4i1rfjkfU1%2Fq6%2FkLqMkfDdDEqWULeIh3ilQ2iOdcgA2LVadFZlMOGs%2Fc0GOqUB1QOull7Vb4e6jE4vctnYmEjlLf8sW0hmWJWMkXy4jXJsfeVpGUK602P39RhuN0Mr8Szdo59hNMqYhyjQK6nX0QehcOM8nVj6UaCGepxOmxdc6be53%2BSQgG7ByBouLAnXE76sT%2BHpJoMrXeX%2FbrbmFWrtYCRG%2BEttzXaog3ZNTLwoF4OC7Zx7E8cI%2FytHOJe6EtkAxMaiVZNOrZ2lm%2BCTVUMgrNlw&X-Amz-Signature=3df7ab3efa0745f85b3ef5f3a6fee9025debd6331098cfdf5608c9a8e429fcfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

