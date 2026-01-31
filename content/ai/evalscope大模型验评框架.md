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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIYKJCUQ%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcwk9%2FILC8d0ikBN4ZqbXRhqh24OLScnAtPma4Riyl1AiBtylk2WejFQYmMLUejpda2YESQtqjJOnbMv1gS4%2BmJpiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnP2U7L2x8qECKCiYKtwDn5LWNXJuxm9UHU5rqcV8CJJ8qP2BPu%2FkZ%2Bz9qm5ZwSi3I5gtBzp2Di0e80M%2BZUWCtb5HcQgzOs6w8Q9vbmA6ZL7vORda0tJVc1dGzmL7TaPxfgDy1kPYq6kMw28R17mrEZHMh2D15rTNKcIuhtRfdkMd2G11u0Ngbpy%2FfYQ9vT92ymPJjtJjZRCwG30087iXeSEtseJYltEdONF%2FhzJAvPh6dN3gaql5dDGmUcNWtmXmXb96yBzjMhm5PcnzH%2FMyye6XBLCwcm75AILK0aEKrSoRMxvZWaZvzJF6rm%2FzEFUSCXfE2veIanzRlNDlcvVySI4%2BVoGl4XvJWb7ijDcYzot1qEUZI8c6C3JiFAdwmBgs7nK2VhxRpVhleCkehvjKyYzvfYQwEO6xO2j%2Brn9QYnGBXXvFZrYwl8JBUWVQ9JMG18Aov88PNV2OZcjjcg%2BCFS0RANJyvVNST%2F0rn%2BPDTVzLV7Y%2FpstLF%2F9s5859sWTkjI0o0nW%2BTCMDHFJcw3%2B1NDn2mvWuIE8IoQk0RPxvKELrUQqOhVczIj%2BGLoUhLhXuHY%2B6bYaCMZJWuaw9qZcbgmyY%2FJSVqzQi9SRMecPGaoRjFcteviAo9bizBdKTeqiJEG6WEq5opZjRNpcw68z1ywY6pgExQXLv2vbttoDTtDNMbbYgsd7CtbWRX5aqREz9y9t0kEsj4uJaAZ1b6R43fcLjtsL4wLXihcaudoh8fhF09sCaRp9H9dgCOtY77zJ4y2ykByldS7IeHjtsOcaB%2F%2BXOIMDs7InLnYzZKcFWHIDaEOqvj31U4ldnp0MGHHssCXiblTInAa8R2nmuOSpJgkTY72rzRf3hHI0g9ajic7Xx22kyE9WwfqOm&X-Amz-Signature=89e7c3278d921e9f71136dc88945263cc88de4fa4b976759b4342883cf8abec3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



