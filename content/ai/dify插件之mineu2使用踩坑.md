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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDMLDFXX%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDYY%2FRKpbCiLa4CKOrUyCM%2FX093UGHWn2STlLwCd9Xf2AiEAkH%2Bqs%2BWYPPY18UUF592zwreXKVvALXAp9AWy0iVikrUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH6JLnReoermY6haSCrcAwoVjo6n7YDGODPATokhnH%2FHVNlF%2Bh71ufg8%2F%2BCxovuGMVBzWhs0wY0fotttvvsSnJfgIq5DkNdND8Cn3AewzfjFaRsAVwt4YO6jmprus1gNsRpJ%2BJxiA3eBFmXPnFfI2Mt7p14FK5B03T50qckIhNaZrUnShqZFecv4ErTNUkPIOH%2FdaUGFD4MbollefVb%2FVA299T4e8cy2fL54dx6PQwnk7B7MmXm2EJE5Bx7MlmFgqx3Ij6Tu4HmeNmcFZfwhGGyF0ZqGzHc10gSxTldDboJ8G%2FE2b%2FVdYoa6waq80ahNF3VSUYRCHJmauWjJ4y5FnVuRAVvtlyU8OuzN1gWHb%2Bn%2F3qkdzEacwRL1cAaKLB9jgG9DXwUDxvF7W2dWF7lAg8HO0Lcz9cLct1pH61aIp1g9FRl2mdfzsBWAJJfHAzE%2FCeH2kZtXtbYo4SY69BPmOt62IQ2JZQpOAyTec7bZHK%2F8ZZ48bdyeIUgLW%2FA%2FCT9q7S6nkQTsxrMeaYFBDzvLZTUrF6NcXlYcCjamiK3eYIDVK2FHK7OU%2B5HtKhz%2B%2Bg99lv0rIjAs2kMIxBDahCvx92BOliYPumW0xMou%2FF42QEfbJrrhXOqPiEXG0v7BZlrqdZOYcz%2FQnmo9QMk5MNLwr8gGOqUBdy3COyGVe%2F1VaTB8niTXBH7hskGB%2Bl%2Bs%2Bxq%2BNdgzE3se5od9ZRcU2Y7DL0cx2kG%2BtSG5vKFnJOmDEUqc%2BbxrT2eX26cFDzrhgb5CnVB4uIHUe1jAiCWnwjdHzqT3gG4Z%2FAuC5KvrUSSiFoIvLpqFKWFUIBoahfiEzTu9QuW715mqazHgHT17kLLQL%2FpV6FdCbz2cNK3CO03F2dD0fHGmeYR63fbT&X-Amz-Signature=de4fa24298d1c7ae6654ce00eadd0311103cf4a8a0cd38c7ec2c165d3c09081f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDMLDFXX%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDYY%2FRKpbCiLa4CKOrUyCM%2FX093UGHWn2STlLwCd9Xf2AiEAkH%2Bqs%2BWYPPY18UUF592zwreXKVvALXAp9AWy0iVikrUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH6JLnReoermY6haSCrcAwoVjo6n7YDGODPATokhnH%2FHVNlF%2Bh71ufg8%2F%2BCxovuGMVBzWhs0wY0fotttvvsSnJfgIq5DkNdND8Cn3AewzfjFaRsAVwt4YO6jmprus1gNsRpJ%2BJxiA3eBFmXPnFfI2Mt7p14FK5B03T50qckIhNaZrUnShqZFecv4ErTNUkPIOH%2FdaUGFD4MbollefVb%2FVA299T4e8cy2fL54dx6PQwnk7B7MmXm2EJE5Bx7MlmFgqx3Ij6Tu4HmeNmcFZfwhGGyF0ZqGzHc10gSxTldDboJ8G%2FE2b%2FVdYoa6waq80ahNF3VSUYRCHJmauWjJ4y5FnVuRAVvtlyU8OuzN1gWHb%2Bn%2F3qkdzEacwRL1cAaKLB9jgG9DXwUDxvF7W2dWF7lAg8HO0Lcz9cLct1pH61aIp1g9FRl2mdfzsBWAJJfHAzE%2FCeH2kZtXtbYo4SY69BPmOt62IQ2JZQpOAyTec7bZHK%2F8ZZ48bdyeIUgLW%2FA%2FCT9q7S6nkQTsxrMeaYFBDzvLZTUrF6NcXlYcCjamiK3eYIDVK2FHK7OU%2B5HtKhz%2B%2Bg99lv0rIjAs2kMIxBDahCvx92BOliYPumW0xMou%2FF42QEfbJrrhXOqPiEXG0v7BZlrqdZOYcz%2FQnmo9QMk5MNLwr8gGOqUBdy3COyGVe%2F1VaTB8niTXBH7hskGB%2Bl%2Bs%2Bxq%2BNdgzE3se5od9ZRcU2Y7DL0cx2kG%2BtSG5vKFnJOmDEUqc%2BbxrT2eX26cFDzrhgb5CnVB4uIHUe1jAiCWnwjdHzqT3gG4Z%2FAuC5KvrUSSiFoIvLpqFKWFUIBoahfiEzTu9QuW715mqazHgHT17kLLQL%2FpV6FdCbz2cNK3CO03F2dD0fHGmeYR63fbT&X-Amz-Signature=bba6960917bac721cd2ed21eeff1c4723ce8ff897ff7db94d8c71f0cc01fe69e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



