---
title: 基于SGLang框架进行Benchmark测试
date: '2025-03-21T00:33:00.000Z'
lastmod: '2025-03-21T02:46:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSTFVDJN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr5xFrPpo47vgkqLzP6tL9vny7SHwKde3rnHaRkmPCpAiEAlIQ6G%2BKderHVu5EosYWlnbNa0BoHd6%2BWHTQrc7kq8oMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhByKHnB1ZUaeoc5yrcA%2Fg%2Bu7rvEPva8dGRKXQq6CcelWCbygk0xIhIx86LdO6ISH%2FZE9qjCYH5MAGvvCF3FDK%2F22FYmvbq6mUm0cdRYVQIV7Sd4Qmw6a44vbwJRa6ywfmbVaSHH2XvmafnoJ%2BjxVNjpOOoDyQFez6DM8mqO3vQbmGrtHovXmpj4TaKhBtFEbeOPjaJ7LdgXjQUmmkrlaSQfveY5wj3ALToWQlZcWZBmWaUw4BZ1TvlmKsMGeTTnOu71wFUNg%2FBOTjTZSdolFR1IytCGyr31%2FprVj%2FqscDiXNKXJYGByJf7Ti%2FCSleH%2FR9CTXzEfslDduZZwTETxapXviEvqn0KIx%2B15m68TJrduonv4mIhXPHZ73ZoszgjuvADh1OFn78zfEEL%2FBa8ekmFJdKuLnPCccrOjoK0g2YhtdwTkYbgB5oZh6CserEax3AjlCEpKBpIMruO7IQ9UA2HNIBacnFwVCehviyNcJQScgYJQFBCe%2BAm880LiuqY5a0TNTeVtPOoQHDPlJdx0iuXeDqvml%2BEgHjsFqH%2BRKk6RFcRa%2BgVQvZEYBtu4ebmI9p%2BjwpAypUpswbmHF1A5x9B3YVdO1MLCSYFA3QshT6KmTOJspQk78T4u765buI6Z%2B%2FUFpZI0Q9VMs3CMKijrMgGOqUBRRPLeLCacIsxxJXaeR8beYIIiGyz9drsFKNBmQWtgNw3SY8rTr%2BQWjY7NXzgUMkD2qojTUqFJAJlJBBm8CSk0r66HKLokQtB2wK6HTsksmLO%2FuIMog1xPZ6wzui8yWj%2F49DC9QrXGT7MOSFPjKRVasoLGqym1VBTfBOx%2FjNLLHnWRHELgabPABqOXn8kxDyO6VUB%2FRZ0nnhIN71DoyWxwLq7C74y&X-Amz-Signature=29214d4fb7ea881640ccfe9d72aa16d2e719f053f0daa9545de4b8c9b3eb2ab7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSTFVDJN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr5xFrPpo47vgkqLzP6tL9vny7SHwKde3rnHaRkmPCpAiEAlIQ6G%2BKderHVu5EosYWlnbNa0BoHd6%2BWHTQrc7kq8oMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhByKHnB1ZUaeoc5yrcA%2Fg%2Bu7rvEPva8dGRKXQq6CcelWCbygk0xIhIx86LdO6ISH%2FZE9qjCYH5MAGvvCF3FDK%2F22FYmvbq6mUm0cdRYVQIV7Sd4Qmw6a44vbwJRa6ywfmbVaSHH2XvmafnoJ%2BjxVNjpOOoDyQFez6DM8mqO3vQbmGrtHovXmpj4TaKhBtFEbeOPjaJ7LdgXjQUmmkrlaSQfveY5wj3ALToWQlZcWZBmWaUw4BZ1TvlmKsMGeTTnOu71wFUNg%2FBOTjTZSdolFR1IytCGyr31%2FprVj%2FqscDiXNKXJYGByJf7Ti%2FCSleH%2FR9CTXzEfslDduZZwTETxapXviEvqn0KIx%2B15m68TJrduonv4mIhXPHZ73ZoszgjuvADh1OFn78zfEEL%2FBa8ekmFJdKuLnPCccrOjoK0g2YhtdwTkYbgB5oZh6CserEax3AjlCEpKBpIMruO7IQ9UA2HNIBacnFwVCehviyNcJQScgYJQFBCe%2BAm880LiuqY5a0TNTeVtPOoQHDPlJdx0iuXeDqvml%2BEgHjsFqH%2BRKk6RFcRa%2BgVQvZEYBtu4ebmI9p%2BjwpAypUpswbmHF1A5x9B3YVdO1MLCSYFA3QshT6KmTOJspQk78T4u765buI6Z%2B%2FUFpZI0Q9VMs3CMKijrMgGOqUBRRPLeLCacIsxxJXaeR8beYIIiGyz9drsFKNBmQWtgNw3SY8rTr%2BQWjY7NXzgUMkD2qojTUqFJAJlJBBm8CSk0r66HKLokQtB2wK6HTsksmLO%2FuIMog1xPZ6wzui8yWj%2F49DC9QrXGT7MOSFPjKRVasoLGqym1VBTfBOx%2FjNLLHnWRHELgabPABqOXn8kxDyO6VUB%2FRZ0nnhIN71DoyWxwLq7C74y&X-Amz-Signature=c91c0d2a5164b79e4925d2753fc5cd611654ac60e68b89929243b0f22cd37f90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

