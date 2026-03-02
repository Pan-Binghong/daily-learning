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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VIVIYLA%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxWZKVr%2FjSSYsd0xnh6O8lY19K%2FH4E7Qm9Cp%2Foc3pViAiEAuDZisY1kbQSiqwGWNSIu8EJTpvyeJbCDdBKlwYD9POMq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDGFGOW8tEJEd0hZILircA1AteMbjvlsMKIwSmhpg5yP%2F8DCQztpuGR%2FuDJa7KyZjFqr2Edf62psFIml6SQLrRm%2BRvLvOKua32wNuQLkjbTfuR1EEnuOOsIDvNcUeWrKf%2BPPSlteSSUtXCIoH954sw17v0PcgGY8rUXdZUyF6d85pZYtfAFq9IwEq4VlT0JDhTMuzP1huEi0UxVliZHMyyl4IuyjYBRX7anBSCVODgLn3tPlEjMvRU%2BV6wVULF3RVFTrmuZZlTBIMk7molnZnNsz28JES%2F454pKN9q8KvXa21IDI6rg4%2Fak5Z0szRsKj29eSESQDGgMtSHz3dFWPPPm0Gr%2B%2Fnc1gCXhHxbQB3Jz67iIm%2FHQPcG4PuIYFBARsaE52X3%2FWs7Pv9NITI9Y35tlIXl5IoRjhvQAolqfBIaXUL0NZziz465WUq7G3lrFZJsqqlxRALPPLP9hqfzyI6ij0kIRzOm7y90uYEwsbo0CHTchMgdaHop1k52krh0FGGQRExm6mGEPjLwygHr9s2W3UCvQmnPgsJ9M2ShwBFGPZdwTHzbjycVvRyKeQE7lVFu7Sg0zK0nz3Z9KAL4JVOxaIPAf9Mz3J0KZ%2BOPZpd3o5%2BSxCFpwfDbET0vANgTLWvLXCoAITGb3g%2BLZFdMKX9k80GOqUB9v4sR%2FV7VMN6iF9%2FH6Q0hN6rVRYZFrosfFZHNP%2B79AXclWdVc0rnj%2FZqLoql8dqNBLKvm%2BH%2BxjVKi9lveXphAf9afqGx71dJCDVseUJTjg%2BA2Zsia5od6SwYrdQ4TyOoWngAV2ldowmEtxPL8%2BBdX7OSyZh2FIvJN7on1lVTwuz8v3mB5vg3dCgLCnnHWnUoKiViJlkbCD309mcEd85EguQJFVSj&X-Amz-Signature=954ff19f11b3eb97d5cabf5de56da2c7aaa6b565c26347748efc1297b5f44291&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VIVIYLA%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxWZKVr%2FjSSYsd0xnh6O8lY19K%2FH4E7Qm9Cp%2Foc3pViAiEAuDZisY1kbQSiqwGWNSIu8EJTpvyeJbCDdBKlwYD9POMq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDGFGOW8tEJEd0hZILircA1AteMbjvlsMKIwSmhpg5yP%2F8DCQztpuGR%2FuDJa7KyZjFqr2Edf62psFIml6SQLrRm%2BRvLvOKua32wNuQLkjbTfuR1EEnuOOsIDvNcUeWrKf%2BPPSlteSSUtXCIoH954sw17v0PcgGY8rUXdZUyF6d85pZYtfAFq9IwEq4VlT0JDhTMuzP1huEi0UxVliZHMyyl4IuyjYBRX7anBSCVODgLn3tPlEjMvRU%2BV6wVULF3RVFTrmuZZlTBIMk7molnZnNsz28JES%2F454pKN9q8KvXa21IDI6rg4%2Fak5Z0szRsKj29eSESQDGgMtSHz3dFWPPPm0Gr%2B%2Fnc1gCXhHxbQB3Jz67iIm%2FHQPcG4PuIYFBARsaE52X3%2FWs7Pv9NITI9Y35tlIXl5IoRjhvQAolqfBIaXUL0NZziz465WUq7G3lrFZJsqqlxRALPPLP9hqfzyI6ij0kIRzOm7y90uYEwsbo0CHTchMgdaHop1k52krh0FGGQRExm6mGEPjLwygHr9s2W3UCvQmnPgsJ9M2ShwBFGPZdwTHzbjycVvRyKeQE7lVFu7Sg0zK0nz3Z9KAL4JVOxaIPAf9Mz3J0KZ%2BOPZpd3o5%2BSxCFpwfDbET0vANgTLWvLXCoAITGb3g%2BLZFdMKX9k80GOqUB9v4sR%2FV7VMN6iF9%2FH6Q0hN6rVRYZFrosfFZHNP%2B79AXclWdVc0rnj%2FZqLoql8dqNBLKvm%2BH%2BxjVKi9lveXphAf9afqGx71dJCDVseUJTjg%2BA2Zsia5od6SwYrdQ4TyOoWngAV2ldowmEtxPL8%2BBdX7OSyZh2FIvJN7on1lVTwuz8v3mB5vg3dCgLCnnHWnUoKiViJlkbCD309mcEd85EguQJFVSj&X-Amz-Signature=56aa4de1eb7ea3a0683babcacc837922559e5bb6b1c9f758ffc78fa69302b5c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

