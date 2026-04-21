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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAXWHAWR%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCqB5IzDQSS68uGLS4axBh6gb%2Bq327SDOLJNinzv1GjcAIgOkql8LmHKh0gRMwdK4v7MgnfWnEUBmg7u35Iaoydtucq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDBZmQ5uQtU4q%2FH4d0ircAxd65%2FRURl9%2BLvi3MjUkdGEBuHVvtLkckAiddnTWHr1PgBynZaRnGLCMF1%2FWi2POca2pt3tzI5xzs8%2F8X%2FgJBK%2BH7iqgwcTsHlwRxOSFxRvPBknr3M3XISHwWlqicvt4AXOeyYK58X943KODqF2yRfwejM%2FID4TYSNsToQRa%2BHh5jidKsb3udeFt2PIxEYWvRFAEiWc4zOvmBVovMp0pr8hWNi9j%2Br50SPLk%2FcPxFPA%2F1iUpvOTxR3B%2FkFsG8A2NviNHL7wig7%2F%2F9hryQjrxzf%2Fc60y6n35MZPSyxVvjWJSTh0u93CR6K1oQnt5pXbwOm9RBWDB%2FolzHwI73YFYESTyf42PKqw%2BqVbOljJmdyLAvW4Kep%2Bwkt0o%2BckUOszFU73B7RX0GCssmd1HxYa%2BOYNjIihvnusV7vMt4EuotTV8odd3AN6k61G%2F13DJ9YO8tZ87Xqw0SGG8Syc1pY6WuNIc3sw%2Br1fQcfuibePoEOXnbIMyo9uxjA0KSBXymJlmmLbeF2h246Glux3R1%2F6SzIWnzz0Zh6cNVmUAUr1U%2BsfLuNg15boo441fb83YG%2BR0xamRqZvKOy%2FSSmPUSIgwEsCOt4Y8H10MhJYSlxQERDBn2SBe%2B%2FQaR8bh6WHEPMKHUm88GOqUBtxNXIrwymz%2FdQziopsYne8853jHdn5gbXuSIiHiLtJ3jwV4%2FFO4D0OKJLu%2FgteFkkdFsECpP0zkF0WKQXTN0BV31%2BNgope1z9x4%2B2vV%2BMISFCAkCADMUQtIqQIJirpul2BrC%2FF%2Bw7bqUxbKsS2B3E9%2FJ34tP46eO2MKbbSUVdxbdkWfyNDUzIV%2FO6c985s814bnN2RiWkQ1CtsCvI9BlvXmPu1go&X-Amz-Signature=c6a4208d9660c59e9718aeac3465a828ce6fdbde8a76a62f423d0650d5f87cb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



