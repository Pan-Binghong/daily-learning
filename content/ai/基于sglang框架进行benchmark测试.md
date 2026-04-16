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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5YCFWG%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHkhgtBRMLEoo2p6KJlTSZmTxFTL7919Wxu83xLbWVfQIgHkkgt%2BFWpiJhjYxDQEdF7qolXzFb28MtyMOQJpxDb%2B4qiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDz8tjcQ%2F1gkjdsAUyrcA9ujQ68MZE%2B7CIIZACflyLlEPrmWfKyG958s44P7Q%2BTOSZuveN3owX%2FRjXSDhH4A9wgpHddws%2FL%2FhRQmHgNaP54hvyo7eWKKA%2FDIrJ%2Bp5qRfroW6uePPHFcmVRZfjElpKH2mEQOoS2uwiYTewv4AFKmaDm%2B1GyogKHTTmUBJ7S7FqEvFTY9pbWnfBzH6sLx%2F5ouJKIv%2FAL9dkA2Nz840j2K6bIW5dIBF2HxkRvjIdcmVzEiT8XfVZKI73qFyfUEJv2FQHdBQPVE1D6dJS620guXvqhB7y0N4xqvMraL4cSy1886GcF3ZZSmVdBi4H30BJgauhxBWjqkV%2FDRSn5uWQj%2B%2BGicv6iYRjg4pM5tiDQT7iIzIkGPG%2BbM6ZsnEZ7tESw8056P%2BSLwoC4QA2Fsiw55ZBbaQw19kHBu4CnYA4Yw9x5eRt1fjELmgD1SJc6C0LgiQhCbC5O8gkeAiXMDIkWiJXO2o6WZECo6nx68VJDPOknWQ74NbYopE5PB8WHiQtQDi2hoDGoeoe9kgCfyr9Qj%2F57E9cC51BAY2SIHZ6r3atJysxMkA3z0JKAPpg6TYDlWfTXjOMlLynE6WLPIjgW4C7QZRTLL0HzK%2Bk8wRoM%2Fm5RARu9W0rHS39cKqMMCzgc8GOqUB8w6L707IVAjn757Ftv4X%2B2XQIXqvc61q4rU68umR2Abd5rPtSPONWb1u7obl1wfLgTdzXBixuYcWE36TBE%2BLEaCGJ7dg6%2BAhT29PBq4E4s391wiuo6Qyy%2FWAckhC55RVokHmMMPWZ2qlMDsSrlhTr9v3RV%2B0HYVDkY6xQV%2Fov675LoSzL4%2Fdz8kHsdI90t%2FYd5vS3T9EpgA0YqW%2F3%2BxBb3oJmi8s&X-Amz-Signature=9c9bb219655348b7d087b1c623795898a06e43ba0677e6e262485f096b9e851d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5YCFWG%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHkhgtBRMLEoo2p6KJlTSZmTxFTL7919Wxu83xLbWVfQIgHkkgt%2BFWpiJhjYxDQEdF7qolXzFb28MtyMOQJpxDb%2B4qiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDz8tjcQ%2F1gkjdsAUyrcA9ujQ68MZE%2B7CIIZACflyLlEPrmWfKyG958s44P7Q%2BTOSZuveN3owX%2FRjXSDhH4A9wgpHddws%2FL%2FhRQmHgNaP54hvyo7eWKKA%2FDIrJ%2Bp5qRfroW6uePPHFcmVRZfjElpKH2mEQOoS2uwiYTewv4AFKmaDm%2B1GyogKHTTmUBJ7S7FqEvFTY9pbWnfBzH6sLx%2F5ouJKIv%2FAL9dkA2Nz840j2K6bIW5dIBF2HxkRvjIdcmVzEiT8XfVZKI73qFyfUEJv2FQHdBQPVE1D6dJS620guXvqhB7y0N4xqvMraL4cSy1886GcF3ZZSmVdBi4H30BJgauhxBWjqkV%2FDRSn5uWQj%2B%2BGicv6iYRjg4pM5tiDQT7iIzIkGPG%2BbM6ZsnEZ7tESw8056P%2BSLwoC4QA2Fsiw55ZBbaQw19kHBu4CnYA4Yw9x5eRt1fjELmgD1SJc6C0LgiQhCbC5O8gkeAiXMDIkWiJXO2o6WZECo6nx68VJDPOknWQ74NbYopE5PB8WHiQtQDi2hoDGoeoe9kgCfyr9Qj%2F57E9cC51BAY2SIHZ6r3atJysxMkA3z0JKAPpg6TYDlWfTXjOMlLynE6WLPIjgW4C7QZRTLL0HzK%2Bk8wRoM%2Fm5RARu9W0rHS39cKqMMCzgc8GOqUB8w6L707IVAjn757Ftv4X%2B2XQIXqvc61q4rU68umR2Abd5rPtSPONWb1u7obl1wfLgTdzXBixuYcWE36TBE%2BLEaCGJ7dg6%2BAhT29PBq4E4s391wiuo6Qyy%2FWAckhC55RVokHmMMPWZ2qlMDsSrlhTr9v3RV%2B0HYVDkY6xQV%2Fov675LoSzL4%2Fdz8kHsdI90t%2FYd5vS3T9EpgA0YqW%2F3%2BxBb3oJmi8s&X-Amz-Signature=632735daa154e6a5a49ca17dd2a299fabf9a9552ca3e1a036823f850d0975604&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

