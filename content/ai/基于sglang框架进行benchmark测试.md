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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TITXHTJI%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIDzEP%2FPFKPC1uhzc69rFYMEYxBt81VQ6Rcq6lqZ1VF7HAiB7wjOYI7rU4yao91h1QLR%2FJzrKuUJrlDdiop8xIz5wZyr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMmICSSdvpgA7aV29rKtwD5q4j9LcaeJQHnRhcCFjZ6HfwSmx4Z4D0e%2FQHcOxIYCiSpBXC%2BcVdIqFK2jm6C7PgXMksEPrnyCLf9PY7S%2B%2FpTgb29apMbeo0in8XS3QORoK9cu6hXY8zhw7A7JxdtRg3wZyILLjj4IMM2lV%2FFSQ2p2w2HhO%2B2w13ToWLV2uOVQxPwucVGSTuJm8ooFYbbH9G4v9MAx0VeFv9ew0DOcLscQ%2BNr9%2B7QRigSiME4b8JzArXCI53xEh6z4Ic3RgK26itkZ4SE%2BxwxRng10WNnc1SIwe0kEsJtU3G4iygVmd2hZsHRzR18pgqBdvypit%2Fs8W1cpVOXImgs3YeEwlHS6eNa5mYdvud%2FLOA%2FR1nuZaxvbLdAG9qO5u5n%2FgzSNYFzyYxatWic%2BPI1vAAMrGIYEEkHt3JZJBfP5TomXAxkLmEMh8f5UDhpLA46cw5eB7qWM9yUpIe0LfnqGJH9T9Wp18Sz15buNJQEXMx5UWzzOzXB8J6uRImrsxVFFDsw1EzBkvFQ4In3G%2B%2FAutr4WxojRdYlaX2jzAohbb7GZWFcn4Kt%2BG%2FNnZriC%2FnNEzxiENRsY54bWpBNO4j3X%2BWrWeK0ynU01AIk7M%2FPPr%2Fd8mgh0yIMn0tA3vP7C2%2FmqJq%2FBUw79TDyQY6pgErLMlWNMa2ARo2jXYN%2Fc%2BieZqqBgpeh7OfHTIrFOq6YFCbGI3unuzgMMDoO9XR%2FTdWGrFfl%2BlDEhZrdpT9Ae8U2bpTjnKTal4Cyo500Pdv0yi22iVS1Ge0C4f4YpnjjummbqsLJaS7RbkpwOzglj0BJSFmEzrTbFRtirNXQC6p3AVcpAfceLjd0qtk0n%2BmpvcXmcugVnzPkBYK6ga0p687hgIYztrF&X-Amz-Signature=1854f7a27e8f43adc938148d67f217ecc3114d8a454f0aac6611c4f83d2842fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TITXHTJI%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIDzEP%2FPFKPC1uhzc69rFYMEYxBt81VQ6Rcq6lqZ1VF7HAiB7wjOYI7rU4yao91h1QLR%2FJzrKuUJrlDdiop8xIz5wZyr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMmICSSdvpgA7aV29rKtwD5q4j9LcaeJQHnRhcCFjZ6HfwSmx4Z4D0e%2FQHcOxIYCiSpBXC%2BcVdIqFK2jm6C7PgXMksEPrnyCLf9PY7S%2B%2FpTgb29apMbeo0in8XS3QORoK9cu6hXY8zhw7A7JxdtRg3wZyILLjj4IMM2lV%2FFSQ2p2w2HhO%2B2w13ToWLV2uOVQxPwucVGSTuJm8ooFYbbH9G4v9MAx0VeFv9ew0DOcLscQ%2BNr9%2B7QRigSiME4b8JzArXCI53xEh6z4Ic3RgK26itkZ4SE%2BxwxRng10WNnc1SIwe0kEsJtU3G4iygVmd2hZsHRzR18pgqBdvypit%2Fs8W1cpVOXImgs3YeEwlHS6eNa5mYdvud%2FLOA%2FR1nuZaxvbLdAG9qO5u5n%2FgzSNYFzyYxatWic%2BPI1vAAMrGIYEEkHt3JZJBfP5TomXAxkLmEMh8f5UDhpLA46cw5eB7qWM9yUpIe0LfnqGJH9T9Wp18Sz15buNJQEXMx5UWzzOzXB8J6uRImrsxVFFDsw1EzBkvFQ4In3G%2B%2FAutr4WxojRdYlaX2jzAohbb7GZWFcn4Kt%2BG%2FNnZriC%2FnNEzxiENRsY54bWpBNO4j3X%2BWrWeK0ynU01AIk7M%2FPPr%2Fd8mgh0yIMn0tA3vP7C2%2FmqJq%2FBUw79TDyQY6pgErLMlWNMa2ARo2jXYN%2Fc%2BieZqqBgpeh7OfHTIrFOq6YFCbGI3unuzgMMDoO9XR%2FTdWGrFfl%2BlDEhZrdpT9Ae8U2bpTjnKTal4Cyo500Pdv0yi22iVS1Ge0C4f4YpnjjummbqsLJaS7RbkpwOzglj0BJSFmEzrTbFRtirNXQC6p3AVcpAfceLjd0qtk0n%2BmpvcXmcugVnzPkBYK6ga0p687hgIYztrF&X-Amz-Signature=c76ef726de7235f164bcae5311c1e44645e99b191cec969cb0edd87a38812550&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

