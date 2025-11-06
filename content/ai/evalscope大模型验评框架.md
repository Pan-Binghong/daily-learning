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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4WNI7PM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPJ%2B24B5Y%2BNd5cM8bwlZP%2FbLnAcIQUG2QbB1hWr8GXpQIgVnval9PgJMqF3am8uUl2Z%2BQX9Tum3g96z48vCmoqA%2FUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLcqsl4PHwMm2DeMSrcA%2B8anLAngYzZ6%2FF%2F754Y%2FoIou%2BH7ZFOCpix5rbpr6ntlJpPTG2hQx5RmKEyxxotddQcdSOKLUC7M1OMVoQxFFba5iE0FNsc4kjU9NQVXsQ%2BayzUNTpe5hHtnA6x30dVOTzme8OxuE%2BvQRgR1zl3OB0eIaEccugFUag3echQII64QeUYSXNL5zYeUA4KpcCQcxYoxAq6JzkbhBdr93eqDQSbtPKxSopiHpnfe7K5hU1gf%2BiwVovwV%2BKuZgVP55nMZ4rrpzucZB3FEXQP2t5AQuOpDAbkv2Rzy74tHGlT6PUnrZC1tvB94afv3as5jVscJ7nwCeoAsCrIaPMHFxQOf7%2F2IXfxQ1XLDrBav3rF8GBi8rWNyP75l3w6%2B%2FUUsfzm3YiAn9f33rjjs3PSxpitgrEkNkFxDFTun8I1cCW6KlJyvh1Mk0zaiG62nEFlvPVBqa1%2BQ6EgNj8UXcar%2FgA8leKA4SIMheAfJK7xfiWXUMXWV3gZic5wJyEC3LD2%2Ba%2Fz8MonX2yZuu2JeydjMBu9ozMcBIzxaLSXLFeEc7kIicOqfnp8j4X0ZmL7D7Mzd%2B%2B1zYlLaOqn7F30oSO%2Fn0HASoiN6WYRPB%2FIJomdlQAaAD5wc6O2n73h35iMHaHQ%2BMO3xr8gGOqUB8bI8KgcMlbnoybLNWzZELuqkP84F6N4IFUn%2Bw1hUWt8TIgUrGvtEbmYLov0eFBKBBTAsz8DymrAJT605JV1ZwLhTYeF%2BtNsxTVdinsIipeCLMXxxsDDxUpBOqNapPpPk49o3f7oy6A2oQ%2FDQltjAE9iiSRncY7Fy2LCBNP1dGzmR359qcP%2Bin%2FEATtHSpoWydw7QD5z9WePFngjvL5hqY4vFP53u&X-Amz-Signature=d308ddddd5ab5c2572e80b865dfcf9905f756945c43c7e2cf994bef055eaff71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



