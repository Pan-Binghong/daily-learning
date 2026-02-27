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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UAXVQHA%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDOibN9yG0ENY6fjG8b1iqV%2B280zedOsI2ysJNo%2Fo23zQIhAIq44DDBqoRw91YxYd1SxPBY1VrlBiUaiZzqp22XGbJ%2BKv8DCDQQABoMNjM3NDIzMTgzODA1IgycCuOQkRw1%2Bvas6hcq3AOt46eknTCqOKcnN6xMn9I73DbWQNaOoh4Efkcs7uq%2F%2Fug7ow7YYxq0hbxzcIKEyiba%2BAc8x6%2FWP8zYd6Q1TBzaUSYxW%2B4sVVUcPPxrHVL77uJydtkMr45%2B5%2FcClQSiN4TrErXWmFAgpnh5M2LVpEy%2FhmaX6GaWPDV%2FqgyTWrZE%2B16j1Bsiw2amKvM8H%2BTEG16zeFHRZpP8xXIuMXftP198Q8%2B5LH4AAKwbT0iNfzCBc9YGwLim7xf73ATEWS6EfPH3CTECkYP1I%2FoJtCR6CI%2FMujlMQaqtHEElMiWL8h7NNpBRlIPZhW0yIJjrOOojyyokyWN%2BNcRLyyGeNt7xhlu941pqt6TnnS0vat%2FRNkf%2Fo%2FipWeLLKFmKEQ2RZmhO64dKgNWUF0WMRdOloIbhkFIX5l4T4Gym1sfuqm9ccefpQv6EvCF%2BRbHXBQMwcIvR6%2BhoAOiOaUz7RNYrOsADB1TNfE1LTu3xb3gkdLyQT6mOYVqgqpGROrwrinlhc7Fhe654oz25icj63PsMPEl2Lx%2BIyaaInNWNWZxLSUdYb6ie3gqNk%2FGJUAuAFmlSsem%2BDhJMSWxxE8KHK%2FmCOHcmEdjEnzpIOjG%2Ftf0h6ozXkX6HPAZl8%2FixNRQ7kZhQYTDmhYTNBjqkAf2I6E8E9ynHQcI6W8FaWmXFLO2GMZiOdR8wPU6IbJ%2BsmJnF8fpqZeYBQ4jTAYpZ9e70SiM54OgDyhJstqNkWewLgtON7elv0w3diM64pJMBWTFXE9TZEQ5hm64uDls8CK7MyJphsSF%2FrlE2rdTbEAf9I3UU45vOC2rsYMW5yO6gziavV6RNqP13aTcwpEsqJFMTKD%2FgHLwxmnze1eMxxGIIMOV5&X-Amz-Signature=66635dc1f6fbc9e38e6baad02275d09055cbd642ce41b9df1366b33155d66918&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UAXVQHA%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDOibN9yG0ENY6fjG8b1iqV%2B280zedOsI2ysJNo%2Fo23zQIhAIq44DDBqoRw91YxYd1SxPBY1VrlBiUaiZzqp22XGbJ%2BKv8DCDQQABoMNjM3NDIzMTgzODA1IgycCuOQkRw1%2Bvas6hcq3AOt46eknTCqOKcnN6xMn9I73DbWQNaOoh4Efkcs7uq%2F%2Fug7ow7YYxq0hbxzcIKEyiba%2BAc8x6%2FWP8zYd6Q1TBzaUSYxW%2B4sVVUcPPxrHVL77uJydtkMr45%2B5%2FcClQSiN4TrErXWmFAgpnh5M2LVpEy%2FhmaX6GaWPDV%2FqgyTWrZE%2B16j1Bsiw2amKvM8H%2BTEG16zeFHRZpP8xXIuMXftP198Q8%2B5LH4AAKwbT0iNfzCBc9YGwLim7xf73ATEWS6EfPH3CTECkYP1I%2FoJtCR6CI%2FMujlMQaqtHEElMiWL8h7NNpBRlIPZhW0yIJjrOOojyyokyWN%2BNcRLyyGeNt7xhlu941pqt6TnnS0vat%2FRNkf%2Fo%2FipWeLLKFmKEQ2RZmhO64dKgNWUF0WMRdOloIbhkFIX5l4T4Gym1sfuqm9ccefpQv6EvCF%2BRbHXBQMwcIvR6%2BhoAOiOaUz7RNYrOsADB1TNfE1LTu3xb3gkdLyQT6mOYVqgqpGROrwrinlhc7Fhe654oz25icj63PsMPEl2Lx%2BIyaaInNWNWZxLSUdYb6ie3gqNk%2FGJUAuAFmlSsem%2BDhJMSWxxE8KHK%2FmCOHcmEdjEnzpIOjG%2Ftf0h6ozXkX6HPAZl8%2FixNRQ7kZhQYTDmhYTNBjqkAf2I6E8E9ynHQcI6W8FaWmXFLO2GMZiOdR8wPU6IbJ%2BsmJnF8fpqZeYBQ4jTAYpZ9e70SiM54OgDyhJstqNkWewLgtON7elv0w3diM64pJMBWTFXE9TZEQ5hm64uDls8CK7MyJphsSF%2FrlE2rdTbEAf9I3UU45vOC2rsYMW5yO6gziavV6RNqP13aTcwpEsqJFMTKD%2FgHLwxmnze1eMxxGIIMOV5&X-Amz-Signature=9aa972e41ad2093caf3741d96391d799bc4d57db230775727a1dceb54417bbad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

