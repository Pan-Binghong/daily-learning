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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS6BVZHW%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDOUcJp4LrUNKubIuuGsi%2FprZo9ydZMor765JzuAgXIsgIhAKhVkh%2Bz4izzY2jJi98W0buT6r0Qr33dYfcLtxeqsQaAKv8DCEMQABoMNjM3NDIzMTgzODA1IgzQDdxtHpLGj7raQJEq3AOroOBsmVw2iL2EDFDIZUNqa2oVpNAnkwPh4tgqkHEvTMSmJ3cafr8wv9pi9HFMxjtOPb8hwqTzxRaFLGJRWslAHl3dek6J0Cj03rij3vb30SVwgqXIbcfVmHHNIiCvl4%2FWRD6I%2Bfcq%2BwwlzxGnRAEhxdoeKZjMvkQe0pnVhpZMh7AL4X0yCeztMAAIGHorYs0M5MZ5ItkVSxOqJi6%2ByNRJDveOyv0iPf496fTHkCP%2F4tSbllwA9ZtWDD%2FmuQ8WE15seUXVi92UkMINnDM%2BWIYBesKvYEomCgufPcVpS5i%2FVEvoo01I2QzN5TWymOOe4kZ3VcpXgw%2BfzOdKU%2BoQRBMKhAR7XhAIUuJs5POTuAPR%2FqLB%2BjwXZWRbWbin%2FtaAgdo7WRUAIoETS0bjEoqLPfqIRD5KGEJJbxbYN9TA0AJwiiuLP9ugCy6Nl7mQWcPkJU2OpfmcbOsruVJH42jTRde52CsUkNQmnUGH0chhe2ZuZ2X2tSqMZiCsenzCsT6%2BWKqxvIjhobCs%2B0VqFv3yhU5oADzmvL8eBUuOUy11JJX91zXZnJhr6Y2qHSFrSVYFRfPsKsUtY%2BxSwNSyWYg6B1z1lEXb0haCDgKNWvk1qTbk%2FYjUgQPNTMZ2c2smITDQv6bLBjqkAbF%2BZ%2FXEvbR7yc1qhpesxGP2YcXnnBJijaG9OwOKRLrjimPUQo3uRHv6XZt1kbwTFC0oWnl8uqruL9MuLwpP0S33ygOonD%2FrfTd5IJ7aalhnxOAbw6JfMrQ5yB4Zh60RA3sCiBM0F1aQTrl9p4Ig7vKE2YNICg%2FKrGRFp3D5pYt2kYBdkteTNxFsprznEm2EFVC3Td6LTofRGwVydvb91pSfpMpl&X-Amz-Signature=60efd3d94beae2697ce5fde84c51cb03d4d84ad4c98abf190d3e065aff6c5eef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS6BVZHW%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDOUcJp4LrUNKubIuuGsi%2FprZo9ydZMor765JzuAgXIsgIhAKhVkh%2Bz4izzY2jJi98W0buT6r0Qr33dYfcLtxeqsQaAKv8DCEMQABoMNjM3NDIzMTgzODA1IgzQDdxtHpLGj7raQJEq3AOroOBsmVw2iL2EDFDIZUNqa2oVpNAnkwPh4tgqkHEvTMSmJ3cafr8wv9pi9HFMxjtOPb8hwqTzxRaFLGJRWslAHl3dek6J0Cj03rij3vb30SVwgqXIbcfVmHHNIiCvl4%2FWRD6I%2Bfcq%2BwwlzxGnRAEhxdoeKZjMvkQe0pnVhpZMh7AL4X0yCeztMAAIGHorYs0M5MZ5ItkVSxOqJi6%2ByNRJDveOyv0iPf496fTHkCP%2F4tSbllwA9ZtWDD%2FmuQ8WE15seUXVi92UkMINnDM%2BWIYBesKvYEomCgufPcVpS5i%2FVEvoo01I2QzN5TWymOOe4kZ3VcpXgw%2BfzOdKU%2BoQRBMKhAR7XhAIUuJs5POTuAPR%2FqLB%2BjwXZWRbWbin%2FtaAgdo7WRUAIoETS0bjEoqLPfqIRD5KGEJJbxbYN9TA0AJwiiuLP9ugCy6Nl7mQWcPkJU2OpfmcbOsruVJH42jTRde52CsUkNQmnUGH0chhe2ZuZ2X2tSqMZiCsenzCsT6%2BWKqxvIjhobCs%2B0VqFv3yhU5oADzmvL8eBUuOUy11JJX91zXZnJhr6Y2qHSFrSVYFRfPsKsUtY%2BxSwNSyWYg6B1z1lEXb0haCDgKNWvk1qTbk%2FYjUgQPNTMZ2c2smITDQv6bLBjqkAbF%2BZ%2FXEvbR7yc1qhpesxGP2YcXnnBJijaG9OwOKRLrjimPUQo3uRHv6XZt1kbwTFC0oWnl8uqruL9MuLwpP0S33ygOonD%2FrfTd5IJ7aalhnxOAbw6JfMrQ5yB4Zh60RA3sCiBM0F1aQTrl9p4Ig7vKE2YNICg%2FKrGRFp3D5pYt2kYBdkteTNxFsprznEm2EFVC3Td6LTofRGwVydvb91pSfpMpl&X-Amz-Signature=032cb8b7f07bbae11345bbdd6c9d10bfa9d1a2430173d338e704fbd6dc9a2b3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

