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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGERMVX4%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwEPEtPojpNSfti7CInMmuN7T7cQ9zVzB5BaZSycEPswIhAL7vDf0ZpzQEqqKlULWNrXaV6anEgvyp8bl1TXdQF%2B4eKv8DCH8QABoMNjM3NDIzMTgzODA1IgxPBngnS9CzMduO7%2Foq3AMfpfqsbvjF4IPZBaeyY61QYz%2B%2Bpe07NG1PKbxvi39S7I6oZHfja4JCCdf9H%2BGKd%2BPusDwOb0AfMb3MyV9DWLmOJI5eoUE61fkTQXhkZezZVR1UzR%2FtQibyENgakJXA8DRNNcpT%2B1Rx2z8ogJ6yU41mCf9WEsNXzfsMG7GVTvhLAe7n9bWWA7aHAXvlLV2Z49pBJWSlfdU2LxW3vOJ5vPzqKWV2rYMU%2FgX%2BdUBR2AZqQ1AkhbN1wJBlI6y8mdqzZw2TFAFFkykCYDCYLUBRvWs7rTki%2BV7zMyLCPlU7C%2B9RBYww5E5U%2F4lBl%2BucPRJqDaCKUeKIx45cD347lo98CHy2GvaJnsWpiLaNY35pzvkGuph4MNdExqwS5vZLGqToFj0Lvx%2FOVvlS5%2BOyAMO6dwjTPLbZieslTzIMgDPCxVlFWmCMefymTTgIGa2Vu0VCvpmGFvxMFQ2w3oUvH%2BsVZbVZZRGNIar77mOjkuhp%2F%2BhNabEv3XJ0txwK5NP77jF48NbNoPIaIKeCzpUGcgd%2F2H%2Fc9VOKt2oUiK9jzPRl8wbx2WMbNcEu%2FihocarZLkBeg17wd55aQeEITIlDvF76SRqS5M19A9JXfB5jbVLlXBY5eFadqlmVt56YsVV6AzCArb3OBjqkAWh%2BkMupOfBu09M26RNPz6i%2BKg8qfZm6tfDPsNlnvIJY%2BoZzSYVsqQ6r4FkVGXxg2keSdDS3UXPtZWCq%2Bb0aLNs087m2PgXdbyfd6%2Bbu%2BlvgtzN8CNEv%2FBQXIco3kCfdHb6bU6MBFgZ5ci6sOMe4G2pRKinFvtzN7DieEaUgf4IDFbofNRjpGemXal3%2BHB9nJqCB2NV38hwy3owjK2MJnGKlCjZx&X-Amz-Signature=fdcc0e7d97fb34984abf52bf12060dbcf55da5f529484117688236295453fe09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGERMVX4%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwEPEtPojpNSfti7CInMmuN7T7cQ9zVzB5BaZSycEPswIhAL7vDf0ZpzQEqqKlULWNrXaV6anEgvyp8bl1TXdQF%2B4eKv8DCH8QABoMNjM3NDIzMTgzODA1IgxPBngnS9CzMduO7%2Foq3AMfpfqsbvjF4IPZBaeyY61QYz%2B%2Bpe07NG1PKbxvi39S7I6oZHfja4JCCdf9H%2BGKd%2BPusDwOb0AfMb3MyV9DWLmOJI5eoUE61fkTQXhkZezZVR1UzR%2FtQibyENgakJXA8DRNNcpT%2B1Rx2z8ogJ6yU41mCf9WEsNXzfsMG7GVTvhLAe7n9bWWA7aHAXvlLV2Z49pBJWSlfdU2LxW3vOJ5vPzqKWV2rYMU%2FgX%2BdUBR2AZqQ1AkhbN1wJBlI6y8mdqzZw2TFAFFkykCYDCYLUBRvWs7rTki%2BV7zMyLCPlU7C%2B9RBYww5E5U%2F4lBl%2BucPRJqDaCKUeKIx45cD347lo98CHy2GvaJnsWpiLaNY35pzvkGuph4MNdExqwS5vZLGqToFj0Lvx%2FOVvlS5%2BOyAMO6dwjTPLbZieslTzIMgDPCxVlFWmCMefymTTgIGa2Vu0VCvpmGFvxMFQ2w3oUvH%2BsVZbVZZRGNIar77mOjkuhp%2F%2BhNabEv3XJ0txwK5NP77jF48NbNoPIaIKeCzpUGcgd%2F2H%2Fc9VOKt2oUiK9jzPRl8wbx2WMbNcEu%2FihocarZLkBeg17wd55aQeEITIlDvF76SRqS5M19A9JXfB5jbVLlXBY5eFadqlmVt56YsVV6AzCArb3OBjqkAWh%2BkMupOfBu09M26RNPz6i%2BKg8qfZm6tfDPsNlnvIJY%2BoZzSYVsqQ6r4FkVGXxg2keSdDS3UXPtZWCq%2Bb0aLNs087m2PgXdbyfd6%2Bbu%2BlvgtzN8CNEv%2FBQXIco3kCfdHb6bU6MBFgZ5ci6sOMe4G2pRKinFvtzN7DieEaUgf4IDFbofNRjpGemXal3%2BHB9nJqCB2NV38hwy3owjK2MJnGKlCjZx&X-Amz-Signature=2e9a03b45303ff463b6d3f203acf5d5a3f7e8278319fb24e9ec4e00e7c0e7aed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

