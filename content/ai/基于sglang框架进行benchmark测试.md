---
title: 基于SGLang框架进行Benchmark测试
date: '2025-03-21T00:33:00.000Z'
lastmod: '2025-03-21T02:46:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKHVCJML%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC24oeIn4lvcuH2oY%2FcxL9uVmLc9w%2FHdpEsOcCpX6HdHQIgPewJfIOdPuw12h2Xne7hYOx3tQwn6qTrTq9vjS0r7%2BwqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDVpFGuWCskc1cEcLyrcAyVSAqE54fNTRUL1WcBw2%2BMrv6iu34m%2FSdI%2B42DxGtuhQx66Ca5jLR9oj39Uq8yr7Q%2Bzhe7YAMbEqq5mDKJ5bO2%2BfyIA6ls%2FS4tsIQ5KL23KCklWtLt6pKcama9wa2Loi1Exs0H3g0hPcKDla%2BlG%2B%2FcaD5s5OonLeULU3Z5YTqxyWyDGC9Fd1LiV6DITIVnxoxUszfmiCkVO2yZUpE3ZITHu2pYD9u3p5aXg8m27UWeReb4A9aOGacCFBib5%2F4gzzypzHFtQB6DBw0JJGittHdD3o4VsHTadAj9ZkYQ3lHpGQEVPC3qZ9Kjj45qn7F9SBxlRiisaImrWU0oclWT2zhsununT%2BfjQmfGAMDsgeWdEepLTO5%2FHsgHaRPu3Jl75aJNEcWZY8MeeJ%2BOAVr0oQF5sr0DEAeJglWPR1eovqhQtFc%2FAXquDL79L0VEfHLhEgWUfIwHHGt1Ai4sOKhIb8aN8nBXZ26hn3bhgcyETnUee%2FPfIUkYK2RqRkxE9DvkD6ECMuyHh0n3OxvHlmIkhBjCtWhw6K1IYPJgVHh72QfY7b7rkIl4aqIawDy5lsnty%2FtirtwkLLqaDryABlXmgf5pzYKjRD40lg0tCVWEZepM4nJspaNcjzS7rHST8MNmirMgGOqUBYVsHhoMMYpBGigQ7Tj2jPkk8KPy99zSb%2FR6YdRoQg%2BsfP2ZhtqSWEPNobdRMEGQnE1eUAjsNd6QqOlLMwn0nnc0vd68e5YWie5TQyM%2BQ7Oe%2F%2FHo2YQRohU6L8WArDT6Kby3nHJCz9qZO2ZZB59qzt9nirLIlYFfuUVOyhPWYgVtuwbCeIwQFwd1X06Pz1GLe%2BD5nWEX5Pv0tvpVfsk33SzZTgL0C&X-Amz-Signature=fb8dfbda5138d7fb08e8aa748ed9c9fad418eda6c24a27a56117a8353e18ca60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKHVCJML%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC24oeIn4lvcuH2oY%2FcxL9uVmLc9w%2FHdpEsOcCpX6HdHQIgPewJfIOdPuw12h2Xne7hYOx3tQwn6qTrTq9vjS0r7%2BwqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDVpFGuWCskc1cEcLyrcAyVSAqE54fNTRUL1WcBw2%2BMrv6iu34m%2FSdI%2B42DxGtuhQx66Ca5jLR9oj39Uq8yr7Q%2Bzhe7YAMbEqq5mDKJ5bO2%2BfyIA6ls%2FS4tsIQ5KL23KCklWtLt6pKcama9wa2Loi1Exs0H3g0hPcKDla%2BlG%2B%2FcaD5s5OonLeULU3Z5YTqxyWyDGC9Fd1LiV6DITIVnxoxUszfmiCkVO2yZUpE3ZITHu2pYD9u3p5aXg8m27UWeReb4A9aOGacCFBib5%2F4gzzypzHFtQB6DBw0JJGittHdD3o4VsHTadAj9ZkYQ3lHpGQEVPC3qZ9Kjj45qn7F9SBxlRiisaImrWU0oclWT2zhsununT%2BfjQmfGAMDsgeWdEepLTO5%2FHsgHaRPu3Jl75aJNEcWZY8MeeJ%2BOAVr0oQF5sr0DEAeJglWPR1eovqhQtFc%2FAXquDL79L0VEfHLhEgWUfIwHHGt1Ai4sOKhIb8aN8nBXZ26hn3bhgcyETnUee%2FPfIUkYK2RqRkxE9DvkD6ECMuyHh0n3OxvHlmIkhBjCtWhw6K1IYPJgVHh72QfY7b7rkIl4aqIawDy5lsnty%2FtirtwkLLqaDryABlXmgf5pzYKjRD40lg0tCVWEZepM4nJspaNcjzS7rHST8MNmirMgGOqUBYVsHhoMMYpBGigQ7Tj2jPkk8KPy99zSb%2FR6YdRoQg%2BsfP2ZhtqSWEPNobdRMEGQnE1eUAjsNd6QqOlLMwn0nnc0vd68e5YWie5TQyM%2BQ7Oe%2F%2FHo2YQRohU6L8WArDT6Kby3nHJCz9qZO2ZZB59qzt9nirLIlYFfuUVOyhPWYgVtuwbCeIwQFwd1X06Pz1GLe%2BD5nWEX5Pv0tvpVfsk33SzZTgL0C&X-Amz-Signature=e25c11ceb2d2614c39f70735f3913da22e17e0d526b4e3ab40bf2ebc150b6d53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

