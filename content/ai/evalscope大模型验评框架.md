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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI2XV2MV%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBEn4gXa6dGYPPmbi3Q5NdktxVzk3gAdknkoRypfLpiVAiEAp4Li3JLj33MzPLyRmfsQJ5PBs3NqpMDEn91bPASMCLgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIvF5xHbjH87XfpvMircAw1MQIIBnFFERDSvS7UCbUTk8Buht37p0Bpyl14QJnxhDpFZku%2BALxzf%2Bb3vqKL8cVrsL2%2FuEL9ORKSmbc5Anpc2VSYA5bnfc5cC8tf91JkLbwbP2ecQLsOV3966ifr9j7Z0hVmNjUoWAHinDCSboHSI9d12KHr3mrSVqZ3UyPYYLo08pTrcE4MrO6FH%2FTrnNPH0MPK%2F6UhJSSAdNaOl2D3rxgqHDx2uIIqhP%2FBMErN%2FOu%2Bbs6FxxPZZQeMU4S36KvTFD5A6%2FOeWQn9Dk7qF%2BPeCEIbuCe8gl94HmQEANWBVxXAbikHgSxs19NjKBeHb1GSsqhH9afOWnzhJsn6evrUBrf%2Bah9H8uAI1lv%2B1k%2BqIWEFV5S5wRyWJ6GeBmYfVVAQlYP10GQDEbWG%2FDc90%2Be8gm%2FEjhwGvQEig0XkPZbMCU3jTc%2Fgd0rlR9Xz0ov%2Fyl54im8SkAsTWsXljN1Lt1RtIrlhIuGcGils6zXz5Zfl4i7zs6SGoFa%2BAHGc%2BBmcJ7bmo6lGB05eBVhx1TKYF5NaPl%2FiFX5Uu5%2BWa%2FI9syx8u0So%2FNjmsWq3YcCSklXbxtq6Nxj3zSacd4mx3BWBziPfdRtuvLVBmnkYkdhPtbl%2BNa%2Ff4TYCsiLsEThRlMI6Vns0GOqUB5rIbnazF%2B%2BZwLa7mmfUXTmJ8E9bdGODo5y8mTilxBEyXqAeFS5F92c3VKAUoJRUxA56bxPDIH2lM3Z289cc82HXS6xB2owprBJYJ%2BJd4KqSibHsrqlnYxwfVvv9XZ2WbJJ8A%2F%2FW8zgmuQTxAAC%2B8Sf0dgoZeGSs29mIF91uHdR%2BD86uPksRJetyo%2BMxkbb0L6QH5%2Be46BliBB0PviSO6EI26xC%2Fk&X-Amz-Signature=21ce631c51507188640b86d799a56555ef736acabf11c8beabc2daaafd9f0b4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



