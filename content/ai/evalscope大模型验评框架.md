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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AIU6SER%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQC22dN9ozaK3qaQ%2FDPuYLWUBctCgkuk1Js%2Fv4h0skX08wIgGtXCvNuwBvLQTK%2BvIA6wKvmO%2B1KUJ6xwSlIWKXFSXD4q%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDCSJ7n0%2FsAP4PHiyySrcA7QatYtTEw8%2BR7TcQDrh0%2FScSueFvaQzOcblN6GNlmZcgXcfMWQtTGirTrdDCwVdQo5%2B4r0a68FZq0PzCLMQllyTUA3KL1rEp6hq2RwN5fSzDrUMK2CNaZme6QRFW1%2BmhnwZUwuMrbnNjYYwPZuGdLMVbHrN1IKnoTu%2BfbdM7TxwGHHG2YWIMGWbXwO2klfGK9OexY2wgUeBHlql3XoYXPTuAeP3LzYcVmKIDfwb00xJyK8Zrgr%2FwFGhz9fVS3hHCC24xCHVkge%2FGnnMicnQxOjxmKzoGl9qa0Yzttes4p1jSJfbggQzjaz98I4YOpTfU0GlRknK8ehWOl2nRnX1mRrq0BYnpcKKrf6AInrEiYNjkw6gfb%2FiNCr3aRKRJ%2FQiYlG3OzCt9MJfHUd6lmTLeOSIX0TP%2Btfboc0h3Xd%2FuHQOHoow9Zh3w%2Fc971kTLyrxgZhgBCJPyzlRbYUukqVLA9w%2B9CGw8Kc%2FLaPEH5sgScEGQfUSK%2B5ouf8O6KGZySKrYvH7cJa17B%2BWnbKIJ39iUYGDjNa2AAU5ZNOUote5B9axnyEV72YjJodOUI0IyIYrIQaCw%2FRmBVxnajmBnxz7booXb0P3k25w%2B00bACfxt%2BB13Ojualu3lTtfjdoKMPmPvs0GOqUB%2Fsisn%2FU7jhuB6RJHO6Ehzxh7m345peaQnnsHvorvuEGNXshclcy6JYgympmT%2BhURatpxYodYVHTZKjHF2WURXnZzp%2Fs7IALSAAYmv5%2B267rZ%2BhhdnM8rTYWAEq1apW34Ju%2F0ZphyzkUKcsX8vKZ3n4RQwJ0pYaqTz4jOMwU78z5MHMMiCEUN1OQv3yO2q5RdHwwdqUoF1b4ref6oqQqhWf0UqObz&X-Amz-Signature=e70950031beffcdab88c0f4da70ffee5c18209d7c70f59a3c8ad074290ec194b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



