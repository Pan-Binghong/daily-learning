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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQP2XTQK%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQCfTsLd7NOv%2FRb3Zw5PRqxU5SVaEHK6pCpYydVI4MrCSQIgbR05jmwycyPphBewiJxpZ7%2Bi1ZN7QNs4jwLHkBJQv6Uq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDJ5bXagA3TyBnE9SZSrcA1NyxY9fV6WZ8bDq1kwo%2FYY4S9DVt8%2FdFeC8ag9pG87fX6QZfCCDmCJrGTrNjoLomHKz1th0ApbyQcdMQIqS4toAls77FOJF2kCigNgG0kYYuym5tD9DAVYYiQf9aY6fQsxU6mbhO8gHovkDuXhcOb9ARs28V4CHojkQTzeirxAwDljVLQ9AgtOwoMynliv5s0vFuBdmjopq3OvYHY1sBky9no12mBx5IjNaddQgwql%2Bt9Us4UVd9DpnS7FwXhKMSCP%2B96F5jsxynvPvMbJcQRXs1RrAcUTihP8NmkQUgsqtFSyohgBzRg%2Fi6TGtuhozhXtcFYmoNnp2psHyH4BHZqCFmVfCrIANJX8UmG2shVqU13OL2r8bRJlANFdq2yhgkNiW%2FaLWi8Quh4FGoduaxJZmyX%2ByBFi36UMobAGM965V1x4RfN3v9SnwvQkcYmWslVg9ocSaX8NS45mSYaOwOQNUSN6jOqjPvjwSgNiRy3sfYKPD9clFFj%2FowtUMWYm12QglYqiPanynkYn%2B2yzCjLs9KE5l5M6vvGsekvV3Ht0ISQormWZK2ekUnOaqtI1bzM5dyqVNiX8Rno9Zj0wE5mEPqQ6y2ndoILF9qd2aD1e2T0KLUSVonz3j3H1KMPjO0MsGOqUBN5%2BaINeQkthVV5K%2Bpcl7RoEnsqiI9grxA1XsA3nh9VdWhQ9g0lAXcEdeS65YHB3OgWae6euOOM4rCny5P%2F63VKGT16LX%2F19q9mHqUNBGjTz981T7LOMJ1WfCeMIdFT2D3Xw7SJ4pbJfnjRQCIDEo2jx%2FxJLn1VaAIZkygQK5ZW7lHSt33bXUJTNSjNWxuTUzbPf6oOkxnP6JJg0uSCtoPU9H1uRI&X-Amz-Signature=425d4ea982db165ecb75e5379d3b7f9b3eca358cd07ac7adde8394ae9365de01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQP2XTQK%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQCfTsLd7NOv%2FRb3Zw5PRqxU5SVaEHK6pCpYydVI4MrCSQIgbR05jmwycyPphBewiJxpZ7%2Bi1ZN7QNs4jwLHkBJQv6Uq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDJ5bXagA3TyBnE9SZSrcA1NyxY9fV6WZ8bDq1kwo%2FYY4S9DVt8%2FdFeC8ag9pG87fX6QZfCCDmCJrGTrNjoLomHKz1th0ApbyQcdMQIqS4toAls77FOJF2kCigNgG0kYYuym5tD9DAVYYiQf9aY6fQsxU6mbhO8gHovkDuXhcOb9ARs28V4CHojkQTzeirxAwDljVLQ9AgtOwoMynliv5s0vFuBdmjopq3OvYHY1sBky9no12mBx5IjNaddQgwql%2Bt9Us4UVd9DpnS7FwXhKMSCP%2B96F5jsxynvPvMbJcQRXs1RrAcUTihP8NmkQUgsqtFSyohgBzRg%2Fi6TGtuhozhXtcFYmoNnp2psHyH4BHZqCFmVfCrIANJX8UmG2shVqU13OL2r8bRJlANFdq2yhgkNiW%2FaLWi8Quh4FGoduaxJZmyX%2ByBFi36UMobAGM965V1x4RfN3v9SnwvQkcYmWslVg9ocSaX8NS45mSYaOwOQNUSN6jOqjPvjwSgNiRy3sfYKPD9clFFj%2FowtUMWYm12QglYqiPanynkYn%2B2yzCjLs9KE5l5M6vvGsekvV3Ht0ISQormWZK2ekUnOaqtI1bzM5dyqVNiX8Rno9Zj0wE5mEPqQ6y2ndoILF9qd2aD1e2T0KLUSVonz3j3H1KMPjO0MsGOqUBN5%2BaINeQkthVV5K%2Bpcl7RoEnsqiI9grxA1XsA3nh9VdWhQ9g0lAXcEdeS65YHB3OgWae6euOOM4rCny5P%2F63VKGT16LX%2F19q9mHqUNBGjTz981T7LOMJ1WfCeMIdFT2D3Xw7SJ4pbJfnjRQCIDEo2jx%2FxJLn1VaAIZkygQK5ZW7lHSt33bXUJTNSjNWxuTUzbPf6oOkxnP6JJg0uSCtoPU9H1uRI&X-Amz-Signature=8b94ad9508c18920f3abbe7706f7412782711470bf868aa2e50402c6a23b3467&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



