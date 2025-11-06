---
title: EvalScope大模型验评框架
date: '2025-03-28T01:13:00.000Z'
lastmod: '2025-04-21T02:58:00.000Z'
draft: false
tags:
- LLMs
- Eval
categories:
- AI
---

> 💡 之前都是使用vllm或者sglang官方提供的benchmark脚本，现在尝试更换为EvalScope框架。记录使用该框架对速度进行基准测试全流程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWWOVGAM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2FzwI1xU9e1DSEezkzjpCr70JKM56Wv7jt5SA%2FK5PZqAiEAu3c33bnLev3R0F%2FfTD%2FAO952JsBh%2FAnVEjfYcHwcwYsqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJHrGyrUqHXOTcUc0ircA1o7povS0X9SrB7auZLErfcIUBRQEOy0BzfZZhdTHTZiSXtaD68irjD%2Bn%2Bb9i9VuK0HezmU3FQ9OzW4LcUbK0PsgA4Z7i0PqetTA6UlAF8xXiG4BbVtt2iXUK7sXGkrooa271NqwF632KJ2IWglC0JZPvJeYjnZM%2BnkJJ4xvngUyBf8PEB89lxKR3vjZ7eKqxeAQIh1mD5MBNIBI7G6ogDxcKOHoYh0ueYpYJAcE%2FJAjGw%2Fe5FD5ueHBKC3rRCWZLcdteOhPvH5402TuOmc73D6rSPXymyzuSp4%2FuvDKAk%2FAAkG2sJ4xqqWP2Zo31GXJxlt8ugk2ltTuNIo9lrOzokwSatCXuKqMc1x6sRycvzQZ8RF2yuEO3TfKpc0w0O5E4tqvV0RCQJRQHon5D0XTi7KjMXFBOC44fx8DOcDLQP2kRPG4Sq1lX4v24GkisG%2Bffkk%2BXbtlGTcEwb3wOw%2BqER6sclNEKNHo5sTYg9kx9K8MepJN%2FEyxg1wF5K3xCKZWo2tZOe5ycjxXHe0%2BNOwVpr2y2KYaUz2bxP8fD4o4tHtoOqjL9R%2BhAZG35%2FKKORCSOvISjRilgpu8Z5nqTB6tjD4kOflh8ZawLfLcD1F1CPSmsovjHAxT7bgSdPpoMOXwr8gGOqUBxjYJjY5mKoDOpcMY1tChhCmTPn8fS1BaZ%2BiTiM%2BASxcSHIfHyImBTNzkDIeokTUN2kpXbXIIZ%2FoCyzR4A89T6h%2BNsVJgM6V%2BejCh%2Fb3RuL7Y1eWdezc48%2Bg%2BZGzGgIVLhwuEulErtajozo8K3C94qD45eduA1mmqwPiiyp8R5OnQlWf66EfJ3VnHAhpY8aFZHkBpgZQJ9JUZoxfIq%2Fuzn5NKZLO7&X-Amz-Signature=099b3f7ac879b24ec4de54c683295f1cc16137539d7e9ee2ee4c0b2e3849084a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 1. 安装

官方提供3种安装方式，1.pip/2.source code/3.docker。

## Pip安装

1. 更新pip
1. pip安装
---

## 源码安装 | 推荐

1. 下载代码
1. 编译
---

## Docker安装

https://modelscope.cn/docs/intro/environment-setup#%E6%9C%80%E6%96%B0%E9%95%9C%E5%83%8F

1. 拉取镜像
1. 创建容器
---

# 2. 运行模型推理性能压测

参数详细说明：https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/parameters.html 

推理性能测试有2种策略，第一种为标准的并发压力测试，第二种为单并发下的速度测试。在该框架下，特别说明了如果需要使用速度测试，则url需要设置为/v1/completions。https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/speed_benchmark.html

## 命令行方式启动

```bash
# eval.sh
CUDA_VISIBLE_DEVICES=0,1,2,3 \
evalscope perf \
--parallel 20 \
--model /data/DeepSeek-R1-Distill-Llama-70B \
--url http://127.0.0.1:8000/v1/chat/completions \
--port 8000 \
--api local_vllm \
--dataset random \
--max-tokens 640 \
--prefix-length 64 \
--min-prompt-length 32 \
--max-prompt-length 64 \
--number 100 \
--tokenizer-path /data/DeepSeek-R1-Distill-Llama-70B \
--stream \

# 为了截图，暂先取消设置该参数
#--debug 
```

<details><summary>测试长截图</summary>

</details>

---

# 3. 可视化

1. 安装wandb依赖包
1. 注册 + 获取密钥
1. 运行命令后追加
1. 结果展示
<details><summary>截图</summary>

</details>

---

# 4. 测评模型能力

1. 首先将模型启动，使用vllm框架进行启动：vllm serve /data/DeepSeek-R1-Distill-Qwen-7B --tensor-parallel-size 2
1. 运行以上命令后，会在当前目录下输出一个output文件夹，其中保存着日志文件。可以将日志路径保存。
1. 终端输入：
1. 访问本地的7860端口：
---

> References



