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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHTU5XHE%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIA3n5ai2S8a2O4U8e9B1KHZrOa8QorzQo5TQTx7x16iVAiEAhEqIivVgb4y8nnVuvqSaOrhmG%2FVxynOivRW0dILSe1oqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKR5UZ5K%2F3Zbc4%2BwVSrcA1jLsGgaW6VHgMGXQ8HRnYcoPDXkXzML%2FTt2HZrTili1fophkKQkaUgsaRZfXaZnx0RPSEhDJzysOKNQiIPYv54gMq8zDTnsZlSU1FU3igaXNzX2KX7lKXsS6iHrd6YVOidh3OdfKjZtkExPx4ETHu06bte%2F1aW%2BtzH%2FSCa6CtPsj6PAUqlsvyuPAQ93iPFbIwLY3o5ON%2FbF0wiNvc2bxCMrw8YSITnjPY3S9wN1g8vSpgSsVlIVsLI03qFYgt%2BQ%2FoeH45RDVcGuykSMTtnM%2B6oJGb2nVZp2fVZWcb14Uvn7Ig6U1LvG2oONfeDp%2FK8POS7%2BTnkoCMu%2FpWvluTFPUmTtGHt3ppptyaqYRipTe%2BsAMeirWBTLR0Ap19XbkxSXP61JxDB0MsktpY6wNCRCsR%2FqIyD3XDDg1MBfFGA%2Fi73a8BfOtV1Uri6AjYPhxI1AiY37f0x2v3LK3i%2BDO8YjvRkOgmJcWshGKnUA%2FB5w7wvq%2B3i7VjBaocXwsgHXox9uX76%2BVqwcNQhxP2kCXt3CdhabTeOGESWltJ%2FmS%2Buxw%2FSu7PcSN%2Blx0sEiEkIjuAG7VGaEbzjgAvuIyEJ8%2Fi552MWlTGvSkbMPJ7%2Fv0pTqcMfeqE1pHZHFzsNGfq6OMKjlosoGOqUBVA%2BJoDbd8W62MmtFRJHRkdvtlHDlqYyv1z1Codd1RQXMFzDBtayZb0%2Fod2%2F%2FdN51iRIARNgE7vY7IidhJluUPxZYJafMWoK5RRudHlyk3kHgeTudioh69g8ECAs6R6uI92XckEgEW%2FuNpZhxd5R2qhnZuuXqyNQwqYaAgCFvM3B2Yp3yZfd%2FBMmBkILAu9wJnqiWFiT24ob8OFYHDgu%2FkCcQSLEv&X-Amz-Signature=3cf42235be97140c457af16599bd0e9681462fd7bb10333ef483b5b17223a5d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHTU5XHE%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIA3n5ai2S8a2O4U8e9B1KHZrOa8QorzQo5TQTx7x16iVAiEAhEqIivVgb4y8nnVuvqSaOrhmG%2FVxynOivRW0dILSe1oqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKR5UZ5K%2F3Zbc4%2BwVSrcA1jLsGgaW6VHgMGXQ8HRnYcoPDXkXzML%2FTt2HZrTili1fophkKQkaUgsaRZfXaZnx0RPSEhDJzysOKNQiIPYv54gMq8zDTnsZlSU1FU3igaXNzX2KX7lKXsS6iHrd6YVOidh3OdfKjZtkExPx4ETHu06bte%2F1aW%2BtzH%2FSCa6CtPsj6PAUqlsvyuPAQ93iPFbIwLY3o5ON%2FbF0wiNvc2bxCMrw8YSITnjPY3S9wN1g8vSpgSsVlIVsLI03qFYgt%2BQ%2FoeH45RDVcGuykSMTtnM%2B6oJGb2nVZp2fVZWcb14Uvn7Ig6U1LvG2oONfeDp%2FK8POS7%2BTnkoCMu%2FpWvluTFPUmTtGHt3ppptyaqYRipTe%2BsAMeirWBTLR0Ap19XbkxSXP61JxDB0MsktpY6wNCRCsR%2FqIyD3XDDg1MBfFGA%2Fi73a8BfOtV1Uri6AjYPhxI1AiY37f0x2v3LK3i%2BDO8YjvRkOgmJcWshGKnUA%2FB5w7wvq%2B3i7VjBaocXwsgHXox9uX76%2BVqwcNQhxP2kCXt3CdhabTeOGESWltJ%2FmS%2Buxw%2FSu7PcSN%2Blx0sEiEkIjuAG7VGaEbzjgAvuIyEJ8%2Fi552MWlTGvSkbMPJ7%2Fv0pTqcMfeqE1pHZHFzsNGfq6OMKjlosoGOqUBVA%2BJoDbd8W62MmtFRJHRkdvtlHDlqYyv1z1Codd1RQXMFzDBtayZb0%2Fod2%2F%2FdN51iRIARNgE7vY7IidhJluUPxZYJafMWoK5RRudHlyk3kHgeTudioh69g8ECAs6R6uI92XckEgEW%2FuNpZhxd5R2qhnZuuXqyNQwqYaAgCFvM3B2Yp3yZfd%2FBMmBkILAu9wJnqiWFiT24ob8OFYHDgu%2FkCcQSLEv&X-Amz-Signature=ccf0c324d0770281f2ca3079e12c25590721cfe473680caabb955addea7bbb23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHTU5XHE%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIA3n5ai2S8a2O4U8e9B1KHZrOa8QorzQo5TQTx7x16iVAiEAhEqIivVgb4y8nnVuvqSaOrhmG%2FVxynOivRW0dILSe1oqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKR5UZ5K%2F3Zbc4%2BwVSrcA1jLsGgaW6VHgMGXQ8HRnYcoPDXkXzML%2FTt2HZrTili1fophkKQkaUgsaRZfXaZnx0RPSEhDJzysOKNQiIPYv54gMq8zDTnsZlSU1FU3igaXNzX2KX7lKXsS6iHrd6YVOidh3OdfKjZtkExPx4ETHu06bte%2F1aW%2BtzH%2FSCa6CtPsj6PAUqlsvyuPAQ93iPFbIwLY3o5ON%2FbF0wiNvc2bxCMrw8YSITnjPY3S9wN1g8vSpgSsVlIVsLI03qFYgt%2BQ%2FoeH45RDVcGuykSMTtnM%2B6oJGb2nVZp2fVZWcb14Uvn7Ig6U1LvG2oONfeDp%2FK8POS7%2BTnkoCMu%2FpWvluTFPUmTtGHt3ppptyaqYRipTe%2BsAMeirWBTLR0Ap19XbkxSXP61JxDB0MsktpY6wNCRCsR%2FqIyD3XDDg1MBfFGA%2Fi73a8BfOtV1Uri6AjYPhxI1AiY37f0x2v3LK3i%2BDO8YjvRkOgmJcWshGKnUA%2FB5w7wvq%2B3i7VjBaocXwsgHXox9uX76%2BVqwcNQhxP2kCXt3CdhabTeOGESWltJ%2FmS%2Buxw%2FSu7PcSN%2Blx0sEiEkIjuAG7VGaEbzjgAvuIyEJ8%2Fi552MWlTGvSkbMPJ7%2Fv0pTqcMfeqE1pHZHFzsNGfq6OMKjlosoGOqUBVA%2BJoDbd8W62MmtFRJHRkdvtlHDlqYyv1z1Codd1RQXMFzDBtayZb0%2Fod2%2F%2FdN51iRIARNgE7vY7IidhJluUPxZYJafMWoK5RRudHlyk3kHgeTudioh69g8ECAs6R6uI92XckEgEW%2FuNpZhxd5R2qhnZuuXqyNQwqYaAgCFvM3B2Yp3yZfd%2FBMmBkILAu9wJnqiWFiT24ob8OFYHDgu%2FkCcQSLEv&X-Amz-Signature=4975adfadb3cb80cc95a9373c4b727444573c824edd6800aaf963fe6af355370&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

