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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L7HKELZ%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwpMHRuXPQdqFv%2FgAqO0yc7noSz11K8X%2BeKiUJTHwsLwIhAIHEtg3Z1ztNfBi8TofmTv%2B9RrvvWhuNfjvWKtFyjQ9MKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGZ4pep1oGhLnOsdUq3AMcCt61VFjej5Nl%2FQZjCWNcsVALKcEQoBIDSJHmJR41ETUmHG0m%2FPWXZlUiaeXowthvAaNA%2FTB%2F2shjrz9bVIaCn1fe9B0Fm7IrwcOErd5HCQojE1zQCfNKYwa1NpiGiDiLRF%2Fd1gS7ZCiHhyMVFWXC4nT6KSjMDHlokMUXmmC90Gur5UHrnkZM9vYiMrlvBzh6CHkpEci%2F%2FdcK22OB8xLfbOh2j7%2BhbUbby97L227o27rW%2Bat%2BCh8f2Kvf6j6dpEzZ4Yd537%2FN7tP8%2B1X7oLUsz9Hpt7Qp8t5pQiiQp0e%2BLzWfgjJiP%2BXupzpoCO05n78MylJ3nwhh51Vg4Nl9IVM7a78xRj5uy13IkZi%2FTYR6F4SOXkohICnQQ%2Fr2WKAO7hkNcQqixcuMBoneOtZEsV5fhAdnFD4%2FxDA5E7ZC0PmPWbv%2FnPnGxYZG3nqU%2Fc5fZVI1l0BaoXU3pjF14H6eyiYpH9yCEQOrV16KZ0oXye3aldB9U3BiIL5lelYZcYRsGLTJr21KBjHmfua%2B3zt5mgXcjGufbzblzqsPGsmii7QiA89SMdmGDUAoztIg%2BezgGKNMa7%2BbrKWBMfQ4GIkZFEZXuznyAGps%2B5ai6uIRTfFm0n6YrB8wDyqktvj7jTCs18zKBjqkAVu76Xx01jWL6e6gUHFB%2B4kopLnWfQTsm%2BBBykTLZGl5wNtLtuqdbarfXaVFb7SLnqz%2FUIau%2BNfesIYMT2GXsV5K3Yf44B195J6Ln6I4vGb3yI5fS85ijMbsZk4yfWsZ8r5QVQev%2Badt7BLz32biyBflYmZjX2mqy4Tefg8VvMogORn2VYBkqbdNiwIkW6DlC7uAn%2B0L%2Fkl6N7AYVoJs93JV6qCV&X-Amz-Signature=bf8ed4d6780cb3649b8821ebf9ccb7488b7d9544a847004815e84cdce4d5ad11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



