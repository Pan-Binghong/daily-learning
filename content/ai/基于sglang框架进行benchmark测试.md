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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7KONFR%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIHVvy%2FH4tbkJIG5f6vR2VtBOnxJFJleVPHkr1AeVrV2jAiEA148znN82PdOgNL9L7ljyFT910M6eFVJXqURhUgcwEMMqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGbrsmtn%2Bxr3RucGWircAwrPIpzXKHRsU%2BTq%2FoueLlHghKi6BZFsaYMDdr9sravFcspVDQZEk9xRE2HU9jiwv7HLBt9WPY4JHdXPrLq%2FyZr1lwEJa2Qcy5%2Bks7Af750AoSyQaqfaMMq8IGbKyPZXucoLB9NIdDqY4qgRwE%2BGOq8f3ZEcpW0SrZmNVeacwJ4wlgwxufxwpY9AAVma6t%2Fu0XcgyENjZO3UIRbXXOYBaBpgvSzriFfOQrtv%2FVCIKO%2FWBw7qOVhnXqHQ4g5jjXl2AtMHFIO2q7rXVLh11gAVmVKOf9b0MAJP04DBSbfbA5K5mWxhNNI6oXzl7fhwA7nQzFVtY2A7hveLenuY1kBUFy%2FxFlbtZzg1IfbKChXef4iAHFMysmOK%2BLVnRuXzMJAXsb5T4ikp2qds03ZacvjHe5eweaMrB6sCulhG0u4W6deSTXrXwB1BOkAcVvy873IBFeEwYdeTGE%2FWoBkZEZQEgJzyZti9LBTKRJgDU06ECaGxbubj1MaS8FNSaiSdjKdTr6o1cn31LHuCgx6ak57DWHj7EuUze5VmeTyOiVMp6JyH9%2BPdO28TERRAw3PJLsZtWtmqusrvMsak2sNIKPhrcnRp0SZ0eQoJURGNQEz8xagY5EdzF1mVJYtcrkmuMILYhcwGOqUBTafiN%2FeaML6aKf5cPDXZAJHpUf%2By9YlsHy95GT4U3L4Ny0HsYnmg%2BUqEJ421lKfduZ%2B9N84P8k38wW1SpWXZ9G1E67eJCEpL5JxBgJmGMwuKiL283P27mK%2FtQEYAcgoQuU9zeS7TZrTu18NhLevSiylur5X7Zbx0WjdUEwOWqIk0%2F%2FDbdxAhotk4zAe8mYNNIZh6jKZF%2FYLiS9DKVCaQTCy5RiXF&X-Amz-Signature=14606c95231b226b180b877e648c2f75455482dbc69981166634849d740672e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7KONFR%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIHVvy%2FH4tbkJIG5f6vR2VtBOnxJFJleVPHkr1AeVrV2jAiEA148znN82PdOgNL9L7ljyFT910M6eFVJXqURhUgcwEMMqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGbrsmtn%2Bxr3RucGWircAwrPIpzXKHRsU%2BTq%2FoueLlHghKi6BZFsaYMDdr9sravFcspVDQZEk9xRE2HU9jiwv7HLBt9WPY4JHdXPrLq%2FyZr1lwEJa2Qcy5%2Bks7Af750AoSyQaqfaMMq8IGbKyPZXucoLB9NIdDqY4qgRwE%2BGOq8f3ZEcpW0SrZmNVeacwJ4wlgwxufxwpY9AAVma6t%2Fu0XcgyENjZO3UIRbXXOYBaBpgvSzriFfOQrtv%2FVCIKO%2FWBw7qOVhnXqHQ4g5jjXl2AtMHFIO2q7rXVLh11gAVmVKOf9b0MAJP04DBSbfbA5K5mWxhNNI6oXzl7fhwA7nQzFVtY2A7hveLenuY1kBUFy%2FxFlbtZzg1IfbKChXef4iAHFMysmOK%2BLVnRuXzMJAXsb5T4ikp2qds03ZacvjHe5eweaMrB6sCulhG0u4W6deSTXrXwB1BOkAcVvy873IBFeEwYdeTGE%2FWoBkZEZQEgJzyZti9LBTKRJgDU06ECaGxbubj1MaS8FNSaiSdjKdTr6o1cn31LHuCgx6ak57DWHj7EuUze5VmeTyOiVMp6JyH9%2BPdO28TERRAw3PJLsZtWtmqusrvMsak2sNIKPhrcnRp0SZ0eQoJURGNQEz8xagY5EdzF1mVJYtcrkmuMILYhcwGOqUBTafiN%2FeaML6aKf5cPDXZAJHpUf%2By9YlsHy95GT4U3L4Ny0HsYnmg%2BUqEJ421lKfduZ%2B9N84P8k38wW1SpWXZ9G1E67eJCEpL5JxBgJmGMwuKiL283P27mK%2FtQEYAcgoQuU9zeS7TZrTu18NhLevSiylur5X7Zbx0WjdUEwOWqIk0%2F%2FDbdxAhotk4zAe8mYNNIZh6jKZF%2FYLiS9DKVCaQTCy5RiXF&X-Amz-Signature=5ce097e774360db694b83c67bbeeee0dd279c41fb9d05d46843ec381375e586b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

