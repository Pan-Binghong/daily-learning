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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLDO3MV%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIHyFJbtoPtbjh0fjnweYYnRhiMOD%2F7JYhzKuWlEjEaGnAiBIOK8l2eU9n9g2CQAVREeEQctr%2FgEF4BiJpX3xr1fZgCqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMokftptWWmBh4tA8IKtwDNtPA4QyXJ1Fya6IDArX8237rI54%2FkKCTpP0cNB6yhSzCi86o6oPmLsnHY9CsJaliBzCfSpMv0DAVJv%2FuJef%2B0HquvBYIc1j%2B2yU9Tu3NrH%2FJkeiy%2FHjsGq5%2FFala2L2%2FziH7CPBJqUz%2BI3DKa6sdhb49oCNoPjmX754oN%2FnGVkbhVrYgN%2Bmr6%2FvrSZ3e%2FFvRMhjfp0%2F7mLrkbXGokdB9Hi0cjP7pOFBJFk50YI2vnlL9SDqG%2BJbudk23DQBIKqQ%2B%2BiHcVbKdSsR9H5oZSFiTeQExsR96jhgnXAWldBJ0wVXbW57IL88i2ootZnx8XN0yBnE%2F9OSowd9yN8K53B55oK35aHyaIEPdwl6Aug%2Bb8lW7E32Sp8duqNU%2BbpKj0mQalQ2C7PST8Wl%2FlWE%2BTQlQSUipnKEC%2BUBh47s5sVbmG%2FxIn%2BKIt5FVLmhfMVRppcQBJjYr9TPAG63WqxLCN8VFgLNMcOGEGqmIhT6kMEPAslK%2FhTt%2FFxqh90KuAdDuBwUlNoIHDvWrWk9M5Izrcf8yTDEqSD6XdLnJkxeLlV5ag5XswPhvKrbIumQudRXmXygMY7Zh6F6U8%2Fi5So5YnY0NdcocQhqJ0e2fyBg%2FZXD8dI1br28iwQzdVHxveLww1L3dzQY6pgHV79F0JiUOLKEo9MxmUTK9hFv%2FPHTxd3Tj8Y8msBvn9E0iyMZRMRLQ23eMKlqEWkK%2FK2PYzW%2B8z3GniePLGXRYpMTDbABnbEP6Kq2lNXaka%2Bj1IRFSXBfmxvlsrZ2LSQZ6bFLTD%2BsSXXhgcOPV%2FuDtqX9LVMyCsCtNVpPuXRRU%2BcBb%2Blp7sivzDNr6RkFlqB9%2FuAbiQNXv%2B5qJY%2BsmD6NXv162m315&X-Amz-Signature=9df382f854b7e3025b95cda92fc64bbe5c8c47b9283a044b2068498814bb1822&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLDO3MV%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIHyFJbtoPtbjh0fjnweYYnRhiMOD%2F7JYhzKuWlEjEaGnAiBIOK8l2eU9n9g2CQAVREeEQctr%2FgEF4BiJpX3xr1fZgCqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMokftptWWmBh4tA8IKtwDNtPA4QyXJ1Fya6IDArX8237rI54%2FkKCTpP0cNB6yhSzCi86o6oPmLsnHY9CsJaliBzCfSpMv0DAVJv%2FuJef%2B0HquvBYIc1j%2B2yU9Tu3NrH%2FJkeiy%2FHjsGq5%2FFala2L2%2FziH7CPBJqUz%2BI3DKa6sdhb49oCNoPjmX754oN%2FnGVkbhVrYgN%2Bmr6%2FvrSZ3e%2FFvRMhjfp0%2F7mLrkbXGokdB9Hi0cjP7pOFBJFk50YI2vnlL9SDqG%2BJbudk23DQBIKqQ%2B%2BiHcVbKdSsR9H5oZSFiTeQExsR96jhgnXAWldBJ0wVXbW57IL88i2ootZnx8XN0yBnE%2F9OSowd9yN8K53B55oK35aHyaIEPdwl6Aug%2Bb8lW7E32Sp8duqNU%2BbpKj0mQalQ2C7PST8Wl%2FlWE%2BTQlQSUipnKEC%2BUBh47s5sVbmG%2FxIn%2BKIt5FVLmhfMVRppcQBJjYr9TPAG63WqxLCN8VFgLNMcOGEGqmIhT6kMEPAslK%2FhTt%2FFxqh90KuAdDuBwUlNoIHDvWrWk9M5Izrcf8yTDEqSD6XdLnJkxeLlV5ag5XswPhvKrbIumQudRXmXygMY7Zh6F6U8%2Fi5So5YnY0NdcocQhqJ0e2fyBg%2FZXD8dI1br28iwQzdVHxveLww1L3dzQY6pgHV79F0JiUOLKEo9MxmUTK9hFv%2FPHTxd3Tj8Y8msBvn9E0iyMZRMRLQ23eMKlqEWkK%2FK2PYzW%2B8z3GniePLGXRYpMTDbABnbEP6Kq2lNXaka%2Bj1IRFSXBfmxvlsrZ2LSQZ6bFLTD%2BsSXXhgcOPV%2FuDtqX9LVMyCsCtNVpPuXRRU%2BcBb%2Blp7sivzDNr6RkFlqB9%2FuAbiQNXv%2B5qJY%2BsmD6NXv162m315&X-Amz-Signature=1b7c0591541c3d72a01b6d83eaf019c41ed340c2abd58cda441b839272180100&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLDO3MV%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIHyFJbtoPtbjh0fjnweYYnRhiMOD%2F7JYhzKuWlEjEaGnAiBIOK8l2eU9n9g2CQAVREeEQctr%2FgEF4BiJpX3xr1fZgCqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMokftptWWmBh4tA8IKtwDNtPA4QyXJ1Fya6IDArX8237rI54%2FkKCTpP0cNB6yhSzCi86o6oPmLsnHY9CsJaliBzCfSpMv0DAVJv%2FuJef%2B0HquvBYIc1j%2B2yU9Tu3NrH%2FJkeiy%2FHjsGq5%2FFala2L2%2FziH7CPBJqUz%2BI3DKa6sdhb49oCNoPjmX754oN%2FnGVkbhVrYgN%2Bmr6%2FvrSZ3e%2FFvRMhjfp0%2F7mLrkbXGokdB9Hi0cjP7pOFBJFk50YI2vnlL9SDqG%2BJbudk23DQBIKqQ%2B%2BiHcVbKdSsR9H5oZSFiTeQExsR96jhgnXAWldBJ0wVXbW57IL88i2ootZnx8XN0yBnE%2F9OSowd9yN8K53B55oK35aHyaIEPdwl6Aug%2Bb8lW7E32Sp8duqNU%2BbpKj0mQalQ2C7PST8Wl%2FlWE%2BTQlQSUipnKEC%2BUBh47s5sVbmG%2FxIn%2BKIt5FVLmhfMVRppcQBJjYr9TPAG63WqxLCN8VFgLNMcOGEGqmIhT6kMEPAslK%2FhTt%2FFxqh90KuAdDuBwUlNoIHDvWrWk9M5Izrcf8yTDEqSD6XdLnJkxeLlV5ag5XswPhvKrbIumQudRXmXygMY7Zh6F6U8%2Fi5So5YnY0NdcocQhqJ0e2fyBg%2FZXD8dI1br28iwQzdVHxveLww1L3dzQY6pgHV79F0JiUOLKEo9MxmUTK9hFv%2FPHTxd3Tj8Y8msBvn9E0iyMZRMRLQ23eMKlqEWkK%2FK2PYzW%2B8z3GniePLGXRYpMTDbABnbEP6Kq2lNXaka%2Bj1IRFSXBfmxvlsrZ2LSQZ6bFLTD%2BsSXXhgcOPV%2FuDtqX9LVMyCsCtNVpPuXRRU%2BcBb%2Blp7sivzDNr6RkFlqB9%2FuAbiQNXv%2B5qJY%2BsmD6NXv162m315&X-Amz-Signature=045ca99698e499b3211d60ccc1b4a6e42f561bc4034102f2a3e923d371eb66c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

