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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKTSPAGZ%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBogd87tF3AlXB4ROLBQHqv9c0Rv17fGZzfK%2FKcXHArjAiEArkzVejY3Wn2rE6qwgELD82nH56OJ5V67D7ydUgjnZ6kqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOMCCI8ZbbV7NTu1SrcA2CAlL2eUZ%2FP%2BW3vSaaa1aR78AcIWXmGH2dH4XzbgU6wlwsKQuZjyhUmQBpDGQDmFjq%2FRuQLTm%2FJMTtH3ocijBke4c2Liv8iFoYphGVgR84e3ZUcikX8%2F21k3rnxqP2EkRncuenE4s%2BJUylDWD4GkSKbr6%2FutnjU2a2iOQG%2FXJ%2FcUte05Inkzu8QD7kiACZ1MXUghbQFF4Vuoh3wiFSJ4XUpbewVi1B5pouMwlGvAJGz5guxvgDj%2Fcu9mBPDG0tu4mzi6EUoEeaW39X%2FFsGUjDtEoBAuuMvlsUZBeLT9EZJFxkFVuFp7HD29Cqoh%2BBUIPt0%2FS5zqGOHr1tlJjuRluwA9EkbPNPnRD5b71tSRmfclQZudxsQNH6mIn0bSlZJCmRJfBwNBxyC4Y9P7Bb9wBnbyWGLwlA3czWLU6c3YTxD5B6IctGKH8grY2wd%2FYGPb4wqWzSOQ3waLNyTDd%2FyApWt1BK15mKy8e9RiB%2Ba6dggndc7Rm4gSYThHNqgrCv3EEZflvud1SYAo4AJyrZw0XKOBGy8xPPMrqwPWuCcDA19MEtEOqWzXWncALpebvTwrdVtrFa3krMJIAt9OyKvS1rV6k1sI%2Fgi2z1J8GH2tqJu1g%2BUW4IsUCkuPaR3kMNDn4s0GOqUB1pj3vcjEkfCBbhtiybZvp4H%2BfALJTHMDcbC%2FZ61s5hJI8LxgIEGTXwRMpGliKWVXKB0ugqoH5U6UucRFX8cpo8TWCci8CI6ZjHias3kwu8H3fGn03%2BXwncl0iWc7aD8mtBCgjIoDWsQxlyQrHT6UjZqK%2BsvafAGhqUqrhZ5BRGSJ1CoJWtZionc477IL1BFz7F8PE8ZKR6jbUxvAtB42q%2BXxWd7X&X-Amz-Signature=83533f0ef333e3f5b4c5215cc52db73e4695b6c5c6f07c74d83cfb6d896bf444&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



