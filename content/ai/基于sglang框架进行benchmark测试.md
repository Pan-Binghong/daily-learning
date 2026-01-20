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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOHDQ6S6%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDu5tnSuvRofTXIn8ig2eHBshGKHSmlBsuULbZrA%2Ff%2FWAiEA1qlgz%2BePlIXZcQwfLqT8gWJ3n7Ok8cWUeKdxp0yZ2RIqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOB%2BNC9XGGk1v9rTMCrcAx2YxdPNll4NYqokZOIa5Sm8VC6O5Yw%2B5hCA%2F%2BuOtqyvNPdchexTjSLojinfV8eO4bDFKJ%2BhzjPJOlLU4oHf77MRMp2H0qLaUtmL%2BncZljwYJ04fgAGOYI5Qb7rPy9SAX1j%2F4H7Vzjq21%2Bz%2FL5ZWUmIKfy%2F3%2BxId0rFpps3qWJz4aNTGeSkac3SQnE5MQN79tA52MCTdd0%2BryGcwApDYx3tdxofIByK1CZ8o42QRPw7H696SEW%2BoOQylnvEDplSMMUcXOSZUYs4AJWySmsiTFLxSgaeXlctdkiaC9DmURAEHqNkl6K3hmEgW8jDS7ZSuTcWMhx0QsgSlRNixJUebjpDeDeAOrlypprRhAULo0rnBR%2BqXa8H6dgkB8sJPqFBSOsg9BkpS5ktLAcwaaHugzMcTrvXCT4mSurhIcTxbCd8zpLXXDEm3XzGdL4jfucpa%2FFE6ZwFYMIs5yQByC5k5xd%2B7twgyi2OuRwkeKnoJAKazqhtpo0RanAMhM72p5cUtCrwzsF8KUQeSSc3ogcRo6PJdzWn0SwqpBNeRvlDahTs2Bkl%2B35o2oE3hmns0i0HKbfJo89X09SzYv5ypxy%2BA2ILv6kNkaCV0beMGSatCQLr4TtKTSbSGviBlKLdrMKv1ussGOqUBQa4K9nKAswkBppCuxhpUTTcWPWBjNZWKoGdL33HLcLp9adlgg7yKT18UR8sSm4eK%2FlFeWFrf5EMhynCGNag3rYgfGJyTw7zZGQz9asUeS9UB%2Bro%2FS8BdaCkJscXeVloM95g6rfjGP1tKsydebQt3WXmXL9tYdsLjQKJ9%2BpW%2Fl0ZsGKl7zTBKw9XwFdxtcXZ7F4woPrTYOxXyUUcf3y8PCDu2alWd&X-Amz-Signature=03a9466fabd8195a2a51e49350ba8a11b62d15dbac66a292b32cf532c75e84fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOHDQ6S6%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDu5tnSuvRofTXIn8ig2eHBshGKHSmlBsuULbZrA%2Ff%2FWAiEA1qlgz%2BePlIXZcQwfLqT8gWJ3n7Ok8cWUeKdxp0yZ2RIqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOB%2BNC9XGGk1v9rTMCrcAx2YxdPNll4NYqokZOIa5Sm8VC6O5Yw%2B5hCA%2F%2BuOtqyvNPdchexTjSLojinfV8eO4bDFKJ%2BhzjPJOlLU4oHf77MRMp2H0qLaUtmL%2BncZljwYJ04fgAGOYI5Qb7rPy9SAX1j%2F4H7Vzjq21%2Bz%2FL5ZWUmIKfy%2F3%2BxId0rFpps3qWJz4aNTGeSkac3SQnE5MQN79tA52MCTdd0%2BryGcwApDYx3tdxofIByK1CZ8o42QRPw7H696SEW%2BoOQylnvEDplSMMUcXOSZUYs4AJWySmsiTFLxSgaeXlctdkiaC9DmURAEHqNkl6K3hmEgW8jDS7ZSuTcWMhx0QsgSlRNixJUebjpDeDeAOrlypprRhAULo0rnBR%2BqXa8H6dgkB8sJPqFBSOsg9BkpS5ktLAcwaaHugzMcTrvXCT4mSurhIcTxbCd8zpLXXDEm3XzGdL4jfucpa%2FFE6ZwFYMIs5yQByC5k5xd%2B7twgyi2OuRwkeKnoJAKazqhtpo0RanAMhM72p5cUtCrwzsF8KUQeSSc3ogcRo6PJdzWn0SwqpBNeRvlDahTs2Bkl%2B35o2oE3hmns0i0HKbfJo89X09SzYv5ypxy%2BA2ILv6kNkaCV0beMGSatCQLr4TtKTSbSGviBlKLdrMKv1ussGOqUBQa4K9nKAswkBppCuxhpUTTcWPWBjNZWKoGdL33HLcLp9adlgg7yKT18UR8sSm4eK%2FlFeWFrf5EMhynCGNag3rYgfGJyTw7zZGQz9asUeS9UB%2Bro%2FS8BdaCkJscXeVloM95g6rfjGP1tKsydebQt3WXmXL9tYdsLjQKJ9%2BpW%2Fl0ZsGKl7zTBKw9XwFdxtcXZ7F4woPrTYOxXyUUcf3y8PCDu2alWd&X-Amz-Signature=10a22d4b92a3a6654220ce4a9412e9fde0fe01d524119f30bca595c6dc88a840&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

