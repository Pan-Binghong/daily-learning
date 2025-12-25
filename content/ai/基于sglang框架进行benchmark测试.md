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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ODEAO7S%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQDx4IsYaZoZKLKbIlFyGMoHRuVq5uOD9kv1IP6Lb6icXQIhAPC9%2Bt4Oi5vhKp06apExAyv9i5eSCCDhksFXpv7ogrSGKv8DCDIQABoMNjM3NDIzMTgzODA1IgwahS1X1R%2BzgAhugS8q3APd0BfortTtKEbijxxPRpS4fKq3CvkdZTAQZuaIOU6zk2IWUQ5GGePD9GpahgtSRpmWrl6Ww4UJlcYMKg2CzECCdviYQ6k7DfFCjmTyAJRySR3iNcdWnF%2F5YFmhnTnDu5hrX3UVvSNeqibxYPfl1UrMKRBNPz6%2FdtuAvbPAsHVGDGPXEl%2Fl7R%2Bgnrp8LBGY2dMsgGXXdnSO%2FN2AMwcJRdmLwQKyI2xsnKa75fyMv66mJLMXUVkdw2%2BCB3r%2FIlXZ49YyBfdWgJWV243b4dVJhZsSSVc7lNsZQZo2%2BPoHqGwxzefU5%2FYmNKlTpP%2F%2Fjuf8Y2msKEpLmnrQt7Vwm2KqT7O5mbJM%2BSq%2B6IcyauJpKt4Ymh3HqgaL0PNkeGyJQ%2F18dAbwzgDBa5rtmHE%2BBVxCCBUb28YpvfwBS6GIi7U%2FxhXnjqS7nIzc60iidHaHxNE4TV0VNudwfwuNA1HOnu0ia18NT4db4NBGHObRSvYBQVYnGnamqIe1eE%2B70L6o%2Bqzv%2FwEFAdWgfCLV3ALIoPpmNVpyixAL2GTLcIA7Y%2BqqrPfDFRyG%2BL5LZhETvGbCzMYjScI%2B%2Bx5Wr7EkW%2B4N5mb%2B9MCXbF5ukDbYsrIzQX3KrMMm2w1w3lP1UgAdzyfoKzCQorLKBjqkAYDX4GsUXhAWP0ioAiN%2BN%2B1Xaxc%2BATS6KWSOr1Am4%2F9XCMAVntz5wYyLB1KkvoAHgskpK%2FoKM916gEeTJS%2BA8Vh1in5rvZWU7gEWsN%2F3HjiYgCYgFqWlK1LQQMq523PgVSJrvir%2BpKetbdvGEOpmpV3ttmglGxgxbVjYAJUHt4VauCJg5W8WbrVYDXv0Jwvr%2FNS8Btoe%2B8GlNOE6DZXs3SanfkCo&X-Amz-Signature=f615c1d7a6f9839543aeb571c4a7899999a984b76cb1b1c623a2fe55440a3659&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ODEAO7S%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQDx4IsYaZoZKLKbIlFyGMoHRuVq5uOD9kv1IP6Lb6icXQIhAPC9%2Bt4Oi5vhKp06apExAyv9i5eSCCDhksFXpv7ogrSGKv8DCDIQABoMNjM3NDIzMTgzODA1IgwahS1X1R%2BzgAhugS8q3APd0BfortTtKEbijxxPRpS4fKq3CvkdZTAQZuaIOU6zk2IWUQ5GGePD9GpahgtSRpmWrl6Ww4UJlcYMKg2CzECCdviYQ6k7DfFCjmTyAJRySR3iNcdWnF%2F5YFmhnTnDu5hrX3UVvSNeqibxYPfl1UrMKRBNPz6%2FdtuAvbPAsHVGDGPXEl%2Fl7R%2Bgnrp8LBGY2dMsgGXXdnSO%2FN2AMwcJRdmLwQKyI2xsnKa75fyMv66mJLMXUVkdw2%2BCB3r%2FIlXZ49YyBfdWgJWV243b4dVJhZsSSVc7lNsZQZo2%2BPoHqGwxzefU5%2FYmNKlTpP%2F%2Fjuf8Y2msKEpLmnrQt7Vwm2KqT7O5mbJM%2BSq%2B6IcyauJpKt4Ymh3HqgaL0PNkeGyJQ%2F18dAbwzgDBa5rtmHE%2BBVxCCBUb28YpvfwBS6GIi7U%2FxhXnjqS7nIzc60iidHaHxNE4TV0VNudwfwuNA1HOnu0ia18NT4db4NBGHObRSvYBQVYnGnamqIe1eE%2B70L6o%2Bqzv%2FwEFAdWgfCLV3ALIoPpmNVpyixAL2GTLcIA7Y%2BqqrPfDFRyG%2BL5LZhETvGbCzMYjScI%2B%2Bx5Wr7EkW%2B4N5mb%2B9MCXbF5ukDbYsrIzQX3KrMMm2w1w3lP1UgAdzyfoKzCQorLKBjqkAYDX4GsUXhAWP0ioAiN%2BN%2B1Xaxc%2BATS6KWSOr1Am4%2F9XCMAVntz5wYyLB1KkvoAHgskpK%2FoKM916gEeTJS%2BA8Vh1in5rvZWU7gEWsN%2F3HjiYgCYgFqWlK1LQQMq523PgVSJrvir%2BpKetbdvGEOpmpV3ttmglGxgxbVjYAJUHt4VauCJg5W8WbrVYDXv0Jwvr%2FNS8Btoe%2B8GlNOE6DZXs3SanfkCo&X-Amz-Signature=661a10198c7e217d792fa7a2efba013247333ce254c40e8f15b2499f6517c469&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

