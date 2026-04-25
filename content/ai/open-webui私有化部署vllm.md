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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466673DJXC5%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFN%2F%2FTB152taSB0hX2vOFyBk5AoQtviU9oaBo9jrCdeSAh9SusxqLyRX349GfB69Sb5uyu7oOQvbs2LxcSy7pyJ7KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzdFH3jhDIQ4Jijj0q3AMBs4IKFNIU0Tk30T1sQtEhtUaThIUL%2FJTIqWxZAYY3XhdBQey%2BdYp9jqigbnFUQEEQYfFdU%2BSMo0X5%2FPDErEmNs7kna4EpcfBIngUXrHi0AcVFUnKk6Ei%2Bgyjjux7Eh8n5hhW56Ux99BbkmZIeH0r%2Fj9H%2FVU2lQxxzghJNoCO4ViLg67Q%2BLukm6%2FrwGunM%2Fr9TJ6e2d9%2Fle3oAe%2FGjxQXEUrY52wZ8p61AUnh5Xfakurw0LlWGuyzlLHRgxk%2FhecgqeVIGVC3%2BDFZzXaazwj42chyJ5HUkll%2Ba37q2Yr%2Byj3K8ZTxFpiSQQB8Zzpi%2BmSS2w1h%2BehVq9UsGU402eSOGGjZ0R%2F2Ig2ehaJ8jDJj3xAQLkqwvPRtBx0Ep%2FNLFIZLpwKw45ry7c97he%2BoLqpvqXowsFhD0kayTMvcpp6iXhi5vRsfX3Azv0BFbopSDffFUnUv7EikM31LyUZCBlQBwxCVHX4nOdIHtL%2F6%2F%2FZs%2FAbiEeafynhgiNkojsqvbtjsJ4aGIB5VmX9B%2BEWhNrHm0mA7WRv2VGrHR5Ij3N9ffyqdOYTuf6DRncgnAPh6DJfquBBGS5MKs%2Fqg1KzrzprcDkUzVU3J5tQ4phtJAHcNUoZD5XyruB17vQOMpfDCx8rDPBjqnAZfHjTDJhw%2FDbkvErJAZQ4U2xeT%2B1NKa1ieRfmNpVr0ud9RIT70juINel9lyNv9aHA%2BM0j2Jft244rknNJjBEHWPdP1KRK4Z7qznQBY79hLHEx1Xnyfxo4ZTKiK24W4dvssdeOEBoikeI%2FrPTgTgKZDBuIKQ9ZaRnoJU%2F6BWaW6uYcs%2BtjqtUJn7GqMPZ%2FnNLuQC2emiXk8Xn9UJNDb%2FD7qa4shw%2Bgjq&X-Amz-Signature=e228e91cdfd6a9fca18ebea8e3975bf56905edc42511da0ba70d0c005e0bbabe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



