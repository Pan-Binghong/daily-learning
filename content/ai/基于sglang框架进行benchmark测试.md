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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ4WHRKL%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCVF79TpzMflUq%2FaIohaM924JwB9yuxLLV3m5SappNo8gIhAN6I9O%2Bb28Q7qDp0i994ORiz2mN9hWUXQPOjCdBOm0A9Kv8DCBMQABoMNjM3NDIzMTgzODA1Igxb%2FVr6sKf5%2B%2BCohaMq3AP0L1FBJE1X8T0%2FQdpTiImH0GfR2V4h3FFtv4N1Jca4Sh%2B%2FUcUGNxzFGwCrN%2BufZ%2BY5BUkpxO0%2FYZ6c%2B3U344WQ1cuc6qgz2k9IHsGz5qhXgRAv1rtJtImpVBcMJJJvrfZt8F%2FMLzLko%2BTSziVhsk5y3kKcDZOCkMklubpQScM9SMeurk%2Bv%2BDzQNyp%2FV0lRRMI0EvNzAy9iajB90Iqv%2BMhP0QXq0v8rwONcNG8cZoy8yvIrJ0PBOd3p9aI%2BgF3vYZyGClhn5%2BaTsXAzrx%2F0wSk8ToJxIFYoal1H0ZN5IV5zsvrJj%2B2yhtNS8swguQ%2BLNcL5a%2Bxs9LLqbwWDXNtATqa5Bb%2FNstu8vGTB%2Bouu0DfNcxquLHS96dQxd85v1pKz40%2BgQ4Ofcj2SnWIzojfMJszP1hGj%2Bdy9F3X4knhv2lrpqgRMWNHBd3QzR%2BfrSRzTE6Sk93x0ApESF1G%2BaIoY7MBw0KPbE84bYthki6D2im%2BZWtvBwhM13EcBDejZtx5lSGRpRMKlLKRFQjVVOwQ4t6LIgll7R97vElGTekq8ZUmJqxkBAuCLAbpslfR%2Bx7fG4%2FqYKStmecgJ%2FT3ThaouaHpa3G1ea4YtOC25v07IwRBJ0gSX4JtfOmytWF24kzCv75vLBjqkAX71EUFVvW4obLzE1g8z6SioqSnV7gYUIlx77TC1GYxM2kEDswwEExJoZGFqXzDp4JDfeddJuyAreFim5%2Ba2xS2gTdSvIA9D8bSzZxv2O1CB3uGEO0gDNgX4U6ccGdgAhdyA95QsGAZ3MrFlHa%2BUYE%2B%2BM5akv2eJpD7oV7a4odddmOfhh1iZ5YsgHqOpOAtE13hRuV7Zk16%2FS%2FYXm2ZLPeLT70zn&X-Amz-Signature=1621960246c4f6eda9f73e01e568db6446050f3da2d10a1c3e9edb07aeaafb24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ4WHRKL%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCVF79TpzMflUq%2FaIohaM924JwB9yuxLLV3m5SappNo8gIhAN6I9O%2Bb28Q7qDp0i994ORiz2mN9hWUXQPOjCdBOm0A9Kv8DCBMQABoMNjM3NDIzMTgzODA1Igxb%2FVr6sKf5%2B%2BCohaMq3AP0L1FBJE1X8T0%2FQdpTiImH0GfR2V4h3FFtv4N1Jca4Sh%2B%2FUcUGNxzFGwCrN%2BufZ%2BY5BUkpxO0%2FYZ6c%2B3U344WQ1cuc6qgz2k9IHsGz5qhXgRAv1rtJtImpVBcMJJJvrfZt8F%2FMLzLko%2BTSziVhsk5y3kKcDZOCkMklubpQScM9SMeurk%2Bv%2BDzQNyp%2FV0lRRMI0EvNzAy9iajB90Iqv%2BMhP0QXq0v8rwONcNG8cZoy8yvIrJ0PBOd3p9aI%2BgF3vYZyGClhn5%2BaTsXAzrx%2F0wSk8ToJxIFYoal1H0ZN5IV5zsvrJj%2B2yhtNS8swguQ%2BLNcL5a%2Bxs9LLqbwWDXNtATqa5Bb%2FNstu8vGTB%2Bouu0DfNcxquLHS96dQxd85v1pKz40%2BgQ4Ofcj2SnWIzojfMJszP1hGj%2Bdy9F3X4knhv2lrpqgRMWNHBd3QzR%2BfrSRzTE6Sk93x0ApESF1G%2BaIoY7MBw0KPbE84bYthki6D2im%2BZWtvBwhM13EcBDejZtx5lSGRpRMKlLKRFQjVVOwQ4t6LIgll7R97vElGTekq8ZUmJqxkBAuCLAbpslfR%2Bx7fG4%2FqYKStmecgJ%2FT3ThaouaHpa3G1ea4YtOC25v07IwRBJ0gSX4JtfOmytWF24kzCv75vLBjqkAX71EUFVvW4obLzE1g8z6SioqSnV7gYUIlx77TC1GYxM2kEDswwEExJoZGFqXzDp4JDfeddJuyAreFim5%2Ba2xS2gTdSvIA9D8bSzZxv2O1CB3uGEO0gDNgX4U6ccGdgAhdyA95QsGAZ3MrFlHa%2BUYE%2B%2BM5akv2eJpD7oV7a4odddmOfhh1iZ5YsgHqOpOAtE13hRuV7Zk16%2FS%2FYXm2ZLPeLT70zn&X-Amz-Signature=2722c98940de71a9f7d863950f66624ba71d87c8c6fd59af2c3c6e3104fc8f31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

