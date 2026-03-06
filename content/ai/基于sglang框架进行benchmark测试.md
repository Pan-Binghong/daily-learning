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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7W47CU4%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIHYRbnL%2BFGmuIO9R7GKgrWEsHVhaa3WsYBM4EpqairdTAiEAlW2HblEEK49FOluVWCnmWsEbTAtxuekV5imfRW2CISkqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP0tVNUhpNvzwuulZSrcA7LSiubXQvNsV4DixzwBJ6p%2FHJaSn6YjzbKFwkhQds5aa%2F0llpw%2F66JHdahVKMpnVvetj0OckyG7cA1FBVY1CADjO3KXNgpbLg3%2BCSc83d2b6e7b64AJvuZ0sogzhwazNibXuC5z6lnDvyITP5ONVFTHdyVQMNmd2s3yR7UVYVkw46c4qIzwLjriDV%2FGkYQzT4syR%2F2NRi6043q9TenrhLUR88ly1OsW5yvrdwAL5k%2FI6a1vURThjY3zig0Hrrm9o63cLy9qpQOsUoMlwJ4nO63grVRJdd%2BXPFGYtOFuuVd09U44hgSZm5SnvMOrqTQc1uw1BRX7x9LWmIk4HD6HJflatA9mdJI3SwFi0SHyoUwZRlik51NiRyyHqbdxACznxzoeXgmjGEs60yHSVxw%2Fcqw5xouSUD%2BZqqDbGBf5mqKjQd7AweQvDKdgf0vBWkb1BXFI4EZ9rD2DaOjemxSP%2BTXuOgKsVRo8h%2B9j%2BfqoMBpZx4hGkGglAi4aa8oXbjxFAoLY5oyYMOkww0daJoe2hetyXQW9oTPaBhhOUJn4o31e%2FWIBdDyxICv8HVaw0yqKEgH2q7YgrUBAWMdt%2BmPe3Klur6ZTklBPlBMBDq2XWqopqgzXRU9LyUPYMyuzMPHPqM0GOqUBKk2pZ4r0JwXdXp7MRKtYkySSHzEPyFjLpRqomFuxMsEnLhDEugieNjtkxHwreamiY2x74j%2BdS6emmzr6FEF5ZwrZ7%2F0uawm7NN3ESR1Cb1O20vyXIliMjguXP8lZzoLSR2CvFILmNOVkMLKRrIuRQmYvT%2Bs85CMFfjXLAzEcokO0rbuLeJlAs5x7qjjidNh3ISONFAMjZnTzy38Hrjsq0aNvAw1k&X-Amz-Signature=cbba4dec1a8f8ce65dee80f334df91206a68b5f1de53326a40b7b3e69c1acd00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7W47CU4%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIHYRbnL%2BFGmuIO9R7GKgrWEsHVhaa3WsYBM4EpqairdTAiEAlW2HblEEK49FOluVWCnmWsEbTAtxuekV5imfRW2CISkqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP0tVNUhpNvzwuulZSrcA7LSiubXQvNsV4DixzwBJ6p%2FHJaSn6YjzbKFwkhQds5aa%2F0llpw%2F66JHdahVKMpnVvetj0OckyG7cA1FBVY1CADjO3KXNgpbLg3%2BCSc83d2b6e7b64AJvuZ0sogzhwazNibXuC5z6lnDvyITP5ONVFTHdyVQMNmd2s3yR7UVYVkw46c4qIzwLjriDV%2FGkYQzT4syR%2F2NRi6043q9TenrhLUR88ly1OsW5yvrdwAL5k%2FI6a1vURThjY3zig0Hrrm9o63cLy9qpQOsUoMlwJ4nO63grVRJdd%2BXPFGYtOFuuVd09U44hgSZm5SnvMOrqTQc1uw1BRX7x9LWmIk4HD6HJflatA9mdJI3SwFi0SHyoUwZRlik51NiRyyHqbdxACznxzoeXgmjGEs60yHSVxw%2Fcqw5xouSUD%2BZqqDbGBf5mqKjQd7AweQvDKdgf0vBWkb1BXFI4EZ9rD2DaOjemxSP%2BTXuOgKsVRo8h%2B9j%2BfqoMBpZx4hGkGglAi4aa8oXbjxFAoLY5oyYMOkww0daJoe2hetyXQW9oTPaBhhOUJn4o31e%2FWIBdDyxICv8HVaw0yqKEgH2q7YgrUBAWMdt%2BmPe3Klur6ZTklBPlBMBDq2XWqopqgzXRU9LyUPYMyuzMPHPqM0GOqUBKk2pZ4r0JwXdXp7MRKtYkySSHzEPyFjLpRqomFuxMsEnLhDEugieNjtkxHwreamiY2x74j%2BdS6emmzr6FEF5ZwrZ7%2F0uawm7NN3ESR1Cb1O20vyXIliMjguXP8lZzoLSR2CvFILmNOVkMLKRrIuRQmYvT%2Bs85CMFfjXLAzEcokO0rbuLeJlAs5x7qjjidNh3ISONFAMjZnTzy38Hrjsq0aNvAw1k&X-Amz-Signature=6eb23e614eb4b658ac651f02a9bb86509fe20a1b80f9bf9edb3d4891281887d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

