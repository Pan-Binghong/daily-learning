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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D7XEAXQ%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICy9J25r4vbib1TSCat8PQxfWSyJQwyJ1yFApA%2FPaurPAiEA%2B2RRZUO%2BADvPj3HuNcOCKlO3k6TkCGWwC%2B%2Bok69LBWoq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDMCDOVeaOhjn6wm7rircA4RTXBe%2FKeB%2BNUTZV9HMxKpxCqS%2BE4X992nlnAiNVFIUpK8oOc%2BwF22zQw%2FWHJNIjml2JEvoQkKc49nRHpBb1kvauXeDeKAQ%2FqTX%2BQLQJxDWjlsYuE4AhNcyocELzXFXTea1QBA2bNWL9EG2fzQCl1YPytvJqoXipJVK4wdAN2dGM1LdNxSGMKhW89xFOdFwQPkYvDq9Rql1Pbs1fTbJNlwqIR8gweoPAPoFsFyZvKPH5H%2FSVYWWFhVYXTdWk8N3cXxtsk9wNulaShd%2FuViHwFvzRKCKJRyv%2F7HIc08bHpq06z8LoTHkut6x6rp5p9uF4sMnAOfRasEW29Ks%2FbCOgJFDY8n06ZHvkaUpusPqKQY6pB%2FbAAxEO%2FJF1cVfa22Qol3VgQuobBDKWYWfXTwyVGNUBwwNibCM9G0J3pSpGwxFZK85t6PY%2FYANm%2FbPIOTMKhJXiYlxajqz0v2DqDHZS0BONOlkXoubNHvm2tF%2BYOzamacVyfRE9Y3dCmf6PuvTj%2FQr5fKctXP0enRd%2FsHvFBbUzioFl5N8DTuyyAjVoRsyS8yIZXxPcoghKVq9cZl4Fw%2FilT0Er9wlCuYHuGO02vu%2BhQ2QZv6FLPnStmJRtcoQWdmcT826YrJBGjaKMPqV5csGOqUBcUJgAO3BUiBQZrsMaMDhrDqSOwpWhqMXbYvAT8MVg8k10TV82fxVPd7vf%2BKLXDeTF%2FU%2FYtBKg02X6eU5%2BsTa47xjr2ZznDCOBt6bpaWqMURY%2FZ44oMZittEpkk27Ja5qW0yxqdnpQqCJGmQGh6XERnQLvKI52Px6Iv725byy5niYbwYYVtupGWHMyAV%2BOHyIloQHDPj4dj%2BEwB9jkh8M2S6qnq%2Fx&X-Amz-Signature=42471b6a5df1db7a2e93c1ef6a6f143ec93008fd7322efacf67673f3e98287c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D7XEAXQ%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICy9J25r4vbib1TSCat8PQxfWSyJQwyJ1yFApA%2FPaurPAiEA%2B2RRZUO%2BADvPj3HuNcOCKlO3k6TkCGWwC%2B%2Bok69LBWoq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDMCDOVeaOhjn6wm7rircA4RTXBe%2FKeB%2BNUTZV9HMxKpxCqS%2BE4X992nlnAiNVFIUpK8oOc%2BwF22zQw%2FWHJNIjml2JEvoQkKc49nRHpBb1kvauXeDeKAQ%2FqTX%2BQLQJxDWjlsYuE4AhNcyocELzXFXTea1QBA2bNWL9EG2fzQCl1YPytvJqoXipJVK4wdAN2dGM1LdNxSGMKhW89xFOdFwQPkYvDq9Rql1Pbs1fTbJNlwqIR8gweoPAPoFsFyZvKPH5H%2FSVYWWFhVYXTdWk8N3cXxtsk9wNulaShd%2FuViHwFvzRKCKJRyv%2F7HIc08bHpq06z8LoTHkut6x6rp5p9uF4sMnAOfRasEW29Ks%2FbCOgJFDY8n06ZHvkaUpusPqKQY6pB%2FbAAxEO%2FJF1cVfa22Qol3VgQuobBDKWYWfXTwyVGNUBwwNibCM9G0J3pSpGwxFZK85t6PY%2FYANm%2FbPIOTMKhJXiYlxajqz0v2DqDHZS0BONOlkXoubNHvm2tF%2BYOzamacVyfRE9Y3dCmf6PuvTj%2FQr5fKctXP0enRd%2FsHvFBbUzioFl5N8DTuyyAjVoRsyS8yIZXxPcoghKVq9cZl4Fw%2FilT0Er9wlCuYHuGO02vu%2BhQ2QZv6FLPnStmJRtcoQWdmcT826YrJBGjaKMPqV5csGOqUBcUJgAO3BUiBQZrsMaMDhrDqSOwpWhqMXbYvAT8MVg8k10TV82fxVPd7vf%2BKLXDeTF%2FU%2FYtBKg02X6eU5%2BsTa47xjr2ZznDCOBt6bpaWqMURY%2FZ44oMZittEpkk27Ja5qW0yxqdnpQqCJGmQGh6XERnQLvKI52Px6Iv725byy5niYbwYYVtupGWHMyAV%2BOHyIloQHDPj4dj%2BEwB9jkh8M2S6qnq%2Fx&X-Amz-Signature=da2047e1f160268c76ae8814df13970dccace7d5765b25a024d2c40671c2dac4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

