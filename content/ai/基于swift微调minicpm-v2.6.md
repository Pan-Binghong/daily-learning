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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642RITZJ5%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T033837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIFdZekgFz2OzHKARUjTIFuQgDN9TVP26%2F5QLdOPQxswaAiEAl6JTJZMIZY%2FQ7sqM%2BT9aoYsbeUALQTqkxdQ7WaNJu8AqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIeON1mRyW044dsyrcA6TDrBvPZKVxe5MD8uM3W%2By5%2BuVjWJ5JqTSdMD4Yo%2Blj78cuE0ek3aqlqEslbwJoga55J9DwEoHRnO8e%2Fj5zQG706J51ZQd6jHjxO0Yh5xnx52631sv6u32pcYm%2BRcT%2B5VVP8YRxaaew5C0kZZVBhQuUaK%2B7%2BK1zIS9%2FU70DXAIFbzKzToMJoDXRXuE3PZFtxQB%2FBHYwzSwiqflFy89Kqnj8iDdfl3o27pQN2umbR6CS%2FVrSh2GzVCBcNOGe%2BPfPq9Xa0ddEjqTPZqcJ6ECMIfnt6aEWqFyL3jsHbdOJ5uMM1ECvMSNghEbZZ9vLG%2FHVVu2b%2Bqop%2FRkXCu%2BVAM8skfxugAT%2BrA0gSmFqx5CNu3YIpXPxPk7kE1Cua%2FjfXwPi6FcfZeFZV8BY22tnYDtCj%2F0DMG3CLBVw%2FCWJF4kPKtCiaIVIUYfIAfFrwREYG%2BTUt%2BF6x%2BNSK%2BkQ4wNQMdov%2BqH2tdK8JOK1BHyR5ZFBx3dzJcQDHMvojt%2BFZCAnSOoQQvwxWU%2F1mchcZMNfV79%2Fr2Qu7yjEd8DuRgCILsVyuvFa8j81GugYfI0jy%2BGuSabl%2FaK%2Bkuz9dm%2F1eR2Eyf%2BV4jIDaGY4IcEmStTnHeataWphI%2FZfN8zQVE9AmaHMMOfsnM4GOqUBdC67buO7RTxMaAHALZW1wLMM3TEsNX%2Bh3lnmluqJ6x78tnyf0shlVMWYU0zHyfVgjDjmq%2Fkzh%2BaHfVJDijwTziPHwVOSQpbZe1YW55CbCYqZROXwOUXiLwSmX2%2B%2BdEdgNugxPGjodrjcgp1ky%2FWQ0JSN9MKNkJCrmS9x8%2BO27L%2B8AV8vf8mIEcWzPpACoyxars2sJE20E%2BpYxXp5n0zIj%2BM46U84&X-Amz-Signature=fd41e3391e8c1d96889592b4e09e76a47d7ae8363541f5a003743dbe4725576e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642RITZJ5%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T033837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIFdZekgFz2OzHKARUjTIFuQgDN9TVP26%2F5QLdOPQxswaAiEAl6JTJZMIZY%2FQ7sqM%2BT9aoYsbeUALQTqkxdQ7WaNJu8AqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIeON1mRyW044dsyrcA6TDrBvPZKVxe5MD8uM3W%2By5%2BuVjWJ5JqTSdMD4Yo%2Blj78cuE0ek3aqlqEslbwJoga55J9DwEoHRnO8e%2Fj5zQG706J51ZQd6jHjxO0Yh5xnx52631sv6u32pcYm%2BRcT%2B5VVP8YRxaaew5C0kZZVBhQuUaK%2B7%2BK1zIS9%2FU70DXAIFbzKzToMJoDXRXuE3PZFtxQB%2FBHYwzSwiqflFy89Kqnj8iDdfl3o27pQN2umbR6CS%2FVrSh2GzVCBcNOGe%2BPfPq9Xa0ddEjqTPZqcJ6ECMIfnt6aEWqFyL3jsHbdOJ5uMM1ECvMSNghEbZZ9vLG%2FHVVu2b%2Bqop%2FRkXCu%2BVAM8skfxugAT%2BrA0gSmFqx5CNu3YIpXPxPk7kE1Cua%2FjfXwPi6FcfZeFZV8BY22tnYDtCj%2F0DMG3CLBVw%2FCWJF4kPKtCiaIVIUYfIAfFrwREYG%2BTUt%2BF6x%2BNSK%2BkQ4wNQMdov%2BqH2tdK8JOK1BHyR5ZFBx3dzJcQDHMvojt%2BFZCAnSOoQQvwxWU%2F1mchcZMNfV79%2Fr2Qu7yjEd8DuRgCILsVyuvFa8j81GugYfI0jy%2BGuSabl%2FaK%2Bkuz9dm%2F1eR2Eyf%2BV4jIDaGY4IcEmStTnHeataWphI%2FZfN8zQVE9AmaHMMOfsnM4GOqUBdC67buO7RTxMaAHALZW1wLMM3TEsNX%2Bh3lnmluqJ6x78tnyf0shlVMWYU0zHyfVgjDjmq%2Fkzh%2BaHfVJDijwTziPHwVOSQpbZe1YW55CbCYqZROXwOUXiLwSmX2%2B%2BdEdgNugxPGjodrjcgp1ky%2FWQ0JSN9MKNkJCrmS9x8%2BO27L%2B8AV8vf8mIEcWzPpACoyxars2sJE20E%2BpYxXp5n0zIj%2BM46U84&X-Amz-Signature=471c21eb1e084e17d7376b6a5d1e683188dd5c561e767df7edbed5da7105a755&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642RITZJ5%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T033837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIFdZekgFz2OzHKARUjTIFuQgDN9TVP26%2F5QLdOPQxswaAiEAl6JTJZMIZY%2FQ7sqM%2BT9aoYsbeUALQTqkxdQ7WaNJu8AqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIeON1mRyW044dsyrcA6TDrBvPZKVxe5MD8uM3W%2By5%2BuVjWJ5JqTSdMD4Yo%2Blj78cuE0ek3aqlqEslbwJoga55J9DwEoHRnO8e%2Fj5zQG706J51ZQd6jHjxO0Yh5xnx52631sv6u32pcYm%2BRcT%2B5VVP8YRxaaew5C0kZZVBhQuUaK%2B7%2BK1zIS9%2FU70DXAIFbzKzToMJoDXRXuE3PZFtxQB%2FBHYwzSwiqflFy89Kqnj8iDdfl3o27pQN2umbR6CS%2FVrSh2GzVCBcNOGe%2BPfPq9Xa0ddEjqTPZqcJ6ECMIfnt6aEWqFyL3jsHbdOJ5uMM1ECvMSNghEbZZ9vLG%2FHVVu2b%2Bqop%2FRkXCu%2BVAM8skfxugAT%2BrA0gSmFqx5CNu3YIpXPxPk7kE1Cua%2FjfXwPi6FcfZeFZV8BY22tnYDtCj%2F0DMG3CLBVw%2FCWJF4kPKtCiaIVIUYfIAfFrwREYG%2BTUt%2BF6x%2BNSK%2BkQ4wNQMdov%2BqH2tdK8JOK1BHyR5ZFBx3dzJcQDHMvojt%2BFZCAnSOoQQvwxWU%2F1mchcZMNfV79%2Fr2Qu7yjEd8DuRgCILsVyuvFa8j81GugYfI0jy%2BGuSabl%2FaK%2Bkuz9dm%2F1eR2Eyf%2BV4jIDaGY4IcEmStTnHeataWphI%2FZfN8zQVE9AmaHMMOfsnM4GOqUBdC67buO7RTxMaAHALZW1wLMM3TEsNX%2Bh3lnmluqJ6x78tnyf0shlVMWYU0zHyfVgjDjmq%2Fkzh%2BaHfVJDijwTziPHwVOSQpbZe1YW55CbCYqZROXwOUXiLwSmX2%2B%2BdEdgNugxPGjodrjcgp1ky%2FWQ0JSN9MKNkJCrmS9x8%2BO27L%2B8AV8vf8mIEcWzPpACoyxars2sJE20E%2BpYxXp5n0zIj%2BM46U84&X-Amz-Signature=6411630a26b8c0da65d42fc9f84d2e61bab48f8b6268c17aae32926662911127&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

