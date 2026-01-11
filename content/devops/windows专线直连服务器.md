---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K6GM7VY%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIBgIlBNERFVb2DLC0KK7eJ8ItoxHhUtsy0SJthPo1dK%2BAiEA2R8ukM%2FjlyeMvAW9qCw8l7DQJCD5x0FeUNGqRrTxX1IqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEVUc3R9cEfUf9INByrcA4D%2BRILawO2i%2FU0nWjek85v9XY3YCoe8tR1hSREnZWCOa4vYR8U3Hy3uyGBZQLKTpukzdJYYHIjzCyAtAQhJVSqcTxHN7Axa65QCKm6I10KgT90EZJyaH6pS6Y7wVv3a7GP3L%2FfL4woKiX9XpJeTGbZj9rQ%2F%2FcnEay1z8NP6D8mlvZkBauzjb7lsl1b2D8Ey1TZ0oOAgI2DCVtfwT%2Btq6Hv1NY3bpBar4tEEDoqG2qmC212Bm4WeFTYKdwZMK3KZDynonIuhLcmF8iHjHIxDT976W8Lch2T2WUXWENE%2Bsu6yo%2FccE9k%2FHZQvLKHv%2B3Pupt1Qgqe2zmLS2td6la3%2F6YGCiotc%2Bcfm2W%2FmKOG984fxK1xn%2BCn5IuoYpNMnQc1UqRcUyQwb6hfbqjHMCB8v3S1QfastQ2puzcflMKl5qsLksdezLDI%2BEwxS3gUT5CEOutAuLIK1alVNnK1jTgs7GQE0hzWm8ixTJziZcwRUDVnAliN23oZWm4G36Jwaply4RTNeL30vz0y%2FgYKKC89wuJYDD3uk%2BvVwMW4kxsOMWNIttYj5GLd6slxywa%2FFqtlSgjVxyFN3zLpVAWQ5brcAmsrIVTYLtzAeM2%2F%2FKUci3cUYOToTilCLucd9d2OIMMH9i8sGOqUBD0sGweHc60C2AeAOkpw9ok9YkTP%2FDI4yK92APofo1jpH%2Fm09Aj61IWt7ONJXTNeUQE98YQnBwDTsGWgvn%2Fr5it8XvCaZdcdnSMHPRpOWCGGIC74PAa%2Fghsb36lnMK%2BWKqNJCF7FEf6qbrFZCWzLO1OMMgfmXXwb%2BqKgx0Qj%2BSwuZikVkE8doQMQ1VBbO0p4sW6LzI6LLHuP5hMJ88mzrOhlVli2T&X-Amz-Signature=c1fa52e56f2c886d9e4d083fdbce3d58daf0624830cf6e41b2360f7d32265f1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

