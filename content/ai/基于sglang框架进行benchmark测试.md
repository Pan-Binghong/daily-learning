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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROEHH53D%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEvp7KgIOKgdSkElobg8p9lhxFrhNfibedrCPMx2lOmAiEA%2BsgPvOmlrWEchLX0tQfIjE8erKq%2FBumNT0cz0gk5p18q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHZHJPeK%2F208l1zNhyrcA%2FxtXFvdOa4%2FnJXGqbkxqb6kwIGgCKh7l7CEaznogpwYEKX6QHrEB968RVFqzat2Z1s0M%2FlPAeq9qY3vBd0kN7NsZ6uUlNkJZnr%2BcXWcwfaRmVLp0Bsey8yJLUCD8%2BkJxfzhE1MAd6FSAtZ66iHuG922k9sRdwqoZw3m%2Bb1FUY0YM4V%2BBnOzf020f%2B58UpaOqWpx9BcTP8n%2FAQglg15vB%2Bh2WMzxZ3qIiRPrNm3EDRNgY3XIb849gCthZxcEy1uK%2BkjjnmWNj6vHtRI2cUcf7Jee6mEcVvMQexHYpym36Q2WpP5HBZPojxmtjsso28rjjv2dIAKUWvDb7ChDZ0KWLGhQ7RUNvjpZeMkqY7wD%2FkbMry%2FBZDJQ6QlmkLwgKoU5OFXXZ1UgsqO4qc7OJ9OwEgoHezuRChScg3PKwtt525XJHuXU28VYcCuq7qYHPNornXqnXUvlUDQce5QEJmDncrOzTx96FKyfShcrQx%2B3KWR5WCIEjFOO5yWc5E%2BSQiRuYEuO0klsU1HNcIDle4iWnfDAPbR%2FK09ppgNu89Cm26tuStyDRjci9hOdgCaQ3KVbA%2B81wolSvA2jZ9RSV95vo%2FRZVs6mQUuIkS0W4EkzLbNq6HyeFrOHGLfn%2Fk2AMIyvvc4GOqUBOPGXB5OVzJ2JZsBNkC%2B13gFK4QyowXzUBlNjLDNePFGKXxoAsl28YWi1w7GKUG2JyvZR1Mbgl8dpeocDo18VsZyPOKSJmgIgfjqyLcFLQAQKCmEbrdu4ZkHfhpMwRrRUj%2BBMYNPYdBDaxShyPDkZU9tLDZ71mM5A6so4Sw3yqquFEkdtuENyq69nPckOLo9DjGLfspvOWQrkmPl0%2FuHWXq2OTUwC&X-Amz-Signature=5ab51818d9953ad040486aa219df71e484e5d984a4adda94cdebe237ff183a3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROEHH53D%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEvp7KgIOKgdSkElobg8p9lhxFrhNfibedrCPMx2lOmAiEA%2BsgPvOmlrWEchLX0tQfIjE8erKq%2FBumNT0cz0gk5p18q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHZHJPeK%2F208l1zNhyrcA%2FxtXFvdOa4%2FnJXGqbkxqb6kwIGgCKh7l7CEaznogpwYEKX6QHrEB968RVFqzat2Z1s0M%2FlPAeq9qY3vBd0kN7NsZ6uUlNkJZnr%2BcXWcwfaRmVLp0Bsey8yJLUCD8%2BkJxfzhE1MAd6FSAtZ66iHuG922k9sRdwqoZw3m%2Bb1FUY0YM4V%2BBnOzf020f%2B58UpaOqWpx9BcTP8n%2FAQglg15vB%2Bh2WMzxZ3qIiRPrNm3EDRNgY3XIb849gCthZxcEy1uK%2BkjjnmWNj6vHtRI2cUcf7Jee6mEcVvMQexHYpym36Q2WpP5HBZPojxmtjsso28rjjv2dIAKUWvDb7ChDZ0KWLGhQ7RUNvjpZeMkqY7wD%2FkbMry%2FBZDJQ6QlmkLwgKoU5OFXXZ1UgsqO4qc7OJ9OwEgoHezuRChScg3PKwtt525XJHuXU28VYcCuq7qYHPNornXqnXUvlUDQce5QEJmDncrOzTx96FKyfShcrQx%2B3KWR5WCIEjFOO5yWc5E%2BSQiRuYEuO0klsU1HNcIDle4iWnfDAPbR%2FK09ppgNu89Cm26tuStyDRjci9hOdgCaQ3KVbA%2B81wolSvA2jZ9RSV95vo%2FRZVs6mQUuIkS0W4EkzLbNq6HyeFrOHGLfn%2Fk2AMIyvvc4GOqUBOPGXB5OVzJ2JZsBNkC%2B13gFK4QyowXzUBlNjLDNePFGKXxoAsl28YWi1w7GKUG2JyvZR1Mbgl8dpeocDo18VsZyPOKSJmgIgfjqyLcFLQAQKCmEbrdu4ZkHfhpMwRrRUj%2BBMYNPYdBDaxShyPDkZU9tLDZ71mM5A6so4Sw3yqquFEkdtuENyq69nPckOLo9DjGLfspvOWQrkmPl0%2FuHWXq2OTUwC&X-Amz-Signature=1ab7eae56f43e298a2395423b42f3da17b0d4447611c8692f6c368063bda3e71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

