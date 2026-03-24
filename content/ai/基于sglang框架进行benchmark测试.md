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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6KCJL6T%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCxOgNJUZuW5dFI5j%2FPFzyNl9CHtOj8nTk4ySGXN02d3wIhAJaz4PLOry49TpX5kXuhK9qA4xJ%2FfBkE9BXninG69Y6OKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzMoy8qd84hGVaKwUq3AMvo%2FMyVFhtZ4vDqNQqS4kzSSd5dBG8zO7ndi3xQ9LqrZRi2OaI2ofXO5a584FE6x%2B09aJOJLRWyhcDYtAFDg6X2rX%2BvO0WOpaVo4OaFYzBmZ7%2FWfgA7Cv9IuQL6j7JcWXHKKVWtLH1Exzc3KXqclTTEqD5UojtWNO7FLZK5tTnYHNsuvKfbG4CGDUxTGm1wY6fla%2BYfDjUyWyYAKWUEWlzCv2zhTPYEEe%2BWYhbGNPR5UqanzUtiuWN9nuQE1%2BdtnYzRPWV2%2BPYaFmjcvJtB%2BZBx1eITQmrLk9L9uI7E7vL7b0Ls1rdca431ywznjuX3G0JtjnOdDrZGa3vgkBpwSAPRpAJyjjpkj1vj2WN8fmldXdlWHTtsldGmFS01QolZiN06HhOnhDTBGK8UQt6B7vmt9UEc3r%2FQeSTp2a9LNr53Evy6VAIQf%2BHPdkSULfwhbuWSzinxPOc20tb0ET1pkghbSdgcP%2F2kIGDsQudyJghFbj1Y%2BvcAWy2SkMGgc3Hm22Cx2qF4xSbKaG%2BHJzWGnc6qCYTK3osyFFKc0w7HDLgbi2aWg2mHOB1W4%2FQLXD4573V9VXe3tRAy94s7p1Y9svK9sPluDj7YZ0WatonO43Aa9sdYTdjr7S%2BkcJKRjDE9IfOBjqkAQyj5D%2FrOzbkQ5osU4FLH5EdUa4Po%2Fw4JOfqikAuMt2tr7mjomA5MPJlAC7%2FvRHNNjbN4t4WpYeWWGtrcbyiR0pABnAzZnfwDfq0qmsEOoWZ5tkPDAd%2FIoZH5AAMosmMg8wkbmoper8%2FTI%2BdddjfxPFZbmA0G5TMbEwycqiKY5SpQLNRaQoK9%2Fh%2BY46lFkMhlHrjJIhp3ml%2FMB5WVeOy5U8i78UB&X-Amz-Signature=cd295e9d516d72d02800046755615eba9bd91bf945124d8dd1159e8faa6c5b3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6KCJL6T%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCxOgNJUZuW5dFI5j%2FPFzyNl9CHtOj8nTk4ySGXN02d3wIhAJaz4PLOry49TpX5kXuhK9qA4xJ%2FfBkE9BXninG69Y6OKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzMoy8qd84hGVaKwUq3AMvo%2FMyVFhtZ4vDqNQqS4kzSSd5dBG8zO7ndi3xQ9LqrZRi2OaI2ofXO5a584FE6x%2B09aJOJLRWyhcDYtAFDg6X2rX%2BvO0WOpaVo4OaFYzBmZ7%2FWfgA7Cv9IuQL6j7JcWXHKKVWtLH1Exzc3KXqclTTEqD5UojtWNO7FLZK5tTnYHNsuvKfbG4CGDUxTGm1wY6fla%2BYfDjUyWyYAKWUEWlzCv2zhTPYEEe%2BWYhbGNPR5UqanzUtiuWN9nuQE1%2BdtnYzRPWV2%2BPYaFmjcvJtB%2BZBx1eITQmrLk9L9uI7E7vL7b0Ls1rdca431ywznjuX3G0JtjnOdDrZGa3vgkBpwSAPRpAJyjjpkj1vj2WN8fmldXdlWHTtsldGmFS01QolZiN06HhOnhDTBGK8UQt6B7vmt9UEc3r%2FQeSTp2a9LNr53Evy6VAIQf%2BHPdkSULfwhbuWSzinxPOc20tb0ET1pkghbSdgcP%2F2kIGDsQudyJghFbj1Y%2BvcAWy2SkMGgc3Hm22Cx2qF4xSbKaG%2BHJzWGnc6qCYTK3osyFFKc0w7HDLgbi2aWg2mHOB1W4%2FQLXD4573V9VXe3tRAy94s7p1Y9svK9sPluDj7YZ0WatonO43Aa9sdYTdjr7S%2BkcJKRjDE9IfOBjqkAQyj5D%2FrOzbkQ5osU4FLH5EdUa4Po%2Fw4JOfqikAuMt2tr7mjomA5MPJlAC7%2FvRHNNjbN4t4WpYeWWGtrcbyiR0pABnAzZnfwDfq0qmsEOoWZ5tkPDAd%2FIoZH5AAMosmMg8wkbmoper8%2FTI%2BdddjfxPFZbmA0G5TMbEwycqiKY5SpQLNRaQoK9%2Fh%2BY46lFkMhlHrjJIhp3ml%2FMB5WVeOy5U8i78UB&X-Amz-Signature=f665b0836c09b0a61fae7cc774d1c659a3bd1cd8c8db197722f6203d003c5280&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

