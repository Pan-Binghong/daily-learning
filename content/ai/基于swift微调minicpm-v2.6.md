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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BTPHGZU%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCK055lpWI52KAREbo7MjD3veoHQoywbgmVMk%2FuJn%2BIgwIgc%2BOn5gmqzGwhFKdrBwnOjF3Ht8Lsw9LqDKNlFBq771Aq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDDV0Q%2F%2B4X%2Bq7BCM8ySrcA3aBJGIDGf9c2At%2BVZQNQpxCGU%2FOXjg3mvnlw4N3J8nZUyN2kevaWFxGENXf2SgWtKVBxE0RvQg%2F4OUeJfl5MR93TwFMmNtaDkZdPeWJWOhPg%2B1qkn8LmrKHaGCGRpdTaiAWXkWwz5mZVyX1NM5DTtBZKsRaMPkTmngECIXyhxwDUpJKBIaVdbKWb3fHwIIycUarwwMCNnKt%2BS6AOt9Sc8itoFLB0T9cMj8v7aj56XQssvGEsAraYxlw9MOrs%2FLnRitOLzL3Baxfn8y07zqEKcjWhoSzMN%2BVRntLr6Qkh8MxJBd7ETEvj1%2BGl0%2Bdb0wJrKSGy%2BwvVqxNaT1i6IL74PKsxfRHSZrZwujD42dln5Zm4kbcHP30yehUJhpQe8n3Ri7JwZuW6wc%2F6aVjT%2BBk7rgeUBJb77Matm2PbIfpMDmxU1nsA0x9Mkvz97t36iGTxyLEyJON%2BB6PyWBkKVD06lQg5%2F23t5Ms%2BheLjCGA%2FIurZG%2FZrSj2KWIcPmkDYhFYB%2BwJttmCxmg2%2BUQ7n6wT9ObEmxnNeQnEebWKHJuyn%2FlaatwlAFuquPdByciZYf1xoW0VQtXns3YvBx7GpwJ520C0N39SFgtmnjJaMtUJiZ5511wVPwkCQhH6SHGEMMyUyswGOqUBGaKWKKZ0oDudE%2FysNEvUMi%2FwUAWlw%2BuHLo6S5x%2FbAGCJXLpI2zCvSAFLv8L8yPYpaKhMr1AumNiUCrSYiNQ1CyPcpvJBHr64QzP2zs7EcxwDYWyUzV9PrP1CseQdiCRErfJye3a7vYKvJmKiOpBTnJcociwp5l2xhsVmZW4HR1dLEPGX%2FJDTPZ5usS37zkvsWRgM4%2BK7Not7K%2FrKINEVxZfBG6Rx&X-Amz-Signature=2f5216288b65cf3bab318f0b68de7dbd673ff64592c435cde8a3f94142a5b639&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BTPHGZU%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCK055lpWI52KAREbo7MjD3veoHQoywbgmVMk%2FuJn%2BIgwIgc%2BOn5gmqzGwhFKdrBwnOjF3Ht8Lsw9LqDKNlFBq771Aq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDDV0Q%2F%2B4X%2Bq7BCM8ySrcA3aBJGIDGf9c2At%2BVZQNQpxCGU%2FOXjg3mvnlw4N3J8nZUyN2kevaWFxGENXf2SgWtKVBxE0RvQg%2F4OUeJfl5MR93TwFMmNtaDkZdPeWJWOhPg%2B1qkn8LmrKHaGCGRpdTaiAWXkWwz5mZVyX1NM5DTtBZKsRaMPkTmngECIXyhxwDUpJKBIaVdbKWb3fHwIIycUarwwMCNnKt%2BS6AOt9Sc8itoFLB0T9cMj8v7aj56XQssvGEsAraYxlw9MOrs%2FLnRitOLzL3Baxfn8y07zqEKcjWhoSzMN%2BVRntLr6Qkh8MxJBd7ETEvj1%2BGl0%2Bdb0wJrKSGy%2BwvVqxNaT1i6IL74PKsxfRHSZrZwujD42dln5Zm4kbcHP30yehUJhpQe8n3Ri7JwZuW6wc%2F6aVjT%2BBk7rgeUBJb77Matm2PbIfpMDmxU1nsA0x9Mkvz97t36iGTxyLEyJON%2BB6PyWBkKVD06lQg5%2F23t5Ms%2BheLjCGA%2FIurZG%2FZrSj2KWIcPmkDYhFYB%2BwJttmCxmg2%2BUQ7n6wT9ObEmxnNeQnEebWKHJuyn%2FlaatwlAFuquPdByciZYf1xoW0VQtXns3YvBx7GpwJ520C0N39SFgtmnjJaMtUJiZ5511wVPwkCQhH6SHGEMMyUyswGOqUBGaKWKKZ0oDudE%2FysNEvUMi%2FwUAWlw%2BuHLo6S5x%2FbAGCJXLpI2zCvSAFLv8L8yPYpaKhMr1AumNiUCrSYiNQ1CyPcpvJBHr64QzP2zs7EcxwDYWyUzV9PrP1CseQdiCRErfJye3a7vYKvJmKiOpBTnJcociwp5l2xhsVmZW4HR1dLEPGX%2FJDTPZ5usS37zkvsWRgM4%2BK7Not7K%2FrKINEVxZfBG6Rx&X-Amz-Signature=92613421e9ea4ebd879ef6c36cace0e2389db9b80b0e05a7ca4215d34a9b1573&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BTPHGZU%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCK055lpWI52KAREbo7MjD3veoHQoywbgmVMk%2FuJn%2BIgwIgc%2BOn5gmqzGwhFKdrBwnOjF3Ht8Lsw9LqDKNlFBq771Aq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDDV0Q%2F%2B4X%2Bq7BCM8ySrcA3aBJGIDGf9c2At%2BVZQNQpxCGU%2FOXjg3mvnlw4N3J8nZUyN2kevaWFxGENXf2SgWtKVBxE0RvQg%2F4OUeJfl5MR93TwFMmNtaDkZdPeWJWOhPg%2B1qkn8LmrKHaGCGRpdTaiAWXkWwz5mZVyX1NM5DTtBZKsRaMPkTmngECIXyhxwDUpJKBIaVdbKWb3fHwIIycUarwwMCNnKt%2BS6AOt9Sc8itoFLB0T9cMj8v7aj56XQssvGEsAraYxlw9MOrs%2FLnRitOLzL3Baxfn8y07zqEKcjWhoSzMN%2BVRntLr6Qkh8MxJBd7ETEvj1%2BGl0%2Bdb0wJrKSGy%2BwvVqxNaT1i6IL74PKsxfRHSZrZwujD42dln5Zm4kbcHP30yehUJhpQe8n3Ri7JwZuW6wc%2F6aVjT%2BBk7rgeUBJb77Matm2PbIfpMDmxU1nsA0x9Mkvz97t36iGTxyLEyJON%2BB6PyWBkKVD06lQg5%2F23t5Ms%2BheLjCGA%2FIurZG%2FZrSj2KWIcPmkDYhFYB%2BwJttmCxmg2%2BUQ7n6wT9ObEmxnNeQnEebWKHJuyn%2FlaatwlAFuquPdByciZYf1xoW0VQtXns3YvBx7GpwJ520C0N39SFgtmnjJaMtUJiZ5511wVPwkCQhH6SHGEMMyUyswGOqUBGaKWKKZ0oDudE%2FysNEvUMi%2FwUAWlw%2BuHLo6S5x%2FbAGCJXLpI2zCvSAFLv8L8yPYpaKhMr1AumNiUCrSYiNQ1CyPcpvJBHr64QzP2zs7EcxwDYWyUzV9PrP1CseQdiCRErfJye3a7vYKvJmKiOpBTnJcociwp5l2xhsVmZW4HR1dLEPGX%2FJDTPZ5usS37zkvsWRgM4%2BK7Not7K%2FrKINEVxZfBG6Rx&X-Amz-Signature=8f75cc8edf3877b5faa147c8552923bdbe1000787a25dde60583e1f4c9c02cd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

