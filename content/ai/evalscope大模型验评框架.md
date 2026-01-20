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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUS2KDJ4%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzXZrs8XNguvTWSr7D3gieBZVUO6uABpZWrm9%2BLWmRZwIgVujjoDktSTqynd6VayhfnDhv4lGJcE4EVhFON%2B%2BhPBYqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEDcf9lF3WKZ5o%2B0PyrcA7vNKotpbS7%2FfnGNm%2BMQiK8qUQm5ut1YMsxwC3kN%2FOztraMWDienbekA3rC8vbbeCd%2Bs8zzxYqXLNu0jPVuZWIeWkEacc1c6s0a0GjfpNzSJwtM%2BvjAQiJ0Bxk86lgCXg2kdr3KaS6ijnW35gP8VoCBoX04Olrxi1UuaYMUxqPdCXCW1ZXjjm1dhuCYirIuYdNr52qJTzPpxldeVCCJVjbV61vtBztFQocDapkHAQ6nutveF8%2B9YQH6%2Bc4%2FwApYPg2Se3niofumwjaB1ZKzVmORzIybxZxB%2BozdxejfNbpZKoyJUl1eMAeNrg8iyyro9s0liOBI9QOdZ23tkjjGmFz8W4q38PSPgxqFlmF2AdXPGVSBGxM0DvWwJZeFrutcdzdwEqMupGBgpCWhujPVH0MulNUaiA%2B28KbsunoxvkOR%2Fj%2BsfGt5S2FtqT0zzWImrlWCeu7DVQIvxFXetlBdCvhK4xwgVs%2B640dE3mECxbNGjt5Fwk4PAwotwy0BRp9tPrdvTRZxfMKs4VSUorxIZGuHRyH0F2LwxR4sLXJzW4L9c7jg8LNDAzjRi5u8X9aBIuGekf0I2GJa9U5b9tgxdGR3s3ODyc3uaGYUUB721S8TocPksGtED2Yl4pALRMIv3ussGOqUBs0tZ8XZ5MofW8JbaFbk4b9lZ6vEK%2BXSed0dhdvD5H%2Fjb40VF4ODTCq%2BtRaj6iVw%2FUgcs7lhpOlDtyeaEtOctsbzAvmS3eJd7VJYADy4ZUdKTtZGe7e01T7mFRcISUfqoOZiolcaxZq1def%2BTuMPi9FBhFfWx5bMYv9rdVfFbRCWLPUL%2FeNa3orGew2RP3n394jzZ9FlZMD99CXEhQMQRJZ7cz8QP&X-Amz-Signature=628d533a8a80bf65146b07f7bd06d36be88fa19ddfe55b081fcc288aa55c6bcb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



