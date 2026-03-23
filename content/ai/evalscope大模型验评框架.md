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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MUIUUGB%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjSQLP2aF7CiTd4fbNpzt4BxX853XUMytxkTnQ%2FhIThAiEAws962ya9W6A9MzEU%2BIwKnWxvuzuEvVleE2XuF6vqWc8q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDAodaMloSm5yi67tdCrcAywHxTNmOxKzAcePSqFE3d03qa4Ddnuay4zn6rS49gRXasWMYII%2FXaZuWkg34PrBJrCHqdEhElgOhnnz90BYwvcALiC1BX%2BmD%2FKiM2mPCKUiZpDxTievxxMuVhEpR8GoRjuxse5ojTNAP1vCw07qN2K1PdQaShAlQ4tTFwfSHKk3mblRx3QwiQKsnu64UluSEOFvy4TA7su%2FeOP2IDMJgD6WKGJIMZZF81Iss0s2a11lA3v4Sr2Wx4VUQddRCF19L4JV149D33BL2A%2BLgyT8fRAUA2IfwgX8P9bAsPpgeBrEmNyO89H9H5Y%2BCnGn4H8B8ZMh41lUiI4hnoeTF5lEdUhLF7YbvQY6yjeempO%2FVR5eQRbEMheOnbszVIomro6w6uch2BGfYTYXipsoPFD1wJzlQipboDEQtt1Z4lf%2BcCrYjmtIRDgs6GV9GRWDfCpDQnLP4%2Bv2Ea1GqJ15QoRs1QBRvvBOeo4y%2BwCWJykC0eKNvxkzkUoDQyhrQ5k0vt2BFo5CLpo6T3Zrb8WOrF2p5u2T6dfjffMD%2Bl9SBiFzAB6XcBM55ULKuJds9QRtky%2FZlntTLjKBb1hSGUO1o9bdy3tWZ6VlUyw4OaVreDn12o%2FLkikqtltwvsgnOu3QMPLjgs4GOqUBL5zPHPC%2Bzms5x9K%2BPIZ7gvgnB9JvbXHbhkroMjGRWVEAYwS%2BfU%2F3AduNDJ4VhRkbsmCsvs1fiLOB0Wuwxx3Ymqb%2FSTWfVTS%2FenrVLWmOhEWmFGf%2Fda75ObraegC8ydT8hBs6gUXHiC%2FJpYUTHccA7%2FzQiQ8nQkSesM1qXpurr4bc246eUrMoQrheM9krPKyLgKc9TsnQT2A6NZku9ACg5M81vznH&X-Amz-Signature=092857587d229c65220df83486e8d6720fdbb0d0f9b1da6fb098c7fb32fb3eda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



