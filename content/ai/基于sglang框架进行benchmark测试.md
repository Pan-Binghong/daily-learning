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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHNCNYYF%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbsUfn5YLARXXhjeOg6Lkc%2FFizFikk2FvbDTS6rMOfGAIhAK8ko7K8HE1jQVuZ%2FoOUytULjuROJMVcxzTSSKcJT3yfKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygG0R9HI%2FsKMw1eTUq3ANqkMSkspR8Xjo5t7LKBz4VXNCJmtH4UVJjf6Ogoy6fRXGIeDqNgKFCcXQYIEhT5zO%2F4X6pl87tP7ep6wyuJ3PQuBzSDxRZ05Tt9a4Sl3oJaQBV%2BMuGjMgLz%2FV4b3Cnvwec69TNxBoxeBxgOoH65YkorWmgaMxyOzArPfjJQpH85NidKNRtaeb8r0I9bgLeWdEDxHJaT0ML5UurvR%2FLDw7z7FizYKpDOd%2BB1ogbt%2Fj3W14W1erRXQwmMGLY3HlNRPFbX4UToO1kO917lKrFBuraGa0xPE8LtACKJINCoaiYb3hp%2FDJx5u1CNeUB5UjJcdEA%2BxSKVF77zRBSrDQ81pwJ7%2FPW1mGuucK8WhbnNSoS9eE1u6N%2BBAyhQW7b8Dxd1xTtk7KEWZacd6MI6vhRFLQNoZY6WB49TLN7nzX6C7Izx364yaYO6FMP6w8YtbXwz99Pw19CCzMlei7m3wGOAQbLD7L%2BtZOR30B%2F2zpQbnofOvY4xrZpT85Z9nOc8FPb07YuqI3knHPvGljgCWqbbUkQfQRlYX1BWNYhT8SK2PQzWIU340QoRrygo9M8dEe%2FjjgAhBAVAlfrYdBGyM90ByGCFd0%2FoXiDptKZJge7ehIZN0johia2o%2F1ZpdUqKzCE8a%2FIBjqkAUdVo9zzToio3w8k6c9jHGpn%2FVGebSPqh%2B5zCCWsi3IUipvFdQGQfIhzeZC1N9c3lMaJD6wYEUGTzNrDDDNM%2FVE4tZ6eI%2B%2FLpzwiPS%2FxqmCUxoGetv5HVHLe5FRL6KKAGTpaStuekCY4pwoldABRxRraaXXYE%2Ff%2BOb6Rm62EtV7%2BCp2FTT4t5q2xGgMb9UVLQItYicAd19Di1vvLL2Ym7oj5kYm0&X-Amz-Signature=deb57bbdc0c3230209652656b3f8208d5e9b1f00ccd7b5e7e0ef9cb918cdc833&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHNCNYYF%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbsUfn5YLARXXhjeOg6Lkc%2FFizFikk2FvbDTS6rMOfGAIhAK8ko7K8HE1jQVuZ%2FoOUytULjuROJMVcxzTSSKcJT3yfKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygG0R9HI%2FsKMw1eTUq3ANqkMSkspR8Xjo5t7LKBz4VXNCJmtH4UVJjf6Ogoy6fRXGIeDqNgKFCcXQYIEhT5zO%2F4X6pl87tP7ep6wyuJ3PQuBzSDxRZ05Tt9a4Sl3oJaQBV%2BMuGjMgLz%2FV4b3Cnvwec69TNxBoxeBxgOoH65YkorWmgaMxyOzArPfjJQpH85NidKNRtaeb8r0I9bgLeWdEDxHJaT0ML5UurvR%2FLDw7z7FizYKpDOd%2BB1ogbt%2Fj3W14W1erRXQwmMGLY3HlNRPFbX4UToO1kO917lKrFBuraGa0xPE8LtACKJINCoaiYb3hp%2FDJx5u1CNeUB5UjJcdEA%2BxSKVF77zRBSrDQ81pwJ7%2FPW1mGuucK8WhbnNSoS9eE1u6N%2BBAyhQW7b8Dxd1xTtk7KEWZacd6MI6vhRFLQNoZY6WB49TLN7nzX6C7Izx364yaYO6FMP6w8YtbXwz99Pw19CCzMlei7m3wGOAQbLD7L%2BtZOR30B%2F2zpQbnofOvY4xrZpT85Z9nOc8FPb07YuqI3knHPvGljgCWqbbUkQfQRlYX1BWNYhT8SK2PQzWIU340QoRrygo9M8dEe%2FjjgAhBAVAlfrYdBGyM90ByGCFd0%2FoXiDptKZJge7ehIZN0johia2o%2F1ZpdUqKzCE8a%2FIBjqkAUdVo9zzToio3w8k6c9jHGpn%2FVGebSPqh%2B5zCCWsi3IUipvFdQGQfIhzeZC1N9c3lMaJD6wYEUGTzNrDDDNM%2FVE4tZ6eI%2B%2FLpzwiPS%2FxqmCUxoGetv5HVHLe5FRL6KKAGTpaStuekCY4pwoldABRxRraaXXYE%2Ff%2BOb6Rm62EtV7%2BCp2FTT4t5q2xGgMb9UVLQItYicAd19Di1vvLL2Ym7oj5kYm0&X-Amz-Signature=004fb8e66841775b46134a2fb835979ef5a28701202ccb03b5a3f84964068a18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

