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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4MRXV%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClp1pg9cd4qYhw%2Bd4Ns%2FP8frcWIGrT1pZSBW4XEGU6yAiBeaTJ2nH9R3Gz%2Bl1BDda2pDzZWlsFXNuT9gpeGNKElMir%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM2%2B7u2p28XzfA8pYXKtwDliAyo64rKvitGSdaGEAwaOnlvT%2FwgrNZaNOcl4Qi%2BkLaVNqxB7lpga31lBpq9veYJKMR2uU3S2tcG%2BFcDJbYqGzBpge5BpHtlPYdkc%2BLyXk7QwNWTpagWiczmFyNEcyqcaZMgo5YpPRWG%2FE9IGmdsK7JecEgn8ug%2BSFkeQVZN62ahpzUCebMWio1NiV0n8qnG8XdeCXtMr5%2Bcdmongr30C7XTILGEYV%2BM81WIpdl3xvg6KSUhEoulKBLFzYXe%2F10tSHPHZKxiAlWLvEeiSFlTK5uoyNuYlsCHZG0JnbjEFzp8A6lZdkBQ5cKEREhebj87dyUt6ORPj5dXuvbVRVdEuoelhzLSM7G9xFQF2b0MCnCVZ4WXsP4KMgZPTSUZaANUWsryxFrwwGdEETlPNMER%2BTswWCpc5w%2FgMGzfid45FWWFVKNniAs4tWEO0anMGgUT6y%2B8q4VvIJBG5x%2BLsPayUgFKcVbKT4Mqhit%2FQ1pm3ENjG9CFdi75fuZ3AQbz1VvWtHDwo%2FcJvxj66qb0rUFxaRMHEAW649E3duoy1EA1ArVlEYqTDvTYwU5h8lJ%2BM0fvseo%2FJtVveuPI20c7XVC4uIHHUPgvst7E%2FoCVQGdoH4p%2BlGAp92vSUajdIEw7KKyzgY6pgG1Le%2F3cEir6n1NeqEYUQvvoLdxCIIFIy3XH3ntoY2w5XagbFCcUnHbTHaJska38ZFw0q25IwaBLaJvQpSUfgO75ciRJ3mDJGF5JvuxVyIxFPouenoKi9WpqQnGvsT1zXFQdUuPzQUeK%2BjGrRCNMB4gOBHj9LEzm15fdRAhs4oUIf705XRvNBM0l9QpsPiKqFL1%2BcSf5FFheb1cpRuVjLiKteWv1mnz&X-Amz-Signature=c8e60a6b1e6d883787d7403e8009221b880d38d3a60344701abefc382968e68e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4MRXV%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClp1pg9cd4qYhw%2Bd4Ns%2FP8frcWIGrT1pZSBW4XEGU6yAiBeaTJ2nH9R3Gz%2Bl1BDda2pDzZWlsFXNuT9gpeGNKElMir%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM2%2B7u2p28XzfA8pYXKtwDliAyo64rKvitGSdaGEAwaOnlvT%2FwgrNZaNOcl4Qi%2BkLaVNqxB7lpga31lBpq9veYJKMR2uU3S2tcG%2BFcDJbYqGzBpge5BpHtlPYdkc%2BLyXk7QwNWTpagWiczmFyNEcyqcaZMgo5YpPRWG%2FE9IGmdsK7JecEgn8ug%2BSFkeQVZN62ahpzUCebMWio1NiV0n8qnG8XdeCXtMr5%2Bcdmongr30C7XTILGEYV%2BM81WIpdl3xvg6KSUhEoulKBLFzYXe%2F10tSHPHZKxiAlWLvEeiSFlTK5uoyNuYlsCHZG0JnbjEFzp8A6lZdkBQ5cKEREhebj87dyUt6ORPj5dXuvbVRVdEuoelhzLSM7G9xFQF2b0MCnCVZ4WXsP4KMgZPTSUZaANUWsryxFrwwGdEETlPNMER%2BTswWCpc5w%2FgMGzfid45FWWFVKNniAs4tWEO0anMGgUT6y%2B8q4VvIJBG5x%2BLsPayUgFKcVbKT4Mqhit%2FQ1pm3ENjG9CFdi75fuZ3AQbz1VvWtHDwo%2FcJvxj66qb0rUFxaRMHEAW649E3duoy1EA1ArVlEYqTDvTYwU5h8lJ%2BM0fvseo%2FJtVveuPI20c7XVC4uIHHUPgvst7E%2FoCVQGdoH4p%2BlGAp92vSUajdIEw7KKyzgY6pgG1Le%2F3cEir6n1NeqEYUQvvoLdxCIIFIy3XH3ntoY2w5XagbFCcUnHbTHaJska38ZFw0q25IwaBLaJvQpSUfgO75ciRJ3mDJGF5JvuxVyIxFPouenoKi9WpqQnGvsT1zXFQdUuPzQUeK%2BjGrRCNMB4gOBHj9LEzm15fdRAhs4oUIf705XRvNBM0l9QpsPiKqFL1%2BcSf5FFheb1cpRuVjLiKteWv1mnz&X-Amz-Signature=42818eb6509642042b247bdde715ba049c8f18039958b8ae4de46c5be0116969&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

