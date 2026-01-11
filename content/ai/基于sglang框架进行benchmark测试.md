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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB4H2BBB%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAdTwQVm1CHDOneRIWx%2Bjh7D3mnNpbpu02nWcIT0iCMZAiEA1t4eH5iet6DMt7lE%2Beem3FXIlsH9OH3B3Pgwpy5T7FQqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLBRNFX6G2j0NiKyrcA%2BQcPUZoWyh5%2FFBADSbND2y0lf7YGcuSRPZSwLmcm6KVlt0x1fyvwy8aoNbh4P1T%2FfOKkTzqtMRpZ58WOVWXOb4K3apfScH2vqKZgOpXPVLwBqL3pDZV4oPtjkFfOKiSIxEIcuNO%2F9kA24Y%2FLhPV4OF70yjBYu%2FV09n0m3xWbRJXyNHUminBzqJWEgca2i4JFkMy9Si2YFb8tnp0qa0lluBfyHu%2BfkYB7D2D%2BFMu%2Fx5ogfpBA1Z8XYHTMEv%2F%2F1Xeg3bCQc9Or2tVcaM9TKWucaEDqUlr9Td1bdAkTccGf67cP8qB3b%2B6RQxxCHnMPgageMe3j5F7wQJXbWuD6HPF1uKvkmQjZQMBuLwkuLKAXGNUHEV1RbmMxD8aSWkQKTNkbQQw3Sjkf52C6XyIhgHJDS8uiiFYaSIUBRBBqbwOk8c3lluxjBvnocUfDFFhcGierIeT1IMNwDO0Yqbdsexax%2Bqy%2FJ7JoMGIgA605UZGsNUa3npNFxEF8xHnI8B7Zj3Xtmp8SzZGsi5vYpbh3SfRw4rZ5pUPdUBJMPK7qhZVaSiq7TRKs5iOwaskQVCEusSJXLTIBPf7b2UG%2FRVjUdjWgnAfzX%2FafrKWUMWGhJISvGcmMuubtnHrkWQF1A9NMOH8i8sGOqUB%2Fq%2FZ4A82%2BXKG7mOrFDkRAlTFHKVZdFM3S1yj9yVWBfQy7nNok7C4kZG1xLrk%2FJH1eKoyVvAv3yxrbppBqM9HgftZxKaSKrAQirCGMnAipwG%2B81i9C%2FPzfSGXR5GFUtmuq%2FGqbAq7WfjS5%2Fxajy%2FJAToIknJWFvkBKnOFkDxaaer5PClR1e9emDDR90mhcrLwlJyZt4VoAWSPGgJ2fll1tE88Ohqj&X-Amz-Signature=18ea8d0e1e789ab7bd7c3265b2e1da54a92d66e13979fe7058bb4d6860bae4cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB4H2BBB%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAdTwQVm1CHDOneRIWx%2Bjh7D3mnNpbpu02nWcIT0iCMZAiEA1t4eH5iet6DMt7lE%2Beem3FXIlsH9OH3B3Pgwpy5T7FQqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLBRNFX6G2j0NiKyrcA%2BQcPUZoWyh5%2FFBADSbND2y0lf7YGcuSRPZSwLmcm6KVlt0x1fyvwy8aoNbh4P1T%2FfOKkTzqtMRpZ58WOVWXOb4K3apfScH2vqKZgOpXPVLwBqL3pDZV4oPtjkFfOKiSIxEIcuNO%2F9kA24Y%2FLhPV4OF70yjBYu%2FV09n0m3xWbRJXyNHUminBzqJWEgca2i4JFkMy9Si2YFb8tnp0qa0lluBfyHu%2BfkYB7D2D%2BFMu%2Fx5ogfpBA1Z8XYHTMEv%2F%2F1Xeg3bCQc9Or2tVcaM9TKWucaEDqUlr9Td1bdAkTccGf67cP8qB3b%2B6RQxxCHnMPgageMe3j5F7wQJXbWuD6HPF1uKvkmQjZQMBuLwkuLKAXGNUHEV1RbmMxD8aSWkQKTNkbQQw3Sjkf52C6XyIhgHJDS8uiiFYaSIUBRBBqbwOk8c3lluxjBvnocUfDFFhcGierIeT1IMNwDO0Yqbdsexax%2Bqy%2FJ7JoMGIgA605UZGsNUa3npNFxEF8xHnI8B7Zj3Xtmp8SzZGsi5vYpbh3SfRw4rZ5pUPdUBJMPK7qhZVaSiq7TRKs5iOwaskQVCEusSJXLTIBPf7b2UG%2FRVjUdjWgnAfzX%2FafrKWUMWGhJISvGcmMuubtnHrkWQF1A9NMOH8i8sGOqUB%2Fq%2FZ4A82%2BXKG7mOrFDkRAlTFHKVZdFM3S1yj9yVWBfQy7nNok7C4kZG1xLrk%2FJH1eKoyVvAv3yxrbppBqM9HgftZxKaSKrAQirCGMnAipwG%2B81i9C%2FPzfSGXR5GFUtmuq%2FGqbAq7WfjS5%2Fxajy%2FJAToIknJWFvkBKnOFkDxaaer5PClR1e9emDDR90mhcrLwlJyZt4VoAWSPGgJ2fll1tE88Ohqj&X-Amz-Signature=227ddf4aa558e56c41f4aca1814d4e221ab58f7b9b01e36c80fb0c188b57f057&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

