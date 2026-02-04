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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DL66Q5V%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQC9jg5o1R6PEgK3FmPj131co3WB5K73suaOCLG%2B1EvKFAIgU5S0htvI4TsAXPBascXd50xhoEMpgeI4dC4brAnwVhkq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDL0GVoWPtylYRUg1KircA2kEjbM59mCxmu4nXwT7Fk2zh%2B414hLf2tWR1nsKiCleTqEo%2B6WJLRUckeu%2F54MboL3vIlad8J4D5yooqWqyfP8OvCJzKfUlhXcD4AcKyFv0Q7v6vDWBebb%2FYXVNaZy7JUz5yA1lRhcNk8NhIrMCrWkMfOGnnXMAumKAESCexDAYgYhgO1taxvSmdBgnMhbUtPMQIkVO%2BllgZtGI0eeM21lLQnSB7YKZCvzj5Ww1CWr%2B%2BZ%2F%2Bi8E7EOOnVjwki5owE9TLv9HeF7buxmM04yq8CvzW%2Fl6o9AgFv3rrItQb5zgr0mTZ9O4OX655bLcLamA5TpRnvJlq%2BTp9BqtXL%2FpI9P5hELRxtQdhd9aKoGMIG2ezgr%2B6H%2B8SxF0fjakd0136tlkjHzOYWCqFPEyr%2Bjoa9GxD0silqiyo8K3naOHPL%2FEqdXQUKZTMeH3jTHtVlKghstdwSvJJO6Fw5SZBz2f1EpRBr8gOJF2FXQ%2FygVvUMskL6Mr0ziCFbm3BQJDqbt6jjrr7Qj4TMKkwEoWqYCRJaLv8tOeYpjALcJMtCBRN6xHfFswy%2BdcwSgz%2FZu%2Fph4tsXIVoUCr3w3SnUYtZqrbO3%2FmrCNCs2urcqyfhEDPC5AaA93Z4I7EVkWf1U7e%2BMJLpiswGOqUBQspzu7L2xcF4fPWTrNu%2FQ47bCEYilPpTtOViAI4ShUk7sfK4G0RID6hjk0SOciynASy4oEbiHEo0Me%2FZfH7iKYWvUl8A2SIgw%2FUvRN%2F1fM5PtoW7zJ%2BawAayGUdyuB832k9wYusHDLezgNCl15PKPTcFNbMyK6RkqkkFqGSxl%2BMpbhpNXH2qghV6mR7sSNvQmsb%2F63aNOUGClW%2FobEk4%2FIg78ci9&X-Amz-Signature=82e551010d50bb922a92cd4d3189f3e6787e85087adcdb774a00c185d0f3de73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DL66Q5V%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQC9jg5o1R6PEgK3FmPj131co3WB5K73suaOCLG%2B1EvKFAIgU5S0htvI4TsAXPBascXd50xhoEMpgeI4dC4brAnwVhkq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDL0GVoWPtylYRUg1KircA2kEjbM59mCxmu4nXwT7Fk2zh%2B414hLf2tWR1nsKiCleTqEo%2B6WJLRUckeu%2F54MboL3vIlad8J4D5yooqWqyfP8OvCJzKfUlhXcD4AcKyFv0Q7v6vDWBebb%2FYXVNaZy7JUz5yA1lRhcNk8NhIrMCrWkMfOGnnXMAumKAESCexDAYgYhgO1taxvSmdBgnMhbUtPMQIkVO%2BllgZtGI0eeM21lLQnSB7YKZCvzj5Ww1CWr%2B%2BZ%2F%2Bi8E7EOOnVjwki5owE9TLv9HeF7buxmM04yq8CvzW%2Fl6o9AgFv3rrItQb5zgr0mTZ9O4OX655bLcLamA5TpRnvJlq%2BTp9BqtXL%2FpI9P5hELRxtQdhd9aKoGMIG2ezgr%2B6H%2B8SxF0fjakd0136tlkjHzOYWCqFPEyr%2Bjoa9GxD0silqiyo8K3naOHPL%2FEqdXQUKZTMeH3jTHtVlKghstdwSvJJO6Fw5SZBz2f1EpRBr8gOJF2FXQ%2FygVvUMskL6Mr0ziCFbm3BQJDqbt6jjrr7Qj4TMKkwEoWqYCRJaLv8tOeYpjALcJMtCBRN6xHfFswy%2BdcwSgz%2FZu%2Fph4tsXIVoUCr3w3SnUYtZqrbO3%2FmrCNCs2urcqyfhEDPC5AaA93Z4I7EVkWf1U7e%2BMJLpiswGOqUBQspzu7L2xcF4fPWTrNu%2FQ47bCEYilPpTtOViAI4ShUk7sfK4G0RID6hjk0SOciynASy4oEbiHEo0Me%2FZfH7iKYWvUl8A2SIgw%2FUvRN%2F1fM5PtoW7zJ%2BawAayGUdyuB832k9wYusHDLezgNCl15PKPTcFNbMyK6RkqkkFqGSxl%2BMpbhpNXH2qghV6mR7sSNvQmsb%2F63aNOUGClW%2FobEk4%2FIg78ci9&X-Amz-Signature=c46c740324d79fc8654d3f168dbb8f5d9adbd963923591c3f4a3f56d39cdc7f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

