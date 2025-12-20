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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVHWFEVA%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWb%2BYqdauRsh9FAtEf4OAURjgenNj5GV0L4RUxKBQR1gIgD5cHQV3X2bABClIpnN28tdhWQ2rXr7%2FlBtiw2HV5XkgqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNY9qVf%2BM3BOWORI7ircAwxjUlQTbX72yFGK90DwWNTWZ0WBDTkkYa0rJ%2B8NBnJxx4U2FSTLtDS%2B29CWEtv9099eAmUV6DzP5GRsbkXMN45BYdta8Xh1EsxHnEHLlb8Ytz%2BM6YgFYitx6nGFIyMDaU2Wy23wfzolr8XgIs662wkjnnTJlVdv60nP8pb65MbL3LUgvYckG3rdtmE46QI%2Bgm7TY5upmLcYh3MB75972DSyOXyS9ukGATZMNkr98cXq6lArqDpBfOL7VRTQXIDuD2CvXfQIZnemUJ%2BqZdtClWOAUMOqppYzIEeH%2BQdA3sqWTNVJExQuTviFAsP22rKOVZ9ggfGFDUZJaugvOCI6Zwy6k91%2BqN9YtEiwp5kbUtVKLYzo8rEryC8yDI6w6m8UaBatzNzVC%2BWiXmOJupIr5okwAnXpkIoa%2FMh4csBOid%2B9%2FfvmO0NaOQM%2B24tcCOUTfriZ7X9qBn4qgF%2F59bEIcZazvTgIRa6TZtAb%2F8%2FSzVVzNeeeAKjXF9gMIyfKnOYv%2B9pHkAG85BlKVq3WHyI0d%2FcT3OwEJxp4mt4iv9C8YjJT%2B7kiBD54%2B78dbUVY1Z2cUFnNZvHnytLy6KmXJVWZBi7fAQkc8iZ3sw%2FXG40qH3I%2FgiOYWgKj%2FIjutXUzMMmFmMoGOqUBoYNrDIUodK6aAyTBpIzO7XH%2F2blNz2lMWQRdktQySalpOOEbcZGdG1lZff%2Br125A3DpsvfGYeo9tmCR6sCgCbAijrn0bekuasIF6VfKJVBVcCDRDf4RrswrXLIHJkirWvU9vpSOh6bBEwALuz5xcj%2BsDR%2FwUfFwDEIqjilt1pr6uxn7dtae7m2XnGNkx%2B8xCYit%2FohY4JLuQ1lrHsOiJIgPC8Wci&X-Amz-Signature=3dca7f2f27760e7ef1024ce5b71c0a380c3142fcc6087b9289d94f61f7874e08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVHWFEVA%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWb%2BYqdauRsh9FAtEf4OAURjgenNj5GV0L4RUxKBQR1gIgD5cHQV3X2bABClIpnN28tdhWQ2rXr7%2FlBtiw2HV5XkgqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNY9qVf%2BM3BOWORI7ircAwxjUlQTbX72yFGK90DwWNTWZ0WBDTkkYa0rJ%2B8NBnJxx4U2FSTLtDS%2B29CWEtv9099eAmUV6DzP5GRsbkXMN45BYdta8Xh1EsxHnEHLlb8Ytz%2BM6YgFYitx6nGFIyMDaU2Wy23wfzolr8XgIs662wkjnnTJlVdv60nP8pb65MbL3LUgvYckG3rdtmE46QI%2Bgm7TY5upmLcYh3MB75972DSyOXyS9ukGATZMNkr98cXq6lArqDpBfOL7VRTQXIDuD2CvXfQIZnemUJ%2BqZdtClWOAUMOqppYzIEeH%2BQdA3sqWTNVJExQuTviFAsP22rKOVZ9ggfGFDUZJaugvOCI6Zwy6k91%2BqN9YtEiwp5kbUtVKLYzo8rEryC8yDI6w6m8UaBatzNzVC%2BWiXmOJupIr5okwAnXpkIoa%2FMh4csBOid%2B9%2FfvmO0NaOQM%2B24tcCOUTfriZ7X9qBn4qgF%2F59bEIcZazvTgIRa6TZtAb%2F8%2FSzVVzNeeeAKjXF9gMIyfKnOYv%2B9pHkAG85BlKVq3WHyI0d%2FcT3OwEJxp4mt4iv9C8YjJT%2B7kiBD54%2B78dbUVY1Z2cUFnNZvHnytLy6KmXJVWZBi7fAQkc8iZ3sw%2FXG40qH3I%2FgiOYWgKj%2FIjutXUzMMmFmMoGOqUBoYNrDIUodK6aAyTBpIzO7XH%2F2blNz2lMWQRdktQySalpOOEbcZGdG1lZff%2Br125A3DpsvfGYeo9tmCR6sCgCbAijrn0bekuasIF6VfKJVBVcCDRDf4RrswrXLIHJkirWvU9vpSOh6bBEwALuz5xcj%2BsDR%2FwUfFwDEIqjilt1pr6uxn7dtae7m2XnGNkx%2B8xCYit%2FohY4JLuQ1lrHsOiJIgPC8Wci&X-Amz-Signature=a177d1a91832f4e05628d4dc9edba3faf8269dcda70659e2610233f5c1986284&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

