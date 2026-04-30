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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P2GGKJE%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDciFrjs9y5PY3m7Zwd7gYrwGFrkeQ8BUBC6RenDa3JXwIgC9K9%2FdUeAD%2ByBrMvfTAvCeU3cqp5VNnta%2BOmyLHBlFEq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDEQcCQ8%2BwYXnHkY7XCrcA%2B0%2Fb%2BjqWZwvwy5xe%2BD4A0kcSiUVTjgFE4UVhYZRtEb%2FxELj5o%2Bak%2FcjRPqrrp3mjMcG%2BqmX6tDgQKUBF9QQX9TXr9BHKS4Iu21wpWZs7IaPWkyrKKyoEiHq9WqSCrmnFfhY%2B0z%2FRL0VGud89EgHIFx8q9ASkAol1m99lJV9pOnqKZ%2FapO0e5bJ%2FC%2BbQFj8l0hNcxPK2gC3GnnbqW9UkWjRhjuH88NZjuNzAa%2B61QAP3gXZ%2BLqzLocEJKJJQO%2B%2FvT0TuCR1QhufQpmSCGqDG5hJm7b035zSofBjRVhmyhBOj0JqMKwuN3oIoJDcxclLAPOxI0XsqY6GJU5QYuyr51wRjnOFBwqkHF8o0%2FEcXBVFkF54vm3hW3uNug%2FEwZsBjaFyvPJ9dQrYDNUzQQPt453iJMNL89lZeFqO2DHTARlWUvc8D7dGKLIwOwuxh9HReQsJ4fJz0RinuBXdNvd%2FUrsGF6tFiq9wVOqIGV0nBva1IA9ktHtJ%2BkSgI4KxwwGXrTOfnVVMlMIk6%2B%2BYecZ6gUNjeu006AXi8%2F5uW1hOCnFXIqtixbaOa4SHxuVOK4n73k64pmZ8nDrpcRPleuNsy4ySh75Llwptz6AvLIMZ3wl3rtMrGfzH5xjuB50dXMM6czM8GOqUB4il8LHIvIXsZk67JInrbovgXkCDTMWtnhQCxiY9uC1hgHeAaKRaOrciNH8GCOZOe%2FyO2SkS4CHdj3UvGMpvzZRH8Zc4UP%2BbQ3HIDHZFY1hP4JYBnu4dECllWX9T%2F7QZ4hgHmUEaAjA6eCpPF2SPLk013LpYd9Ux%2FyTxQX8o%2FOKnppYxivJ9AIBc5ZIr2oFCN6QAOEm4QWFn%2FtEiukyhej3zdDlQV&X-Amz-Signature=d6a2a5bbc97dc38876974e45874ec261b65b4ccf970d9814b15f1aab7a6cd437&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P2GGKJE%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDciFrjs9y5PY3m7Zwd7gYrwGFrkeQ8BUBC6RenDa3JXwIgC9K9%2FdUeAD%2ByBrMvfTAvCeU3cqp5VNnta%2BOmyLHBlFEq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDEQcCQ8%2BwYXnHkY7XCrcA%2B0%2Fb%2BjqWZwvwy5xe%2BD4A0kcSiUVTjgFE4UVhYZRtEb%2FxELj5o%2Bak%2FcjRPqrrp3mjMcG%2BqmX6tDgQKUBF9QQX9TXr9BHKS4Iu21wpWZs7IaPWkyrKKyoEiHq9WqSCrmnFfhY%2B0z%2FRL0VGud89EgHIFx8q9ASkAol1m99lJV9pOnqKZ%2FapO0e5bJ%2FC%2BbQFj8l0hNcxPK2gC3GnnbqW9UkWjRhjuH88NZjuNzAa%2B61QAP3gXZ%2BLqzLocEJKJJQO%2B%2FvT0TuCR1QhufQpmSCGqDG5hJm7b035zSofBjRVhmyhBOj0JqMKwuN3oIoJDcxclLAPOxI0XsqY6GJU5QYuyr51wRjnOFBwqkHF8o0%2FEcXBVFkF54vm3hW3uNug%2FEwZsBjaFyvPJ9dQrYDNUzQQPt453iJMNL89lZeFqO2DHTARlWUvc8D7dGKLIwOwuxh9HReQsJ4fJz0RinuBXdNvd%2FUrsGF6tFiq9wVOqIGV0nBva1IA9ktHtJ%2BkSgI4KxwwGXrTOfnVVMlMIk6%2B%2BYecZ6gUNjeu006AXi8%2F5uW1hOCnFXIqtixbaOa4SHxuVOK4n73k64pmZ8nDrpcRPleuNsy4ySh75Llwptz6AvLIMZ3wl3rtMrGfzH5xjuB50dXMM6czM8GOqUB4il8LHIvIXsZk67JInrbovgXkCDTMWtnhQCxiY9uC1hgHeAaKRaOrciNH8GCOZOe%2FyO2SkS4CHdj3UvGMpvzZRH8Zc4UP%2BbQ3HIDHZFY1hP4JYBnu4dECllWX9T%2F7QZ4hgHmUEaAjA6eCpPF2SPLk013LpYd9Ux%2FyTxQX8o%2FOKnppYxivJ9AIBc5ZIr2oFCN6QAOEm4QWFn%2FtEiukyhej3zdDlQV&X-Amz-Signature=ed4be2bdd7b9a8dbb5e80784348ccd7459ccee520ac0d3a5b43ccff5660867b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

