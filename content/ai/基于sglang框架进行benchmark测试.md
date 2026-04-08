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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBUFDJTX%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIHi3OueAxWQ0Iy7%2FXZCb5PXstnU63EQoBpt1mm8T%2BgNfAiEAt9IFlKfyLzNrnrsLQOWeKd%2BVtISv%2B2LSJdT%2FaAISlR0qiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNKc6LpWP3eccG2ydircA%2BbFRWUWfqhMOQtyKKsq4%2Ffkoxpjm0BsrzbaU%2BowcGvCOyFGO3VTJJPapSXmLOmvRP5WxP0TFwuqPfpyh9z%2BAgmvMV3wHZRCV0%2BoWXl2PRTIrK0JG3NQGXq6idSa%2BujADx0AbewSsRYFM9by3Ql3JXLsuLWLiaJQ6zDYvgEwnWX%2FFd9nE91D21XHj017R5zMDGtelyk7r15IFnVKQeK4WR4Q07CbdDZJj7L7nKHlZA5j67qGUJMmNC4MrjMoBMu7gU3Z4%2FrUhqlGxbsYZ4Z5ueWXqbk356jCvq08E99KaqiRxuEMbcX%2FIvyAMlcltc2TTJFJbGwCM89PPATYQID%2FB1Y9oXVtHXrMrfysyA%2FRR1SD7RcqVKjB0Ce%2BXk0%2BsoeT2jx64qMyceIKGs5tQNwvAxsSAJEKE%2Fo2Dd%2BuNekZPT8SHvCZLqbFGVqorctg5QyWRYldu8zSBFKwtxFHP5IctuRcfH2ZpFEp6%2B8XKogfAxzpmcuRKxgdZDm3eiLqw%2BnrtpSMLDvccpYAWaUlb63mYH1kvrDUNImZHaSINFkgMrej8eMk6zJwBGp3z7TtVpYGSR6tQ2xJSY%2BPiqTWjs2gOKDq92AljmmUwyjJPw9Y1qnBu%2B3dO%2FnY%2FttaiaUOMLqI184GOqUBSgmK1PyVCbMLvfL8Y%2BByYKOuAko3WmkJ7DzY4RiKjFGAFl9nSd3zVLii8jfSwOVi7dn%2BLDGQWGZ5iF3DBuf2grKguPtQnVQ7VjL9VyUwx58dNgBtb0TfNluxxSyaezHD4TPy%2BVf8Ln21gAxPVqssKLOdUJxl5rSfUElyLi1zWuftYObq%2FF1KMZ3kmeYPG%2FgWISd3BKGvgK46SajaGWPDfjtN5GYB&X-Amz-Signature=3d7a786eb9626a5c9c56d5b80292fc915c91a9b09116a79e95a788906451a11f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBUFDJTX%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIHi3OueAxWQ0Iy7%2FXZCb5PXstnU63EQoBpt1mm8T%2BgNfAiEAt9IFlKfyLzNrnrsLQOWeKd%2BVtISv%2B2LSJdT%2FaAISlR0qiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNKc6LpWP3eccG2ydircA%2BbFRWUWfqhMOQtyKKsq4%2Ffkoxpjm0BsrzbaU%2BowcGvCOyFGO3VTJJPapSXmLOmvRP5WxP0TFwuqPfpyh9z%2BAgmvMV3wHZRCV0%2BoWXl2PRTIrK0JG3NQGXq6idSa%2BujADx0AbewSsRYFM9by3Ql3JXLsuLWLiaJQ6zDYvgEwnWX%2FFd9nE91D21XHj017R5zMDGtelyk7r15IFnVKQeK4WR4Q07CbdDZJj7L7nKHlZA5j67qGUJMmNC4MrjMoBMu7gU3Z4%2FrUhqlGxbsYZ4Z5ueWXqbk356jCvq08E99KaqiRxuEMbcX%2FIvyAMlcltc2TTJFJbGwCM89PPATYQID%2FB1Y9oXVtHXrMrfysyA%2FRR1SD7RcqVKjB0Ce%2BXk0%2BsoeT2jx64qMyceIKGs5tQNwvAxsSAJEKE%2Fo2Dd%2BuNekZPT8SHvCZLqbFGVqorctg5QyWRYldu8zSBFKwtxFHP5IctuRcfH2ZpFEp6%2B8XKogfAxzpmcuRKxgdZDm3eiLqw%2BnrtpSMLDvccpYAWaUlb63mYH1kvrDUNImZHaSINFkgMrej8eMk6zJwBGp3z7TtVpYGSR6tQ2xJSY%2BPiqTWjs2gOKDq92AljmmUwyjJPw9Y1qnBu%2B3dO%2FnY%2FttaiaUOMLqI184GOqUBSgmK1PyVCbMLvfL8Y%2BByYKOuAko3WmkJ7DzY4RiKjFGAFl9nSd3zVLii8jfSwOVi7dn%2BLDGQWGZ5iF3DBuf2grKguPtQnVQ7VjL9VyUwx58dNgBtb0TfNluxxSyaezHD4TPy%2BVf8Ln21gAxPVqssKLOdUJxl5rSfUElyLi1zWuftYObq%2FF1KMZ3kmeYPG%2FgWISd3BKGvgK46SajaGWPDfjtN5GYB&X-Amz-Signature=96112d63be031b716212b4878002a5fce05042b53774ee08618cd8b0f3086fc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

