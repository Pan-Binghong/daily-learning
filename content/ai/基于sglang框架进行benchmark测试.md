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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7SJYKNW%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCZwHoEBAyg2YPeUh1D3LpgGXq3raR6KSzJM1Vd74JUdQIhAO2zhjIf21XVGFP%2FzlU7oyDvqbzr%2BKsV7wGYRIM8fJ%2B8KogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVL6gZC1eQ0v0vMuUq3APQmcwrcx0b5Z3FKIZDPppg3e2ZcAqJxWQMn6FlxbRiWPRneaNZcuaLgybcw2wShfoOpy2eVBJnkYbeoDAH5XYJnf23H2%2FqYCnmw5gOLEHLgpomUarrhh60aJk%2BmS0Kbxwt6bMdZ2uUxFlpbXSo9u20QPNL4rtGrZs9ovcbO8EbfmKYvI4RxKDmY2MxrQhebtgt%2BIfyl3IKiyhg7lZZyGPyJYxRCvIsJTAx0uKxq%2BSvdDxf9k9buxr%2BfzHipNx%2BCAGLrG4VoFB1GqLEZc5CKOzNNuHLNeUnzPXUdTJWLwjG%2BN12Ltwl2a5andm9fVkTKAf6YHvOJfFVokwhto2SHdL0SHh52SB9FvLVv2W8io2Z86oJ0Tqf7xvRGJJTe0Tqo%2Bcyv8p%2F1Xb6AAyNYiLqeXkFYFumi2QBv7%2B0Ujf06yc3DJBWPP1nmUIbNOG92g%2FPq2d5AAO4D5uW7bEIhEALc1JZV9VQOgRLLR5DH6TeCPUMWYqsJtHr%2BHVtlgogynZvkx%2F6w3f6LGv%2FoFkyp7Y4mkBQ3r9gzP%2BMM6WLWldOPT6VBS3oEBF7Eg8g%2BrqV%2BXZb8Yqk39ERCXxGfKv1pZcHrWxS3mLNMySijSuqFSSojkioMiigym%2F0b%2BKDJEaXDjD5hoDMBjqkAUJK%2BwS76ry4Qmo3wvmBpDSxITxlNG0E3sDQGByReUNks8lMIkkEujBS16mnQ1bqafEhNNcAorsCNNzj%2Byx4NSQguDy%2FobLcUHQmGKh2qeWbym%2B4mJlweJuhWy6x9iybf51jJoTgEP3i6xirgjuZRclwimhrf6q7%2B6rgHHxxaEG5tiVHLyAGdhufeDiIBb5D6i3MJC%2Fs1JH6c%2Brhbigl7tsjQkMI&X-Amz-Signature=a212a773fa50708ae2ec8d3ecf74cda88480744196451247fe1ef568987a9edd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7SJYKNW%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCZwHoEBAyg2YPeUh1D3LpgGXq3raR6KSzJM1Vd74JUdQIhAO2zhjIf21XVGFP%2FzlU7oyDvqbzr%2BKsV7wGYRIM8fJ%2B8KogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVL6gZC1eQ0v0vMuUq3APQmcwrcx0b5Z3FKIZDPppg3e2ZcAqJxWQMn6FlxbRiWPRneaNZcuaLgybcw2wShfoOpy2eVBJnkYbeoDAH5XYJnf23H2%2FqYCnmw5gOLEHLgpomUarrhh60aJk%2BmS0Kbxwt6bMdZ2uUxFlpbXSo9u20QPNL4rtGrZs9ovcbO8EbfmKYvI4RxKDmY2MxrQhebtgt%2BIfyl3IKiyhg7lZZyGPyJYxRCvIsJTAx0uKxq%2BSvdDxf9k9buxr%2BfzHipNx%2BCAGLrG4VoFB1GqLEZc5CKOzNNuHLNeUnzPXUdTJWLwjG%2BN12Ltwl2a5andm9fVkTKAf6YHvOJfFVokwhto2SHdL0SHh52SB9FvLVv2W8io2Z86oJ0Tqf7xvRGJJTe0Tqo%2Bcyv8p%2F1Xb6AAyNYiLqeXkFYFumi2QBv7%2B0Ujf06yc3DJBWPP1nmUIbNOG92g%2FPq2d5AAO4D5uW7bEIhEALc1JZV9VQOgRLLR5DH6TeCPUMWYqsJtHr%2BHVtlgogynZvkx%2F6w3f6LGv%2FoFkyp7Y4mkBQ3r9gzP%2BMM6WLWldOPT6VBS3oEBF7Eg8g%2BrqV%2BXZb8Yqk39ERCXxGfKv1pZcHrWxS3mLNMySijSuqFSSojkioMiigym%2F0b%2BKDJEaXDjD5hoDMBjqkAUJK%2BwS76ry4Qmo3wvmBpDSxITxlNG0E3sDQGByReUNks8lMIkkEujBS16mnQ1bqafEhNNcAorsCNNzj%2Byx4NSQguDy%2FobLcUHQmGKh2qeWbym%2B4mJlweJuhWy6x9iybf51jJoTgEP3i6xirgjuZRclwimhrf6q7%2B6rgHHxxaEG5tiVHLyAGdhufeDiIBb5D6i3MJC%2Fs1JH6c%2Brhbigl7tsjQkMI&X-Amz-Signature=babd8189c3a0997f8f9e3342dca1784ff19acecea6f17d569f4031ce79056213&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

