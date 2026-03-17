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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MJVPEEQ%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBFJnFV1QdALK8fdEAHd8UBdnxkwPcioLMTMwqebNy6%2FAiEA9SfO5eWaM08Jf%2FHOHUb7tsRknYvLmghua2895%2BVTGzcqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHcd7ZglGB5xy2BHDyrcAw3VpmzrFQCtyNrPwZRb4atyzbSBW97XZwwo%2F0UKscx9b6DGEhGSOoLrfDyQLyc%2Fzsk3dJNE1YSz3lMCv2n2f6e1Qs3TA%2F5nA6isIc7ItVBCYxjqJmuVNL2vQ%2B1Ue2lNWdSXulOLnvOHEU8mxUM8QOEeKJcrFRdEDhKFLRqBYBLQ0HWtkVq2z6vHhfirz3SWSyZd204o1gFqPRLQP94P%2F0l3B92uyA24xFt9k7uVI%2FKVswgLzvecEj3t0%2BQ2KqfAwzNpIIRceXvz%2FCUm4a9A9tNIb4VzPewvA5tWeRjvVPdK9WobzeVH9iZmBlLQkidSvH97E0eXb2%2BUv9q42l483ClDyxmUuZZYWDrkK75aAO9%2FiiFbyMyAzkcKRyxGtOPEF%2B4ZVlRXE0N%2B18hEBtFOPBAwV1Oq3092ftO4uQQPMRC%2Fjb1A4lr75v%2B3MMl2gKeGNIjZJKTNkP8cFjAeptJoVvs85NZnoJ0UxpYZmByok9lZ9O97U56aIblioV976HBqrnxeMpuZ4FQ4TO24lHrMdtJUWd01RPj96LHCW%2B%2FI6vMnu%2B2uAx1e6KYh%2FQoJ9SLxjbq2NEwRPBUcfCwGb1XtQVm%2FyqsVGa9Fh0b6htDdLx9%2BleIsMpcNhgS5bvtBMPXo4s0GOqUBpiaXsumP3IoUl2X6jgycioFTdSSzxjQut7SOlbbsrJxclkzPLUslVXwOKQ1gxcTXbIIJet4s0jmMVQekburIiDdJmz4MuBou%2Fr1uj4kfY%2Fy1X6q1I%2FzsxE4qs8d6Fm5DuOCLqPuZpkbQ%2BCIcSHB7p7UqDX4mLdPGnM6BU8qf%2BQeIUtMtLSkzgY4MGOCOwnEBiFhqKB5ND9ogVOOYl0M4jlNZBUgD&X-Amz-Signature=a5d65f6680aa7e769571195241083108c3666cde74d9a3e5027f56e929892db0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MJVPEEQ%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBFJnFV1QdALK8fdEAHd8UBdnxkwPcioLMTMwqebNy6%2FAiEA9SfO5eWaM08Jf%2FHOHUb7tsRknYvLmghua2895%2BVTGzcqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHcd7ZglGB5xy2BHDyrcAw3VpmzrFQCtyNrPwZRb4atyzbSBW97XZwwo%2F0UKscx9b6DGEhGSOoLrfDyQLyc%2Fzsk3dJNE1YSz3lMCv2n2f6e1Qs3TA%2F5nA6isIc7ItVBCYxjqJmuVNL2vQ%2B1Ue2lNWdSXulOLnvOHEU8mxUM8QOEeKJcrFRdEDhKFLRqBYBLQ0HWtkVq2z6vHhfirz3SWSyZd204o1gFqPRLQP94P%2F0l3B92uyA24xFt9k7uVI%2FKVswgLzvecEj3t0%2BQ2KqfAwzNpIIRceXvz%2FCUm4a9A9tNIb4VzPewvA5tWeRjvVPdK9WobzeVH9iZmBlLQkidSvH97E0eXb2%2BUv9q42l483ClDyxmUuZZYWDrkK75aAO9%2FiiFbyMyAzkcKRyxGtOPEF%2B4ZVlRXE0N%2B18hEBtFOPBAwV1Oq3092ftO4uQQPMRC%2Fjb1A4lr75v%2B3MMl2gKeGNIjZJKTNkP8cFjAeptJoVvs85NZnoJ0UxpYZmByok9lZ9O97U56aIblioV976HBqrnxeMpuZ4FQ4TO24lHrMdtJUWd01RPj96LHCW%2B%2FI6vMnu%2B2uAx1e6KYh%2FQoJ9SLxjbq2NEwRPBUcfCwGb1XtQVm%2FyqsVGa9Fh0b6htDdLx9%2BleIsMpcNhgS5bvtBMPXo4s0GOqUBpiaXsumP3IoUl2X6jgycioFTdSSzxjQut7SOlbbsrJxclkzPLUslVXwOKQ1gxcTXbIIJet4s0jmMVQekburIiDdJmz4MuBou%2Fr1uj4kfY%2Fy1X6q1I%2FzsxE4qs8d6Fm5DuOCLqPuZpkbQ%2BCIcSHB7p7UqDX4mLdPGnM6BU8qf%2BQeIUtMtLSkzgY4MGOCOwnEBiFhqKB5ND9ogVOOYl0M4jlNZBUgD&X-Amz-Signature=9050cb2fdaba9098ca5ce72f718fa09b9bb43732b050000289bea91d59e9420a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

