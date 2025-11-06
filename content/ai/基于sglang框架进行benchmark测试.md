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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIJCZ5HZ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHimbpiSPd3nzevGT47XGQ7tC3083xka%2BghbAVzZZfIBAiATQQch5TJLGJb4cQ5THMZF9uNscb17MMLI3A4Mfd91sSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqRkao4txvuM7dTKEKtwD%2BhTl7wmHwnn8MyFv2WtmUN3A83s%2FuRVIIsvOLc7MYviAXw0QLZkCdK0YvUdP5xxU77c4I9rXoU56DvVu%2B6G5hdJl0eiKT6szdS%2BDqukTlWNZQ%2Blxg6khr9MNV6FhHvxmc1TsB72IfdS6Vt7MvI%2FrMqz8%2Fs2xY7GKpn%2B1Zm0Nchsm7v0kXfBJY0e%2FnPriMi4rlZM544n2X0NPLdZcgXF1u12hZk39UyEmfZTwmOXERAE4MkTC4GB9YKmOD5jKkLXihIQSOn7eSbRPvsT6E5Rl2YcCZBDy5p%2BuG5WxcIJHCEihUuR7jemonpduJfvpO8YKdNvSk55mI2pFj60YZHahZD2V4aHmX%2F6Q0rFw3BOxV0gFc2cMAR47EEPdNCUI2g8RmUBWl05wVx%2FPJHXb3o3SlBdNi10LVuNZGaCEQNFPq7q0f36bSAZo7bcFOOtJRn3CpMtxwyyLyhnvpMiO3E3wIftDOfXoe%2BxWIJsE4jIcTOn3gtD2wjIFstGO02ERZtLJd%2BDZJlN%2B22p8ZMHp64NMHpALTCNM3B5ta0xY8zgt%2ByO1aowNH6JTzR%2FKZ3rTKW7xG1dj4Ly%2B%2FHlQ0ixd3HXqMIjKHuo68JGocxE2e9%2F50j99tB3qm2%2B58tnb0VwwxPCvyAY6pgGM9zebra7My9e5u7cvEV0RP9LyCrGFrdZDTLLqs%2BX3%2Fw9CC82kiRsaEs7voLF2WkbI%2Fn9G6o7%2Bsa2Ak%2F%2BTQSnlIlarA8qPSA4xvJRoSWyJhJlRLxLEakWCIT5pSQvddys%2FBLNd3Gpa8jA6etXTbSHV6G54XMX99BZZB1lp%2Bswo27%2FVhZFRtW4nDhJUh6ME9B2Y82tS9wHZCMzJizVhab1z1w%2BdBevC&X-Amz-Signature=61f5661596cbb09dc30f1f4c67546e36f0b02b22c09888759be41eddc1741eaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIJCZ5HZ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHimbpiSPd3nzevGT47XGQ7tC3083xka%2BghbAVzZZfIBAiATQQch5TJLGJb4cQ5THMZF9uNscb17MMLI3A4Mfd91sSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqRkao4txvuM7dTKEKtwD%2BhTl7wmHwnn8MyFv2WtmUN3A83s%2FuRVIIsvOLc7MYviAXw0QLZkCdK0YvUdP5xxU77c4I9rXoU56DvVu%2B6G5hdJl0eiKT6szdS%2BDqukTlWNZQ%2Blxg6khr9MNV6FhHvxmc1TsB72IfdS6Vt7MvI%2FrMqz8%2Fs2xY7GKpn%2B1Zm0Nchsm7v0kXfBJY0e%2FnPriMi4rlZM544n2X0NPLdZcgXF1u12hZk39UyEmfZTwmOXERAE4MkTC4GB9YKmOD5jKkLXihIQSOn7eSbRPvsT6E5Rl2YcCZBDy5p%2BuG5WxcIJHCEihUuR7jemonpduJfvpO8YKdNvSk55mI2pFj60YZHahZD2V4aHmX%2F6Q0rFw3BOxV0gFc2cMAR47EEPdNCUI2g8RmUBWl05wVx%2FPJHXb3o3SlBdNi10LVuNZGaCEQNFPq7q0f36bSAZo7bcFOOtJRn3CpMtxwyyLyhnvpMiO3E3wIftDOfXoe%2BxWIJsE4jIcTOn3gtD2wjIFstGO02ERZtLJd%2BDZJlN%2B22p8ZMHp64NMHpALTCNM3B5ta0xY8zgt%2ByO1aowNH6JTzR%2FKZ3rTKW7xG1dj4Ly%2B%2FHlQ0ixd3HXqMIjKHuo68JGocxE2e9%2F50j99tB3qm2%2B58tnb0VwwxPCvyAY6pgGM9zebra7My9e5u7cvEV0RP9LyCrGFrdZDTLLqs%2BX3%2Fw9CC82kiRsaEs7voLF2WkbI%2Fn9G6o7%2Bsa2Ak%2F%2BTQSnlIlarA8qPSA4xvJRoSWyJhJlRLxLEakWCIT5pSQvddys%2FBLNd3Gpa8jA6etXTbSHV6G54XMX99BZZB1lp%2Bswo27%2FVhZFRtW4nDhJUh6ME9B2Y82tS9wHZCMzJizVhab1z1w%2BdBevC&X-Amz-Signature=820b384f002ecaeeaeb193276faf1856d52b4b922b00787f1c2fc653e7a124d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

