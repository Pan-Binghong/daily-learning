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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTTQMKP2%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGT%2FitrdzXkS1KCR1fpZK4LYIuQlpf2iQhkj8JzwA0M%2FAiEAnFDGnugCwbQGWbxN9BfCA6ZyTrUKoNgJaEaXzoWpq44qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMEL%2BzanMM4Vcin1VyrcA29cfQXcF0NVvJa8VKKCxZRA6UcwhzqFUBBq0Pxf0zksH1%2Blz17FjpMKGjHYjQXulyClnQgE0g9NTUlpMRTjo1UPtkpWbf833AmIs2s%2BnUAntULpaL8LQejqU8BXdkjyOaumYfygMKy2vPSXT7QtY1NB6gWrzQhbBIIEHcPeKCcp20cVGR%2F5ESlT6GliwW%2F6%2BvusaXrjEYDDK9bN47qxm2Oq4QDmc5caR1HYMK6O7%2F25ce%2FVXb0fCEf6W42JZP87M%2B6K2zulUwBPLKoUrSXQJiTMZMnR%2F2xYa%2BPuD3eoAJ2OV983815FxZ0fGKCzde%2BxtQUSA%2Fcd3q9lUq32sXor2ZvKBlhpc%2B1TdsEL%2BLnJVjYVuXSKT4Z4yanRzmZrm9RopEcsKtYL26KMXcFONHLv%2BEG%2BSmW5Kb9Z9OloP55zZAdjq1oZ85DwpPsHl8RuzCwDCLeEd2FziiPv6LjgC7AuLxN0kciCojYGZEU8jwtz2L3BEFQkk6qfIvHaIDX5URQxDwBn2T729KbCe84dvYTZQq6bXnFI6xpnk1wFbpepbRHlN0GQqzYNs0OCFB8hjBKV7qQixbteP%2BBKARG9L3DiiteCw4DW9qr4yVMRDDmPsQ%2BWlsRCNshpAjSf2Ui8MKmxzM4GOqUBOlXyDLCVRPjrFFj6iq8KmgAKLqdRO2LZCNfE5iS3xgh%2BKsAGtwAsamihsnKhjW7PTdW1Ux3HZxEi%2F3G9KvJNoYTxf7I6fu84H48Y65yrvA2PzZNufnfVlHapnDTtwHSFg8fp8YJV20kAfFvTcfI4jR1x59Cjj5VxtEBSOI3KdwFxEgZTEptV3urhDY58moEbZ25uxIP%2B1D4VLEAZKjZ%2BnKkxXMzw&X-Amz-Signature=f49d298d420296c0916292856350c236dbb978da389859a3a07d71ee88a84724&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTTQMKP2%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGT%2FitrdzXkS1KCR1fpZK4LYIuQlpf2iQhkj8JzwA0M%2FAiEAnFDGnugCwbQGWbxN9BfCA6ZyTrUKoNgJaEaXzoWpq44qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMEL%2BzanMM4Vcin1VyrcA29cfQXcF0NVvJa8VKKCxZRA6UcwhzqFUBBq0Pxf0zksH1%2Blz17FjpMKGjHYjQXulyClnQgE0g9NTUlpMRTjo1UPtkpWbf833AmIs2s%2BnUAntULpaL8LQejqU8BXdkjyOaumYfygMKy2vPSXT7QtY1NB6gWrzQhbBIIEHcPeKCcp20cVGR%2F5ESlT6GliwW%2F6%2BvusaXrjEYDDK9bN47qxm2Oq4QDmc5caR1HYMK6O7%2F25ce%2FVXb0fCEf6W42JZP87M%2B6K2zulUwBPLKoUrSXQJiTMZMnR%2F2xYa%2BPuD3eoAJ2OV983815FxZ0fGKCzde%2BxtQUSA%2Fcd3q9lUq32sXor2ZvKBlhpc%2B1TdsEL%2BLnJVjYVuXSKT4Z4yanRzmZrm9RopEcsKtYL26KMXcFONHLv%2BEG%2BSmW5Kb9Z9OloP55zZAdjq1oZ85DwpPsHl8RuzCwDCLeEd2FziiPv6LjgC7AuLxN0kciCojYGZEU8jwtz2L3BEFQkk6qfIvHaIDX5URQxDwBn2T729KbCe84dvYTZQq6bXnFI6xpnk1wFbpepbRHlN0GQqzYNs0OCFB8hjBKV7qQixbteP%2BBKARG9L3DiiteCw4DW9qr4yVMRDDmPsQ%2BWlsRCNshpAjSf2Ui8MKmxzM4GOqUBOlXyDLCVRPjrFFj6iq8KmgAKLqdRO2LZCNfE5iS3xgh%2BKsAGtwAsamihsnKhjW7PTdW1Ux3HZxEi%2F3G9KvJNoYTxf7I6fu84H48Y65yrvA2PzZNufnfVlHapnDTtwHSFg8fp8YJV20kAfFvTcfI4jR1x59Cjj5VxtEBSOI3KdwFxEgZTEptV3urhDY58moEbZ25uxIP%2B1D4VLEAZKjZ%2BnKkxXMzw&X-Amz-Signature=885220ff18c4f0616000139b1c7b5459060d4f136b6f1a63614efc0844fca8a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

