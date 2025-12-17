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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV5JYVE%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICd%2B7D82TC2JmdQgcuWXfB63keY7THF%2F7W1ukvXrmLwZAiEAuWfMmITr3A%2FnmuqLYJkdp5Q3HsnBrF3PRG111wDjXZsq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGuvUQfaFa5JZWA3yCrcA2ZXGeTJ4UCHsT44%2F09Nz2Z3lStFXMv%2FF4RtGwmmqNnn0xiNKRajpz3Lk1zWfVe9NlAdhXSEX6gqxiFN%2FQ2SbYRNiapVCnEYFpLDXYWQVc%2BCpq2RqaXsDzStUEPLeGltSY%2FwxO8MRRFXpeARRAzNA%2Fo1cyOtEhv%2FbQ9qOPjidQB8AKevxPjWKAmM4kVqn2xhGJE4agOD727Qlj7sY3uXkPFIb5ro2qRsY5fY3aMPFZu2w8A03YVNOH36A138ALGpExmrES6NVSRjRz8ApTpBJToEuU2oa69Skh%2BLDETfL0oJaKzsqDojTKM5VQ24Zhrkqxmlg%2BLvBpjSUKgFrj70cO80w66JFRa4DAI7r7QRF7cccrKZAkjVp7FInUmL4U3ra7LJ5e%2FgS4ju2Un46bXdqOSFvmeeFuW984hW6WHi2lt25vtJs%2FGNNAvN%2B4x0rQ%2BK5ZJRu5HvZgxeeNSBnyFg8%2FHfW%2F6gk9Z5IYEPbguGaxRZzkT1GR%2BJRk%2Bg48O0Zb7PUQ4jKhYq4gT%2FgmLhiW7fdiTgVzF56YbyU7%2BU23l1HUQ0Z0WsX8wM6dgIbQEJLwu8jddiIs%2FjMM2lDbOTDmYDdHDWCPoCCBlJzF1aY5b2VWm%2BhsuUy6NyOwtHnb3VMOuyiMoGOqUBpkhZwaL%2Fm%2BuZ7sn1m1QAxVArnFKwpz9%2FGTMSjwgk6%2BPuVdqYgnnfEFDTfJwrV1TisGM9mbWYEGtEPytmlGIIb1FSwKdJOaEoi8tQeNeta%2FfBTJc77zRIeKdziJmp0Tqa45NhkPKFWoE75FOIEKloNdH%2FDioWwr4r%2BH6lJ7KUYsT6zEkuH0iWQT4ASaPufJj9vEOgbLhUCNC4jGgtCUPFCIWvzKIL&X-Amz-Signature=3824c75170a09ada0cce7da0e993e5bc9ae550c96a41a41df422510e31e6a8f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV5JYVE%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICd%2B7D82TC2JmdQgcuWXfB63keY7THF%2F7W1ukvXrmLwZAiEAuWfMmITr3A%2FnmuqLYJkdp5Q3HsnBrF3PRG111wDjXZsq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGuvUQfaFa5JZWA3yCrcA2ZXGeTJ4UCHsT44%2F09Nz2Z3lStFXMv%2FF4RtGwmmqNnn0xiNKRajpz3Lk1zWfVe9NlAdhXSEX6gqxiFN%2FQ2SbYRNiapVCnEYFpLDXYWQVc%2BCpq2RqaXsDzStUEPLeGltSY%2FwxO8MRRFXpeARRAzNA%2Fo1cyOtEhv%2FbQ9qOPjidQB8AKevxPjWKAmM4kVqn2xhGJE4agOD727Qlj7sY3uXkPFIb5ro2qRsY5fY3aMPFZu2w8A03YVNOH36A138ALGpExmrES6NVSRjRz8ApTpBJToEuU2oa69Skh%2BLDETfL0oJaKzsqDojTKM5VQ24Zhrkqxmlg%2BLvBpjSUKgFrj70cO80w66JFRa4DAI7r7QRF7cccrKZAkjVp7FInUmL4U3ra7LJ5e%2FgS4ju2Un46bXdqOSFvmeeFuW984hW6WHi2lt25vtJs%2FGNNAvN%2B4x0rQ%2BK5ZJRu5HvZgxeeNSBnyFg8%2FHfW%2F6gk9Z5IYEPbguGaxRZzkT1GR%2BJRk%2Bg48O0Zb7PUQ4jKhYq4gT%2FgmLhiW7fdiTgVzF56YbyU7%2BU23l1HUQ0Z0WsX8wM6dgIbQEJLwu8jddiIs%2FjMM2lDbOTDmYDdHDWCPoCCBlJzF1aY5b2VWm%2BhsuUy6NyOwtHnb3VMOuyiMoGOqUBpkhZwaL%2Fm%2BuZ7sn1m1QAxVArnFKwpz9%2FGTMSjwgk6%2BPuVdqYgnnfEFDTfJwrV1TisGM9mbWYEGtEPytmlGIIb1FSwKdJOaEoi8tQeNeta%2FfBTJc77zRIeKdziJmp0Tqa45NhkPKFWoE75FOIEKloNdH%2FDioWwr4r%2BH6lJ7KUYsT6zEkuH0iWQT4ASaPufJj9vEOgbLhUCNC4jGgtCUPFCIWvzKIL&X-Amz-Signature=792771d293c788098e6f2186b7b686bc105ad610b0c8d1176b373bdf3e0d19fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

