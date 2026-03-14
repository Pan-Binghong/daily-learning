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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYE2D5SQ%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxrNMRw0YWkamWIcaHN2I18t8SM6kI7HvWO34hbva2%2BAIgfyXjc2SMPYNNKWQ%2F%2BSd9Y4bO9yhZHaSPIBNJn%2BDkEBQqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG0PV8CZx2fK3X0dXCrcA5v%2BMI7nKWp420bbhdw7pATsnJtO70gUfIQAGqaxaWBePUtl2dXepXuOaoFvAO003bzn6lE%2B3wpch3RF7KLl9WcEBZv%2Be0vUsbDxwwBxJtaN%2FOzrPS%2Bwn%2Fk0JovlCkQBxx83UPta5KYdMJfg0d9jTcuzN6QwMa6w01fHu%2Bn6PxdLX3WVeKdCweQWDNoGfL%2F5RvEZt9E8LEIviTyzdUBTywj3jfXrOZSMsoLXEHxF7w7Eff28iFWgs24B8VRC%2Fprbk4V81fMiyM7YMlJ5%2Fku910J3Vo%2B35fvIRggqeWhW%2BuMq05ID%2B5D11CLFZJas4%2B7ErIllwi03dPLTRC6DF7hqlBbdtCJdebUR2GgyBH5%2FS3wkmQnkOECaKcxx9AYuEx7csrpUjFzjcCPNeF%2FCFvVdUEjeo7MO3oMfmhaHR7%2FdXmUeKOQrin0B6qfwqNDqf5ZGBYeVjUrhLxKTfx7J8BDetMuzqlm1gitA5xfropSdxPxcRZd%2FOsHws1MTp9zaBJcTwHjAcCxX8nfKCQLCmbmzFyYGzeay8W3YLr0IwR7q5PMERwTuCZnsXaqxExUxdzkAdOzvJ%2ByIFkzZo2nBOqkeXjRtkrklKT36Ni2uCdvmuqinYFRAS9N9uncE6p%2BhMNqC080GOqUBWXrHo2AmdcTClU8wQxCm9e3Y%2BN7PEK66%2FpMmTdzS5nDm4W8q5WWg29oUIaEi0lB242Sq14flUQ3g%2Bp9qkXpvhB7H6UWvA05LrnSOi9Jgwk%2FKL8PIkNFg2tZKh1nHrSM8uB%2BkPPan9VBMB6hEXndOOZrXayAwZTBVLmtA34kTHBlmC6bpxVFeAVktezkweUWPRGrZ5jTZeLtD7z4%2FCS7Ut3N%2B0N6Y&X-Amz-Signature=34765f5d511abc4511da1cd3d67022cc9740365a71f6745b447fc037eecb7916&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYE2D5SQ%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxrNMRw0YWkamWIcaHN2I18t8SM6kI7HvWO34hbva2%2BAIgfyXjc2SMPYNNKWQ%2F%2BSd9Y4bO9yhZHaSPIBNJn%2BDkEBQqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG0PV8CZx2fK3X0dXCrcA5v%2BMI7nKWp420bbhdw7pATsnJtO70gUfIQAGqaxaWBePUtl2dXepXuOaoFvAO003bzn6lE%2B3wpch3RF7KLl9WcEBZv%2Be0vUsbDxwwBxJtaN%2FOzrPS%2Bwn%2Fk0JovlCkQBxx83UPta5KYdMJfg0d9jTcuzN6QwMa6w01fHu%2Bn6PxdLX3WVeKdCweQWDNoGfL%2F5RvEZt9E8LEIviTyzdUBTywj3jfXrOZSMsoLXEHxF7w7Eff28iFWgs24B8VRC%2Fprbk4V81fMiyM7YMlJ5%2Fku910J3Vo%2B35fvIRggqeWhW%2BuMq05ID%2B5D11CLFZJas4%2B7ErIllwi03dPLTRC6DF7hqlBbdtCJdebUR2GgyBH5%2FS3wkmQnkOECaKcxx9AYuEx7csrpUjFzjcCPNeF%2FCFvVdUEjeo7MO3oMfmhaHR7%2FdXmUeKOQrin0B6qfwqNDqf5ZGBYeVjUrhLxKTfx7J8BDetMuzqlm1gitA5xfropSdxPxcRZd%2FOsHws1MTp9zaBJcTwHjAcCxX8nfKCQLCmbmzFyYGzeay8W3YLr0IwR7q5PMERwTuCZnsXaqxExUxdzkAdOzvJ%2ByIFkzZo2nBOqkeXjRtkrklKT36Ni2uCdvmuqinYFRAS9N9uncE6p%2BhMNqC080GOqUBWXrHo2AmdcTClU8wQxCm9e3Y%2BN7PEK66%2FpMmTdzS5nDm4W8q5WWg29oUIaEi0lB242Sq14flUQ3g%2Bp9qkXpvhB7H6UWvA05LrnSOi9Jgwk%2FKL8PIkNFg2tZKh1nHrSM8uB%2BkPPan9VBMB6hEXndOOZrXayAwZTBVLmtA34kTHBlmC6bpxVFeAVktezkweUWPRGrZ5jTZeLtD7z4%2FCS7Ut3N%2B0N6Y&X-Amz-Signature=aadc3609e1b1d846c21ea1f73e82fe75767367247f9f96dd1bca748dd7d24187&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

