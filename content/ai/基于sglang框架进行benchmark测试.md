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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2T5WX3V%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCICP3a%2FxM5J19VJh9ZAGRnCnIjtSiQXuAxpS7V17dHfFOAiB3NP0loiw7mz%2F7MbTp3cceRlhHItlNgmZTfX4J7xfq6Sr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMOB6bVWrxmM9QHmBDKtwDlDM6X5dh%2FSi6nHnbWOGVd1A2NrRMV%2F7qIsbTWTaDZGxx1g5SV%2Fvh9VXrhHI02chIaVhPrt6Dhwy901EFbfpaG2yKhx8O%2F%2BmwVKIIPFhQ9h6ohqMDkEMPCxbGu7KtFa1TrsXX9G0xCLx1bbduwcQ%2F93%2Fq0DWIrcwl3DV7CA891Cpf4E9SlexotpcrwIsqQ4vyI%2Fcq8Pti5PomohRfc5kdc%2FZYIcWSKg%2FcMEYxTo7qy%2FoUEHFoAun5S6X6jhu3TZ%2F6qw6xydQPlwUpJGA9TT2r0%2BTWKqdcVODMPjjTmeAuo0RftMNbQNkEhVp4l44PgRcES1875xyDFphXgSDvlG9V1GhpNlQqgfTexMO%2Fx6OZDZiut1QRPLr2VhKh%2FVMu9KmyhQ6UP44wNuJHvPxOjpMX%2B7rXuruq8A%2FFcTpxdaI52lUbSRMKXTHs6TMCw0yo4k54AabbrlKg5Gs9yotq%2BPZC1EM5YL9%2FX8cd3QFbgaToNOVPQempZIL80OCOuMXZWABSDJCutilKRSKR7NRh%2BnQYjxlwn%2BPVVefXL6WESIZf8JhEiBtJABB0F%2FXPTyKm16chqgYsnN3I76Vhlw3yV9EL2zoO5u0oBlGJK3h9jj6Ht9y8ryQHOCzawxZbJYIwwLbsygY6pgFW8JnR%2B30HdlNIjgInE7skqsoR%2BEXT0QM%2FL19cQnX1ackrNQ7Qn260kzjvwhE3izV%2FbPHQWlAnLgpnzEpxDMJ4BPxvfnpphOlf6V6IPdLCj4RYrK%2BqrMD3kN8vb8rHTKE4SMqTu%2Fa4hO9NH6jKbWHEkK5BFnUUggKTKid7rZmv1KXLiylxUVXnSCVymJeHH%2B5AexEyWhtJ9hOx5q6Kx1xfrrxAuhI8&X-Amz-Signature=faa570245593ce14c8a83ec0af1f74e75c8f28d867896844ff2a8459a3a33bc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2T5WX3V%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCICP3a%2FxM5J19VJh9ZAGRnCnIjtSiQXuAxpS7V17dHfFOAiB3NP0loiw7mz%2F7MbTp3cceRlhHItlNgmZTfX4J7xfq6Sr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMOB6bVWrxmM9QHmBDKtwDlDM6X5dh%2FSi6nHnbWOGVd1A2NrRMV%2F7qIsbTWTaDZGxx1g5SV%2Fvh9VXrhHI02chIaVhPrt6Dhwy901EFbfpaG2yKhx8O%2F%2BmwVKIIPFhQ9h6ohqMDkEMPCxbGu7KtFa1TrsXX9G0xCLx1bbduwcQ%2F93%2Fq0DWIrcwl3DV7CA891Cpf4E9SlexotpcrwIsqQ4vyI%2Fcq8Pti5PomohRfc5kdc%2FZYIcWSKg%2FcMEYxTo7qy%2FoUEHFoAun5S6X6jhu3TZ%2F6qw6xydQPlwUpJGA9TT2r0%2BTWKqdcVODMPjjTmeAuo0RftMNbQNkEhVp4l44PgRcES1875xyDFphXgSDvlG9V1GhpNlQqgfTexMO%2Fx6OZDZiut1QRPLr2VhKh%2FVMu9KmyhQ6UP44wNuJHvPxOjpMX%2B7rXuruq8A%2FFcTpxdaI52lUbSRMKXTHs6TMCw0yo4k54AabbrlKg5Gs9yotq%2BPZC1EM5YL9%2FX8cd3QFbgaToNOVPQempZIL80OCOuMXZWABSDJCutilKRSKR7NRh%2BnQYjxlwn%2BPVVefXL6WESIZf8JhEiBtJABB0F%2FXPTyKm16chqgYsnN3I76Vhlw3yV9EL2zoO5u0oBlGJK3h9jj6Ht9y8ryQHOCzawxZbJYIwwLbsygY6pgFW8JnR%2B30HdlNIjgInE7skqsoR%2BEXT0QM%2FL19cQnX1ackrNQ7Qn260kzjvwhE3izV%2FbPHQWlAnLgpnzEpxDMJ4BPxvfnpphOlf6V6IPdLCj4RYrK%2BqrMD3kN8vb8rHTKE4SMqTu%2Fa4hO9NH6jKbWHEkK5BFnUUggKTKid7rZmv1KXLiylxUVXnSCVymJeHH%2B5AexEyWhtJ9hOx5q6Kx1xfrrxAuhI8&X-Amz-Signature=2bed12efe5fd86bf13091408b80d915d94bd7c926c465d3c16e352abff754e54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

