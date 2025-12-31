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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZKZSQL5%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDA%2BesIxosG2JWmaNOOeETFbY4vzXU4Slu4nG6S5ZdeBQIhAO2I%2BW1s%2Fg3%2Bx05Q6dH7AnhiHcNKKDeaB2qFPu0w7CjUKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzyss7tPT7UoojT9toq3APpUwFYRS9%2FDEULcg2GQIySinszFTgqDaC9hD98x%2F%2FVGkmnFU1eyEc1SLavlhlng7%2BIY%2F8uWDyFh0m3NoZVWgDFbKZq9AJlV9l3%2BBO1COb7OyuN0IReVL6qXUC7xYy%2Fg91EPy5mTyfWJHUZqfltGoildKCeMT3ZQkkvBe0yj4YWYFzxfex7ruGDOw83HgVlsLR9tSqyklF3ld%2BtrNxixR0MN%2Be3Zjm0g%2FJMt%2B4YSfj6pfnd4%2B4M%2B6CPfTAT5%2FiA0kXSxso3Vun7q%2FoQ%2BCDW7JDB%2FFMt2uzc0e5uX2g%2BnsYX%2FXjhHK6GQc5G%2FeT2hi%2FCEHSkwEMBPb4rBXNpcjb9%2Be8p9YW2MKAiedKYE%2FZI9GQNJYw0VP5ew5dJCpNEscXZiEi%2F7mdPZvmO0WsvT5Oxc2Wz3YTqq5m6%2BQYfRH8KEl3qMmqYBnKnvTwWznRQ4yfQcxm21ablgGXxzNSfleTPEuGO600dxaxNrFQWSlwLyaVbnuM82K0a9cXOoevCK%2BGeZGV%2BuCbx60c0iJbGykCDdVGDBtlqnkCaIH9iUQ6EAV3CB%2FKduFXPkBXrZrp03fqMCgQ2zPEAgymAjToVtNfLwhrdEXV%2Bt7frtZwmrJbKrDau0259rI4oTHheZvv2UDDd99HKBjqkAfNvfxHZWcvttVsSw3lZEh6TtvjqkFDuP0TiEJFU%2Bwz29bkUX8oKqkfQCrstYEYd%2FRNrZfVkeDDsgBHKDw0aT4OS7tqpOYQWUk0yeyHphIVeaB0Gx0ZWHtWShnhtGn0JVUThJHy2qtR5JEGh1dL9X1RO6DxtRvv8AM2%2FJZxT7N2Fokza57zPHDT1gh7CVq1u%2FBBrvtQ5pW%2FFN1ELO6rFVh1okZwU&X-Amz-Signature=10bbb0d021c0f46af1b583d24edae26de046872bf2d4dc0df82b7c87dcc77c48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZKZSQL5%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDA%2BesIxosG2JWmaNOOeETFbY4vzXU4Slu4nG6S5ZdeBQIhAO2I%2BW1s%2Fg3%2Bx05Q6dH7AnhiHcNKKDeaB2qFPu0w7CjUKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzyss7tPT7UoojT9toq3APpUwFYRS9%2FDEULcg2GQIySinszFTgqDaC9hD98x%2F%2FVGkmnFU1eyEc1SLavlhlng7%2BIY%2F8uWDyFh0m3NoZVWgDFbKZq9AJlV9l3%2BBO1COb7OyuN0IReVL6qXUC7xYy%2Fg91EPy5mTyfWJHUZqfltGoildKCeMT3ZQkkvBe0yj4YWYFzxfex7ruGDOw83HgVlsLR9tSqyklF3ld%2BtrNxixR0MN%2Be3Zjm0g%2FJMt%2B4YSfj6pfnd4%2B4M%2B6CPfTAT5%2FiA0kXSxso3Vun7q%2FoQ%2BCDW7JDB%2FFMt2uzc0e5uX2g%2BnsYX%2FXjhHK6GQc5G%2FeT2hi%2FCEHSkwEMBPb4rBXNpcjb9%2Be8p9YW2MKAiedKYE%2FZI9GQNJYw0VP5ew5dJCpNEscXZiEi%2F7mdPZvmO0WsvT5Oxc2Wz3YTqq5m6%2BQYfRH8KEl3qMmqYBnKnvTwWznRQ4yfQcxm21ablgGXxzNSfleTPEuGO600dxaxNrFQWSlwLyaVbnuM82K0a9cXOoevCK%2BGeZGV%2BuCbx60c0iJbGykCDdVGDBtlqnkCaIH9iUQ6EAV3CB%2FKduFXPkBXrZrp03fqMCgQ2zPEAgymAjToVtNfLwhrdEXV%2Bt7frtZwmrJbKrDau0259rI4oTHheZvv2UDDd99HKBjqkAfNvfxHZWcvttVsSw3lZEh6TtvjqkFDuP0TiEJFU%2Bwz29bkUX8oKqkfQCrstYEYd%2FRNrZfVkeDDsgBHKDw0aT4OS7tqpOYQWUk0yeyHphIVeaB0Gx0ZWHtWShnhtGn0JVUThJHy2qtR5JEGh1dL9X1RO6DxtRvv8AM2%2FJZxT7N2Fokza57zPHDT1gh7CVq1u%2FBBrvtQ5pW%2FFN1ELO6rFVh1okZwU&X-Amz-Signature=319b3c4d6870f11a9603ea870b529e67ee91d50442d5eba35a1294b530e793ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

