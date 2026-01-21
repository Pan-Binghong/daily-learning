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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IFU3IG5%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCl6nXv%2Fzqz9whW3HKxWn7PZd7Y9aIMnJiTZr%2BykOj%2FVQIhALf69QYX7q%2F9m%2BUM0mVsGkSH6%2BiCtpCTdPy0VcFEu7nnKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzgPqZjUG%2F4GzfdQWoq3AM8hN2EbZrQHWH9j2pkUrRGUVs4AARjTEOkOo5NSjX03D4ZIjQ0tVvHVfMnwtPzSbWdUdpnXe7B28ZOtySNm5jvzANVj6u2iHEJVcQa4zlLdi%2Fpoqdmbh0Pqn4wsu8INgsTQ2r7fcgxzlIXUXT7Nop2KZpUCM3Q%2F4453BkfDv1uG%2F6rlaIRPGX5lqAmNgtP1khRQ1MGQVZtu7SQVz3uCqaWomZp4%2BnGWbcYUuGSmb34h1KmMD8ZFacRz0xI7g3nkBwkaf7ap8Uzpjw8HNvYmrB4Eoicd%2BY7iEyVvuoc6JrctB%2FgHtWI2VEYRgFfLmmU%2BpNUa%2FfpOyv6JDCArtNsKDXkH9MkFDKK8kdHfSSSgMSDVpp0LYLjorqyoOaoZUHaExsMvxLt1zGqZaCkO%2FPDm1s2XcOmJTAuayZi2pZByj60mzfwRfaIyw3q57t4ekKoPVTJ%2B4eKEPf0w%2FnD3TYrGhR0Wp3nTFjNY1W2q%2BTp%2BB08W%2FgVtUvFKje90rE98bHmkCKozvT6PRBr2qPVkU7icF22pD33oaa%2FDwE4PjxQa1qSmFg5t%2FGJpd4WzXKdkr4Ms%2FgoxLR9vGKou6BA6xUJsACJi5Qc11wiF0KpPPKg1QTnZieQjmajHXhZRsf7QjCM2MDLBjqkAc8fGuQqAk2cD3WLoRM3rnH2VN7t3EqqxprKIeV06NQ85BIPGlfTcpVFoNKMOBVjS%2BPgpyZC3MwqCPC1VC4rGJ7wdeFGE5Peff8Y3%2Fz6dzB8fC%2FKwb16vZof%2F7EnXtVrWtLqN7VcQJQSo9V23G2EipIEzlBqrGlJQoAo1ydiBOVIiffIO3zXdmDVUW4edDGLy2u9lN9mk17zoXUnjKi%2Fjg6wtOyT&X-Amz-Signature=a1056f055dae5133726bd850ad1de9af7098a0191884a35da20bbf789877dc07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IFU3IG5%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCl6nXv%2Fzqz9whW3HKxWn7PZd7Y9aIMnJiTZr%2BykOj%2FVQIhALf69QYX7q%2F9m%2BUM0mVsGkSH6%2BiCtpCTdPy0VcFEu7nnKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzgPqZjUG%2F4GzfdQWoq3AM8hN2EbZrQHWH9j2pkUrRGUVs4AARjTEOkOo5NSjX03D4ZIjQ0tVvHVfMnwtPzSbWdUdpnXe7B28ZOtySNm5jvzANVj6u2iHEJVcQa4zlLdi%2Fpoqdmbh0Pqn4wsu8INgsTQ2r7fcgxzlIXUXT7Nop2KZpUCM3Q%2F4453BkfDv1uG%2F6rlaIRPGX5lqAmNgtP1khRQ1MGQVZtu7SQVz3uCqaWomZp4%2BnGWbcYUuGSmb34h1KmMD8ZFacRz0xI7g3nkBwkaf7ap8Uzpjw8HNvYmrB4Eoicd%2BY7iEyVvuoc6JrctB%2FgHtWI2VEYRgFfLmmU%2BpNUa%2FfpOyv6JDCArtNsKDXkH9MkFDKK8kdHfSSSgMSDVpp0LYLjorqyoOaoZUHaExsMvxLt1zGqZaCkO%2FPDm1s2XcOmJTAuayZi2pZByj60mzfwRfaIyw3q57t4ekKoPVTJ%2B4eKEPf0w%2FnD3TYrGhR0Wp3nTFjNY1W2q%2BTp%2BB08W%2FgVtUvFKje90rE98bHmkCKozvT6PRBr2qPVkU7icF22pD33oaa%2FDwE4PjxQa1qSmFg5t%2FGJpd4WzXKdkr4Ms%2FgoxLR9vGKou6BA6xUJsACJi5Qc11wiF0KpPPKg1QTnZieQjmajHXhZRsf7QjCM2MDLBjqkAc8fGuQqAk2cD3WLoRM3rnH2VN7t3EqqxprKIeV06NQ85BIPGlfTcpVFoNKMOBVjS%2BPgpyZC3MwqCPC1VC4rGJ7wdeFGE5Peff8Y3%2Fz6dzB8fC%2FKwb16vZof%2F7EnXtVrWtLqN7VcQJQSo9V23G2EipIEzlBqrGlJQoAo1ydiBOVIiffIO3zXdmDVUW4edDGLy2u9lN9mk17zoXUnjKi%2Fjg6wtOyT&X-Amz-Signature=3b39f9664f25fbaa255d968c3720ff3a9dd082596be4d3b3baea96741df623b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

