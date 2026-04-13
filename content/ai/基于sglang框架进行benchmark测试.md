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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKOQRYGH%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGopZD%2BR3LaysPoGvP2ACgiTPeL7YRfQUWhcu6MtLW5EAiEAiOAYmE96742LY0xcJrwJGEDGYqWJ5Z5gf7ZLAWVxOhUq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDLlfRBRQ5O%2BofqBXsircA4oVqz0dEOvzBbBN%2BqgqEjgZV97rhp%2BuTM5AqX8eiYP3LuIOtQSn7GuPBETLngj2995g5KHsLMBJJBIRB1Zt2AsODXdmdLfWZD3ngt%2FC31RZ5gh7ClG8SHUNMtVCxMYskUR7erSfvB67b6zGX4WvsEZ%2FEG%2ByRW1q3q9neCkeoHIag5KwheF0PFNC%2FqsmyTarGN7C6DOL9ttu2MyDQIOKAKcsMUvwuBtLwH8LrAce%2F%2FTr%2FL2uYQnz31%2FXQjfh42LYf15K51ij3M4BlPR%2FgDGAZIpyugJIb2s8kszv0FqXiKVlisQrOddDdVzkUTqg4KtabGJspWJ%2BFzE7Le6FJ43SDyk2SJG2UehitggLr0Qiz%2FY2oN14VmW3KSIq6yF1ex1XIMbBUaxrdPg%2B2mvq5a2ZV5%2BK26P0X2GkC4vvoIf79X07g2XMNdNbSQ3cKBfGHwdFpBqTmc%2FNk7z3afrMeuRz7o9wFTXflXWOqJT2jO%2FgH9OqFDQKdBZrLpWMdDv0g6B%2B7pjBht4w%2FbiPwhmI8cwu359CG%2B0twuhPsL%2ByiGg7CuVH5G4caFOQ%2BLDkxphCwGJsgdHaaDbtsOigPKuE%2BSAZDP22uAgLLqT0HbBINEYc76QX7nwYb0g8ZnpkIl8lMIOy8c4GOqUByIctDpDP9j%2FUlHAjbFhUjJ5rnAGBJoHLB9W%2FxdxW0adRxfBvC7%2B9NW%2BNnEmjla7dOFVraBEOUq3E93pMfQov%2BYVl%2BHUb613TWQz5Z7dlVPWzkhIDjDoEDhZ4bg7C9Ns1N1%2F9EVOwKBnkKG%2FXlCGKsAkQSqtrL%2BcwojOUySDKRljXejgs7rRni5hvLKByFhVDVXeJd9g%2B3qadpBBneRCg53742dLK&X-Amz-Signature=100d301d02671ca07aa2059cb3d2d9d8559b1148698146fc920e8138a76660d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKOQRYGH%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGopZD%2BR3LaysPoGvP2ACgiTPeL7YRfQUWhcu6MtLW5EAiEAiOAYmE96742LY0xcJrwJGEDGYqWJ5Z5gf7ZLAWVxOhUq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDLlfRBRQ5O%2BofqBXsircA4oVqz0dEOvzBbBN%2BqgqEjgZV97rhp%2BuTM5AqX8eiYP3LuIOtQSn7GuPBETLngj2995g5KHsLMBJJBIRB1Zt2AsODXdmdLfWZD3ngt%2FC31RZ5gh7ClG8SHUNMtVCxMYskUR7erSfvB67b6zGX4WvsEZ%2FEG%2ByRW1q3q9neCkeoHIag5KwheF0PFNC%2FqsmyTarGN7C6DOL9ttu2MyDQIOKAKcsMUvwuBtLwH8LrAce%2F%2FTr%2FL2uYQnz31%2FXQjfh42LYf15K51ij3M4BlPR%2FgDGAZIpyugJIb2s8kszv0FqXiKVlisQrOddDdVzkUTqg4KtabGJspWJ%2BFzE7Le6FJ43SDyk2SJG2UehitggLr0Qiz%2FY2oN14VmW3KSIq6yF1ex1XIMbBUaxrdPg%2B2mvq5a2ZV5%2BK26P0X2GkC4vvoIf79X07g2XMNdNbSQ3cKBfGHwdFpBqTmc%2FNk7z3afrMeuRz7o9wFTXflXWOqJT2jO%2FgH9OqFDQKdBZrLpWMdDv0g6B%2B7pjBht4w%2FbiPwhmI8cwu359CG%2B0twuhPsL%2ByiGg7CuVH5G4caFOQ%2BLDkxphCwGJsgdHaaDbtsOigPKuE%2BSAZDP22uAgLLqT0HbBINEYc76QX7nwYb0g8ZnpkIl8lMIOy8c4GOqUByIctDpDP9j%2FUlHAjbFhUjJ5rnAGBJoHLB9W%2FxdxW0adRxfBvC7%2B9NW%2BNnEmjla7dOFVraBEOUq3E93pMfQov%2BYVl%2BHUb613TWQz5Z7dlVPWzkhIDjDoEDhZ4bg7C9Ns1N1%2F9EVOwKBnkKG%2FXlCGKsAkQSqtrL%2BcwojOUySDKRljXejgs7rRni5hvLKByFhVDVXeJd9g%2B3qadpBBneRCg53742dLK&X-Amz-Signature=0fc4e6c4131c46dde61867a9198ba77df56b229861bcfe0cc552439672f950bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

