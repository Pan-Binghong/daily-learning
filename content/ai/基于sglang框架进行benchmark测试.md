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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G6ELQAS%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWletudBhzZuKtSuTfbzkbUTUzxX5HxHiw6NHr%2FEqYLAiBRm2fd97USV6%2BHastPBVXBZHTJYu1AfK0GhkdjlS6lpSr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMXvps%2FfXIa1d%2BnItPKtwDQFoRL%2FJiHZeLs6JRqwIIBpPjjRV0N1yC1BuSfxX0bq8vXEnohdihL%2BW86G5LH9pLW1Va9Sq%2BV%2BCW0290Ws4XLYYGlAq2COYua6eMso12vZlBJXMqvv4ieQOaGcG4DosCawYnMKiaE4KDCrWuHeAZBM7cJfJiHR4dnu6%2F1SRmpHQKHiU3ye1P%2BVX%2ButZlQREnxVHwLmMH9fT9lLrPgg4RucN6npCxZBPwFHDwZfaMb2RaG4Rz4T3%2FvGsOPxL9f86JQMRRwwIAhkG4aObtH1j7aWgWZiq4iLzVthq1JSrYu0TW4%2BCRxaQJ4XIlTDFTwbh0Rr8VJBNGdrpAn%2B9f8PCesbSgkmFfr593nTxSghRTpLKh5g5vpBHeEF%2FWw%2FHyXsV2xPDmEPrk3OiRwq96CNJmq%2FlJ2RCfrWN39ZvPrccit7%2FzNtPMoNbZnOTyUB67Ap91SueHSznDSUewJBBovxyjzo9MKYwxLxqUW4L%2BnVXUf%2FvDrlZlHo1KSZzArjZ%2Bp0lTOZUSNIVPqc6KMGN29ktU6Ynz2T9T%2FY%2FTXfhN9OeDxB%2Bcty1%2BwJYhNCp3XFGula7uvB4Vf%2Fwd1ZfFylfPon2Qau%2FjpmY8ppp0HybV2uj6guqvBaZl%2Bj%2BWCeNxpUUwk7LIzQY6pgHRMuRfqdT3P5ftfzJLPYa0iu5PdodP0cGtxUc%2FIbHvVNjxlWCs4Lb9cRCLlRY3PRBmFK%2BfS5P0ZcLTcaAU5PpxxgPLjswMa5e0VePMqyRnYkZhhIonpVhBoB8TQBfyc6VZlM8VbkimFb%2FTs8TeKNftahcHR050QwsWH0T68a%2F8i1dNHFM3NyKA%2FOH4tVRgS1UsCHqrGIdQoI4thkQMsW8W4DKpTfHi&X-Amz-Signature=5a5f0252be097ad035dffcc37acb2d7dcf8dca32f6483819898bb86bd71f62a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G6ELQAS%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWletudBhzZuKtSuTfbzkbUTUzxX5HxHiw6NHr%2FEqYLAiBRm2fd97USV6%2BHastPBVXBZHTJYu1AfK0GhkdjlS6lpSr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMXvps%2FfXIa1d%2BnItPKtwDQFoRL%2FJiHZeLs6JRqwIIBpPjjRV0N1yC1BuSfxX0bq8vXEnohdihL%2BW86G5LH9pLW1Va9Sq%2BV%2BCW0290Ws4XLYYGlAq2COYua6eMso12vZlBJXMqvv4ieQOaGcG4DosCawYnMKiaE4KDCrWuHeAZBM7cJfJiHR4dnu6%2F1SRmpHQKHiU3ye1P%2BVX%2ButZlQREnxVHwLmMH9fT9lLrPgg4RucN6npCxZBPwFHDwZfaMb2RaG4Rz4T3%2FvGsOPxL9f86JQMRRwwIAhkG4aObtH1j7aWgWZiq4iLzVthq1JSrYu0TW4%2BCRxaQJ4XIlTDFTwbh0Rr8VJBNGdrpAn%2B9f8PCesbSgkmFfr593nTxSghRTpLKh5g5vpBHeEF%2FWw%2FHyXsV2xPDmEPrk3OiRwq96CNJmq%2FlJ2RCfrWN39ZvPrccit7%2FzNtPMoNbZnOTyUB67Ap91SueHSznDSUewJBBovxyjzo9MKYwxLxqUW4L%2BnVXUf%2FvDrlZlHo1KSZzArjZ%2Bp0lTOZUSNIVPqc6KMGN29ktU6Ynz2T9T%2FY%2FTXfhN9OeDxB%2Bcty1%2BwJYhNCp3XFGula7uvB4Vf%2Fwd1ZfFylfPon2Qau%2FjpmY8ppp0HybV2uj6guqvBaZl%2Bj%2BWCeNxpUUwk7LIzQY6pgHRMuRfqdT3P5ftfzJLPYa0iu5PdodP0cGtxUc%2FIbHvVNjxlWCs4Lb9cRCLlRY3PRBmFK%2BfS5P0ZcLTcaAU5PpxxgPLjswMa5e0VePMqyRnYkZhhIonpVhBoB8TQBfyc6VZlM8VbkimFb%2FTs8TeKNftahcHR050QwsWH0T68a%2F8i1dNHFM3NyKA%2FOH4tVRgS1UsCHqrGIdQoI4thkQMsW8W4DKpTfHi&X-Amz-Signature=3017800af7d125f7220aea29d7b2a00955b9f376689e7d1ab06e4e57e368b364&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

