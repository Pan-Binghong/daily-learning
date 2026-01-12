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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OIAO77P%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCyKqxdr148xRis%2Bnbm2HKLvXEIu%2FPA5LWuHD6Jg6ansAIgeY5pst5PZgOxXicW1mhf6qKOgDgMhJShJ4kjxVcWx4gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKPjXQ1yoyAJ%2FTMIryrcA8z4sE1rv5T6cZLvLfUu5yLV0PrKE4frIjib0JX4JHB97SS6EeHxnZ8%2FLMST1CVGhApP48A7tMStIBAsC5EfXe2ui8txB6v8nuuy6SS7dMcnNGG6ydWnTpNwalG2cb%2F5RMdohmSRDx21NgvsNWGZ152LBrA1v3jayQYhn452HWp0mUWzF1aoNK345ennexfhEkoYz8y86RxStIWhQVva1D%2BSsDu8VPAxDQT0%2FCJ%2BYr5ermcZue2Tjs0f9coOW23bYIcnQVdH%2FJTNgNovPkQaDwThvsTalE5GkqFxD6EbOfVkH%2FAhVUx8QmiAwBvY4%2BFrZZF%2BHn22jS0ISOKJsoAoHhuDWCcXc1JKI9YwYdLtOZUSbjwBUKS%2F8aqaai98vLthabs9Aavm%2B8ihgjcS3tv4jGC%2BUkczYsD8jy4ldDumw1zbI0MGRigeiCTH8u1CmFGyoATdcqaX%2FWdeNYz26QpGpbZdDCbhzLxcytBf0Pf6MXk7w0vR5DvIt64MB9k25qFWny7ve7FbJuAtTQprmooke%2BJPwSACX6rjYINy6R40auIJzAa4Q%2Ba%2FhcBEbxEdeVgotVvA%2BXuwW244wevac6jhz2JhfT2KuZNzHFuH%2BY3Q8gdDHPEgY0XqXvqx9CCBMK73kMsGOqUBoX%2BVakoCA9fs2KOt3V0W%2BUYHJ6G3EZHPqhYcAbivfbhH0%2B%2F9xpkz18q5ZMeJKuAJpbCWxsWguC%2FuBXOkQJ2okP6sz3muYyqPjes4ObDWff0X6AngZTH1tJqckcmtWXtT%2FMHLSYSxvqtSyqCQmyVxK8Rfl7cXXjO8stByr0WkJWZoG%2FPAt36VR6FrZJfOAhKTLQ7JNz8zVfKtvQvxLg8GOrBe1meu&X-Amz-Signature=c0abfe8345e3754a1090ed58f80e8c3ea4b70ee81010097448cb4d728281b65c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OIAO77P%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCyKqxdr148xRis%2Bnbm2HKLvXEIu%2FPA5LWuHD6Jg6ansAIgeY5pst5PZgOxXicW1mhf6qKOgDgMhJShJ4kjxVcWx4gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKPjXQ1yoyAJ%2FTMIryrcA8z4sE1rv5T6cZLvLfUu5yLV0PrKE4frIjib0JX4JHB97SS6EeHxnZ8%2FLMST1CVGhApP48A7tMStIBAsC5EfXe2ui8txB6v8nuuy6SS7dMcnNGG6ydWnTpNwalG2cb%2F5RMdohmSRDx21NgvsNWGZ152LBrA1v3jayQYhn452HWp0mUWzF1aoNK345ennexfhEkoYz8y86RxStIWhQVva1D%2BSsDu8VPAxDQT0%2FCJ%2BYr5ermcZue2Tjs0f9coOW23bYIcnQVdH%2FJTNgNovPkQaDwThvsTalE5GkqFxD6EbOfVkH%2FAhVUx8QmiAwBvY4%2BFrZZF%2BHn22jS0ISOKJsoAoHhuDWCcXc1JKI9YwYdLtOZUSbjwBUKS%2F8aqaai98vLthabs9Aavm%2B8ihgjcS3tv4jGC%2BUkczYsD8jy4ldDumw1zbI0MGRigeiCTH8u1CmFGyoATdcqaX%2FWdeNYz26QpGpbZdDCbhzLxcytBf0Pf6MXk7w0vR5DvIt64MB9k25qFWny7ve7FbJuAtTQprmooke%2BJPwSACX6rjYINy6R40auIJzAa4Q%2Ba%2FhcBEbxEdeVgotVvA%2BXuwW244wevac6jhz2JhfT2KuZNzHFuH%2BY3Q8gdDHPEgY0XqXvqx9CCBMK73kMsGOqUBoX%2BVakoCA9fs2KOt3V0W%2BUYHJ6G3EZHPqhYcAbivfbhH0%2B%2F9xpkz18q5ZMeJKuAJpbCWxsWguC%2FuBXOkQJ2okP6sz3muYyqPjes4ObDWff0X6AngZTH1tJqckcmtWXtT%2FMHLSYSxvqtSyqCQmyVxK8Rfl7cXXjO8stByr0WkJWZoG%2FPAt36VR6FrZJfOAhKTLQ7JNz8zVfKtvQvxLg8GOrBe1meu&X-Amz-Signature=3237ec277293d8e06aec83da3c8fcb26f5b6305815104900911d1cfaa4864b7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



