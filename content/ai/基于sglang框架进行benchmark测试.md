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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4XGG6HQ%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIFAVy81pwCNalPwo4Lhwy9zcnFBVqZgBMvtBjMenhNSSAiEAwxvYrqDFvhazekODPGfFzIF0g2HW2nzxG2p40Kejs24q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCjlj0VdcF4ImcYDpircAzktGt2RNcRqfsSSxXuc93ZnVwL83wRbuGjlBds0KtgTj9RH%2FazmFYgQQbdx4hGSy5bYPea%2BALhdB3nCrMtuKyMAEAvj%2FRMDTK%2FlIWwRCoxGBrBsFQzqvAQW%2Ff3jLO5IiTgv6g3DsYimM94qddeui3z2sFVqjg9z392fNHlIkCCix9tQT0JhEMduINRUpshdWrL3ZU2UnHjduO2f%2BAoLiyufgSN4pmQK%2B3qBXNCot7inKGuk4aDZ%2BwMeWaZERWaOOvWH5ZhZst1GllQr1e%2BPXaRPbj%2FhEVXUPJe3XLKjOolO%2Bewp7AD3MRYdd4uIiI%2Bbh41XX%2F3GZfs1Une%2ByEwCimyFQkSUmWRWe9%2B3R4suXZh7%2F1S0kTT1XVLJNEs4D6dHNLEhdDvlFGKTqXtZK3wYA0xbUw0fy%2FIpOtub7fWIaI8rLLJJzOvjawMSY%2Bl1LU2kvbB%2B8XfXMrhaWim5ZCg6th4BnnlcOGc%2FjL0MJpvba%2FxD%2Bd0DMGoPkeuGsefXj64edq9rQa8S21d8%2FTxkjXcePGYX21oCu5Ef76qWAjk2P%2BQ8h4arw46RKuCB%2FDKXU%2Fp3o6dUOZSD5S9UCBPcctk2HFsgxl3YuxAc%2FvOmpHq2I4%2FlRzMgDpq5mywnVTnHMOffuMkGOqUBPFCRP0WNEL4nEYtrZpunDb02bCAmjgHfmLAR06LwfDx52MvFLnL1T%2FzhbL38e9SVPY2n94uW3UHjeK%2F5cW5JWglyQdVXRu%2BVnF3d8MGbiA4xtDJoSFZxAxRGGhTm%2BwNhtqqHCz7y9qFuabSvGhMMtWNfY2wNV4VNX%2BLk30MDAH9oo7QS3gClit%2FJyZq62xMib0yZRF7XkxvjrzTnZhoax6vae5rr&X-Amz-Signature=d0df3f4b580f7db82b5709609bdd83ee278306c7dfe20467a75c710535b552c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4XGG6HQ%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIFAVy81pwCNalPwo4Lhwy9zcnFBVqZgBMvtBjMenhNSSAiEAwxvYrqDFvhazekODPGfFzIF0g2HW2nzxG2p40Kejs24q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCjlj0VdcF4ImcYDpircAzktGt2RNcRqfsSSxXuc93ZnVwL83wRbuGjlBds0KtgTj9RH%2FazmFYgQQbdx4hGSy5bYPea%2BALhdB3nCrMtuKyMAEAvj%2FRMDTK%2FlIWwRCoxGBrBsFQzqvAQW%2Ff3jLO5IiTgv6g3DsYimM94qddeui3z2sFVqjg9z392fNHlIkCCix9tQT0JhEMduINRUpshdWrL3ZU2UnHjduO2f%2BAoLiyufgSN4pmQK%2B3qBXNCot7inKGuk4aDZ%2BwMeWaZERWaOOvWH5ZhZst1GllQr1e%2BPXaRPbj%2FhEVXUPJe3XLKjOolO%2Bewp7AD3MRYdd4uIiI%2Bbh41XX%2F3GZfs1Une%2ByEwCimyFQkSUmWRWe9%2B3R4suXZh7%2F1S0kTT1XVLJNEs4D6dHNLEhdDvlFGKTqXtZK3wYA0xbUw0fy%2FIpOtub7fWIaI8rLLJJzOvjawMSY%2Bl1LU2kvbB%2B8XfXMrhaWim5ZCg6th4BnnlcOGc%2FjL0MJpvba%2FxD%2Bd0DMGoPkeuGsefXj64edq9rQa8S21d8%2FTxkjXcePGYX21oCu5Ef76qWAjk2P%2BQ8h4arw46RKuCB%2FDKXU%2Fp3o6dUOZSD5S9UCBPcctk2HFsgxl3YuxAc%2FvOmpHq2I4%2FlRzMgDpq5mywnVTnHMOffuMkGOqUBPFCRP0WNEL4nEYtrZpunDb02bCAmjgHfmLAR06LwfDx52MvFLnL1T%2FzhbL38e9SVPY2n94uW3UHjeK%2F5cW5JWglyQdVXRu%2BVnF3d8MGbiA4xtDJoSFZxAxRGGhTm%2BwNhtqqHCz7y9qFuabSvGhMMtWNfY2wNV4VNX%2BLk30MDAH9oo7QS3gClit%2FJyZq62xMib0yZRF7XkxvjrzTnZhoax6vae5rr&X-Amz-Signature=997c2c8a66f8268215a3d34a536143210331065d31142478df608516814bdfc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

