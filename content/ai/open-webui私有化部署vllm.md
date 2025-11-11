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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAQEXQBQ%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDZhF6sXjMi6iuk%2BMMMK1C%2BDBTBJ8ag0iLLf5HqUUJLhgIgO2ZgJIjFDTK77q5rj2HuWF9ReemJ9Hk2VOIe6bJlNs0q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDGqkcBJHAbX2FvKPrircA671aNnKRtA5TWvLwReAL9F5nkO%2Fb8iuXQUBhLYmPvJiuOJJxRDQrW3sh%2BvMb1N%2FzcoZCCgM5acRiMRid3tKK3Nsb4D1oX7Nze%2FYPNiTk3DuRUXcPQyyJPlzTXUw1Vv0iCVB8QkCBQSJKCsBg%2B5ftZdGYLZHeGDYY9%2FvskLhfrVP7u5rrAEA8qYXG5FWwAqTxUmQcvEXPRw0uNI6bjvi4Twy9yQq1xMVN1ujJo5cm%2BwWt7m49eAexZJlwNgnHyJrGxJthQKdCeNl5%2BYcR8qAfcsxLtjQNEozgp0hV8STpdxHgOA8pDP87MUU3HEU0%2BtUbNo%2F7AeG50nAtdEZIlC%2B7SOFhnT0BQJTxmYouyxp5Cvuyc7%2BgBu2ckXj0umIUinA%2Fovkcrx5wGea0qqI8RMyJWuQXt0y7A8F5VhLRD7KslJFCbjE3J2s2zHDhWO2aO4f720OkwzkMcHPi%2FNiu1Z4HWo75b4DL8Y7ozc0SQq09DCmIXab5uE5zt2mQjb5CajrcKPRwRbwq3qUrCo2lfUR0kINKmD4E0xdWZ%2B%2Fhz6chUnqwY%2FpDULHDjYaD1%2FD0I0yGle0ylJJgyU5IM4LCBr8YnSRIH7wRuAYr4Hni1EFUknuuh681I4JragX2ntxMMq%2BysgGOqUB8VY%2Bba4hbzBIjtCL3Dvu2%2FNaeF5gN058%2B5fYP6UJpCV1FTDaGMzLTFhmIK8acvZ4m7mdOZXFytvnJLgOoOInTyGttIINWtjrJVzuvsUnj7TzGa9N%2Fqi%2FdLgfAmQG9hiNF0AUbVDimNCakvJBMlPWbFJhYOInDhh5A5aU9dDgUmkIXeXp3X2Eo%2FNesFt5vWOgU7ea5s25QYQYf4jJdD%2Bc69kxn3QB&X-Amz-Signature=1ed79d0350cff7403012a4078cd09dd2f9a9b4fdece8fdafea6f3f8c94a45940&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



