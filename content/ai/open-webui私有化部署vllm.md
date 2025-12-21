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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ENOVTBW%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T025959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIF6QOL63AFpr6A8oMNTr1wVUQYgOyOHuBmXc5tTsju2bAiEA%2Fmz1ZIxJienSDfqQFyNpOH%2BhPczrSjeGObMAKe%2BZSFkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9lYzWCQdCevSmFRyrcAzBHUQ3GZ%2BwoWzxf%2BKyWlush62sSAwgEYeajeevTxV02sUAUb2shq%2FfhXOSf3uoAX31LKVmigzhNwi%2FAHzR1NzT6Xxq5xYNySjQMalMgk777sBEx240MwmO4CLKGq3mj8ruIDnWX9OdhV8lLiAPcJ7mxkQnMG7aRD3byKoMDuKWCiZrL5PlAi9FuJx4EFblhf7H1dPzQej3Wzw2GIYSk1A9RxqErlvWxoJYNTDukGPal5VYgzM7jlU4YdOzbjo7kPSwvY6uWwgi6T8jFMPI%2Fvk6EGXAUvtRQtPVQ1YVGrhwi2IoDoMOJose4dtXQHkieQsivbQy7278canFFX%2Fi4c9hGUMIWBD5fZVhzroftI0JilbpCt2oySyUhM1eCWewnK8223anRIv39P2%2Bm9ifs8pUxnN2Og%2FNXaffQZi1n%2F%2Bt%2BbeYMq5YTaoJW4uPZAOsrQLh0CbstlsR5okYvefHCBhgXhSvPqH4XaKBq00wP1rlmb15BBbdYgemB4tk8Q6k1GT3Tqs6RPSyCVbaac8cBBBeXAzql%2FddZnY3nrfJ0ewiTlyn5HeFPjmud3gfT1CvIgZFvy%2FEfSiZJWXIu5Jj6c8cZv8ShKnjy4q2ndSvpG7u08QHEVVDztmF1njKcMIb5nMoGOqUBLSx7I2kcngtj6dlxkOb%2FMzETOzBg4M%2Fb0vZKG904x91V3YqnCnNABLkIId9mV3gQ2Q58t%2FCf2By0NtnZAhQdDXoLHtQFwRcVhO%2BcY4wXJL0ysUC%2Fw8zw5RkvElh9YJWceEg8Cy9JvH%2FHryRwGu1XdJgSPkYaWViDxnXWqZ0tcgrfb0uo2vpt13j0nfVkuu5T7ThkAgvFCXpuan7Udxms983W2RAu&X-Amz-Signature=75e6a530339656f07b992951dd086ae52082d3037077c55e102ec44a42bb91cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



