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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TFWOZKM%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCVVSVfsShqHCYTcucM4MDFtX1nH7Wre1dXY2VYlBKG1gIgENLV1%2Bpj5Rhjw9uvjcGTdsQAwFxTXUBKaiggk3Rn79AqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgRGwtZW9JUSARwbyrcAwDrUfmEX48ZdmifT9ZMJRJXKdqSnhW6em5kDIwolXfpsH%2FEGOJMQ3crXZJZjpb4SbCg0%2FKuzikIVvlopvZkr3bK9eIXHz9v6qIsr5BjzN8BY2Lfde1gTaPnNGmIKSCNm9GJsAarKfyuBfniUHPe8%2FN0j8RFVcpGv3oLFcPBqq2b%2BD9XK9PnvoaHoJhYYwxCunj49I69sMW4dz8MfUSsT7G%2F6nwIhWAwOsMvGJ33%2BtoRGxdSUIqC%2F7354Y2ADfWR7fc1n2w%2BZLvTHJcExUfJenNN%2FZ1qdlcEDc95aZ8hyY8PDl4S8MDeIH7e6XfIJ70uQ3fayOxRRR3NdVCDmjGYVrXId9BtXnfM%2Fj3KBATPVROPMqdRNA6a7ip5ThLnYC%2BguHwHLEcozB6MVyNo%2BQu72QF69s2DWxltt6RCIrXrw1GtzgrgvndBahMgTgC1yPfy6R73GN1pXz8kVuc1sVaMnLMhmihPHDNQBccRm%2B4XT%2Bd6Y1c%2FTCkJPeDkfsmmtrpwxL4roHBbpE14hYhQajbDSWROdYsrKOihdh3%2FiaWwarVjyR6DenWin5i2HhUXfE8Dr6hbiV5UrtX9CY%2BL2icryyiNC6m50GuN3IRbS58Az5SRQq8VJ9DyW6jCp%2BduMPGm6M0GOqUBOE2%2Bz7UG19lwyBIPHeR05%2FzOrCZmRlPQjPDDyQ%2F4qodzgifd6Q5%2FhpRe3oXkrjZ42qCWMNJOan58OG6T%2BN3myv6h6HyjfujdM%2BP5pRxexnA2VDGZpATojbqkJE1LqnFnAbKvPkStPi8Kedn07nmFE88nh2kuSRZrZxNu%2FaL1RSfj7y6s0Osm7B1a12hHWcRwQLxWhmDsBniYThXhNPfy1H4dq4eQ&X-Amz-Signature=383e56b77acf32038666d84f9b228e10089138217f8be5955b59d59ff59ab86a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TFWOZKM%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCVVSVfsShqHCYTcucM4MDFtX1nH7Wre1dXY2VYlBKG1gIgENLV1%2Bpj5Rhjw9uvjcGTdsQAwFxTXUBKaiggk3Rn79AqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgRGwtZW9JUSARwbyrcAwDrUfmEX48ZdmifT9ZMJRJXKdqSnhW6em5kDIwolXfpsH%2FEGOJMQ3crXZJZjpb4SbCg0%2FKuzikIVvlopvZkr3bK9eIXHz9v6qIsr5BjzN8BY2Lfde1gTaPnNGmIKSCNm9GJsAarKfyuBfniUHPe8%2FN0j8RFVcpGv3oLFcPBqq2b%2BD9XK9PnvoaHoJhYYwxCunj49I69sMW4dz8MfUSsT7G%2F6nwIhWAwOsMvGJ33%2BtoRGxdSUIqC%2F7354Y2ADfWR7fc1n2w%2BZLvTHJcExUfJenNN%2FZ1qdlcEDc95aZ8hyY8PDl4S8MDeIH7e6XfIJ70uQ3fayOxRRR3NdVCDmjGYVrXId9BtXnfM%2Fj3KBATPVROPMqdRNA6a7ip5ThLnYC%2BguHwHLEcozB6MVyNo%2BQu72QF69s2DWxltt6RCIrXrw1GtzgrgvndBahMgTgC1yPfy6R73GN1pXz8kVuc1sVaMnLMhmihPHDNQBccRm%2B4XT%2Bd6Y1c%2FTCkJPeDkfsmmtrpwxL4roHBbpE14hYhQajbDSWROdYsrKOihdh3%2FiaWwarVjyR6DenWin5i2HhUXfE8Dr6hbiV5UrtX9CY%2BL2icryyiNC6m50GuN3IRbS58Az5SRQq8VJ9DyW6jCp%2BduMPGm6M0GOqUBOE2%2Bz7UG19lwyBIPHeR05%2FzOrCZmRlPQjPDDyQ%2F4qodzgifd6Q5%2FhpRe3oXkrjZ42qCWMNJOan58OG6T%2BN3myv6h6HyjfujdM%2BP5pRxexnA2VDGZpATojbqkJE1LqnFnAbKvPkStPi8Kedn07nmFE88nh2kuSRZrZxNu%2FaL1RSfj7y6s0Osm7B1a12hHWcRwQLxWhmDsBniYThXhNPfy1H4dq4eQ&X-Amz-Signature=2637a7d88b4b0aae2784c7745102dad0953af7d0f7c11090b4bd8a5e5a4af028&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

