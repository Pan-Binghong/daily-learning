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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT4BFBDZ%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQD3XOwKJqBO0cVh1phI1aUgMYdVThcCs%2FKmwOHYHVcCpQIgEVlLD7je8KA9KuqQliwOEuDjDaQwyEbOeNve8VIl7Ucq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDBs5o6fWlI0oT3QIZSrcA0LRlMECfMRgb%2B1mLDnGSgoOsgAw3gcA7vRJCsnG69O43Ca9H13Sdix6HgCL21DVvo%2B0uJKM%2FAiVq7GMK31ZPViBT5dJ7E%2FhVX9kkNPBYzW8jPWSz7pwQKbGIsh0LNZbiXta8fc5QBkJsDut%2Brpdec5s1Vn3Wqg0h5yMjLRyrxALPLcq6v1ilDCac%2F%2FjedRDVuvgrPLjBynSamH7NUWXc2BLMa8ESfNkIAdWmCwVcPe3AQmtA90yMp1xzvSRCivFzqU6b6IKNw4xIKflNxF8wBevdE7xaZ9sLZ8BSsDBHBEx2u2QMWj6Uz%2FPUbs9nA08MhknxlcORutyQyL9Xj%2FQjzF05ETzQHQsCcfr8%2BJdUZ92DIWSautVXVJQc0fGUygoQTllu7h%2Bn4bBSfZN%2FLZ3hJpCZ3GmDVDsh0RfVq978z%2FxCECKUGcIT2%2BC5PJTv%2F5th9ZmOADohd2qaUkg5i3yP6INsJR51KxbB5JvQv0mmBQ2%2BvuZswiuQ2FKt%2F9BUTvv1ik4JwYLYJmDr34ujGTdMaS%2BiFKomdeYGApzbwvIv9uwpV7zL6Nhen7%2B1r7InmZxIjBYte%2FF62qL2lSLQAIoeXu2F6UXdUCL1RMbFnI0ajsP8PXEavQw54JX%2BZHgMKnCs80GOqUBud1eY1BmJtMX1L1Qe%2FYxLnmzqLzbKUaYF34SWZbSCm5YlQrIfg8LHsb%2FFM6hsnlApYcu4t5pOMJefe%2FVvLZK7oZ0pdr9DEkYpryJRUuasE599qtoENOrSxokuEFjSTvmYSbBg7aOWj5lMsq4IGwHeMEMMzxBiB3a%2BF5KbjGsh2YHoqkz9TqaA5SxGftwn%2BwGA4Bb0HnI14vSIlKxHXmSr7SJ2LhJ&X-Amz-Signature=6e6ce9c77c5c1d8322836f0008c255af1e02901b7245e531ddd047a9eaf2a99c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT4BFBDZ%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQD3XOwKJqBO0cVh1phI1aUgMYdVThcCs%2FKmwOHYHVcCpQIgEVlLD7je8KA9KuqQliwOEuDjDaQwyEbOeNve8VIl7Ucq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDBs5o6fWlI0oT3QIZSrcA0LRlMECfMRgb%2B1mLDnGSgoOsgAw3gcA7vRJCsnG69O43Ca9H13Sdix6HgCL21DVvo%2B0uJKM%2FAiVq7GMK31ZPViBT5dJ7E%2FhVX9kkNPBYzW8jPWSz7pwQKbGIsh0LNZbiXta8fc5QBkJsDut%2Brpdec5s1Vn3Wqg0h5yMjLRyrxALPLcq6v1ilDCac%2F%2FjedRDVuvgrPLjBynSamH7NUWXc2BLMa8ESfNkIAdWmCwVcPe3AQmtA90yMp1xzvSRCivFzqU6b6IKNw4xIKflNxF8wBevdE7xaZ9sLZ8BSsDBHBEx2u2QMWj6Uz%2FPUbs9nA08MhknxlcORutyQyL9Xj%2FQjzF05ETzQHQsCcfr8%2BJdUZ92DIWSautVXVJQc0fGUygoQTllu7h%2Bn4bBSfZN%2FLZ3hJpCZ3GmDVDsh0RfVq978z%2FxCECKUGcIT2%2BC5PJTv%2F5th9ZmOADohd2qaUkg5i3yP6INsJR51KxbB5JvQv0mmBQ2%2BvuZswiuQ2FKt%2F9BUTvv1ik4JwYLYJmDr34ujGTdMaS%2BiFKomdeYGApzbwvIv9uwpV7zL6Nhen7%2B1r7InmZxIjBYte%2FF62qL2lSLQAIoeXu2F6UXdUCL1RMbFnI0ajsP8PXEavQw54JX%2BZHgMKnCs80GOqUBud1eY1BmJtMX1L1Qe%2FYxLnmzqLzbKUaYF34SWZbSCm5YlQrIfg8LHsb%2FFM6hsnlApYcu4t5pOMJefe%2FVvLZK7oZ0pdr9DEkYpryJRUuasE599qtoENOrSxokuEFjSTvmYSbBg7aOWj5lMsq4IGwHeMEMMzxBiB3a%2BF5KbjGsh2YHoqkz9TqaA5SxGftwn%2BwGA4Bb0HnI14vSIlKxHXmSr7SJ2LhJ&X-Amz-Signature=4a98ef3bbebd2aaa1776ec2f75dcaa4560dc7beef075789560f71e080f9b6917&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

