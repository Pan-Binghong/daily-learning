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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UK4FK46X%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAEAGcdWw73EP4cT7ZBVjhQD4mJ0BriPiJt9VqTICRdjAiB%2F4qEmEPeZYsg%2F4i6e27WVwVqcwD5Q7SzTwh2To%2Fvo4yqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb1Nz26o4sAxk72p%2FKtwD4b6egCKBtD1O8udOcDy1AfM9F49AnKs%2FFZX6aEbFTeQcjnofW3YruZ5FHMITozE1jzIeU3SwctiQmaqyj7LLIZEvMeqW2vAy%2ByrdM8yFo0AyKe%2B%2BzCs0McjoCKCmpyU6QMkK4oXvNKnmKXim%2FZH2r4xMLgI0mo%2B%2F9pPpVnk%2BPhswY0F08xc3aMfSTZvrNWfz1DaJxrWJ%2FjV2wGDfMJGOWLgWKUov%2Bbat1iSvWvXzifsoeBhtGiph7Y%2FaXvkHg4GkeBm8zjrb6iK1a%2BaxrJhBXTCR9gPCCQFusrfH4p82oNxBJM42412SWkR8I9ZG9GHPXdmAZ0Q2kVnnYom5hhXTMzyLB49Srejz%2F956qk82w%2F5PcxWqP09VYGVAfRtxF0wSv1V26WO3mxHsIXY4GCuGq7SlSHI9wppcPPFcUnXjKrXU3tvC6kz%2F7YV%2FDgK1IjReq3jZTDEcVHRXsoayNFE1DXf5fvfYfweOX7OD0AfMjz1cEhZGP9mvXgzxYlQX0nRPGc6%2FqjtYYijU5Cgm6WG7AW2kVaWjXVSL0sslq4GSZsoQNaH1BhQKJp71yEsPgfjA%2BMSvsKdbbaUP1JfzTyDQGmgMeSnpBYuR0eSIjrP2pZP4fsc6D3nd6yjK21swzPCWzgY6pgHzPxvhKHp9Y18SliRW2%2B0frFhtk8xVJLTtH%2B7jvHuaSGyVGbGdQXmVMvMBf5IlCTmWfq4evoMcBSbToRtJrpizbWGEwwCSGhOlFSPnvqjjdJMcjd0sKCuunjJZfF3nwb2czhvNgJ07uocv0iQ1ynH0zazQR3KvY3EYSUZKvsGVyH4agRl5aM3fq3v4H6TMDOZuW%2FSdJ%2FXThCdWw048qjqdg83XnCC8&X-Amz-Signature=5aabcbd7e1b7e05d6eb57a3618f97c7eacb256acc8cdeed5b3fedd02dec9e3e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UK4FK46X%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAEAGcdWw73EP4cT7ZBVjhQD4mJ0BriPiJt9VqTICRdjAiB%2F4qEmEPeZYsg%2F4i6e27WVwVqcwD5Q7SzTwh2To%2Fvo4yqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb1Nz26o4sAxk72p%2FKtwD4b6egCKBtD1O8udOcDy1AfM9F49AnKs%2FFZX6aEbFTeQcjnofW3YruZ5FHMITozE1jzIeU3SwctiQmaqyj7LLIZEvMeqW2vAy%2ByrdM8yFo0AyKe%2B%2BzCs0McjoCKCmpyU6QMkK4oXvNKnmKXim%2FZH2r4xMLgI0mo%2B%2F9pPpVnk%2BPhswY0F08xc3aMfSTZvrNWfz1DaJxrWJ%2FjV2wGDfMJGOWLgWKUov%2Bbat1iSvWvXzifsoeBhtGiph7Y%2FaXvkHg4GkeBm8zjrb6iK1a%2BaxrJhBXTCR9gPCCQFusrfH4p82oNxBJM42412SWkR8I9ZG9GHPXdmAZ0Q2kVnnYom5hhXTMzyLB49Srejz%2F956qk82w%2F5PcxWqP09VYGVAfRtxF0wSv1V26WO3mxHsIXY4GCuGq7SlSHI9wppcPPFcUnXjKrXU3tvC6kz%2F7YV%2FDgK1IjReq3jZTDEcVHRXsoayNFE1DXf5fvfYfweOX7OD0AfMjz1cEhZGP9mvXgzxYlQX0nRPGc6%2FqjtYYijU5Cgm6WG7AW2kVaWjXVSL0sslq4GSZsoQNaH1BhQKJp71yEsPgfjA%2BMSvsKdbbaUP1JfzTyDQGmgMeSnpBYuR0eSIjrP2pZP4fsc6D3nd6yjK21swzPCWzgY6pgHzPxvhKHp9Y18SliRW2%2B0frFhtk8xVJLTtH%2B7jvHuaSGyVGbGdQXmVMvMBf5IlCTmWfq4evoMcBSbToRtJrpizbWGEwwCSGhOlFSPnvqjjdJMcjd0sKCuunjJZfF3nwb2czhvNgJ07uocv0iQ1ynH0zazQR3KvY3EYSUZKvsGVyH4agRl5aM3fq3v4H6TMDOZuW%2FSdJ%2FXThCdWw048qjqdg83XnCC8&X-Amz-Signature=d8a8477ba845be58a143c37b0599528077aeed346d3dbc9deb2ef375e2ec9a90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

