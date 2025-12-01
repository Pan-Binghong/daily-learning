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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFCQMRG5%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDCWVQ0SIUo%2FxBiD8FNc85wjDaPFCu0J2O1YUbS5drJxAIgQ6t7dym2MyaxRT1Y007osrqRfSaQ2bUqIMpCX0QFf78qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrwpHvOkHT1RiZgPyrcA6Wsky3SoD3XgflWtFgRc73VBsRxu1kYPc3zsHR5cpTZz16WrD59Dequxpwyz6RZaF2XAzq%2B1EuuSZJb2iAaQJgUh4Cdt11mxIMjIkzNYD9RjGEHdjyCXBVT%2B8X46uiJLQQoqnSdPoczQv0RFDwJc0QfVuWHB1fNSX6vkkNWGAQgcX3VQ5%2Fsl8Cr4IGPlc99OUfIR5Invq8%2Bkoag6uKY7ehyPzNHonAJSccE%2BkSlpW16ouLAvKlkpdCLgz4YNPDVz9udiCzUlf1ip9GXbexQYRSBrpKpCIXexRwe2cFCFaMGNn0dHPwUWI92AvXH0lchPU7w58%2BFaDJ2fl2yrwvLADViDB2MXkchLcnvHk3kIsPf0%2BopJtUWZ8hFumh%2BbM6rg14IeD9CcOOsyYW6fAxmu41xkK7Piw5GEM4vVLNVbEWj8UvFQ8UsnyWxdSR7%2FamtkE6rVBL03D8rouF0mIFy8rkJOU1wVyO6xCdjuNEwumrTaIMa9dDdBoKx1KUrqLeLatEKT3%2Bz6U1x%2FppC5lsi%2FvUBucLvBgZO8yfVei3fzA%2BDC%2BKFbAYivQHkNmQOujAuJcgNO%2B95E1mgeA8HvYOVmp0u1KqockLXFulOiS8oR3YiL%2FDgxdt3JoA%2BwCOBMIX%2FsskGOqUBNOeCZmYn7ObzxE7IwrbNSNm2YBL46dsEhzCBGbatJHJlTRn%2BwjKFnsyXo16c5pzwZf4r1Zz6sLsSaYsyO6YN0KEZWzv%2BYvoPhDz1%2FOMcwkz4zP4s1py9AId1IUDHOflYXsCPjRTSJL6CGG2otgIFAsSxfEQdxrW733TK8097a6aS0pKzdv%2FY0AhjW%2B558nctSYMgx0VfVQsrUEv23CqUYTBHefMD&X-Amz-Signature=aa9d4a43f448f35bde0def5fcf03b38d489f05c78e51772e218272d0295ae9bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFCQMRG5%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDCWVQ0SIUo%2FxBiD8FNc85wjDaPFCu0J2O1YUbS5drJxAIgQ6t7dym2MyaxRT1Y007osrqRfSaQ2bUqIMpCX0QFf78qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrwpHvOkHT1RiZgPyrcA6Wsky3SoD3XgflWtFgRc73VBsRxu1kYPc3zsHR5cpTZz16WrD59Dequxpwyz6RZaF2XAzq%2B1EuuSZJb2iAaQJgUh4Cdt11mxIMjIkzNYD9RjGEHdjyCXBVT%2B8X46uiJLQQoqnSdPoczQv0RFDwJc0QfVuWHB1fNSX6vkkNWGAQgcX3VQ5%2Fsl8Cr4IGPlc99OUfIR5Invq8%2Bkoag6uKY7ehyPzNHonAJSccE%2BkSlpW16ouLAvKlkpdCLgz4YNPDVz9udiCzUlf1ip9GXbexQYRSBrpKpCIXexRwe2cFCFaMGNn0dHPwUWI92AvXH0lchPU7w58%2BFaDJ2fl2yrwvLADViDB2MXkchLcnvHk3kIsPf0%2BopJtUWZ8hFumh%2BbM6rg14IeD9CcOOsyYW6fAxmu41xkK7Piw5GEM4vVLNVbEWj8UvFQ8UsnyWxdSR7%2FamtkE6rVBL03D8rouF0mIFy8rkJOU1wVyO6xCdjuNEwumrTaIMa9dDdBoKx1KUrqLeLatEKT3%2Bz6U1x%2FppC5lsi%2FvUBucLvBgZO8yfVei3fzA%2BDC%2BKFbAYivQHkNmQOujAuJcgNO%2B95E1mgeA8HvYOVmp0u1KqockLXFulOiS8oR3YiL%2FDgxdt3JoA%2BwCOBMIX%2FsskGOqUBNOeCZmYn7ObzxE7IwrbNSNm2YBL46dsEhzCBGbatJHJlTRn%2BwjKFnsyXo16c5pzwZf4r1Zz6sLsSaYsyO6YN0KEZWzv%2BYvoPhDz1%2FOMcwkz4zP4s1py9AId1IUDHOflYXsCPjRTSJL6CGG2otgIFAsSxfEQdxrW733TK8097a6aS0pKzdv%2FY0AhjW%2B558nctSYMgx0VfVQsrUEv23CqUYTBHefMD&X-Amz-Signature=9a908b454875c219d5ffb0f8cc97573286d98ebfb1eb689da36c68671d459899&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFCQMRG5%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDCWVQ0SIUo%2FxBiD8FNc85wjDaPFCu0J2O1YUbS5drJxAIgQ6t7dym2MyaxRT1Y007osrqRfSaQ2bUqIMpCX0QFf78qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrwpHvOkHT1RiZgPyrcA6Wsky3SoD3XgflWtFgRc73VBsRxu1kYPc3zsHR5cpTZz16WrD59Dequxpwyz6RZaF2XAzq%2B1EuuSZJb2iAaQJgUh4Cdt11mxIMjIkzNYD9RjGEHdjyCXBVT%2B8X46uiJLQQoqnSdPoczQv0RFDwJc0QfVuWHB1fNSX6vkkNWGAQgcX3VQ5%2Fsl8Cr4IGPlc99OUfIR5Invq8%2Bkoag6uKY7ehyPzNHonAJSccE%2BkSlpW16ouLAvKlkpdCLgz4YNPDVz9udiCzUlf1ip9GXbexQYRSBrpKpCIXexRwe2cFCFaMGNn0dHPwUWI92AvXH0lchPU7w58%2BFaDJ2fl2yrwvLADViDB2MXkchLcnvHk3kIsPf0%2BopJtUWZ8hFumh%2BbM6rg14IeD9CcOOsyYW6fAxmu41xkK7Piw5GEM4vVLNVbEWj8UvFQ8UsnyWxdSR7%2FamtkE6rVBL03D8rouF0mIFy8rkJOU1wVyO6xCdjuNEwumrTaIMa9dDdBoKx1KUrqLeLatEKT3%2Bz6U1x%2FppC5lsi%2FvUBucLvBgZO8yfVei3fzA%2BDC%2BKFbAYivQHkNmQOujAuJcgNO%2B95E1mgeA8HvYOVmp0u1KqockLXFulOiS8oR3YiL%2FDgxdt3JoA%2BwCOBMIX%2FsskGOqUBNOeCZmYn7ObzxE7IwrbNSNm2YBL46dsEhzCBGbatJHJlTRn%2BwjKFnsyXo16c5pzwZf4r1Zz6sLsSaYsyO6YN0KEZWzv%2BYvoPhDz1%2FOMcwkz4zP4s1py9AId1IUDHOflYXsCPjRTSJL6CGG2otgIFAsSxfEQdxrW733TK8097a6aS0pKzdv%2FY0AhjW%2B558nctSYMgx0VfVQsrUEv23CqUYTBHefMD&X-Amz-Signature=c0c6cadab1f1ed6ffd10dbc147c8eb9c10b8c1a04063a1f971dbb80fe440bebd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

