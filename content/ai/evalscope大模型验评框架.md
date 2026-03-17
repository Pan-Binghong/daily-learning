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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JCQQWEI%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQCZZADaBAp4R1VrbR0DFQ7aFzIf5a3A%2B%2F0OUKdr8wnrlwIgYVUJoJV8KKziSdoVRxcx42AnLYmkmZQJMFNIOcmmXxkqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2BEeu34qWgG60qzYSrcAxofUrGO0YErDOZHDYgNRWePwkE2B8Ffrw4XglkIxv2tqOWsVcilE0LSTHFQPw7%2FPGJ9eDtzWbNkOD2UT6A7oKLP3gccTokcyY5vuCfWW5r%2BoyP%2FEkODWf1CNy3q1luk230jAZozxkZF2Pq24nLPqMlzOgKGAI1ReDZzn%2FjsD9geIi9%2FIhXHWhXHxd8tS4gnEJtSUaopaAWTkyHdRexU9h0l8AOYUXmuGGyyYZq9gtBkmYlaFWTQYVcJ0v3v540uMpcWXVZGR05ZKILRrlQ4ntR6AJWEbiTq7c8NaKf1A52HhbQcGDmRdusa1N6T57ytcQeDAL5GkjTFjx1RThIC0lOHV9vtVA8KZOu5BG2AbCyrB%2B6SGmi2RYENTLi74rJVhyfKDO%2F4dx72Py3CrDVJwBbrmBszyAeY2vKfGyCBF1k%2FPNHo68NUUzXqpAt02HLvKInnBBycJCkR%2B9Otx2srz%2B23dHS7QulzEx0lyjBT07tickUYLKzjClMWALGB2muk2nZLHgujwAOfebyJGyvVmJ4WS9BiBcmV2%2ByP51mJmMEyqs8XOTwizZPQ5YHE0092rFlg1V%2FaZp4bGKNGZsPwxHCBuQkqFyUWxLSvgL8Mv%2F9W6bosh39m6pTrYAlXMObo4s0GOqUBB66gAErP%2BlwkEse%2FDChGu7un1bbO%2BOKStqDZ9SiIr%2F5BEmy24eL%2F8NBh717aNs%2FVYsZ3uww6z%2Bf7Z7NWHbXxFHlffUWzSuH4d7q%2BIv4cMk14JLydvej%2FC1aW6aFU259Q20sVEQ%2BXuVY%2BdUmw31DsFZ2ueoHZymHFPI0mAVhGUPcXL%2FMeE7S7oq6CfJizfGW27TsHTP3yggEOhSi6PM81GP0AUMNh&X-Amz-Signature=7ccdd5cb0780de25deaab1800baadf0595decb002b90f05b21c3858e4013162f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



