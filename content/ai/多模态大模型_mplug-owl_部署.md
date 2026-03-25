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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDSWOSX6%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCq611LYLEcoNQ9tx9TqO3cX1hHCgOfYLKIf%2Fm20mY%2FjgIhAK1Dc4pX6cBK6rXQQ2yOboVMjUk7rNufEYMBtPzSUiUhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyoOod%2F6L7QUqqIDKcq3AN89C7hqVizkHI9aDmAN5mz2rDraVDiyDck8tnoWrL%2B2UDDdbTwWp63EXko7ykiqazNAGoZxXkt0oAuMqPQIE55gXKOgpxvRBew5yE7cfl5uJIUyJZVMFES8mUh9GJ3wxNZqg%2BPWElh42CLdxSU9Yguggqu2cz3twJGckl0xk2V2%2BIrzaZahBlDSHmg1VKItDaH6pRaGOkY7RDO8343WROUCVULqLarbrZO1%2FF1dMGNXrbP2uQ5ZsN4kYznUAxh7z8ZrIaNMcUeZbdgBn%2B3XwJ3zU7S9rnldSsKHjggrPcx%2Bp2wHen4L6vuETyPRBIyyysPsey3ImPEjnovv46vL%2BiC24lJNDeBrge2gvOtCQdc%2FZk3hPFA4xFjr%2BeKRhkibc3Ce4Kx0shqITiWdhBsE4deSf7H39ibMn08DJEPOr44E5%2FoGdAp%2Bdy%2BEED%2F38SyuT3IKFT3jBVUMhL3jQQ54wqNPxXBghB%2FUz5zUIyVzj9fi8XmuUTuPifZeWOscbKcJ%2B06bRi24ovRS4%2B%2BtlQlKlKfX9fDdgeCHRXRjozf8sbpe3KS%2BbUajLRLzj5%2FKLfL5F%2B23SIZgRJeDJliz9jYRPCdydGjUMpP9gmRqi7HhkUdvFs0eOr%2FmI0BmLNWaTC41o7OBjqkAY29iEHwuW6Z6qI8xvrRwDTUts4vrI1TPEoiSKPlTtLy57uanheNHRcPSn3BSULnzX5qcR9zM9zmX0Aj3OUwjkm1dLW30eYkR%2F4RUqRrEg5oO0mx6rvHU409UnVWcX0S6LEuwEONB6eah3ehEl55fr2yh34pUakqR9JlZd6xw9pg8efD3YL41u9gMu5FXXtL6m5p0cqmMi%2B9MxbrWHzSfqCFfJkP&X-Amz-Signature=0eb956903fcc59b61e6b887970d311060015a23e2919d4b18c27cf6e00cdc989&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDSWOSX6%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCq611LYLEcoNQ9tx9TqO3cX1hHCgOfYLKIf%2Fm20mY%2FjgIhAK1Dc4pX6cBK6rXQQ2yOboVMjUk7rNufEYMBtPzSUiUhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyoOod%2F6L7QUqqIDKcq3AN89C7hqVizkHI9aDmAN5mz2rDraVDiyDck8tnoWrL%2B2UDDdbTwWp63EXko7ykiqazNAGoZxXkt0oAuMqPQIE55gXKOgpxvRBew5yE7cfl5uJIUyJZVMFES8mUh9GJ3wxNZqg%2BPWElh42CLdxSU9Yguggqu2cz3twJGckl0xk2V2%2BIrzaZahBlDSHmg1VKItDaH6pRaGOkY7RDO8343WROUCVULqLarbrZO1%2FF1dMGNXrbP2uQ5ZsN4kYznUAxh7z8ZrIaNMcUeZbdgBn%2B3XwJ3zU7S9rnldSsKHjggrPcx%2Bp2wHen4L6vuETyPRBIyyysPsey3ImPEjnovv46vL%2BiC24lJNDeBrge2gvOtCQdc%2FZk3hPFA4xFjr%2BeKRhkibc3Ce4Kx0shqITiWdhBsE4deSf7H39ibMn08DJEPOr44E5%2FoGdAp%2Bdy%2BEED%2F38SyuT3IKFT3jBVUMhL3jQQ54wqNPxXBghB%2FUz5zUIyVzj9fi8XmuUTuPifZeWOscbKcJ%2B06bRi24ovRS4%2B%2BtlQlKlKfX9fDdgeCHRXRjozf8sbpe3KS%2BbUajLRLzj5%2FKLfL5F%2B23SIZgRJeDJliz9jYRPCdydGjUMpP9gmRqi7HhkUdvFs0eOr%2FmI0BmLNWaTC41o7OBjqkAY29iEHwuW6Z6qI8xvrRwDTUts4vrI1TPEoiSKPlTtLy57uanheNHRcPSn3BSULnzX5qcR9zM9zmX0Aj3OUwjkm1dLW30eYkR%2F4RUqRrEg5oO0mx6rvHU409UnVWcX0S6LEuwEONB6eah3ehEl55fr2yh34pUakqR9JlZd6xw9pg8efD3YL41u9gMu5FXXtL6m5p0cqmMi%2B9MxbrWHzSfqCFfJkP&X-Amz-Signature=128e3d86000df945fe4ea3419135af8d271e7f6d6cf8c6873aeb847354a35260&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

