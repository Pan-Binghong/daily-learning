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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URCMFZCS%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDj0fKeFU8splm2%2BKtmhA6HdJP4wb%2Fn58qUG4sd4RhNoAiEA7DBMAhmm0afomlL87gDos5BmW88Nmx96QEjBuz8aWPAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDKuvTt7orkMR2jQSpircA0Msx%2Bb5grIatwXXYq8dpWzHicp2IdBFZZuzMx9acsHVCVq77iB2rwUTJYhWVOvBRSjPOuQT6EfQ8F61dPlxubjnltg8APiBQoAmdf2fZ0ewTBYPebfqC8jXszf2GfRmuM3ugXOAFNoyhi5R7rvBBDynK%2BEbm%2B5Ip%2FCH6AXOYsGr4D5axXbkM1lMpyR36bsz%2BZBkOv95c5iLHaiErTR59SRRJyyFwEQrRvL350y3HmwzeS%2B0T%2Blsb%2FXVaFoCeu1%2FUUGzZRC9W0HrQzatB5dTX12IZ7Aj1A6I7edPk%2Br3IfsIoN7HOGe6JDN4X5TOh%2BWFTpBcShjCgxYk5IrooyOyw4Fwu0A3BX3w2%2Ft95IHlq6Kcrl8oPiCVvAclG2tl1XRwRGiaUmjREsUrqqQksc1rjORev8X8YAoAW6P9AVuinVlc8mwKf%2F%2FTVJNURLHnnhUY7qElMbgEWklfDT8MM%2BaEU3VjEkgBPvt0zX9UwsRbqus1uJKehoCBTdWgLL5lznbg6jIUuuZDeW0f5%2B8pXbWgIk1HpKUjmVhTXYGosmB5KewNKDOQ3cmTKVGbtqHAhTVgUuEPXvqafbikSs7OucavXMIs9dJ3lKdKv7DZtAXUwIqPRNrb7AhIbXlCF0%2FUMM%2FA38gGOqUBlYz1iQAJz8H7H9vABMEsUY6LEICFybO05DexSVb4eVD5N8zTvelFfjHm24PUfZn49xG0ddRsp1zejuQO8%2B3ysjrDnNbrb33zzAqPXPL8ZY8%2Fsm%2FvaaILsS%2F3EXuwgktgVnOCI9RFFhQjP9a0PDoMCSWVUPHIH%2B3pMlH834IMnADrfMNboIw%2BLFthZfbSGJ1w2pjbpGolBbsWjtq5P3PqEOdcHfUo&X-Amz-Signature=ead04ea473452bacbf9e547e5627456b95661a342c7c2e4c9ff109c1dce04378&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URCMFZCS%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDj0fKeFU8splm2%2BKtmhA6HdJP4wb%2Fn58qUG4sd4RhNoAiEA7DBMAhmm0afomlL87gDos5BmW88Nmx96QEjBuz8aWPAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDKuvTt7orkMR2jQSpircA0Msx%2Bb5grIatwXXYq8dpWzHicp2IdBFZZuzMx9acsHVCVq77iB2rwUTJYhWVOvBRSjPOuQT6EfQ8F61dPlxubjnltg8APiBQoAmdf2fZ0ewTBYPebfqC8jXszf2GfRmuM3ugXOAFNoyhi5R7rvBBDynK%2BEbm%2B5Ip%2FCH6AXOYsGr4D5axXbkM1lMpyR36bsz%2BZBkOv95c5iLHaiErTR59SRRJyyFwEQrRvL350y3HmwzeS%2B0T%2Blsb%2FXVaFoCeu1%2FUUGzZRC9W0HrQzatB5dTX12IZ7Aj1A6I7edPk%2Br3IfsIoN7HOGe6JDN4X5TOh%2BWFTpBcShjCgxYk5IrooyOyw4Fwu0A3BX3w2%2Ft95IHlq6Kcrl8oPiCVvAclG2tl1XRwRGiaUmjREsUrqqQksc1rjORev8X8YAoAW6P9AVuinVlc8mwKf%2F%2FTVJNURLHnnhUY7qElMbgEWklfDT8MM%2BaEU3VjEkgBPvt0zX9UwsRbqus1uJKehoCBTdWgLL5lznbg6jIUuuZDeW0f5%2B8pXbWgIk1HpKUjmVhTXYGosmB5KewNKDOQ3cmTKVGbtqHAhTVgUuEPXvqafbikSs7OucavXMIs9dJ3lKdKv7DZtAXUwIqPRNrb7AhIbXlCF0%2FUMM%2FA38gGOqUBlYz1iQAJz8H7H9vABMEsUY6LEICFybO05DexSVb4eVD5N8zTvelFfjHm24PUfZn49xG0ddRsp1zejuQO8%2B3ysjrDnNbrb33zzAqPXPL8ZY8%2Fsm%2FvaaILsS%2F3EXuwgktgVnOCI9RFFhQjP9a0PDoMCSWVUPHIH%2B3pMlH834IMnADrfMNboIw%2BLFthZfbSGJ1w2pjbpGolBbsWjtq5P3PqEOdcHfUo&X-Amz-Signature=830f6f335e8ddad5ae9f7e9319b70275ac1e1db7b87a4b8a04ad2e9767ed29bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

