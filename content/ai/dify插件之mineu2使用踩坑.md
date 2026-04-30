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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YX3SRJL%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIFoL4VKHSaosrHJ19RT4UjVRqkHvUx4TDQWeI0%2BlyA58AiA72HGIs2XGWZ4k70N6Z8Oqb0pVOvQZOsaKYuflCjBMsyr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIM9e3FZ16ad0q%2Fg2jHKtwDLbzJkHV7FbWa%2FU7kmynMq9F8ZBO%2BbjuBK1us4nbJEbNBaXNR32fxxTAZ8AcmBMa0Qfkqd8xr4aHqact%2FPofRUkAXkeSSBaqvuhj2OU4knJC3xGH8Vim1c1u%2BL8RINg6hSAF1nTKthm%2Fs5DtHgsw3qQKFz%2FPPdkI4janTE42LY8ibbAral8SRNlPdFOjJXM04Rv4y%2BPO2O%2F7M8kNkgd575XqWiJxManeGEoyMLx2nY5qoTd2fJKtqvvSnedj9quNTNFLU4LWXDCxd3bTmoB9idQE%2BMXpymoeDE3clmbU2RWmi05Rd4me8CnPYnr%2Bhuv5LdOpaVv4yyRhRtx8p9f9gAIiwwT%2FST7m5rmuDWkkTpY09sAiIz3VVaVqtOpSd8%2BDSxW8X3glva6EtI%2FQHFcdsaBvb9JuL8Qco6WdC%2FZX%2BFKDHUWX4xwRgFT5xt5HcF6uCPI2yYEiCmW3oj53acJvjD2aIfsPoSUFp4mpM4vF7taKQ7Boae0HVAa7Vn1FfQ1%2BFODRxyjgs7wMvTiGstmZEhBb9VzVRL8So68wScNJCitkU0MAv0a%2BOriFwrg%2BmynsXPrIFKO%2FtY4vs%2B%2F%2FYqSQ5h6mKgBuFJJ%2B3hyIWheW%2BPfMHkCMnBbTRsCyoHhIwkpzMzwY6pgEZ9i5z3JcN9tv8hOqjHTW6V0ndDc%2BB6dcX67gU9HDQwGsMPZKco1HJxpINPcMsSdrLRbKjo%2ByFhTgjMVFusnf2yIhiBytLuEdumPO9POOtuAgZ8n75DW0bpXw7QwzlWTbxbW3Fge8sSHVODefwujkeIcudk1ENRS0JPOSbsx4yFc06SYiPd9EFNZxssigLsWJvLLfvyC030yhkhV%2BC%2B8i3NGM3mizQ&X-Amz-Signature=349dac99c9d3c029ed1fce3e59cabf091b0e7032efa519913d81eae8e14aaf41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YX3SRJL%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIFoL4VKHSaosrHJ19RT4UjVRqkHvUx4TDQWeI0%2BlyA58AiA72HGIs2XGWZ4k70N6Z8Oqb0pVOvQZOsaKYuflCjBMsyr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIM9e3FZ16ad0q%2Fg2jHKtwDLbzJkHV7FbWa%2FU7kmynMq9F8ZBO%2BbjuBK1us4nbJEbNBaXNR32fxxTAZ8AcmBMa0Qfkqd8xr4aHqact%2FPofRUkAXkeSSBaqvuhj2OU4knJC3xGH8Vim1c1u%2BL8RINg6hSAF1nTKthm%2Fs5DtHgsw3qQKFz%2FPPdkI4janTE42LY8ibbAral8SRNlPdFOjJXM04Rv4y%2BPO2O%2F7M8kNkgd575XqWiJxManeGEoyMLx2nY5qoTd2fJKtqvvSnedj9quNTNFLU4LWXDCxd3bTmoB9idQE%2BMXpymoeDE3clmbU2RWmi05Rd4me8CnPYnr%2Bhuv5LdOpaVv4yyRhRtx8p9f9gAIiwwT%2FST7m5rmuDWkkTpY09sAiIz3VVaVqtOpSd8%2BDSxW8X3glva6EtI%2FQHFcdsaBvb9JuL8Qco6WdC%2FZX%2BFKDHUWX4xwRgFT5xt5HcF6uCPI2yYEiCmW3oj53acJvjD2aIfsPoSUFp4mpM4vF7taKQ7Boae0HVAa7Vn1FfQ1%2BFODRxyjgs7wMvTiGstmZEhBb9VzVRL8So68wScNJCitkU0MAv0a%2BOriFwrg%2BmynsXPrIFKO%2FtY4vs%2B%2F%2FYqSQ5h6mKgBuFJJ%2B3hyIWheW%2BPfMHkCMnBbTRsCyoHhIwkpzMzwY6pgEZ9i5z3JcN9tv8hOqjHTW6V0ndDc%2BB6dcX67gU9HDQwGsMPZKco1HJxpINPcMsSdrLRbKjo%2ByFhTgjMVFusnf2yIhiBytLuEdumPO9POOtuAgZ8n75DW0bpXw7QwzlWTbxbW3Fge8sSHVODefwujkeIcudk1ENRS0JPOSbsx4yFc06SYiPd9EFNZxssigLsWJvLLfvyC030yhkhV%2BC%2B8i3NGM3mizQ&X-Amz-Signature=8db3d002ec2c08a8220b23647f642912f502a7365e19c4c575f76dc8695a2de5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



