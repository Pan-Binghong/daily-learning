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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBXBVEMW%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFrrH34RZMBnBZLKICcBWbKozErKMR9dZWfMHNz%2FSKDAiBnz8rRNz9hQDguyh5Fi0ArFUlJlvoRIFag08xItAzmmSqIBAiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMABOo30HavuaUTWUMKtwDe8fdZbJob2o%2FQ3XOXfMugxFH7af3hSa%2BtQp15nL4ktTSmkHP1y4jE8XTFD0dxA%2Bx6g9eyZyLTsONuWlQ1hjdKfN%2BqLvcs9YP%2FAsVYg9KbGxBunNSkcexP6FuJ7PrWkAHeTKC3A%2FXQhnpz8eeylFFlDRXE7FXb%2BPUJ0hY9vHlgImduj5ZGUhFgGRPVI549Yg1PW5RT6qVMz%2BRfzgslbgZxkXNNB8rJnyXfjgIpzM29UeJFK4rF6kcoDUZEa7FQNWzUs9jT5Ho2UW9u8IxfIxRlvvYdCWicIPw3pstXmTFHQTGuBKDbsAqvE8r710Oap8R3Yh8LlJxogVRgGb1bIv9FxZr3ZJRFoD1lACqZNw6W1PZSjzaXPVgQdU3LRjqOghdyk8WrLSeYUESQl5dAbrpvPRc6PdcGb8dnIAS7DP3DUfB%2F2xrRN0DEVHk6XJtajrG1dE1ACP0Glh57ef66cy8LGOKAA2vKsXkSubypJRxR9iThibEGH8xg9s1%2B2j971Mal6YcI%2FvjA1iyPpk3HkGXK5IRa7Vo19Fv8pZdOmaphN2pxMS2lUqak%2FmVW07ot45IikVfupJyYiUGG8OCiWvFma2DC5IaXONUKsMJZfx5VBBF10G8n0bdFwoUZKkwq8rwywY6pgEpiZZzarYiKGCj3%2FebFiXHoeppcRDcDY32xFwMA4VUAZ7wNcK170TqhZSSvraoTNF7Z%2FNPSMjolmyfZTQXPmisonTRpFqr7l3JmohJ%2BhjMkRU%2BJrxqcwadCGGaCTsnICeBUVjQ5WAe71OBJSEcz7uoBl9wtGgyOObbGNjgepIqpN5%2FAHoW3RbseUQDfN6jxv6g3sH03JMXUXGty4qBmQJB6kCQS%2BiL&X-Amz-Signature=f6548ac2a01ff80c21d5f53c3b8d5b78bd7024e50e2b1f9f723399321da65c87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBXBVEMW%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFrrH34RZMBnBZLKICcBWbKozErKMR9dZWfMHNz%2FSKDAiBnz8rRNz9hQDguyh5Fi0ArFUlJlvoRIFag08xItAzmmSqIBAiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMABOo30HavuaUTWUMKtwDe8fdZbJob2o%2FQ3XOXfMugxFH7af3hSa%2BtQp15nL4ktTSmkHP1y4jE8XTFD0dxA%2Bx6g9eyZyLTsONuWlQ1hjdKfN%2BqLvcs9YP%2FAsVYg9KbGxBunNSkcexP6FuJ7PrWkAHeTKC3A%2FXQhnpz8eeylFFlDRXE7FXb%2BPUJ0hY9vHlgImduj5ZGUhFgGRPVI549Yg1PW5RT6qVMz%2BRfzgslbgZxkXNNB8rJnyXfjgIpzM29UeJFK4rF6kcoDUZEa7FQNWzUs9jT5Ho2UW9u8IxfIxRlvvYdCWicIPw3pstXmTFHQTGuBKDbsAqvE8r710Oap8R3Yh8LlJxogVRgGb1bIv9FxZr3ZJRFoD1lACqZNw6W1PZSjzaXPVgQdU3LRjqOghdyk8WrLSeYUESQl5dAbrpvPRc6PdcGb8dnIAS7DP3DUfB%2F2xrRN0DEVHk6XJtajrG1dE1ACP0Glh57ef66cy8LGOKAA2vKsXkSubypJRxR9iThibEGH8xg9s1%2B2j971Mal6YcI%2FvjA1iyPpk3HkGXK5IRa7Vo19Fv8pZdOmaphN2pxMS2lUqak%2FmVW07ot45IikVfupJyYiUGG8OCiWvFma2DC5IaXONUKsMJZfx5VBBF10G8n0bdFwoUZKkwq8rwywY6pgEpiZZzarYiKGCj3%2FebFiXHoeppcRDcDY32xFwMA4VUAZ7wNcK170TqhZSSvraoTNF7Z%2FNPSMjolmyfZTQXPmisonTRpFqr7l3JmohJ%2BhjMkRU%2BJrxqcwadCGGaCTsnICeBUVjQ5WAe71OBJSEcz7uoBl9wtGgyOObbGNjgepIqpN5%2FAHoW3RbseUQDfN6jxv6g3sH03JMXUXGty4qBmQJB6kCQS%2BiL&X-Amz-Signature=78db3c978e66f9c41fbac6dd00ac0c7338a772c2246e1fc4d4a8d26a4867f99e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

