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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCQIYOY4%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcPPELa%2FABjoG33ZGwxuyN4lc%2FN3b1VNPVFt7mE7MjdgIgKpisJTuHvR3NgjgV5LnULYRbPSQBpkYb%2BtAKhRNFPr0q%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDGLBSZJ6JDvzdy%2FJ5CrcA1Fl75gJb99lvrY%2BmRoe2n0iHn3fhKpYnQ%2BdHOn7lOiF0xjwfVwt685IeqaSW%2BEnen%2FsMVHhYgHHwuT7YYgn5l0X4zMHUkYz4yA54s7fJ5rs0y%2FySJmFpmncKd4jCYfUcc9COlA28qh%2BR9OiV7%2B22bUMC0THYOl9%2BssyF03FAVrl%2F4lbWRwKR5SVPp78cE%2BW1GQFgDCcBY8unK3%2FLqnOwh48%2B4E5nZQyiZRQzBc3OzNYL%2BgqgU8uwZiwxWoZdO8HR4o26%2FLSfw0Ka%2FwKWnI2HNV%2B8eWeAHGA10tA6u%2FVd0fiMuYjl8XKf%2FFeIsI4xraW8MN04Kz3EnPMxqyLgTedrleNM5EhazxsZ4tna5XhGv6zLG5k%2B6%2B95u%2Bj5t9Fyt3GDFFB%2FH%2B6XUxN%2B7agrGnWN8onf2Bu4UYNEEwnpaiYnwsTugliUr1mXeGQ%2BUmyZMI7QzTfI8ucl67hVhauIUlGa7Yws3Cv%2Bkt3jbi57kIAfvnkCjHk4ghaxhr8g7UzNRUeRU6%2BoHM9j1MB5%2FGKJ1FMbpsrAXd1nvIj6ZZ04UO2jZ1hQGP2WuRnqcjsUR0DFSNKOPaSVSVlCECJ32QI3dxncR%2BmoZvr6skTlCIY34UHaDxyH%2BLmKtbd1tWcQ61uMPeW5csGOqUBdYrq9FUdvmauJ3Qml2idfy3md39va9Y5iK5tBJW5DsV4WGcyGMcjP5c91gt5YDSWm84TZ4Ff1u1A7HBwbwrweOzFpKN7r0y6jNPofC1UpvlS7nDYaSWfpYHZ%2FgGYcm7i5%2BRjo8lhG3NrC7OlLIiM7%2BC2AFI0u28lOU1qYVEZBCQHjoCOTuYhKSaMKW4p6dCcOum5CwHGMadWNp2%2B9Tif59HXdn9e&X-Amz-Signature=5e06601181487e8a46394f4755255cdc16e4b032405dfdbfe1e7ee1dda36600b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



