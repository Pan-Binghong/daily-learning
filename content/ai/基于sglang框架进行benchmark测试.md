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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHEZCRA%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICewncFY7L0mYmqJU2Zx%2F1d3R8X9POYl2wsr03deVF7SAiEA62xSyUOgPyH7TTwRcaDXn1NnDwvSvwSrfnMTnL3rK%2FUqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCSnDrCmgNVm%2ForjlircA%2F3n%2BfIDVzluD7jBaAQoonphM7OF69pcaaRQtcN4Qro3E4MuNJnThYO1myap87ChYvQdATim%2BiSu0YSs2LUtIjMs84Dby3h1nu6xoBb7IVjwh5uO5xwSU2UOrn445GVh4RKpyFFaqGhbp6TkR2EQLk68ocvP55tYC96NwWpIMr7yIH%2FjFyPUjnElr2oe5OHTAsL0rs2nn%2FP%2BCxDWoGSc9X7vj8WG5IRjnDIEv%2BDnXt9kWXxt7Y1hhywGZ%2B722gjEewRz4529WAEvCq3sAcaG0G0jdg%2FUBnpgcZ%2FjkBFzQTRgoCPpPTvrx5WPJGaKGOMTUPiPd9rdRWA6Cab6EA3DzUg9vwEE0hZ2ZckdfhfKEzaJaqukMV%2FAVI6LcquUmPpIkau2OW0LS61pYYiNT58vV7860gg9GLvNmpGS1I6VNYTwzgDI10oEEVdMBnTXxlNdvsMthNc8cU7j0BYtWDvfwP84IrRTYthj0Q49TvGObNLhZ7qXsex0m4QMlVHHhNUsUwNB%2F6ratKIkufR%2BVUu993WJLOz80t1Mrn6XXR96Eht8xWWufWlkLIbm0YCiy5jno%2FdBEuQMPajdf5%2FuvSEZcEnYURW6ogmn4V6vmh7G1%2BeuZGAIwyCkqTRqKc3uMO%2BQ38wGOqUBB%2Bb5ixYoR2RfjbOa5pLKS52YlhO3Cvrh6VWa4P5yueAJos2XTqotrk5%2B47TOg3aibaVTDz%2FhWGxZ0xmGUjfCB5Mje9oUVwfHto8HQbavywmqGP%2FGwK4xcrD0Mr02xD3%2FjdoHDhSNHN4IuRKnIEHa2WyZmlCsfFV32v5i0pvuu9zMCnLFJTVHWPgZDZpu0KZsRnmKMgfsD5cfZmvDTh24BRvC8KfQ&X-Amz-Signature=f35bc9cc4586c448c22d3002b015b52c10fee6da26878ccf1c96d533de9977fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHEZCRA%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICewncFY7L0mYmqJU2Zx%2F1d3R8X9POYl2wsr03deVF7SAiEA62xSyUOgPyH7TTwRcaDXn1NnDwvSvwSrfnMTnL3rK%2FUqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCSnDrCmgNVm%2ForjlircA%2F3n%2BfIDVzluD7jBaAQoonphM7OF69pcaaRQtcN4Qro3E4MuNJnThYO1myap87ChYvQdATim%2BiSu0YSs2LUtIjMs84Dby3h1nu6xoBb7IVjwh5uO5xwSU2UOrn445GVh4RKpyFFaqGhbp6TkR2EQLk68ocvP55tYC96NwWpIMr7yIH%2FjFyPUjnElr2oe5OHTAsL0rs2nn%2FP%2BCxDWoGSc9X7vj8WG5IRjnDIEv%2BDnXt9kWXxt7Y1hhywGZ%2B722gjEewRz4529WAEvCq3sAcaG0G0jdg%2FUBnpgcZ%2FjkBFzQTRgoCPpPTvrx5WPJGaKGOMTUPiPd9rdRWA6Cab6EA3DzUg9vwEE0hZ2ZckdfhfKEzaJaqukMV%2FAVI6LcquUmPpIkau2OW0LS61pYYiNT58vV7860gg9GLvNmpGS1I6VNYTwzgDI10oEEVdMBnTXxlNdvsMthNc8cU7j0BYtWDvfwP84IrRTYthj0Q49TvGObNLhZ7qXsex0m4QMlVHHhNUsUwNB%2F6ratKIkufR%2BVUu993WJLOz80t1Mrn6XXR96Eht8xWWufWlkLIbm0YCiy5jno%2FdBEuQMPajdf5%2FuvSEZcEnYURW6ogmn4V6vmh7G1%2BeuZGAIwyCkqTRqKc3uMO%2BQ38wGOqUBB%2Bb5ixYoR2RfjbOa5pLKS52YlhO3Cvrh6VWa4P5yueAJos2XTqotrk5%2B47TOg3aibaVTDz%2FhWGxZ0xmGUjfCB5Mje9oUVwfHto8HQbavywmqGP%2FGwK4xcrD0Mr02xD3%2FjdoHDhSNHN4IuRKnIEHa2WyZmlCsfFV32v5i0pvuu9zMCnLFJTVHWPgZDZpu0KZsRnmKMgfsD5cfZmvDTh24BRvC8KfQ&X-Amz-Signature=92e0143aa87ec3a2384b1b98d95a9b143218b387365a5b0ebff7c8592eef3bc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

