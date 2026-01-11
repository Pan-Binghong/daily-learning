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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPLTM4PO%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDocATCKRuJ%2FhJw%2FJlDALZC%2B0TcE0cAPfgeHDe3DWGzAAiBNCRDWydofW0%2B0WPdYkxFl2qxCGlSa5PgumScgH21JMiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkhzFBgW%2FgtdyMOzHKtwDK2AwOkoJkonBHGqmcks%2BudeGs7Q6QygRru78AZ2QuheC2FCmMKtda4GIs5rPVO9fF%2FwK2vkdEKoJEZiF4%2FGDWKzUaEfb3jTEjpOCVmwBtGVkO65qGDrCbC%2FqTTuRAu%2FVlP1v68%2FsMCinCRXYqoTaXxfUzpFacC2oowBhyl9elu%2FRJgPLVtjVcA0md7sZDmMvoL49hzmnMVxWF7RTGzvEySnYvY%2Bcp6WCcKWP1x2T1gpy7EglJsbqU9LOkjy7985A8fX4YjruGEREHA0G8ejl0D6mocJkyKOEEQxMK3iIeupyfvFA6KbNyw3C%2BcV8D5Itv3YW9GgLxUAnV2yXBsJJVcUXv8S0DeRu3oe1CtqU6A4YDbqjahSq21RvdyKtPraJ4Wq%2BfaOxQBPMk0PoHve8oFhgJ26B5dRA6hpLvdEMEygS6QFXFpmK%2BEuXxh06galSzlkURCgWU7alJcqSe2LRtOpqYXf3ztPZj14gcgBWMS%2BDPQkpHqHsO%2FfhN%2BCA9K8yk6%2FYOCspHeA132rcOj7vUHuJTk2nFjMKjvQgy9ZKCXW2WxbSMUZoU0JLRjVKxqlsveIyFx%2Bxfnxd2GQmVJ9nJfIC54D2HMBCBcN8VDz63i%2FadSmxCNhfZ76i%2BvgwxvqLywY6pgHiz7Av%2FVs4T2hl73ObsWtBWqMAxpAaAVYqLt4nxB%2BSwKrbYkZPIt0p9kcwOPAaDYiwt5fM9qYGqBHK3Qm3w8VfE4up6n8cWpwUh4zBUv6X7Csvly%2BSaneKc3hG%2FeuYYEhei8x5KOOgiF0oTIwCIm3VyLzAsRM6%2BOQDxtGKYZ4HwKmMxwaw9n%2Fts9mS7T7OTJ2dT6HMBOhM6HVWveFMt7xUDuFbijJZ&X-Amz-Signature=9510c20fd10e581fd8b377c6d353f7a400030ef3960f2f5c49643fd0c27f4e05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



