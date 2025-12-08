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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HIJBYUZ%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGCLs1ozQyEBIHRTVHqf4o2PgLMimcr8hsSsRbfCjiHgIgOK1X9yp7As8NdGCdttH5nkhS3UY3iLOgbUJdslYypgkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFq%2BWj4i9zxOtZo2wircA0BMXGZRHIFmfmztx9g2FKPL5HJb9QwwiqlEb3iMj%2FH83tCDPG2ewBKFImANcM%2BI07xSG9hpO3vlq3QKX3XXVz1wtSqWq6b9ZusBoGtn6PoKX6i3eMkqO8iDHCqVaSgl%2BVsJUqlxta68Og%2FtYAwcaYtpBaD7pfeQsUJfI27Zp%2BlA1gn5%2FQBJGVcnwYAK8Reex1hLMqQVRyiQZVwBiPLmCZrSe4JBnch%2F22vzZGLSynkpH3VQobFK5K%2FQh5b98lwHQ4XsU%2Fd5RFuwS9K37hjohrcXNv5FEU%2FvSGWoZHgjnmdtSa3y1vLaeyy3yccw9h1Ao2dPPKOv7l9gqhbO87i9KflMNA29qpXCMtw9feIW0kDoOFv6lwtSnCroSsJ1VYlsti9xJ5wgR%2FpMpgcssoPOAu7kDlENHhy10jrh36ZNixJoXKH3erpAGKFRwSLEWhmsc%2BWq06ewXT9Vsc2lygspph7lTpchG%2BuDH1w6jSIKWbXZCh3rWMleC2omY9b2Fja60E0TxIX%2FxIgxpFq%2Fl7UKMz5pRinZcr3n3fUkUBjm0cdEjbyMNgTwZMBnTHgYjv%2FoMVYrqDIO1jsk4hXLjXeHCaN2%2BO384Er%2FlPuFh14PwBUYJMCIRnyc1ZJmfdAYMOzu2MkGOqUBa%2B4mn4rPgOExAnU9kdRqINDFFSRQNwlT2%2Bwi7mMfSnA5fmoLwxwZuuAwzoNUNyznIFsbP%2BaDzE3KL9ydE%2FUdNyKAe3QLCHuBifHrTyNJWY9xP1zpC86sUmnKAg0Qg51A1aYvSzLo8M5rNa1JS8NHPfAU4DvWOhsqgrdlRU%2BYTQCBpeEn895sQz%2BJ14M3gheiHuAnELBpzh%2Bl4%2B00HZVr5EfbGMQw&X-Amz-Signature=1246b1d846c3e17cb79916dab435f1b9648354ba18f55dae63d12031d328332a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HIJBYUZ%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGCLs1ozQyEBIHRTVHqf4o2PgLMimcr8hsSsRbfCjiHgIgOK1X9yp7As8NdGCdttH5nkhS3UY3iLOgbUJdslYypgkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFq%2BWj4i9zxOtZo2wircA0BMXGZRHIFmfmztx9g2FKPL5HJb9QwwiqlEb3iMj%2FH83tCDPG2ewBKFImANcM%2BI07xSG9hpO3vlq3QKX3XXVz1wtSqWq6b9ZusBoGtn6PoKX6i3eMkqO8iDHCqVaSgl%2BVsJUqlxta68Og%2FtYAwcaYtpBaD7pfeQsUJfI27Zp%2BlA1gn5%2FQBJGVcnwYAK8Reex1hLMqQVRyiQZVwBiPLmCZrSe4JBnch%2F22vzZGLSynkpH3VQobFK5K%2FQh5b98lwHQ4XsU%2Fd5RFuwS9K37hjohrcXNv5FEU%2FvSGWoZHgjnmdtSa3y1vLaeyy3yccw9h1Ao2dPPKOv7l9gqhbO87i9KflMNA29qpXCMtw9feIW0kDoOFv6lwtSnCroSsJ1VYlsti9xJ5wgR%2FpMpgcssoPOAu7kDlENHhy10jrh36ZNixJoXKH3erpAGKFRwSLEWhmsc%2BWq06ewXT9Vsc2lygspph7lTpchG%2BuDH1w6jSIKWbXZCh3rWMleC2omY9b2Fja60E0TxIX%2FxIgxpFq%2Fl7UKMz5pRinZcr3n3fUkUBjm0cdEjbyMNgTwZMBnTHgYjv%2FoMVYrqDIO1jsk4hXLjXeHCaN2%2BO384Er%2FlPuFh14PwBUYJMCIRnyc1ZJmfdAYMOzu2MkGOqUBa%2B4mn4rPgOExAnU9kdRqINDFFSRQNwlT2%2Bwi7mMfSnA5fmoLwxwZuuAwzoNUNyznIFsbP%2BaDzE3KL9ydE%2FUdNyKAe3QLCHuBifHrTyNJWY9xP1zpC86sUmnKAg0Qg51A1aYvSzLo8M5rNa1JS8NHPfAU4DvWOhsqgrdlRU%2BYTQCBpeEn895sQz%2BJ14M3gheiHuAnELBpzh%2Bl4%2B00HZVr5EfbGMQw&X-Amz-Signature=a4f803f16898224b29eed75ea9b4141456cc19d7921472d18a0093be9e65e4bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



