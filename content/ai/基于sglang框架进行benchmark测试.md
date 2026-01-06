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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXGXD4F5%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjTMFDhcEXKn7%2BADLEhOnapm68sKJlPT1g1jt8AXfHyQIgCFI2E8MEMyr5cm7aJq7uZgKBKWq%2FU3gjYLQjqi4WZLIq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDGTcFm6wYtDzGFjw9CrcA2wBniCm9rfC4msiA5yvr9b3sEVRKCIpjK9FBm69WM%2BNw38CgetpEdtgfrcTVK%2BMV1qZCHibf62Z7a9WQ0KOivZduzeFXunxKIaBaCs43o4x1Fr298XPA%2B7AITQzDTNFX%2BGu4LAHsSY5vQLc%2F5Kvb0cz1R38KGT0gLtUReuxAOD1Slt1CahUNARflj6U%2F2T67f65RrasF96fzD4q6awR%2FgNhCK53h6euyF7%2Bp%2FklRzE4xJ6cLImZ4eczhVKFh5UPUeExDzfSyS3vpY%2F%2F2FAE4OoSYUQ9%2Bm7BUqvXmLmnGIcj9XiJw139OGm9IGpCL2jijfRcDUjDByVovNTTanAwqUftKV1lyLStrI7joj%2BsHglyMB6NCVs8aQwq9jtj%2FIgRJnZSjRJ1ZXGLzLKFqmAMN%2B7xt%2BXjVJwZWDwFpxoZtTYAXSnY0dRboveBGtFyF2DLE5ghcLPUi7b0J0kBYJZGzb7oEEqm2S6Lcy0tUCONGiIPfxDJHO84Ymeej2PQTnUrUIPAoBqHB2Zq2Y%2BzlW6jIfwF5igG3dpbhMkEbAI51Gs4TeyI5q%2F%2FcpLvin1P5b6FFqdxul6Ew4wIXjrmSjA92F4WLgMiGpIsAabpGMZ3uUy%2Fws4gs3JweQzAJFUYMKzl8coGOqUBzL9Bdszl2KXnucvS%2BnqtZwNQ3%2BNt9O8NBfp3dACt%2BdAfSdvwY%2FpAwL7Jd9hTl8WGsU4cChKwnkFEzFzcMCiDjTqbF%2FdwMb0G2r3UXMnSGv5NecF32Lp7tJ8o%2BI2%2FJ6GET34aST65mH%2BU9GRBxe2pbw6d9x7GW1m%2BlhnFLysYQxrfMABFf2jF5aqZNDwH9IobtzA5cdqteglRuHNHl8oP66UMIOfF&X-Amz-Signature=768b7d10deb71fee9df142b6cc22b54a23fc09fae803df9a2f506b44a8633efd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXGXD4F5%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjTMFDhcEXKn7%2BADLEhOnapm68sKJlPT1g1jt8AXfHyQIgCFI2E8MEMyr5cm7aJq7uZgKBKWq%2FU3gjYLQjqi4WZLIq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDGTcFm6wYtDzGFjw9CrcA2wBniCm9rfC4msiA5yvr9b3sEVRKCIpjK9FBm69WM%2BNw38CgetpEdtgfrcTVK%2BMV1qZCHibf62Z7a9WQ0KOivZduzeFXunxKIaBaCs43o4x1Fr298XPA%2B7AITQzDTNFX%2BGu4LAHsSY5vQLc%2F5Kvb0cz1R38KGT0gLtUReuxAOD1Slt1CahUNARflj6U%2F2T67f65RrasF96fzD4q6awR%2FgNhCK53h6euyF7%2Bp%2FklRzE4xJ6cLImZ4eczhVKFh5UPUeExDzfSyS3vpY%2F%2F2FAE4OoSYUQ9%2Bm7BUqvXmLmnGIcj9XiJw139OGm9IGpCL2jijfRcDUjDByVovNTTanAwqUftKV1lyLStrI7joj%2BsHglyMB6NCVs8aQwq9jtj%2FIgRJnZSjRJ1ZXGLzLKFqmAMN%2B7xt%2BXjVJwZWDwFpxoZtTYAXSnY0dRboveBGtFyF2DLE5ghcLPUi7b0J0kBYJZGzb7oEEqm2S6Lcy0tUCONGiIPfxDJHO84Ymeej2PQTnUrUIPAoBqHB2Zq2Y%2BzlW6jIfwF5igG3dpbhMkEbAI51Gs4TeyI5q%2F%2FcpLvin1P5b6FFqdxul6Ew4wIXjrmSjA92F4WLgMiGpIsAabpGMZ3uUy%2Fws4gs3JweQzAJFUYMKzl8coGOqUBzL9Bdszl2KXnucvS%2BnqtZwNQ3%2BNt9O8NBfp3dACt%2BdAfSdvwY%2FpAwL7Jd9hTl8WGsU4cChKwnkFEzFzcMCiDjTqbF%2FdwMb0G2r3UXMnSGv5NecF32Lp7tJ8o%2BI2%2FJ6GET34aST65mH%2BU9GRBxe2pbw6d9x7GW1m%2BlhnFLysYQxrfMABFf2jF5aqZNDwH9IobtzA5cdqteglRuHNHl8oP66UMIOfF&X-Amz-Signature=f6c650c6e18d83c444841f2a5433d5f05af7865e552fc971c2ea020bd0644248&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

