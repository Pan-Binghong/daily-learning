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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDAPLWFX%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQetp32h1sQa5MDq%2B2HbeCzqmk%2F8voaJqX9NvonWO7fAIhAKPIVAHyi374OWfV20RVap15um733nbzqG1YO4zsAhCgKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6xAkf9pY%2FAyI5D84q3ANNbxLZXOInGGmrv7r%2FgM7cEODc7sq8xjW3jbZPcETSIt6fOnOUy93eAlXo1nfzuzAEno9fokNpJZSxL6PBKMzBzvwhxCuiQmvnbXIQDtRqFXqfpD7p6BEmh4O9bzEIJsNwFqEXgkHl7TxnfckQznXChK7O30LF%2BVokScqlUcBFApDOJUJo6t33WIxg1MpWoQVQ8G3X9VQwI4dGsUt1b8w3RXIktHsUGGyL9UBuMWie3QSPVBQ602%2BNxLEr2l6qSnrNUlyBcjF8vTtYRD%2BDhdQ4HiiHUOeUkP4NF%2FC3SGKdFOw00VChucppMALQexV6NkObwGBdHrlEJM9f9KVeIEnzbd1dd%2BrBCCfR%2FP1Rw%2FIfJrrmZJrA4JXt2L%2BLqzz9F7uk%2BuD0sUuWw2nbbvGXLpHCrIgEGjd%2FV3AmnAxjYXSsaCwRkXVgS4Y0b7CAhrdE4LW2NfEP2lLi3SjQeUxKNx1Ud0hb2LJ8qd3axdtkgReg35bc1JV0kUGwuMcbZPoPNRXsOzzE5xTBTT0%2B46THA1d2nTO0KseFOU8vBF6v5QXdidiGh9p2bPZ4398TYHKXgZKlSXA%2FjwzqKFq2KeEgEd9pxcBq%2FFOHbb0MFYqu69GSqnd8%2BqDE1oaEEg2XjTDj3qPNBjqkAYuebbTKAdLwszsR05W%2F6Mcv2o9Naq6SIoT4wliUPxjyxN0DHsGPoMd7P6o4iUWSDrlds2Qbp6CH9PWhRIrySdVYhG3AG4AePuntstHuDKA80edKMvVT5SvMtUD2KV166BClva1RfmSzgwcinT9GB2gadEFsFwmwn%2B4diUTwHLfkVzA%2Fn%2BIzo7UorpFs4TW6JFp4jHg6bTy%2FEryetnTY6ZxpKwzg&X-Amz-Signature=0d59bdc00784ff07de6974ab57312d5a3d208bd40d5e269d8d28448696ccdce4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDAPLWFX%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQetp32h1sQa5MDq%2B2HbeCzqmk%2F8voaJqX9NvonWO7fAIhAKPIVAHyi374OWfV20RVap15um733nbzqG1YO4zsAhCgKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6xAkf9pY%2FAyI5D84q3ANNbxLZXOInGGmrv7r%2FgM7cEODc7sq8xjW3jbZPcETSIt6fOnOUy93eAlXo1nfzuzAEno9fokNpJZSxL6PBKMzBzvwhxCuiQmvnbXIQDtRqFXqfpD7p6BEmh4O9bzEIJsNwFqEXgkHl7TxnfckQznXChK7O30LF%2BVokScqlUcBFApDOJUJo6t33WIxg1MpWoQVQ8G3X9VQwI4dGsUt1b8w3RXIktHsUGGyL9UBuMWie3QSPVBQ602%2BNxLEr2l6qSnrNUlyBcjF8vTtYRD%2BDhdQ4HiiHUOeUkP4NF%2FC3SGKdFOw00VChucppMALQexV6NkObwGBdHrlEJM9f9KVeIEnzbd1dd%2BrBCCfR%2FP1Rw%2FIfJrrmZJrA4JXt2L%2BLqzz9F7uk%2BuD0sUuWw2nbbvGXLpHCrIgEGjd%2FV3AmnAxjYXSsaCwRkXVgS4Y0b7CAhrdE4LW2NfEP2lLi3SjQeUxKNx1Ud0hb2LJ8qd3axdtkgReg35bc1JV0kUGwuMcbZPoPNRXsOzzE5xTBTT0%2B46THA1d2nTO0KseFOU8vBF6v5QXdidiGh9p2bPZ4398TYHKXgZKlSXA%2FjwzqKFq2KeEgEd9pxcBq%2FFOHbb0MFYqu69GSqnd8%2BqDE1oaEEg2XjTDj3qPNBjqkAYuebbTKAdLwszsR05W%2F6Mcv2o9Naq6SIoT4wliUPxjyxN0DHsGPoMd7P6o4iUWSDrlds2Qbp6CH9PWhRIrySdVYhG3AG4AePuntstHuDKA80edKMvVT5SvMtUD2KV166BClva1RfmSzgwcinT9GB2gadEFsFwmwn%2B4diUTwHLfkVzA%2Fn%2BIzo7UorpFs4TW6JFp4jHg6bTy%2FEryetnTY6ZxpKwzg&X-Amz-Signature=b98d841455b43f73ad6e3f910ad6cb83e8827c2b58900a09a8c6fd6c8bac2c14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

