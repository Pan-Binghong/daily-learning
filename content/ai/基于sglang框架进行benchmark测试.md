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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LDO5JMR%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOXi8gOzdWf4ZZVcHq4SAVgPDZK6iVJsGVjlWYQJHliwIgJpJkHpRiIhu2AdkbWGFl%2BpP%2B6UhLwfyBf7WMyEyyz50q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDCQq4K87yo2o1CdurCrcAy6l3DrpLQx7rXf4aL8PjBIBaeVKxRN2xz0nyxhGj5JJ7TO44IPfP2F4SZme4OOkG5Bu%2B276G0ea9zOJuciTJ0UlrKYZgfR2YaPofnVKvwADQWKrlIzyKlrTtz77QAAy264i04rMqymZ6G%2Fwo2ynY9NvGll%2BRkvYP87iTd8VwqPQBCO8nB%2F17PzWBMmj5QXaF96cfBwrTcaEV6otZofoPdA3gKPQ8s9sLLOqK%2BBczPSgZfs4uMaz65dezqx001NlGgtjXqXQ445drAZ6CLgJ99%2FRW85xSTNw%2FXVrtkH%2FsOxFiwL%2B3w5A6scj2VFim1qVe6CsEqUNv%2FswT9YnlojMn1YUrA1neBpzohk5%2BvwWEund%2FDQdZlyNxNI9mLKa1nWTUZFpyP3F0A45mXZCPtdYMnzwd5JKJAEpdQzNUyNTg9G4NWkJD23ilJycyyTSluN0dp7N0tYnCNcasYjtd%2FwIxli1ifun4X7MX3gv8b0HXRxc0UtZ1bfLMRhCOYJKL%2BMvFpqsEs0R9cjxWt4seTrJsmeURXdFJQivziuUUI8Cun5HhsiZ%2F%2FeuGKf2EF3pdd2Qrm3K2ZLHfy2tH4PhUMNabO5ZYKW8FNj7nqYmPER8v9EqOAZnap8HZqjL8wK1MP%2Btt84GOqUBl0Lq%2Fn5ByVlUM8g3i%2BC0xk%2FD%2FHRJps2%2Bhkt14nuDCsAu9x3S%2BEP4S0S7a%2BklnESU4l4qBTVLoj1g%2BLo97HHcRaatJ9PN7OMWtkj2rgjqLDBDTANcFMA1QCXqFbmb5L6s7DBFIKX9gdqNP0nc3qP4Oy%2FWfGlWWjkwXFoFMCBc1FnUhwYPKe0XEEfAjAnX5PHqAtk8zF2OP9LFaW1vcBqctDbYxuKq&X-Amz-Signature=34e74b47e7f0ffbb2b8f3a578048c523e9ac5a3a5bb339d8bbc3c630a4b40134&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LDO5JMR%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOXi8gOzdWf4ZZVcHq4SAVgPDZK6iVJsGVjlWYQJHliwIgJpJkHpRiIhu2AdkbWGFl%2BpP%2B6UhLwfyBf7WMyEyyz50q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDCQq4K87yo2o1CdurCrcAy6l3DrpLQx7rXf4aL8PjBIBaeVKxRN2xz0nyxhGj5JJ7TO44IPfP2F4SZme4OOkG5Bu%2B276G0ea9zOJuciTJ0UlrKYZgfR2YaPofnVKvwADQWKrlIzyKlrTtz77QAAy264i04rMqymZ6G%2Fwo2ynY9NvGll%2BRkvYP87iTd8VwqPQBCO8nB%2F17PzWBMmj5QXaF96cfBwrTcaEV6otZofoPdA3gKPQ8s9sLLOqK%2BBczPSgZfs4uMaz65dezqx001NlGgtjXqXQ445drAZ6CLgJ99%2FRW85xSTNw%2FXVrtkH%2FsOxFiwL%2B3w5A6scj2VFim1qVe6CsEqUNv%2FswT9YnlojMn1YUrA1neBpzohk5%2BvwWEund%2FDQdZlyNxNI9mLKa1nWTUZFpyP3F0A45mXZCPtdYMnzwd5JKJAEpdQzNUyNTg9G4NWkJD23ilJycyyTSluN0dp7N0tYnCNcasYjtd%2FwIxli1ifun4X7MX3gv8b0HXRxc0UtZ1bfLMRhCOYJKL%2BMvFpqsEs0R9cjxWt4seTrJsmeURXdFJQivziuUUI8Cun5HhsiZ%2F%2FeuGKf2EF3pdd2Qrm3K2ZLHfy2tH4PhUMNabO5ZYKW8FNj7nqYmPER8v9EqOAZnap8HZqjL8wK1MP%2Btt84GOqUBl0Lq%2Fn5ByVlUM8g3i%2BC0xk%2FD%2FHRJps2%2Bhkt14nuDCsAu9x3S%2BEP4S0S7a%2BklnESU4l4qBTVLoj1g%2BLo97HHcRaatJ9PN7OMWtkj2rgjqLDBDTANcFMA1QCXqFbmb5L6s7DBFIKX9gdqNP0nc3qP4Oy%2FWfGlWWjkwXFoFMCBc1FnUhwYPKe0XEEfAjAnX5PHqAtk8zF2OP9LFaW1vcBqctDbYxuKq&X-Amz-Signature=415d7bc4e2d149b5bfe78e4194c840072ff68ace80aa47ec8050a479c9500255&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

