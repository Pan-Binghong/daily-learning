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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFUMGQXA%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3PPcq%2F1z0cf%2Fq4yeKlP3HGz%2BM7N5a%2F%2BLNEogXh7mPKAiEAnhPJncivCNQ497dcJPqX0bTkNz1enTRAmb9Grlsnpy0qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGHmqQRNSyE1HEihSrcA2PrH7cQcb4k5GZmfWbZGSnfEk6ikkI7ed9N0KF2BiQ6Y7rACxy3wrcFWSnfaBLxIwhiwKzyotmFZsPFo18cDO9%2FziKN5gL%2Bud2Is2DiUVcQgoisQYOYshjeioQsfiqD9gXD2JAqDLlrdsIn6k91wGir%2F22k0dETqAvLBLRBkUJfoFa6DqpKnF9G7cA2w%2BO8478weBIcR0tB%2BTUpM0OprxO6TUdzR0qBCAyMf5SrnMXXMKWg7HVsGwVrx8EDH%2FAMgb9flYNijgyYWBV%2BdxPFOczvpgANDssgm9ZGefWaDaNDs4ZRnWWWqXmrgtWO%2BvjHyCJ2SNPkIsa1oUDerqqC3u9Hb5IeovF5DHth7Z53908onu3i5ckCbj9naJGZGvBEF7dUEoL4Wsjwt3ERySxvguorfC7y0PcGQRGKm0x80Eeet02X%2BwuVL9A%2F2oNvPM0ArflZKw0p59wls7c8KO1arXxlspdrdqWX10%2FKFyf3Ot9NdumTuHONyCMRToEguVd1vQFuG3JFWZbae57wCpiYo9fWmTr%2BROGZTgeASDErPlgtmuE3osa%2BXXdLn2HWUbx20TYmAE%2FJ6W2kX3iNwk7ot5bz81VdIVd%2ByPQP7n25OOwoIBHtn%2Fj3prJDQC1JML7hksoGOqUBo7CmstxSOyO67r%2FDaFl%2FFlpR8gnK%2B4V9m7UoQcoXXDWdvoaOIwW%2FU646o%2BH321JsZtFLGswyTlLlWOi3d1wZxKKtAX6RmgBxJraEVBY0HJTbkMVOUOst%2FT%2BbK78ipW1cT2gFumqI4SxatQx%2F7EJJsmOFpjCyixY%2F4kpvzsWv1ZWjYt3S4UQXTbsElHjj77Ot%2BaqNjqcVVxFmNcKpSrlzB4%2B3zYfG&X-Amz-Signature=8ee6952fe85e741eea96c859da6134f0f6d31fd0f09f927b3fa8808bcd1dd429&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFUMGQXA%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3PPcq%2F1z0cf%2Fq4yeKlP3HGz%2BM7N5a%2F%2BLNEogXh7mPKAiEAnhPJncivCNQ497dcJPqX0bTkNz1enTRAmb9Grlsnpy0qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGHmqQRNSyE1HEihSrcA2PrH7cQcb4k5GZmfWbZGSnfEk6ikkI7ed9N0KF2BiQ6Y7rACxy3wrcFWSnfaBLxIwhiwKzyotmFZsPFo18cDO9%2FziKN5gL%2Bud2Is2DiUVcQgoisQYOYshjeioQsfiqD9gXD2JAqDLlrdsIn6k91wGir%2F22k0dETqAvLBLRBkUJfoFa6DqpKnF9G7cA2w%2BO8478weBIcR0tB%2BTUpM0OprxO6TUdzR0qBCAyMf5SrnMXXMKWg7HVsGwVrx8EDH%2FAMgb9flYNijgyYWBV%2BdxPFOczvpgANDssgm9ZGefWaDaNDs4ZRnWWWqXmrgtWO%2BvjHyCJ2SNPkIsa1oUDerqqC3u9Hb5IeovF5DHth7Z53908onu3i5ckCbj9naJGZGvBEF7dUEoL4Wsjwt3ERySxvguorfC7y0PcGQRGKm0x80Eeet02X%2BwuVL9A%2F2oNvPM0ArflZKw0p59wls7c8KO1arXxlspdrdqWX10%2FKFyf3Ot9NdumTuHONyCMRToEguVd1vQFuG3JFWZbae57wCpiYo9fWmTr%2BROGZTgeASDErPlgtmuE3osa%2BXXdLn2HWUbx20TYmAE%2FJ6W2kX3iNwk7ot5bz81VdIVd%2ByPQP7n25OOwoIBHtn%2Fj3prJDQC1JML7hksoGOqUBo7CmstxSOyO67r%2FDaFl%2FFlpR8gnK%2B4V9m7UoQcoXXDWdvoaOIwW%2FU646o%2BH321JsZtFLGswyTlLlWOi3d1wZxKKtAX6RmgBxJraEVBY0HJTbkMVOUOst%2FT%2BbK78ipW1cT2gFumqI4SxatQx%2F7EJJsmOFpjCyixY%2F4kpvzsWv1ZWjYt3S4UQXTbsElHjj77Ot%2BaqNjqcVVxFmNcKpSrlzB4%2B3zYfG&X-Amz-Signature=2bd129401af4c270ff91d32c751ae40fbabf2c7e5168a0eefcfed31c24680c08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

