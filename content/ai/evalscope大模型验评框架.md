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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VX67T7T%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCz8z9IZun%2FNHYyODBBMR1XpKG1%2BPrlcxS6b%2FZ77ow%2FegIgcMJBnNxm5Rvvy2NUt38%2F5Zvj1t6QyIdK5wfIMovO4RsqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKb75Hvp%2BIfbVpJcByrcA7fGrABfRGvby%2BIAaMe1htXX5abGv6kkafkt%2BK4dXk7G0INVYx8CkU%2BVQrr30TL6EJh%2FabB6SK%2Bg2PXC%2FlDICw2AbU0lIRIkCsk7hdDK0R%2FgSh6dQl16lRmRBiJnD5KQjlB6gBM89yHnECOcqXzocbdXv8AMpQUEk1QgabPvA2qMJfS5%2BNWyKTjuQIrfA%2FYkWsrXw23op%2FTiVDPwxVvr2GUG6nWuasmMKPEb9rILjWI7CrwYxoiuUCjTPngUyN%2BGC%2FXXj26fELiE6wwPFMXLyyYZLn%2F2SScGlARNe63W%2FCJlg7uKS1zt7Q%2FHR9m8nYufS6JWYbCTgVFa%2BWq0%2FS1ZF%2FsQVV2JQVbXsGzfsuQoM4nK%2B7A5u9O2PJi%2BSYMyrPJdX%2B0%2F4RlWmIW8W8OwajPKDZZQlwJS8f9jy1sVGwvA3h09hYnCh0UHeVMN6l5AOzZqKJoC9ApCLRqRLdEm06cu0uFHmxFPA%2F0zJXCGQht4uL5%2F5SQFSOiaUeayKwcuhL%2FCi9FVhp7f%2FlGLfCcr6dde30dkBtuNT9XnsboALVNlN3W3WdoOBmLtUcGR%2BUC2VGFE7KGFq4av1b2KyeLGwzuK1Qv25TboC7FDCbbbZyOZuFaLRZCCoesvPzrsHr2EMMD5hssGOqUBEwlYGuUIwMsGOaK7R6iXHv5iJp%2FDZoxDkr7YnEIU7aSTyQKS%2FUEEGcYE0byQge%2FjahjDXXR5ViQeSNXodWTKggBzB22YcNBWx2pCb1WIw2I%2Bbh6sJQa%2FjFdRHthUj4veqUa%2BcE1SAMm9imp8y83X%2FFGTjSmzQMPcieZVFe7IyXf449oyZeNmuecAvOSxOBaW2Cjvbl3xsEsFZjfz9qjhetKMlOtx&X-Amz-Signature=cf984b1d451d73d05d96980361926449e50869f5895a337871955e9dab12f21e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



