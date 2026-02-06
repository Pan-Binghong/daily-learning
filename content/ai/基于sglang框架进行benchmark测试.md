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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLL7WMC3%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQCG11f65m8rTgY4iXe8eY5CFy%2BZpmJ4i4LmtHjn69jWzgIgYDDK1oK7n8V5OtB1nFPJieNxuVZkea0th2JlVgWNh4Iq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDDL%2FlMsd%2Bmw2E%2FxjLyrcA1m%2FGVO5h%2FAmOv3OHpEhqbFmZYOnx%2Fi2rcwyH6J8z590CY5wXV3aYDuN8gAD%2Bzw5FtFCnJGANmbUGn35O8tmmUQoxlXS6PrE37JqkoCAYXovNLWw%2BBgtpzpQSgXqzffgpKvciy1%2FRSvxH9tSFI6ladMDkKpn26eykDl2vXii08MZHX21dM6JLZmH20klDkReiCZ7I03t7CjST7uUbCvgjFuBJGt2V5yp9jdvwC4wVgoZqXO0VzwibomLznwStxT9rv7PMgFY02JvuN%2FlaP6bmYz%2BtLnGu1zUmnWM5PyA6DrI0vtiCUgRDfyKDe3x9URNfd6fzrIMKB1uucwmcfgVBxPxZg%2ByLHGAaMwPyJslTFqSZhMRlIx%2FU%2FqZzGUdW9H8TwDZoPJVNHQqxxouHPR1kh8%2B3qIASJujT%2Fy9e5R4AEsXwThtqKv5GyHOe8MaA%2BAF1sXxDJR%2FVjehUv3cL8gXkCIkorvgz5G%2Bz3ktRv3AvXNidfsziILJdmBuY7WUxjhxuKZCQRbh9QFlBh5l6KXFN%2Fypka7rRovFF5NO8quHqdm8uxANUXzAFEwVOZisPTm6G%2BotLuZNQGvh0Dpal2cO1rPNvVfMvX%2Buzs0wgxIWaHVkhAMafaOo2MSsd6viMP65lcwGOqUBeClvZLfPbfYhXmT5gci0fhpfYDWLcXvtOT7J5rh1b5w%2ByxxAIFv0Ye9QL2sdM5yvttBl7YPN7Z6PW62GRBAGksBycIRV3ncqES6nHP1tqBDwQOuPrDe39JfhkvN%2FDSrVPVBApoCoC3mUeRmBCyUjh0RZgvsFFzQDFTuZ%2BZ1eAHwwO9WML36n4lVFYSfefoiVoIDXVxYwVRgEPquA2%2FYr2%2FF3p%2Fsj&X-Amz-Signature=b216b61b715265d7f6566cc22e542dbec4290f00ed9bedd958ef0fbd23c4dfa2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLL7WMC3%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQCG11f65m8rTgY4iXe8eY5CFy%2BZpmJ4i4LmtHjn69jWzgIgYDDK1oK7n8V5OtB1nFPJieNxuVZkea0th2JlVgWNh4Iq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDDL%2FlMsd%2Bmw2E%2FxjLyrcA1m%2FGVO5h%2FAmOv3OHpEhqbFmZYOnx%2Fi2rcwyH6J8z590CY5wXV3aYDuN8gAD%2Bzw5FtFCnJGANmbUGn35O8tmmUQoxlXS6PrE37JqkoCAYXovNLWw%2BBgtpzpQSgXqzffgpKvciy1%2FRSvxH9tSFI6ladMDkKpn26eykDl2vXii08MZHX21dM6JLZmH20klDkReiCZ7I03t7CjST7uUbCvgjFuBJGt2V5yp9jdvwC4wVgoZqXO0VzwibomLznwStxT9rv7PMgFY02JvuN%2FlaP6bmYz%2BtLnGu1zUmnWM5PyA6DrI0vtiCUgRDfyKDe3x9URNfd6fzrIMKB1uucwmcfgVBxPxZg%2ByLHGAaMwPyJslTFqSZhMRlIx%2FU%2FqZzGUdW9H8TwDZoPJVNHQqxxouHPR1kh8%2B3qIASJujT%2Fy9e5R4AEsXwThtqKv5GyHOe8MaA%2BAF1sXxDJR%2FVjehUv3cL8gXkCIkorvgz5G%2Bz3ktRv3AvXNidfsziILJdmBuY7WUxjhxuKZCQRbh9QFlBh5l6KXFN%2Fypka7rRovFF5NO8quHqdm8uxANUXzAFEwVOZisPTm6G%2BotLuZNQGvh0Dpal2cO1rPNvVfMvX%2Buzs0wgxIWaHVkhAMafaOo2MSsd6viMP65lcwGOqUBeClvZLfPbfYhXmT5gci0fhpfYDWLcXvtOT7J5rh1b5w%2ByxxAIFv0Ye9QL2sdM5yvttBl7YPN7Z6PW62GRBAGksBycIRV3ncqES6nHP1tqBDwQOuPrDe39JfhkvN%2FDSrVPVBApoCoC3mUeRmBCyUjh0RZgvsFFzQDFTuZ%2BZ1eAHwwO9WML36n4lVFYSfefoiVoIDXVxYwVRgEPquA2%2FYr2%2FF3p%2Fsj&X-Amz-Signature=89ccaa3bd9be0c9f15c6760ae2f7c4ff3dace7df8fc1bf2598e4e30180a117bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

