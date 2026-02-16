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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLMEMLSB%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQDMCYYqnGdGdW4dgDuG8aaGwGxfg1BHgLg03Kj5P1v0bwIgDpTYOK4MkOTbQlOYj2Qw8PYLup0CQmwSUp8qmYLz9Ysq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDM0raxZtuZyMOBajlCrcAzhC%2BuaIBRPxqA7qGL3n3GtAKR%2FQtnLorfhR6nN4kKDxSNfNGlLzkJXnnahi9qlw5WtcuGiyLQJe6Bkcq5bP3dephoU49kCaiQ52zQYFQWNFcZBvm7%2Fv2M%2BW%2B%2FEgiZ9r%2BCmXzMhViQLQZUZbAlvo6HA6jXIO9WPMgkxNi8qw%2F2eoEDKg2lLmE1yfoO5wht5X5Vr%2BJXJas25Iz3fb7RiaaQ%2B%2FDNqBDJKxucqjuGobj%2Feb79uRknEU7z0bOe5mS2VKa8%2B%2Bn4Y68EQUSuYPQ7kxd0FjH9BweHuFqSQ%2BaWpvEdYoJvKmkgqaTvlbfwn0qAiDafJYDdUxZuJQ6cOJKrtBLpMAE8TW0gu9615MUAMw8Df%2FrCKVbtUCii0r9WiS7PTg5JvrirJQfiHFlDMYJPvXWrmRhpNLL4srWiXu08mrTtweMpNfzBEdGuV3V7SHffs35adLSLAUc6Vuqrc32OcFiIymEpeT1R8ZTet9ixl8Zo6BrXEXvQGvfS8IY3sGUtcT4DGuqB0%2BVhP5nIw1X1pByPd7SRt5H%2BvfpwT4wNedaJ0BEUBsRcEpBzYDFhb5Hcfz%2BIrDlG49DdS9%2BCSE7%2F8sit4CidnDEwFwa9X7QJMdCJo2tc3Q7uwtfFkeBNUGMI2UyswGOqUBq3l0pk76C%2B5JME16gIjHwftH7kiW4DpMa3lKa0r1ENvAGQCUh%2BYTnnCAXXXsKJpWo3%2FnzwhuajqjQ1vxbCt4exbBsm%2Fk8UZ79ODlknb9Pu1BMAmvDXD9GmQrZ%2BgMvXlgLCD9xN%2Bajmxid%2FSgbr5vMwQ3IOZ%2F8TMUIfpVSWUi7knch%2FhEySqp292k7VlBsmU4YF7Eh7gCqriev2Y%2BNdEiq7GfLO53&X-Amz-Signature=a147ee41030f3f88099ce1f80043388f5e4be4d12afa69cd62353243d670a792&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



