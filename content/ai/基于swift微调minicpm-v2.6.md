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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSU7HAEM%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCICJsmtiEG2ekvApNvyTXwHNvfnZANl31hNZix%2F0Vyaf0AiAHoxeE0mxt9TXauq2lNXcxFlz4blz%2B0raQCR40wx821iqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoBy4d8iSA3tsklRiKtwD%2Box2aBwDzcofX6Noh%2BiEOegM0wF3Nbkz9SX9ZCFMa%2BPPE4eZ%2FFaqrlB2HV5JtBQm7ozgvArxBITlHhLphyvR%2F5l%2Fw5P%2Bp6DB8zCojgczHW%2B3qwuvl5A4OvUUetTol%2F3qRlsgc7tsmiNUq2DyfovK8sxLziPMbqs8irXLPk9t4%2B6a9FIGXocJ36QQcQ3pq3E0mmtMrKQ4wu%2FipDJUmBd%2FdjmZlv1zm6iaIR7PsNS%2BBvQ9lxqaGg7QZtXPR54pRD7qL62fp1aWsx9j03RmutSlbuE67OWpa%2FPH9%2B9lA5H9frrw8%2FcP%2BxpKECDrdYkKyUFMwdVsNWd%2BNBMpAYxDYEFwVSl8x0LFUBvsqdAj28XO32xQdityU3ZwWSa0smYq35TrlZm7RRcB9ZmwTDOFizaJ6H38f%2BoS755lNtQZCFozXrsXtCuVpTEcdHYymo7OuGcNftgvAGKZf0QCG%2B%2FfSfp5hRgzyjP6GiRMxBSHH1uAzSg17mE3inOWAqwaqETWUdzu5aianRdrA5dvFw9Go%2FMs108Nb8fsOl8Ir1ZTQgQs6ASaYlNFN4xjKeZfLPUCSmyfj2IDQxYqVYwvB4efKsCqj0VRdarkLtNMxaiMPuzuaCdo8p%2BR%2BmZfl9RARU4wqefizQY6pgElH53u8kP5V3r4zD9fanXX%2FIkJsqYXH4qwihooNaQYW6w2nbDx6Dx2Y5Ey01ge6waucQq13dmCMsOY3R1%2BdDRvlQMDjjjwDkHZW8KKvyVciF%2BfiB%2FT%2F%2BTjdhcTKS4%2BEj6p37%2Bb5rwn1Ckr1xg2kO2N1SLZhH%2BbFG6a%2Bo64YXP8h8W4X1H4EA%2B81J%2BnfKhVtfu65x2M4s%2F9FzaoZjZSMr84FsCZd%2FHz&X-Amz-Signature=31b6cddd67fbc89d4bd848f3891b1b735ff09022ea86be0f9ccb5d8742bf8832&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSU7HAEM%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCICJsmtiEG2ekvApNvyTXwHNvfnZANl31hNZix%2F0Vyaf0AiAHoxeE0mxt9TXauq2lNXcxFlz4blz%2B0raQCR40wx821iqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoBy4d8iSA3tsklRiKtwD%2Box2aBwDzcofX6Noh%2BiEOegM0wF3Nbkz9SX9ZCFMa%2BPPE4eZ%2FFaqrlB2HV5JtBQm7ozgvArxBITlHhLphyvR%2F5l%2Fw5P%2Bp6DB8zCojgczHW%2B3qwuvl5A4OvUUetTol%2F3qRlsgc7tsmiNUq2DyfovK8sxLziPMbqs8irXLPk9t4%2B6a9FIGXocJ36QQcQ3pq3E0mmtMrKQ4wu%2FipDJUmBd%2FdjmZlv1zm6iaIR7PsNS%2BBvQ9lxqaGg7QZtXPR54pRD7qL62fp1aWsx9j03RmutSlbuE67OWpa%2FPH9%2B9lA5H9frrw8%2FcP%2BxpKECDrdYkKyUFMwdVsNWd%2BNBMpAYxDYEFwVSl8x0LFUBvsqdAj28XO32xQdityU3ZwWSa0smYq35TrlZm7RRcB9ZmwTDOFizaJ6H38f%2BoS755lNtQZCFozXrsXtCuVpTEcdHYymo7OuGcNftgvAGKZf0QCG%2B%2FfSfp5hRgzyjP6GiRMxBSHH1uAzSg17mE3inOWAqwaqETWUdzu5aianRdrA5dvFw9Go%2FMs108Nb8fsOl8Ir1ZTQgQs6ASaYlNFN4xjKeZfLPUCSmyfj2IDQxYqVYwvB4efKsCqj0VRdarkLtNMxaiMPuzuaCdo8p%2BR%2BmZfl9RARU4wqefizQY6pgElH53u8kP5V3r4zD9fanXX%2FIkJsqYXH4qwihooNaQYW6w2nbDx6Dx2Y5Ey01ge6waucQq13dmCMsOY3R1%2BdDRvlQMDjjjwDkHZW8KKvyVciF%2BfiB%2FT%2F%2BTjdhcTKS4%2BEj6p37%2Bb5rwn1Ckr1xg2kO2N1SLZhH%2BbFG6a%2Bo64YXP8h8W4X1H4EA%2B81J%2BnfKhVtfu65x2M4s%2F9FzaoZjZSMr84FsCZd%2FHz&X-Amz-Signature=c12141b7c784388bcd647bebe222fbe283fd97e048a4ce8b83ea0682897924b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSU7HAEM%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCICJsmtiEG2ekvApNvyTXwHNvfnZANl31hNZix%2F0Vyaf0AiAHoxeE0mxt9TXauq2lNXcxFlz4blz%2B0raQCR40wx821iqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoBy4d8iSA3tsklRiKtwD%2Box2aBwDzcofX6Noh%2BiEOegM0wF3Nbkz9SX9ZCFMa%2BPPE4eZ%2FFaqrlB2HV5JtBQm7ozgvArxBITlHhLphyvR%2F5l%2Fw5P%2Bp6DB8zCojgczHW%2B3qwuvl5A4OvUUetTol%2F3qRlsgc7tsmiNUq2DyfovK8sxLziPMbqs8irXLPk9t4%2B6a9FIGXocJ36QQcQ3pq3E0mmtMrKQ4wu%2FipDJUmBd%2FdjmZlv1zm6iaIR7PsNS%2BBvQ9lxqaGg7QZtXPR54pRD7qL62fp1aWsx9j03RmutSlbuE67OWpa%2FPH9%2B9lA5H9frrw8%2FcP%2BxpKECDrdYkKyUFMwdVsNWd%2BNBMpAYxDYEFwVSl8x0LFUBvsqdAj28XO32xQdityU3ZwWSa0smYq35TrlZm7RRcB9ZmwTDOFizaJ6H38f%2BoS755lNtQZCFozXrsXtCuVpTEcdHYymo7OuGcNftgvAGKZf0QCG%2B%2FfSfp5hRgzyjP6GiRMxBSHH1uAzSg17mE3inOWAqwaqETWUdzu5aianRdrA5dvFw9Go%2FMs108Nb8fsOl8Ir1ZTQgQs6ASaYlNFN4xjKeZfLPUCSmyfj2IDQxYqVYwvB4efKsCqj0VRdarkLtNMxaiMPuzuaCdo8p%2BR%2BmZfl9RARU4wqefizQY6pgElH53u8kP5V3r4zD9fanXX%2FIkJsqYXH4qwihooNaQYW6w2nbDx6Dx2Y5Ey01ge6waucQq13dmCMsOY3R1%2BdDRvlQMDjjjwDkHZW8KKvyVciF%2BfiB%2FT%2F%2BTjdhcTKS4%2BEj6p37%2Bb5rwn1Ckr1xg2kO2N1SLZhH%2BbFG6a%2Bo64YXP8h8W4X1H4EA%2B81J%2BnfKhVtfu65x2M4s%2F9FzaoZjZSMr84FsCZd%2FHz&X-Amz-Signature=c7f9aeb24257d2000787c4bc755ceb782539bfdbfe1acb440bade09ebeafd292&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

