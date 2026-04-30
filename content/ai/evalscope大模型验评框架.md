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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S3O6HCE%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDSiZzxMNzDfg31HT7VlRL4jBQMrjwqPUzkteR32zvEUgIgBbo0l6713iLdZbGKrq5WzC90Cu5mJgYpZhqSErrSXG0q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDHyFSDH9srgLdBLsKyrcAx9AowjQCf%2BVRQ7IBa19aZdYVA2O3hQXGDlUSQND3l6yKa0Tu7NN9H91QodOMaXDdDdSsY56QiDhdRAudjXMc9myibLsX83Ot7ONzaKy4VWWpdKGMWU22YC9YLf3XtIoKHnFQ7SpLDhjrN9qWm6hEFbCFYv81WmFq4DhUz2ajDskdEfmP8m3sNLFYcpgnhTWi4c6%2B1HeOmWQ47Fdpb4eF%2F9%2FGfLyuZ24nAuJq%2B8HFXuV4igkn1hCoHlIOqjouZE%2BH5Gj%2BmqEOF7ol0g9u7bd92T2pGwQK0Z1MzJaNizrbAf22XQEiPuAq81P4zCizuQY0U15LjzqucamB8DEOL0Ky%2BDbqKQfAnXJ%2Bi9Isatvzttl95gIT07fWIrK7OXBV11LR96xm7OXUs13uSf3v%2Be7fg%2F6hiP3EUuCpBSjvIaBw7949fc4ZNQFbtD0YwzCi9TTNBFMhVm11f2tni%2BTw2ux2hgPCmoySU0%2F4b8CoFXfhYqZFS%2BexZ%2Be7tP6ShUoldUKcCn1xDiXCl5SiI7TORU%2FI%2B8ACSt5g9MX0ZS4RlgoOLH3rZ5bFOo07G2Fz0BL41Ntcla6JRW7xieBYwLyDUNv1XYOmkS75dDh3Y116bkRb6MV1mg2zXihnReRvPD4MLKbzM8GOqUBRDKK4VN5kVNokrUBQizngDR8MjwVW1mcOfWARAAMIFqpy5yS4RgYZ%2FIXk%2B9oF34hs84u7851N206NXSf1nIT%2FZ1lONan2rKrLtVZXke980nsVNZ%2FFmFd2nKsrB%2BmekqgZ0OvzlksGDBnipJ6CjbXWeSLTUugZfQ7aOu6tt4u5xkAzlhC4KvFNpQMWh%2FYIAYZaxImiQfSIdlbRJ2Ab8c1bIgXflZQ&X-Amz-Signature=4188cec21b166d2383240dabf3cdd90e6531b01f7ff2a40942b675a70c70c2ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



