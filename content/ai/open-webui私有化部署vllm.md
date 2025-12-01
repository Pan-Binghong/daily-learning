---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXROPLBA%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDHmnY0rl7o71aJ8VAaL8EHig09w9TKihvxxkSFPOTUfAIgLFTFaK3e7%2Budo2Y4mB%2BU8xvowvwPZpepGaVEc7T9Z%2FwqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFJi6AcM0oPOyamTpyrcA%2Fcdf0QgBzV4ZWtIiOjRyIQyWxe1JM7B7e93fmWMv3o1E3SLNuAbpl7npuv%2F8ZhkEDadf5EQOs%2B%2BT%2F6O%2BhmJ%2FqlIq8VkVpZ22kUoRnEsoFr4tiPSsiUcGnH7egLbPw2ZG0AYl9cMO2iFggXvGAKyJoU5nnDc0bmtFfDlxJIAC7Hk1fRb%2FbVFxdrjiBCj8X3O7CrWVKBIDebPMWK4Kt6e0Zby0vLjOjeDkaeuywplmAIBkxqMjod3oeSxa4uEZ4QL5N3eR1InfXGOjGkEKm4auVy5jfOhkcttEgYFedD1gwqEDeobLUzyxH%2FEkRa35k0J%2BlW9NApjQwAvuNZ7ODUKV2GfIhJ81rJ8yzDKdRuKVuARzmQDkRw7%2B6G3Vm8F3fgFbrnn1Z2vJDAwahb2Ig%2FBphaRgx03Pu07P9%2FHF9AYG6A0QvhRlW%2F25lI32p2dn0IA3Sn1YFAyru6VQO3ouxaeh%2BmRSfQVl4dtRbFiY3ShtoN4X7Slj13aDOEXhnoZcu%2Bu53dNavVfVmDZ%2BHp4wQMYRj2R9aud%2FaprS%2BpNbQvJs2IrHI2Q15op42SCLexVH5%2FpJDAOZeX3a2x9aUcTZwrVAezKYg8fTi0HrcyGpDo637GshXnNKamo8GIjpHfsMM71s8kGOqUB27nz%2FsFVZO9oDyZOCtOGAqD57xEL1lbkeGIaGkZah4M%2BCCdHFZnbikNOdOokq48mWRBUNyACpSTFPr99rcN34Sev0qmHv5KSYR9eyHMKMJmVSdRKejbawGknxJ289%2FcsqwbzEaUC%2Fc9LChhdlFW29d2Hlb0IN7XFZzsTBrXJMPxnI81UL820vgpLskyZo0Ox6k2ofWfxmDaD5iQVRcdUIpeKT1r6&X-Amz-Signature=56ca75e7f50d2787018f1ec08319ca11362766e96bc569067d217b2914160296&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



