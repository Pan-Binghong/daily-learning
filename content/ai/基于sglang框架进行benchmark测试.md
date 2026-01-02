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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYIL5U7N%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDCBUbzXCvxv%2Bj%2FYIXn24ErkltGNMg8DhYa9bFYgL3VTAIgPE7l48foMOTjDqOCOG1IYGGMPyoxyjbfEhdIR1tgxUwqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPxJviMPnWTaA21qSrcA7gHsydsz6r%2F%2Fry3TbP4b%2FHgKImPS8n7DqUvY6ebtgh9jEHWIzDn3HGytvRpwstVqRk3fx%2BsuAVYvII4MRZacUlfHj3uR5mbolRmR1OmRAgvZROdr%2FaBKFQWXwQNIysCJUyo3nm0z6dUPDMhL6W9rYtvLrLRDgIIdkxLXjnlHgQzBtk4aHAKtrip2KXHRuTO7HcZFPIoXtXWCLyLWoEraRA%2Fr8FqovJNH%2FQtDtMcMlOFVP387T6J%2F7Ux25%2Bo0vxDHzsamwem2Yu2KNiytPt9vs2CfK3c8GOVTRxa%2BoixyrSXVvn6PPaIYKKn5raSMUnUGYbLVtpm09tK%2BmeHJ8UL567I3EmqfXEL0T92YCk0MNsWaYNjmoifdv9TRahPnIT8h35wzUBbtC0RSipzjhR%2Btskq2jQWHBT1ftnaHxaV5fiGQ2sUCxxbzc5ROQ1ihJ7NUtIwJc8Ox4jLq%2FLkaaSAPHcOikisj8BsZxIpJGMPtuWgwmpn%2FlZZ%2FnepgOZDbm6F6QOTS3dEb4sIm9ctjfWSSQsqbXBYFN%2Ba8SXQQqVA8SdRV8Uorl5pAWDIDEbyFDUbeY4WFshXBij0SjEto%2FxkBe%2BRpeCZbJRieC40nOP0KoUm7qm0Q1ygO24vjGhIMMjQ3MoGOqUBQPJL5KOx2r4k1JilnI4jSkAmfOUyX1Pmqvb5whSJyG%2FYVRkq6MSA4nNxjwj%2B3%2F7H9xc%2FN6Sd7gqUP4qLvfAMHumZp0TqJuiYryVkt2tGZrdifGoqqYmGmbZYSe0T249xPE5c4IdlKBVD%2Fg4VCUl8DWnXo4ER%2FZDl1GvQvhm5YJQrpiA8rRG2lqS%2FNb59OMlBACIueuNmSqD1xndv6ZnANDdHIrmp&X-Amz-Signature=6b26c097e693e3dfdb5ed5a9d1eb0813e23ebd755cfa0e5854cbe1d602641a08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYIL5U7N%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDCBUbzXCvxv%2Bj%2FYIXn24ErkltGNMg8DhYa9bFYgL3VTAIgPE7l48foMOTjDqOCOG1IYGGMPyoxyjbfEhdIR1tgxUwqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPxJviMPnWTaA21qSrcA7gHsydsz6r%2F%2Fry3TbP4b%2FHgKImPS8n7DqUvY6ebtgh9jEHWIzDn3HGytvRpwstVqRk3fx%2BsuAVYvII4MRZacUlfHj3uR5mbolRmR1OmRAgvZROdr%2FaBKFQWXwQNIysCJUyo3nm0z6dUPDMhL6W9rYtvLrLRDgIIdkxLXjnlHgQzBtk4aHAKtrip2KXHRuTO7HcZFPIoXtXWCLyLWoEraRA%2Fr8FqovJNH%2FQtDtMcMlOFVP387T6J%2F7Ux25%2Bo0vxDHzsamwem2Yu2KNiytPt9vs2CfK3c8GOVTRxa%2BoixyrSXVvn6PPaIYKKn5raSMUnUGYbLVtpm09tK%2BmeHJ8UL567I3EmqfXEL0T92YCk0MNsWaYNjmoifdv9TRahPnIT8h35wzUBbtC0RSipzjhR%2Btskq2jQWHBT1ftnaHxaV5fiGQ2sUCxxbzc5ROQ1ihJ7NUtIwJc8Ox4jLq%2FLkaaSAPHcOikisj8BsZxIpJGMPtuWgwmpn%2FlZZ%2FnepgOZDbm6F6QOTS3dEb4sIm9ctjfWSSQsqbXBYFN%2Ba8SXQQqVA8SdRV8Uorl5pAWDIDEbyFDUbeY4WFshXBij0SjEto%2FxkBe%2BRpeCZbJRieC40nOP0KoUm7qm0Q1ygO24vjGhIMMjQ3MoGOqUBQPJL5KOx2r4k1JilnI4jSkAmfOUyX1Pmqvb5whSJyG%2FYVRkq6MSA4nNxjwj%2B3%2F7H9xc%2FN6Sd7gqUP4qLvfAMHumZp0TqJuiYryVkt2tGZrdifGoqqYmGmbZYSe0T249xPE5c4IdlKBVD%2Fg4VCUl8DWnXo4ER%2FZDl1GvQvhm5YJQrpiA8rRG2lqS%2FNb59OMlBACIueuNmSqD1xndv6ZnANDdHIrmp&X-Amz-Signature=8fa4b2e344571745431b8dc02bfeac17c087c5c236ec13d1b0157773572c276b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

