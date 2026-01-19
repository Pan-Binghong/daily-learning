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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RDA6IIA%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdJkyBuWymCcuVeMS7By20Y79JqZ4YaxMiERDk9%2FHOqgIhAND1sek1FGtQq3FORTPamYBBlO%2B7QCwKHTpxOET%2F0dIUKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBatXGg5kqVoupiX4q3AO7ETDtrr1ocis0FWpcD3JGP4dVijBwmyNEBIw%2BTtQLmjFbEYyW%2FrmRZvhlXYbok2COvHdBo4%2F9zDKK8YsW4BND5DPZzv2%2BXt8RmLecXPECcdSm3d5hXVN77Olk7zJCJmZeeYV3nYyrCIT%2BoeMusO2ozs5t%2FZfEUBamgzxgNS8r7mWYp0YYsviPMvvf%2Bx5wtbODTzW53KmoGqZG6R29Ntx5FSD3WlxLzb4QN6eFsIa2oNwWe1fcfyhVt2hbDne0AYjo8Gvcn0FgcejFfKI8rCFoJDrg0Ob%2FOWSE4oYkWHmXuPz76%2BJ43wXKgTSnKzlm3j8lWYLB3kT5NkKwAFlr18CxLweZjUeTjMU5h414c13AsnDn5Kyoy1Dv9EEgvEAP7n9QHPgvjHKLZjY7y5q1UboyULnbtp9jjhkeRtKmognB98IZPVM4NtfPv0lz5UNIDBYwlT61U289TNEabA6f5Wb7T4lp4qOlX2Tv4ZJd1F8VKe05bN8k4q7cah3zz6uJLBIQ4r6rYCLIGxMg0%2BAha1U5IbxHn8b%2Bgp%2BRRUdXbrv4exiyN2J6OFvbZ9Xi1svs%2FCVaxSReBcxNYxzDiMhzWedBg8ahBPxkFo1IYIdmBBKJPu0n%2B7pKEcGr3jPjNTCV3bXLBjqkAVuAJwuk6wpx14WN6HzwXmhcDTUMWUOILqEwrepIcbB5LvGnIa8YGbPo7gzIODVfP3ib%2FTE5f66jY%2BfwzJAevyAtKB47WC5JgTZwJhSr4YUHffVvsvrULwwGpfG8VBEZ73wW8nh1OUKlElegoZY4e1keWQ3Ik%2FwBKOnK78GksJ4EC9NBerqYMtPldW2r3pYkL%2BNqCM%2BWnU%2FTLylZ4mALKmOJMDFv&X-Amz-Signature=cf897db93f48e40997c002c179b675fe6810305145212665da91df385237c0f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RDA6IIA%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdJkyBuWymCcuVeMS7By20Y79JqZ4YaxMiERDk9%2FHOqgIhAND1sek1FGtQq3FORTPamYBBlO%2B7QCwKHTpxOET%2F0dIUKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBatXGg5kqVoupiX4q3AO7ETDtrr1ocis0FWpcD3JGP4dVijBwmyNEBIw%2BTtQLmjFbEYyW%2FrmRZvhlXYbok2COvHdBo4%2F9zDKK8YsW4BND5DPZzv2%2BXt8RmLecXPECcdSm3d5hXVN77Olk7zJCJmZeeYV3nYyrCIT%2BoeMusO2ozs5t%2FZfEUBamgzxgNS8r7mWYp0YYsviPMvvf%2Bx5wtbODTzW53KmoGqZG6R29Ntx5FSD3WlxLzb4QN6eFsIa2oNwWe1fcfyhVt2hbDne0AYjo8Gvcn0FgcejFfKI8rCFoJDrg0Ob%2FOWSE4oYkWHmXuPz76%2BJ43wXKgTSnKzlm3j8lWYLB3kT5NkKwAFlr18CxLweZjUeTjMU5h414c13AsnDn5Kyoy1Dv9EEgvEAP7n9QHPgvjHKLZjY7y5q1UboyULnbtp9jjhkeRtKmognB98IZPVM4NtfPv0lz5UNIDBYwlT61U289TNEabA6f5Wb7T4lp4qOlX2Tv4ZJd1F8VKe05bN8k4q7cah3zz6uJLBIQ4r6rYCLIGxMg0%2BAha1U5IbxHn8b%2Bgp%2BRRUdXbrv4exiyN2J6OFvbZ9Xi1svs%2FCVaxSReBcxNYxzDiMhzWedBg8ahBPxkFo1IYIdmBBKJPu0n%2B7pKEcGr3jPjNTCV3bXLBjqkAVuAJwuk6wpx14WN6HzwXmhcDTUMWUOILqEwrepIcbB5LvGnIa8YGbPo7gzIODVfP3ib%2FTE5f66jY%2BfwzJAevyAtKB47WC5JgTZwJhSr4YUHffVvsvrULwwGpfG8VBEZ73wW8nh1OUKlElegoZY4e1keWQ3Ik%2FwBKOnK78GksJ4EC9NBerqYMtPldW2r3pYkL%2BNqCM%2BWnU%2FTLylZ4mALKmOJMDFv&X-Amz-Signature=43881092e1e675028f14f8b52c479d59e231fd233461768093e68996333ded77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

