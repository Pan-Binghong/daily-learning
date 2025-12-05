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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMIRJTYJ%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FninqUwuc6gJzoV2FUvnpM0d1JphAQRk5o%2BFiVWTr7wIhALloSkGwkCYTNIsmNNZ53BIjb09k437HlSC3ojNii0lUKv8DCE8QABoMNjM3NDIzMTgzODA1IgzYjQffCi7n3PkRodkq3AO4Ppqt5pRnAAoNV7F5xHAWfdfH45%2FueRCgBc%2FKx7lOjnAj24KcFOflbKvfc3Ue0VdUGJ3B5gFBay1rzbx22tJe2e2Rsgr92aRg%2FBM8IQaIWievJyqIdOLSjZ1enU0vnymOcMcDAFXIW969Tb%2BKNICzi%2FoI6GXBoLlXrAZ3dPIBKQgJ5Jz1%2BeP3fpUhWU4bGPvPILnv00Us3dAhfoPPd0y9A6vOpx1YsxnQpelYbZFPYc6oizO0xZiFqurALpjE0odd%2F2faL%2BunGPKUCezN7kB4FDvBJAmiXckHSt5V0FyueF4VpBjGzFXwKVrjpweECaUkruSyObVMBMc8KYtLh6hjSDhq6X43VkYR7%2BmNkMrURq9l0CPQ0UNVh27O0W6y7N7eNpx84zOjp5%2B3JaiUMNP%2FzYJD1q4Z4S4vCc5PC9R7HI2HuIPYunV7eOkn1T%2FhLpy4Sgp0UeR%2FQ%2Fkcu2SWX2NPhkodlkB0RKHkKbPPU9AJpeeX1XNXbhNJVNxMkgXT31wX2Lq6i5s8gYQmjc2ao1ThzkMb%2B7qLwuNF1L40F3rTvB1TcCYzWPFEAikfTP1NONuKVMcXTDEPVJajs9ciQR%2FDePS1Akw%2FWFA29px0%2B95SPLXR5kApW3uZPdEWoDDdjMjJBjqkAS2OGljs4%2BWHfTHhVI5Fp6VjKNYuOZY4P4M3BtzNQvbO6fl2%2FWy7Hcg5ru1v6tvFaV3vrFRn9eNepdiAy%2BnRr6%2FtLC7t8ziEF0DV7r0TLvJJ8hO26G5KJboRGcmC8%2Bh4kTUU90zDRfWWZds6cjn1wyHu8dn48RXAhx30%2Fry8jIU1ENS%2F3KB0IwV9p%2B7S7fxuZiqJ7hPaGTjL%2B4h6DW%2Fzq4WYLjzE&X-Amz-Signature=85e5aa4effe1d7714a13b5513349d3c283a887bdbf557e67a0f2d8f598cbc6a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



