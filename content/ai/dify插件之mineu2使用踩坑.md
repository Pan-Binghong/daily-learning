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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFTRL2T%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQCfHP10FmdivWQy6bSAIR633AQEm1s7Mci37zIy7mBNLAIgYFeYgZxWVOivbi7CYyN1rQfeG0P19Xmj90WOuyuFcJYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKU7TIAGRPGEWeowASrcA9FLWrHT4AoKz%2BnK18FoNH7WdigC5tfkAMgZPo9y2JUoVf0xBVUSooMhZHyg5m9e%2Ft5IBEjscOPK4OVxrAXoSyr9Y6nB5S1XrEtYn6K%2FmsK9rOptIxrOZXBEiswUKC5u3nEZmzIVljCyI5kz%2FgELsCQixdm5mcnG08YnQ6YXFAVFd307yYv9QDrQ56uCj3LQ9lO9uBAmUM3%2F%2BLbp7sZ7tsDgiVqD3MapaA0u1rac%2Fr0bAgMHt3ZVuVaqhG4lMXqsZm8m49ahf7BmOLbKcXHTLdJblxUzTwYMwLQTo%2F0t634GFC%2Fpm5nbbCygrd8eQ%2F19tGqnDri8acuZPnfFtk9uFz42oUMtp%2FlJ%2B%2BQHcuac35XHHaK9AdYEyRLOB1EScKe5XYJPAlaAb%2FaR68PfUufTHS%2FCZFtg%2B%2F3bar7ygYmaWIptgReP%2F9xjHzU2wJXCdIhjwNybP8i7ctkznsjKyVHGkjupLwlAG3wgzupoSk%2FL24r9BO0gHOOuyZ1M5QPe2s6tD5I1PL%2BSO7kas7KaXZJFGX0R3LqCAV3S28cfwy49VnuBIMAVt%2BrWwE6MuFcV3Eu6hNwiyBEvH%2BN01nrbjriTsOm1WUxe5SJE3EvzbejkuIiQ6ffQkFKuN0Fz95iZMJXI3MoGOqUBzYB0wII1qjVm1sGxsvwqTJFpSK15ReBFWyrzh6ytzFEHfBQKLOKibV1aj4ixU976IJok47rQMvKSJ4VxlgLnxnWvzMkD6TNQQzjFjd3Bp4nQ8BooM0NyDPqt0UGFrgqCYWmMXBcXdChUWoxTtpH0SXyHrVxi5zxM5kUBDvEW9PIDM8v%2FMH%2B3ArhRGR32S4kYX3Ju00UaXEbTLc%2F%2FLlOSKWvAf704&X-Amz-Signature=6651ecc78095c3c02b691af466ef77720cf37e719ed31b8e30e458abbe3e1d4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFTRL2T%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQCfHP10FmdivWQy6bSAIR633AQEm1s7Mci37zIy7mBNLAIgYFeYgZxWVOivbi7CYyN1rQfeG0P19Xmj90WOuyuFcJYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKU7TIAGRPGEWeowASrcA9FLWrHT4AoKz%2BnK18FoNH7WdigC5tfkAMgZPo9y2JUoVf0xBVUSooMhZHyg5m9e%2Ft5IBEjscOPK4OVxrAXoSyr9Y6nB5S1XrEtYn6K%2FmsK9rOptIxrOZXBEiswUKC5u3nEZmzIVljCyI5kz%2FgELsCQixdm5mcnG08YnQ6YXFAVFd307yYv9QDrQ56uCj3LQ9lO9uBAmUM3%2F%2BLbp7sZ7tsDgiVqD3MapaA0u1rac%2Fr0bAgMHt3ZVuVaqhG4lMXqsZm8m49ahf7BmOLbKcXHTLdJblxUzTwYMwLQTo%2F0t634GFC%2Fpm5nbbCygrd8eQ%2F19tGqnDri8acuZPnfFtk9uFz42oUMtp%2FlJ%2B%2BQHcuac35XHHaK9AdYEyRLOB1EScKe5XYJPAlaAb%2FaR68PfUufTHS%2FCZFtg%2B%2F3bar7ygYmaWIptgReP%2F9xjHzU2wJXCdIhjwNybP8i7ctkznsjKyVHGkjupLwlAG3wgzupoSk%2FL24r9BO0gHOOuyZ1M5QPe2s6tD5I1PL%2BSO7kas7KaXZJFGX0R3LqCAV3S28cfwy49VnuBIMAVt%2BrWwE6MuFcV3Eu6hNwiyBEvH%2BN01nrbjriTsOm1WUxe5SJE3EvzbejkuIiQ6ffQkFKuN0Fz95iZMJXI3MoGOqUBzYB0wII1qjVm1sGxsvwqTJFpSK15ReBFWyrzh6ytzFEHfBQKLOKibV1aj4ixU976IJok47rQMvKSJ4VxlgLnxnWvzMkD6TNQQzjFjd3Bp4nQ8BooM0NyDPqt0UGFrgqCYWmMXBcXdChUWoxTtpH0SXyHrVxi5zxM5kUBDvEW9PIDM8v%2FMH%2B3ArhRGR32S4kYX3Ju00UaXEbTLc%2F%2FLlOSKWvAf704&X-Amz-Signature=9b19071e4dfea895c750872c1b4313b59b89dfdcf4eda1a78e5f61df5a8b5d59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



