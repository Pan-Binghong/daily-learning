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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRKUKMSB%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCT3KpV6HNHWGTTAZjSVqQoLxboLM6Z%2BpuLiXljwNgdaQIhALVxFYvuUjYfGX%2Fx23iDVInur40swY8Lv%2FhGrXrjKK8RKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5azKE4Dyhdg5WkKoq3AN%2Fr4MUYjCks%2Fb9VwY1udng1czGVO6gJfqH8UmdYU4JW0GRy%2FRS4luXc%2F%2BJwxLo%2FiAHHEDB2%2FeqZydR5PalA%2FCrYQpshFrPT1kqs1D5JgebamvtZFtzdD3vROSWgxTMnYPfIM%2B83Ly3%2FAGrHo5s5zaYaT%2B0WL11ue8cD2PzvI7ec9QIHo6EHNQedz4niF%2FeQ3vFSYN19qYpF9iLehWe9qanKb6WJ%2F7Tip8OgFr8zg65jSXDcyDNqaGxohawt6kUU9xc%2B5y6SBAT2DdHQFeVZtDLA3JyCzhzbULhRZP405PD64IvMwsPB2qAGp16saUQJYMVF1xkb0y0i6AudKXG5k17OulnXEQUpdT1PejPzyWqGhtA2uHLAA%2BY8Inp1TIGWiAXf4CvVQbnghQisW9yDikJtheeDOGQQdAwS3Pr8mFju0rfxZCG%2BJjq1GzW9UGfcFtSjiNxiQAuPSDQyUsyEKj%2FU2WQSSBmm2vO6HTlcVp1gUcR31%2BQ92sCpFFUteeN38hp%2BoeRduOnWLnhcYbQIro83laYKLh2b4QuQ5BblGM038Cd62t1JOJDvvKgBtepnoykIyFJsBvyAB3vcw2MShEHfLHa7fU%2BiVTMQ6EVwbHi6zdEvRzKdSJ6XIO39jDz4OTIBjqkAZHcqACsEC6qIOhcLNGKXSZy%2BehAs3%2BGsKGB%2FsXJQesV18dYIEWOkrNfr5ltCjSA25NhtDcfwZzcGdDoCv%2FbWa%2FsqZbW7J9P7m3RgpC9EQ1n1g8QA8JT%2Bp6GDTlU360Sj4Ku%2BlPCBuFKO%2FiMUCk8npdEwhtbfUJtQtl9GfqtGaAu5BdxgX3BqoV3D26vLbLmUx8%2B3glLw7i6AIc0SEcnHbo3Qjyu&X-Amz-Signature=d8b2115348ecfe1f9b3bd346447b130dd59e3387f3fa85ee8ef714638e0dd7d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRKUKMSB%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCT3KpV6HNHWGTTAZjSVqQoLxboLM6Z%2BpuLiXljwNgdaQIhALVxFYvuUjYfGX%2Fx23iDVInur40swY8Lv%2FhGrXrjKK8RKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5azKE4Dyhdg5WkKoq3AN%2Fr4MUYjCks%2Fb9VwY1udng1czGVO6gJfqH8UmdYU4JW0GRy%2FRS4luXc%2F%2BJwxLo%2FiAHHEDB2%2FeqZydR5PalA%2FCrYQpshFrPT1kqs1D5JgebamvtZFtzdD3vROSWgxTMnYPfIM%2B83Ly3%2FAGrHo5s5zaYaT%2B0WL11ue8cD2PzvI7ec9QIHo6EHNQedz4niF%2FeQ3vFSYN19qYpF9iLehWe9qanKb6WJ%2F7Tip8OgFr8zg65jSXDcyDNqaGxohawt6kUU9xc%2B5y6SBAT2DdHQFeVZtDLA3JyCzhzbULhRZP405PD64IvMwsPB2qAGp16saUQJYMVF1xkb0y0i6AudKXG5k17OulnXEQUpdT1PejPzyWqGhtA2uHLAA%2BY8Inp1TIGWiAXf4CvVQbnghQisW9yDikJtheeDOGQQdAwS3Pr8mFju0rfxZCG%2BJjq1GzW9UGfcFtSjiNxiQAuPSDQyUsyEKj%2FU2WQSSBmm2vO6HTlcVp1gUcR31%2BQ92sCpFFUteeN38hp%2BoeRduOnWLnhcYbQIro83laYKLh2b4QuQ5BblGM038Cd62t1JOJDvvKgBtepnoykIyFJsBvyAB3vcw2MShEHfLHa7fU%2BiVTMQ6EVwbHi6zdEvRzKdSJ6XIO39jDz4OTIBjqkAZHcqACsEC6qIOhcLNGKXSZy%2BehAs3%2BGsKGB%2FsXJQesV18dYIEWOkrNfr5ltCjSA25NhtDcfwZzcGdDoCv%2FbWa%2FsqZbW7J9P7m3RgpC9EQ1n1g8QA8JT%2Bp6GDTlU360Sj4Ku%2BlPCBuFKO%2FiMUCk8npdEwhtbfUJtQtl9GfqtGaAu5BdxgX3BqoV3D26vLbLmUx8%2B3glLw7i6AIc0SEcnHbo3Qjyu&X-Amz-Signature=73e2a6af042aa5ad2a3ffdb3d16cb96bbec1c9a2236405b2c39a754071c59e46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

