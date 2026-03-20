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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WVYAU74%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIDy%2FmMCx8nAlFSTg8MtRetEVmypYcTgNHewmpHvanMM2AiEAjUWoiCkQh3GfAaOkg8F9ZOLvogCj8%2Fa4pKh8lwzv13Mq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBksa5bHFC1C63uQYSrcAw2BfRMMzRZjWjhNGXz5LlKo%2FAzCvR%2FqnunCOJcoWQyXz0Jg1Z7YJfQowb2oIXcwgVjyA%2FTOnYAbqTPfM0QhTdIA%2FBmJ24ryFFtQ8u8ZqB%2FBmcGwJ0OQG3dzpfPbm2HKu23luV%2BqJYRAsN4l3AkDxOYxWwmcqKbmbN5BrCZpc6VoTKW05mtQPy9JqTXWRV0HJT73Y1msI4GJFwzWPoD9fGL9wCLGE52p%2FmHpXJrq9%2FLYdbIqo7%2FcxGzLP8oDlpOpLvCPov5qFJhGjJewBi44lzbwRlApAUW8EDmzgqDqi5qznZf%2FUiwu2X%2Fx44yJY9Y8SkdFl%2BQmnlR6KqQNakhnhc24XTwhFXv5hErmf5DkvXVrVkF%2FZH%2BXS5xc%2FSSE7lVwIKjAB8231siImTN8Fn8JRDtNFKgpEcLPuDivZDaCc46I9NcE%2B8P9lpIdkOR%2FB4VCgnwAK3Lf6c%2Bxf1g%2FCgX8wIxcGD4iTDZFBiCXMSTyBTuMRAFLywGezGb5I0Enfi2GgKn7j1okRlZ5b7lGs%2B3neTp1ZLFpAfpFk5QE4qdPlYclXdppUBO40JQI%2FuPUFJ9BHg77xqRRr2ZIRRmkcvMnF%2Fo2UicIfEyLkTmswTgvvsZMns0tnjDHG600FJJ0MKe38s0GOqUBUvYHVT%2FguuC0wYW9IbThKqrxf1XbstYW%2FiV%2FZMQi5w0C5NAxeUVmQ1LInUE5PjT2Mih%2F69glMiWMiCgJpa00Lt4KV8Eqq8wYtwWA9e3r76rnBuqVwMTeo%2B26FEE4vltm6rwgWCI6cw5pMdrOampWiANV%2B6k%2B0oIcnUfFCt9bhP4Ez61THyMLllUt2aCzjEWBMbE5WEcSyfluu6hJ1xMUH4VIfxHc&X-Amz-Signature=664411bb7a60f41256dee91bd633f8ccec8c4cb8b431b60041045f261fb8e597&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WVYAU74%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIDy%2FmMCx8nAlFSTg8MtRetEVmypYcTgNHewmpHvanMM2AiEAjUWoiCkQh3GfAaOkg8F9ZOLvogCj8%2Fa4pKh8lwzv13Mq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBksa5bHFC1C63uQYSrcAw2BfRMMzRZjWjhNGXz5LlKo%2FAzCvR%2FqnunCOJcoWQyXz0Jg1Z7YJfQowb2oIXcwgVjyA%2FTOnYAbqTPfM0QhTdIA%2FBmJ24ryFFtQ8u8ZqB%2FBmcGwJ0OQG3dzpfPbm2HKu23luV%2BqJYRAsN4l3AkDxOYxWwmcqKbmbN5BrCZpc6VoTKW05mtQPy9JqTXWRV0HJT73Y1msI4GJFwzWPoD9fGL9wCLGE52p%2FmHpXJrq9%2FLYdbIqo7%2FcxGzLP8oDlpOpLvCPov5qFJhGjJewBi44lzbwRlApAUW8EDmzgqDqi5qznZf%2FUiwu2X%2Fx44yJY9Y8SkdFl%2BQmnlR6KqQNakhnhc24XTwhFXv5hErmf5DkvXVrVkF%2FZH%2BXS5xc%2FSSE7lVwIKjAB8231siImTN8Fn8JRDtNFKgpEcLPuDivZDaCc46I9NcE%2B8P9lpIdkOR%2FB4VCgnwAK3Lf6c%2Bxf1g%2FCgX8wIxcGD4iTDZFBiCXMSTyBTuMRAFLywGezGb5I0Enfi2GgKn7j1okRlZ5b7lGs%2B3neTp1ZLFpAfpFk5QE4qdPlYclXdppUBO40JQI%2FuPUFJ9BHg77xqRRr2ZIRRmkcvMnF%2Fo2UicIfEyLkTmswTgvvsZMns0tnjDHG600FJJ0MKe38s0GOqUBUvYHVT%2FguuC0wYW9IbThKqrxf1XbstYW%2FiV%2FZMQi5w0C5NAxeUVmQ1LInUE5PjT2Mih%2F69glMiWMiCgJpa00Lt4KV8Eqq8wYtwWA9e3r76rnBuqVwMTeo%2B26FEE4vltm6rwgWCI6cw5pMdrOampWiANV%2B6k%2B0oIcnUfFCt9bhP4Ez61THyMLllUt2aCzjEWBMbE5WEcSyfluu6hJ1xMUH4VIfxHc&X-Amz-Signature=febeffed8ec318e9f8f34f1d499548a444273020b47c1e384eba6be3a27067d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

