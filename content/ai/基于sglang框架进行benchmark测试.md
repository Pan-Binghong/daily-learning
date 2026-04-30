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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUJDYECR%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCmCTO4x4R%2B65YIA9AcK1S7PhpaNYSiZM3TbGGLPx3MvAIhAIlbrU4ym7l489hKljXQu35mvbQinynaJ2XqZ5gsXNoOKv8DCAkQABoMNjM3NDIzMTgzODA1IgwCdLkQvq4VTBNCSsMq3AOieLAbm1xf6PdpHDBgXA9mMXk08dsmjmAeHjIRA89A0kmKFPrzshKe5YJtgDMeg4Zz%2B%2B9AwJfCr0GydY0n4%2FIr%2B5MUfQ2cLpGKCHw65Qjq%2FGGHWV%2FfNMaR0uoZ%2FYl1%2ByfH0Kj65xhBB%2FNifjiOLt%2BaLxvEw7HVNbn7RB0Zu4ihjnD8J9foc9n2yedMrf%2FLxdmJ1abRdABwnhbQfnwfzN6WbfPOzrHvflmwSZb32ucxc4s4QdNBjNTPRRcect8cjt2B4Zv05k4xTAGg%2Fxb8WwkpJaLzCoKjmi06rtbv6sYL0B8lv2JX0BznnDJE7CuBBNJIa2xarbD51cOgxlMhawBAeGZ1Z5cflLTx%2BFnDWtNaUVORI9X%2F2%2FdSZOnNudpSx0khkYZHCeYOzXvg1Qtnpmx4U3jsHaHmbPRa8Z8c%2BRYZjWyq%2Byi65O8d8ag6x8J%2FA89lfXHcqzsRybLYhTEzY%2BwexfXoCjgFU3doVd7kul4X4KMp2PSFzRdshwLWq7mkel2qRNoa6ewM0zlNkuUt59izweoxUOsG7SdWB6y8UqKXXrqWdEjClpm4A0CncOisZ%2BOdPS%2FPULH0v37m8tEUWF8%2FxiL7O2TcOqPy6zFUaO%2BCLd%2FmlQVJFKBjeI6ZVzCYm8zPBjqkAR%2BJcbJw3rUkZo4YiiceUpGL5ox0Tv0YwKc3K7lKisSEIRE%2BhY15mnt%2BSDHc9%2BvABrt6ujvjGaWlRDKRW82FeIVrBvesSp2SBnOuCara%2FrZmj2N5T%2BoYzZGzMLbXxXame6YYJjIfYGobe5LeEaWXHO9xRAKgdCIrbuHbxcmapVmJu1sMCVuLozB4rWgaFJSkkhnwnojTk%2FanXyr19YaDzWEoOaQr&X-Amz-Signature=c0a1a2dc39e100969426607a764709288874ccf193a0ad7204c0d2cbe629aad3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUJDYECR%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCmCTO4x4R%2B65YIA9AcK1S7PhpaNYSiZM3TbGGLPx3MvAIhAIlbrU4ym7l489hKljXQu35mvbQinynaJ2XqZ5gsXNoOKv8DCAkQABoMNjM3NDIzMTgzODA1IgwCdLkQvq4VTBNCSsMq3AOieLAbm1xf6PdpHDBgXA9mMXk08dsmjmAeHjIRA89A0kmKFPrzshKe5YJtgDMeg4Zz%2B%2B9AwJfCr0GydY0n4%2FIr%2B5MUfQ2cLpGKCHw65Qjq%2FGGHWV%2FfNMaR0uoZ%2FYl1%2ByfH0Kj65xhBB%2FNifjiOLt%2BaLxvEw7HVNbn7RB0Zu4ihjnD8J9foc9n2yedMrf%2FLxdmJ1abRdABwnhbQfnwfzN6WbfPOzrHvflmwSZb32ucxc4s4QdNBjNTPRRcect8cjt2B4Zv05k4xTAGg%2Fxb8WwkpJaLzCoKjmi06rtbv6sYL0B8lv2JX0BznnDJE7CuBBNJIa2xarbD51cOgxlMhawBAeGZ1Z5cflLTx%2BFnDWtNaUVORI9X%2F2%2FdSZOnNudpSx0khkYZHCeYOzXvg1Qtnpmx4U3jsHaHmbPRa8Z8c%2BRYZjWyq%2Byi65O8d8ag6x8J%2FA89lfXHcqzsRybLYhTEzY%2BwexfXoCjgFU3doVd7kul4X4KMp2PSFzRdshwLWq7mkel2qRNoa6ewM0zlNkuUt59izweoxUOsG7SdWB6y8UqKXXrqWdEjClpm4A0CncOisZ%2BOdPS%2FPULH0v37m8tEUWF8%2FxiL7O2TcOqPy6zFUaO%2BCLd%2FmlQVJFKBjeI6ZVzCYm8zPBjqkAR%2BJcbJw3rUkZo4YiiceUpGL5ox0Tv0YwKc3K7lKisSEIRE%2BhY15mnt%2BSDHc9%2BvABrt6ujvjGaWlRDKRW82FeIVrBvesSp2SBnOuCara%2FrZmj2N5T%2BoYzZGzMLbXxXame6YYJjIfYGobe5LeEaWXHO9xRAKgdCIrbuHbxcmapVmJu1sMCVuLozB4rWgaFJSkkhnwnojTk%2FanXyr19YaDzWEoOaQr&X-Amz-Signature=5d45b7c9011170a756f8eda3c6f62102f4c920d5cf832eefaab9081ce4fcdddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

