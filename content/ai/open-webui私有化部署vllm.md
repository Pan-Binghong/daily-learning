---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2VKNPWY%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHkqsAyTk0UGW11vurhNl4mRBzAjYTLHCvPRqlRyzZwGAiBNyQQ7aeRXHaj%2BkBO8EtZeY6ULpOZ0DEzRJUfo5L3ruSqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi2M9d0tMEjgdNVAyKtwDBDsBy5RxFpk2dqFN43lazp49Ayl5SatKaKAeptolv6Fw43znq%2FFgevygQbo3FKgnu%2FQDs3Fl0%2Br7q%2BUZEt%2FEaXZhBemP9VNEmYmtigTdNniNCRJGRRe6Bcjyy%2Fis72CG9idFOzoV5xZLrnaM6rABwzR9T40HMQLEjWvVarNLyVf6ZXwhFJn3w%2Byf6QEgC4W5LDQee4ZUCYL0A9KAbUNVW%2FRrULdg9UKIjv7GEANUofKLjqBbSVNXGWHaKmTyJsJpUPuUypwgS5%2BocNNjKsaEhp2IGVrGfLVJ%2BXdoBNOadVwkArBJZZty%2Fumif1SS5qPGzdSf4W4bqqzrvSfLX3p%2BYcUwcLjBN8AQbY%2F1lWxIu8lyjWHmT684U4DuGcQRwUijQc7%2B9GjpY%2FOItro7XKj0KEiE3ETydUATQwTnys5tz8IPqMuo385QkHfRkU%2FE%2FBjoZzdHUzX%2Ffo2SWkO6szOKJ5aaxKOOiiEtD2hsnTNCRVWoiC8N9om8vBxFz2bO2vy%2BzZPVsU5oDybaLjDUk6xGvygZagPmwaViuK0TwPPty84d54QsG7Lb0v9qykZyB%2BYS2%2F%2FCYuLZSS71JahENB2C7n3b2cx%2BmJSD%2F%2B5RYoodDVXrctli0VgCRY6N4R8wqpjXygY6pgF1aHqvBztH2eQWo4WMhWYwST62jnypxt4DvYZsP3ubHPeBOJ0wL%2F9nBtDo%2ByDxVF7FGdQA%2BZFZOeDQlvgmmwy2pnY2mMazvDj0aevDGh8JA%2B%2F0dehp%2Bhv9k6HURPmOfwlKNxaHIVpda7tDCxWjYPNC5rbL6LL47fCkeUb2joZZont1C%2FwxU6Sz2vw%2FXjvVbJVIPlKRtCKiA0HaL95SvGSObqX7TSAg&X-Amz-Signature=82cccb45411654d9850d7129ad2b8554344613b6f9be67b879bc759b32160450&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



