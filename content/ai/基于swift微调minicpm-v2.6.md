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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TPZNZWP%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQDzcDOlRyZzgzO39yZOKabcZ%2BiTTtZ1%2B4k7bTLfNK7BrgIhAPH3q0WwVZs%2B9CcWoYXDFDD6xps0WSk3kGe%2FkKWsd4mSKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzW%2Bd%2B9EPglxSQbh%2F8q3AN22VfOYN2HeiRrwonrRuEsGsCt5UJq2GwkJQpYj0vKu0%2FMQkvdw%2BV0mCmWOdxvGSB1BqB1kcZzcxmQ8YK4k1XLIZtkXhH30InHhhAwej9I10fK3m5phtPzcdr5uXP5FAlLp6hQ1pcLs8tkDuFQupwlxv9mzoVQWzr5cQjrxzOkrvhXKVZcIIjbmWF3B1985uri%2Bhp2oXkQzJmtWQSs9Z5GSs1ynva06yDR05QHGkzSUGHyPODHQY69ElywNzKcqtMcr8W%2BqDZNZuALpfbYVmR2qaRAB1seEfq0rbNCrQSD%2B19uUNVFVknrX5Dy9kE63WCfC%2F4dlpSpruRfZfgTYy%2FVDwSFptoImLPsn2KgqEk3G4iOzlANvG8timejtRMzV0XFjtjyH9eVm%2FAz1TQqltgtbE8VAGQEio%2FTrnU7UscwbtXjes52PsLvbGuVjeq78RXglJRNSOpbJzi%2FjLOCEPrx62G8w64bc7m8j2yDvAHbCNaTUWxrpqWWlGTqlxYh5xcpA5XzirSPceblJE4I9kQ6a4pmqxBNomAoXaD9a%2BDgJqDnSsVqB4g%2BaquRrfS1UYu7o8UkAWwHSqetOjLrdahjfBRlP%2BToDhUWnIGbQaHeM65BT4z1qBxvq7L%2BcjDp2IXMBjqkAfF5hek9A9i6zyH5p6gtHRbFVFLPs8u%2BzH65umJ1F6DYla%2BdMbktvEiAL9XrRS7nbmDh8PI0C9lDjqMM1T06Sfpkjmrxq%2BYtAmjHhHQzJepUwgCw52wTSJzBmGXjJeYDjska1TTiEf%2Bm7ZUGxIkkFqKejeUY%2F6zHxNrMDDuZ6E663DvbeSsTMJXIaI1A%2BdFB9LeBa88qoDbhmhXIfC%2FgnbeHAwym&X-Amz-Signature=3a03a31813b16dde9b73113778a136d46795cb37a446ef1d604272eefdb0654d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TPZNZWP%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQDzcDOlRyZzgzO39yZOKabcZ%2BiTTtZ1%2B4k7bTLfNK7BrgIhAPH3q0WwVZs%2B9CcWoYXDFDD6xps0WSk3kGe%2FkKWsd4mSKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzW%2Bd%2B9EPglxSQbh%2F8q3AN22VfOYN2HeiRrwonrRuEsGsCt5UJq2GwkJQpYj0vKu0%2FMQkvdw%2BV0mCmWOdxvGSB1BqB1kcZzcxmQ8YK4k1XLIZtkXhH30InHhhAwej9I10fK3m5phtPzcdr5uXP5FAlLp6hQ1pcLs8tkDuFQupwlxv9mzoVQWzr5cQjrxzOkrvhXKVZcIIjbmWF3B1985uri%2Bhp2oXkQzJmtWQSs9Z5GSs1ynva06yDR05QHGkzSUGHyPODHQY69ElywNzKcqtMcr8W%2BqDZNZuALpfbYVmR2qaRAB1seEfq0rbNCrQSD%2B19uUNVFVknrX5Dy9kE63WCfC%2F4dlpSpruRfZfgTYy%2FVDwSFptoImLPsn2KgqEk3G4iOzlANvG8timejtRMzV0XFjtjyH9eVm%2FAz1TQqltgtbE8VAGQEio%2FTrnU7UscwbtXjes52PsLvbGuVjeq78RXglJRNSOpbJzi%2FjLOCEPrx62G8w64bc7m8j2yDvAHbCNaTUWxrpqWWlGTqlxYh5xcpA5XzirSPceblJE4I9kQ6a4pmqxBNomAoXaD9a%2BDgJqDnSsVqB4g%2BaquRrfS1UYu7o8UkAWwHSqetOjLrdahjfBRlP%2BToDhUWnIGbQaHeM65BT4z1qBxvq7L%2BcjDp2IXMBjqkAfF5hek9A9i6zyH5p6gtHRbFVFLPs8u%2BzH65umJ1F6DYla%2BdMbktvEiAL9XrRS7nbmDh8PI0C9lDjqMM1T06Sfpkjmrxq%2BYtAmjHhHQzJepUwgCw52wTSJzBmGXjJeYDjska1TTiEf%2Bm7ZUGxIkkFqKejeUY%2F6zHxNrMDDuZ6E663DvbeSsTMJXIaI1A%2BdFB9LeBa88qoDbhmhXIfC%2FgnbeHAwym&X-Amz-Signature=c04248d1867ed879fac13d8430c8b742f915fb183ea91eb89aa531b2e29696b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TPZNZWP%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQDzcDOlRyZzgzO39yZOKabcZ%2BiTTtZ1%2B4k7bTLfNK7BrgIhAPH3q0WwVZs%2B9CcWoYXDFDD6xps0WSk3kGe%2FkKWsd4mSKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzW%2Bd%2B9EPglxSQbh%2F8q3AN22VfOYN2HeiRrwonrRuEsGsCt5UJq2GwkJQpYj0vKu0%2FMQkvdw%2BV0mCmWOdxvGSB1BqB1kcZzcxmQ8YK4k1XLIZtkXhH30InHhhAwej9I10fK3m5phtPzcdr5uXP5FAlLp6hQ1pcLs8tkDuFQupwlxv9mzoVQWzr5cQjrxzOkrvhXKVZcIIjbmWF3B1985uri%2Bhp2oXkQzJmtWQSs9Z5GSs1ynva06yDR05QHGkzSUGHyPODHQY69ElywNzKcqtMcr8W%2BqDZNZuALpfbYVmR2qaRAB1seEfq0rbNCrQSD%2B19uUNVFVknrX5Dy9kE63WCfC%2F4dlpSpruRfZfgTYy%2FVDwSFptoImLPsn2KgqEk3G4iOzlANvG8timejtRMzV0XFjtjyH9eVm%2FAz1TQqltgtbE8VAGQEio%2FTrnU7UscwbtXjes52PsLvbGuVjeq78RXglJRNSOpbJzi%2FjLOCEPrx62G8w64bc7m8j2yDvAHbCNaTUWxrpqWWlGTqlxYh5xcpA5XzirSPceblJE4I9kQ6a4pmqxBNomAoXaD9a%2BDgJqDnSsVqB4g%2BaquRrfS1UYu7o8UkAWwHSqetOjLrdahjfBRlP%2BToDhUWnIGbQaHeM65BT4z1qBxvq7L%2BcjDp2IXMBjqkAfF5hek9A9i6zyH5p6gtHRbFVFLPs8u%2BzH65umJ1F6DYla%2BdMbktvEiAL9XrRS7nbmDh8PI0C9lDjqMM1T06Sfpkjmrxq%2BYtAmjHhHQzJepUwgCw52wTSJzBmGXjJeYDjska1TTiEf%2Bm7ZUGxIkkFqKejeUY%2F6zHxNrMDDuZ6E663DvbeSsTMJXIaI1A%2BdFB9LeBa88qoDbhmhXIfC%2FgnbeHAwym&X-Amz-Signature=71f8c2efc4a2a5995492ebfcf57bd188d97f274b993d23eb80b60c4ab6bce8bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

