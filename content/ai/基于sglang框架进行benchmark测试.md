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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3LJ6UMZ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIA2CLjs9hi70VJ0zN8DUODJPeLrktA8HDic1cfmgi7UaAiEA9Ees3TQEVQ2fUlQwWCufpzrc2jM0EJsXXKodKz3o7oQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCnerUJWAIC5gS4%2F5yrcA4blMcJLBoq5ZeBVPmFaQRKFO7QRCHsH7knt9LWzMwrkHM4v2Y0aqAPEb9%2FO34bqUTnbBGWAdfF5V2tTfm3VzqK%2Bb9ULBR%2F2VMdPoFDoLeezUPuMrHNS8oy8Yv2Oc%2FXLovKBRuK91o4PxIKMzgqy3KCwPgTbZXwJCVYnV%2BdIoOV9DDwnnh4h46clP0g06Jud5uFPJYx2w2SDYgG9VtvHDX5%2BgUNIy0FjllqSkbroRyB1KNQ1d%2BA5oFxwD%2FiZwF1PjCtT3uhC32KYIe%2F9WlBsIZTuEepAjuX1XZ1RXHjLx%2BJYp2wGbClGILKGBSRRKOzMOjnCLL6R33g9EClo0kTDWGmxIYNq8ld8wjAtjqM2lH5F3fzqHIc0y6DiKjHQXZCLlReWNO5krUXt8DUdOw0Cp4xAUEEXkjPft65MRiShFyYWQWruOlFTQktoIkenVOdn1uqO8SjjBMuEpxz8Yv0Hq9fXoEdHZYGfDcvCU1l%2BvHjScZJx1AarTCi0Requ8Hq60vderw2SsX%2BDqOHr%2BBPCHqwmoYp7QfSUIdD4u1ZKEyYEL2cQI%2Bj%2Fyafs7bE3whAGQKRMo0ULoURaJ3cSgr9zpKUbeEoTovEc6x7kHQmqRm0fpScHrbYDxV%2FY6nXtMOeczM8GOqUBUy87StE4kRGdyKpImLrjjpffbQ7vPzvPvIw3dK8WUWLKCxD0geeBrHgi7kh4DTxACPbr35ryZY65m5QE9s18te1S0aIily4DNf2hsL76j2v7e2s1YGQ5jniAtCyqzk0X8UieoJwNvKFY1gMIs4uE0XXHVfqLyZZR1bWTQ4jqeWPJG%2F3VrtTUxPkRsGnFInYS06QLU4dWS2xncsHMIbaTBtX3a6%2BN&X-Amz-Signature=0e3cd38f7488979e700c90d95fb80169d24193bd3868722196590deae3293e1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3LJ6UMZ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIA2CLjs9hi70VJ0zN8DUODJPeLrktA8HDic1cfmgi7UaAiEA9Ees3TQEVQ2fUlQwWCufpzrc2jM0EJsXXKodKz3o7oQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCnerUJWAIC5gS4%2F5yrcA4blMcJLBoq5ZeBVPmFaQRKFO7QRCHsH7knt9LWzMwrkHM4v2Y0aqAPEb9%2FO34bqUTnbBGWAdfF5V2tTfm3VzqK%2Bb9ULBR%2F2VMdPoFDoLeezUPuMrHNS8oy8Yv2Oc%2FXLovKBRuK91o4PxIKMzgqy3KCwPgTbZXwJCVYnV%2BdIoOV9DDwnnh4h46clP0g06Jud5uFPJYx2w2SDYgG9VtvHDX5%2BgUNIy0FjllqSkbroRyB1KNQ1d%2BA5oFxwD%2FiZwF1PjCtT3uhC32KYIe%2F9WlBsIZTuEepAjuX1XZ1RXHjLx%2BJYp2wGbClGILKGBSRRKOzMOjnCLL6R33g9EClo0kTDWGmxIYNq8ld8wjAtjqM2lH5F3fzqHIc0y6DiKjHQXZCLlReWNO5krUXt8DUdOw0Cp4xAUEEXkjPft65MRiShFyYWQWruOlFTQktoIkenVOdn1uqO8SjjBMuEpxz8Yv0Hq9fXoEdHZYGfDcvCU1l%2BvHjScZJx1AarTCi0Requ8Hq60vderw2SsX%2BDqOHr%2BBPCHqwmoYp7QfSUIdD4u1ZKEyYEL2cQI%2Bj%2Fyafs7bE3whAGQKRMo0ULoURaJ3cSgr9zpKUbeEoTovEc6x7kHQmqRm0fpScHrbYDxV%2FY6nXtMOeczM8GOqUBUy87StE4kRGdyKpImLrjjpffbQ7vPzvPvIw3dK8WUWLKCxD0geeBrHgi7kh4DTxACPbr35ryZY65m5QE9s18te1S0aIily4DNf2hsL76j2v7e2s1YGQ5jniAtCyqzk0X8UieoJwNvKFY1gMIs4uE0XXHVfqLyZZR1bWTQ4jqeWPJG%2F3VrtTUxPkRsGnFInYS06QLU4dWS2xncsHMIbaTBtX3a6%2BN&X-Amz-Signature=c38733d83be59829c31fbd369ee8cbd18e16fe708cfcb8cf9aed518f18fb843f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

