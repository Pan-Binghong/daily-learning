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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FA6GZ2U%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7yCH2H3246QZULi6xHuCIa%2FkEFKOl9gN%2BHt0TH80IKQIhAJ1zETXWIm0YZVwrppBrUUxXAd1kGTTtvS0BHqXVbHHuKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGenqV99MQIuVHCwAq3ANylO0D26l0tuFFJRwJBX6X99UTabJMy0FiKFa2SjGamrjIWpXg4Yw21tVJUCguYity6BsWzR%2Fe1pU6pVhFOtcSEDZZhZzRW%2BvZjR3L4mQNPipHpfgQNdTxs4WWc94XfYkGXXFKKQbINmUv9I4v9HpooO6h%2BMihQIyNc%2Bs7SHymlMPYs4JVbhMJ2AMMPCPL%2FM9Qc%2FXUJ4wzvlWIhmBmdoqFJtlax6eoIZEquYbiqoRjMsrm5kveZga1U9v2pD4LHUAF7ezBjl%2FtcQ1GTalBsHqzqIALM4CrObKnRu5I6IsGPIr7IQSobG79FkkuCidYSFPWOFqtN4sX8CeVKF0%2F3xonhCxJb3abSxFwBITuOtKn1TCFJwDCgJ0RFqpDtnanWfwEOqLkF8Axc%2FBRb7d2BKM%2FX5cquMYRtW2ur5A1uXVwLedpiV8OwiUz9GgIIk0ErZucsk%2BF10gvMM9dThY6jNXciA1FLMrzFDrk1QD9v4wXexHMwuL%2FUINsjlZnMgm0kJfj94af%2Fb9b7iOWzE6lqYlmVvOwTXWRwbwiJLIu3zJZkJAasBhdkUCILsa5ibTQNDJN4xw1QmKFPeip2cH8NAB%2FNX5n429FcBHC%2B1QI3JKEXVqBeJL2v7mXAPT%2FWDDtmO%2FIBjqkAZG0XVrMJC1T%2BITvC7vAvF3lUEDrIU%2BPXCj%2FK0XMLy6rlXdi5AHYWj7K9947BxVaPwDKrqRcffjo9%2By9Cwc8TmXBlETZV0hKyt9gjvn2JIPdzv%2BQ9ofnt37IDzuHo8%2FWuU8%2FfK3AwGSQpFrI9RQcbwgO7jFEWFRJTwZs8H9BNgB7juLIGuKVq3bSv6bCME1DjJ8a1kCLMZeu5t%2FoufZv6oY3RV%2Fs&X-Amz-Signature=d373d395c6f2f63964f321d02eb07951b59b43b94eaa5d86aed1e8aa896fe922&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FA6GZ2U%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7yCH2H3246QZULi6xHuCIa%2FkEFKOl9gN%2BHt0TH80IKQIhAJ1zETXWIm0YZVwrppBrUUxXAd1kGTTtvS0BHqXVbHHuKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGenqV99MQIuVHCwAq3ANylO0D26l0tuFFJRwJBX6X99UTabJMy0FiKFa2SjGamrjIWpXg4Yw21tVJUCguYity6BsWzR%2Fe1pU6pVhFOtcSEDZZhZzRW%2BvZjR3L4mQNPipHpfgQNdTxs4WWc94XfYkGXXFKKQbINmUv9I4v9HpooO6h%2BMihQIyNc%2Bs7SHymlMPYs4JVbhMJ2AMMPCPL%2FM9Qc%2FXUJ4wzvlWIhmBmdoqFJtlax6eoIZEquYbiqoRjMsrm5kveZga1U9v2pD4LHUAF7ezBjl%2FtcQ1GTalBsHqzqIALM4CrObKnRu5I6IsGPIr7IQSobG79FkkuCidYSFPWOFqtN4sX8CeVKF0%2F3xonhCxJb3abSxFwBITuOtKn1TCFJwDCgJ0RFqpDtnanWfwEOqLkF8Axc%2FBRb7d2BKM%2FX5cquMYRtW2ur5A1uXVwLedpiV8OwiUz9GgIIk0ErZucsk%2BF10gvMM9dThY6jNXciA1FLMrzFDrk1QD9v4wXexHMwuL%2FUINsjlZnMgm0kJfj94af%2Fb9b7iOWzE6lqYlmVvOwTXWRwbwiJLIu3zJZkJAasBhdkUCILsa5ibTQNDJN4xw1QmKFPeip2cH8NAB%2FNX5n429FcBHC%2B1QI3JKEXVqBeJL2v7mXAPT%2FWDDtmO%2FIBjqkAZG0XVrMJC1T%2BITvC7vAvF3lUEDrIU%2BPXCj%2FK0XMLy6rlXdi5AHYWj7K9947BxVaPwDKrqRcffjo9%2By9Cwc8TmXBlETZV0hKyt9gjvn2JIPdzv%2BQ9ofnt37IDzuHo8%2FWuU8%2FfK3AwGSQpFrI9RQcbwgO7jFEWFRJTwZs8H9BNgB7juLIGuKVq3bSv6bCME1DjJ8a1kCLMZeu5t%2FoufZv6oY3RV%2Fs&X-Amz-Signature=982d27c823e15aba7ecc24631683ac2a2a9b25cc3320a0cdb615d9462d12777d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

