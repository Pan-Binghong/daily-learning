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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662B2FRNLV%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIBQOCDIJA7xrOlcfhoboZkoRP95UlBRMahaB2wncyA15AiEAv2Z1aC34piY6vK%2BgdNd0e%2BcVzOHVhwLtzza2o%2FGgKVcqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN9ni1bhHXjajEvmxSrcA%2B5E2Ilv06Uxj%2FRt1e%2BimaUCOVV2jTS2b%2FPlDS4xcoQK3fI1LiCTRw3k9IOI%2BwiqAMDAoJKLCvaxIzQicA9esuVxNZYxIRvz8uE9Ec3WVgnfMFtMnZkeTQJVSlM9ZxiNtIvIU%2FQop1Q7lSri0Oy19sMSb0arGTLrC6ee37Xbnl5LnjQqmMY8%2B3ynjwqdE8lfKyVVk37VANYtjPpD9tAHz0KjWVeWAx%2FOdhYE84vDTfgxSEU75O9Um%2B9wE%2FRPk11JDJB%2F4Eoj4vGeSPhJ8rVooFuJkltf32SWD21b%2BIEN95snhIlunlSnVLugXvvM9VE8UbUm2oRuiyWSBbloITgrKe0yqR3piNCz%2F4GRDsWCktC8Zra99D%2FzW22j2UNSspiHlBbVgZ3qGvEdidC4x%2BVUzGXojtUwW8xseG8RhJMqek%2Bz8bGSalgeZ7dDrungNFGrubPfu33GAGQZujV1oDUByXmZY5HNetbU1gsW%2BX55ezUD2ooX714sNxRA%2By4klFfvU5x27JfPV42S5GFdA6qmJrNsJTr2yd%2F%2F%2FLRR8fvD%2F1V3o6tNGMAsmqQhlhLcPIiGi%2Bwhc2fszOok4nRLPi9lP%2B3hw1CstJM5C5yt0o4uW0Q%2FasOjmTub1W4AUOXyMIjmosoGOqUBAYxrESATK1WBx9vpXlHwnwwACIFnPJwCDYyaTfRgq%2FzaVLBwQuE%2B98nR1fEyV%2Ff%2BQ4lUvq6Ou%2FIH06jdBOjxdUuB%2FycYxNSXZgZburx1HOEv1G5zMh%2BphNuaFtdmcDv%2FFnl0lQqGv%2Bd6Ctq1fbbPJWmzVEqMQ2sFS6jwKKa5IK1NOFIVoGxMd7ErPU7JCU6%2Bf08hHFelW1wosGBM1Xovws2MHTuJ&X-Amz-Signature=54a99d4268969380fe5acf773c685d9e8b6350950cbd18a84bd6d47a1f96eb2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662B2FRNLV%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIBQOCDIJA7xrOlcfhoboZkoRP95UlBRMahaB2wncyA15AiEAv2Z1aC34piY6vK%2BgdNd0e%2BcVzOHVhwLtzza2o%2FGgKVcqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN9ni1bhHXjajEvmxSrcA%2B5E2Ilv06Uxj%2FRt1e%2BimaUCOVV2jTS2b%2FPlDS4xcoQK3fI1LiCTRw3k9IOI%2BwiqAMDAoJKLCvaxIzQicA9esuVxNZYxIRvz8uE9Ec3WVgnfMFtMnZkeTQJVSlM9ZxiNtIvIU%2FQop1Q7lSri0Oy19sMSb0arGTLrC6ee37Xbnl5LnjQqmMY8%2B3ynjwqdE8lfKyVVk37VANYtjPpD9tAHz0KjWVeWAx%2FOdhYE84vDTfgxSEU75O9Um%2B9wE%2FRPk11JDJB%2F4Eoj4vGeSPhJ8rVooFuJkltf32SWD21b%2BIEN95snhIlunlSnVLugXvvM9VE8UbUm2oRuiyWSBbloITgrKe0yqR3piNCz%2F4GRDsWCktC8Zra99D%2FzW22j2UNSspiHlBbVgZ3qGvEdidC4x%2BVUzGXojtUwW8xseG8RhJMqek%2Bz8bGSalgeZ7dDrungNFGrubPfu33GAGQZujV1oDUByXmZY5HNetbU1gsW%2BX55ezUD2ooX714sNxRA%2By4klFfvU5x27JfPV42S5GFdA6qmJrNsJTr2yd%2F%2F%2FLRR8fvD%2F1V3o6tNGMAsmqQhlhLcPIiGi%2Bwhc2fszOok4nRLPi9lP%2B3hw1CstJM5C5yt0o4uW0Q%2FasOjmTub1W4AUOXyMIjmosoGOqUBAYxrESATK1WBx9vpXlHwnwwACIFnPJwCDYyaTfRgq%2FzaVLBwQuE%2B98nR1fEyV%2Ff%2BQ4lUvq6Ou%2FIH06jdBOjxdUuB%2FycYxNSXZgZburx1HOEv1G5zMh%2BphNuaFtdmcDv%2FFnl0lQqGv%2Bd6Ctq1fbbPJWmzVEqMQ2sFS6jwKKa5IK1NOFIVoGxMd7ErPU7JCU6%2Bf08hHFelW1wosGBM1Xovws2MHTuJ&X-Amz-Signature=d4beb60f6407e31fe4de8a856dc30052289f566bd9128f213b09ada254e1b3be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



