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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EU3KLBK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG7OXRECb4R3FZBoYWG27o3YuSY8R2jg0mKQDbywiJoMAiAEan7PdemIrn7QhRsbBK8I%2BYtzHK9Y82p%2FyBH16QymLyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ1ROxsqCGAZC9RA6KtwDhU8f%2Buteqx8hvIcNhtNxBFj4TMSDLlu%2BtvPcCnxy02BpW1VtBAzdoYDgWtGR00UJG7G%2FMBwcevbzhCNa%2FuRClKp%2B6YBHRUjXY4owC8msvdfZesS1v7L2VIM7xLbedvVgfuU%2F41lQ0%2Bzntads5p6b3ZDoPMJqY4JOxKjsIgNhrdypmaPw76eRoIKaEzrDJvA13eI1pDvwhM%2BJ4E0BfleAWEuj5v1Pwv74ujR7pv%2F419SW5QfTiQ9uEYGjIeC%2BUbjB3bFqy%2F6OoRDM83rSil8FCHs%2Flo7MkTz09imAVxjCyDb9VuR7DuHZmBrYu4DVM%2FkDX5gwHyxiJCe9UOq7CGteN4SpqUE9kXtHjHEptOk7NPuX3%2F9tM2NtPTF6mVBogrWj%2BKBkdvphq4Z1KBpD2usoRosO2GJsmhlqBpwMHfqIlVZIKDsU1xV0FT7DP8lyNwdIRmmVVxX%2BZYEkC3nYzcbjoHsJvgwW3G2wYN%2FPLDEB9jyypHWyY7o5qVixUnyRxb6k6QF0qvESyuhK6YqaRrhR5HtW4PiEp%2FXKVmgFb%2F%2BUReu%2BqWzyi3MAM9gfcgHSZPMfltOqeaviJXAXwYamIGUz21n36%2FMBvhsdRxz9suHti0qCW7zX%2B3XsMl8WJpow5Ny1ywY6pgEEBou6%2Frn5J3Mr%2FVlDtZb90gDd819hTAno3753XsPRGiqmZGfbUMvPPBuXZeBAQg23RqSy1mNrdc7Crkb3mGx3aTvhfRywpBDp0t7YDbgTynNUy2T4IsOAlpam1BShpafOEPHoMqfd9GVkOSVC%2FxSwe7ol9kaxDwyzgeQ8qPg0nwMPcKSNIu97zcFIrWQNbW9NhjSMqqhI%2BXDkUmYVkn2TJm0PyGyw&X-Amz-Signature=be66638cfd2afb84b56b687771ba9507913240999a9349d0a7941c8ee48d8063&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



