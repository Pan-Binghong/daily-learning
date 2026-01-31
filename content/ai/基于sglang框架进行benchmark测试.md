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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NGPSJCC%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGtUxKPPPTFL%2BAQVtvwSCnReTh1kUZSdB9s2SZjwmJ5fAiEAwZbHa5HYkIpClCk97uWqAHxi1AKX1k3DeoY9BhqmUzkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8z8uH48vqem%2FvYUyrcA6z%2BVfpURNX91pcQf2C3jlZfHI0XohZ43br%2FN09SXB%2Fru43F3qHPUKXP3xLFLy9HAAEUdXX3x3OSnl7GAkccaiD97jziII83gsjPzQqpiCFBu%2Fejg3s22fwYg077qK0UIHkt3mFNllPXeBkO%2BXxjRSx%2Fkh76yXHJhVB2v%2B1mDGeBE%2F%2BinID4VpLwrX9qnfnVb6X%2FCU3eKj0%2FbCnY7jNSUgUVrv%2BR1JXdw0XY5MifUG7gSC%2B%2FEdXOrpOmlMroaQKtv4DOVlIRTWyYo6gQ3lvRJhgfC8AqzYDxVSw4J28aLP3pFGfMfJNOkCybu%2BcFjoI1PS1j86Tf9JUDGwGoN9BSQDdO0vB7dDSSfBUtU5Q5VC6Roo3NY%2FR4xvgftqZIF1%2FlunDaRyrLzjFTPjBmnMMnAkxoKTbI2bNH2qtEvKM%2B2CALeuXbVJH7PUQRo30NXTPGT28UJOZZ1P7V3sMjrB24qqKAAITJ5hybtoFTjFMiFRrOQo0eK4Vj72ldni3c8755pOdC%2BbCGWKSes0V2cMQhXfeBhT9zA2EjifKg9RbW01fnkf70JIp1exsmNiOwjT1rvg13eEwsFcx9hpwCn3OOr%2B8pi9K5WuHDNp6i4Vv6ZD1z1lWV3Nx%2BK1M1A5%2FcMMLM9csGOqUBKTIuf8VmPrQzG04ZlEEiH9R0%2FX93tgwSl7NlnV7iuLoWH8U5LxThYWyo0j030k9sQSzana9go%2BvwGGVFwflkqAs8%2B3uZXZQ4e3ZF8iIiKyMyXY8l1b04cw%2BIvnF1XE9cozNvn4ygjNIOWnOVxomYT8sY03kT8Me9Xe4VgWv9gS3ZMqDgLJahvsPz4TE9owoCsCxa0QpMFoCnAmmBL3N1zjkJimaL&X-Amz-Signature=c8f54f145e825d47f34009208d342f67aea21cb45209ba347016e3ae55148cfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NGPSJCC%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGtUxKPPPTFL%2BAQVtvwSCnReTh1kUZSdB9s2SZjwmJ5fAiEAwZbHa5HYkIpClCk97uWqAHxi1AKX1k3DeoY9BhqmUzkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8z8uH48vqem%2FvYUyrcA6z%2BVfpURNX91pcQf2C3jlZfHI0XohZ43br%2FN09SXB%2Fru43F3qHPUKXP3xLFLy9HAAEUdXX3x3OSnl7GAkccaiD97jziII83gsjPzQqpiCFBu%2Fejg3s22fwYg077qK0UIHkt3mFNllPXeBkO%2BXxjRSx%2Fkh76yXHJhVB2v%2B1mDGeBE%2F%2BinID4VpLwrX9qnfnVb6X%2FCU3eKj0%2FbCnY7jNSUgUVrv%2BR1JXdw0XY5MifUG7gSC%2B%2FEdXOrpOmlMroaQKtv4DOVlIRTWyYo6gQ3lvRJhgfC8AqzYDxVSw4J28aLP3pFGfMfJNOkCybu%2BcFjoI1PS1j86Tf9JUDGwGoN9BSQDdO0vB7dDSSfBUtU5Q5VC6Roo3NY%2FR4xvgftqZIF1%2FlunDaRyrLzjFTPjBmnMMnAkxoKTbI2bNH2qtEvKM%2B2CALeuXbVJH7PUQRo30NXTPGT28UJOZZ1P7V3sMjrB24qqKAAITJ5hybtoFTjFMiFRrOQo0eK4Vj72ldni3c8755pOdC%2BbCGWKSes0V2cMQhXfeBhT9zA2EjifKg9RbW01fnkf70JIp1exsmNiOwjT1rvg13eEwsFcx9hpwCn3OOr%2B8pi9K5WuHDNp6i4Vv6ZD1z1lWV3Nx%2BK1M1A5%2FcMMLM9csGOqUBKTIuf8VmPrQzG04ZlEEiH9R0%2FX93tgwSl7NlnV7iuLoWH8U5LxThYWyo0j030k9sQSzana9go%2BvwGGVFwflkqAs8%2B3uZXZQ4e3ZF8iIiKyMyXY8l1b04cw%2BIvnF1XE9cozNvn4ygjNIOWnOVxomYT8sY03kT8Me9Xe4VgWv9gS3ZMqDgLJahvsPz4TE9owoCsCxa0QpMFoCnAmmBL3N1zjkJimaL&X-Amz-Signature=236817a80fded08f9235a378cdcc9928aa60565b971762e4743f3ae123578bd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

