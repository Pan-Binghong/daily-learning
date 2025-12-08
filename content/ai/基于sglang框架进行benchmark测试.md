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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UROSKMYA%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID6vjrZJbi3aO1RacNhMsmmOV1hsvHx5QoWa29a4mfJ4AiEA054unB%2FQlbisX6sks2cZoi62DNuYq2Z9hhQc%2BHmTpkcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdtjGCt0PAPEUXzbCrcAypFGNvDHqaee4jb1MA%2BeTxC5rBgZFdZA02q4YAzgMUm2WvX8CRAuCBPSqRxSDOPCb98lMhrHm33StK8QYUGavg9JfFJTggOlrlXsqp7ubK7LcVUi881zEXBeLH8nqqKIaLPE%2FcgJDIRvg%2F9DvVKqw0NIVUxaxVAtfqlZj9XbgLapfbl7ING%2BmsmmPCbMlDiAoIUog5GgLwgoqBv0b47mfGpno%2BrAlNTqfuNTNu%2FLYRNEa8QKnovZVjAKu6y3ymSWgUeq8pPcQxoKZEFtorJx4xNzvW%2BoJwOrWmukQ3fgc9PIqOOkeY6qDFsF6NJYrOp%2FBtFPDrMG%2FYYCGfmYwuXUN%2BG12wBxsxI38qHJe%2FfeOZD6Kf1qIykWeSSNUNl%2F9AggXla79Y7EaBrdP8AHPuztGzwf%2F%2FProIISqHkbN%2FMQWqrkVoRKMwlGc%2FEDNqMK5yjWStuf6wHLGnUNVUbTBXxYIaUH9Jl%2FjQUYhj8Aa4DBmP%2BvGfQWPRGC4tegDljWaXAn2oMBb0OU3HHaYkcgeGKqzT4g%2FuVVQXrGH3NtNRdBFsMiZP%2Fo%2B78X9SFrr8UYXf%2BLxUhKoigh13LmxehXWf1Nl8O%2FqNfT0AmXpwVSFMlqHvOxI%2B63%2BsmiAhOR8oqMMDv2MkGOqUBKkZttDpBF1zjKqbF01yl78BI8T2sxBBfuGPRLEwx9WLPwJuyAwMu4HgXoV%2FtrEqcpiavL%2FRIucGDnA9pbcDtdnxn36bkyHct0FP1DthH5nUU6Kucs16rv0dpaYibTTGTeWnr2vlpsQdX%2Fhtv2gMQlUQsNkd9bIPoJ8Fbnky3GZ7eTKlc1tsX2kh7MUlvA6%2BUcOx7Fn1RymllNLhioWhJa2aM%2FxCw&X-Amz-Signature=2278fde8c08adb3c5006815e2049d1f390ebc85b7bc62cbcf898833c87313301&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UROSKMYA%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID6vjrZJbi3aO1RacNhMsmmOV1hsvHx5QoWa29a4mfJ4AiEA054unB%2FQlbisX6sks2cZoi62DNuYq2Z9hhQc%2BHmTpkcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdtjGCt0PAPEUXzbCrcAypFGNvDHqaee4jb1MA%2BeTxC5rBgZFdZA02q4YAzgMUm2WvX8CRAuCBPSqRxSDOPCb98lMhrHm33StK8QYUGavg9JfFJTggOlrlXsqp7ubK7LcVUi881zEXBeLH8nqqKIaLPE%2FcgJDIRvg%2F9DvVKqw0NIVUxaxVAtfqlZj9XbgLapfbl7ING%2BmsmmPCbMlDiAoIUog5GgLwgoqBv0b47mfGpno%2BrAlNTqfuNTNu%2FLYRNEa8QKnovZVjAKu6y3ymSWgUeq8pPcQxoKZEFtorJx4xNzvW%2BoJwOrWmukQ3fgc9PIqOOkeY6qDFsF6NJYrOp%2FBtFPDrMG%2FYYCGfmYwuXUN%2BG12wBxsxI38qHJe%2FfeOZD6Kf1qIykWeSSNUNl%2F9AggXla79Y7EaBrdP8AHPuztGzwf%2F%2FProIISqHkbN%2FMQWqrkVoRKMwlGc%2FEDNqMK5yjWStuf6wHLGnUNVUbTBXxYIaUH9Jl%2FjQUYhj8Aa4DBmP%2BvGfQWPRGC4tegDljWaXAn2oMBb0OU3HHaYkcgeGKqzT4g%2FuVVQXrGH3NtNRdBFsMiZP%2Fo%2B78X9SFrr8UYXf%2BLxUhKoigh13LmxehXWf1Nl8O%2FqNfT0AmXpwVSFMlqHvOxI%2B63%2BsmiAhOR8oqMMDv2MkGOqUBKkZttDpBF1zjKqbF01yl78BI8T2sxBBfuGPRLEwx9WLPwJuyAwMu4HgXoV%2FtrEqcpiavL%2FRIucGDnA9pbcDtdnxn36bkyHct0FP1DthH5nUU6Kucs16rv0dpaYibTTGTeWnr2vlpsQdX%2Fhtv2gMQlUQsNkd9bIPoJ8Fbnky3GZ7eTKlc1tsX2kh7MUlvA6%2BUcOx7Fn1RymllNLhioWhJa2aM%2FxCw&X-Amz-Signature=5254c538078453b303996bba995c49b964f1e70a45c718cdd2d43aff0b8dd9d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

