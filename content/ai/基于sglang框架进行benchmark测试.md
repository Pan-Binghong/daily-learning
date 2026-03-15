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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3J6F2K%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCel4cASg%2Fg%2F4kDgIZi5rChZ2Cn5A9Hnh9JxVM1pGvunAIhAKmr3OLj2NA9Bglq2qk7QDWHfIyqm45lSMSzvFWyWT1IKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZbovqBV2W2fsK%2BzYq3AM4xmRUGiayjCERah5PdZjnYx3HPXPkHTiFAgrTOEuJw7lv38LE5Lir0KZMeQbJc%2BptTHJIQ8vqIf32goaBkvyf4A%2FL51F6EbW3PR1PmTi3nDmxdKKWQbd4ksWn9XI4SbY0s%2F6ySxC5wjwzICq04G0jLxvUFbEC2ENC5NRFGcOpq5BYv0G7H4%2B26ekbq6%2BAUL5MZpAJVsya9tOHfzwZh6SYleN5yp1cvczXlOcd6H9L%2BrP1VgnxqDvKR0rH4JEwxZKLbS%2FDPc1ns09c8WVnipURWpNHRrUIRw5byEARcawWRdkMpSbD%2FOW3KKsQlIw1kf1dlYKWCFYdv6EXj5XMODylYHyjuadd8BbrLZcT%2FZsaET8ZfPhqzqK7DgUx3LgGAoiPQTTVW1MX0a8JR0usVcqpSLB68YnWbzLhqXBBBrm1intjT%2FNUqZw7YuGbS%2FOKqLDN5Vd5BO3rGICUf8Nc34hcvA2MQi48kh4YuGaGdhf9Mx7jKqA2%2BXQ5j4u8ndbNV5aM%2B%2FZcFkAd8SzZla777Nsq8ZHtVtmRPLTqhSydQpQEroQ2hFfy0f3cLBghDdzIZOurbQIArPqZco8jOyxZp%2FBZTi3e5ZRMZzmyHXthFqWSNNYPoZscYvXERqO5ZTD3kNjNBjqkAYC8b9xvOUu0TpqzAUpSj69wAF5N%2BK0iKFgzaRAqTYT409ITVwSZ4BOdEUzmO7qg%2FKelVkm8E7S%2B442J9Nm5gmYJ9v8l323qHTXH9FI%2BhzdZNbuIFUDTzPdbCBBJjS7NpMSPFSchZF8aEnb1UVMK8XOp733oSBwQmzadMXxOWyinvtg6r1HDggqvn9KUeRT%2BK5F99O0H2sOxi05JpkRf8G5ShX6o&X-Amz-Signature=9c43c46c5b25a85334733d3366ff0b5f6eed92d5c88ee44c686eb2cd3c1ceade&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3J6F2K%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCel4cASg%2Fg%2F4kDgIZi5rChZ2Cn5A9Hnh9JxVM1pGvunAIhAKmr3OLj2NA9Bglq2qk7QDWHfIyqm45lSMSzvFWyWT1IKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZbovqBV2W2fsK%2BzYq3AM4xmRUGiayjCERah5PdZjnYx3HPXPkHTiFAgrTOEuJw7lv38LE5Lir0KZMeQbJc%2BptTHJIQ8vqIf32goaBkvyf4A%2FL51F6EbW3PR1PmTi3nDmxdKKWQbd4ksWn9XI4SbY0s%2F6ySxC5wjwzICq04G0jLxvUFbEC2ENC5NRFGcOpq5BYv0G7H4%2B26ekbq6%2BAUL5MZpAJVsya9tOHfzwZh6SYleN5yp1cvczXlOcd6H9L%2BrP1VgnxqDvKR0rH4JEwxZKLbS%2FDPc1ns09c8WVnipURWpNHRrUIRw5byEARcawWRdkMpSbD%2FOW3KKsQlIw1kf1dlYKWCFYdv6EXj5XMODylYHyjuadd8BbrLZcT%2FZsaET8ZfPhqzqK7DgUx3LgGAoiPQTTVW1MX0a8JR0usVcqpSLB68YnWbzLhqXBBBrm1intjT%2FNUqZw7YuGbS%2FOKqLDN5Vd5BO3rGICUf8Nc34hcvA2MQi48kh4YuGaGdhf9Mx7jKqA2%2BXQ5j4u8ndbNV5aM%2B%2FZcFkAd8SzZla777Nsq8ZHtVtmRPLTqhSydQpQEroQ2hFfy0f3cLBghDdzIZOurbQIArPqZco8jOyxZp%2FBZTi3e5ZRMZzmyHXthFqWSNNYPoZscYvXERqO5ZTD3kNjNBjqkAYC8b9xvOUu0TpqzAUpSj69wAF5N%2BK0iKFgzaRAqTYT409ITVwSZ4BOdEUzmO7qg%2FKelVkm8E7S%2B442J9Nm5gmYJ9v8l323qHTXH9FI%2BhzdZNbuIFUDTzPdbCBBJjS7NpMSPFSchZF8aEnb1UVMK8XOp733oSBwQmzadMXxOWyinvtg6r1HDggqvn9KUeRT%2BK5F99O0H2sOxi05JpkRf8G5ShX6o&X-Amz-Signature=8a64240aa499042c24316ebfce6112627d9ce43b067f00330560461bd26afd92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

