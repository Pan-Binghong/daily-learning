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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD6KOG4U%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCorach9HBUce4AUujIrl5REUivrwle6plEvY%2F%2FskPeDAIgTaDSLxdm6SG2bvqkRVQCHCjFvvAq71C0%2BtIXHU53HbwqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpYxBSbDLRB3pHHHCrcA0cLm1tQeqN1U0GEhIp70TmycPbEO2anxuwP3c93l4fGCskPXjaDndepnGkOvndWdYvrZgWnZ0XJ%2F27hxuNTkIoAhfMBMcC1kZ92c06iACFnxLwYIyL7UL8A7WoqYIM3kciqiaBamzPODEwd0uVgyahpGjb5tHk6oKZmW39JKft7vqu4jXBQciMdYxLgac5yWCl6KyAKasqzl%2BHtHw3nokETiVjwgcD%2FpoWzk3HoPoWPWxd5A1oYRPhgyRTd3mhz4ZWakmzUFPPNI7B3G1iVFjNXPWYFICX1Jn11Urj02ogZVqVSXj3B60RQepMBT%2FIPdw3R1AA6otb0VZiE1LCMM%2BBZU45o9sDVOcNDxQISBaJY5BJyaHmriYqeXHcgGyRKmyFkRV2HjI1UVCUah0SywVX8OM5lH050VgEPFRU0VcN7epMIvIRwsPCm7SmVYD5zIIeKHocGVNcqT7Crh4CsgL1r60Ld5Yag3wnwE2Dgnvo6lUyiKcoy7OG424tyCSz7KnHqBPUIPfPVAFW3Av62Y1%2Bn9Fr9TIihZu2mFxLKJjP5wiDyl1pJoYX0RzSLa5lxGPvKOOyP2fxvUpw76j88i74E6ECf5SEgoa%2F1BobUQTCECrjruyjlQsJVAlQyMLuU%2FM4GOqUBo9wz9sXeVJPBtvZ7JADgVfl8g98PSsYyRd3AFmwYZSNtmTDT7fPnYkB2LxU6bLsmRGDJlWpOzXIHb1NSvWWowX1ZiCTzW54%2B7xCi%2BV4CfJDWZ1JXldIkWttR3FFDgdvfGp%2FqiyzJFjJrQS5W%2FE2TZgyBtftIMCEREUhWKkKftTEAmc8Hs8ck8tpHS0Nxk6ukmQf8AV0A0V%2FoOWPZ9ctf5QsPWLlN&X-Amz-Signature=9f20f5e9fd62d0bb9b6d0e13cdb07e45ee3b21e51c257f8f63a1cc3e6ccde055&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD6KOG4U%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCorach9HBUce4AUujIrl5REUivrwle6plEvY%2F%2FskPeDAIgTaDSLxdm6SG2bvqkRVQCHCjFvvAq71C0%2BtIXHU53HbwqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpYxBSbDLRB3pHHHCrcA0cLm1tQeqN1U0GEhIp70TmycPbEO2anxuwP3c93l4fGCskPXjaDndepnGkOvndWdYvrZgWnZ0XJ%2F27hxuNTkIoAhfMBMcC1kZ92c06iACFnxLwYIyL7UL8A7WoqYIM3kciqiaBamzPODEwd0uVgyahpGjb5tHk6oKZmW39JKft7vqu4jXBQciMdYxLgac5yWCl6KyAKasqzl%2BHtHw3nokETiVjwgcD%2FpoWzk3HoPoWPWxd5A1oYRPhgyRTd3mhz4ZWakmzUFPPNI7B3G1iVFjNXPWYFICX1Jn11Urj02ogZVqVSXj3B60RQepMBT%2FIPdw3R1AA6otb0VZiE1LCMM%2BBZU45o9sDVOcNDxQISBaJY5BJyaHmriYqeXHcgGyRKmyFkRV2HjI1UVCUah0SywVX8OM5lH050VgEPFRU0VcN7epMIvIRwsPCm7SmVYD5zIIeKHocGVNcqT7Crh4CsgL1r60Ld5Yag3wnwE2Dgnvo6lUyiKcoy7OG424tyCSz7KnHqBPUIPfPVAFW3Av62Y1%2Bn9Fr9TIihZu2mFxLKJjP5wiDyl1pJoYX0RzSLa5lxGPvKOOyP2fxvUpw76j88i74E6ECf5SEgoa%2F1BobUQTCECrjruyjlQsJVAlQyMLuU%2FM4GOqUBo9wz9sXeVJPBtvZ7JADgVfl8g98PSsYyRd3AFmwYZSNtmTDT7fPnYkB2LxU6bLsmRGDJlWpOzXIHb1NSvWWowX1ZiCTzW54%2B7xCi%2BV4CfJDWZ1JXldIkWttR3FFDgdvfGp%2FqiyzJFjJrQS5W%2FE2TZgyBtftIMCEREUhWKkKftTEAmc8Hs8ck8tpHS0Nxk6ukmQf8AV0A0V%2FoOWPZ9ctf5QsPWLlN&X-Amz-Signature=3567fa579ea46e2a276d9bcffecd7b7f7d1ef60e42933410f98b45df60059e86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

