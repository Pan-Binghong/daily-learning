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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWSRDZD7%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmNUBJ4VENw20iYgiu%2BUmP0xkA81eepOWJxnzOTpch8AIhAKa9pfPx3UnUOvW0JulsdiQyae6Hq%2BurLF32UZy9jcNuKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxU3n53KzZ5FnV%2BvYkq3APv0wbONXt0FQVkzU6wO0jJu9DhhjpBsshm1W0KmW4YagbPCKFJPTATVpLJDsPJMxVAspq6UQmZ2Uh1xuDnBtD1Ug2oodS9%2FUAIskMXrDyrCfZAeWSe4vZSN4naSC9w9NG06LG9VyOMdlWpxgk1%2BhDUeq0xd0qh%2BShzS17%2Bel8y3JgBP9yUaw8IhhPOKrZTq4EjQVSOialt%2FgnqeJV1XHHdzVR4A3%2FrP3Lf7pSt0FD74s0372xvxhVx5n5ILqc1VVTfED3QfxbOhlrlZUvRYdgqJ9TtpgRI%2F1rud2%2F4cSGbmf7JQ2L3lxF98bTdTyNN1abhNiFCWjq6%2Bh%2BMmQ2no4jdvfpghTQotH825PKL0pCJjP5Fq9kYsx7M4pM3MY5ICjzzntOyXX6Pp%2FYYBANBBjVGm%2FqICTckEy3AbAj4d90n6CqKOP%2FeVRHU1t9QiYUowy16cPv%2Furz%2BdYNgrrLLS%2BnjSpBNI7xli5B1L9Vsy9E9oVxevMIfO4ws0IWRGpCFJqFJPnnlu9ax9UY9qclqNYLhRTxOHmP6YgiM%2Bbh1LoWg1BxlQazYR9gyUulydHQkHqy6KvKVZhry12xw7WRNuEtwmK%2FjFIq%2FFcgXAd7L%2BCtKiKG0QhqLQwOLkmbmxzDKvOTMBjqkAYMD4TBvrVJXgB1Og0QPuvtFwhStiU%2FpyhF%2Bv1OJe3TFKq3fxXmL8Z0EAFtChyz%2FN%2FJVf6WcCow6DPN9W7HLlPbxpeMd4n%2FfgiWa4o6rFeQ7Nh114fcP0F%2FAWuglmybX9PRPQaH6mkVLtDkPJPQaPkXoTznVmA21BFd5yqAzrR2WU5bzYIKpd6hU8XZKTicKxCBtlegbN51FEWVGSzcqphG9rVfJ&X-Amz-Signature=421fb860edf5e172f48a8fdd1237aee65284de5d90700cdcd9f1f03c32cd8f17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWSRDZD7%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmNUBJ4VENw20iYgiu%2BUmP0xkA81eepOWJxnzOTpch8AIhAKa9pfPx3UnUOvW0JulsdiQyae6Hq%2BurLF32UZy9jcNuKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxU3n53KzZ5FnV%2BvYkq3APv0wbONXt0FQVkzU6wO0jJu9DhhjpBsshm1W0KmW4YagbPCKFJPTATVpLJDsPJMxVAspq6UQmZ2Uh1xuDnBtD1Ug2oodS9%2FUAIskMXrDyrCfZAeWSe4vZSN4naSC9w9NG06LG9VyOMdlWpxgk1%2BhDUeq0xd0qh%2BShzS17%2Bel8y3JgBP9yUaw8IhhPOKrZTq4EjQVSOialt%2FgnqeJV1XHHdzVR4A3%2FrP3Lf7pSt0FD74s0372xvxhVx5n5ILqc1VVTfED3QfxbOhlrlZUvRYdgqJ9TtpgRI%2F1rud2%2F4cSGbmf7JQ2L3lxF98bTdTyNN1abhNiFCWjq6%2Bh%2BMmQ2no4jdvfpghTQotH825PKL0pCJjP5Fq9kYsx7M4pM3MY5ICjzzntOyXX6Pp%2FYYBANBBjVGm%2FqICTckEy3AbAj4d90n6CqKOP%2FeVRHU1t9QiYUowy16cPv%2Furz%2BdYNgrrLLS%2BnjSpBNI7xli5B1L9Vsy9E9oVxevMIfO4ws0IWRGpCFJqFJPnnlu9ax9UY9qclqNYLhRTxOHmP6YgiM%2Bbh1LoWg1BxlQazYR9gyUulydHQkHqy6KvKVZhry12xw7WRNuEtwmK%2FjFIq%2FFcgXAd7L%2BCtKiKG0QhqLQwOLkmbmxzDKvOTMBjqkAYMD4TBvrVJXgB1Og0QPuvtFwhStiU%2FpyhF%2Bv1OJe3TFKq3fxXmL8Z0EAFtChyz%2FN%2FJVf6WcCow6DPN9W7HLlPbxpeMd4n%2FfgiWa4o6rFeQ7Nh114fcP0F%2FAWuglmybX9PRPQaH6mkVLtDkPJPQaPkXoTznVmA21BFd5yqAzrR2WU5bzYIKpd6hU8XZKTicKxCBtlegbN51FEWVGSzcqphG9rVfJ&X-Amz-Signature=31618732135aa340c2ebb23925acaa97511546c24735248eca50e42aa3a3ca33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

