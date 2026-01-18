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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YMA45B5%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3VmGTyDW%2FbIDXfu6NnPXSBmI25dBWgJXw0qSQD9NKlAiEA5ZW9pGk15164AUOnZZ%2FkA68ZZqjXoPpVubcYWb13aQMq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDA0CAPrbc2TKQalajircA9EgqQQr5UCJXojxgRpxXdIRPjwas%2Bj94%2BUp7K6jyUE4YjcCb6TN59N5TO4nODP%2BWT4k2swzsCCQXtuZn7zitxFYG%2Bs95f2XyftHD6zz%2FRSMCyqlv9hkryF0cwKLUBIMjoVX8uKDb8fJl5nVgLtTAB8pr%2F%2BiBOPfgfLF%2B6wJOvqwLsPQuuiDJzUn6tSV4iJNCc1HrzryfuTt9wPtvcrawJHdLYEqUuWK89Glfp6%2B5DKL3cTC%2FqqPOCNJVIxWrZPwNGWmJuUrVVbyFZc9gQkPfQHd6WABnEuTnVFSrFgIdH29j%2B2ciIBR70RhrSP2vaVXQBaXaxD0%2BaxdlcQaJrxv%2FaH5eq%2Btsy6gV1iAeIm%2B7fJMA2McBS8GDvoGWRBQ2KxDVQqb7M7jPQVZmmYdwILcXEVafcRG00ddOfiYL24ot7VZDVcVNPVCdex01XgIuxAogSLc7gbmWVP5whL5cpI8OaUWcjhesRnc4o6JMdqn1Lr0ZNdmxarn8kCEYmqCW2AZgCODahL%2FtimJEfiE04wWxVYBjcGrlzSxY5VHkPVof3XFnprJ0mp5b4D4D1uxLwFvUV8v1fPiRoZoJiiEWzoLdxEhY%2FTgj7T7n5zwHnUzTaqy34S3u7sUBnX9BgXfMNqBscsGOqUBFMUM959oRnXtF1msjts%2BBQV0YGG1IZTLH4ee%2FU2wgK6M%2FBj%2Fs7loCVmp6uo38DmlNkpOL9gWt9fWgCNWFUvDFHGNGpzf24iynSnMc45Yo%2Bz%2BO%2B%2Bc%2FM5vV9agyP5BWenrRcKn9GZElUgVNpj5IIhV4lFhphwvetoRcxbm1GB6m3xt1a%2F7ezodiSZ4XdvRznRc8N7HenfjJcvx5988f40xG%2FEfTlrX&X-Amz-Signature=05d318982f07c49dbd0d9559966d06732b444bbc9dbff06d0054fbd0288b251b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YMA45B5%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3VmGTyDW%2FbIDXfu6NnPXSBmI25dBWgJXw0qSQD9NKlAiEA5ZW9pGk15164AUOnZZ%2FkA68ZZqjXoPpVubcYWb13aQMq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDA0CAPrbc2TKQalajircA9EgqQQr5UCJXojxgRpxXdIRPjwas%2Bj94%2BUp7K6jyUE4YjcCb6TN59N5TO4nODP%2BWT4k2swzsCCQXtuZn7zitxFYG%2Bs95f2XyftHD6zz%2FRSMCyqlv9hkryF0cwKLUBIMjoVX8uKDb8fJl5nVgLtTAB8pr%2F%2BiBOPfgfLF%2B6wJOvqwLsPQuuiDJzUn6tSV4iJNCc1HrzryfuTt9wPtvcrawJHdLYEqUuWK89Glfp6%2B5DKL3cTC%2FqqPOCNJVIxWrZPwNGWmJuUrVVbyFZc9gQkPfQHd6WABnEuTnVFSrFgIdH29j%2B2ciIBR70RhrSP2vaVXQBaXaxD0%2BaxdlcQaJrxv%2FaH5eq%2Btsy6gV1iAeIm%2B7fJMA2McBS8GDvoGWRBQ2KxDVQqb7M7jPQVZmmYdwILcXEVafcRG00ddOfiYL24ot7VZDVcVNPVCdex01XgIuxAogSLc7gbmWVP5whL5cpI8OaUWcjhesRnc4o6JMdqn1Lr0ZNdmxarn8kCEYmqCW2AZgCODahL%2FtimJEfiE04wWxVYBjcGrlzSxY5VHkPVof3XFnprJ0mp5b4D4D1uxLwFvUV8v1fPiRoZoJiiEWzoLdxEhY%2FTgj7T7n5zwHnUzTaqy34S3u7sUBnX9BgXfMNqBscsGOqUBFMUM959oRnXtF1msjts%2BBQV0YGG1IZTLH4ee%2FU2wgK6M%2FBj%2Fs7loCVmp6uo38DmlNkpOL9gWt9fWgCNWFUvDFHGNGpzf24iynSnMc45Yo%2Bz%2BO%2B%2Bc%2FM5vV9agyP5BWenrRcKn9GZElUgVNpj5IIhV4lFhphwvetoRcxbm1GB6m3xt1a%2F7ezodiSZ4XdvRznRc8N7HenfjJcvx5988f40xG%2FEfTlrX&X-Amz-Signature=110fd87915320f21c4bbcf8791aee8f441220dc9aa303033718282da50982e63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

