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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WNCGNT2%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm311TJ4o9mla2PTstQgX8hKhuvR7fU0Y20SFcpRhtOAIgMR6T0QYdk%2BKCxJZW%2Bo2xRfNca8VvnYNtlpg2K3ifrwsq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDE4dE5bMaIt0BvqEtyrcAxc9s9c0UmxPDWq1%2FAuh5SYZXmeHRXfCM4237c23NKMSk8laMfDGf1DXzLTBQ%2FdUcLnX4%2BLFSezdlH9%2BOMwCJFUo5XINoxwp0e6oj0SeswkwKe%2B3NGdlo0RsgBRef1l6pqd%2BC3Gqm8f3bCMdaBaTxkfPaPOC0vxQE37Eg2WJpH54t1nMjOYrzMAXz7CwBxePEk24VAbT1aYE2%2FUy4288U04FEWvp7tz3YspRSu%2FrXO4EwNM6ogaiknoQVpX3yoapgOp%2FLSTeQzfFXVg4HFsknmGgG2uxC0rUNdafgcLRcgHrPJb7RfU8WqFz7zW4LLTd2zw%2BOrsqnxx0vj6xiTwhZ8uLoYdePozVbMqHx8uO%2F0EVAlZYbOpnTEJU0KTEGN5BlxLyduQ5r7rdkoBwTEPtsUZhr1JxkjfefZLuRJyOH53Gqx%2BuZoyYc1QJA98h3AdITwLT9tXGEeByUG7F85vOEGtpcuLehK2KXdG%2BmHZwft1fmJ99c%2F7RO6z2uX1WPAlrRdEfI12LWkG0IYNSpS0IevdZkztoPB9CJkKPkl0DGiBFGvrghPXsejubGVjuo3SdWD2d0RqiEl7Bjs%2Bkgj9IDILt2gTpxXHDOpU0COIjdnN8Wdx7OHq%2FpL81%2BOmeMP2tlMkGOqUBJKN9pb3w9h3ocbUJYfB6pxjmMEVZhCSacar76rcno4S3K2dZrPkgfy0MlSHZRI73llWmC%2Frcblz%2BD0dwKPRnvQJ9%2Bp%2BzQPBDNMtz3LhpRja8eHK4VnWJQ0ZsBwHPNo3rzvbG8vLkv3Bhs%2FBNuD%2FVy%2BOaF0Ct%2FlS7dWPBxMdBp3eTceEz54HLW%2F7XzHdjqGr9r%2FktQ6Mle06J3oDm8BH%2B0SP6Wowl&X-Amz-Signature=fd9fecedafd7fe0f2be404c11b92845d69e6ab57cf850ba7fa14f404e26c8c00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



