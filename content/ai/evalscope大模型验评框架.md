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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HHXQB2H%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGpMIcXOPb%2BDqpaG3xjKPpeEuKP2BroTDpDlTUFWWOsBAiBD7PuyMvizIWK1i9kNkCNyfX%2BGK2UPI1kGioo5d1xRayqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZbq1DrDWXWUILLLzKtwD%2FBOKXtN1aAnur07MV21KQLqZNVItnXcqYsdFiuP%2BDrUlid7TPyCT6QPeDuOknQJmAyUCWEyJtcNdKBivldAi9qEQgv4%2BeUtnIlgpqnHFI6zfjjimQTV7rwiHILG8OOZ6IkxdrOHCHvrcR2eRLp7bLbL3BvpUl%2FcaeEfYJ9YAte%2BgopwrOLcopRzIOgOHqwJ%2F%2FwcMPSVj6wQH7KcVtLh2tfcUvhrCPcBjzVzrZy3va1Imcb3WPkdKcd48Z1w%2B%2FkYQW8iqPZxupklPGDvd2jhc9LvCJQWFjnoF75j9egj0%2BvVsvWHWjvglZpTAGFEhRlZq1JT10kZKQYVn987mDe7NS%2Fre8Z9yUUSme5m3QcIbidxB0tKpQO0vbltoewt3Nt3VNPawBltjc9cnmaWUmkHBL74Dvx1IseQPvJSdoB1lNNWhW1KYRZIzlQOzN19BOW6JvZEvOrb6ilxuHqd9k5NKiZQrWY7azHuH1fhtz%2F0n0mCR4vzPg7qgqBp7qkr12C%2BSjrmkOj3Yvzy476gwzseEHh8kdsS3mpjIEitfNbDJiDvJlnrkghM0c%2FvtJ0NryfAtVY5HtBFx3VqMP4x6V%2Bgi2zBm7eleOyULjRf65uaGiigb80wvC%2Fn5sF0Z1acw0Y%2B2zwY6pgHtzULOs7m2KAeLA7opDrl7XQI6nPO5P0ZW%2FzCwIB7ylmFwdLwGZKaSDhXNnfl7nMLD5JK%2F8W2FRP48HdVyVlgaqFa35mZ1ePjrFp9rYrihee45ImPPKGUc6PVBZ6rlZHWxotKkoF%2F3dD1c74p3manaDZ2bgKCGwXwZD%2FUczSM8Qns8jvP7StsQWKo7vIru2aO46jJJ0eUwPi4bIPf1iCtZlM7uOAL7&X-Amz-Signature=8fe708b161ed8e89229df376747281338cf9cef85a8a62f8b46530bdbeeffab8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



