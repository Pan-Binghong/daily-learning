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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6THPILD%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHTumvJbaGqXgRb2HtiIFzxqKZxHcvtWQt%2BET5loyv6mAiEAwlbtr74qSilKLUMWRmLHJb3g39R5IwTXs4I6iKZsQQIq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDOuq5B74Gzz035cW%2FSrcA22xvqd5BzvzXT3JHHzH99d9CcHI%2BWlhPFqWyzb6Dh7tualI4C6q8XGtla4yXqDuJFxFj0pa9fix49Xve6mAsCAD8xsA%2BY9lmGq4cTJXHYuMpbG%2BwywUBS9xsPxXojZTTnP4MNaUMC%2BUUkKwXmP9fQZ2Mc6vARpQ4di%2BMuPMh0BvAitDXfE6e%2BaqkSC8ek%2BCTat6KpqKTcJGcRV2VYNDEVEFn5q0PMf9iSbOxW5XzHjMzvY%2F9afU9n8Bzm3pm7TfuBEPkRaA90lvrk0FpsEzBnN4QAWOj6YDMYecIB5fC0wKmbX5ty5PGWn1RXuGYg6KJaNj6FUHJ7Krji5Or7ZBeTH%2ByXqdRyADqveKQGYbuj0VwT3wedcv01NSJNEoPmr7iA6wHtzaRGnOVIuQ6D4gUpgnb2g%2B9LRGNLNnjcGN0VLDjQD2pP9CLVzO4X8JriJ6ZhYmTT529pYSrCXcX%2Fs3ROGAxfRQgsGpQRtgY7xRTb%2B2qTIME7FwkNwF4iHfpZrW0sIG3KS5%2ByOcfKQg4fn5YlEIHSNCa6mbnODPoDr8mCa%2FEKWD4MaKiTTszxDOpwzcPWCc3qVBl7SyTvmzmHCiFsbTeP02oWkG5NfwKbK5z4wCz0%2FMCJMcrfNkR5SMMICwq88GOqUB9KdoxY5UBhovcDtQMfYq1rhelCRTD3CvRCXn9gAkifrmdxJaUTFaNPJmmmCuOIoB8EdQ6xERshVeuxz%2BiU5eB9D5mtyPI3xFE9HEEJtF%2FIH1W8mQtL0Rsq0QoSFj8BnWxyFf4YlJKMov3jJxPIPDVUVGB6aQqDxd3xjxYf7ZUCQVxRx8JLv6LVE5GW4pv%2FBMxZwQDptnlV%2BKt0EntZm42bTVbwb2&X-Amz-Signature=1df41dfe8f125a430cb10adb268ad323e65ca0e299099254d5dec865609571b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6THPILD%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHTumvJbaGqXgRb2HtiIFzxqKZxHcvtWQt%2BET5loyv6mAiEAwlbtr74qSilKLUMWRmLHJb3g39R5IwTXs4I6iKZsQQIq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDOuq5B74Gzz035cW%2FSrcA22xvqd5BzvzXT3JHHzH99d9CcHI%2BWlhPFqWyzb6Dh7tualI4C6q8XGtla4yXqDuJFxFj0pa9fix49Xve6mAsCAD8xsA%2BY9lmGq4cTJXHYuMpbG%2BwywUBS9xsPxXojZTTnP4MNaUMC%2BUUkKwXmP9fQZ2Mc6vARpQ4di%2BMuPMh0BvAitDXfE6e%2BaqkSC8ek%2BCTat6KpqKTcJGcRV2VYNDEVEFn5q0PMf9iSbOxW5XzHjMzvY%2F9afU9n8Bzm3pm7TfuBEPkRaA90lvrk0FpsEzBnN4QAWOj6YDMYecIB5fC0wKmbX5ty5PGWn1RXuGYg6KJaNj6FUHJ7Krji5Or7ZBeTH%2ByXqdRyADqveKQGYbuj0VwT3wedcv01NSJNEoPmr7iA6wHtzaRGnOVIuQ6D4gUpgnb2g%2B9LRGNLNnjcGN0VLDjQD2pP9CLVzO4X8JriJ6ZhYmTT529pYSrCXcX%2Fs3ROGAxfRQgsGpQRtgY7xRTb%2B2qTIME7FwkNwF4iHfpZrW0sIG3KS5%2ByOcfKQg4fn5YlEIHSNCa6mbnODPoDr8mCa%2FEKWD4MaKiTTszxDOpwzcPWCc3qVBl7SyTvmzmHCiFsbTeP02oWkG5NfwKbK5z4wCz0%2FMCJMcrfNkR5SMMICwq88GOqUB9KdoxY5UBhovcDtQMfYq1rhelCRTD3CvRCXn9gAkifrmdxJaUTFaNPJmmmCuOIoB8EdQ6xERshVeuxz%2BiU5eB9D5mtyPI3xFE9HEEJtF%2FIH1W8mQtL0Rsq0QoSFj8BnWxyFf4YlJKMov3jJxPIPDVUVGB6aQqDxd3xjxYf7ZUCQVxRx8JLv6LVE5GW4pv%2FBMxZwQDptnlV%2BKt0EntZm42bTVbwb2&X-Amz-Signature=b2ec7a460afd02ee7ee5881f3cf1e900247eeffcd073848aabf2bf04343b2afd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

