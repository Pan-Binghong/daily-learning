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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVHXVYKN%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQUI3Bs0RH29HdrXEXeE%2FcOUtdgbStbWKqXAasARE5ogIgIwtRCg3eL2IlD5LM7yY6gF9aV9Lm23clmbREVSK44Akq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDBvGGM101QPdUrk4jyrcA3KFUmlVwLG1qon%2FMEqd6O5wW4bQeG8r12fK6VBlnJT7bNya2b8sae6JxKfRVRsp4S0ELsVJVJJoPD1GlD2H9t%2BcSKam9OYXdOZIOMg7a%2BOaADVZqYHSjGWpzvqeT6cx%2FPyst3MmMH9%2BXRBlGL6m8pk4YG3tZ1FO6dTHzpVqU2gvJJ4YFbKRX9VqIhCHxmrlgb497bIJz5iM4jAinaa1h%2F9cwW1CDzSNI6%2FlsKt5JJiTx0qiOaXq2Y9oHMegWw1LSaIwxVYHd0o7MKPzRArwYsmZvBZcROlJ7frpcGfXsdvqjl3Bj5q2RPLP60xSZmbbTKumPq8CekZlmdWWJ1cYBSkK6xtP%2BjWjoW8NmiAMTlTHpZAlpk%2BA1NPb6HM3a855GVX1FfS3laSQQMrx4ZkZpy2c5Ma2qI2PTAW9VV1tKnkoHPuRrTI320NNcA2nhKdHhsW183CHVQDtlRiPdYFSnCvoBgzXBXu646tjGONZbCJT9yNvGsVuVB1fNApCPolvRx070UQFz7ByA%2B7hvEajUqQUQ3%2FQ2ht0UerAcS6N1TtKZ7naz1isKmOv2aTAf6ENX5MkVHVh3s%2FRiKfwhIzM5stJho0vjQ8P%2BLgjyddAk4asQgWZFHb4I0pEV2uNMKHOjs0GOqUBR%2BrhZbxQAeAZ1qVuiCInjV0%2B6FtGRI%2BxPWb6QHZByFH6cANpZxdYLy2%2FcO8g9QNfdL%2Fom9Th6IvwF%2BNqRU27KD61tY07T7RJr4O4junGzJPfxP0gsA0GfUFxKFM%2FKOVTtwjU59nJqi3bu5DlHXbmIEtxyp0vtguMjOzNpOlzLmV%2F95sBbbQ6hBQ%2BamOGNZd2Nkojxr4LYcYh8jI2iT6iyTO%2FDB7f&X-Amz-Signature=593c3305e4c448fb3e0260779dd26858d3d77a66f930549d917cacafb8f9785c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVHXVYKN%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQUI3Bs0RH29HdrXEXeE%2FcOUtdgbStbWKqXAasARE5ogIgIwtRCg3eL2IlD5LM7yY6gF9aV9Lm23clmbREVSK44Akq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDBvGGM101QPdUrk4jyrcA3KFUmlVwLG1qon%2FMEqd6O5wW4bQeG8r12fK6VBlnJT7bNya2b8sae6JxKfRVRsp4S0ELsVJVJJoPD1GlD2H9t%2BcSKam9OYXdOZIOMg7a%2BOaADVZqYHSjGWpzvqeT6cx%2FPyst3MmMH9%2BXRBlGL6m8pk4YG3tZ1FO6dTHzpVqU2gvJJ4YFbKRX9VqIhCHxmrlgb497bIJz5iM4jAinaa1h%2F9cwW1CDzSNI6%2FlsKt5JJiTx0qiOaXq2Y9oHMegWw1LSaIwxVYHd0o7MKPzRArwYsmZvBZcROlJ7frpcGfXsdvqjl3Bj5q2RPLP60xSZmbbTKumPq8CekZlmdWWJ1cYBSkK6xtP%2BjWjoW8NmiAMTlTHpZAlpk%2BA1NPb6HM3a855GVX1FfS3laSQQMrx4ZkZpy2c5Ma2qI2PTAW9VV1tKnkoHPuRrTI320NNcA2nhKdHhsW183CHVQDtlRiPdYFSnCvoBgzXBXu646tjGONZbCJT9yNvGsVuVB1fNApCPolvRx070UQFz7ByA%2B7hvEajUqQUQ3%2FQ2ht0UerAcS6N1TtKZ7naz1isKmOv2aTAf6ENX5MkVHVh3s%2FRiKfwhIzM5stJho0vjQ8P%2BLgjyddAk4asQgWZFHb4I0pEV2uNMKHOjs0GOqUBR%2BrhZbxQAeAZ1qVuiCInjV0%2B6FtGRI%2BxPWb6QHZByFH6cANpZxdYLy2%2FcO8g9QNfdL%2Fom9Th6IvwF%2BNqRU27KD61tY07T7RJr4O4junGzJPfxP0gsA0GfUFxKFM%2FKOVTtwjU59nJqi3bu5DlHXbmIEtxyp0vtguMjOzNpOlzLmV%2F95sBbbQ6hBQ%2BamOGNZd2Nkojxr4LYcYh8jI2iT6iyTO%2FDB7f&X-Amz-Signature=8a531d93a506ccb39716e9d488817b375c7fb218de1bca879d68d0eacff567e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

