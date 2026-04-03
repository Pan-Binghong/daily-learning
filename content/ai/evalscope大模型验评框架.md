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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEKVIWZO%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn6QSVvfY6zb9yoMZnhb05hirj8WMNPeAr0p%2FnzlrgGAIhAMpRHlTltiWsm0JbsccLCIqmA%2BRoPZ8VEOEMhZwaEqDpKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwH9NzC3I6wjIW8ersq3AOyVvD5rjAoA6vtaHjbN5Cj2ivHWB%2BzGfmQZG5jRrfBcVA5CsMHif3kP%2F4Id6OYx9WUGNLTV3LO9u47aGLNQ4EZ9MYjyOrEL30vNWK5M81kOap3QBRBJQ%2BfbQUkfyp%2F8KEvRndDSbA96du9MKh06SoU%2FuJCeq%2FeDGjr57ibcsyRagXmR8nxFFfAImOrHwp6fS9vhKswJB173Tjjr2xws7hfTYwJgVxE3posHwzxij2c1Ez%2BaSlPlZq1aWu1N%2Bn3a9Rf%2FAOmu4rJwP5RdoLwGjkUAGSDsDvV7Ik2PNoZ8kW9t3tXBR0g%2FVneNodpjsyNkGDlYOwkDBGVc90LxHC0RyQtDegvB%2FHp4UmCwdtXADLJ0dzbfK2sWYKFZyctd6QJLJ0p%2BMVC%2Bwp4H%2BZjZK5OQArl8yRCLaAwZn3RIdfp10Q%2BWnL0SoZNo9mQ5uchjgEOUPQGBA%2F4gdbSHaZRI7pZrFWjNCxKSfSQkrNjD2LDFSUYfioEr%2Bkxtkz59WfKEC36YeJnuR%2FDMRH7%2Fu2qbr82E8Oa5sESnw%2FtvFnr4TiN7uBWxyuBllK7WXUzWzku56Ev811oe8KA5OVfRvfjftrlsKW%2BNADhVnJB0mx06tnbAj%2Bn8FnJV%2BDdK1deNFF2%2FTDp0L3OBjqkAeOcfEIzjfDLtWaIhFheobZXO4jAltUdl5mTr3id5pvXsz7mPSt6VBrR3X2hzv0VAnHR74FR0M%2FwOLaI4bZ3FMtABrLlNd4EJ1uWadju1cuUCeqtqgQgPV5FnblhrgyZbvfSw7U0WnOv4aDA6jkCFumHoHBDC2qIpRt5GOMEFll3RpDTYXW66Oej3b0Ce0PcXBvORYP0qPm6IgA%2BvLCcCjkzxriV&X-Amz-Signature=2d8f64bf6ee1cbfe8b2390633b5c189241d5f875fe2655b50d45fca8b9dc220d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



