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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXCJYJG%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F9bJfR71VnYYMvYB4zJMD0nmFO7pQur50dNn%2Fl6XFewIgaZGMB2vKesHNxWkfoazRhQBHcYuz4d%2BHN1lu4kVma%2FgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOUUEANHZ%2BTQfteASrcA%2FB5ZWf4C7Sh8YEsBhmE2K%2B33IGbU4v%2FZnWX%2BNvArPWoyzpwWlhe05%2FWVJpAO2QK6wrDdWEsppfZJAQxNSAm2ZwQvvmVMDr04qwHbqgDkp0FLv1q5EAGqPYCoUkcPZ%2FlZfgwVgs5gYx03sq%2BZW3u42JkKVISc1fM7yxGn77O1iIkANk4VU32oVIv6nwpszsynrLeI0uC8uFpnuqTGC7fezrBFV7OMrjx3f5zyjhi4FM21OnfTTUnbXrqm73N7DJRnupCgU%2F3OZ5IrlE%2FbqSos6lzMcrgeg%2F1A0XHMN85R%2B0clyLx6K0j3ikNuwnUgbIzqPui4pp8WH11JMp7jQasyh6jmXPjJ8uPmSt9sqsRgI41WfAP6%2FdDBanJgR5dBk%2BMn%2FeQd5rpIy2gQ4MzzleqMzcFAVVhOWrhBYPp6oKCvOoi7OS7BxKbcEt9Iqh95E%2Fj8utSMBGTm%2FnyJEJD5e4unCIciYbB5nrFaydywfh5Li1HE2frb6J9Uba%2BheSUiQIRiSG0F8Usu%2FGIdGFESMKnfwAZvyE0%2F0MMZ2nbp7%2FzcBeZ%2BHGQIzR57iwV0Qjvz1YBFBo3bvtEAQ7y2CJ%2FL5MGLj6e6wdUw3NOooUsAH%2Fa3p13IIceWH22z%2FzAzfHJMP%2BVpcwGOqUBif7PkB3mDGJ%2BtoYJAYFp32AbD109AmlysOfw7EtF4OMJNwmeKF6e4EDPJA5mmLQ634mIO4bFAI5M9tbhppGJlghtbyc%2B21lj0e%2BRLiXJNhg9eHskTsdQobq9IoZbsjcNyZlOBo%2F%2FITx35nJ5jvO2sIXRBv3Dx%2B7rBPV0UGAdIGFGFeiVmZWe3SZ1SMjKqut05IJEsJNAh3WH2X1JWNjZ9qYrU4C%2B&X-Amz-Signature=06d515ba21a2a206553c9017637bd9402d8726ae620b23abea534038e11f4b63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXCJYJG%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F9bJfR71VnYYMvYB4zJMD0nmFO7pQur50dNn%2Fl6XFewIgaZGMB2vKesHNxWkfoazRhQBHcYuz4d%2BHN1lu4kVma%2FgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOUUEANHZ%2BTQfteASrcA%2FB5ZWf4C7Sh8YEsBhmE2K%2B33IGbU4v%2FZnWX%2BNvArPWoyzpwWlhe05%2FWVJpAO2QK6wrDdWEsppfZJAQxNSAm2ZwQvvmVMDr04qwHbqgDkp0FLv1q5EAGqPYCoUkcPZ%2FlZfgwVgs5gYx03sq%2BZW3u42JkKVISc1fM7yxGn77O1iIkANk4VU32oVIv6nwpszsynrLeI0uC8uFpnuqTGC7fezrBFV7OMrjx3f5zyjhi4FM21OnfTTUnbXrqm73N7DJRnupCgU%2F3OZ5IrlE%2FbqSos6lzMcrgeg%2F1A0XHMN85R%2B0clyLx6K0j3ikNuwnUgbIzqPui4pp8WH11JMp7jQasyh6jmXPjJ8uPmSt9sqsRgI41WfAP6%2FdDBanJgR5dBk%2BMn%2FeQd5rpIy2gQ4MzzleqMzcFAVVhOWrhBYPp6oKCvOoi7OS7BxKbcEt9Iqh95E%2Fj8utSMBGTm%2FnyJEJD5e4unCIciYbB5nrFaydywfh5Li1HE2frb6J9Uba%2BheSUiQIRiSG0F8Usu%2FGIdGFESMKnfwAZvyE0%2F0MMZ2nbp7%2FzcBeZ%2BHGQIzR57iwV0Qjvz1YBFBo3bvtEAQ7y2CJ%2FL5MGLj6e6wdUw3NOooUsAH%2Fa3p13IIceWH22z%2FzAzfHJMP%2BVpcwGOqUBif7PkB3mDGJ%2BtoYJAYFp32AbD109AmlysOfw7EtF4OMJNwmeKF6e4EDPJA5mmLQ634mIO4bFAI5M9tbhppGJlghtbyc%2B21lj0e%2BRLiXJNhg9eHskTsdQobq9IoZbsjcNyZlOBo%2F%2FITx35nJ5jvO2sIXRBv3Dx%2B7rBPV0UGAdIGFGFeiVmZWe3SZ1SMjKqut05IJEsJNAh3WH2X1JWNjZ9qYrU4C%2B&X-Amz-Signature=5171ae0defc597b9dcbaef24ab0569834ee60c51cf8e1eaa0b2b3a8d3cba5047&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

