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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKH5C7TG%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIGpcAzSW0FMNKPfSyYr%2FOkNpASGEygWaU93oPHZ6SXwBAiEAswOxn8E1hBIIGrN7qIq5vpXYpOFuyA0BWLSkyaN3DP0q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDGwtxuhCCj9Ul4yumSrcA1t0B9o0YD%2Ffb6GKBZrJjpXv1QBoCMZctC5SyCtnEPdnoSUqkNjU3R2I%2BryBoclLsb3Xl7EV6O8Wm6h0Kt3A%2BzXE0onZhwbbBDeKoGfmRFj8uoqq5vbBFlscpJlJd0FA1GMZUc3vTyI0Q60R3pGlf8iqT8kmQdG8YBqWW1Xy%2BJwgo4caYJgw7DPW1B%2Br%2FHmGTR%2BUK2H2DBc%2BMRLVp8ymDB7IrMg1RAEzZjT9vWCu1Vah5Hbcmqk8XBGIhLVl1jA0fdb2Ko5u2HbWz4flUaaPe8Sk3rWFkj8ycGMwip09VR7IdTWGc%2FAFQ5gvARzlwJlysYgEdlGdq3U9Bi84sllOytl%2BhObbc5iNOkF%2FuXU%2BEoHl7alC%2FHjCpxfxq3Ky4fFR0l5Mq3zB5HmMt%2FDIVVdwdzL11ET6Jt6nbQzQSocjiHIKfzFsVwSIM17T25jojmnUQqTQR3X9wr06m4AwRujtfr0WJXyopTqqmcQ7yFi8p4cWKZZYq5Ds1C6Gu9mFCJrIaaera0r%2Bi68ZGqnTpGt6o2G6J8VaSLgJ5Lq%2B3zo5pRKwO83Ux0t5N3T4O9c0oGuRz95%2BIOME6dE313UlBZqu%2BL5kvi7n9mCM2e%2Ft4vPOYpsmVbAQH5yHfcoKnFPEMLW%2Bos4GOqUBc2f5kOYPOKdDpXkxdmTCtkgHJsb4tcPL7WUhdw%2BUZhUgj7UNIGSmgWHfibKsUwFdLYHFjNVrVl7pD67iUD8KwQT7GXoHUPXRbaPUWlIr5xPbc%2BmVF8c43440cj6Z7kf77j1at4NLIVa3SKEO5iTFwX52sR5je67lkv61a68HI5hLoPOq1eEPcAAi5yXu0dRP4EZ1oFYnoYE38WS7UflZvdifVPO%2B&X-Amz-Signature=aa7c3fdcbc574aac7bd8509b3a1864255010fd4f2bf132df53dc6254986b9f1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKH5C7TG%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIGpcAzSW0FMNKPfSyYr%2FOkNpASGEygWaU93oPHZ6SXwBAiEAswOxn8E1hBIIGrN7qIq5vpXYpOFuyA0BWLSkyaN3DP0q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDGwtxuhCCj9Ul4yumSrcA1t0B9o0YD%2Ffb6GKBZrJjpXv1QBoCMZctC5SyCtnEPdnoSUqkNjU3R2I%2BryBoclLsb3Xl7EV6O8Wm6h0Kt3A%2BzXE0onZhwbbBDeKoGfmRFj8uoqq5vbBFlscpJlJd0FA1GMZUc3vTyI0Q60R3pGlf8iqT8kmQdG8YBqWW1Xy%2BJwgo4caYJgw7DPW1B%2Br%2FHmGTR%2BUK2H2DBc%2BMRLVp8ymDB7IrMg1RAEzZjT9vWCu1Vah5Hbcmqk8XBGIhLVl1jA0fdb2Ko5u2HbWz4flUaaPe8Sk3rWFkj8ycGMwip09VR7IdTWGc%2FAFQ5gvARzlwJlysYgEdlGdq3U9Bi84sllOytl%2BhObbc5iNOkF%2FuXU%2BEoHl7alC%2FHjCpxfxq3Ky4fFR0l5Mq3zB5HmMt%2FDIVVdwdzL11ET6Jt6nbQzQSocjiHIKfzFsVwSIM17T25jojmnUQqTQR3X9wr06m4AwRujtfr0WJXyopTqqmcQ7yFi8p4cWKZZYq5Ds1C6Gu9mFCJrIaaera0r%2Bi68ZGqnTpGt6o2G6J8VaSLgJ5Lq%2B3zo5pRKwO83Ux0t5N3T4O9c0oGuRz95%2BIOME6dE313UlBZqu%2BL5kvi7n9mCM2e%2Ft4vPOYpsmVbAQH5yHfcoKnFPEMLW%2Bos4GOqUBc2f5kOYPOKdDpXkxdmTCtkgHJsb4tcPL7WUhdw%2BUZhUgj7UNIGSmgWHfibKsUwFdLYHFjNVrVl7pD67iUD8KwQT7GXoHUPXRbaPUWlIr5xPbc%2BmVF8c43440cj6Z7kf77j1at4NLIVa3SKEO5iTFwX52sR5je67lkv61a68HI5hLoPOq1eEPcAAi5yXu0dRP4EZ1oFYnoYE38WS7UflZvdifVPO%2B&X-Amz-Signature=4557d9b8165b95cb3c51e960a1ebe45b4596839acd374c78d53e6c08bf0521cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

