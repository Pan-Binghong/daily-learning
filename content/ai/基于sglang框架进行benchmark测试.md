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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCPAGMAR%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQC7Bb4doOTU54tQetEqMJT51bUADN2RzsiUeOz7XVi7QgIhANiF8bFts4UbLCrXxWo83kLfbdzhdBH4W8XODZFFzbLLKv8DCEUQABoMNjM3NDIzMTgzODA1IgzJRToAW8ZZvTziHmYq3AMCjyLKUg%2BftMpqMC5nxAX9Ij4a7pfKNmu6KzWw5XvlfRdXwFgNo2umkKcKGgsnN6Rkskgz717e5zEhPC5I678tc4oBG0HFVoPE8TJ6hlhqXMuAnHQR6I340gAVwC%2FwjeozG068GYOYKvWTUJlP46tIcJTv6DDAKciaVPfR6yItgxh%2BV6I5PTF4jSSnRFcBfCxa%2BsU2anC%2F73eb7y0Jnzp9ei33Aeu1LljAN2sPm4HMElQzpCYVOMDq3wZlQ5IRVDPrILqrD1XdW2keFXFb1JnxhPrVmFaGQpdeqyLsJk7j2goPlILdGozfuqhBdMWg%2BAPIOHE9bCmDXe6BrQ9UnL638da6ptgwGiteOlrDg7YjZly%2BowBY4PCXtM2tBxJjP6tn839A6gYBO1vSjRYcYCQPIy0zBARNKqA9EPMAKDetVlWrcqV%2BOcy%2FzYB0NTKOqR68J0lDSwAPIeuwBlOsjAVPjvmmoWkWRfmILpCMQO4D68tv4cly0Yo5j5ziGMpDGXRxSRVrQbL3GTnbgZJTOxHyP6b2JP05OopgmTlCcidTNz2zBfOncH6CfLNRbGLdviiTBCpzkkxbWmh3JCnu85AmZ9xdnGVVfl1a2%2BKg0cx3NBJxK6F5AhfBaeizyzC7v8%2FMBjqkAZKj6N0YgK8wuuhSjBGO%2BqqAX8%2FT65hliwFiuh15I8Hnq6Q1bGeVy2lh7BfpPcgpjs2YlP%2BkpPfLX4mbF45JNlRyZa7muCOLbPDQrzFBD0s0ybc5c5isXnT6zm6jIeECg8P0INUsFmHXDt8fSXWDMvWkTFcxDEramcf5WYL9lF78uCLBILUQGwNQIYUTgKpofey1AVaNZ8zZN1X2idF%2F3B3oFhHK&X-Amz-Signature=6120d7dc2e8eefd869467c0ec18c588d070d014daa927f142c056ff49b9c0a2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCPAGMAR%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQC7Bb4doOTU54tQetEqMJT51bUADN2RzsiUeOz7XVi7QgIhANiF8bFts4UbLCrXxWo83kLfbdzhdBH4W8XODZFFzbLLKv8DCEUQABoMNjM3NDIzMTgzODA1IgzJRToAW8ZZvTziHmYq3AMCjyLKUg%2BftMpqMC5nxAX9Ij4a7pfKNmu6KzWw5XvlfRdXwFgNo2umkKcKGgsnN6Rkskgz717e5zEhPC5I678tc4oBG0HFVoPE8TJ6hlhqXMuAnHQR6I340gAVwC%2FwjeozG068GYOYKvWTUJlP46tIcJTv6DDAKciaVPfR6yItgxh%2BV6I5PTF4jSSnRFcBfCxa%2BsU2anC%2F73eb7y0Jnzp9ei33Aeu1LljAN2sPm4HMElQzpCYVOMDq3wZlQ5IRVDPrILqrD1XdW2keFXFb1JnxhPrVmFaGQpdeqyLsJk7j2goPlILdGozfuqhBdMWg%2BAPIOHE9bCmDXe6BrQ9UnL638da6ptgwGiteOlrDg7YjZly%2BowBY4PCXtM2tBxJjP6tn839A6gYBO1vSjRYcYCQPIy0zBARNKqA9EPMAKDetVlWrcqV%2BOcy%2FzYB0NTKOqR68J0lDSwAPIeuwBlOsjAVPjvmmoWkWRfmILpCMQO4D68tv4cly0Yo5j5ziGMpDGXRxSRVrQbL3GTnbgZJTOxHyP6b2JP05OopgmTlCcidTNz2zBfOncH6CfLNRbGLdviiTBCpzkkxbWmh3JCnu85AmZ9xdnGVVfl1a2%2BKg0cx3NBJxK6F5AhfBaeizyzC7v8%2FMBjqkAZKj6N0YgK8wuuhSjBGO%2BqqAX8%2FT65hliwFiuh15I8Hnq6Q1bGeVy2lh7BfpPcgpjs2YlP%2BkpPfLX4mbF45JNlRyZa7muCOLbPDQrzFBD0s0ybc5c5isXnT6zm6jIeECg8P0INUsFmHXDt8fSXWDMvWkTFcxDEramcf5WYL9lF78uCLBILUQGwNQIYUTgKpofey1AVaNZ8zZN1X2idF%2F3B3oFhHK&X-Amz-Signature=b92ded3e8130f8642ecf183e02f42ef24431dd40aa3e589f1357fb7eddfb1e4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

