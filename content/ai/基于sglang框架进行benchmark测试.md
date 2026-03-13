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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIU3CGGH%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9IwkU5Hb%2FBG89%2BJtcGDQiP6Ve7N6sKSDawJoZio0XDAiEAtW32kBbkhHLfhtoNGklJ9TUZrx%2F5HjrOtny4baaf%2FHsqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNraJL5c3yhNFTR1qircA2resgUe1WoHCX3v%2FG0tkDB54A9DW991AYB1bsfQZUzCo1FaDnxS8hD4lvFDJJNGL4xFZTY3JEf%2FzxpCK9bRScfH9AP7nrGzwdI%2FSxgqkAZV5j8l72X8TolUAJ41%2F98r%2B9l1rsLFyl1ud9337wI2yqjDzn%2BRktNf9kU3LtOPHYcoZVP48N4ACBIwBbAm8i9j3CS2zG2Ilqjn4rNt1k%2B94BzqZTbKySB6IsuSqT2pCc0l%2FlAR9sS6s65kwXR4aQQUMx3EYShkybFuI%2BTwGcb46pm0K1477n9gZj2Gb7V7BWgvisjmPljH1NrD3KgERxmiZI4BptPIqkpzcfnykXDJuC2VG3fGBZpny85BKK8JyGQwGLDb4%2FIFPb0uj8%2BYbLsUj9y5mbpRR12xGcrPccsthv%2B8EiM8InF1jSWuIVueRGNRWlObCzuxQmOgba8nqHUWPg3%2B2NHf%2BdHVGG75ROoUk0SwDSKdsbcP0%2Btnc72Q80EVfnHTLVx9rwTzNsJXg90Jv%2FNY7FdZRlbLV8kaNUGAu7QfgwEd9ayzXsszvdazqAnYtb8ibFW9vQ%2BmwTQWlVrriHtD2YM0fwAseCHTotcrE64PqjwXOxcr8KLjZDeMQ8AMz44ji4KldXXb7yI5MOi3zc0GOqUByBMCWuuWRasPRvkEnB74Z8dn%2FuTi9TmW%2FAeKbBR8aogVfkqWrBrJKRoPcXFn94bMJNJBGSMUJ3D4WFMYyJPMQP3e15SmDOj2FjF%2Bd%2BmTsoiW3S436YHalZAWH2q6uQmv8au4%2B5eQWR5FdoBrEOqzUzGPj0u4Crh9hQf5zNIUL3BrE%2BW%2BdEIg0Yl3doP84fRhv7wYtQpw00W66BodgiBKHTkSqePh&X-Amz-Signature=281bad1c2d335aec966698bc02c45ebcd54ed9e39b0c326c28d68dda2ddaeaad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIU3CGGH%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9IwkU5Hb%2FBG89%2BJtcGDQiP6Ve7N6sKSDawJoZio0XDAiEAtW32kBbkhHLfhtoNGklJ9TUZrx%2F5HjrOtny4baaf%2FHsqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNraJL5c3yhNFTR1qircA2resgUe1WoHCX3v%2FG0tkDB54A9DW991AYB1bsfQZUzCo1FaDnxS8hD4lvFDJJNGL4xFZTY3JEf%2FzxpCK9bRScfH9AP7nrGzwdI%2FSxgqkAZV5j8l72X8TolUAJ41%2F98r%2B9l1rsLFyl1ud9337wI2yqjDzn%2BRktNf9kU3LtOPHYcoZVP48N4ACBIwBbAm8i9j3CS2zG2Ilqjn4rNt1k%2B94BzqZTbKySB6IsuSqT2pCc0l%2FlAR9sS6s65kwXR4aQQUMx3EYShkybFuI%2BTwGcb46pm0K1477n9gZj2Gb7V7BWgvisjmPljH1NrD3KgERxmiZI4BptPIqkpzcfnykXDJuC2VG3fGBZpny85BKK8JyGQwGLDb4%2FIFPb0uj8%2BYbLsUj9y5mbpRR12xGcrPccsthv%2B8EiM8InF1jSWuIVueRGNRWlObCzuxQmOgba8nqHUWPg3%2B2NHf%2BdHVGG75ROoUk0SwDSKdsbcP0%2Btnc72Q80EVfnHTLVx9rwTzNsJXg90Jv%2FNY7FdZRlbLV8kaNUGAu7QfgwEd9ayzXsszvdazqAnYtb8ibFW9vQ%2BmwTQWlVrriHtD2YM0fwAseCHTotcrE64PqjwXOxcr8KLjZDeMQ8AMz44ji4KldXXb7yI5MOi3zc0GOqUByBMCWuuWRasPRvkEnB74Z8dn%2FuTi9TmW%2FAeKbBR8aogVfkqWrBrJKRoPcXFn94bMJNJBGSMUJ3D4WFMYyJPMQP3e15SmDOj2FjF%2Bd%2BmTsoiW3S436YHalZAWH2q6uQmv8au4%2B5eQWR5FdoBrEOqzUzGPj0u4Crh9hQf5zNIUL3BrE%2BW%2BdEIg0Yl3doP84fRhv7wYtQpw00W66BodgiBKHTkSqePh&X-Amz-Signature=9f6bb7647a0bd5626882948114da55acb84aca096b0da6cf94c58d352821a568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

