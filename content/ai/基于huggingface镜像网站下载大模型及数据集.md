---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOEH5MDO%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDH9POb1u6%2FLhgm%2BA%2BoSoXDzu3WgF23O1JkVFRzBRe0mAiEAiXJKTSVO8tRUrZ1wIxIPZrxp4OvykNknzbLRtUjAClMqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJR1%2F8oLe%2FuvnL4x0ircAyBi4TIHE9MKaYZ4X5uiABnq9Oj38K3H%2BpJpSwOKIvr3Ghb%2BH%2BxAPuw7u1utKMX2FScGDS%2B1Nc5%2BSDWaxgrC8wnGjXZrbrDlwcVpAsQvf7rOazz4A21xSvgiI%2BUHPCuxp11EbtWbtRzK%2BceT0ix%2BC4q1ZGx0Yqu0TMZFo1OKa2YRxMJCyUg22WAppJfhsgTz8PaEDegyXMcNsXWm2iHpIiJhCcp1Yq62rHYVgDc8SEDEUwdORAcXYAf41b7HGXYtgJ01lx6UrCss8uFC%2FREoqkVfadX4nnqOzVeV9JPQ5kxk7EkvJZi2eIx4J50modnHU0gix4l2Ei2DNQs61C94tVovr6MoZFtZYXnel8%2Bv%2F8pF6YZfyrqVtJ2ndDpw5IfpsU%2BzFEBGdhSxNYp5LKngA2F6imFuvlfbA3GSs38XvWl%2B6WPI9DNxbErGVPupKq8ykOpRiKRJj1QgmoYB6fGBPDKTs%2BonVS6r7wnBX9Bo9yIvfX%2B2zdjl1mo3POJ1woSosJPeY8991BdCsqRnMPBLQ7S6GsLQcARWB0IOmU%2FTgiObiMwTIALNOeXmHSwGRLIH7zZUhmfwg9aJvHm9c95B1BliPKcpS8Qd898IqcXt5%2FxaPxob0X5A%2BXZbpSdkMLTEqswGOqUBgRIqXlI4TqRyP2hihIMcuCj6x3tEa1AsxFPtm5z8I%2BfjVpm7yk8PHwOylzcFDXgjNd0v9ft05JFFwZNFtMOfPVbq0m89lM0ylwa%2BjILlkyoJTh2too%2Fpb46XaOb79yeeNOdsQlcgbWoEnQ0%2BoqAc0sb%2BuEtRkE09fDS%2F7nXHkvq9n4ZJi9LRkkTSJ%2FEJr7dpu3Dh42wFQgmYVlsnb2%2Bgu2DQkW1%2F&X-Amz-Signature=d21577a22fc3fcd6a4c98f06460881d8cf5d01512aa0d6b18db0229858baf4d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOEH5MDO%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDH9POb1u6%2FLhgm%2BA%2BoSoXDzu3WgF23O1JkVFRzBRe0mAiEAiXJKTSVO8tRUrZ1wIxIPZrxp4OvykNknzbLRtUjAClMqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJR1%2F8oLe%2FuvnL4x0ircAyBi4TIHE9MKaYZ4X5uiABnq9Oj38K3H%2BpJpSwOKIvr3Ghb%2BH%2BxAPuw7u1utKMX2FScGDS%2B1Nc5%2BSDWaxgrC8wnGjXZrbrDlwcVpAsQvf7rOazz4A21xSvgiI%2BUHPCuxp11EbtWbtRzK%2BceT0ix%2BC4q1ZGx0Yqu0TMZFo1OKa2YRxMJCyUg22WAppJfhsgTz8PaEDegyXMcNsXWm2iHpIiJhCcp1Yq62rHYVgDc8SEDEUwdORAcXYAf41b7HGXYtgJ01lx6UrCss8uFC%2FREoqkVfadX4nnqOzVeV9JPQ5kxk7EkvJZi2eIx4J50modnHU0gix4l2Ei2DNQs61C94tVovr6MoZFtZYXnel8%2Bv%2F8pF6YZfyrqVtJ2ndDpw5IfpsU%2BzFEBGdhSxNYp5LKngA2F6imFuvlfbA3GSs38XvWl%2B6WPI9DNxbErGVPupKq8ykOpRiKRJj1QgmoYB6fGBPDKTs%2BonVS6r7wnBX9Bo9yIvfX%2B2zdjl1mo3POJ1woSosJPeY8991BdCsqRnMPBLQ7S6GsLQcARWB0IOmU%2FTgiObiMwTIALNOeXmHSwGRLIH7zZUhmfwg9aJvHm9c95B1BliPKcpS8Qd898IqcXt5%2FxaPxob0X5A%2BXZbpSdkMLTEqswGOqUBgRIqXlI4TqRyP2hihIMcuCj6x3tEa1AsxFPtm5z8I%2BfjVpm7yk8PHwOylzcFDXgjNd0v9ft05JFFwZNFtMOfPVbq0m89lM0ylwa%2BjILlkyoJTh2too%2Fpb46XaOb79yeeNOdsQlcgbWoEnQ0%2BoqAc0sb%2BuEtRkE09fDS%2F7nXHkvq9n4ZJi9LRkkTSJ%2FEJr7dpu3Dh42wFQgmYVlsnb2%2Bgu2DQkW1%2F&X-Amz-Signature=cad7ae10cc26536796593b64a64c8538c90189b4f5df24d4d2686351e18b91a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



