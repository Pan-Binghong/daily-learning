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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG66ORA3%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEBvnurBpjTdC8NnFwcRtfJvUuGk3ioKaNPggxh3uafAiBZ9051y08ZmTSJwJEwcf6MvY2tvJOu4UEnDQSSPjwMiCqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBpE9F%2BsAl0seVVZTKtwDYPqzjiE7nWLo9Mwa0c7%2B6%2BeI8hybsDgcNDvO6X%2Bojt81V7LwLOkDxCAY1o4dK2Juxe9X6kbPp%2BV%2FDgUtK4OX%2FA8wi0sd530MoJ6emOJoslfB3oXSlMACIxtdNuMAedyFAb7%2FcBoFXL8UY1fxpBhBDDzpG5%2Bxjwyztj62UfBmcTUU4f%2FOC1z1WPkMdzUBWLY1U%2BDrHL%2FajXt23veBoCHqWpdgFR3C6TdrG7VUC%2B3sWO9z9hIyzJPCLoyvIp8sYIVIrGAj6atdLg2V74d9GgpzqRIuhJQh7e5%2FmadhwBS89%2FrtoKYdQ1mLOlgnQZHnzkrdBpOTNW1O4F0bb2s528b2Ue0NBlAf2xFDreXL1HALhZjT1s0FOluGwMBriVCiRRbaW%2FM%2BMT4XJQnVkS%2BTcqgewNBMydE6bILuov9EzelhfDSr7y0erq%2BALgueI0rV%2FH4pRbOpfsulFZ%2B3AAxLPghTfxOW8YiLVTkhpg93l3mqFlK5Tm9cSeQ2j%2BZ4yCHNVAA0OVhmGvxUDKc790X6J%2FkYYQQbjX6GZDxzAXdfKJrktvrJxhH3IvuQxy34PiNeBXDxrAsdL6ozNyXugOrQHgLM7WPIpkV6veldZwpuqZMJ3ZtS5Xi6x55BaAHTmmMwzp3HzgY6pgHqR2t1KlSXDeZ8Jzdmwgwk11GNqZploOX8L0u2bxmFsQHM5YbNzW4%2Bo%2Fh7cudspYvpSIjdcSPTEJ2ADW5k8lJvNlUPqLt5XNTn8NQMExr1yJ3YuGqUXkSjVTyw%2BJTbwjfMtMxPVPBoacrrH3nrgEnRYkZUBKaRovjy8RSVtJpapoaCWDevCsH3zEhW6WyvUTSLVU77WACoSaUUQaff8d7lz%2B5Wo9JF&X-Amz-Signature=606ba713d158f66618224bcfa634698f189ce9f76d9b7fdaa2ed1fa104edfb36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG66ORA3%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEBvnurBpjTdC8NnFwcRtfJvUuGk3ioKaNPggxh3uafAiBZ9051y08ZmTSJwJEwcf6MvY2tvJOu4UEnDQSSPjwMiCqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBpE9F%2BsAl0seVVZTKtwDYPqzjiE7nWLo9Mwa0c7%2B6%2BeI8hybsDgcNDvO6X%2Bojt81V7LwLOkDxCAY1o4dK2Juxe9X6kbPp%2BV%2FDgUtK4OX%2FA8wi0sd530MoJ6emOJoslfB3oXSlMACIxtdNuMAedyFAb7%2FcBoFXL8UY1fxpBhBDDzpG5%2Bxjwyztj62UfBmcTUU4f%2FOC1z1WPkMdzUBWLY1U%2BDrHL%2FajXt23veBoCHqWpdgFR3C6TdrG7VUC%2B3sWO9z9hIyzJPCLoyvIp8sYIVIrGAj6atdLg2V74d9GgpzqRIuhJQh7e5%2FmadhwBS89%2FrtoKYdQ1mLOlgnQZHnzkrdBpOTNW1O4F0bb2s528b2Ue0NBlAf2xFDreXL1HALhZjT1s0FOluGwMBriVCiRRbaW%2FM%2BMT4XJQnVkS%2BTcqgewNBMydE6bILuov9EzelhfDSr7y0erq%2BALgueI0rV%2FH4pRbOpfsulFZ%2B3AAxLPghTfxOW8YiLVTkhpg93l3mqFlK5Tm9cSeQ2j%2BZ4yCHNVAA0OVhmGvxUDKc790X6J%2FkYYQQbjX6GZDxzAXdfKJrktvrJxhH3IvuQxy34PiNeBXDxrAsdL6ozNyXugOrQHgLM7WPIpkV6veldZwpuqZMJ3ZtS5Xi6x55BaAHTmmMwzp3HzgY6pgHqR2t1KlSXDeZ8Jzdmwgwk11GNqZploOX8L0u2bxmFsQHM5YbNzW4%2Bo%2Fh7cudspYvpSIjdcSPTEJ2ADW5k8lJvNlUPqLt5XNTn8NQMExr1yJ3YuGqUXkSjVTyw%2BJTbwjfMtMxPVPBoacrrH3nrgEnRYkZUBKaRovjy8RSVtJpapoaCWDevCsH3zEhW6WyvUTSLVU77WACoSaUUQaff8d7lz%2B5Wo9JF&X-Amz-Signature=7112c4c022ef7390606e10377f63c8497638eb5f767a4650810a9e595fe1a01c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

