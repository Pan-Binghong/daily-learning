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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4MRXV%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClp1pg9cd4qYhw%2Bd4Ns%2FP8frcWIGrT1pZSBW4XEGU6yAiBeaTJ2nH9R3Gz%2Bl1BDda2pDzZWlsFXNuT9gpeGNKElMir%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM2%2B7u2p28XzfA8pYXKtwDliAyo64rKvitGSdaGEAwaOnlvT%2FwgrNZaNOcl4Qi%2BkLaVNqxB7lpga31lBpq9veYJKMR2uU3S2tcG%2BFcDJbYqGzBpge5BpHtlPYdkc%2BLyXk7QwNWTpagWiczmFyNEcyqcaZMgo5YpPRWG%2FE9IGmdsK7JecEgn8ug%2BSFkeQVZN62ahpzUCebMWio1NiV0n8qnG8XdeCXtMr5%2Bcdmongr30C7XTILGEYV%2BM81WIpdl3xvg6KSUhEoulKBLFzYXe%2F10tSHPHZKxiAlWLvEeiSFlTK5uoyNuYlsCHZG0JnbjEFzp8A6lZdkBQ5cKEREhebj87dyUt6ORPj5dXuvbVRVdEuoelhzLSM7G9xFQF2b0MCnCVZ4WXsP4KMgZPTSUZaANUWsryxFrwwGdEETlPNMER%2BTswWCpc5w%2FgMGzfid45FWWFVKNniAs4tWEO0anMGgUT6y%2B8q4VvIJBG5x%2BLsPayUgFKcVbKT4Mqhit%2FQ1pm3ENjG9CFdi75fuZ3AQbz1VvWtHDwo%2FcJvxj66qb0rUFxaRMHEAW649E3duoy1EA1ArVlEYqTDvTYwU5h8lJ%2BM0fvseo%2FJtVveuPI20c7XVC4uIHHUPgvst7E%2FoCVQGdoH4p%2BlGAp92vSUajdIEw7KKyzgY6pgG1Le%2F3cEir6n1NeqEYUQvvoLdxCIIFIy3XH3ntoY2w5XagbFCcUnHbTHaJska38ZFw0q25IwaBLaJvQpSUfgO75ciRJ3mDJGF5JvuxVyIxFPouenoKi9WpqQnGvsT1zXFQdUuPzQUeK%2BjGrRCNMB4gOBHj9LEzm15fdRAhs4oUIf705XRvNBM0l9QpsPiKqFL1%2BcSf5FFheb1cpRuVjLiKteWv1mnz&X-Amz-Signature=2bbc3ad5a1ccdb78e10599b295cf6a0e5396862fb018033d424d421fd7199185&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4MRXV%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClp1pg9cd4qYhw%2Bd4Ns%2FP8frcWIGrT1pZSBW4XEGU6yAiBeaTJ2nH9R3Gz%2Bl1BDda2pDzZWlsFXNuT9gpeGNKElMir%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM2%2B7u2p28XzfA8pYXKtwDliAyo64rKvitGSdaGEAwaOnlvT%2FwgrNZaNOcl4Qi%2BkLaVNqxB7lpga31lBpq9veYJKMR2uU3S2tcG%2BFcDJbYqGzBpge5BpHtlPYdkc%2BLyXk7QwNWTpagWiczmFyNEcyqcaZMgo5YpPRWG%2FE9IGmdsK7JecEgn8ug%2BSFkeQVZN62ahpzUCebMWio1NiV0n8qnG8XdeCXtMr5%2Bcdmongr30C7XTILGEYV%2BM81WIpdl3xvg6KSUhEoulKBLFzYXe%2F10tSHPHZKxiAlWLvEeiSFlTK5uoyNuYlsCHZG0JnbjEFzp8A6lZdkBQ5cKEREhebj87dyUt6ORPj5dXuvbVRVdEuoelhzLSM7G9xFQF2b0MCnCVZ4WXsP4KMgZPTSUZaANUWsryxFrwwGdEETlPNMER%2BTswWCpc5w%2FgMGzfid45FWWFVKNniAs4tWEO0anMGgUT6y%2B8q4VvIJBG5x%2BLsPayUgFKcVbKT4Mqhit%2FQ1pm3ENjG9CFdi75fuZ3AQbz1VvWtHDwo%2FcJvxj66qb0rUFxaRMHEAW649E3duoy1EA1ArVlEYqTDvTYwU5h8lJ%2BM0fvseo%2FJtVveuPI20c7XVC4uIHHUPgvst7E%2FoCVQGdoH4p%2BlGAp92vSUajdIEw7KKyzgY6pgG1Le%2F3cEir6n1NeqEYUQvvoLdxCIIFIy3XH3ntoY2w5XagbFCcUnHbTHaJska38ZFw0q25IwaBLaJvQpSUfgO75ciRJ3mDJGF5JvuxVyIxFPouenoKi9WpqQnGvsT1zXFQdUuPzQUeK%2BjGrRCNMB4gOBHj9LEzm15fdRAhs4oUIf705XRvNBM0l9QpsPiKqFL1%2BcSf5FFheb1cpRuVjLiKteWv1mnz&X-Amz-Signature=ffeebdd158b02d1e7de43fe11b0cfd678be85c8d6f7671feb1e3e1df0573d546&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4MRXV%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClp1pg9cd4qYhw%2Bd4Ns%2FP8frcWIGrT1pZSBW4XEGU6yAiBeaTJ2nH9R3Gz%2Bl1BDda2pDzZWlsFXNuT9gpeGNKElMir%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM2%2B7u2p28XzfA8pYXKtwDliAyo64rKvitGSdaGEAwaOnlvT%2FwgrNZaNOcl4Qi%2BkLaVNqxB7lpga31lBpq9veYJKMR2uU3S2tcG%2BFcDJbYqGzBpge5BpHtlPYdkc%2BLyXk7QwNWTpagWiczmFyNEcyqcaZMgo5YpPRWG%2FE9IGmdsK7JecEgn8ug%2BSFkeQVZN62ahpzUCebMWio1NiV0n8qnG8XdeCXtMr5%2Bcdmongr30C7XTILGEYV%2BM81WIpdl3xvg6KSUhEoulKBLFzYXe%2F10tSHPHZKxiAlWLvEeiSFlTK5uoyNuYlsCHZG0JnbjEFzp8A6lZdkBQ5cKEREhebj87dyUt6ORPj5dXuvbVRVdEuoelhzLSM7G9xFQF2b0MCnCVZ4WXsP4KMgZPTSUZaANUWsryxFrwwGdEETlPNMER%2BTswWCpc5w%2FgMGzfid45FWWFVKNniAs4tWEO0anMGgUT6y%2B8q4VvIJBG5x%2BLsPayUgFKcVbKT4Mqhit%2FQ1pm3ENjG9CFdi75fuZ3AQbz1VvWtHDwo%2FcJvxj66qb0rUFxaRMHEAW649E3duoy1EA1ArVlEYqTDvTYwU5h8lJ%2BM0fvseo%2FJtVveuPI20c7XVC4uIHHUPgvst7E%2FoCVQGdoH4p%2BlGAp92vSUajdIEw7KKyzgY6pgG1Le%2F3cEir6n1NeqEYUQvvoLdxCIIFIy3XH3ntoY2w5XagbFCcUnHbTHaJska38ZFw0q25IwaBLaJvQpSUfgO75ciRJ3mDJGF5JvuxVyIxFPouenoKi9WpqQnGvsT1zXFQdUuPzQUeK%2BjGrRCNMB4gOBHj9LEzm15fdRAhs4oUIf705XRvNBM0l9QpsPiKqFL1%2BcSf5FFheb1cpRuVjLiKteWv1mnz&X-Amz-Signature=7d0515449a9ca53b502f874db6222bb4bc7144e59133b99958402928519edd2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

