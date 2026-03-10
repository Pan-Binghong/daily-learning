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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZTVV6IA%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCNBmSSOHt0V4e7ABYhtFdjuDfvNfB50mOZANaQc7NHNwIhAKpn5cl9c4j72BN6aXBGoaW%2Bi2MxcRKEzdv9Don5q5XaKv8DCDwQABoMNjM3NDIzMTgzODA1IgyqbWWpcEaQF9S5lnAq3AO9RQ1PSx6BkZtOZbrTjE6YFyfvOqIZA3VCWZfC0gH9OpQM6RUffyjLIRTSR99XTSD5C38pkG4jrUtRj7kpu4c8%2BPwYDgJ6A3ITJsqNK%2B1qiWuy7ZcwA3DitR5%2BLGFjC%2BwOxKnp6yDBgx4CpLTR8mPGrKjJb%2BNv4t7HXcgZUWpZbqZSBE%2BUJYK%2Fv1HODhLH%2F%2BXfTgUJy2ieWz7gIzg5s4%2BXMdN4rcX0pc0EfyFUVa%2FiIKL1IGB0gtQ03%2F466rOqRavPbliM2mICHbvuBsAkOfZjgY3xv%2FRDYWy25NlVtsL6u1tLCAzcLsNKkQCMvakIQwx7n%2B976pnA0XjvtFpQ5%2B38ECgkGwbhc2xqh5xgDmEMmzm%2FY29t14f%2F%2FJbnmX8l%2F3pfy1Dqwbv69bceNG%2BW4M9%2BGVgKoERSfZ2qlZt%2F9SN2D1Vmo7jiydd1uoRqbkOy6FpF2XbZrbGvAiQiDlcknEwcGpR6y%2FprezpXYH90ltq67%2FcnQSpkvzroNLbCbs70TfoX5fC%2BrISpd6QB%2Bus1NQeC6nKp2G0FhOFTt4iubV2qWDORqy8L%2FyKLuma%2BHIZU2v5TxQmzYh%2BiESe5VfOBK2DUpD%2BbLaqmhc8G1LQPt4eORXTYPPZj40BXBH0qNDDpj77NBjqkAZ1vI3jG5SMlaNkANUF4oKWdUhvN2S%2FlaEzmp8uK%2BOyzXF0aOH9wBnChkHOL8ShUsXPxOm6tU9o1ZQ5m5Ep8APqG5Ruh44sTbZ9QRRfE2eonBBb7IB1bycRysLbBzOsF3nAhHfYf%2B6mNYum16YDHfsgxTdMT8wflqqeVc9ZQyUy2G8MjgTtJM0pW70gLVlwPNv3KQVbVDOFncaY7cqctTdH00nsR&X-Amz-Signature=06ce6cc2219d44fcfe440c8aac5de6932e07b466db18f14ed686bdb249161ce7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZTVV6IA%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCNBmSSOHt0V4e7ABYhtFdjuDfvNfB50mOZANaQc7NHNwIhAKpn5cl9c4j72BN6aXBGoaW%2Bi2MxcRKEzdv9Don5q5XaKv8DCDwQABoMNjM3NDIzMTgzODA1IgyqbWWpcEaQF9S5lnAq3AO9RQ1PSx6BkZtOZbrTjE6YFyfvOqIZA3VCWZfC0gH9OpQM6RUffyjLIRTSR99XTSD5C38pkG4jrUtRj7kpu4c8%2BPwYDgJ6A3ITJsqNK%2B1qiWuy7ZcwA3DitR5%2BLGFjC%2BwOxKnp6yDBgx4CpLTR8mPGrKjJb%2BNv4t7HXcgZUWpZbqZSBE%2BUJYK%2Fv1HODhLH%2F%2BXfTgUJy2ieWz7gIzg5s4%2BXMdN4rcX0pc0EfyFUVa%2FiIKL1IGB0gtQ03%2F466rOqRavPbliM2mICHbvuBsAkOfZjgY3xv%2FRDYWy25NlVtsL6u1tLCAzcLsNKkQCMvakIQwx7n%2B976pnA0XjvtFpQ5%2B38ECgkGwbhc2xqh5xgDmEMmzm%2FY29t14f%2F%2FJbnmX8l%2F3pfy1Dqwbv69bceNG%2BW4M9%2BGVgKoERSfZ2qlZt%2F9SN2D1Vmo7jiydd1uoRqbkOy6FpF2XbZrbGvAiQiDlcknEwcGpR6y%2FprezpXYH90ltq67%2FcnQSpkvzroNLbCbs70TfoX5fC%2BrISpd6QB%2Bus1NQeC6nKp2G0FhOFTt4iubV2qWDORqy8L%2FyKLuma%2BHIZU2v5TxQmzYh%2BiESe5VfOBK2DUpD%2BbLaqmhc8G1LQPt4eORXTYPPZj40BXBH0qNDDpj77NBjqkAZ1vI3jG5SMlaNkANUF4oKWdUhvN2S%2FlaEzmp8uK%2BOyzXF0aOH9wBnChkHOL8ShUsXPxOm6tU9o1ZQ5m5Ep8APqG5Ruh44sTbZ9QRRfE2eonBBb7IB1bycRysLbBzOsF3nAhHfYf%2B6mNYum16YDHfsgxTdMT8wflqqeVc9ZQyUy2G8MjgTtJM0pW70gLVlwPNv3KQVbVDOFncaY7cqctTdH00nsR&X-Amz-Signature=4eef22d92b4cb4f7fab7c1be906b5730dddda069190c8bf08f80ef95cca8fd7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

