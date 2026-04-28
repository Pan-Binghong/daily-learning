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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EY5F2TE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIF5St%2BXlXb5QOi%2BQLhCEYUmcRG8qQtmyCvdMb7HJ3HvUAiAalSjRxM0aiLtjFN9JYGIkWm3NJWb3icozhxKY5pqNgiqIBAjV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjQtUgOwRnhFApBVKtwDeUK7gWi6NBT3N21FUx95MePYJ7TXq23i2kRj7d7OUCGk0sQcb%2F4sRBTRB7jq%2FPBwJKm0N13JN1mHy5AHPmcdKuar9v08ZIC5Cqfe9TEtj5zZZaecLAbdBltS0jH88lHe6tEqXA3unU9QFLllpFoiD0H6JvtX0r2paPd2UAIPUscWYMQGlGGaIgUp6s8FmXDL74NSRHLjU9ghebmqhoeN7aCJiCXBHNYa88NQNzUDjKCdvFU5YZbvi3t5JnBUlQflMiYRv2mxA2KU%2FU1vawXsON88lYauMEVMynmpEIlZPvPsVdE3DsxtRnqDS3zJtsHN25MM4AKcUgbOtaFSLENFIgSln01KkEXdkEK5UF1wDfFwlhzCCkHtwHTc%2F61QfSaiJohl2VQwNSQoDXVjG9JjvqCykLjGDHkW8tQVru4OAK1LO%2FtUOXkdUR5h8sZY5KsH1X5bE34CaL2DwWw4gWzWxRq%2FtFnEbM8GOmuwVOMsHpEiYP8dPdMLmaAFMCmmzprLxut0935T9ZmE6uKAID%2BarNno1J%2FCMqnu%2BYmcQGw21ZqDdxeFcOcbkYP6PT5Shk%2BRr9jtJ8mzNdTalMrpsW0XZoUuNYFEkjNhpllpEz%2FB53kWZwn4GaU85H3ruiwwuOzAzwY6pgE1b9y9QnMKeEiv8%2FRrN4E8bZM3G%2FGKMCEyzPGzlXxLDxEzypEZJwqtIogGHg9abo%2BdM8%2Bi277rCYHaCtBLdg85HdiNSUevVeK%2FcmA59%2BU81np7OvcK%2B0sUl21giWh%2BYRNOH%2BK39iDL2RrPuSaXCo4jikWU1TWAw9CU%2Bz1QNo%2BClAf0T7guGMLyNdUND8LBbnV1aBlAWBjbnlp89n1%2BAIlRpbjz3BDd&X-Amz-Signature=84491c6b48349ff9814ba47ab8d80975b26be8182c9fdb95f469059112c99aee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EY5F2TE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIF5St%2BXlXb5QOi%2BQLhCEYUmcRG8qQtmyCvdMb7HJ3HvUAiAalSjRxM0aiLtjFN9JYGIkWm3NJWb3icozhxKY5pqNgiqIBAjV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjQtUgOwRnhFApBVKtwDeUK7gWi6NBT3N21FUx95MePYJ7TXq23i2kRj7d7OUCGk0sQcb%2F4sRBTRB7jq%2FPBwJKm0N13JN1mHy5AHPmcdKuar9v08ZIC5Cqfe9TEtj5zZZaecLAbdBltS0jH88lHe6tEqXA3unU9QFLllpFoiD0H6JvtX0r2paPd2UAIPUscWYMQGlGGaIgUp6s8FmXDL74NSRHLjU9ghebmqhoeN7aCJiCXBHNYa88NQNzUDjKCdvFU5YZbvi3t5JnBUlQflMiYRv2mxA2KU%2FU1vawXsON88lYauMEVMynmpEIlZPvPsVdE3DsxtRnqDS3zJtsHN25MM4AKcUgbOtaFSLENFIgSln01KkEXdkEK5UF1wDfFwlhzCCkHtwHTc%2F61QfSaiJohl2VQwNSQoDXVjG9JjvqCykLjGDHkW8tQVru4OAK1LO%2FtUOXkdUR5h8sZY5KsH1X5bE34CaL2DwWw4gWzWxRq%2FtFnEbM8GOmuwVOMsHpEiYP8dPdMLmaAFMCmmzprLxut0935T9ZmE6uKAID%2BarNno1J%2FCMqnu%2BYmcQGw21ZqDdxeFcOcbkYP6PT5Shk%2BRr9jtJ8mzNdTalMrpsW0XZoUuNYFEkjNhpllpEz%2FB53kWZwn4GaU85H3ruiwwuOzAzwY6pgE1b9y9QnMKeEiv8%2FRrN4E8bZM3G%2FGKMCEyzPGzlXxLDxEzypEZJwqtIogGHg9abo%2BdM8%2Bi277rCYHaCtBLdg85HdiNSUevVeK%2FcmA59%2BU81np7OvcK%2B0sUl21giWh%2BYRNOH%2BK39iDL2RrPuSaXCo4jikWU1TWAw9CU%2Bz1QNo%2BClAf0T7guGMLyNdUND8LBbnV1aBlAWBjbnlp89n1%2BAIlRpbjz3BDd&X-Amz-Signature=c1372d6d3d197dbc0b39ac9101666c124b21d462f1392f6097b1b89387ce1f37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

