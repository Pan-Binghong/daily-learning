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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDBWBXPW%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQDCaflKTXrAtA5YuWMhhCQ0MLROHatEzG%2FR%2F50mZiRGLQIhALNsKBe2KJpZ0T4V%2FpUylkvHUk1FR%2FtUJcfnfo5KBc4uKv8DCAwQABoMNjM3NDIzMTgzODA1IgyRE6oUpLNnKsnZMMYq3AP4cHZ6S0f%2BRQoHpmUKgxdoFUEL80N1yibnHv1ckSG1wM43BxcoN9YV9TjUxFCtAmQGGIg3bKhsdvV9u8IT1L294ooiuekSEaKUgcXX8Ea0YEUSGRF2vPs7MSkvWaMGvVWlt7TFmHxkmfPoVSRB72cdC16MYZ1mVtlXECoyp%2BBjz1hm4RZFh%2Bl3Uj1Th9SmUjiA%2BXhseZW2X4QL1xJPmFpgXN9bnNPlFSYO2gTA8ZrWJWc37AbaWpr47gMVkyCjwki2y%2BYMH1x9K3zUUpjr%2BvtCoW8F19IDjL6TKY59w1dudzKRvQENiXVqgGJWtaRB4YiaaOC6R6SUDfgPzXRxhPiUXDT6IQeOlMHT9nn0JDej%2Fx%2FDgW0fopQwrFlP7XPX%2BcJ4HjNBXYEi0E4RGfoouAJMl2AbKAqFR1Q4svaJC2g46qdA%2F8%2FmKdFZdmqEojcebvogxZH37xsT%2FXdpU6NLUWlS3HixlGlv%2Fsfv0whx1QRjLIPCHpp5MMOIJonvmAHGUqR0E9l7XkJIT2OWyhehop8VAFxBvWMc7o5HbXQRbtdurYPM%2FiJzxKF2Cg3H%2B%2F6i%2BgW2q40Ka%2Fu8dhiy204F8QzpRAoJLzr%2F%2F0uASdEg1dEeN3dzuqkyIX0zljoftzCMstzOBjqkAdC2xPc0sQqYCh7rqd9eViONoBemb3AG0wg2Wos5EGU0HCIz7cK1DJPrb6jjv%2FucZCzEZlxe3birvH%2BMnA7LIrBGRrZ%2BEI%2F0pBPFkPlR5ayNQ2FPHeGCvh1icoK1iRyz8InMK6VyNZhjSyZOtKl1XKHJHIb3C6TUN%2BcRHMYtAYxIzNli9QhGeCCn9Iqz0JgeqXT31FQWHdODIcGDHE0eyTzTubl7&X-Amz-Signature=4ef1ccb8df020e9c63f1a7b4af8ac30427b7c568a09b18fb84d143489b84304c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



