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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ELQOW2W%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIByaA%2BdDFsTNXYP66CuRfpVXpwTH5QXhXF%2FHZcYA8BaBAiEAxkHi5SCrCtRe8tKq%2FSV8emP4Scd6T2TuE0MIl4DV9dMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJur2v0NoBraYChICrcA%2BzUZrV%2FGVxMtIfEvGigtdc7VwgT8TB5ZQmwBdU7wNjzz960uATAIMwHgOOdvkyIJ%2B6nA8dCrZRxRTsYeOJSgIOmFUKGPrwqmOCNTHOb64Jh4iAt9B%2B273WJcKN3h8V0VaVv3ehZ%2Fv%2BIFzxEsCD4KsncJRR8sIhZZ9JuNe%2BOfXyP%2B3tUO9kSPMwUxw7I264kPNEgNKqV%2F47QahMu1MHB0C6V6Yj4f0Z8%2FuVhTDWbg6sIiO2Yj1CJqL80NSq22aKXDQ0m5mB9W4%2Br%2Bf3NAYaF86nlnNdI1OQnTvqJhnbu0FD%2FWQK7Tb7yx2j9803KeS4oBj4CPyx2y4leX4wW9i6LPnUI%2BSMKRgrdVPtybYY1rznWES3CKZsJhvEBin3X3uTwNRH9KKGc16N65waO8F3pzGUzwPQZiSIKwgIUO4xa3Q%2BCsrAN9zyNx8k5Lg2esRUg2yRhW7keopgDq5qYKwOJKOrNTp1rc%2B0R4hd72sQ3j4v6LrtxYEwSBXgtq6aGgu7Lk3ui02AWCFscdkOPQ7qIskoNyAhYmaNRn8Mx4NEtOhdKRLNNnt%2Bufa%2FDtMe6PQDeMxyXpN%2FxMf0VLJAPub6yYpZikFisNhrBF3Pf5s0DBMvksFME%2ByDbUoB%2BiaX6MOO19MwGOqUBbDr2rAKK2OXiKRGfKwIFt91oTxuu9c8LlOtxp9SszxTSi0nnVv1ephycZi%2FKqgdgxYI68TXLF8u8YI7xRRsVH1dG9DI58DxLglEhTO5qVTaxJr2txcEkjw8JoGQlDfnnqMZaxzmyyntjK%2FQY8H7HVgzKOVVTPi8kg58SXiCdyyevT9yks99aTstPNKedoSV0hMFAGnOS3pUc2cSQonsBRqk%2B%2B8bv&X-Amz-Signature=d1f8fbef6167d2c0b3eba4fde64fa549125b0c2b8c8c4c27b97f33a3d96f0399&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ELQOW2W%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIByaA%2BdDFsTNXYP66CuRfpVXpwTH5QXhXF%2FHZcYA8BaBAiEAxkHi5SCrCtRe8tKq%2FSV8emP4Scd6T2TuE0MIl4DV9dMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJur2v0NoBraYChICrcA%2BzUZrV%2FGVxMtIfEvGigtdc7VwgT8TB5ZQmwBdU7wNjzz960uATAIMwHgOOdvkyIJ%2B6nA8dCrZRxRTsYeOJSgIOmFUKGPrwqmOCNTHOb64Jh4iAt9B%2B273WJcKN3h8V0VaVv3ehZ%2Fv%2BIFzxEsCD4KsncJRR8sIhZZ9JuNe%2BOfXyP%2B3tUO9kSPMwUxw7I264kPNEgNKqV%2F47QahMu1MHB0C6V6Yj4f0Z8%2FuVhTDWbg6sIiO2Yj1CJqL80NSq22aKXDQ0m5mB9W4%2Br%2Bf3NAYaF86nlnNdI1OQnTvqJhnbu0FD%2FWQK7Tb7yx2j9803KeS4oBj4CPyx2y4leX4wW9i6LPnUI%2BSMKRgrdVPtybYY1rznWES3CKZsJhvEBin3X3uTwNRH9KKGc16N65waO8F3pzGUzwPQZiSIKwgIUO4xa3Q%2BCsrAN9zyNx8k5Lg2esRUg2yRhW7keopgDq5qYKwOJKOrNTp1rc%2B0R4hd72sQ3j4v6LrtxYEwSBXgtq6aGgu7Lk3ui02AWCFscdkOPQ7qIskoNyAhYmaNRn8Mx4NEtOhdKRLNNnt%2Bufa%2FDtMe6PQDeMxyXpN%2FxMf0VLJAPub6yYpZikFisNhrBF3Pf5s0DBMvksFME%2ByDbUoB%2BiaX6MOO19MwGOqUBbDr2rAKK2OXiKRGfKwIFt91oTxuu9c8LlOtxp9SszxTSi0nnVv1ephycZi%2FKqgdgxYI68TXLF8u8YI7xRRsVH1dG9DI58DxLglEhTO5qVTaxJr2txcEkjw8JoGQlDfnnqMZaxzmyyntjK%2FQY8H7HVgzKOVVTPi8kg58SXiCdyyevT9yks99aTstPNKedoSV0hMFAGnOS3pUc2cSQonsBRqk%2B%2B8bv&X-Amz-Signature=44a48bf69e401a53ffc86b78944e335a3117e851eb061961e1dcf8a64f0dbbd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

