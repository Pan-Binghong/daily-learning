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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFRBTI2U%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAeUXq%2F6fKTS%2BoIhuuo5fSnXUuZGXL%2Fs0j4GepHTgQjqAiASPKqIk0OA62b%2FTDzVPBcrKjtLr2aVSYxx%2F6IHF3jhUyr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMss7Se%2BUdOx6gGOOvKtwDJGILQPQpzmLrLyMpraq1O%2BaYcgXT%2FZGxg0e%2BUZT6f66sAYXlBeZATLF5UwurNv2ZTLQVBHqQwMiHdi7PXwbEwxW8J45fUnpnAwnZtongKRAvL64P%2FVMuToALzMV6bnPKzDJF7mNqEBarS1qKpfbgLk0UF4rBBHH71dePlTaQnAik9czP%2F6rPlfplaZbOZZu%2BKvNWAppFIPvhs3WhcpmthmReccbFS%2FqSoAgndwL1PK6DYYe3Jxav1saUk3TCn%2BfuMFO33D7R6646pSLYg7icj8hUrGnuIKvxBomCuNz%2FW3J7OJ%2F5OHXoNjW8PoIyo7OET547r%2Fk0dJUoZnvfNHi4sTvcJwcBn8nbZG6FQny0o8ud5V4e1WqJeTfbJ2UXbXQL9WkShhzzxI5ecuWmFQp11Pod8jubHjfeiZqrW17Z9FNfz2iwOuptZ1iQyyskZzFx1o0esMNvxRwGRJLonzLU5jvTIlzfJR9oEla6XK6zBfGgLPakuAUs3ReJZABi2%2FUt6gXrEd2WALfE4iYNqQd5WrWywP7h3uaGCJUFpO3qEii5b60wBKI%2Blr3j%2Bka7eXnRL0Ha3c6fKns2nVksaZOZf0izYL1Rk7RD4KNpvZGjJg%2BUE7omeAJLc6gztWMwqJWJzQY6pgEoYfG0uGGrzIenofuJOBfTWE1gUf0hELHHkbgN4qLy7IH7ZlxmcBgZtMK9D3sbWSnJ3KzZiiBH%2Boor3%2FZOu%2FcEWxKy%2BuIuA5h5SQGqMM%2B0L%2FEP4FMHeUQ1Ul2aRM%2B2a2MMGFBjsiaklF2i26QbZ14fU0pLWwPf%2BEXXBpffIV9Q1D26bh8sQF85ullXuQLWJDX4NrSf0a86qaCEasGBXnvovjDrARQk&X-Amz-Signature=5adaf2cefb5cd96bb83c4cfa7513b9e27e21e2d0517b857a3a7e25151a35fccb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



