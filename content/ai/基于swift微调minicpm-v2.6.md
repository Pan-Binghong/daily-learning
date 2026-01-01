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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667B54MJWR%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCICK7ZtHpWHBBX76ok1oIVqb7dIaRV%2FwGK3YncWV8FuQ4AiEA%2BeaFGWbvC6VJiAKeqJdBLwv8kPoiMqCzfzofBu0O7cwqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCMlAwPoF2K5HMGdircA%2BK0jkh2Rxh9rpTJUxP0%2FsxJ2bGLoIAkTm4InvdGei5CWN9V1AT7eendY1NrkPV9QEpG%2FR8ed96KxiPFreOodighI7qpxOmj1AwqQF43eJqD8HNqAKWOb2fo9D%2FBMAgLQbDhlNyEl4zNqNoXna126jduBzc4nRkQLDFZO%2FTbScLRLO2Arav4BB9XK8e466AMkVP7rmnSECgIr%2BWJnQmuPdlVCavP4WUcLW0fPQ6y7gj%2FWxTsWTtAiq1uLiNAEUYHNhdWGVlpsf%2FyJ7B%2BM1FdIQnla38Y5uOUxemgcz4Yoey8xw048JVy2E45K43kUdet5k4HpOqGnW6GKwOOH7lTg6cXCnKLQsHlbFvRzVylZoczQq4EchmhIV08lhzbVWymFb5CdS1RtNXDlGR970nABHFFm2FvGo9elRFIeKXsR290bm3r6PhytObsV%2FA3WN9px4Xb145gEulV48CxMihr2jkro2pdkVGsnTgpjyVdEKGL%2FTRMza4wGndLda4JsrXSLnvBzp1goXR%2FqNisitGCqG5VIjMQ3vTEVN4QYs95zLDMFQ3tCJLD1ctl1%2FwuGzKdMuBXi4PtvKmLYgMsrG1AT6utzVoCfHrlQi4q343HkTiCxoZX75OYipoaZmZwMOyg18oGOqUBTMrWuCmpkIcDkXiCjQOVy8TH%2BQHkqvhMQFJuhiDg5KlRMHzIUDaLRHigQUkE4UFVbXfA0GwWVj6WPUyupOa3nWWBpJf8ab%2BLqAeF5NkK6Pw%2B5zaghflNJOy0sdSv9XgVYzH0XKb71H%2BvmRP69cx%2BhI%2Bseb5F6uXsBj6Mxj%2FGbwVyt7rz7iGg5Cv%2F8ftOE11TOMbBf9C7DfmPhNYscVphUkT6wnX3&X-Amz-Signature=9af4779ba998fe31ae6c8e5ce25442497e16259d14a55ba972199d116b75646d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667B54MJWR%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCICK7ZtHpWHBBX76ok1oIVqb7dIaRV%2FwGK3YncWV8FuQ4AiEA%2BeaFGWbvC6VJiAKeqJdBLwv8kPoiMqCzfzofBu0O7cwqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCMlAwPoF2K5HMGdircA%2BK0jkh2Rxh9rpTJUxP0%2FsxJ2bGLoIAkTm4InvdGei5CWN9V1AT7eendY1NrkPV9QEpG%2FR8ed96KxiPFreOodighI7qpxOmj1AwqQF43eJqD8HNqAKWOb2fo9D%2FBMAgLQbDhlNyEl4zNqNoXna126jduBzc4nRkQLDFZO%2FTbScLRLO2Arav4BB9XK8e466AMkVP7rmnSECgIr%2BWJnQmuPdlVCavP4WUcLW0fPQ6y7gj%2FWxTsWTtAiq1uLiNAEUYHNhdWGVlpsf%2FyJ7B%2BM1FdIQnla38Y5uOUxemgcz4Yoey8xw048JVy2E45K43kUdet5k4HpOqGnW6GKwOOH7lTg6cXCnKLQsHlbFvRzVylZoczQq4EchmhIV08lhzbVWymFb5CdS1RtNXDlGR970nABHFFm2FvGo9elRFIeKXsR290bm3r6PhytObsV%2FA3WN9px4Xb145gEulV48CxMihr2jkro2pdkVGsnTgpjyVdEKGL%2FTRMza4wGndLda4JsrXSLnvBzp1goXR%2FqNisitGCqG5VIjMQ3vTEVN4QYs95zLDMFQ3tCJLD1ctl1%2FwuGzKdMuBXi4PtvKmLYgMsrG1AT6utzVoCfHrlQi4q343HkTiCxoZX75OYipoaZmZwMOyg18oGOqUBTMrWuCmpkIcDkXiCjQOVy8TH%2BQHkqvhMQFJuhiDg5KlRMHzIUDaLRHigQUkE4UFVbXfA0GwWVj6WPUyupOa3nWWBpJf8ab%2BLqAeF5NkK6Pw%2B5zaghflNJOy0sdSv9XgVYzH0XKb71H%2BvmRP69cx%2BhI%2Bseb5F6uXsBj6Mxj%2FGbwVyt7rz7iGg5Cv%2F8ftOE11TOMbBf9C7DfmPhNYscVphUkT6wnX3&X-Amz-Signature=6a6af113a2a115e41c1a3029a39de604b48c7dfac85b0c279e9e4aca9fe8e081&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667B54MJWR%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCICK7ZtHpWHBBX76ok1oIVqb7dIaRV%2FwGK3YncWV8FuQ4AiEA%2BeaFGWbvC6VJiAKeqJdBLwv8kPoiMqCzfzofBu0O7cwqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCMlAwPoF2K5HMGdircA%2BK0jkh2Rxh9rpTJUxP0%2FsxJ2bGLoIAkTm4InvdGei5CWN9V1AT7eendY1NrkPV9QEpG%2FR8ed96KxiPFreOodighI7qpxOmj1AwqQF43eJqD8HNqAKWOb2fo9D%2FBMAgLQbDhlNyEl4zNqNoXna126jduBzc4nRkQLDFZO%2FTbScLRLO2Arav4BB9XK8e466AMkVP7rmnSECgIr%2BWJnQmuPdlVCavP4WUcLW0fPQ6y7gj%2FWxTsWTtAiq1uLiNAEUYHNhdWGVlpsf%2FyJ7B%2BM1FdIQnla38Y5uOUxemgcz4Yoey8xw048JVy2E45K43kUdet5k4HpOqGnW6GKwOOH7lTg6cXCnKLQsHlbFvRzVylZoczQq4EchmhIV08lhzbVWymFb5CdS1RtNXDlGR970nABHFFm2FvGo9elRFIeKXsR290bm3r6PhytObsV%2FA3WN9px4Xb145gEulV48CxMihr2jkro2pdkVGsnTgpjyVdEKGL%2FTRMza4wGndLda4JsrXSLnvBzp1goXR%2FqNisitGCqG5VIjMQ3vTEVN4QYs95zLDMFQ3tCJLD1ctl1%2FwuGzKdMuBXi4PtvKmLYgMsrG1AT6utzVoCfHrlQi4q343HkTiCxoZX75OYipoaZmZwMOyg18oGOqUBTMrWuCmpkIcDkXiCjQOVy8TH%2BQHkqvhMQFJuhiDg5KlRMHzIUDaLRHigQUkE4UFVbXfA0GwWVj6WPUyupOa3nWWBpJf8ab%2BLqAeF5NkK6Pw%2B5zaghflNJOy0sdSv9XgVYzH0XKb71H%2BvmRP69cx%2BhI%2Bseb5F6uXsBj6Mxj%2FGbwVyt7rz7iGg5Cv%2F8ftOE11TOMbBf9C7DfmPhNYscVphUkT6wnX3&X-Amz-Signature=116c095181e5eb3fb24d5ef879816ea2f21a6a8afa44b070700c5f6e7c4b2619&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

