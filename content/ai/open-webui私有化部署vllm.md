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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URUPPSLY%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDIn86%2BmpJGAhXNIYHvSkabIScMay4WHokXIoGEyxfYAIgP8OtSDLCZSizKVV3ixrN%2BiSXflFgIwh%2FBQLt4PAGg3oq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDChqGiKXtrWiXDC4BSrcA4uAHwudUe%2BxhBt8FoG7z5Iktf6iVYjdvI7Gte7d28nTadba4uFaFdMDnT22WsyGduH9h5a2iQLfINPwiwB9xZVYFfd%2FMkRSmhiHstIM%2F%2FDk75cRR2uRbzXZFq0G6%2FbmbXiF7DJ4Xiof%2FjqQXkkE6iRmz%2FmofCKTrKoBpC7lIFV6FBezmuBVvjc1tCdnuXh%2BBSRlngCmofsoDgnrqMeZsfm7TrUSE5SuNsd9kjouFsX6T3Nk7Edmu1y8dmYYL9lQ8ZCy3I7gsMG4WzS6GqlAbJJ0ixb4hlI0tYE2%2BzHbrTMawqjSMpsNE%2Bn6LjE6quxCYwWFsH55K%2FY5Xnjx8i2vTr%2BrIcAxFdK%2Bbel1WJFheT3L9BgWNqf%2B5Bvr0tvMwz5inqA%2BdFkcMPVXZHQWXHFM0KMGRHoAkcUnEvKtmxC0NTtL2zg4tloB%2B7JGL6iNuQk860XTV3Yili6%2FALSM5t7Gh0pspebrzfSFiN4kEq7%2BQeqQL4caRojMN0enfMcMWMR99pxmeBtxT%2BeM8Ya7hNkK01iDdhcX1MedHfftw3DpvfyZODnk%2Bxm03%2F9hW2H66Rs5%2BwNb%2BUYy%2BVrHyqqv8Z0mLp6VTSMx2WPNKQfWjpYVvYUAxr%2FqvciS5Ss9%2By9GMIX%2Bk80GOqUBGjaI4WRuhOCOUiog5UMe2Yo22d9308I9lf6hC8Qb%2BTs4fVVA0YSZJvRi9QweGgqbSIIDoCgDe3T%2FA9ViHq9jV76esxPNWAF1OewzE79D7goNHgPQ%2BespK3yEMY64Nbn1LmykiqdzSoIg7ZOnl0m5SDW5OXnjv6fAc0Q6sL7EQwuLWHgAnK5RrDDr9YuTGI9ZZ5%2BVGtRINl57WEWbYbJ88biem664&X-Amz-Signature=478b97e6316379a960fdc82e39999e172422c78e941088f871d21d7faea81baa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



