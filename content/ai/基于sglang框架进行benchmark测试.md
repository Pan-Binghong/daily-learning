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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4EQY3LK%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQC2kewiwFeGcvlNuQEwv0wc6zpWTZWler3Iw3dJwmciPAIgObIYzhneAgvURGp4kOtyX9pMCNk8kx6uXGYesvplGJEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJLmxA2y%2FO7aT2NG4SrcA%2B0gNkfgB5EkfseBQ9EZQY7Y1V23114HH%2BqIpGHCj%2BI3IL9n9LxOZr4FOtw51mtg9VOPYLPl1TN3XbhzDakvbau6I5WOF8Lm8Z05hTVWla1ol7jK%2Fzz67ozMgmHFkpKbHjKXuba2luv1b0B%2BhNyReF1tBlryL%2BQ4SLoe7z%2BUIrrGMyyzjExAodsoBXDsLD3uYaed8QN3%2FDmcOokKHTE8aIitP3wwiutE9DpeypLPdmdir3PpyAxb3SkcwddImI9taweFRMz1lRgChcAwFepyqj%2Bixsoc1EVYO%2BkFleYwPwtZAiItaFe0JxxOdOY773p%2BIt%2Bu1Mes00pKczrOepS3UHuYCCqRDvGgV2tTn%2FLsapAuABcN4laoD%2FVp%2BVxLsm2DvGJ2fI9shXoI8Zc8k2PXHdvPVfMiP64Gh3OwoZs%2BBdBebyN55LTCxFyDU%2FyFjw2Rpq6I8lpE77za4LV3htsqjDNJsAQdI6UQnQ5mlLw7Qx4%2BofhUawyxIxRUvl1O6CFIXrlaKggCebVG1JtZGTHx9xK3RmNq1MepXZPi1%2FAdxK0iyTqMztt8WyMmQQBui29l2fVnEd95N%2BxgmxriRZ%2FgtCsjvkuIb9Ac3yxtrqrxS4drvD7s%2BhI8E5%2B7hV1KMI%2F%2BuM0GOqUBHMDO9eAjIVJGAw2tUX98Cvf9aoePjALcg94Yo3jbjppvzHBB1EF7PdCs4PgIX%2Bmq02ANckzToQVZDfNCEg3OkofyW3eJhWG6s2qaCqgsQu68a%2FEyt4lbrHUCVq790bdg9SKT5xpksWcQU0O4JbVJAIq9q7MOWaKUeOat1Qdpk7FKep7VOPyCTj2qgPqMmFKEzIkc8Vub7u%2FGQP3x%2BUDzzkLJgLcn&X-Amz-Signature=5d11017f995e499196d094a83cf600479079fde385c459bc7d6156bb948f160d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4EQY3LK%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQC2kewiwFeGcvlNuQEwv0wc6zpWTZWler3Iw3dJwmciPAIgObIYzhneAgvURGp4kOtyX9pMCNk8kx6uXGYesvplGJEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJLmxA2y%2FO7aT2NG4SrcA%2B0gNkfgB5EkfseBQ9EZQY7Y1V23114HH%2BqIpGHCj%2BI3IL9n9LxOZr4FOtw51mtg9VOPYLPl1TN3XbhzDakvbau6I5WOF8Lm8Z05hTVWla1ol7jK%2Fzz67ozMgmHFkpKbHjKXuba2luv1b0B%2BhNyReF1tBlryL%2BQ4SLoe7z%2BUIrrGMyyzjExAodsoBXDsLD3uYaed8QN3%2FDmcOokKHTE8aIitP3wwiutE9DpeypLPdmdir3PpyAxb3SkcwddImI9taweFRMz1lRgChcAwFepyqj%2Bixsoc1EVYO%2BkFleYwPwtZAiItaFe0JxxOdOY773p%2BIt%2Bu1Mes00pKczrOepS3UHuYCCqRDvGgV2tTn%2FLsapAuABcN4laoD%2FVp%2BVxLsm2DvGJ2fI9shXoI8Zc8k2PXHdvPVfMiP64Gh3OwoZs%2BBdBebyN55LTCxFyDU%2FyFjw2Rpq6I8lpE77za4LV3htsqjDNJsAQdI6UQnQ5mlLw7Qx4%2BofhUawyxIxRUvl1O6CFIXrlaKggCebVG1JtZGTHx9xK3RmNq1MepXZPi1%2FAdxK0iyTqMztt8WyMmQQBui29l2fVnEd95N%2BxgmxriRZ%2FgtCsjvkuIb9Ac3yxtrqrxS4drvD7s%2BhI8E5%2B7hV1KMI%2F%2BuM0GOqUBHMDO9eAjIVJGAw2tUX98Cvf9aoePjALcg94Yo3jbjppvzHBB1EF7PdCs4PgIX%2Bmq02ANckzToQVZDfNCEg3OkofyW3eJhWG6s2qaCqgsQu68a%2FEyt4lbrHUCVq790bdg9SKT5xpksWcQU0O4JbVJAIq9q7MOWaKUeOat1Qdpk7FKep7VOPyCTj2qgPqMmFKEzIkc8Vub7u%2FGQP3x%2BUDzzkLJgLcn&X-Amz-Signature=391eac9c4ce8955950ac6ce3ef269f73a56efcf3123fad5b39508cbd1e56fd85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

