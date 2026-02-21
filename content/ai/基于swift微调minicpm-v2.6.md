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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KJQQ7LK%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCP7DaJ1b4PSsTmILS%2FdhjkZa9c52RS7Mux2T6RTQTnWQIgKQQM0sbR0Eq25G4K%2Fd%2Fnr%2BwPXBVc3Jt%2Fil%2BVMkAAH58qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHUwW3sJMKBvEtC1CrcA8WcqG32M5TNpmxxJlM2csq5iEQUIX2oTgnA5vSmEyE%2FNeTP1KF2Km2q1IrptDRJ%2Bb4Mdy4v3lJvIu%2B32p6PY78sP3HbCdOC5cG1U3IP1NC7iGsYX%2FWJxX1%2FoVzN4TJUrss%2BN325vn3vibAgAdpZOIYgiaMy5S7zcN1C4ERNOnNLR%2Fmm6g5K2FVyjbT3khbngi83oyIM5JYOYHORkO5lqtVRLzT5ipq0HAW5nZcONfXgQDu4OcQSOIxrIe5TCovlOmOU%2Bxth8lnPZpr%2FJA5KUj2NlZX%2B4S%2B4q1YZy6sT%2FjbFYCZ6grIZAB%2BAJYCM%2Bg%2Fapti4GBxo0JT6uqWozUgEIaHVDPHmnE5ZhygKy8XCa06Ym87pcFHdU%2Br9Kpke64sqqNEfpf4jhTj4wMiuhs%2FO5FgoWd9cCDeLEdHiXm0N4toGOR5aeK7x%2FeHGUWiZSIz5yZw2NqHBbodYBGh0rGTWs3R52gZ%2BygAheV4AwMrptcRUsuhdnJOE7aNlt2V7hNlZQuEnUlCA0%2FXd9bN%2BNwVhhlfJkFY88RUaKjm5lgXGyuBn4XDAxdNNIHXokBSFlE0bgLHzCLqBItdPxvKHQtiPhMf2E3ihjjy4MHprJ9cPkN1q9kk3GJij2bl5Pl5VMIy95MwGOqUBmKHlPjMfbLeN4MM3BZVzUJClZL1q%2Bdx2MZlOLQjLD8j3e1F0q%2Frib4ehjAZn2Id%2BB6K%2FfFpbMSRw6JTnAVVG%2Bqy2mC5l7C5hYJMXRZ8CSsGrJd%2FZbPnJSXA922pmG8dqELS3W674gHzWE%2B6SD4B9DV1xIFBGWiuxQJ4SGarmYSFDEThSKSKAS0qmfOYdb7hNDPcs9%2FkPWaht1etsuwsKJMAs36Y%2B&X-Amz-Signature=03067997cb83fe5348d0943d771deddbde701ab19fa7cc3ea2dd55f854941619&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KJQQ7LK%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCP7DaJ1b4PSsTmILS%2FdhjkZa9c52RS7Mux2T6RTQTnWQIgKQQM0sbR0Eq25G4K%2Fd%2Fnr%2BwPXBVc3Jt%2Fil%2BVMkAAH58qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHUwW3sJMKBvEtC1CrcA8WcqG32M5TNpmxxJlM2csq5iEQUIX2oTgnA5vSmEyE%2FNeTP1KF2Km2q1IrptDRJ%2Bb4Mdy4v3lJvIu%2B32p6PY78sP3HbCdOC5cG1U3IP1NC7iGsYX%2FWJxX1%2FoVzN4TJUrss%2BN325vn3vibAgAdpZOIYgiaMy5S7zcN1C4ERNOnNLR%2Fmm6g5K2FVyjbT3khbngi83oyIM5JYOYHORkO5lqtVRLzT5ipq0HAW5nZcONfXgQDu4OcQSOIxrIe5TCovlOmOU%2Bxth8lnPZpr%2FJA5KUj2NlZX%2B4S%2B4q1YZy6sT%2FjbFYCZ6grIZAB%2BAJYCM%2Bg%2Fapti4GBxo0JT6uqWozUgEIaHVDPHmnE5ZhygKy8XCa06Ym87pcFHdU%2Br9Kpke64sqqNEfpf4jhTj4wMiuhs%2FO5FgoWd9cCDeLEdHiXm0N4toGOR5aeK7x%2FeHGUWiZSIz5yZw2NqHBbodYBGh0rGTWs3R52gZ%2BygAheV4AwMrptcRUsuhdnJOE7aNlt2V7hNlZQuEnUlCA0%2FXd9bN%2BNwVhhlfJkFY88RUaKjm5lgXGyuBn4XDAxdNNIHXokBSFlE0bgLHzCLqBItdPxvKHQtiPhMf2E3ihjjy4MHprJ9cPkN1q9kk3GJij2bl5Pl5VMIy95MwGOqUBmKHlPjMfbLeN4MM3BZVzUJClZL1q%2Bdx2MZlOLQjLD8j3e1F0q%2Frib4ehjAZn2Id%2BB6K%2FfFpbMSRw6JTnAVVG%2Bqy2mC5l7C5hYJMXRZ8CSsGrJd%2FZbPnJSXA922pmG8dqELS3W674gHzWE%2B6SD4B9DV1xIFBGWiuxQJ4SGarmYSFDEThSKSKAS0qmfOYdb7hNDPcs9%2FkPWaht1etsuwsKJMAs36Y%2B&X-Amz-Signature=ac249052836a544b4f4916c7504789dc03f0bcbac1ec0bc4c994c7855ab867cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KJQQ7LK%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCP7DaJ1b4PSsTmILS%2FdhjkZa9c52RS7Mux2T6RTQTnWQIgKQQM0sbR0Eq25G4K%2Fd%2Fnr%2BwPXBVc3Jt%2Fil%2BVMkAAH58qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHUwW3sJMKBvEtC1CrcA8WcqG32M5TNpmxxJlM2csq5iEQUIX2oTgnA5vSmEyE%2FNeTP1KF2Km2q1IrptDRJ%2Bb4Mdy4v3lJvIu%2B32p6PY78sP3HbCdOC5cG1U3IP1NC7iGsYX%2FWJxX1%2FoVzN4TJUrss%2BN325vn3vibAgAdpZOIYgiaMy5S7zcN1C4ERNOnNLR%2Fmm6g5K2FVyjbT3khbngi83oyIM5JYOYHORkO5lqtVRLzT5ipq0HAW5nZcONfXgQDu4OcQSOIxrIe5TCovlOmOU%2Bxth8lnPZpr%2FJA5KUj2NlZX%2B4S%2B4q1YZy6sT%2FjbFYCZ6grIZAB%2BAJYCM%2Bg%2Fapti4GBxo0JT6uqWozUgEIaHVDPHmnE5ZhygKy8XCa06Ym87pcFHdU%2Br9Kpke64sqqNEfpf4jhTj4wMiuhs%2FO5FgoWd9cCDeLEdHiXm0N4toGOR5aeK7x%2FeHGUWiZSIz5yZw2NqHBbodYBGh0rGTWs3R52gZ%2BygAheV4AwMrptcRUsuhdnJOE7aNlt2V7hNlZQuEnUlCA0%2FXd9bN%2BNwVhhlfJkFY88RUaKjm5lgXGyuBn4XDAxdNNIHXokBSFlE0bgLHzCLqBItdPxvKHQtiPhMf2E3ihjjy4MHprJ9cPkN1q9kk3GJij2bl5Pl5VMIy95MwGOqUBmKHlPjMfbLeN4MM3BZVzUJClZL1q%2Bdx2MZlOLQjLD8j3e1F0q%2Frib4ehjAZn2Id%2BB6K%2FfFpbMSRw6JTnAVVG%2Bqy2mC5l7C5hYJMXRZ8CSsGrJd%2FZbPnJSXA922pmG8dqELS3W674gHzWE%2B6SD4B9DV1xIFBGWiuxQJ4SGarmYSFDEThSKSKAS0qmfOYdb7hNDPcs9%2FkPWaht1etsuwsKJMAs36Y%2B&X-Amz-Signature=644af3a6b94009dc6928624232ddc5becbc44df1fe3e483f83af195c3a4fcf04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

