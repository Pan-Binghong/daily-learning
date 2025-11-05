---
title: vLLM框架部署|性能测评DeepSeek蒸馏版全流程
date: '2025-02-15T07:52:00.000Z'
lastmod: '2025-03-28T08:00:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

# 环境安装

1. 安装docker
1. 安装nvidia-docker2
1. 配置docker源
1. 拉取镜像
# 模型下载

```bash
python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install packaging -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install modelscope -i https://pypi.tuna.tsinghua.edu.cn/simple
modelscope download --model deepseek-ai/DeepSeek-R1-Distill-Llama-8B --local_dir /data/DeepSeek-R1-Distill-Llama-8B
modelscope download --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --local_dir /data/DeepSeek-R1-Distill-Qwen-32B
modelscope download --model deepseek-ai/DeepSeek-R1-Distill-Qwen-14B --local_dir /data/DeepSeek-R1-Distill-Qwen-14B
modelscope download --model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B --local_dir /data/DeepSeek-R1-Distill-Qwen-7B
modelscope download --model deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --local_dir /data/DeepSeek-R1-Distill-Qwen-1.5B
```

# Benchmark测评

1. 下载官方代码，内含benchmark_serving.py性能测评代码
1. 启动容器
1. 安装vllm推理环境
1. 启动模型
1. 运行性能测试脚本
# 结果一览

### LLama8b

### Qwen1.5b

### Qwen7b

### Qwen14b

### Qwen32B



