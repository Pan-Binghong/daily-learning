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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K3TABLP%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDWO3k%2BKbAzAs7Zq5mmd5HUR%2FjPhI%2BoffKG%2FjWu9%2FBnxQIgG51BHljUuK2nSbbJeoMAxsKGdT2Bsm8ebXDbEm7eNPoq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIqWdfha4N9BuUKejircA4Q4UpOcxKqNfpKtOwhviwoLvppusQYBgCqA3mlyMs4NKmapX7HmrQFFNfm7d55VluBAg01KtpoH9TWTXX5a9bMCsi08E5qxHQeaUfS0fE9dDRGlFlPQwL31snykCv1nGM73giDQQuUIdG0fVC0exRZCzq3SkGS4%2FOKyR7zSJN2bzIUzPu9u4MDoJHsmmEgx3kzaAs%2Bg5V7e8ykRxWFM6DaYV7D0Xni9UIzXimlSBjL%2FxZr2Wk%2F2YGRjw6ChcRbP90L0MYgHkCj%2B8K94bqDwT%2FZNYcYK8tXZxZH5sO97k4ApbrUsW30DiFkNEhkKGKqioQ1w5SVIxvSSwgdfjBB0Q2Rs3Ey%2FceUGpYnF5OQ0KOqQJkemWb0HV8W8NuJuiY0vmbBMrdqtvcdqUqQj7ZpUlxRANXNwoKzyKMls%2Bp55NN8E%2Fgd44XUCg91aFJmcZnh1kC%2BmSgEMdw%2Fiv5Z50n25T5TDGQtqbu5F9CDfA8im3dKU8VUhxUZLB%2FeuYyyyFpoLVTB8U%2BwPqnhkKJZUNNvcggYD8MxNYjm81meS1nYcB%2Fu8%2B9Y1pNTFsPv6jM4h5%2BGfXOwCWvbemxXjuj30GXXxrMdFITsGbNu6X8q8iEIh9HtQIf3K0hq4VBJRqtIhMKHvm8sGOqUBu5%2BbP5ujueMXC6cb55MbsEIZXXl5ELL1RwlQkAfn2naYTmIj%2FTZibwqw683e1P0bQq0ujIa1C4Kwrbv9n28qHe%2BDl9qCM64mIMAO9WDbMOg55rYtYXnNC7L411GJMSz%2FNXwSEOiqpuyFvmK%2BCAF5F3Yj4TAL2ssWCmeeaI4kLBNAkyGfEc6OQClOlq01WPH6YXdP23jvd9kEGDsERQMOPyDKftUK&X-Amz-Signature=832eb6a5da459a4d129e7651d17f13858df2919aac5c5a113f93c5f06e486e0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



