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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WBURDEQ%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIBLC2LWYlt5z4zpCLPJqpBaKvJFuzEkQFxfq7%2FWaF%2By7AiEAh3X1zoTF3F0iQsm4VTlcOpgkiStzIh8sHzze2i3h4FYqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAxT%2F8L%2B4p6tyVwyFircA9bwIAkE4%2FyYB%2FiAks1bZ4XQ6M53QFKbDUyF9ol9ip0Xq8uDlexLV0fpRd9ACJdiv4WI6EDAh0HTg3PgxeBv014QFJyW16DznL4QEbFWQ3nyJ1SknYpp9mCyShiZD%2FrIdok3wRfAALXjyvcKQmHyrmDhsubVyLWNvLqp38L1BhGCBcoEDZ%2BEXsQoOhx0DTLzGwZmkYjXjy73CYrFy3NW%2FFeB7XFNcBMHMEzordYJbuHkq2GEPN%2B8UNEA%2FsTiYpLCl%2BgcHfqNQH34S1jqZhscFcDxjG9VGxMgx3gCPyPPmW00B4s12ALty84XY%2FoiHwvLjhQDoK6Lc03HQB5H%2FEg93czZR9z2dNMaAQfNiVAEC4LifSC2GkgvJAGFDNNuZ%2BkCuqWSbpHlDgGccsFjzPGOYpCpKhVU1CRqg67rAfMhKADiMg5oU863wY0UyaVKylo2V9SbFRcFs2W0XsPMTJ5fswI6uiafDCdKvtZv8N4u%2BT4w0QaVpT0vFZ6DUwDAQkgbZvpYvEzVJB00CFpYigCCKvC%2Fzi0cWCa6CPM%2BaX6oDJTmYGcoYCWosmcvkpPxbyX7MvBH6Yy8JlPxsumEedCXngclE6g1M%2FEd8l%2FzVKk5q2pDpkrLw4S7rMS8XN0kMKCvy8sGOqUB60Dp3WlZauSpPvkaD1gLDgBjZK1xwih5jmbAoQjv2em3rXG1PVSN5XWU4vPRzklboCov8Brn1U6U7NvUu4tOL%2BqltLKz0%2BW3UCwEu0D1mXfHJO%2FkoL8rPOoojST6o88sXYicQhKdJrNJaQqd%2B0XEswyJR8ctVncezqgYSodkBAutBywH2n2%2FQLkfouysS9XO0csf%2BBBfRVSvZKvv5no%2FRse7EHn9&X-Amz-Signature=ca203c2f223000ab87d4801c44a60f48f5dc95f82a91a93a53a189774f383711&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WBURDEQ%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIBLC2LWYlt5z4zpCLPJqpBaKvJFuzEkQFxfq7%2FWaF%2By7AiEAh3X1zoTF3F0iQsm4VTlcOpgkiStzIh8sHzze2i3h4FYqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAxT%2F8L%2B4p6tyVwyFircA9bwIAkE4%2FyYB%2FiAks1bZ4XQ6M53QFKbDUyF9ol9ip0Xq8uDlexLV0fpRd9ACJdiv4WI6EDAh0HTg3PgxeBv014QFJyW16DznL4QEbFWQ3nyJ1SknYpp9mCyShiZD%2FrIdok3wRfAALXjyvcKQmHyrmDhsubVyLWNvLqp38L1BhGCBcoEDZ%2BEXsQoOhx0DTLzGwZmkYjXjy73CYrFy3NW%2FFeB7XFNcBMHMEzordYJbuHkq2GEPN%2B8UNEA%2FsTiYpLCl%2BgcHfqNQH34S1jqZhscFcDxjG9VGxMgx3gCPyPPmW00B4s12ALty84XY%2FoiHwvLjhQDoK6Lc03HQB5H%2FEg93czZR9z2dNMaAQfNiVAEC4LifSC2GkgvJAGFDNNuZ%2BkCuqWSbpHlDgGccsFjzPGOYpCpKhVU1CRqg67rAfMhKADiMg5oU863wY0UyaVKylo2V9SbFRcFs2W0XsPMTJ5fswI6uiafDCdKvtZv8N4u%2BT4w0QaVpT0vFZ6DUwDAQkgbZvpYvEzVJB00CFpYigCCKvC%2Fzi0cWCa6CPM%2BaX6oDJTmYGcoYCWosmcvkpPxbyX7MvBH6Yy8JlPxsumEedCXngclE6g1M%2FEd8l%2FzVKk5q2pDpkrLw4S7rMS8XN0kMKCvy8sGOqUB60Dp3WlZauSpPvkaD1gLDgBjZK1xwih5jmbAoQjv2em3rXG1PVSN5XWU4vPRzklboCov8Brn1U6U7NvUu4tOL%2BqltLKz0%2BW3UCwEu0D1mXfHJO%2FkoL8rPOoojST6o88sXYicQhKdJrNJaQqd%2B0XEswyJR8ctVncezqgYSodkBAutBywH2n2%2FQLkfouysS9XO0csf%2BBBfRVSvZKvv5no%2FRse7EHn9&X-Amz-Signature=9d298edd60435b374690059c01f52e8001c5e320bcb415252157326c5ba9ff42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

