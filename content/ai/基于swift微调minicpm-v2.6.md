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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7DAFRYH%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYgSOYQ53P9FffkglGtQ0s%2F9uKDL%2FMywgMwPclOzk1%2FAiEApRrY5%2Ffr%2B49Dhz31cNa%2Fmatw2h3eCXsBFKl1T7OL%2FYgq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDD09nihhjxEMOwa5kSrcA2D9IUMimR4aAhembZFQAHZ5JMIyijInFmjMSLss8g72QFLQWAzrB%2F0t5dJ4MTgXTLRdI5L2%2F7f%2FMgWnBNkiH50AIUI7phwUuhmPjOZtbzOWt2ulElxmfU5juOaW%2Fu7Zuo4aICrYkfnoi9b%2F6tfwSvxmzow7RxMhDwvOIBrvh8cdmFADSU%2FK0ASPMRaWg7CNtvCzOmNSQpCaKFVCN8Z6XodIXGJl6qwev4TTvj%2B7zDHkdxHn4Y8qs0Nu9NzOhl9TGsc7irYD1rqE7pUxsQV4PEUHSQmN4VhiVOhuJ2tnFAH4OpyCnVrVWrYTZZEH6mQr%2FsCUGCS2GTN03sjagepZbuDy0QmJgwFozalR5Sj%2Bi5Vp1kBLnRj6R1lm8Shg71I5A6wcIf6fu8qYawldTSWfxqOyKD%2FHc8NFMpMUpvUMsmhPPkBFqyNAtaZAWrj0GbI%2Bmj9oJ6yjRYx4tTXmzc%2BnJPBnI98FIm2PMgBx%2BH2OEcDohel69WDDNwt5ZKGBliOQkNxZ0GpSjqLN3AVF6zwnyYrGGOGyfd1md5XQ0v1tRuBI1UIM8fLotDtxth3d8EvyPYwQh4ioPpwACW4adUWPH4PLtkaU1gmeu3HAXojL2hrP6DMAlTJnCeUoLSX4MJinzskGOqUBsISnBBBh0bWo1%2BmoNsxBZGblZGA0y7EMAbCAvZHCQYRJ5m%2BS60w4oEcxJXvH8Mot%2BN2pF0p0aBoF2yPAZMAmSjJ5fQyyY%2BWp%2F2g4xCmmN%2BQaVj%2BzSqb4tu0GzyUij1PfupDLR%2FI%2BXFzuy77oTtcTkikYARfmjCWGQP4NFtPzQdVlEA3K%2BSECdZpTcBwjYF7ooYa3Z6PwfzyD4e3dYLKHdtwxt%2BBz&X-Amz-Signature=b5e31cd036fcbcd70af9eff382800cab2683abe34c9d4b9fd13c82008909e81f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7DAFRYH%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYgSOYQ53P9FffkglGtQ0s%2F9uKDL%2FMywgMwPclOzk1%2FAiEApRrY5%2Ffr%2B49Dhz31cNa%2Fmatw2h3eCXsBFKl1T7OL%2FYgq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDD09nihhjxEMOwa5kSrcA2D9IUMimR4aAhembZFQAHZ5JMIyijInFmjMSLss8g72QFLQWAzrB%2F0t5dJ4MTgXTLRdI5L2%2F7f%2FMgWnBNkiH50AIUI7phwUuhmPjOZtbzOWt2ulElxmfU5juOaW%2Fu7Zuo4aICrYkfnoi9b%2F6tfwSvxmzow7RxMhDwvOIBrvh8cdmFADSU%2FK0ASPMRaWg7CNtvCzOmNSQpCaKFVCN8Z6XodIXGJl6qwev4TTvj%2B7zDHkdxHn4Y8qs0Nu9NzOhl9TGsc7irYD1rqE7pUxsQV4PEUHSQmN4VhiVOhuJ2tnFAH4OpyCnVrVWrYTZZEH6mQr%2FsCUGCS2GTN03sjagepZbuDy0QmJgwFozalR5Sj%2Bi5Vp1kBLnRj6R1lm8Shg71I5A6wcIf6fu8qYawldTSWfxqOyKD%2FHc8NFMpMUpvUMsmhPPkBFqyNAtaZAWrj0GbI%2Bmj9oJ6yjRYx4tTXmzc%2BnJPBnI98FIm2PMgBx%2BH2OEcDohel69WDDNwt5ZKGBliOQkNxZ0GpSjqLN3AVF6zwnyYrGGOGyfd1md5XQ0v1tRuBI1UIM8fLotDtxth3d8EvyPYwQh4ioPpwACW4adUWPH4PLtkaU1gmeu3HAXojL2hrP6DMAlTJnCeUoLSX4MJinzskGOqUBsISnBBBh0bWo1%2BmoNsxBZGblZGA0y7EMAbCAvZHCQYRJ5m%2BS60w4oEcxJXvH8Mot%2BN2pF0p0aBoF2yPAZMAmSjJ5fQyyY%2BWp%2F2g4xCmmN%2BQaVj%2BzSqb4tu0GzyUij1PfupDLR%2FI%2BXFzuy77oTtcTkikYARfmjCWGQP4NFtPzQdVlEA3K%2BSECdZpTcBwjYF7ooYa3Z6PwfzyD4e3dYLKHdtwxt%2BBz&X-Amz-Signature=04e4b459cd763b3d308878c60e270d96c4136c1786789b00ae47ed50d438d400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7DAFRYH%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYgSOYQ53P9FffkglGtQ0s%2F9uKDL%2FMywgMwPclOzk1%2FAiEApRrY5%2Ffr%2B49Dhz31cNa%2Fmatw2h3eCXsBFKl1T7OL%2FYgq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDD09nihhjxEMOwa5kSrcA2D9IUMimR4aAhembZFQAHZ5JMIyijInFmjMSLss8g72QFLQWAzrB%2F0t5dJ4MTgXTLRdI5L2%2F7f%2FMgWnBNkiH50AIUI7phwUuhmPjOZtbzOWt2ulElxmfU5juOaW%2Fu7Zuo4aICrYkfnoi9b%2F6tfwSvxmzow7RxMhDwvOIBrvh8cdmFADSU%2FK0ASPMRaWg7CNtvCzOmNSQpCaKFVCN8Z6XodIXGJl6qwev4TTvj%2B7zDHkdxHn4Y8qs0Nu9NzOhl9TGsc7irYD1rqE7pUxsQV4PEUHSQmN4VhiVOhuJ2tnFAH4OpyCnVrVWrYTZZEH6mQr%2FsCUGCS2GTN03sjagepZbuDy0QmJgwFozalR5Sj%2Bi5Vp1kBLnRj6R1lm8Shg71I5A6wcIf6fu8qYawldTSWfxqOyKD%2FHc8NFMpMUpvUMsmhPPkBFqyNAtaZAWrj0GbI%2Bmj9oJ6yjRYx4tTXmzc%2BnJPBnI98FIm2PMgBx%2BH2OEcDohel69WDDNwt5ZKGBliOQkNxZ0GpSjqLN3AVF6zwnyYrGGOGyfd1md5XQ0v1tRuBI1UIM8fLotDtxth3d8EvyPYwQh4ioPpwACW4adUWPH4PLtkaU1gmeu3HAXojL2hrP6DMAlTJnCeUoLSX4MJinzskGOqUBsISnBBBh0bWo1%2BmoNsxBZGblZGA0y7EMAbCAvZHCQYRJ5m%2BS60w4oEcxJXvH8Mot%2BN2pF0p0aBoF2yPAZMAmSjJ5fQyyY%2BWp%2F2g4xCmmN%2BQaVj%2BzSqb4tu0GzyUij1PfupDLR%2FI%2BXFzuy77oTtcTkikYARfmjCWGQP4NFtPzQdVlEA3K%2BSECdZpTcBwjYF7ooYa3Z6PwfzyD4e3dYLKHdtwxt%2BBz&X-Amz-Signature=540a84bef15f84b0b3d16b82c6b10d5bd516afa7d9ba83890392e3cbb597dc16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

