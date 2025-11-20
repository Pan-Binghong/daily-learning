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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCJAT6K%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCDhk1uBFZPdlQmGEaxgbUSnt80o9NqpT8%2FQ7PpkTu74gIgXp4g3GtxaNEqHACP0o7WAz%2Bzpx3%2Bk%2BdG14LRj6T1%2FmcqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDeu16pQA3kqqofDECrcA4g6PTA36CDanpOyLzeETORK3LxGGlOqqZ%2BPGr2NamA2WoeoMPAqZTqDkx58XLD2yvHL10KZgJPAP%2F5CzbgHmmWd3y2fEbDHI6mvzqG973MlrLOvc2EiR4dCbX7MHPTL9oUkVBaXExFQ04SjeeJOtbzFRn7dLqTSp9MFEsOtKHaq4nkcZ61A7eQIlg0pLoQ8byo%2Bnoo0fd9TDfv40tflVRul2fXXQOYJzQaMuQZeXclwdKNwVP8uotEObAyOfX9KLTvHLZT98xYJ5zJkLlj2JL6bFI0WTrDfTHULnn5bnnSqhHkRUZOKzZ%2FC4h7A9wYo5HsE%2Bki7nbmMHntRc4bqBERYDtcvf0fqihkAVidRbGgblcFVHQx2%2BPptHQof8oRijpL2Dq6%2BJ6czqAk5f3jwzHsoF9aae8Y6MicXcyUwppa33WszSpqCnHs1fk1smfRTBX0j8BLL8qxVhT2ah%2B5LdKv7%2FmZmQ%2Bipr8wTQqVpPVVUNaae3VhzLd%2FkqlYA%2FyKqk%2BlUY3ry5xC2FmBR0DL3xSEuaM3O6obc0lItZ8qdDEwJVj1XdADFVtq4peLwG9IAk9F6hl4YdkUBxg2EIo1ubvtShpHN2C9szsRgxDAFHR6W9X6iID68SXtTbsNRMPPq%2BcgGOqUB3UAqRtsrL6sUEtAX9F%2FhlfHDe8yVOESASq0OPnfalSH9edO0DPIpumVJCLmpXM5vq6y3y7rVeqJHWr9vn%2FkaCd03Ly0ANXT2ijOcqAQzholZhh9VIa4wftpkogElOkSZbUmSh3P9NcgnOrdGo7GeKZJfnuOVkLRV04kkU5Dqz%2FC7TcaMBcURhfiJw6ESxUdratPmRdDilPT5iXyZpNDBvUKazAiq&X-Amz-Signature=edfba2b33ffd995ccd1169cb4310b2718484bf02f787fe0cdfd3143854cc0569&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCJAT6K%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCDhk1uBFZPdlQmGEaxgbUSnt80o9NqpT8%2FQ7PpkTu74gIgXp4g3GtxaNEqHACP0o7WAz%2Bzpx3%2Bk%2BdG14LRj6T1%2FmcqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDeu16pQA3kqqofDECrcA4g6PTA36CDanpOyLzeETORK3LxGGlOqqZ%2BPGr2NamA2WoeoMPAqZTqDkx58XLD2yvHL10KZgJPAP%2F5CzbgHmmWd3y2fEbDHI6mvzqG973MlrLOvc2EiR4dCbX7MHPTL9oUkVBaXExFQ04SjeeJOtbzFRn7dLqTSp9MFEsOtKHaq4nkcZ61A7eQIlg0pLoQ8byo%2Bnoo0fd9TDfv40tflVRul2fXXQOYJzQaMuQZeXclwdKNwVP8uotEObAyOfX9KLTvHLZT98xYJ5zJkLlj2JL6bFI0WTrDfTHULnn5bnnSqhHkRUZOKzZ%2FC4h7A9wYo5HsE%2Bki7nbmMHntRc4bqBERYDtcvf0fqihkAVidRbGgblcFVHQx2%2BPptHQof8oRijpL2Dq6%2BJ6czqAk5f3jwzHsoF9aae8Y6MicXcyUwppa33WszSpqCnHs1fk1smfRTBX0j8BLL8qxVhT2ah%2B5LdKv7%2FmZmQ%2Bipr8wTQqVpPVVUNaae3VhzLd%2FkqlYA%2FyKqk%2BlUY3ry5xC2FmBR0DL3xSEuaM3O6obc0lItZ8qdDEwJVj1XdADFVtq4peLwG9IAk9F6hl4YdkUBxg2EIo1ubvtShpHN2C9szsRgxDAFHR6W9X6iID68SXtTbsNRMPPq%2BcgGOqUB3UAqRtsrL6sUEtAX9F%2FhlfHDe8yVOESASq0OPnfalSH9edO0DPIpumVJCLmpXM5vq6y3y7rVeqJHWr9vn%2FkaCd03Ly0ANXT2ijOcqAQzholZhh9VIa4wftpkogElOkSZbUmSh3P9NcgnOrdGo7GeKZJfnuOVkLRV04kkU5Dqz%2FC7TcaMBcURhfiJw6ESxUdratPmRdDilPT5iXyZpNDBvUKazAiq&X-Amz-Signature=cec47f47ac3adcbf8b66f68c4c81e0cb8ba76e28f586891d1e648ad41f103f36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

