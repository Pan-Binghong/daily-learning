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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NAJO6RL%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0jUFNedEma62VE%2BjvtJNZAtclPJbCTxdvYD21AJ3HNgIhAKGICFb4PXT2UEC9fiqPSBYKkHK4EbnCiM6vHEO15aJBKv8DCFwQABoMNjM3NDIzMTgzODA1Igyhep7ChiQAvAAmrTkq3AMbBSRmmtXdncWTiRaf5EV%2BxCIv9bS%2F2xGqbdflUcc8E%2BwzpSD8uc13K5X3cgOaCN7iDOuUcRkrYNYwGwSfWMSEWdeKsY%2Fx6g2kR8T26MN5amfYuYwxhEeiwwNI0wtiLT6%2FbJbz2kk3n%2FCQld5QH45JCOCy2PmVEL5Q6OAVt9VW3n0dU1wloLW9NS42W3dlVADyeOyKwBEp77st9sflPz%2B7CdVu5zVT%2BOcOSiC1S6STPZ4RYP8lhpuDnvNSeQSAjwnNhJBJBcGEyGCdoomNw7oVi16vCiKy7VyP0n%2BvowznYUVWuR4aR4hkNwemR22LIUNVbUdnSP%2B3tkjetglRANNhadnMJc4LdHSAV7HXPeO1RfHi7Heh7fyY7GLvtT8mcwi1Bwe2a4rlaeGmBJVxbeVvGobLaMZrCpyCaUJ%2BbPlpKPinDNs6K4Vqrxjf2I6lWcQkaEk2VQCPXxFCz9Q0M3XSbsYwngN64O7PJC4UdpzQHZbffc%2B8b8OlR9kXyUk4g1n8ddmtcr18DeQlYgENMiCUB%2B%2B%2F2gPZItAFKM6QeLeUSETCJ8C2bKsd0kOX%2FckofLetgqOEvcNer9OJXLr9jchXeExFY8RL28jaS9GW3Ee5jKHhmCAekbOWloOcXzCjjYPKBjqkAZCWbKMwiyLdAXPBYfucfyHhRAkkWslA%2Bn7QtGv7eK0gSkmywTVrpuoQtrAmlMYokCR2S6YdkOXcBy5Xtky878gTv8uXCf682LT%2BTPkUAXlHRVHSMGvgvJWvbjoESVv8SwaT6cMSG39e8hl29txbxfKBgEYHqmtGqVkAoqHMgsdSUMw7q5oFz39886ndQex2cdqNb%2BXHO7PU%2FIJI4GaSkRPljl46&X-Amz-Signature=10b003b5d483c4f2e4f0f0c68aa5c65b4925af28dac93a3b548d9f268413e738&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



