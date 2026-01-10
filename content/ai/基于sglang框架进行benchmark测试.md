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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HVLKIMU%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEf5suP%2FkrHYJKY7ke88AJj06aY4wXsIku8lpUk13Bi9AiEAo0CtiGFECN1KvlzPq4HO9TVc%2BLcV4nRmEJ1qV3pqRmgqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMC70tUgXXtETfuAVircAyEB%2BfLp9%2Fb1KFsp9pYgvh04Vh2Lxx1r6nnigA4I0o35VHdjjhCuBOfZBCEsHc0bMvu60OH9qvmcKUaBsjPCqPRLWqFdSzVSOOlCfnjTpEj2KKrvJcV4O%2B7F23Q%2FPXR%2FcL7O%2BKF1v9djfiCSCyPVRw3CliOjC0OyIva5M8srFgVcWIrFWmB9NHJLifQyKAaG35frmnqIkXrTOi3RPi4I4eKAMwNOaLOmM59IEr9UB4oxkgMq%2F2Kd%2BQuW7hHBXYUFEn6ZbBoYbAueXhYfa5Rh41ZthSjVUqRwXUIkZC%2F0oJFDrz0kUOzcRPin227IgSA%2BvjGPTvpVpezPIFssuQh3V8lpIZ7EIH2sKeVzdU92yH0r0yWR4qr7VapX2EmRYCKmzKrjp0salJRneiaEgI7y9RVhkCikQ9nO82XTv9QzqRMm7RIRG0qR683H%2BTfYlrgisNbGjycU9ex3RSo4sk%2Fxp7fTjvZPve4rHEuHlfkOty4GHBmwaEMbc%2FlWP%2FZpF8Eh7e3OUdXXdqbF4xIAW6llVWYKSBppTgbjH78oL9gZtnWXbiUrSDRYjvNoh%2FkArAooNUikOU8vO6lpctVGOjuvrE3IMxczNMXLjaZtUn1vtNyWfusIZDu9YFz1K9j%2BMPz4hssGOqUBVS%2Bg2eRU%2FCXctG0owBO7pHHX8jZBQA1KQ0yazo4odVHat%2BhWyACC4MKuQPXZBl8skuIIVy0kzDJkluR33TV0%2B3zufXlO8lckztQM09EfUzoNI6sbAOq7F4C4dFET8F8ilYiWfEDRgrzCyhfGClKtko3vQUDoRk5bAzPv%2BfINdPjIXGSMrJNCZWTJHmfm7rU7m7U6lfRsDoHiHMl4TspSporARzDM&X-Amz-Signature=f83864d234a115f1f48f6b074ad8170169b9ab67d99b56efb596008da14f7af3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HVLKIMU%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEf5suP%2FkrHYJKY7ke88AJj06aY4wXsIku8lpUk13Bi9AiEAo0CtiGFECN1KvlzPq4HO9TVc%2BLcV4nRmEJ1qV3pqRmgqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMC70tUgXXtETfuAVircAyEB%2BfLp9%2Fb1KFsp9pYgvh04Vh2Lxx1r6nnigA4I0o35VHdjjhCuBOfZBCEsHc0bMvu60OH9qvmcKUaBsjPCqPRLWqFdSzVSOOlCfnjTpEj2KKrvJcV4O%2B7F23Q%2FPXR%2FcL7O%2BKF1v9djfiCSCyPVRw3CliOjC0OyIva5M8srFgVcWIrFWmB9NHJLifQyKAaG35frmnqIkXrTOi3RPi4I4eKAMwNOaLOmM59IEr9UB4oxkgMq%2F2Kd%2BQuW7hHBXYUFEn6ZbBoYbAueXhYfa5Rh41ZthSjVUqRwXUIkZC%2F0oJFDrz0kUOzcRPin227IgSA%2BvjGPTvpVpezPIFssuQh3V8lpIZ7EIH2sKeVzdU92yH0r0yWR4qr7VapX2EmRYCKmzKrjp0salJRneiaEgI7y9RVhkCikQ9nO82XTv9QzqRMm7RIRG0qR683H%2BTfYlrgisNbGjycU9ex3RSo4sk%2Fxp7fTjvZPve4rHEuHlfkOty4GHBmwaEMbc%2FlWP%2FZpF8Eh7e3OUdXXdqbF4xIAW6llVWYKSBppTgbjH78oL9gZtnWXbiUrSDRYjvNoh%2FkArAooNUikOU8vO6lpctVGOjuvrE3IMxczNMXLjaZtUn1vtNyWfusIZDu9YFz1K9j%2BMPz4hssGOqUBVS%2Bg2eRU%2FCXctG0owBO7pHHX8jZBQA1KQ0yazo4odVHat%2BhWyACC4MKuQPXZBl8skuIIVy0kzDJkluR33TV0%2B3zufXlO8lckztQM09EfUzoNI6sbAOq7F4C4dFET8F8ilYiWfEDRgrzCyhfGClKtko3vQUDoRk5bAzPv%2BfINdPjIXGSMrJNCZWTJHmfm7rU7m7U6lfRsDoHiHMl4TspSporARzDM&X-Amz-Signature=fbf7a0221306d7b49cfc6f431f9cefe32c9daae9ca19fa9702a4b6a856badc43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

