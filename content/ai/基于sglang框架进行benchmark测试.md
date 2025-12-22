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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGZKSXSR%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQC9EWG8QFf72bB%2BiCJbBP%2B9kVX2ez0QnISmCgcYrdA15wIgTJkXQ9zIWbk2G2lUROirTsrAxWMfhaUnhmmr9MSeF30qiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUM%2FyzACnOYV45NHCrcA%2B3LxKQIrhu3FSWPlkup9qmbScuJjOAku%2FIiwbrLzBBeUg0wtSL25xra3iBsO5QWbfLHokZ0UMyZ2QmpDzQXaGaoLD0X9ljL5f9%2BCZh0pQVdkqF8U4PBW242Lch1UDhX3Un1mv44t2yh8HMaOSRX0k9VJdnv641U4MHi9lZ%2BamUp6LYPauliVTyXxRuNqCdZ8HvDNx6lTrzhXtqKjRHiFWCn4AKGiM0glP5TDgrlOtSjxft3Ynz%2Bxp2X%2FUjafAEdS0v6i4CiY6801c3jFQoYsYFXnhX0wIMpXCKBHYcovQFIz4VJ0qraDBhjibWhHBbiThHUxGlIMBVbeOxBRqdccd0Pbrd4jXtkOWt1XlFTSW1Afy1kQISV7rBvbTuDC5gJ7jDSmMjjOhcemU6q9ZfyyKf9%2FlBBJI9ATuxZ0ORMqfheByJrCgdMyDuKS2BAND9zF6QG9WWm9ABtoz1XLM0bw65jA1nczzLQ4jbQegSTTTyTPXGbTAyd4thL5J0iqEB6RWP82gdXDgTKvS65sHy%2BwYlSKmLxUOAvREvwUp2AOG%2FVdeMqpQl5LGtGFYhwA4UL2AFbPcnGJy3Rpx%2FMsdQYorqivqaNMumWrIu2WLDA2qqZelryIxvRFRoB9utOMKLlosoGOqUBN8LJbzl%2Fz7JqlUAaNl78Xp0dLz35r0ePAbGEi09CofGLMcCqGKJpDdBZ1R8OBRqbIxERVMWzHfPDUBSTyigbrbNcKqXKpPsqFcnVM7o5qrWh9vtGrPg9pviJYkboDPniJL5GJ9st3cbQ6e6Sy92aZpKiVeWiVHFZH0q2HmXdWrRwoAQ6Sx34fHmrHCiYO9C32mHzsef1gSBVyKfp4pf53zgLnXZO&X-Amz-Signature=9f8c6030462cf1cd9d40ddfd65d9346e661899ecd6634fdd21b6a8085bf23f1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGZKSXSR%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQC9EWG8QFf72bB%2BiCJbBP%2B9kVX2ez0QnISmCgcYrdA15wIgTJkXQ9zIWbk2G2lUROirTsrAxWMfhaUnhmmr9MSeF30qiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUM%2FyzACnOYV45NHCrcA%2B3LxKQIrhu3FSWPlkup9qmbScuJjOAku%2FIiwbrLzBBeUg0wtSL25xra3iBsO5QWbfLHokZ0UMyZ2QmpDzQXaGaoLD0X9ljL5f9%2BCZh0pQVdkqF8U4PBW242Lch1UDhX3Un1mv44t2yh8HMaOSRX0k9VJdnv641U4MHi9lZ%2BamUp6LYPauliVTyXxRuNqCdZ8HvDNx6lTrzhXtqKjRHiFWCn4AKGiM0glP5TDgrlOtSjxft3Ynz%2Bxp2X%2FUjafAEdS0v6i4CiY6801c3jFQoYsYFXnhX0wIMpXCKBHYcovQFIz4VJ0qraDBhjibWhHBbiThHUxGlIMBVbeOxBRqdccd0Pbrd4jXtkOWt1XlFTSW1Afy1kQISV7rBvbTuDC5gJ7jDSmMjjOhcemU6q9ZfyyKf9%2FlBBJI9ATuxZ0ORMqfheByJrCgdMyDuKS2BAND9zF6QG9WWm9ABtoz1XLM0bw65jA1nczzLQ4jbQegSTTTyTPXGbTAyd4thL5J0iqEB6RWP82gdXDgTKvS65sHy%2BwYlSKmLxUOAvREvwUp2AOG%2FVdeMqpQl5LGtGFYhwA4UL2AFbPcnGJy3Rpx%2FMsdQYorqivqaNMumWrIu2WLDA2qqZelryIxvRFRoB9utOMKLlosoGOqUBN8LJbzl%2Fz7JqlUAaNl78Xp0dLz35r0ePAbGEi09CofGLMcCqGKJpDdBZ1R8OBRqbIxERVMWzHfPDUBSTyigbrbNcKqXKpPsqFcnVM7o5qrWh9vtGrPg9pviJYkboDPniJL5GJ9st3cbQ6e6Sy92aZpKiVeWiVHFZH0q2HmXdWrRwoAQ6Sx34fHmrHCiYO9C32mHzsef1gSBVyKfp4pf53zgLnXZO&X-Amz-Signature=e0b6573503478f81e0a99f4b2da67465e17f97ee81a17e265ddaa5818dfb93bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

