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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RA5FA2F%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxQaRjpEHxwXd8vyPQQfpptblgg5u%2FnD%2FJMyGDmD686gIgc8eWjrAQuV%2FCwCtxoxCZxPdHkkgW4qCwdTqNLNp02YkqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKEX5ii4Yf4eiFj6vCrcA%2FYcm4HjHEAtWUZMUiXTEyqw%2B%2BHGpS8ZRpS0GNiNObxFJhRyzu0ZggdYylQWmykd8dE0qMnW0G8ht5uGXJjKDriz1Cdl9fuys3vywLtYVmlmGmFNSP5xzEmUobtCVbDIziuiN3PJaSOXNxlFE7X31LAvzCQzFi%2BZR1lkQB51sBoj1lubSDsn%2BQwikz3iXIPYh4OLyx6wweO%2FHeqLTXJ8PGAodwUxBe7T3VVwk6z9U%2BGBKNz63YsU0AX6d1w%2BF7lz86YHs93HQ72YV5sw8cuCpTjAlSFAjfqDu3gZ6GRvADsfZdetyx625Hhc4dF4yInD%2FlARAphs%2BnpEyc444eO31NNz1x%2FMrLC%2FPG8kLLGumcoscQ%2FufusRuFWiPaulqyM%2Bi4orGSOR0HJ9452GTHnYWlgaAr%2FGDZWkHUK8%2FrzV9Ns6orEG7VTsInitCeEXo51ylMD4V2hdi7wckRWLh97q9Qo9lns03LY75wTCcC%2BwcLDjGIp%2FmLNPAzh8XkPCuI%2BDhKyPDfNqeTEdLphnloPLrR5aAmMvyF4EC9QCUUo%2FWSQ6Kg3ShOq3Lx6PH0g9AJMWDSDVeF8i558l8TicCLawoRLOtiFhQSoG2UJmPKG1TkRAlVHU7TZg7%2B%2B7co91MOnJ8MsGOqUBD%2F0V8ULrv%2FiDmy%2FHdLP80RCTIFhxaa%2FBmswrMwjzReL%2F8NU9axvGQbbD9Un7edsT9jD4raRC1fHPR0%2Fxtn9cUzyHodzLhoSXj2%2B6a9tKF%2FrYGEs%2FLHijuN44cqFbCTz%2FeIiZkivHlaqB5x48uUis%2FeLZkzCDdQcW3N4uLEb%2BkFWQAFNuhvfWEW1pntUds%2B1qcqn4t2eI9%2FI00b0o07JlFIAMB9dN&X-Amz-Signature=4f280360608c17adce9a0a147f5a59628701fae943600c316cf6397cbdce807a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RA5FA2F%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxQaRjpEHxwXd8vyPQQfpptblgg5u%2FnD%2FJMyGDmD686gIgc8eWjrAQuV%2FCwCtxoxCZxPdHkkgW4qCwdTqNLNp02YkqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKEX5ii4Yf4eiFj6vCrcA%2FYcm4HjHEAtWUZMUiXTEyqw%2B%2BHGpS8ZRpS0GNiNObxFJhRyzu0ZggdYylQWmykd8dE0qMnW0G8ht5uGXJjKDriz1Cdl9fuys3vywLtYVmlmGmFNSP5xzEmUobtCVbDIziuiN3PJaSOXNxlFE7X31LAvzCQzFi%2BZR1lkQB51sBoj1lubSDsn%2BQwikz3iXIPYh4OLyx6wweO%2FHeqLTXJ8PGAodwUxBe7T3VVwk6z9U%2BGBKNz63YsU0AX6d1w%2BF7lz86YHs93HQ72YV5sw8cuCpTjAlSFAjfqDu3gZ6GRvADsfZdetyx625Hhc4dF4yInD%2FlARAphs%2BnpEyc444eO31NNz1x%2FMrLC%2FPG8kLLGumcoscQ%2FufusRuFWiPaulqyM%2Bi4orGSOR0HJ9452GTHnYWlgaAr%2FGDZWkHUK8%2FrzV9Ns6orEG7VTsInitCeEXo51ylMD4V2hdi7wckRWLh97q9Qo9lns03LY75wTCcC%2BwcLDjGIp%2FmLNPAzh8XkPCuI%2BDhKyPDfNqeTEdLphnloPLrR5aAmMvyF4EC9QCUUo%2FWSQ6Kg3ShOq3Lx6PH0g9AJMWDSDVeF8i558l8TicCLawoRLOtiFhQSoG2UJmPKG1TkRAlVHU7TZg7%2B%2B7co91MOnJ8MsGOqUBD%2F0V8ULrv%2FiDmy%2FHdLP80RCTIFhxaa%2FBmswrMwjzReL%2F8NU9axvGQbbD9Un7edsT9jD4raRC1fHPR0%2Fxtn9cUzyHodzLhoSXj2%2B6a9tKF%2FrYGEs%2FLHijuN44cqFbCTz%2FeIiZkivHlaqB5x48uUis%2FeLZkzCDdQcW3N4uLEb%2BkFWQAFNuhvfWEW1pntUds%2B1qcqn4t2eI9%2FI00b0o07JlFIAMB9dN&X-Amz-Signature=e0d9e73828aa911bd44094455a542d181044f850fca37458cf911a50b2f2e851&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RA5FA2F%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxQaRjpEHxwXd8vyPQQfpptblgg5u%2FnD%2FJMyGDmD686gIgc8eWjrAQuV%2FCwCtxoxCZxPdHkkgW4qCwdTqNLNp02YkqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKEX5ii4Yf4eiFj6vCrcA%2FYcm4HjHEAtWUZMUiXTEyqw%2B%2BHGpS8ZRpS0GNiNObxFJhRyzu0ZggdYylQWmykd8dE0qMnW0G8ht5uGXJjKDriz1Cdl9fuys3vywLtYVmlmGmFNSP5xzEmUobtCVbDIziuiN3PJaSOXNxlFE7X31LAvzCQzFi%2BZR1lkQB51sBoj1lubSDsn%2BQwikz3iXIPYh4OLyx6wweO%2FHeqLTXJ8PGAodwUxBe7T3VVwk6z9U%2BGBKNz63YsU0AX6d1w%2BF7lz86YHs93HQ72YV5sw8cuCpTjAlSFAjfqDu3gZ6GRvADsfZdetyx625Hhc4dF4yInD%2FlARAphs%2BnpEyc444eO31NNz1x%2FMrLC%2FPG8kLLGumcoscQ%2FufusRuFWiPaulqyM%2Bi4orGSOR0HJ9452GTHnYWlgaAr%2FGDZWkHUK8%2FrzV9Ns6orEG7VTsInitCeEXo51ylMD4V2hdi7wckRWLh97q9Qo9lns03LY75wTCcC%2BwcLDjGIp%2FmLNPAzh8XkPCuI%2BDhKyPDfNqeTEdLphnloPLrR5aAmMvyF4EC9QCUUo%2FWSQ6Kg3ShOq3Lx6PH0g9AJMWDSDVeF8i558l8TicCLawoRLOtiFhQSoG2UJmPKG1TkRAlVHU7TZg7%2B%2B7co91MOnJ8MsGOqUBD%2F0V8ULrv%2FiDmy%2FHdLP80RCTIFhxaa%2FBmswrMwjzReL%2F8NU9axvGQbbD9Un7edsT9jD4raRC1fHPR0%2Fxtn9cUzyHodzLhoSXj2%2B6a9tKF%2FrYGEs%2FLHijuN44cqFbCTz%2FeIiZkivHlaqB5x48uUis%2FeLZkzCDdQcW3N4uLEb%2BkFWQAFNuhvfWEW1pntUds%2B1qcqn4t2eI9%2FI00b0o07JlFIAMB9dN&X-Amz-Signature=bd13f8197357e2fb72fc5f93d83c10a1534bf34e5b4e9422067ae5dac0a719c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

