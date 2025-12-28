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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GVSAPVC%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPBqWrFahWRbn%2FICffLGJrrWaKzYPshN3mwruwUKtKZgIhAJ11msfEE1MfKtY6w10SjnHperlxsLxRp08pzt0d1H8yKv8DCHkQABoMNjM3NDIzMTgzODA1IgwtieyH9hkTdQMa%2Fq8q3AOH8k18Qcgb166gilYm4rPrFmPQYxGfc9sqa9xV%2BwR4Bq1HYqgZ7Mq%2F%2BZ9YEJL4ZORPI9GLNlu8k2uREk%2BH8s%2BRQLJOBJErNb2C9tYdc0mpbSgMEcKbIuWX8jKp0SEKktFSwL%2BTbomne%2BZGxRS%2BOB%2FIdcKFjqQdQl5fF7L5GHRMcKqBCwBGnNWcQ25fvW97ChTD%2BuD%2Fu29tGifxVekpVEcDJilC8CytX8%2FAWTsNc496U4gts3rOoQ9rUx0CNO9GeEtj23jzEWwWqmkov0%2BJLo0DdhXVils2d3hfJmin1tOc0ihVJ71O6vNZIi0n%2Bi3YAkkcAjZ08c3Otjhwt%2BrM5MynT%2BVBCbjmtNMSRnngIZI%2FjTIQIfSkPdhASTjY9DvpQNp4z0nu4kEwfjJ%2FQgmVRVUoH8DWXhg61vM6QjqmDHMh7DnVNhd%2BIL2x7WwAaSJgfqWVrxNj8i%2BayF1zhwKMy9x9NpuhhT1jWlKdTFgpeylqbFCRlDc1fifUe7OPyEmbCZWFOuU9rvNvmCRDmEsOTbvTdm2VLUdQ4%2FEnQF8Wp%2FKR%2FbVDh3WNd5kIiZEkuOcXvC656dlbyTaHXXRuqxq8dIaJE4GM3B2sdMtjsYkCQ3YhulMCcQhqUTyMJ7i6xDC%2F48HKBjqkASGzpfJ0lhgo6TClev1KfrpmhpCj0WFaCDY%2FYtzbTDvNazbpPRLO1Icz9JdhCiJosIqoLqoILtUZeXbkBMgCCyDZgHWFU5pvPsgWEO4QiykvorllleLzFwC9VV1q7irRR8EHTRr4T117IzVL3cQ26AXQKyQCKISGKq7kY7jnXvbWM8MRq2GTHGV6n%2FasHkT2EHPFFSUpRVDl693pSpH6THMkBDxY&X-Amz-Signature=1a650132c4a81aaf32eda44105ddcfc16e64f159d2cbfb908b4bdb7ce8d62be6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



