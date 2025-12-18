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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SV6KBQVA%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH83LM%2FHfdU4xDGK2iobJ16Kqeyq3V4F1nhPsSYK3el3AiA9jlCialD54m0T3TvbfJs8jRtT6kjOW2W7ojB7saBlmCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvMSuZ%2FGaUcjWbukcKtwD9AVhoIDMCOEC8fKhJvMOq2pVdIbhVeYwRACS1ro7CDSzfmtbL%2FjnwkjpxX00cQTmZ6urCIZaff5NWud7SuFPBRmjNwbIJm2jK5bY6MbEhH9%2BYR1mLgkr99SfbajTgjz6CdgLcI0jyaECatrmNtN1xcoA02vxPMm6DLuMF%2Fe8xSjlufKeWrE8DNmhd7ZP1IT7ki1Nv3b9VexJa7TqswhPBAZmqSGzueKCROiG8%2FXjusIJj9mHTqfwdZaCwvs8uiTTnCc%2BjwDoX8u%2FQWw%2FUbYlbnyopT7%2BANVxV4A24iHLtUtKGtZytj4ZOfQK4MQGGLu5w%2FghTrgNEEDEI5frVs6ep4eESMktWSINcJqdpflzkoP%2FVBQ4jhMkYYnpPAi2XqYm4jIA%2B4qDWQKij1oKysiBxu8icq1Vjj7W5yXjN%2FkCPm0I%2BBV7hSPdhxpXoSBFEf7FhgSfm6x5UCGSfndk2OCmVCfUDnZJqX1YTku%2BgD4vQnfWFAN84LAeWdM4FjVtChI7XV8DRgLBnzLFuc9TNtFLnd7xDuIQ2Lpn4HvkD%2B5bZaS1b6pJnGfH2nhvDdIPrFovLZqx76%2FGlGziDmAQ1UmsnErgUZ6cU5NOTqQW8dLanYcqoJ0ugcOQj2ay87Aw8smNygY6pgH9X02Smy2hRurTokr%2BF3aolO39tjCMYnSz7wYATC4uIIM7Zpa28lJ9QrVLRBqw1s%2FWDOkPH6MkgJ4veLgsb7bOt3fuSOPhxb1vJPnZy7ZBslq5ny1gAhOq3%2F%2F0Gi9YXhPhIctsEA7%2BZz4ruZFOVND52i9K9Ux7Nv9vPuQDt4WTgXr3BnO0ZAr4%2B05VW5KEumjI%2FujGXZ382Hv6uebwOZmUF%2BMW755f&X-Amz-Signature=06342d68afc798076fb6660fa5c243d700d6dd4716fa26564ddfc487e109cca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



