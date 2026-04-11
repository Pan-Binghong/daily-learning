---
title: 基于SGLang框架进行Benchmark测试
date: '2025-03-21T00:33:00.000Z'
lastmod: '2025-03-21T02:46:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 SGLang最近更新了，打算重新写一份测试手册。并且优化了一下批量测试脚本。测试对象为DeepSeek-R1-Distill-官方提供的六个版本。

---

# 1. 环境配置

拉取最新版SGLang镜像

```python
docker pull lmsysorg/sglang:latest
```

---

# 2. 启动容器

```python
docker run -dit --gpus all \
	--shm-size 32g \
	-v /home/weights:/data/ \
	--ipc=host \
	--name sglang   lmsysorg/sglang:latest /bin/bash
```

> 💡 -v /home/weights:/data/ 替换为自己模型的路径。

---

# 3. 进入容器

```python
docker exec -it sglang /bin/bash
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XV6E6ONU%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIE27qtprUMPMUPeQ83NLZdElKTetHByr0nwqI4OkPC2HAiEAii1VmSFMIWEcpfraKwgu2dcyUUj%2Bnh0a%2B724ipecSPwq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDNvmbPRX4RobDi5fvircA1QAZCgJAT1xjTvvtJwAYP5biFL8v4gDKQQUk9Zdd%2BdawBFzYPUwqnbB6JkoeClWfuA5Y2uTTsJXs3CIuSP1JzE3B5nGSjesRsHwlS8q5wEJOEp42aA2TnSn8PEQNAlNzv7tbIjhZbKY2eNTFujKMmwcmZQldSpT3Ms3Cg0xnHJjje1ZlQuRtu0JclEKCCvsdgCk%2B20mhnqH%2FTiCy7RWrUQEYdCC3CL5INU%2Bs2dgSwDi0QYwMcl8vFDz0p2YDwED3FZJOnB0KDq9zt0B6MwNfb8znLFZED%2FnJrU5ugEh8L7Nss17hiHMDWvYAIbZ5CT9j40%2FpNJB5jPWqN%2FPrMx%2FDyAVev0uxr%2F0MC5gzesfQc%2BOmH5pJufZ0lRNFOcvKgR2G8N6dsgRYgTkDKJ5HMkuPtbif0ZptW9gHUqCyHt3ERgJ6t%2B3kOonTlkNvkiyGfE1crFd4l1SeK7E8lN0wylPcREaAG7TO1ppEsGAfKdJEn%2B5XXiDdsXpYh61mnqxSdH5qnpvNjQdRStDw%2BT17SyQGu5pj3vZoXhNOwbnmGMkkdettSDoUOY4Uiu1CZ96Jku1HSVBvGav2ZncyCgvuQZ4MZ%2BMXB3%2FP1G75OR2kHKYlRpJfZ05oY7igIoZCNGmMNDp5s4GOqUBEsDOV74AfXzwaS%2BzdNPtqI6c94fsLjJT3L2JP6cuYG5EKXKtrqT47BWelBsq26%2FzOAHBN3vGhrvbIQbtKSInoJl2VhD%2BE1ZIxPArBk6y3grMLqZKAh1iswfSUaedt%2BBSWEQj%2BigSqepmxPF5%2BB0Emzt6Nbd90%2FBLOMHL08wYrT%2FWezaMSeReHQoWh8q45I8b0jbWyn0F9bmMQAV8tBl2hCkw6JJb&X-Amz-Signature=804ab30193591eea566fdbf082cd53753deba9666098bf4a2b1fcbea6d62d521&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XV6E6ONU%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIE27qtprUMPMUPeQ83NLZdElKTetHByr0nwqI4OkPC2HAiEAii1VmSFMIWEcpfraKwgu2dcyUUj%2Bnh0a%2B724ipecSPwq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDNvmbPRX4RobDi5fvircA1QAZCgJAT1xjTvvtJwAYP5biFL8v4gDKQQUk9Zdd%2BdawBFzYPUwqnbB6JkoeClWfuA5Y2uTTsJXs3CIuSP1JzE3B5nGSjesRsHwlS8q5wEJOEp42aA2TnSn8PEQNAlNzv7tbIjhZbKY2eNTFujKMmwcmZQldSpT3Ms3Cg0xnHJjje1ZlQuRtu0JclEKCCvsdgCk%2B20mhnqH%2FTiCy7RWrUQEYdCC3CL5INU%2Bs2dgSwDi0QYwMcl8vFDz0p2YDwED3FZJOnB0KDq9zt0B6MwNfb8znLFZED%2FnJrU5ugEh8L7Nss17hiHMDWvYAIbZ5CT9j40%2FpNJB5jPWqN%2FPrMx%2FDyAVev0uxr%2F0MC5gzesfQc%2BOmH5pJufZ0lRNFOcvKgR2G8N6dsgRYgTkDKJ5HMkuPtbif0ZptW9gHUqCyHt3ERgJ6t%2B3kOonTlkNvkiyGfE1crFd4l1SeK7E8lN0wylPcREaAG7TO1ppEsGAfKdJEn%2B5XXiDdsXpYh61mnqxSdH5qnpvNjQdRStDw%2BT17SyQGu5pj3vZoXhNOwbnmGMkkdettSDoUOY4Uiu1CZ96Jku1HSVBvGav2ZncyCgvuQZ4MZ%2BMXB3%2FP1G75OR2kHKYlRpJfZ05oY7igIoZCNGmMNDp5s4GOqUBEsDOV74AfXzwaS%2BzdNPtqI6c94fsLjJT3L2JP6cuYG5EKXKtrqT47BWelBsq26%2FzOAHBN3vGhrvbIQbtKSInoJl2VhD%2BE1ZIxPArBk6y3grMLqZKAh1iswfSUaedt%2BBSWEQj%2BigSqepmxPF5%2BB0Emzt6Nbd90%2FBLOMHL08wYrT%2FWezaMSeReHQoWh8q45I8b0jbWyn0F9bmMQAV8tBl2hCkw6JJb&X-Amz-Signature=6e56eb1209c099ecbca3249c07d5c7bb6a82ce1fea99a0627f02419c413683c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 5. 吞吐性能测试

## 标准|官方测试流程

[https://github.com/sgl-project/sglang/blob/main/python/sglang/bench_serving.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/bench_serving.py)

1. 修改bench_serving.py中的代码vim /sglang-workspace/sglang/python/sglang/bench_serving.py,将SHAREGPT_URL的域名替换为hf-mirror.com 。
1. 运行测试脚本
3.Result

---

## 创建解放双手版本

1. 创建shell脚本
1. 运行脚本
---

> References

