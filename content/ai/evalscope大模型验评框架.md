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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT77Q6WE%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCpyc0xPi1prhubKUMgAMsIEktZ23gFtNOOMXE7gCNOdQIgKChBczsKDqI96jniLKAQjxtayaYTSjjEFZ7RTwCKkgsqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2dx5wuzmPpXuqoSircAwTeYXN5Chq7nuvcXldENyxGQJFF77RAsXF0Q%2BQQBE1dqzvXorgba3xA4ota3823iMV%2Ft4xHci4anRICJfHonY4tapnrLNj7Cjoprc2qq2y6Kl9%2B5AO2%2BgFwcwrwgdxrR8k1WVGvy7uqqAyWbfwWNsY8006NfNFT9IXSVjtNUEibp2tLdReXsfAqdqYdzWdoAq3l7N7WDkzVRci2ktqWbNS%2BnLnSP0mktA40vS1tMhiOm40KdzNP8CAwUM%2BYUeitwVzke3TRvJHkPLRSPca3tGghgYIqkWc9hb%2BK1W9M%2FJEqIqJR1W576ZLC9SKLHGQZxG2N4ZQY4k8XVtfcnl79ozCmHLG7d%2FVM3Q%2F73B8x9AljUDAKy9LGJX0KOcwlsCjHoRQFWoYXY4LLGBZliKWIJjx6MnmelWG0Ud2B%2BryPM6redZN9HlqbhXXp0ox%2FRrMZ6gkBEG89GS06ZdeGj9G9Hxf00e%2BGDRsmYn2pfMJPqXwC4zCXhodBCZsuZurj1Y61sxyDxUOEVTdsOvN1CG3A5yJWwIe%2FBifMBcmX5k6HH2VAGT59rFAIF61wyvV0CCGZaDjiUfp5QA7%2Bd6j0QeClADxbE9sUPoXVKxI6o4NTUc6UfWhmv4X90ucNMrg9MPmEs8kGOqUBbTULtCCqfvIsOLeYY9vavSkaPp2BAUnCvhH8cYjr6rzDjJmGIkbiVXCkX0zr5V8IKRL9Lx9Faud7dA3GHbyBh%2F9p7ANWfD1TmrKT4ww%2FxznBq1FSwRaYv3j1YVdYuVYhmQpiQQ2SGmwHmMCMqczsHRHp0flTJBlo5BMoxDU6cNOoLyOrb7gKxtUK9PCEfe38t8JT%2Bcp7gNiqq3QpmTLcDwf8vDag&X-Amz-Signature=f0c0bf3e5cd24d1b3fb45886de92e7eb1b3c18e7bfcc1451a618060acf9c1c1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



