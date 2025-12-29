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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPEFXSBU%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuriopmxOOqFZibNw0%2B1lLPadDSHrazOcD8%2F5cB7paigIgVuO9aA5uJsD3kKo%2BrP9SNZQpN1GeJA%2Fyrsh8Ry00vuIqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdHSPNL82inrchIFircAyAROVbC0fY3z65yIueN3m7I24XjeHh%2F4jN760zS94wb0nw9h2SyDPCqe%2B3OszP4OwR21mN215yOZ9y2y8fxrY6mMTGuDQS379hFe8FykRSrvTOCEGOAr0MDcI91HpMLKTTGzOIFGWOkQTZXadJZcrzmYDLcEQ5sCHjdmJ6mikzu6bjkZcL3%2B26ZKZvxrl7pjVCthMC8o4%2FJtoaDni%2FvTvyFDko%2B0Ypvwg%2FtC17srFkQvdjyrNyMc3ShWzKynNgL8z6Jvhu%2FyNtcAvp2tE1jIEIzEJo%2Bptm%2BzWdAe24m6SdPetpG%2BOGHugWl9Vnv9H8%2BQsiemA7Rr9X9Lml6F5eMj0ceRRojv6soZm4iBtd1EfN4hqclf0gsqQj0iYlnHclkhoqmWNg9RkdZWHcwIkWOyt%2FHzEjJ0D5YW9ZVhmT6OAHkDgiIrPv68x%2FhDWaIt8sy8bGCPynjasOADnG%2BwTzY7mK7oNlq6wKp7aTR8VcG1XeVqeqwSP3bF76RtSSaA3pXnuD3p%2FgCrLn8gwvRP7vRKE2BbXCVANxFQqOqeZTgQPHJTBIeqG8i1ZdKSgx7kYTxcg0nbPQDpNUfKYL3cAFtt7fskA3%2B1KsXWsI2EAPDICZeMeltsGK%2BfdwJtScYMKWix8oGOqUBEPPpkqZMDp9MkCzdmDhYybEtr0Agi02lyEn12mFQZa9%2BW5FlVRxUyFLVgyIHPoLPilNri6z0ikikl46LXOZrvMJ66YZN8DEFIreGh7UmPSdHsnvOIYJ66oLJu09CzUWolLIZOQfX9b7MjswkvlhbvdBZgmUdSPlB7aBAZraoj%2F8J5gtW4xxCXjR52Jh2m9GC4huEKMuwnOPVEe5EuiRRzT1Z%2FepZ&X-Amz-Signature=d89150687a6f4408c9a0e43eaf0a79c375c883185a729c5f7203cbca2425de9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPEFXSBU%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuriopmxOOqFZibNw0%2B1lLPadDSHrazOcD8%2F5cB7paigIgVuO9aA5uJsD3kKo%2BrP9SNZQpN1GeJA%2Fyrsh8Ry00vuIqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdHSPNL82inrchIFircAyAROVbC0fY3z65yIueN3m7I24XjeHh%2F4jN760zS94wb0nw9h2SyDPCqe%2B3OszP4OwR21mN215yOZ9y2y8fxrY6mMTGuDQS379hFe8FykRSrvTOCEGOAr0MDcI91HpMLKTTGzOIFGWOkQTZXadJZcrzmYDLcEQ5sCHjdmJ6mikzu6bjkZcL3%2B26ZKZvxrl7pjVCthMC8o4%2FJtoaDni%2FvTvyFDko%2B0Ypvwg%2FtC17srFkQvdjyrNyMc3ShWzKynNgL8z6Jvhu%2FyNtcAvp2tE1jIEIzEJo%2Bptm%2BzWdAe24m6SdPetpG%2BOGHugWl9Vnv9H8%2BQsiemA7Rr9X9Lml6F5eMj0ceRRojv6soZm4iBtd1EfN4hqclf0gsqQj0iYlnHclkhoqmWNg9RkdZWHcwIkWOyt%2FHzEjJ0D5YW9ZVhmT6OAHkDgiIrPv68x%2FhDWaIt8sy8bGCPynjasOADnG%2BwTzY7mK7oNlq6wKp7aTR8VcG1XeVqeqwSP3bF76RtSSaA3pXnuD3p%2FgCrLn8gwvRP7vRKE2BbXCVANxFQqOqeZTgQPHJTBIeqG8i1ZdKSgx7kYTxcg0nbPQDpNUfKYL3cAFtt7fskA3%2B1KsXWsI2EAPDICZeMeltsGK%2BfdwJtScYMKWix8oGOqUBEPPpkqZMDp9MkCzdmDhYybEtr0Agi02lyEn12mFQZa9%2BW5FlVRxUyFLVgyIHPoLPilNri6z0ikikl46LXOZrvMJ66YZN8DEFIreGh7UmPSdHsnvOIYJ66oLJu09CzUWolLIZOQfX9b7MjswkvlhbvdBZgmUdSPlB7aBAZraoj%2F8J5gtW4xxCXjR52Jh2m9GC4huEKMuwnOPVEe5EuiRRzT1Z%2FepZ&X-Amz-Signature=7016909397f2abecddbd1626d3c39b1e02b12750cf6d748cd8ddfb02c597ff18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

