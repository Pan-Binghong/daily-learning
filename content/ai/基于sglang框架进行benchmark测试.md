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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F6WIIVB%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxQo%2BLM3cqXhkedfixct9yOsUYe2qaeXfQ41lm0%2FLIKgIhAIAPHJ42r59YloR%2BrkazuTlXxFe%2BP44HO5wRuTC2SjeaKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwoauliBivS6Ws77Vsq3AOk1ktW4pwGVr2fBB4EABi0kOQP57AZqhZHFwudkyG%2FngCtCdyonX8TORv2S9XLBiGNwuQjI1RWGLRc7j5hOVHLiM%2BQB8dDCtrN6LVCGzKJIwrI9Jz7VXRAOAX343uWpYHaagd2VLkXm2QcBFNerPM1RCd%2BULX9eheMzW0OO8rzWhPLStOdqy%2FsbNOvxEk7m3fH1HGLXR6PcorV6wMFdPBMlq42%2FhMFv%2BMw5ulmfVTWK5Sas9UGxZ1hqHcjwH1rl0XTUlZZ2nD8LlGAtOmaTqhrVfs%2Fv2UEt8Hvn5JohYCAT%2FuwYduupL76ZrdclBnRcPhEVJDLNwRBJqw3Yk6S0u%2FrrjvjL98JCj5%2FVJ98vllomtno77NAhrC%2BbbJ%2BD1VQEcuUYTGPlTL6Mk5otMvXBugj5lVz3n5s7laEj0WZJBEOPNW9yKa7bm1xIju49RdqeqeksvBwJd9C6zYqCULThjFTCJ6zKQgY7ocp9U6F8GxZuSoE0jsaZCS9S4CDcw3Fk5VJBN%2B20Mvq5Fv5Jty5zOeNn5EB%2FzyiMl4Qnu%2BKmtwKaOzlNKiyIKxVw%2BJPjoTIHKnQq0IgesUx9yY1FbbKZuIcsNLp0xu2P4OGrnvdpW1mIeYxxT04hx2JhrhkrjDGpY3OBjqkAQpAyTfIKxtJrXMbMxZn0peki%2FITIQlw%2FBPXHLzqJ7TR3A9iMLaypv%2F2JjaGuGjsTn9tnvXArfEkrYDl1Gqoktf2QbCy7W5rry3THFOjW2BKpVLDdPdV3JgxOLnGwbZs7AlZhlxXxdYFeRttAX6fLRteHdSxwAvhn7Vf6gwJaW%2FjImtLjWzfTr6rGgvHOcXuQOylf0zCDd2pXDI9ExLWET1aHQyF&X-Amz-Signature=07d289d01fa4974b5a7d944286e302f3aa382aebed6aa58b60f3a83d4a06b5ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F6WIIVB%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxQo%2BLM3cqXhkedfixct9yOsUYe2qaeXfQ41lm0%2FLIKgIhAIAPHJ42r59YloR%2BrkazuTlXxFe%2BP44HO5wRuTC2SjeaKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwoauliBivS6Ws77Vsq3AOk1ktW4pwGVr2fBB4EABi0kOQP57AZqhZHFwudkyG%2FngCtCdyonX8TORv2S9XLBiGNwuQjI1RWGLRc7j5hOVHLiM%2BQB8dDCtrN6LVCGzKJIwrI9Jz7VXRAOAX343uWpYHaagd2VLkXm2QcBFNerPM1RCd%2BULX9eheMzW0OO8rzWhPLStOdqy%2FsbNOvxEk7m3fH1HGLXR6PcorV6wMFdPBMlq42%2FhMFv%2BMw5ulmfVTWK5Sas9UGxZ1hqHcjwH1rl0XTUlZZ2nD8LlGAtOmaTqhrVfs%2Fv2UEt8Hvn5JohYCAT%2FuwYduupL76ZrdclBnRcPhEVJDLNwRBJqw3Yk6S0u%2FrrjvjL98JCj5%2FVJ98vllomtno77NAhrC%2BbbJ%2BD1VQEcuUYTGPlTL6Mk5otMvXBugj5lVz3n5s7laEj0WZJBEOPNW9yKa7bm1xIju49RdqeqeksvBwJd9C6zYqCULThjFTCJ6zKQgY7ocp9U6F8GxZuSoE0jsaZCS9S4CDcw3Fk5VJBN%2B20Mvq5Fv5Jty5zOeNn5EB%2FzyiMl4Qnu%2BKmtwKaOzlNKiyIKxVw%2BJPjoTIHKnQq0IgesUx9yY1FbbKZuIcsNLp0xu2P4OGrnvdpW1mIeYxxT04hx2JhrhkrjDGpY3OBjqkAQpAyTfIKxtJrXMbMxZn0peki%2FITIQlw%2FBPXHLzqJ7TR3A9iMLaypv%2F2JjaGuGjsTn9tnvXArfEkrYDl1Gqoktf2QbCy7W5rry3THFOjW2BKpVLDdPdV3JgxOLnGwbZs7AlZhlxXxdYFeRttAX6fLRteHdSxwAvhn7Vf6gwJaW%2FjImtLjWzfTr6rGgvHOcXuQOylf0zCDd2pXDI9ExLWET1aHQyF&X-Amz-Signature=434adcf82f68c0dca486aa7733be8cd2b8f53e4fffa3bf3181ebbb6adbf7f6e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

