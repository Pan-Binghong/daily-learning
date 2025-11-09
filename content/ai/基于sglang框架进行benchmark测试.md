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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ3RNEMS%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCWoY%2BQSVxmue5mPoqssBwe3FEAnMWFpWVxyRXYMmCE7gIhAPBPVeSzzJbRXCqScPTBdSZTZOtzHxto7AUlblM2hnnkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxh%2BaACKGV2M45rwy0q3AP573WpWC%2B7MYR6IbBYcjyMCGYGt%2B30TiL89H01Ob3%2Ff4nlC4fnE70aB6mgcFGfuEMZldarb6Ut%2FuHn680dyPu0yhjxHQ5Z0nZ4cnRpTF7X0z1zuRNZDIx3Wg%2BSkRdgsu2kTpDiSKfXr1btZpFxD%2FLSmvnwEwqAPSVMhyGWwMRjCHhMtQ2HGH2cfsxujwJqBl8Vwt4Fr9jo3hM%2BjgxdaaT4AOQ3i8As4eyiu43m4m4e9GGAVCmFrONHDCIdVf0sUn6PbsHkzcf9nfsz4tdoIajyU6jzrPUQtGZt4VasqRf87R7wyvtUvAykw0XHYEPON46tIl7aotIrPmEhAaiO6jzi3zVxiKG3GeYBMlizhfUWvoMfzRnVXezOV1udIOW4U4r4hMLWlUuaJ3x6hsagy%2FDWvFEJB6J%2FX3XoKzzUGyoPMc0VXPMS8JNNDAfUI37IqrIQE9Cu1z1H4iv5QWUwXUTlACaeC3W9eMrd%2BN%2FrlimdvhpMo7ZUu4WRiTNO6iyG2UcPf1umeBwuiziDPBaYqkFWMdrb%2Bmy1GZ%2BLDyqP2IthGltTz6N4xh3KQ5q2SKG6cQC12QZWZklJyYDw3tSu5GkrmUcOZC8b0b8FqTXrcQFBlM2W%2BEPwp4AJXILQuDDwt7%2FIBjqkAUwuwWoYNA5fJh1%2FdLTAHnZcwk1cxCEv2lXdPESMTUr4UJ%2BBVBCK8gKQT6D20JiOfmaWGTowpVeLm0EnoIzaQgMenBQUgpjxgWXhGeUIhLpZRNHkjOBB8edW3E5k7Ak81yIc1w%2FeDji0KUq5vuAIaoXdmpLKd3Sd86AyKFpQca%2Fq9AGmR0u4CMmKRPeIFX8p1KddG0gFwYwdAAac18H5prkE7jJQ&X-Amz-Signature=c19638c102b9c1e1c57b66832fd6d9964cd58fb9c068e1d1111a93f06745076b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ3RNEMS%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCWoY%2BQSVxmue5mPoqssBwe3FEAnMWFpWVxyRXYMmCE7gIhAPBPVeSzzJbRXCqScPTBdSZTZOtzHxto7AUlblM2hnnkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxh%2BaACKGV2M45rwy0q3AP573WpWC%2B7MYR6IbBYcjyMCGYGt%2B30TiL89H01Ob3%2Ff4nlC4fnE70aB6mgcFGfuEMZldarb6Ut%2FuHn680dyPu0yhjxHQ5Z0nZ4cnRpTF7X0z1zuRNZDIx3Wg%2BSkRdgsu2kTpDiSKfXr1btZpFxD%2FLSmvnwEwqAPSVMhyGWwMRjCHhMtQ2HGH2cfsxujwJqBl8Vwt4Fr9jo3hM%2BjgxdaaT4AOQ3i8As4eyiu43m4m4e9GGAVCmFrONHDCIdVf0sUn6PbsHkzcf9nfsz4tdoIajyU6jzrPUQtGZt4VasqRf87R7wyvtUvAykw0XHYEPON46tIl7aotIrPmEhAaiO6jzi3zVxiKG3GeYBMlizhfUWvoMfzRnVXezOV1udIOW4U4r4hMLWlUuaJ3x6hsagy%2FDWvFEJB6J%2FX3XoKzzUGyoPMc0VXPMS8JNNDAfUI37IqrIQE9Cu1z1H4iv5QWUwXUTlACaeC3W9eMrd%2BN%2FrlimdvhpMo7ZUu4WRiTNO6iyG2UcPf1umeBwuiziDPBaYqkFWMdrb%2Bmy1GZ%2BLDyqP2IthGltTz6N4xh3KQ5q2SKG6cQC12QZWZklJyYDw3tSu5GkrmUcOZC8b0b8FqTXrcQFBlM2W%2BEPwp4AJXILQuDDwt7%2FIBjqkAUwuwWoYNA5fJh1%2FdLTAHnZcwk1cxCEv2lXdPESMTUr4UJ%2BBVBCK8gKQT6D20JiOfmaWGTowpVeLm0EnoIzaQgMenBQUgpjxgWXhGeUIhLpZRNHkjOBB8edW3E5k7Ak81yIc1w%2FeDji0KUq5vuAIaoXdmpLKd3Sd86AyKFpQca%2Fq9AGmR0u4CMmKRPeIFX8p1KddG0gFwYwdAAac18H5prkE7jJQ&X-Amz-Signature=2e862ccc02901845c9b5c9c0eea061fcc1e338d344e56fe0e92e6a9a5193481e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

