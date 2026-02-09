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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTODLXDV%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFAHNvR9%2FViXNiz%2BdtM3%2FfTe691yoPmFPdwh3NymTfEgAiEA2UAqJeAnc51BcM1NQaOgr4h5GuOcs%2FeeOPtcOmz4zdoqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2GoN62u2MN2joFGyrcA033U8smaqX5ZcJqJrTz3Kd55nHofiovy8e6TCPB4ldbQ%2F%2FSo2LlgDMSnl8W6F4LW8VFKLvEV7RHAr6jE0my9HzZpqIR%2Fon%2B2gt0kS0%2BiJgD8ddEIWSLtx2o1lerm876gmAZ8Yag0ZsFrvifdBpnpXvX6OEv5fNLvNAK1w2WrH1g2EEcs%2BqDft6s4kIpoeLzYho%2FL%2BIML25jPuAJzWKvL6xmdcYV%2BDN9azZudS5IQp2viFRtLwY%2BRkekctxbOLvm%2B0fKubFJ2rYAKJtC0ocNWzNeGXTEhm9c2NAKF2POrlF0p6a7IWH%2Bu5pb1AkNvaiv5qPFfYVYiAencpa14fmQcyR9lK%2BggcN8ARLZfh5SFC0yEYyqf9TVJfj%2BG0WQMKugd9JUpO1P1GyJ3GHCkhl54kcD%2Bd5TgbZPB%2BCAVrZjtwXuVn3oovG5612NEQPhvb3yd1pkbC%2FvYJuGNsaqL00QDfEO5oWyT8f7twwoC88cgT6tPQj7bIsVD8uReAT2w2V67FhkFtlyQax6MFppP1fPRhr9sEdCqANMxyBqtleJCvWv0zQ3Giv8scG%2BEKN%2Bx5adlum5U0I0aumjylbAn11aCPG9DHHsCsXj0kvC3EQuS8rrPx%2FnwwxxLZ78zs8DMOWVpcwGOqUBSoOmElFEf35f451PdIoZe%2FPBl1qH47qbVmJdxxT43ekgBVCKxNqjCXARUg28bGZZ0cNmH1cqpCtXPkPMt5ARQencjIY8tzifNz0QqErzjdF58DeW4I7m3YmzM2AYOvTk%2BwRG4QIfDStsTx8Sao9cOq24j8IJVfYNvRWxtDdzgY7ykl1Bu5%2FXPjLfoFievAA6YxG2aZUt3OqJMqInHfvZikfp59m2&X-Amz-Signature=5924bed4d2a34d717cb7eef9311806b9095648209763f1699893a38d31fb5fd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTODLXDV%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFAHNvR9%2FViXNiz%2BdtM3%2FfTe691yoPmFPdwh3NymTfEgAiEA2UAqJeAnc51BcM1NQaOgr4h5GuOcs%2FeeOPtcOmz4zdoqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2GoN62u2MN2joFGyrcA033U8smaqX5ZcJqJrTz3Kd55nHofiovy8e6TCPB4ldbQ%2F%2FSo2LlgDMSnl8W6F4LW8VFKLvEV7RHAr6jE0my9HzZpqIR%2Fon%2B2gt0kS0%2BiJgD8ddEIWSLtx2o1lerm876gmAZ8Yag0ZsFrvifdBpnpXvX6OEv5fNLvNAK1w2WrH1g2EEcs%2BqDft6s4kIpoeLzYho%2FL%2BIML25jPuAJzWKvL6xmdcYV%2BDN9azZudS5IQp2viFRtLwY%2BRkekctxbOLvm%2B0fKubFJ2rYAKJtC0ocNWzNeGXTEhm9c2NAKF2POrlF0p6a7IWH%2Bu5pb1AkNvaiv5qPFfYVYiAencpa14fmQcyR9lK%2BggcN8ARLZfh5SFC0yEYyqf9TVJfj%2BG0WQMKugd9JUpO1P1GyJ3GHCkhl54kcD%2Bd5TgbZPB%2BCAVrZjtwXuVn3oovG5612NEQPhvb3yd1pkbC%2FvYJuGNsaqL00QDfEO5oWyT8f7twwoC88cgT6tPQj7bIsVD8uReAT2w2V67FhkFtlyQax6MFppP1fPRhr9sEdCqANMxyBqtleJCvWv0zQ3Giv8scG%2BEKN%2Bx5adlum5U0I0aumjylbAn11aCPG9DHHsCsXj0kvC3EQuS8rrPx%2FnwwxxLZ78zs8DMOWVpcwGOqUBSoOmElFEf35f451PdIoZe%2FPBl1qH47qbVmJdxxT43ekgBVCKxNqjCXARUg28bGZZ0cNmH1cqpCtXPkPMt5ARQencjIY8tzifNz0QqErzjdF58DeW4I7m3YmzM2AYOvTk%2BwRG4QIfDStsTx8Sao9cOq24j8IJVfYNvRWxtDdzgY7ykl1Bu5%2FXPjLfoFievAA6YxG2aZUt3OqJMqInHfvZikfp59m2&X-Amz-Signature=b219a8141fb58f4f425c98f7e33290ead26745e8d6c2aea5d796afd483c5099a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



