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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFLZOCF2%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICYxEltwNAA2m%2FZiMh0R9SHya0wnB2k76Ja1o%2BwRqzhsAiEA9yITGIImXvCUEKqqBrGeGl11JOr2jG0ktK7v0DAwoCoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMgVbELhQXOV3egP4yrcAxhiJfSglvCsBBikT8lITdGegt390WnggOiM1fCZbbdE1BX3UBaR6Q9BUL1YJVA1vSactZMb79gTxEotmhO2H8fJC1Wsb70R%2Fz%2FiTpIFoNsATlzKnTbMfGvK8E14KH8VkbLPftfndsJ0%2BdnlzWZ7rBdBD26evfLht9X8dS2kyxI3kIysAcqyvDW%2F3x7QshcN0npsZ%2FocogwgmB2SB9ur02a9zI9qH1mbsub5J%2BB9YAsUUwtrggvi8ZY7i5LbpO6VzFO%2FIjghiqzOwQHEs8ht%2BSS%2BCYeGsIKnQZCYvjL9uoHk5V26DTqQNvO7%2FwWBUCRmmB73eDFERvH%2BBHPqWsve5qM%2Ba5FJj%2F4qm7tA9%2Fq8%2F9WOyFLD%2Fqkqshkhj8Aj6dO1ZCqe3qRQEUg2nwnq4JJg1YoPMiVWnzf848EAXNb%2FV%2FcCcrmj5PfdKxUt7aaa3aFGTRj6OxHLTpyiSKlrhjUq%2FiBNZSSr7czvQIwlh8QITjahiU2V5686lXmPPJfrozBhFPT2BkWJRbreWRZiTucYJE%2BGEv48F%2FsMv747XH7CDfdyPu66CyQUigLtCc1vBvjnJgqDPu8ajjtw2fVWC0MidA%2BvraMXjKE13faSwjBIPDzT3FZK23NjFiFop%2FL4MLbEqswGOqUB5yP%2FWrBIOQ%2B9%2BB7WOXN5ULG4OivpwwvG%2Fd3Og9SP6KtT%2B5q5mG4yXqQSDC15powTB6XrscZAbGO9423vLePUO2Tu8Snas1cwKunYwKnJpSKdYw%2F6laSVirB5ISQyIGhTf4j9FW3yFTZJF%2FuJ0GdwbY6zZ%2BZM3ccHhEDvyw1nS%2FIIzbG2VTjhkdee01d%2FqxV2VI%2FAne55C9wK0YnsHFSXoOdjrKyj&X-Amz-Signature=0f12f282620815cdc6de35490078f640144b8800184615d26607c7a0c4dff539&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFLZOCF2%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICYxEltwNAA2m%2FZiMh0R9SHya0wnB2k76Ja1o%2BwRqzhsAiEA9yITGIImXvCUEKqqBrGeGl11JOr2jG0ktK7v0DAwoCoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMgVbELhQXOV3egP4yrcAxhiJfSglvCsBBikT8lITdGegt390WnggOiM1fCZbbdE1BX3UBaR6Q9BUL1YJVA1vSactZMb79gTxEotmhO2H8fJC1Wsb70R%2Fz%2FiTpIFoNsATlzKnTbMfGvK8E14KH8VkbLPftfndsJ0%2BdnlzWZ7rBdBD26evfLht9X8dS2kyxI3kIysAcqyvDW%2F3x7QshcN0npsZ%2FocogwgmB2SB9ur02a9zI9qH1mbsub5J%2BB9YAsUUwtrggvi8ZY7i5LbpO6VzFO%2FIjghiqzOwQHEs8ht%2BSS%2BCYeGsIKnQZCYvjL9uoHk5V26DTqQNvO7%2FwWBUCRmmB73eDFERvH%2BBHPqWsve5qM%2Ba5FJj%2F4qm7tA9%2Fq8%2F9WOyFLD%2Fqkqshkhj8Aj6dO1ZCqe3qRQEUg2nwnq4JJg1YoPMiVWnzf848EAXNb%2FV%2FcCcrmj5PfdKxUt7aaa3aFGTRj6OxHLTpyiSKlrhjUq%2FiBNZSSr7czvQIwlh8QITjahiU2V5686lXmPPJfrozBhFPT2BkWJRbreWRZiTucYJE%2BGEv48F%2FsMv747XH7CDfdyPu66CyQUigLtCc1vBvjnJgqDPu8ajjtw2fVWC0MidA%2BvraMXjKE13faSwjBIPDzT3FZK23NjFiFop%2FL4MLbEqswGOqUB5yP%2FWrBIOQ%2B9%2BB7WOXN5ULG4OivpwwvG%2Fd3Og9SP6KtT%2B5q5mG4yXqQSDC15powTB6XrscZAbGO9423vLePUO2Tu8Snas1cwKunYwKnJpSKdYw%2F6laSVirB5ISQyIGhTf4j9FW3yFTZJF%2FuJ0GdwbY6zZ%2BZM3ccHhEDvyw1nS%2FIIzbG2VTjhkdee01d%2FqxV2VI%2FAne55C9wK0YnsHFSXoOdjrKyj&X-Amz-Signature=7987ae4407a844c86252c5c6cb5abc4f8f7eb069a3371fb0ed1287e3f6a4436e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFLZOCF2%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICYxEltwNAA2m%2FZiMh0R9SHya0wnB2k76Ja1o%2BwRqzhsAiEA9yITGIImXvCUEKqqBrGeGl11JOr2jG0ktK7v0DAwoCoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMgVbELhQXOV3egP4yrcAxhiJfSglvCsBBikT8lITdGegt390WnggOiM1fCZbbdE1BX3UBaR6Q9BUL1YJVA1vSactZMb79gTxEotmhO2H8fJC1Wsb70R%2Fz%2FiTpIFoNsATlzKnTbMfGvK8E14KH8VkbLPftfndsJ0%2BdnlzWZ7rBdBD26evfLht9X8dS2kyxI3kIysAcqyvDW%2F3x7QshcN0npsZ%2FocogwgmB2SB9ur02a9zI9qH1mbsub5J%2BB9YAsUUwtrggvi8ZY7i5LbpO6VzFO%2FIjghiqzOwQHEs8ht%2BSS%2BCYeGsIKnQZCYvjL9uoHk5V26DTqQNvO7%2FwWBUCRmmB73eDFERvH%2BBHPqWsve5qM%2Ba5FJj%2F4qm7tA9%2Fq8%2F9WOyFLD%2Fqkqshkhj8Aj6dO1ZCqe3qRQEUg2nwnq4JJg1YoPMiVWnzf848EAXNb%2FV%2FcCcrmj5PfdKxUt7aaa3aFGTRj6OxHLTpyiSKlrhjUq%2FiBNZSSr7czvQIwlh8QITjahiU2V5686lXmPPJfrozBhFPT2BkWJRbreWRZiTucYJE%2BGEv48F%2FsMv747XH7CDfdyPu66CyQUigLtCc1vBvjnJgqDPu8ajjtw2fVWC0MidA%2BvraMXjKE13faSwjBIPDzT3FZK23NjFiFop%2FL4MLbEqswGOqUB5yP%2FWrBIOQ%2B9%2BB7WOXN5ULG4OivpwwvG%2Fd3Og9SP6KtT%2B5q5mG4yXqQSDC15powTB6XrscZAbGO9423vLePUO2Tu8Snas1cwKunYwKnJpSKdYw%2F6laSVirB5ISQyIGhTf4j9FW3yFTZJF%2FuJ0GdwbY6zZ%2BZM3ccHhEDvyw1nS%2FIIzbG2VTjhkdee01d%2FqxV2VI%2FAne55C9wK0YnsHFSXoOdjrKyj&X-Amz-Signature=f9d6841634ccf4f617b4f9b240514df464d520f47cbc352c307e121dc9c9d294&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

