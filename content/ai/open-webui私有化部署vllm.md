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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCWP3Z23%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGc5NzzrhSe1tlvb1jxvGEqrnhUyPMzwMW90JZThji2AiA9kOwq0rs7B5zNUq%2B9%2BHcFNlkCEKZ7IGB%2Fm5eGof3k8Cr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMexxS9IABdz0gqhuLKtwDTyMdFCJpYcungo8i8EUPgA510e8Ebr4tAPegDZ8K7L0vn7tUn0GVDXp%2BcQwrGbKrB6uA%2FXNY3JBrvw9xa%2Fkd2bMQShKMg0U4Pl%2BSSYPE4Pf7los2DGkAkcM%2FQ1OhYgG5Qr1JtYkw3GW2K0oY42JKoDwipVccTiEgKaLa5ASP3x6ovY8%2BZEATuY53jLVv81Ujtti93c4diqS9H%2FB7dkOvflJK13nhW96uiVHA3BkXzR8%2BzL5qz%2Fsj3gE8JTg1AnqQEgwJL5%2F9c%2F%2BxeNU39tPhKKWiq24Na7hNEZDPk19phle%2FVaBkdO259pB35DFl4fJ%2BU%2FmmIRzToOBiqg7fMdAxrEpJlNUwvjw2sPHVtTZFaINzb1bb185iww89DCJMroP9jRSZzcrFWfRocYr2FzPUSAZ%2BPEyXBBfSw%2BNgmvMjl7cBT%2F1YCPDJk5yT5bUiQmtCEoDoYDf3bYaV9ojnrkZB4F2Denex6xfmeawbBN4mhlxcVYIrG1dzcK6iRk62Jsnzw1CJ8f5vYHnp6JvlXF9lhjADlIDpgHFcJIuyXjjsiffi7nPgD0ZKR%2FRGpwzqZTqbBeZHleBMiPoUcQWsdk%2Fd9Z9IcrfH5Q0dRtGOvuAi9vKkbX7%2B%2BuRXCq7xi8kwt6fOyQY6pgEgEyp7lc3KxXafMp5MnrFWC%2F4jonYUibo1H6AUSUWALXppFI97%2FEOVIs0GEaqvQ0Hffyk7%2FNCnR0LDA8SNJGPAK8fdzJvnOXKOAWSnQgGJso8pGpksyEddyKd6gM7f6GUAMHmWb6h0ZjQXnyvrosYVJyxpKBL1kg%2BUH3tYxf01Sd6TbqxAsoLznfh5q2ngjHxRz3IgBWydIo2HOaqmv0Yod%2F6iHIct&X-Amz-Signature=0a5b6bfd5d75241a03dc15644d222f333f431b4b70a777531c457d8c2e16af8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



