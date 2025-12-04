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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ME7A6IX%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIBh9HEmSrM8khjsX%2BKIUNv4Jz5WJ0roZ%2FnzJnw4aq1tEAiA0z4Gzvxq9z8ol2aTE6%2BLB0uUcDtFx%2FCg46rGg%2FozwECr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMCsnxWQbxihzOyylFKtwDuDzkse3v4ikdT3lUjAu15Zr7D4IkkC3OnYROJxh%2BAA2NQi%2FNrxRbPd1wgsvFfirScDvz%2FP68dadXFq9AgTu2%2B4JGoqc8nWwQS%2BrW2uN3vlQj10BKCdnC7m93IZrSMzW3%2BtUPC0nPJDiWpa%2ByRCGM3nzjL2VqJ7g%2BUz5LE1NfTT7Y9u7I3XNQ94MXrWph1iwpFg6shHPeGsF0MXZARt%2Bxq6cipo8LFL7LSJ%2FysnF8pNNrfd2wRdBvJglq2ka2A6WnBrNAXcwrbEZGKWOZJmWbaT%2FXoq1pbZI52ZHmeBVahYlHES1K6007sGvhCuxDMg%2BATZqtp8UlHtdhWvkYsfWR8WCnX9Ch82R%2F6ioG4DuvXIw2YlW5yd3UVmiBy92j6OmM9eRs60J3HauhiaQC%2FCCC9GPm3ETUeBiG%2FbmB4PzLaIkPlqR7YWT48BCLZltYPk0kuLcGiKxx6O0D1%2FoqxfE35Tan4XrO%2FYEaGIbOhH7sHuVJY%2BjNhOTM8vepmCS4lbibvUEcBohmq%2BuwVVhJXKu7LZJWEpor7jfVlC9IKVU5bDPE%2BdVjnuSFwNUMNakHzdjxLRdzgjG1AHLeYMP%2BcMmuj5WSob0rRfP1VO%2F91xNjtolhcEA4gqtm%2BY9AIxQw%2FNTDyQY6pgHM9oPTfq%2FCoH%2FwQo2vhGRtmZia10Asb7D8m3gmoKhvu4fNtcmglOAG4ET6pcZ3h4NOr5%2BJD0%2BcReRikBANjXL85%2F2JaCiRulTcloPs%2BNNkHsq2qNCpXRkW99574xNbGuHB6oDRGPLVVcDFSyk5LMh9AIbrVvMt%2Bv5jwdho7dIHgnVbxMxJLVDCihWt3QdkSooydIMQbOM45Fp40mlIstTh8vUOy%2Foe&X-Amz-Signature=c29092ad532d7260a15d7e6d18ff223727a70d874da2fe4733319ef7b0fbc24d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



