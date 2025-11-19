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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3BIA4XT%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDxkYRggvOzRUDEVibY4TI0Zll%2FpGav51t5rQPQgV2wVwIhAO1Ob75l1Ok5HKflY8NA3TpYcWgGlTxrfBKwS%2FWOXt2EKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvQQ0wLFVwmVH7RJYq3AOy6vF25nu9fBKc2wKQ2CicqUsfO1DxaUthT347MZNrNfnN1aAbkLdYG1pE%2FAj%2FA0AeJAWBaKq%2B97vCgUzWd2VmG8C9RH4xN0i6MYQdJnXOsPR6xe7fj5yqs%2FlxjejvTSCQ6AWURWY%2Fu8Uyspccq5GniRMSibglOY3KHDys%2Fp2csZ7n8E5Bh2OZ1vdJliSxqvWNFXBhHhd4uMKrpkMFGcqtj4hWuIta1ktVIFdlWDm5nGNCwPL7h0TIuGqFRnhEdt0T57rJVIJSSkh86ZMLm8kT29MR%2FFGfCGdBuAyremvl5DCUji4tTUf1W9spUxxNxZ6I477%2Bt9xvL%2FSzoHrNvdNUps%2B7qs6tqPcDZoSDTIE6%2Fjfz%2BVo84BXxLCWAn%2BsEqF5a%2FsTy78WdziD85LfZcn%2FvpyzJZlnpsxWi0RH0G2Cv6VAsEyWlVxEBuz%2Fqk8dmlvMkv2CiCzKBhPOTCe1pUwvpwUF0HcY1tPky02pEV49kVsHcjIjRAO2llLunOgqemXyXKVFHE%2FYZMtp0%2FmilStVvemI4oym%2BiAmNs8CKk7Ij8kwxN7XIbWCY0HhGPvqciWf4epyetceW1TxtzObnWSPevbV9dwJiOCwSUG2qCCGBNhOapq8VWORRtewsnDCdyvTIBjqkATyGstHqO%2F2qA4MHguTWGApcffQj9lYtHOLJvnVWbuFRxl6hLYy%2F5FmvjS1ikMrr3jqi%2BocvgwgQ9q04trP4fPJXUE2vAzLaMat7gO08%2BGt6w%2BigchhfKQIwV4X5CfekIISARR9d2LPdK8O4vfQIKDifentbSCOrMiQr7vSsPrqlUWMrb%2BhhaNLKvMh2lc%2FASNsuzVp%2BETX9HjKI4kiMRGxOBxJ3&X-Amz-Signature=6da8b012df188de31004dc300dcd6ce16f2cf8f9279513971d34232dc8502089&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



