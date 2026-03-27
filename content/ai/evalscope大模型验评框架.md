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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SRICEUP%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIGV38Ss7j5MAxr1KSzAJGIihXwLTlLGoumU25jHOxo3FAiEA4uOqDNSl7r8emO3fsNE2PMVngewj71jmuwoxOOhnHHQqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJDaMOkCwGIa5UYDlircAzAVl110zu97VeB7AgjpN5IJWwZisqYxSJxfPb2R%2B1Jvn51d7Jt9c3GZpmWZ7g4vtKSisYvYI%2FXf1Si6LQ1tD1t1Z%2FyhARvC5HUi1LpvTE30sRP2iziAAbHV6fYgvexe3vNh8FxfIZG2kzdacD%2Fyct6BSxyMGV1NtkaRhaQ%2BLfXM6iUWRX0DXuxobO7TywY3tn3K5nDOoQgykZ%2BbyspOmvMiQNkJaEVCLFDDptCiD3TKH4oagrzKqH1H2uqYKxXC5jjAKfkd2LWY0ir2FuXIikl74PtsZmdbJuAsqCdtsisI4HpQtD9GNlYeuUI%2BxYdrfEHCb8sP0n3OPk%2BfuRm%2FaU%2BMR8%2B5jCyGRbqLPuGTyduSR6f6pLY%2FByH6WA4iFZzgt7nxZzA2a%2FkMv2esv%2BghpktQ4xvBJxOrdYJloXjyctMwMgIqIzwh%2BU0O0Ot59Ng3GNuLZuX8E5YbCm7Z4Orz%2FLUoiGgBii7GTfpfZL8HMor3fp4zhfkE4h6fgYO7uGHwxVvdcUlhEjAqaXTXxaQ%2BlBTGLB0TwD1DKDygxZp57BvvAR1ZhRcGf3CFUqBFQn2q1QdbQ2QUplv4UkcBhoA4bIL%2FOQ9YqcANPaQ%2BXbRZcjvrYLZXCUP%2BuY0vcsEDMNPqls4GOqUB4agipTRMpJSPnslWbyNRRpKcGhnP6LNJbPyV4vim0ZsXqKK3aTURlha1N20iyHs97tVqRzedCjHDvUne2uVkOxpRWSGWVONg%2Fsk6r%2FrsqxGBYBC%2BdCHuV6W4CqDwR%2Fav5YXsbA0sKN%2FQ%2FEVR4xI4NrZyOpIhsH1dH5%2Fd%2FD7e2IYZZcKdsTSPbx8iIc8wsmhhluhl5i3cZtSfiQm%2FngZUkJqu5XT%2B&X-Amz-Signature=d39b15a1f298086946104d9ff27c9d8f28eb9cd16ac1866e9482eeded241355f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



