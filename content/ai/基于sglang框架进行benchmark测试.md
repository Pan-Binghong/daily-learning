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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDZJL52J%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIFa9DiPsDGPUKqQAkzNa8SGFEhZI1mkLMWN4j3sU7tluAiAYaphDfxH9LOQB%2FaHohf8LQK5uxyq6bXTruKYd3%2FM%2BeCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMc7GJGN9JWB2Ev%2FUFKtwD4GjYX2mhCle9eJCW7RfwF2CPt8ZPOVS2yRo9x2SGIOyrRP%2BtSTVpaslTJO2zepiCqMhlUMCUXgZWmbL%2FKH9e%2BP3opi70orWe9XN2xlyz2g9kCI1oLHGSrF5gRwHvXH3HwDhSHk8ewMN88D3IlXLsU2c6riIMmJajCuTmTEdoPy0lgSXf1Lks6fHyuGXTxORMn7ChmNoDWJoO8aZDFjmydGDeAoGHLz27jDxg1R%2BpE%2BI%2BnBBnPcaRvtSY0j3bbQgdkctzlXP3Kb0%2BVQ8qIxwG333BgsIxGLkWU8pQrQI6qEe626urNf8N9NfI1QW3xvPzGL84y%2BHuKBFWZh8w%2FxS1tW1DxfWdL%2F0tuNeo4cs2tN42Cy2U6DgChGpQERnz3XTbd4e2%2FfNhTCBl5zm2F0rzFOExd2odv6%2Fxo2y1FgH2Ak0l%2FFKnRLUCRky3r%2B05%2BTm62j%2FvxtJ1edq%2Bt0w%2BJ5C%2BSws3hCFhQJvDJpxAvl1juDZYoNBQXuM5BYPLGKoXMwIwItAK0omUXp9eyV4%2Fp%2BiediBWRLUZoaHLNjJ%2BZrrDC2G12Gdqu2vsBSuXHjNS%2BLY43EH56zrh%2FSoxtdTH3nNbX%2FnITRV29%2BVt6MQbAq3fmg8xJFW7aMLx5274Bfsw4JuhywY6pgFg7jP4qatw8XjLbsnrVBHwrCeGJh7jxGp%2FQowklVXIZXwzbv690JGx%2Bgc0%2FwSBkK1dmPEl9KF8L8BaufMba0HkVRrDxR8pNwDU9PuGn%2BX%2F0a67ACMgFN5EzzwHXKeEuf7nVfNDCySCzPFR%2FoafZfx%2ByTw7AByzl39MinBlPS4s8h3Pw8K0Dk3LAciTuKTbiB%2FS4r4DKsHDQBMfpn6hzWBFSm3a6UT2&X-Amz-Signature=df0113b40589f8b785d8edafa5cdbf939b55851c218fefd17b801658b16c8031&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDZJL52J%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIFa9DiPsDGPUKqQAkzNa8SGFEhZI1mkLMWN4j3sU7tluAiAYaphDfxH9LOQB%2FaHohf8LQK5uxyq6bXTruKYd3%2FM%2BeCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMc7GJGN9JWB2Ev%2FUFKtwD4GjYX2mhCle9eJCW7RfwF2CPt8ZPOVS2yRo9x2SGIOyrRP%2BtSTVpaslTJO2zepiCqMhlUMCUXgZWmbL%2FKH9e%2BP3opi70orWe9XN2xlyz2g9kCI1oLHGSrF5gRwHvXH3HwDhSHk8ewMN88D3IlXLsU2c6riIMmJajCuTmTEdoPy0lgSXf1Lks6fHyuGXTxORMn7ChmNoDWJoO8aZDFjmydGDeAoGHLz27jDxg1R%2BpE%2BI%2BnBBnPcaRvtSY0j3bbQgdkctzlXP3Kb0%2BVQ8qIxwG333BgsIxGLkWU8pQrQI6qEe626urNf8N9NfI1QW3xvPzGL84y%2BHuKBFWZh8w%2FxS1tW1DxfWdL%2F0tuNeo4cs2tN42Cy2U6DgChGpQERnz3XTbd4e2%2FfNhTCBl5zm2F0rzFOExd2odv6%2Fxo2y1FgH2Ak0l%2FFKnRLUCRky3r%2B05%2BTm62j%2FvxtJ1edq%2Bt0w%2BJ5C%2BSws3hCFhQJvDJpxAvl1juDZYoNBQXuM5BYPLGKoXMwIwItAK0omUXp9eyV4%2Fp%2BiediBWRLUZoaHLNjJ%2BZrrDC2G12Gdqu2vsBSuXHjNS%2BLY43EH56zrh%2FSoxtdTH3nNbX%2FnITRV29%2BVt6MQbAq3fmg8xJFW7aMLx5274Bfsw4JuhywY6pgFg7jP4qatw8XjLbsnrVBHwrCeGJh7jxGp%2FQowklVXIZXwzbv690JGx%2Bgc0%2FwSBkK1dmPEl9KF8L8BaufMba0HkVRrDxR8pNwDU9PuGn%2BX%2F0a67ACMgFN5EzzwHXKeEuf7nVfNDCySCzPFR%2FoafZfx%2ByTw7AByzl39MinBlPS4s8h3Pw8K0Dk3LAciTuKTbiB%2FS4r4DKsHDQBMfpn6hzWBFSm3a6UT2&X-Amz-Signature=a3603e48b7a059cca2d41835ed18001c05835b40e7975a4d22b60ce25721c900&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

