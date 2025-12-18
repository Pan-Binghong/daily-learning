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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZBZDDNX%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAnOYs2Qfx36XbM3%2BqDg1pAQHzlPemerdO4VydW2qSldAiB%2BTyhDsAXKXhOhhf9vQijcTHB1CZZW8W%2B78m%2Fwhy07GCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMORQZXK2U%2F8HGoUF0KtwDTvmiXiBveNs8Zua9V4u4rlaOK1ud6Zh0PbniDUAK55be2l8A8j%2FixQmT%2FxDTqAQLfeSKmyl6v7caQSwhbZ0cT09gOqUhirmoImUVvm4VM9XdTQO1jwEJieKuYPyYRNVH4XEQXTUemyBuriDBf13AyUzgWySAH9hecmtlOhOp4EbkyywVmZyewongQ%2BLdHAtX3KqpMM8UTGtrd1SaR5HusR2yiVeciLRwSNXahwuuxVuSZXm1VTi9jbLk4x6vxxksJK5d8SUhZrpbfTu7hwYcdXLy6sbP%2FiG9oyaI6VPsRSm6p%2BhA4XNllPDwS%2BKUedIezcGCXyy9MVBFmL5TNPb8dWHTAlLnQOnAoBCHi0m2V0rZNVVoIiGciLlE61OigCx6%2FXGpjdDIOt3Lmoq5rfoff3U1QPWvsLI6eQIua85zXI05cC9Wvqi6jjwOGZH618Mcm2%2FPOLQUgGv7xSr2qd1H2dqRdB9T9OmLyDPNzedhh6ed06vVcMciwqrWslsRh%2BEEolFQuSNGmVJ3Sy3Fwm7AueJMEp7IOUz8xOMPuaqXuXH07wO3wMYpp5zEbzFZmLlb9%2BQgsEZ54s%2BzCudFvO7kBmjBpIcP1P7J%2FO0Bs91W3GwO6naSua0%2Fpra41HkwtcmNygY6pgGhEQqjphJQkhhBwK9zQbMhLP1iLnu1OeFR%2FF7VmLhv2uwMfzc9bqnrn4qWd6p2m7OaJKB1GCd1t0t0OMQ8W598j%2BP4XW71F3FwFP%2FACVMPiGZLo3HFWgJltxnkSdgwFaW4G8ul8XGAeBSgBJwR5M5SSWUL13sl8xb9yfgw%2FJKzxQsuzlxpkyZr7WWrVMDeZagjGhHM3vUsulCVyjeZjpWvNInbclAf&X-Amz-Signature=0d3ab4550fc01facd6bf5843e79e4e4ba56ba3ec68da757b46b78505051f63e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZBZDDNX%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAnOYs2Qfx36XbM3%2BqDg1pAQHzlPemerdO4VydW2qSldAiB%2BTyhDsAXKXhOhhf9vQijcTHB1CZZW8W%2B78m%2Fwhy07GCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMORQZXK2U%2F8HGoUF0KtwDTvmiXiBveNs8Zua9V4u4rlaOK1ud6Zh0PbniDUAK55be2l8A8j%2FixQmT%2FxDTqAQLfeSKmyl6v7caQSwhbZ0cT09gOqUhirmoImUVvm4VM9XdTQO1jwEJieKuYPyYRNVH4XEQXTUemyBuriDBf13AyUzgWySAH9hecmtlOhOp4EbkyywVmZyewongQ%2BLdHAtX3KqpMM8UTGtrd1SaR5HusR2yiVeciLRwSNXahwuuxVuSZXm1VTi9jbLk4x6vxxksJK5d8SUhZrpbfTu7hwYcdXLy6sbP%2FiG9oyaI6VPsRSm6p%2BhA4XNllPDwS%2BKUedIezcGCXyy9MVBFmL5TNPb8dWHTAlLnQOnAoBCHi0m2V0rZNVVoIiGciLlE61OigCx6%2FXGpjdDIOt3Lmoq5rfoff3U1QPWvsLI6eQIua85zXI05cC9Wvqi6jjwOGZH618Mcm2%2FPOLQUgGv7xSr2qd1H2dqRdB9T9OmLyDPNzedhh6ed06vVcMciwqrWslsRh%2BEEolFQuSNGmVJ3Sy3Fwm7AueJMEp7IOUz8xOMPuaqXuXH07wO3wMYpp5zEbzFZmLlb9%2BQgsEZ54s%2BzCudFvO7kBmjBpIcP1P7J%2FO0Bs91W3GwO6naSua0%2Fpra41HkwtcmNygY6pgGhEQqjphJQkhhBwK9zQbMhLP1iLnu1OeFR%2FF7VmLhv2uwMfzc9bqnrn4qWd6p2m7OaJKB1GCd1t0t0OMQ8W598j%2BP4XW71F3FwFP%2FACVMPiGZLo3HFWgJltxnkSdgwFaW4G8ul8XGAeBSgBJwR5M5SSWUL13sl8xb9yfgw%2FJKzxQsuzlxpkyZr7WWrVMDeZagjGhHM3vUsulCVyjeZjpWvNInbclAf&X-Amz-Signature=c8b7a040119e8133e1bfd70fb360f40f961ae4bb32a75f7a8d1289dfd607c2e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

