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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI65O7IJ%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTZsOvPG2vOp%2FXCxe2Sf%2FyYnoLCSfcWm9PJfkxtmlHOwIhAL70rLIGFtnVQL83FW%2BaP%2F6cvzgJVqv9LA5qctuIx8bGKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU2O6aQ%2BmaEpIoCJkq3AMNpffcJ6YPGHaKKSKaVrmC7caa03oZilAmS6sJdIOVIF9AoRo9q0J16em7e5WdnwyXR4RdFy2BAdJw1aVo0vVbOV%2B7dH6oU4V1IqQLfkcaVoA9bWSRmCiEjvQkwayysrI7MI7ZLtz5d0rF9Ng%2BVMtQVRv15Otn2VAmXoySOnIYdT2UGTjFI0uGBuFtYJSav3IxIJVmEv1kODmqZlXHGmjHJ3oDXgY0%2BZ%2FwbP9VIUSGlRDiw5cP5tj6WlhtWoQvd4o5Eq9n%2Fht1fJp4j1VoU3UK67bloXlqhLiGb%2FWGI6l7SsT%2Fa5QpZA0UqWnUnXXETHb7sfNzN7M1JBbHFHiPPmP%2FItXZU5tFj%2FeDh7YfpMPvGAiyQv432ukHThoYYm8nZy%2FVg2hsETrVHeBOC8gCXm%2FC9lvgNlBbaqEfywRe93TQKc4mrcpj9zr5XWxnboWfHp%2Fu2oSwmFXw1LZzBXDoc0i%2F3%2Bck3Wgs%2FlV50GAV4gPHZjfo0rB5fl5T%2BDo8M2UQvxFF70nvVlg7KYr6Z%2Fu9swkn8B033hm09Jp6e0k4Kjv5PE%2B3slUQT4n9XDAsbxI0%2FtkWrYhrtnq%2F%2BGyxE8Ochr14dCP0UR9z174zL24%2BU895oZPW5Em8vCXSL%2BvXvzD%2B8qPJBjqkAXVGT0ykz0iS4s4IKtye7K79Ci3YMyNNaiBv8slJiPOYg1ikXQPWOe0wusjiBs1YlsW4Cox1VLtw6my7NNWyF0Si5vBHbJrB2Cphre5FA1Pi9O%2BqnV4PIJk7EBE0cEGx7pmBkw7nK3%2FPjSNjcpBnzaOMHEDURtde5Fi5KjtTuWckczI3PZyXp%2FTBaSCxwgKocG2Xk7%2F86TWjHo66XTnOIIUVERrt&X-Amz-Signature=b20ad37587f356a06a75ec5b455656e5abf709d3a542d230c1aa53bb910349c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI65O7IJ%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTZsOvPG2vOp%2FXCxe2Sf%2FyYnoLCSfcWm9PJfkxtmlHOwIhAL70rLIGFtnVQL83FW%2BaP%2F6cvzgJVqv9LA5qctuIx8bGKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU2O6aQ%2BmaEpIoCJkq3AMNpffcJ6YPGHaKKSKaVrmC7caa03oZilAmS6sJdIOVIF9AoRo9q0J16em7e5WdnwyXR4RdFy2BAdJw1aVo0vVbOV%2B7dH6oU4V1IqQLfkcaVoA9bWSRmCiEjvQkwayysrI7MI7ZLtz5d0rF9Ng%2BVMtQVRv15Otn2VAmXoySOnIYdT2UGTjFI0uGBuFtYJSav3IxIJVmEv1kODmqZlXHGmjHJ3oDXgY0%2BZ%2FwbP9VIUSGlRDiw5cP5tj6WlhtWoQvd4o5Eq9n%2Fht1fJp4j1VoU3UK67bloXlqhLiGb%2FWGI6l7SsT%2Fa5QpZA0UqWnUnXXETHb7sfNzN7M1JBbHFHiPPmP%2FItXZU5tFj%2FeDh7YfpMPvGAiyQv432ukHThoYYm8nZy%2FVg2hsETrVHeBOC8gCXm%2FC9lvgNlBbaqEfywRe93TQKc4mrcpj9zr5XWxnboWfHp%2Fu2oSwmFXw1LZzBXDoc0i%2F3%2Bck3Wgs%2FlV50GAV4gPHZjfo0rB5fl5T%2BDo8M2UQvxFF70nvVlg7KYr6Z%2Fu9swkn8B033hm09Jp6e0k4Kjv5PE%2B3slUQT4n9XDAsbxI0%2FtkWrYhrtnq%2F%2BGyxE8Ochr14dCP0UR9z174zL24%2BU895oZPW5Em8vCXSL%2BvXvzD%2B8qPJBjqkAXVGT0ykz0iS4s4IKtye7K79Ci3YMyNNaiBv8slJiPOYg1ikXQPWOe0wusjiBs1YlsW4Cox1VLtw6my7NNWyF0Si5vBHbJrB2Cphre5FA1Pi9O%2BqnV4PIJk7EBE0cEGx7pmBkw7nK3%2FPjSNjcpBnzaOMHEDURtde5Fi5KjtTuWckczI3PZyXp%2FTBaSCxwgKocG2Xk7%2F86TWjHo66XTnOIIUVERrt&X-Amz-Signature=67ae89415924b4444f174a2d358d9c830e1c5821a27c54b15a0e1b31823881f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

