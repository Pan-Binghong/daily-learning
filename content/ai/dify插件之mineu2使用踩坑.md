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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YRSGQXC%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQDRazpXoobS9oej%2FoAHndlPNt0zP3epuBqSaUzcG3GlBgIhAITIRrTR4d8k7rc1gBBqM4qOo9%2FNTd5tQeNQLYzp9TKWKv8DCDwQABoMNjM3NDIzMTgzODA1IgyCHeHdUk%2BtI6xKJOkq3APBL2in1m4zJtIR%2FLNbLbYUG7d4RSgZMNdTllyQ9VgHFFXS51DojBZ9dufg9NPYtW%2BoHpbn1Lcot%2B%2Fio709QKemf8vQTD6BnRn%2BiQU3uPA7oxI0FnUWGUS6oEO3qZSI0dBoK3CjVYE7mHIG8lBTz9tnY6eDHxpjG8%2FkV9m7wvRvATzFaNtWgwAR3hyIRPl94w28T4FTSMbzjtbljDXSX3x3MoZHPISqTlgE1G3cBhFsk4Q28frK68fOQ2UsB%2BNfDrWJt%2FhSdJUyhaR1CsSMqRbQCK6duWXfZQYhRNMLSAWlPEAGJwgMVRqLE8B2sVCH%2Fi0o0MDfIdIP%2BUKD2pJfJuRfBbv392im0FAYHfQo6xn%2FFvti8KbS4mg5tcMCqudJ6FnWzs7SBgcC%2Br21jxYZCSO9hkqrhYYCMMoR27%2FI%2BsJQb69bQRm8pXrIKvhk%2BXZOVuLxJdwpfH2PvR1RqOkZP7yajv0cBLaJqlHTJDB0GSVGE%2BTJX3JNXsVqs3FCeAbjGqXDGl2qvQfow1SpeCrSg7eUAFKJ9iLQv3mVrER0nq9pBZkzioBnAycakMof3b8zF3c0qovrpUjrdrsRAW7PE8gDKgjPrDOPpDyh5Bh8FSgsenim9xw0OXkwpRBRCTCDuZXMBjqkATEVyKw%2F3ImBXwObxU%2F0oXgMWHLKZVTnMp%2F1zmtfzU2p7vVftWjFJ3m2Sc7vNhlVHOy5z5Rcn2dHc2bUS8UR34df61TUa6UN1RGXDMaKanV%2BkDZ%2F4C5HaoaMSWHw48uExpY%2B2AySTEWA%2FGwkQNzp%2FtmBSigBQr6Enmv3CNDgPnHMH%2B%2F1CxqFPvDeoQit7tCtY552ooSylj5MRsmyOdek%2Brn70G36&X-Amz-Signature=f1f3e772ffbdb74a1334e7ab121e6d844a50e88fc18bddf4ee7620299b76b31a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YRSGQXC%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQDRazpXoobS9oej%2FoAHndlPNt0zP3epuBqSaUzcG3GlBgIhAITIRrTR4d8k7rc1gBBqM4qOo9%2FNTd5tQeNQLYzp9TKWKv8DCDwQABoMNjM3NDIzMTgzODA1IgyCHeHdUk%2BtI6xKJOkq3APBL2in1m4zJtIR%2FLNbLbYUG7d4RSgZMNdTllyQ9VgHFFXS51DojBZ9dufg9NPYtW%2BoHpbn1Lcot%2B%2Fio709QKemf8vQTD6BnRn%2BiQU3uPA7oxI0FnUWGUS6oEO3qZSI0dBoK3CjVYE7mHIG8lBTz9tnY6eDHxpjG8%2FkV9m7wvRvATzFaNtWgwAR3hyIRPl94w28T4FTSMbzjtbljDXSX3x3MoZHPISqTlgE1G3cBhFsk4Q28frK68fOQ2UsB%2BNfDrWJt%2FhSdJUyhaR1CsSMqRbQCK6duWXfZQYhRNMLSAWlPEAGJwgMVRqLE8B2sVCH%2Fi0o0MDfIdIP%2BUKD2pJfJuRfBbv392im0FAYHfQo6xn%2FFvti8KbS4mg5tcMCqudJ6FnWzs7SBgcC%2Br21jxYZCSO9hkqrhYYCMMoR27%2FI%2BsJQb69bQRm8pXrIKvhk%2BXZOVuLxJdwpfH2PvR1RqOkZP7yajv0cBLaJqlHTJDB0GSVGE%2BTJX3JNXsVqs3FCeAbjGqXDGl2qvQfow1SpeCrSg7eUAFKJ9iLQv3mVrER0nq9pBZkzioBnAycakMof3b8zF3c0qovrpUjrdrsRAW7PE8gDKgjPrDOPpDyh5Bh8FSgsenim9xw0OXkwpRBRCTCDuZXMBjqkATEVyKw%2F3ImBXwObxU%2F0oXgMWHLKZVTnMp%2F1zmtfzU2p7vVftWjFJ3m2Sc7vNhlVHOy5z5Rcn2dHc2bUS8UR34df61TUa6UN1RGXDMaKanV%2BkDZ%2F4C5HaoaMSWHw48uExpY%2B2AySTEWA%2FGwkQNzp%2FtmBSigBQr6Enmv3CNDgPnHMH%2B%2F1CxqFPvDeoQit7tCtY552ooSylj5MRsmyOdek%2Brn70G36&X-Amz-Signature=0b740d27f67f420edd3d652e532ccd42a38fa4b0ed8cba0ca8673677cb8ae389&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



