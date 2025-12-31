---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4CGOFZI%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIChRmHuhuhqKsISoR1yQnBbvJ2pcc4KsbiJvqfCojJnnAiEAhCKiSignzyN0ESN4jHyO3rhd4aYJzswbzPJUIwqL5MkqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD1qdHraVq9vR9LopSrcA5rpLhWrQMo5s8ASEE1GcJzISNSPz1xnN7sk5G93SVhSlj5GuCM5ahIMxiP9upo2Zp8dC52atAbWOXQR%2FHrPh5bEXDIQMIZmzjsfrWSTbfFTmbOzgLKZZDmgZ3Ol0zt8rUlr6LoyZKcU%2B%2BrpYofwYLRlid6yZkfJPKZI5C19alGUBtHNe4VR0cTxoWhrRM8BMhW%2F7bfBbiLnsSjhfp1quvWrLmSajBxLxTsC3bgQ3uxEXqt09vCWBnivt6tmYuJOa1BHXKnlcjXadE7ktjsiPeOugB3SmTMmNmRAg2AECHl2t3IYwD5SzI35lI8ekwFlOvFPcZ491lRJaoi3sBhcmq0Rc00HJDWHIDNxEba5nKu52KF71WyJxLuvT7mAVB8kUcSdSPLYSQOTNHzhxtrAeeBIxKnAsQGC0CoI30Nnns0YERH24kg19dysZw8LcxYWx7z27KS6ahbzMMCF%2F1gRTRCsswWQgiGdi%2F%2FT1rfEHvN2xBEvCEH2mQ9%2Bjqnggz7IxwZfg1jvZxcdYUoy%2BqBiqOgsqiHczb9X7SukhQA71V8pNw612tnh7ZeXtva%2BWRGhw4D0KKvvM6otllG4j3clFuF%2BesEMKFeZEi00a4QcZvUh5KiC82T3qRzYtR0HMM720coGOqUBAYXNSw7F06AItaQ6suU44RnNiZxMd3GsCJ0Wk3ZZOM0Y5htdqpj9F6s70VHxNOL9oCT2gR8xgHG1OCEI3CYskejBwpedspBoCaN4lJPdO9kR6dln6tCmQd%2Bx%2F2sf2rEm34vzuqCqpzUH%2FrnNIg8jEFnvGKIbAjKivCPxhWs69aB3SCsJI9iArVY4BRHl6AOnXPMl8ucfV7gkJ%2FNSLGlqgNLZpbMc&X-Amz-Signature=17230c1e03774c89f09313d84966c7c9ac67c0ee19d0be60a220738c4acf5aeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4CGOFZI%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIChRmHuhuhqKsISoR1yQnBbvJ2pcc4KsbiJvqfCojJnnAiEAhCKiSignzyN0ESN4jHyO3rhd4aYJzswbzPJUIwqL5MkqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD1qdHraVq9vR9LopSrcA5rpLhWrQMo5s8ASEE1GcJzISNSPz1xnN7sk5G93SVhSlj5GuCM5ahIMxiP9upo2Zp8dC52atAbWOXQR%2FHrPh5bEXDIQMIZmzjsfrWSTbfFTmbOzgLKZZDmgZ3Ol0zt8rUlr6LoyZKcU%2B%2BrpYofwYLRlid6yZkfJPKZI5C19alGUBtHNe4VR0cTxoWhrRM8BMhW%2F7bfBbiLnsSjhfp1quvWrLmSajBxLxTsC3bgQ3uxEXqt09vCWBnivt6tmYuJOa1BHXKnlcjXadE7ktjsiPeOugB3SmTMmNmRAg2AECHl2t3IYwD5SzI35lI8ekwFlOvFPcZ491lRJaoi3sBhcmq0Rc00HJDWHIDNxEba5nKu52KF71WyJxLuvT7mAVB8kUcSdSPLYSQOTNHzhxtrAeeBIxKnAsQGC0CoI30Nnns0YERH24kg19dysZw8LcxYWx7z27KS6ahbzMMCF%2F1gRTRCsswWQgiGdi%2F%2FT1rfEHvN2xBEvCEH2mQ9%2Bjqnggz7IxwZfg1jvZxcdYUoy%2BqBiqOgsqiHczb9X7SukhQA71V8pNw612tnh7ZeXtva%2BWRGhw4D0KKvvM6otllG4j3clFuF%2BesEMKFeZEi00a4QcZvUh5KiC82T3qRzYtR0HMM720coGOqUBAYXNSw7F06AItaQ6suU44RnNiZxMd3GsCJ0Wk3ZZOM0Y5htdqpj9F6s70VHxNOL9oCT2gR8xgHG1OCEI3CYskejBwpedspBoCaN4lJPdO9kR6dln6tCmQd%2Bx%2F2sf2rEm34vzuqCqpzUH%2FrnNIg8jEFnvGKIbAjKivCPxhWs69aB3SCsJI9iArVY4BRHl6AOnXPMl8ucfV7gkJ%2FNSLGlqgNLZpbMc&X-Amz-Signature=9605d020e6cff74f2bd24f8663683e8d0c94849da8e179531df8dbafd4998c27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

