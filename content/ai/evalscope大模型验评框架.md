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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4DPC5CG%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID2H2CMakotO0ZkDZ6cm9GKewTZ3ly5nWVIKbXZlmSvkAiEA70mSh5YeCmaQkfeu%2FXvYz8isOsay14a6FtlCY4f69Rwq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDCLP8DuRsBiQUbxFoCrcA5KvoCADyFIDnWxZ6HBVA9OA2BRsp4JWRTHEzler%2FVMd0jsUpvDSjkAjk%2BUkVujl2wv9hrysEmGReb21CurlMLWeCB2olNVJ70htid%2BoM3NWERgDIQv9W19YnZVKdzEEmgnmrxvhHNghZfG78g1W0nHzSU53Sr8liQt5URqq4HvMa56a3AmND83viASHPkyWEq55f0Lesg4T1p1qP3DjJAArHmi0peh%2Fmb0MG6QgR4AL2TqHDpeAuHHhc40ePFDvqH2DBBBOKEkBW0J6Wtpuer7sUlzwcMUJdp1tKhMT0LxpQ2GiDkarmkAcS2qMzr%2B5ODT3EOFInPiEpvcKZVWoR8opw4KWljsb9rzIaXerFWqOlx4DXwuwtnRg68PYSKSD25br%2FK4KMlwDnGpDvMLECwx4UEtYiyBTXS7xuZs%2Bj%2FJE4KoiGa5frKozF1lebRtTFUOGHFgr%2BcMYEulSSOeKjfftjQgxWaVRmVyXRyYJeEydZzgZ%2F%2BbLaeZQ2ZRC1VsXqZxZoZ2qPkLysLxXYDdvwdfRxpQVKtirYz50CmnoMNUYh3NRbnAz5%2FE6zrvXV4%2Fi5y2QWUpBfwT6mF7%2F3rhWpKUrYYL7OZg2QorCV%2FOaQvagsYSnG6WJhE6XrjzJMKWCscsGOqUBw%2B92lvdxDra0GxzixZo1iwN78yWaqZTbwd0iAlIQLSTom91wnglYPm2X67ppoX84zAUsBaEPBlGqTpHQB5PjddtixTCUxDxWi2mPwUVYW8jjRptY8rOjIbg%2BUUhL6ux4i%2FvIgPGHwnR%2FshAlgWEzqy5xr6mQ8TqflYo4%2BPPauGmGQ6yp13jhFZ1tiL0kPCxC3KKrwB%2BFJUdVJzvkzUNQboPZarGa&X-Amz-Signature=c10e7744187a6801aa00554e6ffbb40a01491d18ef188d0e77e851558130ee91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



