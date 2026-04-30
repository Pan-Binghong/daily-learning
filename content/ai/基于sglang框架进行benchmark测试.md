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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRVJYYDW%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCID5pLHVS%2BpwW3%2Fc3YFxE%2Fn5K0yG%2BDUqO3lh3qjqvCuBuAiAM9FwXZ4r76kQE%2Fdt9QH7dQ90f7Of4FdG06hf7QkUMSyr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMvEGXMopH%2F98WW4U4KtwDx8XgVRenot1sg6DXs9MzET%2FA2PJtXwHyYsQxUk1clX9SjBx6I2erCvmQppU1zhLr2iCZNqHUQ2A83xcSk%2BHpELUp3d%2F4y3w6gikCm%2Bw9FeHdzAOaVCv7M46zrEWMCsHdOGbSVjRWaag5Wv3gwYb6zu1fz5WLApriCjOPMQSlNKDnChEDEja3UcwRe8cdN%2BVKAQmc3%2BjtcfJ4S4PKm6U%2Fms2Xy%2BTOVEyRo%2BwI2I5f9%2F2%2BAJPPXIUBp5k1Jigf6djCC9ZJlGmc9ed0DqBpAetT5F1yKWinPeVz5KCYjEUcbmKaNI%2BAnjST0fkYq0eIXvcyCb0ELZb1avBJvda8B5jOmyRI1zk7KtvWdYs8degAKY6uELRcMbTvdq4pSn1IfsdE3iNhQa%2B8dDSxvTXW2aiQldW3B8JxAR44PI36sWj0RKPX66pSaPLlvjVHyi9OXmeueuE749FdPbNySfTWiMfPE34hErSb2WZgxQJf%2FC1iZ1vURQAwL3JLWbov7PeYCQhT8bOB0M%2F9Id%2BdZ07snMY5Hg%2BXjc4w%2FWCBu95c8OIYmUuazQQ%2FgWQHXn6oADMjxP5reY2hETuPLQZL4dYv6PXzUcEAtw0XEBg93UADjpKH1zm4CAjvXp15hR2Er3cw9LHLzwY6pgFC9IoWBsWt8zGp8QkuuSXHyUV9B8gPheXDMXQrBe1aMm5F8fTjV4%2BufrzE7VPYxFRdZkK2%2BgYg35cmzbkTwoSMDlcrwqyz4D8q%2Bj9IigNsq6MH9Y4iQr5OPj64BnUV3gos47sQ1Qmm5FsJWUNa2XvJTLwUkqvq7FWSM%2FSzGvYc41TpAAC7qUMc%2FLN1buCPdd2FkJ6vx3nZpbiOd8uEPagbkEXYfyTi&X-Amz-Signature=0353b8205fd8684b9cee9425463e554688954b7113c9a3dd301c2fb787d376de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRVJYYDW%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCID5pLHVS%2BpwW3%2Fc3YFxE%2Fn5K0yG%2BDUqO3lh3qjqvCuBuAiAM9FwXZ4r76kQE%2Fdt9QH7dQ90f7Of4FdG06hf7QkUMSyr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMvEGXMopH%2F98WW4U4KtwDx8XgVRenot1sg6DXs9MzET%2FA2PJtXwHyYsQxUk1clX9SjBx6I2erCvmQppU1zhLr2iCZNqHUQ2A83xcSk%2BHpELUp3d%2F4y3w6gikCm%2Bw9FeHdzAOaVCv7M46zrEWMCsHdOGbSVjRWaag5Wv3gwYb6zu1fz5WLApriCjOPMQSlNKDnChEDEja3UcwRe8cdN%2BVKAQmc3%2BjtcfJ4S4PKm6U%2Fms2Xy%2BTOVEyRo%2BwI2I5f9%2F2%2BAJPPXIUBp5k1Jigf6djCC9ZJlGmc9ed0DqBpAetT5F1yKWinPeVz5KCYjEUcbmKaNI%2BAnjST0fkYq0eIXvcyCb0ELZb1avBJvda8B5jOmyRI1zk7KtvWdYs8degAKY6uELRcMbTvdq4pSn1IfsdE3iNhQa%2B8dDSxvTXW2aiQldW3B8JxAR44PI36sWj0RKPX66pSaPLlvjVHyi9OXmeueuE749FdPbNySfTWiMfPE34hErSb2WZgxQJf%2FC1iZ1vURQAwL3JLWbov7PeYCQhT8bOB0M%2F9Id%2BdZ07snMY5Hg%2BXjc4w%2FWCBu95c8OIYmUuazQQ%2FgWQHXn6oADMjxP5reY2hETuPLQZL4dYv6PXzUcEAtw0XEBg93UADjpKH1zm4CAjvXp15hR2Er3cw9LHLzwY6pgFC9IoWBsWt8zGp8QkuuSXHyUV9B8gPheXDMXQrBe1aMm5F8fTjV4%2BufrzE7VPYxFRdZkK2%2BgYg35cmzbkTwoSMDlcrwqyz4D8q%2Bj9IigNsq6MH9Y4iQr5OPj64BnUV3gos47sQ1Qmm5FsJWUNa2XvJTLwUkqvq7FWSM%2FSzGvYc41TpAAC7qUMc%2FLN1buCPdd2FkJ6vx3nZpbiOd8uEPagbkEXYfyTi&X-Amz-Signature=08dbf93b8eb746939be69eb6003ea8e7bf804a89dedd2b3debd6b8405bc3f838&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

