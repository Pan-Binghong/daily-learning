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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZFVJO6N%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSl4%2B9eyaV%2FvmN9h%2BGohTS39IDdMFqC90S3YvrudxQRQIgSE4GVvctyhQUAGiXlge%2FA3yAoMm0lrCYuv%2BTCyHQdHgqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNza4hJSoWi5wmIgLSrcA25uEVxo702QXliz5s%2BGjPhf6qDZe8C2dgdVdknzCzDn5U7iGd3ZJn%2BD1BC1ZsgJ9JBqsnK%2BcEGj06mtdmrs8QZ7Ib0tH2hrLWPftkk%2BQ807VQQtAxIykcqa3e8TRmzLIY%2BKBi8aG6yIecB1E8bd%2FBLkx3d6HdCjNzuK9MwcY8eXQSBZSqWSkCK0LA5pP2RKL8R3ZVGEtmPmxrabtQwsDzyaQ9oi%2Ba8YmhttsNzKR%2FhHsMtLRyYEQMMg4nupRDeBVIO366lPsD%2FpVoikQE11CfqqiMM1kMz8cClCZIyvmkIy9fyHtAKvOFYgUdcZ6K93ZJX2wYVL11VJx1gmafPvRF1ENzRSiQUbX9pu%2FouUBAnkDvkzdNrU1TlhS1Img7l%2BNfvBFWbj09VFeEbXj9xeoG%2BLwf%2F1v1ELTfqnFoMqdXZz2NgEWF8T3NEUELJvVqvPMgxjlJwS7BejVtF4IdwoqIuXriyayI5Ef%2Bp3EGonm3s4X8PixZZrzZmYcdiwhdCJ0QmowHwEBwr50tsgWpOfQjNyG1%2BmeRoMLwdH6XhEBCDUfiKONnypH%2BCXxLooYcjEtkSfwRGyYiM5EZc7jMMlN2xDX6K%2B8u8LIY40iB%2FSCOl48zsYbcTTSXEZk7tUMNG2u88GOqUBpq8aoPftxN%2BwVdIjMhZSMDxOGV2pROxrxvgo41EedW0Wx5ClBU9kMekSnUXiw2nQqJMpaDaTa%2FZWLiH%2Fkzl1Nmz0o98D0dMcQmcTwU%2FEcU9DHoxZYP6ofyRGsqAs7vDYEUJMqFNbXx6p4scEq9XQv7C9THmhx1YCbd94jrxLVgLO0%2BpKPGrcAXkmuxgFGw2zcpyGqIqZ15w%2B9OaTK3garo9j1BEy&X-Amz-Signature=4d823af10056b9d515f7baf5fe3765b92bbeef2d08bbd7c3800d8e3d4660978f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZFVJO6N%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSl4%2B9eyaV%2FvmN9h%2BGohTS39IDdMFqC90S3YvrudxQRQIgSE4GVvctyhQUAGiXlge%2FA3yAoMm0lrCYuv%2BTCyHQdHgqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNza4hJSoWi5wmIgLSrcA25uEVxo702QXliz5s%2BGjPhf6qDZe8C2dgdVdknzCzDn5U7iGd3ZJn%2BD1BC1ZsgJ9JBqsnK%2BcEGj06mtdmrs8QZ7Ib0tH2hrLWPftkk%2BQ807VQQtAxIykcqa3e8TRmzLIY%2BKBi8aG6yIecB1E8bd%2FBLkx3d6HdCjNzuK9MwcY8eXQSBZSqWSkCK0LA5pP2RKL8R3ZVGEtmPmxrabtQwsDzyaQ9oi%2Ba8YmhttsNzKR%2FhHsMtLRyYEQMMg4nupRDeBVIO366lPsD%2FpVoikQE11CfqqiMM1kMz8cClCZIyvmkIy9fyHtAKvOFYgUdcZ6K93ZJX2wYVL11VJx1gmafPvRF1ENzRSiQUbX9pu%2FouUBAnkDvkzdNrU1TlhS1Img7l%2BNfvBFWbj09VFeEbXj9xeoG%2BLwf%2F1v1ELTfqnFoMqdXZz2NgEWF8T3NEUELJvVqvPMgxjlJwS7BejVtF4IdwoqIuXriyayI5Ef%2Bp3EGonm3s4X8PixZZrzZmYcdiwhdCJ0QmowHwEBwr50tsgWpOfQjNyG1%2BmeRoMLwdH6XhEBCDUfiKONnypH%2BCXxLooYcjEtkSfwRGyYiM5EZc7jMMlN2xDX6K%2B8u8LIY40iB%2FSCOl48zsYbcTTSXEZk7tUMNG2u88GOqUBpq8aoPftxN%2BwVdIjMhZSMDxOGV2pROxrxvgo41EedW0Wx5ClBU9kMekSnUXiw2nQqJMpaDaTa%2FZWLiH%2Fkzl1Nmz0o98D0dMcQmcTwU%2FEcU9DHoxZYP6ofyRGsqAs7vDYEUJMqFNbXx6p4scEq9XQv7C9THmhx1YCbd94jrxLVgLO0%2BpKPGrcAXkmuxgFGw2zcpyGqIqZ15w%2B9OaTK3garo9j1BEy&X-Amz-Signature=8535db2174766e57ddb065693ae6a11b1fdc07d55eecdaf1dd496eddec87c765&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

