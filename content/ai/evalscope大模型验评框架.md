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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2PULWR%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEVjVl9w70SRJeQMYqNhknbj9iLQ%2F6qO46Qf5yyZ04VgIgXaTELL25%2BfoJyyCtS0FisUHTXAlgFm3YN7zhdWuk0D4qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2FtclmV%2FnoHL68uwSrcA5yV2qDvG12fw42rCqktfVnSmhVqvFu7O2KYyLs%2Fds7sPlRJpZnqAmJU3UuK4yJPwHnePaEtzvG2884aamyIfZTJrlImbE7R76VwzSgLjy3EpOZ6TYRBkATWsPgPgQ7ztbVW1iVkikLg9MGWH7ZAxrpEQ1J3buJd3cbwSLHwXhcKa9a%2B9v1KcaAfUb3Po0b9t6omCGVYR9V0%2BHzNhb59bNS0J%2FNceAuemgotV6r4EkNJqIBm5hdAMI%2BQFnw0A%2BXmWOOS5MOCUlyO1ouX8dqdaCFUUgBT3Gy1zNtelxWsYmLPLOzP8vFYrrL029hGT%2BoqKOpdYlrFUqAK2O3w3E%2B16VxE6rMKwpl2MuXpSjlKmfbqdMzS%2F2p6u04idM6vHamK7f3F%2F6f8NGKzK8RZ%2FIse6YuoCYahEvxnsp84u%2FMhk%2By%2FVaszkNI2AC5dcQvgOuLsnPcjjaHyeLV4MZq73eFshdYfEoqhltLMaV99gFIAqOoGkzC9cIiaKAtXb2O2wzzgavg3p8mfcbMfGcC%2B16ZnajZfvv%2F8hE%2FAfEpxj5olhm9uu53P6O%2BefLrvbRdscXXv%2Fg%2BK3Oih347iCs2jYjdPWW84alJXz7G6HoGu%2Fl94Neic%2BQX%2FsR59M9rXtWGpMNbEgcsGOqUB8XU6VICOp6ZLnbYJBtv8gzCJ3lTarDxppahXSEd8254NGI1wh9poQLHzY%2BkVK6%2BAugIiXUajLLR7GUA3gikeyn6PhLRGCAWMi8BDoaXF4GZFRps9N7ZVbleAXoUALq8p3lhVJNrkgxHjqDGLZq4BrFQNhwHyKR3tLis8SLQQjh6YVuKmShzossFYAM5VpF0%2BwzocByBivriAC748YsW%2BVTR%2BobJ%2F&X-Amz-Signature=841f2466d59d6ea8364fdd638a777e542177ba1396174ebed23a82f297637647&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



