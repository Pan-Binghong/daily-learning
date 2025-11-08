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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ABCKLL6%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDg1VQe4E5O5eU60aSwhYYhLI140Uuv5gIE0u10JKTlIAIgUP%2B7Ln1A9g3sYQIs2SF1lJtjvWdiIuykYg%2F5i%2BsB7%2FkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGVNvBb7CUj9ghoQircAyRTSiI05fjcHntRXL3syQTJRUW%2FM03Do8e6pQHHMWfzg%2BWvxegZ%2FQ0G1uWYEFHDZvoy%2FvBTVZIl%2BihnMD7SBF%2FQDZe6xi7JfcmwvQKood0tPIS5GHufOu%2Fg02EbVlEZRdsaYlwK5RZpih7Sip3IRtGxZLVdQZpLCvD6NTD%2BVTkh7PvRN9O3pNRc10CPEXFImHlLjrbQisL2cXxCjkqEoYypifburARHQ%2B4T4oAE5WnSY3XEbJ0N0W8ux8WQav6hdO7DZVGepsxvqNdaIbIauX0hhzzfbgdNOKE52KWJ6RC4Nga71kEoDXm92SgVno06%2Fi0yeXZSe8v3xuBaeIOmRi53I2KVGoTGudFILwznYp6vrLLyoV5%2F7KZVNinApXQc8Tqs5MBOOC5Zg3gJCbpFFy%2BUxkheV6gvOZomcmGot1uQWbodj6DR41%2BiUQU69KnrALFHR4HJO%2BT4WW%2BoTAp3j8rYsYcJ00StAN%2BJeeb5BKCzyN4NUiLQnH%2Bb3qJV0yQ1x4DvCTVd89YE3W6wzL5JcsEWsYF8LDcO76cryZnq0AJgVwTbPBSPn0HUspC9Zmq92j3cOSe2J750imFIn3kKN5MFucGlCAmyRnQr5X%2FsbLuPk7zIVtem1GY1Ns%2BiMMzQusgGOqUBSkJJ545C2v0bWZW%2FGBDIUFdg74Ab2keqtqWIQk%2BQnnUfFoXAF5AzI4Udihec546uxaBoalrUhDuKeeSSZCY1Mvs7wG6gWsRcWUYbprMqDIPCSkvD9u15HvD9pF%2BKTQ%2Fl5HGwIfgh1%2FCS3xwv6P0f6yreQ6X3Q5JqVojs3Lj%2FTl%2F0veygt9sIxT58VNQm3TbVV2O1jiOj5IKQkcNJdYCv0JzUp2WN&X-Amz-Signature=1bd59742bed2e23bb5cc740a9cbd75819bd49401ff57f2f5d74fe87e62dfffb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



