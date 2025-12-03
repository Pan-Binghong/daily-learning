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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VETO3AEU%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCfu0RoDpvjYHE5TJQNfGFwX09DRqhrn6ldmk1ZgPsN8QIhAJmVzymrsKWJtscpM%2B8POSZeUrezHsUAIr6Ghx11W7h1Kv8DCCIQABoMNjM3NDIzMTgzODA1IgzudEv%2FQ69fIdn%2BYj4q3AMu7WsjeRBqUK9iv2p8OpOMXIP%2BZoNNrN2TZN99v6u6CtkBn2xPeGQW4wAFMKG1%2BJvmIOkLMmaCcgWkZR8NonsfG36pbN0EU3uPd0uSvgN4ED1k3m%2BaFUtgJjD8QzoR1qnd5xXRvog%2FpK9Txrz8ICT1QbnyWxKgt0uelLgkaJ1TizelTej6o4F3eqvTwb4bOEZpAD6cRlRVDCcRrKdwM8%2BUehF2Pl7ebVFXtlEfxhspW8C3ar0qpXhE3K5JUqu1LPnLSYOGlvUWfRfrYCEjrdlHOtttBUH77KwrzihTkf8R%2BhVHIC0JqnZCOnGafJ4aU4d0hxpcBnjPnFQvx8uysk%2FHFakMLhSy58Zr0zIkyhtzvrN2dTFIB3oBce5JENpW3IVbARFTK9qls4y2G0J1znfFlGaJhGqdR4vBlKuNdjZNuRXQDb7vOtLsOTpn8f7hakBhMl0%2BDLWTadCRZU%2B0srBa98AJrnd4y6TjbdHjU80GrERnsGxZUirAAn5u1Ku3assN%2FJweRLe0svn%2BAsOHhH5BNDs6q0fDNzokzOMEcZbxM0oBDcWYWjA0TsF2u9WF9UfeuLCGdNqFIjJq4tZ%2FfFC%2FawI1idCS%2BE5YDUTCgBk%2FioZSy51aJI7DsQWb7DDUlL7JBjqkAc9FG2WumUVkLL8bsE7QTwWxqAgOwcwoj%2F4XJSnX5qU4Pcaw%2FYfHuHmuOF%2FgzVDHNBIM%2BeL%2Bl8EYSkFBawrSsf8cgbJq%2FR6TmZ7Q7NZsOmMrbtpXQ8d4%2BM6DGv9gUlMvH0traDRrvNTb3%2FrSmBHkwNZOGiZmtxLkU0h9bX%2BdREnrgI%2FBrvzJHp0QoIf%2B3ux55sa%2F4l3r9P5MEeIuyIkSkXqr%2F7Gn&X-Amz-Signature=6cbfd9398d252e834613fcbe78803e5441355b59c2025f979f02f4cad45bf483&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VETO3AEU%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCfu0RoDpvjYHE5TJQNfGFwX09DRqhrn6ldmk1ZgPsN8QIhAJmVzymrsKWJtscpM%2B8POSZeUrezHsUAIr6Ghx11W7h1Kv8DCCIQABoMNjM3NDIzMTgzODA1IgzudEv%2FQ69fIdn%2BYj4q3AMu7WsjeRBqUK9iv2p8OpOMXIP%2BZoNNrN2TZN99v6u6CtkBn2xPeGQW4wAFMKG1%2BJvmIOkLMmaCcgWkZR8NonsfG36pbN0EU3uPd0uSvgN4ED1k3m%2BaFUtgJjD8QzoR1qnd5xXRvog%2FpK9Txrz8ICT1QbnyWxKgt0uelLgkaJ1TizelTej6o4F3eqvTwb4bOEZpAD6cRlRVDCcRrKdwM8%2BUehF2Pl7ebVFXtlEfxhspW8C3ar0qpXhE3K5JUqu1LPnLSYOGlvUWfRfrYCEjrdlHOtttBUH77KwrzihTkf8R%2BhVHIC0JqnZCOnGafJ4aU4d0hxpcBnjPnFQvx8uysk%2FHFakMLhSy58Zr0zIkyhtzvrN2dTFIB3oBce5JENpW3IVbARFTK9qls4y2G0J1znfFlGaJhGqdR4vBlKuNdjZNuRXQDb7vOtLsOTpn8f7hakBhMl0%2BDLWTadCRZU%2B0srBa98AJrnd4y6TjbdHjU80GrERnsGxZUirAAn5u1Ku3assN%2FJweRLe0svn%2BAsOHhH5BNDs6q0fDNzokzOMEcZbxM0oBDcWYWjA0TsF2u9WF9UfeuLCGdNqFIjJq4tZ%2FfFC%2FawI1idCS%2BE5YDUTCgBk%2FioZSy51aJI7DsQWb7DDUlL7JBjqkAc9FG2WumUVkLL8bsE7QTwWxqAgOwcwoj%2F4XJSnX5qU4Pcaw%2FYfHuHmuOF%2FgzVDHNBIM%2BeL%2Bl8EYSkFBawrSsf8cgbJq%2FR6TmZ7Q7NZsOmMrbtpXQ8d4%2BM6DGv9gUlMvH0traDRrvNTb3%2FrSmBHkwNZOGiZmtxLkU0h9bX%2BdREnrgI%2FBrvzJHp0QoIf%2B3ux55sa%2F4l3r9P5MEeIuyIkSkXqr%2F7Gn&X-Amz-Signature=3130dd968fc3a69eef079d3051c515b27a5b3b14b37a0aec5cd23628f1d70172&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

