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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GEXD5PE%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCikET6wit7K1CoPVvQN3Jh4dm%2F9OJ2HdqXpyFcCietMAIgFz0l3fkn01AbrEwvI8j72TwhXYGbYj1r6EXzOub%2BFtkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDHeANGE%2BYqQmzvb0NyrcA%2BXXDOg3TjEdvPHqLUUAtUE8PgYD%2BibMgygaPVWwYsdUn%2FoMfD%2B9XM9W4qj046Zj46ggKingRe86syYZBJbt1J4zYbje%2F8WwtOdZLNNMJXGeyGdrVXmRXxCLVySg%2FjWS0oNqMslaTGYX3NCe6rkg4ofmojLYu3ndMnFalOekZRsMwrlgiLJflp5Pjmc4Fu3N4H0QFU%2Bn25V5D%2F78Tdy8RDbQG50cZal21KrC3QBL8chtGWTt%2BQWTQj1PD7FtwPcMtXK5XKi9xbUzGADLlZKXcpBfasRB3NuKaMTRDuyLfIey3n36tcY9vZmfOpMiRZ73ioCO57OnM0WVLuAto6jurgEp%2Fl1cKEFYuOQhHZ3NnW13OZmi2O3e8NpxMorCtaZI%2BQPExyMlVx2mwsAk5tmHecn8Ov3bcm9bDae7kgzzZkk20H44LmN0Bf3bV8JRpmb%2BZYg68tvKaHI7L9WXWQNQhWv3dheq7sMG8YrS%2FBJjHaz7awQ0PfaHCH1HaX4YsAmqd0dxl0J44WvAG1K3cYY4cuCAxatBlBHsV5fPn9HphJxfalx7NZU6r4poM4J1mTq7e6xinXIGHiurCZIF6oH5JNwDhahXIgtczaLawm%2B09Mo0XmuaUPv4Xo4kDzzxMPHDmswGOqUBq%2BvO8hVCEp%2FKCkBMj2ahR9LoB14BlQkeYsuVzggsCKOqOTTP5KJroVKxYi9z1uDpaNJ576D%2FTevJXDExwxUA4poC5FLHP%2FzEVWvENNGgXh9DaIyQAzmG6GXcizoX1bZduIJmQj3S6KHYQkJJQGRVED3vbTubiVhLfrVFMHiEDTjFi%2FzbKnaCJydyxp9SwIVu3%2BMDiMJWw5m3P0nN21tuxzoudxof&X-Amz-Signature=cc813c3b07ddb75502587f5fdc8fe0c0ad54a7852d51d44595ee98df49b7b14e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GEXD5PE%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCikET6wit7K1CoPVvQN3Jh4dm%2F9OJ2HdqXpyFcCietMAIgFz0l3fkn01AbrEwvI8j72TwhXYGbYj1r6EXzOub%2BFtkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDHeANGE%2BYqQmzvb0NyrcA%2BXXDOg3TjEdvPHqLUUAtUE8PgYD%2BibMgygaPVWwYsdUn%2FoMfD%2B9XM9W4qj046Zj46ggKingRe86syYZBJbt1J4zYbje%2F8WwtOdZLNNMJXGeyGdrVXmRXxCLVySg%2FjWS0oNqMslaTGYX3NCe6rkg4ofmojLYu3ndMnFalOekZRsMwrlgiLJflp5Pjmc4Fu3N4H0QFU%2Bn25V5D%2F78Tdy8RDbQG50cZal21KrC3QBL8chtGWTt%2BQWTQj1PD7FtwPcMtXK5XKi9xbUzGADLlZKXcpBfasRB3NuKaMTRDuyLfIey3n36tcY9vZmfOpMiRZ73ioCO57OnM0WVLuAto6jurgEp%2Fl1cKEFYuOQhHZ3NnW13OZmi2O3e8NpxMorCtaZI%2BQPExyMlVx2mwsAk5tmHecn8Ov3bcm9bDae7kgzzZkk20H44LmN0Bf3bV8JRpmb%2BZYg68tvKaHI7L9WXWQNQhWv3dheq7sMG8YrS%2FBJjHaz7awQ0PfaHCH1HaX4YsAmqd0dxl0J44WvAG1K3cYY4cuCAxatBlBHsV5fPn9HphJxfalx7NZU6r4poM4J1mTq7e6xinXIGHiurCZIF6oH5JNwDhahXIgtczaLawm%2B09Mo0XmuaUPv4Xo4kDzzxMPHDmswGOqUBq%2BvO8hVCEp%2FKCkBMj2ahR9LoB14BlQkeYsuVzggsCKOqOTTP5KJroVKxYi9z1uDpaNJ576D%2FTevJXDExwxUA4poC5FLHP%2FzEVWvENNGgXh9DaIyQAzmG6GXcizoX1bZduIJmQj3S6KHYQkJJQGRVED3vbTubiVhLfrVFMHiEDTjFi%2FzbKnaCJydyxp9SwIVu3%2BMDiMJWw5m3P0nN21tuxzoudxof&X-Amz-Signature=6037542c1ed2968b244a739e229f8b3e6cb6b26644b1cc86780605c709046a88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

