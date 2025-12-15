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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQPBG2EU%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCmwSmNdL3toe0R53UHP1y9CIsOw6nVhY2gFM6Q7oTE6AIhAKMFo8HrxTAJDHA371OeyTvtYEIpRkPms59LEoCsg7NXKv8DCD8QABoMNjM3NDIzMTgzODA1IgzBAxfnG%2By6nYvHz8Eq3AMXzvLuoex4QINwvP%2BzqJX6hvM5HLUPnmf9ljpF8zs%2BlnrWWE7OQZO98h5aw12J%2FbgZbiHY4fRRsXb9f61qPNOnDVuC%2FkhP0tQsNJPSVp2LyXsAtOM%2BEvyBmP0%2BohOnth16VJKl%2BZL%2FHgLzYJ5dP0GsmFysQtzJ%2BJ5ggXZzqyLXffc3TKRNMEuYwG9RVdzKRjW5NA%2BvyPFo528urSsgD52fBZ%2BnhpeUSVUVATWJjfL8N4L1O77XhKjnX1onaIu%2B0VOwtskXZt9be5tBSHtw82wz3m%2F97bGYpDQ2MbQI7iHKH%2Bzb%2ByEY6u%2F0FORrcCI5Fcjuvaq0x4QY8dLC%2FUfuJWanMfqN3cPRLOfPuL%2BnuRSOZQReBVk70GJxS4kNRlhK5E9DOp8bBmBBvqrXpSiF6qiGWwpAu7LFon%2B7uKNOSGtjOTiNqqCYzYqc%2FJgAOPdP1x5uhB%2B7EYVX%2BLapamYhy8tN9yRI4QHPfo1BMFWIZbMZJPNEQXiITdp5sAPXAhgjl5QZFekflIV6m2%2BMQFV2GXN6SljRRXFRTtLuizw3TchU9ipnOcJSgGAYl1i4YOI0VBh96WoyjqFFl%2BJNGvxYxppnApaPZDjldS6GOKJ4FcB6VoE%2BQgcFuYN9SuvtzzDj2vzJBjqkAeUYAnp94vWLErinCyyXkDDwlYfCin8Y8hH8BUdNP1Lhknjiq54UdJRiJT9E5B7Ld32bh97rFTUv9wUb%2Bdw4LhPQTDSIJEZqsEsw7WN%2FJwuXYMOV7cYywYQtbOn1Dq4l6jOOtNA4ANCzbCaGcbXqHSE2mxN6wCYTmlwKynk0S%2F1TdPDELilgZjiRQB0Hos8W%2FR4yqFphpYZ2O8ZSDwZ6e0FUiHbm&X-Amz-Signature=fe91a4b0245bb1a84a3aae7ded057b1a475f66543816a63f3cf802f9053d0f94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQPBG2EU%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCmwSmNdL3toe0R53UHP1y9CIsOw6nVhY2gFM6Q7oTE6AIhAKMFo8HrxTAJDHA371OeyTvtYEIpRkPms59LEoCsg7NXKv8DCD8QABoMNjM3NDIzMTgzODA1IgzBAxfnG%2By6nYvHz8Eq3AMXzvLuoex4QINwvP%2BzqJX6hvM5HLUPnmf9ljpF8zs%2BlnrWWE7OQZO98h5aw12J%2FbgZbiHY4fRRsXb9f61qPNOnDVuC%2FkhP0tQsNJPSVp2LyXsAtOM%2BEvyBmP0%2BohOnth16VJKl%2BZL%2FHgLzYJ5dP0GsmFysQtzJ%2BJ5ggXZzqyLXffc3TKRNMEuYwG9RVdzKRjW5NA%2BvyPFo528urSsgD52fBZ%2BnhpeUSVUVATWJjfL8N4L1O77XhKjnX1onaIu%2B0VOwtskXZt9be5tBSHtw82wz3m%2F97bGYpDQ2MbQI7iHKH%2Bzb%2ByEY6u%2F0FORrcCI5Fcjuvaq0x4QY8dLC%2FUfuJWanMfqN3cPRLOfPuL%2BnuRSOZQReBVk70GJxS4kNRlhK5E9DOp8bBmBBvqrXpSiF6qiGWwpAu7LFon%2B7uKNOSGtjOTiNqqCYzYqc%2FJgAOPdP1x5uhB%2B7EYVX%2BLapamYhy8tN9yRI4QHPfo1BMFWIZbMZJPNEQXiITdp5sAPXAhgjl5QZFekflIV6m2%2BMQFV2GXN6SljRRXFRTtLuizw3TchU9ipnOcJSgGAYl1i4YOI0VBh96WoyjqFFl%2BJNGvxYxppnApaPZDjldS6GOKJ4FcB6VoE%2BQgcFuYN9SuvtzzDj2vzJBjqkAeUYAnp94vWLErinCyyXkDDwlYfCin8Y8hH8BUdNP1Lhknjiq54UdJRiJT9E5B7Ld32bh97rFTUv9wUb%2Bdw4LhPQTDSIJEZqsEsw7WN%2FJwuXYMOV7cYywYQtbOn1Dq4l6jOOtNA4ANCzbCaGcbXqHSE2mxN6wCYTmlwKynk0S%2F1TdPDELilgZjiRQB0Hos8W%2FR4yqFphpYZ2O8ZSDwZ6e0FUiHbm&X-Amz-Signature=99822730f1fa7e63e7c4b64aab0fe33bb2c7af7e488e4351f001ab6f9b56a654&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

