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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBHMZTBH%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2Frw7VWDLpR5VTARG8ToDbBMMdU2CdbRMsWt9AOKiUSAIhAPSR1HDaThYlqWbU75b7A%2F4r%2F%2BA8iZXWfo0Cc7nrKQY%2FKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9gNFv2j6Av%2FMM80Qq3AMyHsbygB7cFsPum7UyIVD%2FlmP7NwFrcpCd1Cv8pZgkrmTyBcFVdd7ZN3RVRcIGGvj0n4ONSmITssYGHV8cHYkW76ojzkcxxz8oJKkkCZ6RBSX3pkvh7WYSg%2FqN35vO6nx9Jh7fgwdPp6J1ne5jDJFv6fsmtV9snv3gKllBecHMqdbBME6kAPbT6Rjdsa80OvEnubqyzefU2%2BC7dzA4MOBT%2FGq45AhdOLtPOLSGPe4FGMgpUwTabjOU1EBu%2FzEvf0VLU7EPg%2F6PGupt0I6BDRZbXEEvluRsw5fiU3A1lM7ysFJ3FDDHHWZGhO4iOcKPKjnKYFIQkCYpNJ2ePTy4kTGKH3P8PaMuCnDyFZQU5yoCIvWelQtjqMBHfyrwrWh3ti9Jr%2F%2BLunyNVhAMYSx7JYg5HKImEaD63%2BJ4MF84r58zpkhKnxOMxD7ZxC%2FuF%2BMXpJmXYFocS0h2iwOCdBnj%2BnOCa7bNXiaEmvJLiUjSsObYBmhBbUm4u943YFTHDObPSZ42v1%2BP5BUJTt6yNYNmg9WMyMUsPLtvY8GmA%2BY%2FVUrTA2v8v6PNILbmCONNjNo9fxtT3EMAFDuMHXeNKWGCFXX3DiM4F2y%2Fc01eMm2mM2LnUSNadDmUITVs%2BjxmezDchZjKBjqkAZffFXoD9jwPL26d2p5dcZLsSt2mkYdqJv5LEJmnmLe5f7IbPmLwyw5MjfZxgcDRXbKfnTaGt3Ls7wF6K8eZAajr7mvw8Wx9h7MvdL5mDFc%2BghI2WyYDfT0G%2BIydxWBeTbOT9R%2F8QIY7o%2F8LdnS1pglEh2tKaJv%2BzTqtaIIm%2F1fP2liWCvJld%2FN6exMsyl5iyAO6%2BsmhBJRAk3OmsoOCwMQrrI4b&X-Amz-Signature=e1461e38f07a37f5182656cd59e9f17555f18373273958e52d3c1fe6b564a6f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBHMZTBH%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2Frw7VWDLpR5VTARG8ToDbBMMdU2CdbRMsWt9AOKiUSAIhAPSR1HDaThYlqWbU75b7A%2F4r%2F%2BA8iZXWfo0Cc7nrKQY%2FKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9gNFv2j6Av%2FMM80Qq3AMyHsbygB7cFsPum7UyIVD%2FlmP7NwFrcpCd1Cv8pZgkrmTyBcFVdd7ZN3RVRcIGGvj0n4ONSmITssYGHV8cHYkW76ojzkcxxz8oJKkkCZ6RBSX3pkvh7WYSg%2FqN35vO6nx9Jh7fgwdPp6J1ne5jDJFv6fsmtV9snv3gKllBecHMqdbBME6kAPbT6Rjdsa80OvEnubqyzefU2%2BC7dzA4MOBT%2FGq45AhdOLtPOLSGPe4FGMgpUwTabjOU1EBu%2FzEvf0VLU7EPg%2F6PGupt0I6BDRZbXEEvluRsw5fiU3A1lM7ysFJ3FDDHHWZGhO4iOcKPKjnKYFIQkCYpNJ2ePTy4kTGKH3P8PaMuCnDyFZQU5yoCIvWelQtjqMBHfyrwrWh3ti9Jr%2F%2BLunyNVhAMYSx7JYg5HKImEaD63%2BJ4MF84r58zpkhKnxOMxD7ZxC%2FuF%2BMXpJmXYFocS0h2iwOCdBnj%2BnOCa7bNXiaEmvJLiUjSsObYBmhBbUm4u943YFTHDObPSZ42v1%2BP5BUJTt6yNYNmg9WMyMUsPLtvY8GmA%2BY%2FVUrTA2v8v6PNILbmCONNjNo9fxtT3EMAFDuMHXeNKWGCFXX3DiM4F2y%2Fc01eMm2mM2LnUSNadDmUITVs%2BjxmezDchZjKBjqkAZffFXoD9jwPL26d2p5dcZLsSt2mkYdqJv5LEJmnmLe5f7IbPmLwyw5MjfZxgcDRXbKfnTaGt3Ls7wF6K8eZAajr7mvw8Wx9h7MvdL5mDFc%2BghI2WyYDfT0G%2BIydxWBeTbOT9R%2F8QIY7o%2F8LdnS1pglEh2tKaJv%2BzTqtaIIm%2F1fP2liWCvJld%2FN6exMsyl5iyAO6%2BsmhBJRAk3OmsoOCwMQrrI4b&X-Amz-Signature=75592516434c2f37407d734252cbb8194d56812877bd19781471908716cb58ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

