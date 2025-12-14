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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676O7ZYGP%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCLRmbZRp20R%2BK6Rxv7tpoX2le%2FxIR%2Bx4U58YACbOBZawIgXO%2FtMCBn2GEBZDRHz9WtpkvYi35R2nOGdugYKHr76qwq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDNFSkdnZW8S2Aq1NzCrcAwNYCXUpxV0DeHZ05CaFzR%2FGgIbOKMCZWbq01nzwGc9bh5j7K6whsgqxgJmUsXat%2FAA1UxvR6FuNQbk04krORl1DxSB%2FWfIeezbTSUVug4G6mpI3FthQcvCqx8v93%2FhCMbmD%2BFljWdQYtqlmvPmVCQuIkifoin34sCDb1UmVH2NbuO3hedfUR%2FxyO0x2cQRE85tsDdL9dHH%2FS6UwtcE9haMdhoHE1TihXP0y3S3RTME%2B9%2FbiS0e4Lu8pENG%2F9UOdSr5d7QZY3302ExCRlIgPOqvpkhLmnMeZrpebLW2KY4Z4kzxTKq7ok89WOk4DOFlC0vJtT4MzjWogYCPZgB8zkD0n1pxuv5CAucXtbUTs1n2rRzMvMxLyyu6U3csGPBnBUb68orq7iHwvwQlhU1Jxv8iKemvsbu78B2COs7g90T62%2BajJ%2B0rX9JVHIjNHti7lAIT3xWbXwEWp3OaOK8j00RlaHagsR%2BAcwgyG6YQ7HEuLp6o2h3Jkac%2BIsLXBz5dKUagtMR19zZqqZ88Fjyf2Iz%2BY2s1T32k75CjAmGRnk7IdZDe62laXlL4p5b2PqyFQX0abE2JxpTXOYdLruLhnGiXT4HJe9Pbtldo0tn2u805U115Bywneis3jIIFXMNWv%2BMkGOqUBQKkDRa%2Fz8t%2FV6%2BAsiOyYEfUOJHYr19UXMHM%2BSsha%2BEzL0Q6k5qO44cnTe5xmr5c%2Fr3LgCzRWNLjJSD%2FblKuNt%2BQN4laRjnxxrZUaLcNQ8vU3VN7g7NzhOu5eUGoLOU0SpcqbJdKW7Jbuk3l67GkWr%2FFCMOifEBgQWf3dR7gH5ccOP1Of5QLK135jZtFXFKbJU9C0qsbgqf0fj1oMXVBn9vEnJzDU&X-Amz-Signature=9d5df02ac103fce3070c087dc3d782c976fc5ffc4e5c865195afe4bcebf28802&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676O7ZYGP%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCLRmbZRp20R%2BK6Rxv7tpoX2le%2FxIR%2Bx4U58YACbOBZawIgXO%2FtMCBn2GEBZDRHz9WtpkvYi35R2nOGdugYKHr76qwq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDNFSkdnZW8S2Aq1NzCrcAwNYCXUpxV0DeHZ05CaFzR%2FGgIbOKMCZWbq01nzwGc9bh5j7K6whsgqxgJmUsXat%2FAA1UxvR6FuNQbk04krORl1DxSB%2FWfIeezbTSUVug4G6mpI3FthQcvCqx8v93%2FhCMbmD%2BFljWdQYtqlmvPmVCQuIkifoin34sCDb1UmVH2NbuO3hedfUR%2FxyO0x2cQRE85tsDdL9dHH%2FS6UwtcE9haMdhoHE1TihXP0y3S3RTME%2B9%2FbiS0e4Lu8pENG%2F9UOdSr5d7QZY3302ExCRlIgPOqvpkhLmnMeZrpebLW2KY4Z4kzxTKq7ok89WOk4DOFlC0vJtT4MzjWogYCPZgB8zkD0n1pxuv5CAucXtbUTs1n2rRzMvMxLyyu6U3csGPBnBUb68orq7iHwvwQlhU1Jxv8iKemvsbu78B2COs7g90T62%2BajJ%2B0rX9JVHIjNHti7lAIT3xWbXwEWp3OaOK8j00RlaHagsR%2BAcwgyG6YQ7HEuLp6o2h3Jkac%2BIsLXBz5dKUagtMR19zZqqZ88Fjyf2Iz%2BY2s1T32k75CjAmGRnk7IdZDe62laXlL4p5b2PqyFQX0abE2JxpTXOYdLruLhnGiXT4HJe9Pbtldo0tn2u805U115Bywneis3jIIFXMNWv%2BMkGOqUBQKkDRa%2Fz8t%2FV6%2BAsiOyYEfUOJHYr19UXMHM%2BSsha%2BEzL0Q6k5qO44cnTe5xmr5c%2Fr3LgCzRWNLjJSD%2FblKuNt%2BQN4laRjnxxrZUaLcNQ8vU3VN7g7NzhOu5eUGoLOU0SpcqbJdKW7Jbuk3l67GkWr%2FFCMOifEBgQWf3dR7gH5ccOP1Of5QLK135jZtFXFKbJU9C0qsbgqf0fj1oMXVBn9vEnJzDU&X-Amz-Signature=644431f3e8683ded8a112b445194a2b62d0a70e4941a96856f0cb21ae34cd612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

