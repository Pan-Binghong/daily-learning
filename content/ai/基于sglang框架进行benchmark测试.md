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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWSDEMMC%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFDEdSnJ1%2B7ogRdnQbUSvnIYBn7ojwX2946%2FHfAkXfYkAiB4g4CAud5sBYI%2F4i9yJpx88tT04Mgr7UUb17FuvxHZsyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnurwjtwJqdjexFBRKtwDbYNAq4%2Fgv1%2BdkF0QxR%2BfbKDiMVyhkI6xq9YcVL0lARMye41iVSruULEypbCJt5F3RA4Iwp4UloCyOD2vkTTjvJHDM%2F%2ByvXqH5QxoeRdk8Y%2FOHWjQgVxsDr7Dn6r6xa1icRTcwOLr%2Bh%2FLDZnG35G0gkeLarNOi%2FHJlraVDVig1vHKYTys9uVsz%2BAZW1sux3wHhmoU1bOBh9HtYwNCDCR61IAP%2B%2BfUmjvmawPTPgm%2BcDP5xdrUwK7sggRjrzkdsyNkVf1KgvE7MacMQDasWuaZDQjuO%2BRqVjYevkFt%2Bf4%2BXB8VzV8uMO7SJJHep7VWO%2FELX5nBzI8hr1Kz%2BZwhtY2W3GcEpxKcKr3gWGl5ER8uyPZObj%2FWFy7EVayzaeYIRu8mpn3aCspG3MJep7rO8YkX7KD0EImclY22cHGayO7aC2Tw5LytFp2vaRNxt3llVRKWT36qaCmMn61OBZgGyRkKzDIHg5PnxIx8UHF9hd2BfwEr%2BYBVQEnbLM7dWR3yrHtWaWguLyuD2scDNw0CsWy9nfpCCsIJl0jxdj2TsMX%2B6bp1s6O%2BiBXHJuXkMtT3B6qHMjPjXB0AK59PUYP%2F7fIkS%2Bunt2CjzVtlZeHQEbZI%2FhVua5aAE0wFGTWkHF0w6%2FPpzAY6pgELhArGogiV%2BtO0eq1xhEYSeYKTRstvg%2BcIgDSN5Jcs8gMB%2BcEIq1l1d%2FrCU8ekZJH20wtpybtCBZdl%2BLRLY%2BKBV3YQeBrBfTOaikYOq8PaThOjs3XLhVrznEvcOCUZBj%2Btl35lOnvxPt7hTtF5WffqCbAXcKQbCJFGQ5Mzk1GfGWVLVRUq1PD1D%2FYGIIHgOkd9TKE4OnfCd1eFAfIZYqQ3sE3t%2BjWt&X-Amz-Signature=dda267459ca294d1c49cdd2faf46d7ca6f5bed484c1e0a4151e6515f0bd262c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWSDEMMC%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFDEdSnJ1%2B7ogRdnQbUSvnIYBn7ojwX2946%2FHfAkXfYkAiB4g4CAud5sBYI%2F4i9yJpx88tT04Mgr7UUb17FuvxHZsyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnurwjtwJqdjexFBRKtwDbYNAq4%2Fgv1%2BdkF0QxR%2BfbKDiMVyhkI6xq9YcVL0lARMye41iVSruULEypbCJt5F3RA4Iwp4UloCyOD2vkTTjvJHDM%2F%2ByvXqH5QxoeRdk8Y%2FOHWjQgVxsDr7Dn6r6xa1icRTcwOLr%2Bh%2FLDZnG35G0gkeLarNOi%2FHJlraVDVig1vHKYTys9uVsz%2BAZW1sux3wHhmoU1bOBh9HtYwNCDCR61IAP%2B%2BfUmjvmawPTPgm%2BcDP5xdrUwK7sggRjrzkdsyNkVf1KgvE7MacMQDasWuaZDQjuO%2BRqVjYevkFt%2Bf4%2BXB8VzV8uMO7SJJHep7VWO%2FELX5nBzI8hr1Kz%2BZwhtY2W3GcEpxKcKr3gWGl5ER8uyPZObj%2FWFy7EVayzaeYIRu8mpn3aCspG3MJep7rO8YkX7KD0EImclY22cHGayO7aC2Tw5LytFp2vaRNxt3llVRKWT36qaCmMn61OBZgGyRkKzDIHg5PnxIx8UHF9hd2BfwEr%2BYBVQEnbLM7dWR3yrHtWaWguLyuD2scDNw0CsWy9nfpCCsIJl0jxdj2TsMX%2B6bp1s6O%2BiBXHJuXkMtT3B6qHMjPjXB0AK59PUYP%2F7fIkS%2Bunt2CjzVtlZeHQEbZI%2FhVua5aAE0wFGTWkHF0w6%2FPpzAY6pgELhArGogiV%2BtO0eq1xhEYSeYKTRstvg%2BcIgDSN5Jcs8gMB%2BcEIq1l1d%2FrCU8ekZJH20wtpybtCBZdl%2BLRLY%2BKBV3YQeBrBfTOaikYOq8PaThOjs3XLhVrznEvcOCUZBj%2Btl35lOnvxPt7hTtF5WffqCbAXcKQbCJFGQ5Mzk1GfGWVLVRUq1PD1D%2FYGIIHgOkd9TKE4OnfCd1eFAfIZYqQ3sE3t%2BjWt&X-Amz-Signature=3e206fcac3e9bd0cfd2ccc759c4965d4d0f85fd9cfbb2bfad6432551b0555072&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

