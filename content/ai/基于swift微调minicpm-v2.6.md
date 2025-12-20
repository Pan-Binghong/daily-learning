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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWV5KFR5%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcFJyQjEOh%2BA6YlwmRXNSilTSi%2Fhm3zUNY%2BUnJl8h4iAiAJ6Oxsgm91okuek9CP5p%2F%2Bjvmki1EE8gL04w1OmnBNbSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsFgYGVUJjjTZ73eYKtwDIkdRQXO5045j8Jj8zGOhAHEiANZ%2BSD181UBkATMA4A9c%2BpsE9gFxsqvKDP3t4d%2F0Cd8%2FxYrvjnrTCRQzIKDdxqUHWLLXD6N%2FPw7%2BTCoun8O6cBJ%2Bk5ToQ%2FicKrXpCiJih1drcAZPzi0fHQhd0dstGX%2BUHmprUWLnacY8N6hN5yUF8W1ivET1s1g7ils6fpsOJuVkBR3G15edUs5Vu2chUNb382bMT8i2MsHMXynNmfVDb4iHgCkseIktmSWd1a9z92QriZwwaPv%2FQRaWYhGUarN4PA2S7TEO%2Feb%2BUQAZuKxPwlsq53T89ASv9EmWKJJpUo4UppLnpPQjQe%2Bz7CSlWkBXUOj9JJft3tzzAWhnXdFVJowkASSIXQwXgRmfFasarIAYTFv5zDhFSBTaU2c8TebkmRioREhz%2FpmEZso%2BzF2XxhRTT1gIlQZ9T1bA8xOcu2xqu7rqeumy9D6ClidM9J3%2BxFKZQ0JZGs8aJKaIGCTixlwKVg4ag%2FXa3J7rHDUUSRKR3z9h7ievcsEIn0AxmJxkbiHyJjTAyXD%2BGI3xy8vPlqPNS9zD5MhMmOMMVk0baxXMesPrkMgU3ZmVi2iqjg81usfW9pXB3w1DMprqI69WN0Owe%2BBYNNJay1Yw3IWYygY6pgEa3LPFMwJsqpHfIH0DB2SuWEeNUR6x1JMe4pP8fIkrRyL8fn4hnV8mVRi%2BSitAVguDZYh7to87qGfgjypAnZ0ZxeKwjlu2A%2Ff%2BedRbFMn8l42wYfmVbPNxm4TrsIY5qxDXk7Wm7AJ8%2B43YR2n3s9pCHmaG2nwshGnxgYieiHITwHQAhzO37C06g30S7kYAIXr9aQiu0P2jY1%2FsCW8zhrBgLlF8HocW&X-Amz-Signature=89ced902e0b91bb0501444c84ec18a8f3c60bd3bd929a6045a05a4ab27bbf1e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWV5KFR5%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcFJyQjEOh%2BA6YlwmRXNSilTSi%2Fhm3zUNY%2BUnJl8h4iAiAJ6Oxsgm91okuek9CP5p%2F%2Bjvmki1EE8gL04w1OmnBNbSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsFgYGVUJjjTZ73eYKtwDIkdRQXO5045j8Jj8zGOhAHEiANZ%2BSD181UBkATMA4A9c%2BpsE9gFxsqvKDP3t4d%2F0Cd8%2FxYrvjnrTCRQzIKDdxqUHWLLXD6N%2FPw7%2BTCoun8O6cBJ%2Bk5ToQ%2FicKrXpCiJih1drcAZPzi0fHQhd0dstGX%2BUHmprUWLnacY8N6hN5yUF8W1ivET1s1g7ils6fpsOJuVkBR3G15edUs5Vu2chUNb382bMT8i2MsHMXynNmfVDb4iHgCkseIktmSWd1a9z92QriZwwaPv%2FQRaWYhGUarN4PA2S7TEO%2Feb%2BUQAZuKxPwlsq53T89ASv9EmWKJJpUo4UppLnpPQjQe%2Bz7CSlWkBXUOj9JJft3tzzAWhnXdFVJowkASSIXQwXgRmfFasarIAYTFv5zDhFSBTaU2c8TebkmRioREhz%2FpmEZso%2BzF2XxhRTT1gIlQZ9T1bA8xOcu2xqu7rqeumy9D6ClidM9J3%2BxFKZQ0JZGs8aJKaIGCTixlwKVg4ag%2FXa3J7rHDUUSRKR3z9h7ievcsEIn0AxmJxkbiHyJjTAyXD%2BGI3xy8vPlqPNS9zD5MhMmOMMVk0baxXMesPrkMgU3ZmVi2iqjg81usfW9pXB3w1DMprqI69WN0Owe%2BBYNNJay1Yw3IWYygY6pgEa3LPFMwJsqpHfIH0DB2SuWEeNUR6x1JMe4pP8fIkrRyL8fn4hnV8mVRi%2BSitAVguDZYh7to87qGfgjypAnZ0ZxeKwjlu2A%2Ff%2BedRbFMn8l42wYfmVbPNxm4TrsIY5qxDXk7Wm7AJ8%2B43YR2n3s9pCHmaG2nwshGnxgYieiHITwHQAhzO37C06g30S7kYAIXr9aQiu0P2jY1%2FsCW8zhrBgLlF8HocW&X-Amz-Signature=5ab3413d287d30d0b30d0306d6a8855057ab6c523ef1770ef22e763954a5d87b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWV5KFR5%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcFJyQjEOh%2BA6YlwmRXNSilTSi%2Fhm3zUNY%2BUnJl8h4iAiAJ6Oxsgm91okuek9CP5p%2F%2Bjvmki1EE8gL04w1OmnBNbSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsFgYGVUJjjTZ73eYKtwDIkdRQXO5045j8Jj8zGOhAHEiANZ%2BSD181UBkATMA4A9c%2BpsE9gFxsqvKDP3t4d%2F0Cd8%2FxYrvjnrTCRQzIKDdxqUHWLLXD6N%2FPw7%2BTCoun8O6cBJ%2Bk5ToQ%2FicKrXpCiJih1drcAZPzi0fHQhd0dstGX%2BUHmprUWLnacY8N6hN5yUF8W1ivET1s1g7ils6fpsOJuVkBR3G15edUs5Vu2chUNb382bMT8i2MsHMXynNmfVDb4iHgCkseIktmSWd1a9z92QriZwwaPv%2FQRaWYhGUarN4PA2S7TEO%2Feb%2BUQAZuKxPwlsq53T89ASv9EmWKJJpUo4UppLnpPQjQe%2Bz7CSlWkBXUOj9JJft3tzzAWhnXdFVJowkASSIXQwXgRmfFasarIAYTFv5zDhFSBTaU2c8TebkmRioREhz%2FpmEZso%2BzF2XxhRTT1gIlQZ9T1bA8xOcu2xqu7rqeumy9D6ClidM9J3%2BxFKZQ0JZGs8aJKaIGCTixlwKVg4ag%2FXa3J7rHDUUSRKR3z9h7ievcsEIn0AxmJxkbiHyJjTAyXD%2BGI3xy8vPlqPNS9zD5MhMmOMMVk0baxXMesPrkMgU3ZmVi2iqjg81usfW9pXB3w1DMprqI69WN0Owe%2BBYNNJay1Yw3IWYygY6pgEa3LPFMwJsqpHfIH0DB2SuWEeNUR6x1JMe4pP8fIkrRyL8fn4hnV8mVRi%2BSitAVguDZYh7to87qGfgjypAnZ0ZxeKwjlu2A%2Ff%2BedRbFMn8l42wYfmVbPNxm4TrsIY5qxDXk7Wm7AJ8%2B43YR2n3s9pCHmaG2nwshGnxgYieiHITwHQAhzO37C06g30S7kYAIXr9aQiu0P2jY1%2FsCW8zhrBgLlF8HocW&X-Amz-Signature=717db73c2580a2dab8b23ba89629eea0cadf630c4627f00d89dd28679616f8bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

