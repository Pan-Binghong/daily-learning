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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C6BMMRI%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCko5EgdOoWB7zb8qBd5IK3N2J0cSC7bTy%2BUo1T9isPJgIhAKg49IIulbW%2F5d%2B3sufE6pjaeMVyKdwGRftNrdreyXaoKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweDpRR45RagBFnweoq3AOCzIKKCX6FQ09Nid1Wbx6RLH16NriSt5f4oB9%2BlrsBfekT6AdGNWZUfXODb8pV8aXoLHZwmT%2Fvnp6Mf7W%2BLQOYxyaCyZ9OLRrsm0%2BnIWeYSzSn5CvOqQ%2BcLoo54s7GLTPlP48ODAoGbmCByl0hoKbGsMKFY0iLTW9XLLPhSO9WS%2BLFBPFVf0DsephgHflo5Ri7VVutSuR%2Fs53LRW2P%2FK5Z5yAJxxiqxZTUfF6b%2FazvOtIUqvWBzGG%2FrL60XouCg9kmFhLVTP3DfJ9YX1Bc79U9DfjIQqsiEIWMszsNoYmtMpSbax3xiqjH1U8iYJyT92fIxROjWCDAkaziETQYCou7r%2F%2BZSY%2B7P3lqFGvEBZrPu2he%2B%2BIEAWRENiAtgo9Lc7bZjVnWrENimfSvTNIBDqgR9n813Pj5%2BWBdtgC1qOqZO40M46h3OE37Ts7KsceObMKKVoP5p5JvgiAr3sqGf01nfRTyf84%2FHcN%2BHixDm3R76nz0Vvmb4AP6T3Vn0NoD0AHKo0DU4%2Bh32p%2FDUJa7nHicA5E5A%2Foi523dMRNm7rR1FfJgry4vt8084drUdnozOr4sEJbzf0RBWKlv0utmVmXwa3TsmEnOfANZ2cPgB8b0%2FAuDPZwV6ZToTC02OjDc9dHKBjqkAZHYjIWtAeYoo5IcKURq%2F4nNBGTUk1lt1btq2988X%2B33iq70GFJ36DF2%2F9tiq7UQ4SuDRoIGMh8Kf5wsHC%2FT4g3VrLPd%2BmHrEQ52966bOeO3aIyfYYXsY1obtl6Xu4zRzNMVIwQDH%2B%2BywI60FDu0Fs0QQZNPxN9R9ZZZYxzBdtCgsPiH%2FVlHr0WZ%2BX18hIRGGtJC%2F%2FWr43Mbdf90jCrxCrzg1xCQ&X-Amz-Signature=12495e9f395eec008317f3227822a8301aeea44318407353dbf13b8df46c6d45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



