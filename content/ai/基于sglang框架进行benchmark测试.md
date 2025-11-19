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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TSWYI36%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIEhU0C3F%2F0jvfS5yAydn8WG9qZJ8SSOc4gTpFECCmzJKAiEA1HyF5uxPVXHu%2B3%2BMRw4anS3l%2BTqq95TfaTlata3WDwIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOe64XnEuXupLGq4dircA%2B15MiUWfNZsbOjXXWr96DdspIpGOCmuA33VJWsp32gqRRbWsVmar87bygnrJrH9PYDE1H9uqynfUQrs0HHJ4RtF9kfuV4i%2BSECSPLrKqIwdBTBYJEhdapTcUp16NmYwD1lNg56iTO5r5InZryoweTfrHbXlVtybX4g7y57hihamZNv5WCZtD%2FJBkS1BziVMe6hKP0jJ2DC%2BcraB5IlAVtbA%2FeQwmdWF6vrl6fen0f3UNQS01cZbYvZqu5QqzGgpncvhfdeKu8m5d6UeVDJaVnpTnMt7DoJXKZbspqpQD1H%2B9MiTpKpAZYANwc6FO23t1vPurS2EELFqAPaMeIGayFs3WgLvm4neJbN6Myqr54M17HeyFABkI7oycMvFv76rOszq4u4y01ROGJBx8OfJ1JDFXD%2FrPaTpUvuT3otgrTl6KjLH4hqWyqsEVtJjxOdOxQPG6lmu5k6IdZjrkI64rN5QIr1VuAixmLX34zryDikaJCQ52sJaeGOsYSFqqUtHfIF2LdP65nFH%2F9rz5CE7UQIFxIMt%2FB6CB8KRnr8cl5EaH9pqR70Z4E7g4SPCEQMidoZfKdINu%2BohQv0NlOkj2UZ4oKfGqMvjbXp82jV%2B0nh1%2Bw974AfF%2FGBLXfNMMJ%2FK9MgGOqUBpxetyKUvQC%2BftKgMhqNRxDk%2BnZA7htYTX45J9yaGtMlTDgH6H%2FSQk2ljgWocX8v7xcdrzuSXKPfJ61PVajomu7eqqUx1zSeU3VYA8iSOXpRKnihKpuQ%2B6OV17tZfIAoWPiDk1oQ%2F%2FO4VSXVzbv%2FEaYuOSxcRK1cB%2B%2FoP1%2B2eDACKedqs4JYo8f8hGrty7fwsLA8vlUTAE3jA0PaE1PMh%2FpqKEa0o&X-Amz-Signature=ceb09bcc543e3088138e16d1546f53d1b7a61f8e5786586e04e81f16e4ac0065&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TSWYI36%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIEhU0C3F%2F0jvfS5yAydn8WG9qZJ8SSOc4gTpFECCmzJKAiEA1HyF5uxPVXHu%2B3%2BMRw4anS3l%2BTqq95TfaTlata3WDwIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOe64XnEuXupLGq4dircA%2B15MiUWfNZsbOjXXWr96DdspIpGOCmuA33VJWsp32gqRRbWsVmar87bygnrJrH9PYDE1H9uqynfUQrs0HHJ4RtF9kfuV4i%2BSECSPLrKqIwdBTBYJEhdapTcUp16NmYwD1lNg56iTO5r5InZryoweTfrHbXlVtybX4g7y57hihamZNv5WCZtD%2FJBkS1BziVMe6hKP0jJ2DC%2BcraB5IlAVtbA%2FeQwmdWF6vrl6fen0f3UNQS01cZbYvZqu5QqzGgpncvhfdeKu8m5d6UeVDJaVnpTnMt7DoJXKZbspqpQD1H%2B9MiTpKpAZYANwc6FO23t1vPurS2EELFqAPaMeIGayFs3WgLvm4neJbN6Myqr54M17HeyFABkI7oycMvFv76rOszq4u4y01ROGJBx8OfJ1JDFXD%2FrPaTpUvuT3otgrTl6KjLH4hqWyqsEVtJjxOdOxQPG6lmu5k6IdZjrkI64rN5QIr1VuAixmLX34zryDikaJCQ52sJaeGOsYSFqqUtHfIF2LdP65nFH%2F9rz5CE7UQIFxIMt%2FB6CB8KRnr8cl5EaH9pqR70Z4E7g4SPCEQMidoZfKdINu%2BohQv0NlOkj2UZ4oKfGqMvjbXp82jV%2B0nh1%2Bw974AfF%2FGBLXfNMMJ%2FK9MgGOqUBpxetyKUvQC%2BftKgMhqNRxDk%2BnZA7htYTX45J9yaGtMlTDgH6H%2FSQk2ljgWocX8v7xcdrzuSXKPfJ61PVajomu7eqqUx1zSeU3VYA8iSOXpRKnihKpuQ%2B6OV17tZfIAoWPiDk1oQ%2F%2FO4VSXVzbv%2FEaYuOSxcRK1cB%2B%2FoP1%2B2eDACKedqs4JYo8f8hGrty7fwsLA8vlUTAE3jA0PaE1PMh%2FpqKEa0o&X-Amz-Signature=2c82b19303080e089ea66c39bf075e4352fdb71efb24bbf45852786c4dbe88d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

