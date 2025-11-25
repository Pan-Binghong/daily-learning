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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676NYMRHW%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExaZyrnS00Eq%2BBmP7NTtNrvcdRAVX7GjOD%2BbPagfalkAiBUKYbZ2P58MZCcJCgFCg58wEZJV7bh34TBHPLO59kdair%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMPrdWpcDKDZDH1BseKtwDSh8Jaqbd%2BGG%2FJbSjqYZw1%2Bz5D9DhLl6qLAIdYqJ76AMyXAP3RkFAqju1FwPXzvEiG5wEWK4ma0sfBx4T5Yvz6zgECFpotCqOwPRv70JqZXiH%2BBXMWLhkWDLwjBTFiBHD7wK8T9kw3a80CV9kEQbf%2FG1%2F%2FJcc77VJUqytC9AYuIPQbBEQpWgo3%2Bc5QzLtAsHiEqoB7fyXhCtfComBfNtQHb2bzi4%2BBJkq71HEWuHShfXDRkVTI0KwTx0K7vcOlQhiAWgmyJT9ivthXl6ORvY9Ut%2FPU%2B%2Fwmj4yAocngd8FGFrr6LJc2DoOWwmEHIZ4uE6z0KzyitZ7akNFJ70s%2BU%2BKO7%2BkpR4envc2IUeZtaEWCNcr1XjSfOMNyFBsLzm8D1y9q97Q1bxs113OXdPDgvSn7kdEqHDEvv8dZdfb%2BkkfcRpZBDX1n%2Ba%2BvJC%2BQEvm9z%2FbSLONmqdyc2Qau9PGwsXmtPemPNDvRzUbL3Fh3OhMmhKx0uMJ4jUClmU8%2Fh9l0zoSvYkRAmyYOKb1MkccMuk2x%2FM1O27Gr0xBlLivjS4NWDrUpP4bAhJ4pKkgktcmk6TduyNtE1svXVilvHmsLXKZTDQhI4N3Warxp%2F%2FVMVaxblaS0p8wsGuNEKxhN2wwra6UyQY6pgEIwDxixkjBUTtJyLJ6AwyNPCXPQTyOcU3%2Byu9bImXGM3Qkprv8BBqdYp4%2Bnm3NpQQ9%2FwW7ANoBvRfD2%2Bm%2BKqc4DP5F8pIJxTjB8pfnzvLfZkEqjYg2NkV9XrgxMO%2BISJhSdwEBqFeNZdPcP97Cxnjakgs1Y86FUClNqzxHiDq6fVOj6eSNM3x5wGGaSWC2YOMGMdgl9mUCvE4phWk0J3s2wVeqswT%2F&X-Amz-Signature=d27182eab7a31e77505a96ae26d2d3a3cec7efd0135de24abd9e113f3f79c0b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



