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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GHTR5NG%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3kp7LxTy9M0LAcK3MCtX6fjseR4Ed1%2FZEcu3Aaeiy%2FwIhALDJJSkhtWUISeMjU73wBatAA6rZ8ygIviWVwiN6A0qhKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BMz9GYM8F26BX78gq3AM3FJey%2FpKv3CqykjRQSYn23xXmyBA5EIdxqxsx%2FEp7mwSoHK7l4BC%2BDbgYTCryrO6M5%2F1LzvSUqDJSX6EYoXfuSJsQgFmF%2FahPpHz10j8cu6rKFQYuuiWpQNPrnzM7v8oHZu%2BaRVOMYZRH1EazUKsQbkCgY5ylsLXdpyv8kf2H39uEtKGtz%2FefxRmRx9TiEVoFc7wa%2Fw8xWh1rd7y4VP0mGstKQPdDNaLR2GffWAQlOIklHS7Osf92MNFQjbV2GKCPGb%2BWbXFaYkaJyVqUPRKRajEfgAkgmkhEIxTvNAai3K%2FGOjrtYWXqW1WdpSk2A7zIwYMaGKseP2v%2FBICrrjbMAP2%2F9T5DXXEv7FJeg%2BitBhmzi9JGN0o8jbhUcJDT2Dm6FomN9ms782opSveYW2x0ft%2FE2k0ByER6mjnJTpfmkD1ZJBqzcmVvGXIcsC%2BmrpZavTWVlz%2FZgLMr6b3PQ5WRxvQg5AtpgyZWPmJkqyO8Tk3cQnsWeN87ZC9%2Bl8UVyRHobqM58Leki3ZiN%2BQz3SxX2%2BE0SyEyWZ7Gm4xYJQUevsisVWtDR2p9RSsjm4KKbK3HmqmcoTaAoumCsKa1ke222ON5keCjnqtkdk%2F07koplatkq76YhWO7%2FrlyATDX8bDPBjqkAbo6%2BzxltYtqgAW4I1%2FeUm8tR2mhEFJM%2FY06eBMpon68wN9EWtEmDbmN3Y5SENbYuC7ipQSR8hPKNHyf8s7XW%2BHxvY%2BOvf7wFycHfSQNJMO0uSvTYnmrpVCRSk3ibVX4NQ7qrCwMh4iA6TdAqqeCkLXjCOEKJgEu1R5UVHdOukfyS9ONwHAry5PX1XLoxM3eV5K80JErEzXbPEKFDErayRfyYjCB&X-Amz-Signature=f34365aa3f6e82775981d30916a775166b0d9d6c57c37648115f0309fb131550&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GHTR5NG%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3kp7LxTy9M0LAcK3MCtX6fjseR4Ed1%2FZEcu3Aaeiy%2FwIhALDJJSkhtWUISeMjU73wBatAA6rZ8ygIviWVwiN6A0qhKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BMz9GYM8F26BX78gq3AM3FJey%2FpKv3CqykjRQSYn23xXmyBA5EIdxqxsx%2FEp7mwSoHK7l4BC%2BDbgYTCryrO6M5%2F1LzvSUqDJSX6EYoXfuSJsQgFmF%2FahPpHz10j8cu6rKFQYuuiWpQNPrnzM7v8oHZu%2BaRVOMYZRH1EazUKsQbkCgY5ylsLXdpyv8kf2H39uEtKGtz%2FefxRmRx9TiEVoFc7wa%2Fw8xWh1rd7y4VP0mGstKQPdDNaLR2GffWAQlOIklHS7Osf92MNFQjbV2GKCPGb%2BWbXFaYkaJyVqUPRKRajEfgAkgmkhEIxTvNAai3K%2FGOjrtYWXqW1WdpSk2A7zIwYMaGKseP2v%2FBICrrjbMAP2%2F9T5DXXEv7FJeg%2BitBhmzi9JGN0o8jbhUcJDT2Dm6FomN9ms782opSveYW2x0ft%2FE2k0ByER6mjnJTpfmkD1ZJBqzcmVvGXIcsC%2BmrpZavTWVlz%2FZgLMr6b3PQ5WRxvQg5AtpgyZWPmJkqyO8Tk3cQnsWeN87ZC9%2Bl8UVyRHobqM58Leki3ZiN%2BQz3SxX2%2BE0SyEyWZ7Gm4xYJQUevsisVWtDR2p9RSsjm4KKbK3HmqmcoTaAoumCsKa1ke222ON5keCjnqtkdk%2F07koplatkq76YhWO7%2FrlyATDX8bDPBjqkAbo6%2BzxltYtqgAW4I1%2FeUm8tR2mhEFJM%2FY06eBMpon68wN9EWtEmDbmN3Y5SENbYuC7ipQSR8hPKNHyf8s7XW%2BHxvY%2BOvf7wFycHfSQNJMO0uSvTYnmrpVCRSk3ibVX4NQ7qrCwMh4iA6TdAqqeCkLXjCOEKJgEu1R5UVHdOukfyS9ONwHAry5PX1XLoxM3eV5K80JErEzXbPEKFDErayRfyYjCB&X-Amz-Signature=ee7d6b3e510fd4c103f936d3c93f5b82cc0e724032a05897576741c8b9063460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

