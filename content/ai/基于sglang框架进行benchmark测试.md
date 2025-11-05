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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WP4SNACM%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGYR5D509EeNIulPgyDVlmdJQwr3rmO1G07izbZuP261AiEAiYaNwVjMUe9q93ftzo3Bt1Z%2Fc7CeBV4sDdm2JRDznQIqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAxsa2oWF1jazQ1JtyrcA%2FRc6naKPjQPBw34N%2BdiCycX6IFpAHSg2BoO5wz8Sn0s4IuWMOWqkdPjTQeXYRy18q%2BZLAlMWU13Yae%2BJWq%2FnLlqPtiSaQgcMctjR15EG00A5IjSTx6cjwjtYEX3myLN9DxNblwKe3gLgVZNhu2Ju7oMMQZxMc%2BRBP1ySLH59S%2BkjJtO%2BY2BTT7C38ETAg9lca2e50Z0C1VQZ2iP9R1NmAJDxmGOKTbQLu2ifJ5iqdfQ%2BZ9AaDaf2WGMjyibqEHXAeFI5l4WmUfdftMgxOzMHwYFYXT%2BvnvgBIPGwIqCrIjjUEv1NGOUW61WVNOc5mSbSymfYEwvH3C3YhLRDQq5kuGJs1l8SQerqDZLO9Y1SE9IvNekObFF%2BvLJFNzalIw8rObwdtjGsxWWWeenHBsDmEwlbW%2F3FVxVcF%2FzWFA8oFfz9Z3AoK7keZGpsDe1iWOQEfYq%2Fjb%2BUr%2BBS1kxYBlvKFjpdm4l4YlrC5EDXMybbkNmZIX8k4oiepERBlLK%2BsBsIeCiJusqTbZUbTCVXuwEQyxcN4WaNEeo%2BUsUjMJ2pGpK0KW9EmFMFo6e%2BC6bhE5XaouyiQn4P8FI5trA1SINYVhnySc24GFWqsqmIwO4H0E%2B%2Bkl42oulk%2FuJsFwCMMSfrMgGOqUBZsUuNt0BuREl5LPLzum5LEzoZQUNMJfUeoHtH4S0erwSIo8kIMuLmLn1jsSFu03sbOi3TqSBcnYBvIEZXkicvH8x9eRd5gCzMXGrkg2TmDyiB05qMMqrqy1Qf0k8Rk1GW66A3o9%2BmPVvfOc3InGDrbBYggo7A4sDbgNhv3M2Vzw0mnYmu7WNclnKe6bAwt3uwytN3WMREbCHwmUaqXKnxjlVdGjg&X-Amz-Signature=d8907f2f6e6096d8c2f278c8bde7ca828d990bfd02d665f1859d903091dbdfb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WP4SNACM%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGYR5D509EeNIulPgyDVlmdJQwr3rmO1G07izbZuP261AiEAiYaNwVjMUe9q93ftzo3Bt1Z%2Fc7CeBV4sDdm2JRDznQIqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAxsa2oWF1jazQ1JtyrcA%2FRc6naKPjQPBw34N%2BdiCycX6IFpAHSg2BoO5wz8Sn0s4IuWMOWqkdPjTQeXYRy18q%2BZLAlMWU13Yae%2BJWq%2FnLlqPtiSaQgcMctjR15EG00A5IjSTx6cjwjtYEX3myLN9DxNblwKe3gLgVZNhu2Ju7oMMQZxMc%2BRBP1ySLH59S%2BkjJtO%2BY2BTT7C38ETAg9lca2e50Z0C1VQZ2iP9R1NmAJDxmGOKTbQLu2ifJ5iqdfQ%2BZ9AaDaf2WGMjyibqEHXAeFI5l4WmUfdftMgxOzMHwYFYXT%2BvnvgBIPGwIqCrIjjUEv1NGOUW61WVNOc5mSbSymfYEwvH3C3YhLRDQq5kuGJs1l8SQerqDZLO9Y1SE9IvNekObFF%2BvLJFNzalIw8rObwdtjGsxWWWeenHBsDmEwlbW%2F3FVxVcF%2FzWFA8oFfz9Z3AoK7keZGpsDe1iWOQEfYq%2Fjb%2BUr%2BBS1kxYBlvKFjpdm4l4YlrC5EDXMybbkNmZIX8k4oiepERBlLK%2BsBsIeCiJusqTbZUbTCVXuwEQyxcN4WaNEeo%2BUsUjMJ2pGpK0KW9EmFMFo6e%2BC6bhE5XaouyiQn4P8FI5trA1SINYVhnySc24GFWqsqmIwO4H0E%2B%2Bkl42oulk%2FuJsFwCMMSfrMgGOqUBZsUuNt0BuREl5LPLzum5LEzoZQUNMJfUeoHtH4S0erwSIo8kIMuLmLn1jsSFu03sbOi3TqSBcnYBvIEZXkicvH8x9eRd5gCzMXGrkg2TmDyiB05qMMqrqy1Qf0k8Rk1GW66A3o9%2BmPVvfOc3InGDrbBYggo7A4sDbgNhv3M2Vzw0mnYmu7WNclnKe6bAwt3uwytN3WMREbCHwmUaqXKnxjlVdGjg&X-Amz-Signature=6f4ef574b021a1c7eb32ae274e552c4097481d2dd112342bed3b96489413933a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

