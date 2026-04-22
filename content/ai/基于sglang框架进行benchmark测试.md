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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGHAYGL5%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHxWLuDOU%2FJ9LD9NUODQnVIf1eOrZ20%2BIxBGz%2F5i9K4uAiEA7PlnMXcmYXMV6oShqzcRBYeEA8vHUvDIAi74fzUvtrYq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDLanifzboQUMBQoCZircA7nfkG8Fcg5bcBvQkAHEoI6kPCZQ%2BUKYiFqstCYo%2Byi0l9vTU%2B9WlB3Qr9NNwNbTMf5W5KhBrudG66%2BvoXtqjbRlFyC8C3fd41GQlSA6IweHwodTc0KHXOXk220824y4%2FYRbmfMc%2FzjynKGQM0cMkXaNBENIZyeq3Ks5FTqQ2aHJ9l2KrewA4h4%2FMyh2BW%2BuQim%2BmAslt0Kg5w5sRme7xpVZO5qNmyL7MRXMpmc5wLgiMIGGjB7OxX5Wj5XRR4lXQQiZsp30Al3b4ZkG8kTCLqNOfRQ9eUriFkldFKj35aECCoEvbkFWq1tCJE%2BsihN4nJsGeJv6C19GgOEZoE13gu42v564S5ynIpXoi4C5FdYzeM%2FiZF7knl0DSf8rM8jXqTzpUMxZ5%2FeXmQtvCOq3D3vz2f9rtjLNjiMBY93knqaPZHltoah48%2BI%2FbmJw%2FfJH09xDkgjpN0K0ERT8HbVURw8azxlByJQSNLYw3vW66Wk%2FauvGEMYX3zOJDYxJ23JStYnYSDPlut00tlnhPpfHqbnzWPJeA4f05uiY75NRskRcFIa7szSLrBjjsJGUUTcfYymfOMZsgmR6JX2yca%2B%2BwW%2BY81VPUtQyqNB0xyNWp5jXQXoQuF6g0D%2FszY2QMN37oM8GOqUB4PrxRTw7CZzevKytcKz7abGVpfJkwG%2FKoL4t3GD%2Ba9Q1hWekn5KxStNAXdpc3stW3WETuhxW2GFoTbxLG0raFMnlBUkKkTpi9%2FvLB0dheS1ZKJ8SPMTRSBcwF%2BNskZ9szLCvE6DYgAkSfIQMXPywrz8C5Ryq3lpDAkGCNhBul0uhul9OMP9RXfrIWfEGjZUP1QqrL3KO3VbkxNyiYGscHLzvCG4h&X-Amz-Signature=4036d32b7c8269f1d63058ea546eaca700626fd85ac6d80dd40eebc38b76a6ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGHAYGL5%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHxWLuDOU%2FJ9LD9NUODQnVIf1eOrZ20%2BIxBGz%2F5i9K4uAiEA7PlnMXcmYXMV6oShqzcRBYeEA8vHUvDIAi74fzUvtrYq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDLanifzboQUMBQoCZircA7nfkG8Fcg5bcBvQkAHEoI6kPCZQ%2BUKYiFqstCYo%2Byi0l9vTU%2B9WlB3Qr9NNwNbTMf5W5KhBrudG66%2BvoXtqjbRlFyC8C3fd41GQlSA6IweHwodTc0KHXOXk220824y4%2FYRbmfMc%2FzjynKGQM0cMkXaNBENIZyeq3Ks5FTqQ2aHJ9l2KrewA4h4%2FMyh2BW%2BuQim%2BmAslt0Kg5w5sRme7xpVZO5qNmyL7MRXMpmc5wLgiMIGGjB7OxX5Wj5XRR4lXQQiZsp30Al3b4ZkG8kTCLqNOfRQ9eUriFkldFKj35aECCoEvbkFWq1tCJE%2BsihN4nJsGeJv6C19GgOEZoE13gu42v564S5ynIpXoi4C5FdYzeM%2FiZF7knl0DSf8rM8jXqTzpUMxZ5%2FeXmQtvCOq3D3vz2f9rtjLNjiMBY93knqaPZHltoah48%2BI%2FbmJw%2FfJH09xDkgjpN0K0ERT8HbVURw8azxlByJQSNLYw3vW66Wk%2FauvGEMYX3zOJDYxJ23JStYnYSDPlut00tlnhPpfHqbnzWPJeA4f05uiY75NRskRcFIa7szSLrBjjsJGUUTcfYymfOMZsgmR6JX2yca%2B%2BwW%2BY81VPUtQyqNB0xyNWp5jXQXoQuF6g0D%2FszY2QMN37oM8GOqUB4PrxRTw7CZzevKytcKz7abGVpfJkwG%2FKoL4t3GD%2Ba9Q1hWekn5KxStNAXdpc3stW3WETuhxW2GFoTbxLG0raFMnlBUkKkTpi9%2FvLB0dheS1ZKJ8SPMTRSBcwF%2BNskZ9szLCvE6DYgAkSfIQMXPywrz8C5Ryq3lpDAkGCNhBul0uhul9OMP9RXfrIWfEGjZUP1QqrL3KO3VbkxNyiYGscHLzvCG4h&X-Amz-Signature=9df2d9ec6a34240fcf2d1a9f8cf82ec0f7adb536b31a42681fb50c6a253e6cb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

