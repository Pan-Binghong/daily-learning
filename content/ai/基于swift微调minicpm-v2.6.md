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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4EWYWHV%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T025948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCH0Z8ejaI4ObU0i4%2B2cfKekID9z9nFxbnXoo3KNRuyF8CIQDwo%2F%2FdXObVGH8WFG24%2BkMniAVQcgeFtbC7cr7ahZfYgiqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkxowcKrebqZci%2BfRKtwDRqReu59nisQy9uG4AnMurmGWzFjIGIB1ic6zpuDZJonkeIxBkbWP6xx9WqTD8wbeL2FaeZZcU6gc5KcPxOVntRfNujdCTIX6KA7TD5h0dLXOYvytBVAzbUxDFqAOcYuDKuo9PFungBa5o5yS0jbVWdowNy6ZDeXMTAo2W0G1V0IQFWGbyRvCaHrK7z1xRBtIroXeBCstuZy7%2F%2Fq3BibrMPbQNRuosc9vs%2F%2BQEX5GZf0ZML4dj0Wz2b5iA2O95l3QvFZg3QkPDNKDdHxtTmKUhxnq03t3ptLkCw1FN1KB90ZskfXgqsKcnfhxBiaE9V00c6%2BtYwuIsUQtPs2eSxBtj8LNJrnZRqKOV3%2FmpYg%2F8Q5pHwVP8kkG2jcdq0CByZdiRoMoXNVNnN7bHrnqsvw482%2BBc1KEM%2Fxr0WB6vAnmwqPFE2pPxa3O%2B7p9mmuiNYC%2FrpqsIitBw1KHSiZ35BbKdYxj1%2BoUrEzktSKXU8OcB%2B9bdcNvkvOtbIiPOinVaOpV9N4KaH8Us3oiwFt4QO7AXJubm67oqmcI8ZvCN8uWn6e%2F9gU0otFJS%2FnnXnu1tix3XhEywqYBEHo%2BNZ5PUApv57TaPsTrX49d6ODy5JGt0qgj%2BMEfPSNt7zhb4ZYw8LbcygY6pgEDHN25SEmsNGsenkZfxEZMbiudGccHIZME48l0P5l5fTp2VjpjQb6LshdMZReHj51Uza6lvupfn23jBpkaFWZh4En0wFArmWPxlcgV%2BD3YWPuLVFXexKAZuVdGuDwUunTIDx%2Bnl57QQlbcEbSMkLWtn%2FpauKIoK2B9IuYX%2FXVgOXGM%2FSu9isz5hpDulcFUxoQrjz6C2MMvTyP8h%2BG3xFVYN4wEWSyk&X-Amz-Signature=538480f6b13e83a46619b739cd5eb363307d0e44700a3e5cd90118c1f6fa67ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4EWYWHV%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T025948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCH0Z8ejaI4ObU0i4%2B2cfKekID9z9nFxbnXoo3KNRuyF8CIQDwo%2F%2FdXObVGH8WFG24%2BkMniAVQcgeFtbC7cr7ahZfYgiqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkxowcKrebqZci%2BfRKtwDRqReu59nisQy9uG4AnMurmGWzFjIGIB1ic6zpuDZJonkeIxBkbWP6xx9WqTD8wbeL2FaeZZcU6gc5KcPxOVntRfNujdCTIX6KA7TD5h0dLXOYvytBVAzbUxDFqAOcYuDKuo9PFungBa5o5yS0jbVWdowNy6ZDeXMTAo2W0G1V0IQFWGbyRvCaHrK7z1xRBtIroXeBCstuZy7%2F%2Fq3BibrMPbQNRuosc9vs%2F%2BQEX5GZf0ZML4dj0Wz2b5iA2O95l3QvFZg3QkPDNKDdHxtTmKUhxnq03t3ptLkCw1FN1KB90ZskfXgqsKcnfhxBiaE9V00c6%2BtYwuIsUQtPs2eSxBtj8LNJrnZRqKOV3%2FmpYg%2F8Q5pHwVP8kkG2jcdq0CByZdiRoMoXNVNnN7bHrnqsvw482%2BBc1KEM%2Fxr0WB6vAnmwqPFE2pPxa3O%2B7p9mmuiNYC%2FrpqsIitBw1KHSiZ35BbKdYxj1%2BoUrEzktSKXU8OcB%2B9bdcNvkvOtbIiPOinVaOpV9N4KaH8Us3oiwFt4QO7AXJubm67oqmcI8ZvCN8uWn6e%2F9gU0otFJS%2FnnXnu1tix3XhEywqYBEHo%2BNZ5PUApv57TaPsTrX49d6ODy5JGt0qgj%2BMEfPSNt7zhb4ZYw8LbcygY6pgEDHN25SEmsNGsenkZfxEZMbiudGccHIZME48l0P5l5fTp2VjpjQb6LshdMZReHj51Uza6lvupfn23jBpkaFWZh4En0wFArmWPxlcgV%2BD3YWPuLVFXexKAZuVdGuDwUunTIDx%2Bnl57QQlbcEbSMkLWtn%2FpauKIoK2B9IuYX%2FXVgOXGM%2FSu9isz5hpDulcFUxoQrjz6C2MMvTyP8h%2BG3xFVYN4wEWSyk&X-Amz-Signature=ec99371ea821c0c7a1b9de1faa1baaa8ae13e62f5562815177fbd0576f1884e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4EWYWHV%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T025948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCH0Z8ejaI4ObU0i4%2B2cfKekID9z9nFxbnXoo3KNRuyF8CIQDwo%2F%2FdXObVGH8WFG24%2BkMniAVQcgeFtbC7cr7ahZfYgiqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkxowcKrebqZci%2BfRKtwDRqReu59nisQy9uG4AnMurmGWzFjIGIB1ic6zpuDZJonkeIxBkbWP6xx9WqTD8wbeL2FaeZZcU6gc5KcPxOVntRfNujdCTIX6KA7TD5h0dLXOYvytBVAzbUxDFqAOcYuDKuo9PFungBa5o5yS0jbVWdowNy6ZDeXMTAo2W0G1V0IQFWGbyRvCaHrK7z1xRBtIroXeBCstuZy7%2F%2Fq3BibrMPbQNRuosc9vs%2F%2BQEX5GZf0ZML4dj0Wz2b5iA2O95l3QvFZg3QkPDNKDdHxtTmKUhxnq03t3ptLkCw1FN1KB90ZskfXgqsKcnfhxBiaE9V00c6%2BtYwuIsUQtPs2eSxBtj8LNJrnZRqKOV3%2FmpYg%2F8Q5pHwVP8kkG2jcdq0CByZdiRoMoXNVNnN7bHrnqsvw482%2BBc1KEM%2Fxr0WB6vAnmwqPFE2pPxa3O%2B7p9mmuiNYC%2FrpqsIitBw1KHSiZ35BbKdYxj1%2BoUrEzktSKXU8OcB%2B9bdcNvkvOtbIiPOinVaOpV9N4KaH8Us3oiwFt4QO7AXJubm67oqmcI8ZvCN8uWn6e%2F9gU0otFJS%2FnnXnu1tix3XhEywqYBEHo%2BNZ5PUApv57TaPsTrX49d6ODy5JGt0qgj%2BMEfPSNt7zhb4ZYw8LbcygY6pgEDHN25SEmsNGsenkZfxEZMbiudGccHIZME48l0P5l5fTp2VjpjQb6LshdMZReHj51Uza6lvupfn23jBpkaFWZh4En0wFArmWPxlcgV%2BD3YWPuLVFXexKAZuVdGuDwUunTIDx%2Bnl57QQlbcEbSMkLWtn%2FpauKIoK2B9IuYX%2FXVgOXGM%2FSu9isz5hpDulcFUxoQrjz6C2MMvTyP8h%2BG3xFVYN4wEWSyk&X-Amz-Signature=b5454e4b0dbe8088570a63db379e2a368c509e31341cf4dbd6697a256ea6673f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

