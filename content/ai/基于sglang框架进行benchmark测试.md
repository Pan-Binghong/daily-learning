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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNBLCR4Q%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHnbkkN9ggsjqxJYsx%2FA54V7EhjtM1oJByhHgPOnGJQtAiEAzSI%2B6Ijd7CZoBOXAWBboWg27q3aDIuJ5hE0GD45Y6NAq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDBzFNSQbodANUeDmJyrcA%2BYPSE%2FJBUCU2ctkrlKTtz8sq9nnjB1VCkFoHc4KbpwYO2AWrHQ1etzgZmPN9CAnBOC8zR2FunwIxPUeG0c0LIl%2BWktZqW1481YaR18qKXtrdG2Ljia6dGGPTMixs5Fqy%2BaObZkNTxfjmMbnR%2FrTSdM72d8gakezoJOeUQu51G4nfJfM3XnJ%2FGuxTWLYGdvpW62k1eN4U2%2B%2F4LR1l0W7wGldl3oyScd2LzVF8l8lJnr90%2BC46qJuXE9gpKSWsK08m3dy2JgcDgbCgsfQbGOoMGS6NSDlgXa4hT4D2MHswfTNSrycWfWCDNVtlNv%2BCQf%2BPHn5NgrhTWMY%2B5xMbwpinZoRJDCfhydfaySzROzgwfiilWGRLAe5yNViLp1fA8TnKUUVzD3MCyLp0MVoP9wXtX8%2BpnyQyZ7pibb0jLZrpXOVx6iZznMIpYl52KbsG9eEK5R3LXCtgLq2%2BAEGhpsT08djbMcEhBK5HCZmqH8thWXULhBmOoEQ7jDRUZMUkqzerXvYFoInbSANMI2db7oXCLu8pRQKifQ%2BZIvUzjJBh7MQpP5CP%2Bt905NJMsgIsKOzs5N2LcKiN48RQ2dJhvGlwxqsKfUy3BSNl4CB%2FoJO6IiDMoUufqAyL6DT1dKVMOe%2BysgGOqUBwJ6sb2k53miN4g%2F06u6bVwrYY2uAwvkXN4hlvjXI0x5AF1E4QOnMyojmHm0lIpxi%2BAWuYpFAkFPRmmvBoBTOngRI5xbJ0XZoCD4gBFv8auht5CphKOH36VFkJ3a1IxKmvCAoGPKaGfp7DYKCMFgWsRPu5%2BUIMULuY5pHDv9joq9y7Ob%2BcJUxXNv24Bn8WYf6FrsQc7ySEF7EX1EL0025c6B7Ku3V&X-Amz-Signature=4ae5b4062b3ebf968a49ab44f66e79a80d7e183e25df6adf89ad517adc66673d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNBLCR4Q%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHnbkkN9ggsjqxJYsx%2FA54V7EhjtM1oJByhHgPOnGJQtAiEAzSI%2B6Ijd7CZoBOXAWBboWg27q3aDIuJ5hE0GD45Y6NAq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDBzFNSQbodANUeDmJyrcA%2BYPSE%2FJBUCU2ctkrlKTtz8sq9nnjB1VCkFoHc4KbpwYO2AWrHQ1etzgZmPN9CAnBOC8zR2FunwIxPUeG0c0LIl%2BWktZqW1481YaR18qKXtrdG2Ljia6dGGPTMixs5Fqy%2BaObZkNTxfjmMbnR%2FrTSdM72d8gakezoJOeUQu51G4nfJfM3XnJ%2FGuxTWLYGdvpW62k1eN4U2%2B%2F4LR1l0W7wGldl3oyScd2LzVF8l8lJnr90%2BC46qJuXE9gpKSWsK08m3dy2JgcDgbCgsfQbGOoMGS6NSDlgXa4hT4D2MHswfTNSrycWfWCDNVtlNv%2BCQf%2BPHn5NgrhTWMY%2B5xMbwpinZoRJDCfhydfaySzROzgwfiilWGRLAe5yNViLp1fA8TnKUUVzD3MCyLp0MVoP9wXtX8%2BpnyQyZ7pibb0jLZrpXOVx6iZznMIpYl52KbsG9eEK5R3LXCtgLq2%2BAEGhpsT08djbMcEhBK5HCZmqH8thWXULhBmOoEQ7jDRUZMUkqzerXvYFoInbSANMI2db7oXCLu8pRQKifQ%2BZIvUzjJBh7MQpP5CP%2Bt905NJMsgIsKOzs5N2LcKiN48RQ2dJhvGlwxqsKfUy3BSNl4CB%2FoJO6IiDMoUufqAyL6DT1dKVMOe%2BysgGOqUBwJ6sb2k53miN4g%2F06u6bVwrYY2uAwvkXN4hlvjXI0x5AF1E4QOnMyojmHm0lIpxi%2BAWuYpFAkFPRmmvBoBTOngRI5xbJ0XZoCD4gBFv8auht5CphKOH36VFkJ3a1IxKmvCAoGPKaGfp7DYKCMFgWsRPu5%2BUIMULuY5pHDv9joq9y7Ob%2BcJUxXNv24Bn8WYf6FrsQc7ySEF7EX1EL0025c6B7Ku3V&X-Amz-Signature=21966eb76ad7a121c44fb4f88221393812998273fb335315817977ad8515e9b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

