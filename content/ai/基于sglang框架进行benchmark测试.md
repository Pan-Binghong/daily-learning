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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UICI2C4P%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC00fQU%2Bn1JeSiUjD4PYh1NFPF7k%2B%2BPiU4Veas3WHl%2BSAIgYBqkmcHpVTb4cRlPiv%2FonqSPH0swVyq7dcf%2FHCXex3EqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMw8Vw18brFt2yGxKircA0oFDGwaTSihH7RAPo4dZf7FBe6gETDVO949IBKYa%2FnqKQRbHO5T2y1oQ0eA4WdqGKdNjmml62xGHZRswrSy1V62VBCQY6ZLFNynw4HCXgVGdw1uhjY23Nm6Xq86c5uElx72k0A2b%2FtY5DXvZAguqizFUqgBZe5unm3fMoN8bkjOplC8xgisJaZleCqVIgIeElU97UJfABzYYaMsnJvr6uEIPA71IVxuE6EoLRr%2BI0%2B%2F7gkHR%2FozM2Z8BZkOcpBBhRQyCiUPbAhNQun0Uc%2FnPRH0KSyTWrx6kCz6LgjEX1ijGoTMvUkskND192pmJkxAnwLvXjh58q%2B%2FSkM7IslA9zI35PkoFn8EL%2BO%2BdNafplAs8oVu2EVtUdOXQl%2B6yBnH%2Fe0Ha%2FOGdSvwl%2FLMkx%2BDSIJEKwQG93ZZckXCQ2I2titDhSmHMEjMnN6S%2FoG0cSxpGk6JIIekaJ5SpiSoUWo%2BtWqFL7q6AG7PWOi2VWdPUG5t6htacAdP4QIiEIBZPp8jaP1p1HWq9EmOfPMCz%2B%2BHBFh4xtkscGN75kllAWLPgu5gZm%2FW1LB6fjDDGHFjXPxQ0GGohICa2YOo18MbLQzAsKSzasPntsfQbs4LuzrcUhsL2g7rnPQ887ud66kEML%2FDqswGOqUB2xuMXm09HdDStrtZ9vfQKVUw7%2B0xi%2FDRnZqkC2%2B6qOIJmoF4uQpmAhkF74KKCnzkevXtELTvGs6X4K3e3Snvo0msxajLjPfbmeVFC2Df%2BnvVZA5arEdqumreiliO3nr6BOoPv1GCbpt60CwYr7y1C0SquIlXlmS3AHjRLOfCscqjba%2FlgDVL4mtSgy5knfd22bWeefl1IEm7PkM8YGN8ew6xoLx%2B&X-Amz-Signature=5c82fcb9cc346a5c0b66451463aa06137a873ee5590b58a041fb8c3d8ac58d4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UICI2C4P%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC00fQU%2Bn1JeSiUjD4PYh1NFPF7k%2B%2BPiU4Veas3WHl%2BSAIgYBqkmcHpVTb4cRlPiv%2FonqSPH0swVyq7dcf%2FHCXex3EqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMw8Vw18brFt2yGxKircA0oFDGwaTSihH7RAPo4dZf7FBe6gETDVO949IBKYa%2FnqKQRbHO5T2y1oQ0eA4WdqGKdNjmml62xGHZRswrSy1V62VBCQY6ZLFNynw4HCXgVGdw1uhjY23Nm6Xq86c5uElx72k0A2b%2FtY5DXvZAguqizFUqgBZe5unm3fMoN8bkjOplC8xgisJaZleCqVIgIeElU97UJfABzYYaMsnJvr6uEIPA71IVxuE6EoLRr%2BI0%2B%2F7gkHR%2FozM2Z8BZkOcpBBhRQyCiUPbAhNQun0Uc%2FnPRH0KSyTWrx6kCz6LgjEX1ijGoTMvUkskND192pmJkxAnwLvXjh58q%2B%2FSkM7IslA9zI35PkoFn8EL%2BO%2BdNafplAs8oVu2EVtUdOXQl%2B6yBnH%2Fe0Ha%2FOGdSvwl%2FLMkx%2BDSIJEKwQG93ZZckXCQ2I2titDhSmHMEjMnN6S%2FoG0cSxpGk6JIIekaJ5SpiSoUWo%2BtWqFL7q6AG7PWOi2VWdPUG5t6htacAdP4QIiEIBZPp8jaP1p1HWq9EmOfPMCz%2B%2BHBFh4xtkscGN75kllAWLPgu5gZm%2FW1LB6fjDDGHFjXPxQ0GGohICa2YOo18MbLQzAsKSzasPntsfQbs4LuzrcUhsL2g7rnPQ887ud66kEML%2FDqswGOqUB2xuMXm09HdDStrtZ9vfQKVUw7%2B0xi%2FDRnZqkC2%2B6qOIJmoF4uQpmAhkF74KKCnzkevXtELTvGs6X4K3e3Snvo0msxajLjPfbmeVFC2Df%2BnvVZA5arEdqumreiliO3nr6BOoPv1GCbpt60CwYr7y1C0SquIlXlmS3AHjRLOfCscqjba%2FlgDVL4mtSgy5knfd22bWeefl1IEm7PkM8YGN8ew6xoLx%2B&X-Amz-Signature=283bffdea704e558d57180ed669136d1061611042aec9776a5581aff82202d56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

