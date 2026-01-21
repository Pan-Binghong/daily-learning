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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C2XYK5J%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCY3kRiZb1TbMhX6Jfb0eyMeH9oGMhcCnG%2FcW%2BpEIooAiEApJewjo02poC5iYqBtCkw5APJcWLZb5HxJ5tcp95%2FHecqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB1Tf6iFXaAoEBMGWyrcA3cG6Pb8moZQyjjwky4qFbq3x71UHIesRhcKmF2nqoWAZiYlikE3Rq5jDdNvKv5tVvueWXkGV%2BXjAcYdZ5TJE7%2FvHNnRK5KgJPJQMbRTZrykM3PE4o9bg8XZmRvfGusj4nOAKUBB9JtMsV50ylPS6eIPCZQ34KH%2F6qiEeao2KKCWhrqgkGPrjO93mdd32jrxjepNL3J0ERbIW8BmhHceWJ34qLrsiiLDPThORMtla3BdI15cCOVwEhL01W3dMlnLd4PWBkwfK1AAqZ%2BW%2BopitJOGDE30zN%2BtPG5FVxm1TQlnK%2Fx4PXM%2BCgXcCLXYItmgnHqGiojoqtYEteugGnC4iDnv1xxWQT230RRUan2Qvx5j8qQIgFZhfzUYHBzi3uRSQ9WiCgi4fVWufYyPL5MPbY9N8I5SlmsIAZjIQUWa6fPgtKF7itchyI67eqsYdW6SP%2FuXaHLq4BK24hqIgqIDDY8Hp4L76qe0XUR%2BbJxMFEAiwOAEen0ToGmdl38gTB7NGg9mykPckn2%2FyIInNNZTdeGPhvgvPBPCCNqX81nlvQ7XhwtEA9Vkd6MMvk7sCkXNqbjGTJASwYdUINclMvh8vQ%2BzAJGdzmmeeFs5qdbuljOfmPV7ealayZns%2FtEMMJPZwMsGOqUB8SXPBaeUya9nZpRHR%2BZq3eEUICYOWrWotdtrLrv8qlZZtILxgjEUUHTBuo%2BnCbbsHsE6R17Rx2JPKvhcpDMiD2aiz1t3GVOFFEgO0QIHM02yfbfjMDpqll6BlrOCfufLHcT%2FQxGboIUVWWJ%2BF8qBmpMgtayhK5i8mlEtf2R1pLRXCvTS4BiSgCS7QwqBpbc3a7mG3UmB2B5Am4mAXBz9zwxL%2BtX9&X-Amz-Signature=db4373e1880d331ea0bff6f2bd7d9a7dc98da34ca94b498a0fc134859fc1b39e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



