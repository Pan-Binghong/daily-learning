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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IS75ZVD%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQDjGk%2Flt%2Bo%2BDOR%2BNSPRBtIlZWr%2BYuu8PZiRFZRqih9sFQIhAIqa4vO0CAcJcKTiKt7IeSaJ6wLg%2FaDgBZZT36Gnlk77Kv8DCCwQABoMNjM3NDIzMTgzODA1Igz6q5%2FjNSeOWN2Aoa0q3AMW8mfzkdYhi%2BjLjey0xO09D70svO691slx1vnqMtiMOC0fKGRJLONK0ODWm0ntYOfJRJhkc43fZCfSmxNeg23BLuDXzUvjCHfAmqqEyykdp%2F6KmomlAgzD7uYFLXrzf0f6%2Bsp01AVp%2B71kU2RuX1P3FS1JVaOu1Pyss4XxeX%2FU0qNRDdVsjcZ7sL99Atdh66JyZYNK%2BeYraA%2FxckHgX0pL%2FDh3o%2Bv2s1hlzy58LzpaUzIJN%2BNaLIzVolDmF3J3raaPZunBgd8s6L60chT9XuC7BcEQkdF%2BKuNiESGm5Zxm9FnXWFYA7YZPlG6b24XARZ%2BglpB8E%2BW9%2Br2hEo6aiCEbhvQXFSEv2iOtCoMOZLfmvBf3%2F8EhVX8RpKjGOCNr%2BsMqorcFYSHXHP5c81Vf9tuRr3kn8xENdu6OAfE4T2K7f%2FcYMVJQoMOpzYv%2BIx8dz0q6MOzRbnhVjWirvrpTM58S2XPhHXUy2KMV9acsSJFveH4Z%2Ba7uc%2F4I%2Fs%2BhndQpZFSi3AxHm%2F40pa77ticUKgEAyCC3j5WPglLY1ePwK2PnG0iIz%2FxVHVr92QewRusvFcnJevtqTqcDrgzNR7NOWD%2BaN6bgLZk%2FEQNi3Z17CXKuQKV5qDqwmxnf4xAQETCH1JvPBjqkASX4vFlaoG1VuFT9xlQ3v3cArqUtzT3uwASSE%2BxLb3naT25pnJnpEZgQnMQJM92KZnGy7kKPgOHoXc9jqNZaLv58cSIzK4yQonU7rEJC%2BYLX0itPyGDttl4IW%2BKOWnLQhduX9Zv%2BymjlX7Ue2liukjncwU8DKcdxaYYU%2B9GsWxOdR8mCxuWQ926MEM%2BujXfmFj4YktnG4jvXe8ODsM39srNPuxYO&X-Amz-Signature=460142bcf29ef44ca1b510069fe25da006e5d459e5964f443e3bce02667c6f9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IS75ZVD%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQDjGk%2Flt%2Bo%2BDOR%2BNSPRBtIlZWr%2BYuu8PZiRFZRqih9sFQIhAIqa4vO0CAcJcKTiKt7IeSaJ6wLg%2FaDgBZZT36Gnlk77Kv8DCCwQABoMNjM3NDIzMTgzODA1Igz6q5%2FjNSeOWN2Aoa0q3AMW8mfzkdYhi%2BjLjey0xO09D70svO691slx1vnqMtiMOC0fKGRJLONK0ODWm0ntYOfJRJhkc43fZCfSmxNeg23BLuDXzUvjCHfAmqqEyykdp%2F6KmomlAgzD7uYFLXrzf0f6%2Bsp01AVp%2B71kU2RuX1P3FS1JVaOu1Pyss4XxeX%2FU0qNRDdVsjcZ7sL99Atdh66JyZYNK%2BeYraA%2FxckHgX0pL%2FDh3o%2Bv2s1hlzy58LzpaUzIJN%2BNaLIzVolDmF3J3raaPZunBgd8s6L60chT9XuC7BcEQkdF%2BKuNiESGm5Zxm9FnXWFYA7YZPlG6b24XARZ%2BglpB8E%2BW9%2Br2hEo6aiCEbhvQXFSEv2iOtCoMOZLfmvBf3%2F8EhVX8RpKjGOCNr%2BsMqorcFYSHXHP5c81Vf9tuRr3kn8xENdu6OAfE4T2K7f%2FcYMVJQoMOpzYv%2BIx8dz0q6MOzRbnhVjWirvrpTM58S2XPhHXUy2KMV9acsSJFveH4Z%2Ba7uc%2F4I%2Fs%2BhndQpZFSi3AxHm%2F40pa77ticUKgEAyCC3j5WPglLY1ePwK2PnG0iIz%2FxVHVr92QewRusvFcnJevtqTqcDrgzNR7NOWD%2BaN6bgLZk%2FEQNi3Z17CXKuQKV5qDqwmxnf4xAQETCH1JvPBjqkASX4vFlaoG1VuFT9xlQ3v3cArqUtzT3uwASSE%2BxLb3naT25pnJnpEZgQnMQJM92KZnGy7kKPgOHoXc9jqNZaLv58cSIzK4yQonU7rEJC%2BYLX0itPyGDttl4IW%2BKOWnLQhduX9Zv%2BymjlX7Ue2liukjncwU8DKcdxaYYU%2B9GsWxOdR8mCxuWQ926MEM%2BujXfmFj4YktnG4jvXe8ODsM39srNPuxYO&X-Amz-Signature=922e2ee4d8bf1aa769acffe8a67e5e2cbee4e5d9f1b5dccb53fafae754af7542&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

