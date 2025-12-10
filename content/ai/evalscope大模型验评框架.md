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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4PF3GDY%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHJxjyly%2Bcg1Xl1dJw%2FUP7B3vHPxKn9nLgk0YIR3u7rsAiEAjyKbc2E4%2B22ekSpupsuPxCg6b%2FYu8WsevJoIDYXFwqkqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA72eq6tJwUTwQQ%2BlCrcA03N1dLWyeJvxLkWCbr2ZST4jPDHFum2Ahd5%2FAmxz3S0wpIRGGbVICaSuZ%2FxTpUmBQMpfbKcGT8XS9AC6n6x7anaB8MjzDfad7x3PDOmAwu4msQIFae1%2FIepqRlzlv4pPnEU7W8n3ndZjFJGblX%2Bx%2FKSJtnkWcyqIT7W1yGeYQbJpkKHz1qwdueUplc%2Fvk%2Bg9we0jiV2S8fIN3qqiFt5DEbfDpPtDdE9wHi8rxq%2BrymFU6FLIA68Ynjv4gLRFs3YhZ33xLaVLWmgpzXJv3DB1%2FLUMCv1yA79bNwP1Z18O13%2FTFoMOi1oFG1eTQHzyV0SwXRcvhp2IWAxJmbBgJyATdZ0NNsLQn%2FO5NZ4MxjN5NJ9fSuUk2%2B5Dy0Rk6%2B50JnVrHAYlMTvRzFRE4Rq4Fr6M2XUfIVn%2BmeDPfZWCzZAs1OZSbSdDb3N3eRHV5osDoo3rNpzCxuDtXEhkYyt%2F6M8eOSRI2Oa%2FiaGDZyjJLyDhTiq%2BxJ%2BKGSngpTAt%2FADvwj345wBSBI39CVH1%2FPufruIzDWMRKSEsQHbVQxEjjcNcJkrtAiR9Rbcw6pYmffSF9DlWvqwlRwOrx7bAhlOyecQFqRLeD3CEbJBK63FePqOIZ05%2BKVYja3IM0xkSK9kMLS%2F48kGOqUBLCyJtU2o4N86qhOEaZDOszHEhJY1MIO%2F4kMu1oes1mSgiYlhI2hBULARGRkYQBL%2BFod%2BARAUn650GJOuCq5qIAAHKdqltBMha49d28xR%2Bi6Q2sX3D%2Ff%2BvI62AWYgItRtCat%2Ba%2FlLCnFCForNJk9xzJS4JCBa86sEWtpgpkGrda8XlKDH77rEHfLUglSLCnRQmfnVDxn42N7FO%2BlJCGaUj8ZNzJUD&X-Amz-Signature=2230f3777b8648d12dcb82bfa969659360effd0271e281a14f640915ca496478&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



