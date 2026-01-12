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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVSILYCB%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIDWqgyLJxqOFFZxOAP0Yo8g%2FUnDlMqBljqs3B7sR7PgJAiB1TCrKa4oPPSFjpdtBwhcqf%2BSzyLt9zzRlEIc5L1lUzCqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0owSpmDbq%2Bdx2jpjKtwDr%2BQrTyWNiQDi4k6YQZdPpx5pAqGk7vY8BlyXTW%2BirVubBROyPxR50Plxha1j8z6BDxoVhbhzQ%2F1B0pxU0aiRuzCCkvB7InP%2FpVBQN4oqQTeTdhXgITwPG3w3mxR8sF3nLE2a1dF5KNgpMkMnrKglfctk0iMouveReY3qdc4lY6rnRA5s%2BFTDBi%2BqMgR5HrIjoO7Qp5%2Bz1gXoD5y620PyxNlg7Mbx7sRBm3oTNITlv4b65FmjMeCBVZNG56cs1xKg3Y2b6JYQ4%2FlMbLhI3U3liuorhHJJeTEIvk6vYFuqbDWLqsXNC%2F16s8CPTiyuDysOgB8u%2F%2Fq02dS2SjcOUXC667aOk0T7pRTT03fMqZZ8YG2BocOWmljBoA5%2Fwi7rOZ%2F1sVQ7xM%2F23YqWkUuhopmtYFp%2F%2Fvamj%2BRInWVZMzjZTEwNt%2ByoE9MBOZqkewBMfnAM%2F95SZRzorO0PdSlYb2Iq%2BDb4DlP5lxpZWINM4%2Fhi2kYsA0ArWkfbMPmFXCJZVMzf9CPRgLTio8DmrdasnZzfkcZhmTqb0kioIflbOiO%2FaztFotMHNP3n7mPv5HKD4WmCk0oXNB5kWqPYPBOb780LzjPSa6IuNfGf2wHl4XQxQL5H1MTyt1DvY%2BkPnocwsPiQywY6pgHnVwkjDvcghUoqdZoqX2A5XiFI0eK1wJ3VZpCzlCbtQSloT8Cske%2Fa%2FHdOQ141%2FbHy8mb6y2%2Bx2mvR7dCXh8XPB7qlEfvt7XuRKE504JCsmm2a8%2BIlqSbl704k99a7TL761LDeNzvtqhnHQzYPVilsBYUcyprQNVBp0asR1mI5Hm%2Bl%2BhmRuB6hCtQzYg%2Bu7huFBesqSrSitZLsGMvwLazvbtnW3xx1&X-Amz-Signature=4b64a231536729ae428104b2f99989b5285999717ffcdf819fa39136021c5480&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVSILYCB%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIDWqgyLJxqOFFZxOAP0Yo8g%2FUnDlMqBljqs3B7sR7PgJAiB1TCrKa4oPPSFjpdtBwhcqf%2BSzyLt9zzRlEIc5L1lUzCqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0owSpmDbq%2Bdx2jpjKtwDr%2BQrTyWNiQDi4k6YQZdPpx5pAqGk7vY8BlyXTW%2BirVubBROyPxR50Plxha1j8z6BDxoVhbhzQ%2F1B0pxU0aiRuzCCkvB7InP%2FpVBQN4oqQTeTdhXgITwPG3w3mxR8sF3nLE2a1dF5KNgpMkMnrKglfctk0iMouveReY3qdc4lY6rnRA5s%2BFTDBi%2BqMgR5HrIjoO7Qp5%2Bz1gXoD5y620PyxNlg7Mbx7sRBm3oTNITlv4b65FmjMeCBVZNG56cs1xKg3Y2b6JYQ4%2FlMbLhI3U3liuorhHJJeTEIvk6vYFuqbDWLqsXNC%2F16s8CPTiyuDysOgB8u%2F%2Fq02dS2SjcOUXC667aOk0T7pRTT03fMqZZ8YG2BocOWmljBoA5%2Fwi7rOZ%2F1sVQ7xM%2F23YqWkUuhopmtYFp%2F%2Fvamj%2BRInWVZMzjZTEwNt%2ByoE9MBOZqkewBMfnAM%2F95SZRzorO0PdSlYb2Iq%2BDb4DlP5lxpZWINM4%2Fhi2kYsA0ArWkfbMPmFXCJZVMzf9CPRgLTio8DmrdasnZzfkcZhmTqb0kioIflbOiO%2FaztFotMHNP3n7mPv5HKD4WmCk0oXNB5kWqPYPBOb780LzjPSa6IuNfGf2wHl4XQxQL5H1MTyt1DvY%2BkPnocwsPiQywY6pgHnVwkjDvcghUoqdZoqX2A5XiFI0eK1wJ3VZpCzlCbtQSloT8Cske%2Fa%2FHdOQ141%2FbHy8mb6y2%2Bx2mvR7dCXh8XPB7qlEfvt7XuRKE504JCsmm2a8%2BIlqSbl704k99a7TL761LDeNzvtqhnHQzYPVilsBYUcyprQNVBp0asR1mI5Hm%2Bl%2BhmRuB6hCtQzYg%2Bu7huFBesqSrSitZLsGMvwLazvbtnW3xx1&X-Amz-Signature=3b4a041533b962ea4eedbdef01a1f960623fd5a3b3c92807e00e74f4f91de2e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

