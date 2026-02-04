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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJBXLOEC%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIFx6p4%2BuyFFnivZmblDpPSS59l0sU8lOrLAuftgeB6ruAiAtxJKkO0gPiX8h5cN3Sb0tW%2BZG9J6OOYdszwGueF2utir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMrtwMGEMdlQDp3m57KtwDAJGZk%2BWFgxnZBwrKZ5UlQ62n0dIQ3sicl8%2FUqpDljzLhA05VLj0B4Vz6tozhNAoScn6pDPZXwdx1QQPuW8iWRLd15Jr2C%2FtfQ8qeYUfDwZKt3qoKnSh3q2GcwGqZkeSyrq5rnEfhK3k0%2F56%2FhzvtA91OE17vg9SQVFVeElQpR1dorTQWoW8CyLJYrbotgrSemA%2Bd6T9LAoTIfZaRYxPYUS0dksy8Fox1zaNCyz7dpbdc37jviWSLlmue3t8gO1idldCAKQ57sPZKRZkKDMlqozZqXya2rRLXEFst61E6mW6smRvF0uIApwkfmavxTfp7ds3N%2FCUNedly6W8txvjr9POJjygOpSHXCRDUaFYDjQPACOzYkJzb2SgFMRWFTX6Mz7CqrfkPNj9%2Bl9ZMW8LVfAxP5SVZZUH0SE2BhgE43CLJ2iLpseXS4K%2BvWQ9N135c0up59Bl%2FZ5btmhC2iQM1Bb1tGNbk0WsBYHCVOvwUageUXvrAkD6hahaAMcb1m0GWG%2BoLH6JIIep2nL8xigA3NxR7Lj6lweOyFM0G09ij8yPZ%2F6YXsuGOhq0DTB%2B1593H1C%2BHE3QEDc9Lf2pM6KX4N2i6VaHk24UI2werkyL%2BH%2Ftf4jHlx2hnky9hft8w9ueKzAY6pgFLTkJucbhUiUp36TvcODuhgzznQUPNR%2Bs%2FZMWexVAWjFMaCeg3TkLCVo2M%2Br%2BnWW59Wj1gt3nLnNQDBgCKpdpz7vaUped%2FsFL%2FyE1M8155kbGWtewWVrURGzO%2BsQ5ROkEc9iIA%2F6S3aV2lF9CGqysQFz01jVUbK72BzR3u0B%2FaudczQHHgsyV95v09OWPkar2CY3NZng7389HFYwX8JHBd5kugs5Pf&X-Amz-Signature=79fbba70390cab54ac61883fc049b9555f6c7849a52f626668877a69258500d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJBXLOEC%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIFx6p4%2BuyFFnivZmblDpPSS59l0sU8lOrLAuftgeB6ruAiAtxJKkO0gPiX8h5cN3Sb0tW%2BZG9J6OOYdszwGueF2utir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMrtwMGEMdlQDp3m57KtwDAJGZk%2BWFgxnZBwrKZ5UlQ62n0dIQ3sicl8%2FUqpDljzLhA05VLj0B4Vz6tozhNAoScn6pDPZXwdx1QQPuW8iWRLd15Jr2C%2FtfQ8qeYUfDwZKt3qoKnSh3q2GcwGqZkeSyrq5rnEfhK3k0%2F56%2FhzvtA91OE17vg9SQVFVeElQpR1dorTQWoW8CyLJYrbotgrSemA%2Bd6T9LAoTIfZaRYxPYUS0dksy8Fox1zaNCyz7dpbdc37jviWSLlmue3t8gO1idldCAKQ57sPZKRZkKDMlqozZqXya2rRLXEFst61E6mW6smRvF0uIApwkfmavxTfp7ds3N%2FCUNedly6W8txvjr9POJjygOpSHXCRDUaFYDjQPACOzYkJzb2SgFMRWFTX6Mz7CqrfkPNj9%2Bl9ZMW8LVfAxP5SVZZUH0SE2BhgE43CLJ2iLpseXS4K%2BvWQ9N135c0up59Bl%2FZ5btmhC2iQM1Bb1tGNbk0WsBYHCVOvwUageUXvrAkD6hahaAMcb1m0GWG%2BoLH6JIIep2nL8xigA3NxR7Lj6lweOyFM0G09ij8yPZ%2F6YXsuGOhq0DTB%2B1593H1C%2BHE3QEDc9Lf2pM6KX4N2i6VaHk24UI2werkyL%2BH%2Ftf4jHlx2hnky9hft8w9ueKzAY6pgFLTkJucbhUiUp36TvcODuhgzznQUPNR%2Bs%2FZMWexVAWjFMaCeg3TkLCVo2M%2Br%2BnWW59Wj1gt3nLnNQDBgCKpdpz7vaUped%2FsFL%2FyE1M8155kbGWtewWVrURGzO%2BsQ5ROkEc9iIA%2F6S3aV2lF9CGqysQFz01jVUbK72BzR3u0B%2FaudczQHHgsyV95v09OWPkar2CY3NZng7389HFYwX8JHBd5kugs5Pf&X-Amz-Signature=56af02a96f9c88c3c5b7801ded86cf60b16dee251bea0b789964ab8c13271fd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

