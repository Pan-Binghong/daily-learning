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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ISPZBBE%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD%2F170Gumv546zl6tY5bGQetIH9VZBo4ATk5srZyyI9OAIhAKPleRAC7lsXpNioaH41Im5wvKaoRxIzOjr%2Bh7k%2Fz4BtKv8DCAQQABoMNjM3NDIzMTgzODA1IgxcLArOL6MaQNZl9ykq3APRF%2F3TW%2FWJM3VqBg1JXrFv30QMPYZVY38lbzErLh7CJ50p%2BWz7RVl3JI8yHWgyIUuV98IZzelBqdDCrLADWF8wlvUlkPx9lwx8viWi2grwhT6NybXqXEjRxSpKJGAyWRcCB%2FGdmAUzmvFhVlS0aKVE0MoWayAbhB7Q%2Fc9s7%2BB8Jt2zgp%2FN61VS4S5RxlqFSSOLRvckZkovwuRdTCNy2zGzGpjOhIfZNiNugGGsnOLVY0dtRImMhNJkJ3HB3MQsmHFxcy4JQWZeUFPEZ0FazUf%2FqE8vqhkDukBSbhbQeg7vScdKsf8KYytywkCAS4v1A%2B8U78MITEsZ1Pa47HhFYJtJM4PQZixPu8jZgXbNn5HMlEn%2F3pxEnTTayxXZrHlU6OQ7pdJ24YXYX5pM4y3ohIdFUyJt6f1THLc9dVPh%2B2GLlD3LZtbfKCMFR58Zhgp0Mprf0j2zWP9mU74sBG4ER4D0qNwB71Cj8pFRBaO0sfUdfH%2BiVUgPMiqDmnbS%2FvfFaXRY6DbgF47OgiWwsKtDHOMvXcDHfpZzRfJrFU%2BewfnfzDz5Bp%2BowywO2ToZ8HB2nWMSuWag52Hcve5FdiPb2xTRd4Peby%2BDY6d9f21S382Sjmdyr7P8kUMiWDkScjCO%2FafKBjqkAb5TnppULt7RawooyIygk22YaG78TqsqAJTDEObk8tfwsgJpPH9wJnBq2CL%2B2xvaBMvc%2FWHiqV7n%2BKF1JuJcghSyZOrJ%2FObyVldLQnRkx65W8uyL3D%2FN0a6Y6mpUu2g7EbH7%2FYlt%2FFUdvYoLMGH%2F%2FI4591CX1bNHS0OU4utmfdLowlS%2Bm0sE4k%2FkH6CgGSnN7ncr6XBMP2a1CtRn4DFkDeWE9E50&X-Amz-Signature=8f414e42a3c93069282a81df6ef15b51425fa94db2fca716a464b8e224828668&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ISPZBBE%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD%2F170Gumv546zl6tY5bGQetIH9VZBo4ATk5srZyyI9OAIhAKPleRAC7lsXpNioaH41Im5wvKaoRxIzOjr%2Bh7k%2Fz4BtKv8DCAQQABoMNjM3NDIzMTgzODA1IgxcLArOL6MaQNZl9ykq3APRF%2F3TW%2FWJM3VqBg1JXrFv30QMPYZVY38lbzErLh7CJ50p%2BWz7RVl3JI8yHWgyIUuV98IZzelBqdDCrLADWF8wlvUlkPx9lwx8viWi2grwhT6NybXqXEjRxSpKJGAyWRcCB%2FGdmAUzmvFhVlS0aKVE0MoWayAbhB7Q%2Fc9s7%2BB8Jt2zgp%2FN61VS4S5RxlqFSSOLRvckZkovwuRdTCNy2zGzGpjOhIfZNiNugGGsnOLVY0dtRImMhNJkJ3HB3MQsmHFxcy4JQWZeUFPEZ0FazUf%2FqE8vqhkDukBSbhbQeg7vScdKsf8KYytywkCAS4v1A%2B8U78MITEsZ1Pa47HhFYJtJM4PQZixPu8jZgXbNn5HMlEn%2F3pxEnTTayxXZrHlU6OQ7pdJ24YXYX5pM4y3ohIdFUyJt6f1THLc9dVPh%2B2GLlD3LZtbfKCMFR58Zhgp0Mprf0j2zWP9mU74sBG4ER4D0qNwB71Cj8pFRBaO0sfUdfH%2BiVUgPMiqDmnbS%2FvfFaXRY6DbgF47OgiWwsKtDHOMvXcDHfpZzRfJrFU%2BewfnfzDz5Bp%2BowywO2ToZ8HB2nWMSuWag52Hcve5FdiPb2xTRd4Peby%2BDY6d9f21S382Sjmdyr7P8kUMiWDkScjCO%2FafKBjqkAb5TnppULt7RawooyIygk22YaG78TqsqAJTDEObk8tfwsgJpPH9wJnBq2CL%2B2xvaBMvc%2FWHiqV7n%2BKF1JuJcghSyZOrJ%2FObyVldLQnRkx65W8uyL3D%2FN0a6Y6mpUu2g7EbH7%2FYlt%2FFUdvYoLMGH%2F%2FI4591CX1bNHS0OU4utmfdLowlS%2Bm0sE4k%2FkH6CgGSnN7ncr6XBMP2a1CtRn4DFkDeWE9E50&X-Amz-Signature=9eb291c2d0f3a55f39cc6bfb19ce8ea38a9da98efefcc5eb21388b720f4aa07e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



