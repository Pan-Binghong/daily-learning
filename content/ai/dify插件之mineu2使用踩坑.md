---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QNDDVUV%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIGXYWrJD51nnuYqrtENH5B8WZxGysn%2Fanjp4Ok0jwCoHAiBQSc5LDofoayXPxdu6dI9o6qdee%2Bs8WHR2Oh5M3zD%2B8ir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMSzNl1CDeqXPmuejhKtwDydYKye4c%2BUqhCYHDMG%2BMeHlWQkBlXM3AZNiV8fthI9Fm8uu75MVcv1N9eqQob9OsejDlLEtwzuOwK6PKW7Lve6EGJmos5Wqf7ANPJVeL8CbLeEe8Z9NIC1f6yln6gCyykTCz1SPJq0V7z1QcOEkYhzfu%2Ba%2BvBMWtzvnL0XxIrLvfLslTL6pr5Kfp9lDpSuzBEx2YCgs1rtwksW2ihgO475cdZClMeG6bcY9%2FLTQ%2B27W300xiwU64%2Br%2FFcc0GJYV%2FzEgYDvuRXxB5EoawT6Gk0zKFx11RWGrhsBj1eFzAxWqdaNebFvfwZsxWXaUtrDFlqL7MnztWR5DktkQiR7JhLk%2B16pvVvdmCrdqHm%2FCVU3kjBPknn%2FUXePuhDq%2FOqvXw8WA3AWOF2NKScQKVilv0xRRyr8uQRxqxXZSsyVVc%2BnSB%2FWMqXriNVzJCVEpPWCpaIjZ28ABqk1MiSHN5dTj9SMV8MuCpToC9LuC2VqIIjeq0cYLygZ%2BARB2UYlRW0QyTkkcLUMBbLUfKH%2FMt6epq84h1GJOGTPyM5e8f9HwdbhwTzFiKLGdhpBC0KarVojTaiiwbmrlvKmdcIx20Sx1B3qDw454PnFO%2F9Y6e%2FAEc91RcKAFYmwskBXKOvhwwnZOyygY6pgGgYrc9tmG0g%2FNLYDMlrSk1rIBW9d0KCGo%2BNMLjHe7E52MBM6ia8t5HDNGTLImZmyEcFH4lSIb1fuBJsBfwZNbyGC2xKJ218aF%2BiUpyvSCwb7LLOrBG6q%2FRZOhR%2Fwod13laBWk2YU1OR84q1i2DVMhnhCvdf%2BYrdT0ujeFPJpOXCXt%2FxN9u8woVySl6CylQJ%2FDPUOCiCVIcllhqLRFvCgw1cOLXCKXA&X-Amz-Signature=5922c5c7a61e09cf4627f9b520a9c791965d7a4fd3c4821bc6d251e01f1a6e4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QNDDVUV%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIGXYWrJD51nnuYqrtENH5B8WZxGysn%2Fanjp4Ok0jwCoHAiBQSc5LDofoayXPxdu6dI9o6qdee%2Bs8WHR2Oh5M3zD%2B8ir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMSzNl1CDeqXPmuejhKtwDydYKye4c%2BUqhCYHDMG%2BMeHlWQkBlXM3AZNiV8fthI9Fm8uu75MVcv1N9eqQob9OsejDlLEtwzuOwK6PKW7Lve6EGJmos5Wqf7ANPJVeL8CbLeEe8Z9NIC1f6yln6gCyykTCz1SPJq0V7z1QcOEkYhzfu%2Ba%2BvBMWtzvnL0XxIrLvfLslTL6pr5Kfp9lDpSuzBEx2YCgs1rtwksW2ihgO475cdZClMeG6bcY9%2FLTQ%2B27W300xiwU64%2Br%2FFcc0GJYV%2FzEgYDvuRXxB5EoawT6Gk0zKFx11RWGrhsBj1eFzAxWqdaNebFvfwZsxWXaUtrDFlqL7MnztWR5DktkQiR7JhLk%2B16pvVvdmCrdqHm%2FCVU3kjBPknn%2FUXePuhDq%2FOqvXw8WA3AWOF2NKScQKVilv0xRRyr8uQRxqxXZSsyVVc%2BnSB%2FWMqXriNVzJCVEpPWCpaIjZ28ABqk1MiSHN5dTj9SMV8MuCpToC9LuC2VqIIjeq0cYLygZ%2BARB2UYlRW0QyTkkcLUMBbLUfKH%2FMt6epq84h1GJOGTPyM5e8f9HwdbhwTzFiKLGdhpBC0KarVojTaiiwbmrlvKmdcIx20Sx1B3qDw454PnFO%2F9Y6e%2FAEc91RcKAFYmwskBXKOvhwwnZOyygY6pgGgYrc9tmG0g%2FNLYDMlrSk1rIBW9d0KCGo%2BNMLjHe7E52MBM6ia8t5HDNGTLImZmyEcFH4lSIb1fuBJsBfwZNbyGC2xKJ218aF%2BiUpyvSCwb7LLOrBG6q%2FRZOhR%2Fwod13laBWk2YU1OR84q1i2DVMhnhCvdf%2BYrdT0ujeFPJpOXCXt%2FxN9u8woVySl6CylQJ%2FDPUOCiCVIcllhqLRFvCgw1cOLXCKXA&X-Amz-Signature=d2a03be0923e2c5fcba49aa5d168279ca1e84a32c308294043aeacd0134dae36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



