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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSAB7OKR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA31l6q1Y3XaXZ9SNPRzpXgrZi5fS4vYb7LjuCdtOSRIAiBtQ2eCIZEQ%2Fzno9EQnfMubYBIg36SIOLDPc1VQMXR3Rir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMykZNVUewnk9clqQyKtwDZt7N%2FovGzy8WGo1GPY%2BuxQBzFFqoofIEdRLGHupGdfOYDlpVY%2B%2BqSM4DrK51poWchdCwhmA%2FKo7B94S%2BS7oVqwXhcLtUwx5FwQY7CUjD%2BO2ZtZNu4v2VY%2FyX8gTD7fkQ1TVCPH0p4H7xtF0yFSrwAvqKnVqjn3IrmdBzGSvVmtXrlR6Xfi2lOLRnHFI4BfNBRQiuVci2%2BKw17sVl3xia4FL9D5BNXLinp0w3y1qUrfcfaL0x0wULTjTJTydqwUuJF4fstgGCOSCvC9WDw3P4G%2Bv0WQhacT8ojUs9t2xyTMUiW%2FWrKuNqX%2Bzgj3sW1L%2F33LUsF67wchmGw2BFV5N37n1w9ZT0LlrzQZM4aqTKOvLdYPuc4E92MSWhRmbBJOW7P1n58cRZD2lgs%2B4Xs7UQWoCv4zUcFHK6jaE5%2FNFd3jUd7jwjMjgqhmzcXEJu2ddPo355S7qPxUxi1CmmsF9%2BB6vUG8P9bkoK4VAdulrfdPvFRbi6s4EGdWUCqdLWCKvjlJv2Y%2BunZf89R1Xck0mteqYyd207NZqfExW1K9qYhKwvVe0qOUNXDKbZEmS3duwGSsc9DjTJDtZsQXP3OquB8ZYoajx7PuLOa2R9q%2FFdj2rLqSVr83iT0PEnT1Ew1YnayAY6pgEDADZ04dQJhlD7%2Bjg9jGC41Q6AH1n3DCmyD5xyOMZZ1u1KsHSdcKtxWVkdX4D%2BqCdP1QlT9DxPoI7%2BWungYVOw2LBC630wSzz%2FgQACz4LNdiWtCmju3efBObIr2NHaayClgW84Bt0xlkblga5ejgsBU6qYm%2FmQXaY01Q3qbZvVGrBmQoutOBPrRk39j4G2VKPEocKNVIEpBkLS1kp%2Bnpu6JSbC14vT&X-Amz-Signature=26b9eab5c5d1bd2731b243053826104e8eb14c7573627f442757fca40db46c10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSAB7OKR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA31l6q1Y3XaXZ9SNPRzpXgrZi5fS4vYb7LjuCdtOSRIAiBtQ2eCIZEQ%2Fzno9EQnfMubYBIg36SIOLDPc1VQMXR3Rir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMykZNVUewnk9clqQyKtwDZt7N%2FovGzy8WGo1GPY%2BuxQBzFFqoofIEdRLGHupGdfOYDlpVY%2B%2BqSM4DrK51poWchdCwhmA%2FKo7B94S%2BS7oVqwXhcLtUwx5FwQY7CUjD%2BO2ZtZNu4v2VY%2FyX8gTD7fkQ1TVCPH0p4H7xtF0yFSrwAvqKnVqjn3IrmdBzGSvVmtXrlR6Xfi2lOLRnHFI4BfNBRQiuVci2%2BKw17sVl3xia4FL9D5BNXLinp0w3y1qUrfcfaL0x0wULTjTJTydqwUuJF4fstgGCOSCvC9WDw3P4G%2Bv0WQhacT8ojUs9t2xyTMUiW%2FWrKuNqX%2Bzgj3sW1L%2F33LUsF67wchmGw2BFV5N37n1w9ZT0LlrzQZM4aqTKOvLdYPuc4E92MSWhRmbBJOW7P1n58cRZD2lgs%2B4Xs7UQWoCv4zUcFHK6jaE5%2FNFd3jUd7jwjMjgqhmzcXEJu2ddPo355S7qPxUxi1CmmsF9%2BB6vUG8P9bkoK4VAdulrfdPvFRbi6s4EGdWUCqdLWCKvjlJv2Y%2BunZf89R1Xck0mteqYyd207NZqfExW1K9qYhKwvVe0qOUNXDKbZEmS3duwGSsc9DjTJDtZsQXP3OquB8ZYoajx7PuLOa2R9q%2FFdj2rLqSVr83iT0PEnT1Ew1YnayAY6pgEDADZ04dQJhlD7%2Bjg9jGC41Q6AH1n3DCmyD5xyOMZZ1u1KsHSdcKtxWVkdX4D%2BqCdP1QlT9DxPoI7%2BWungYVOw2LBC630wSzz%2FgQACz4LNdiWtCmju3efBObIr2NHaayClgW84Bt0xlkblga5ejgsBU6qYm%2FmQXaY01Q3qbZvVGrBmQoutOBPrRk39j4G2VKPEocKNVIEpBkLS1kp%2Bnpu6JSbC14vT&X-Amz-Signature=467001a803ae9a28e18ca16454c4487964c849e32d31467dfe25af489c5968a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

