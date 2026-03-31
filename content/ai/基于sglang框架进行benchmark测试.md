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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD7EQO7G%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDtT2a1cM3pxlkGPpYeedC%2FjjOHYv%2F3f%2Bi%2BqfsfmbzEXgIgOzfXZE5Yh3rLkpn7Uenq0G1%2FUmSFdC79xGW7KIajUn4q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDOeNdq8DaHWUXSQTRCrcA8mIf7O8jEhaJ6%2FP7KJnVyFarMWT98RnKQnOylOYkNwh2dgiDhC%2FFnarGH2fSG1s6QgkoOnOi8UuYIpIk60kypYbxY69ph%2FR9uzGP%2FHU7CoHngbwxyws6h4NEO9tn%2BtxFneUXN74TPJjb1%2F62Eg02u8JWHUXZKrcwZMvoqohly45r7UPscbhNozRb%2BrIEdG9XIv6zowySX13KhC6y4gEHwT2GMX95VpoU3%2Bry3W6QVm8TcU9hXQbtzdmw0YCTY3TrTRvxlsOGAU7QmlOjK%2F7tLbUxLTYP8SvFKym8s01nZW%2FCkeZjCVIhMsSS2%2FKveP8WEYkHFtm4W8WWkDfPPuuFvaWEt1%2B1NVatAWWUtXozN%2BFjngm%2Bp25Jmc0EmAtHJOLEWrryjvqEX74VaTXtWEx62tYxtNUWvm0UrH5nDisoMYA3klnhY1KUuk5pwldnqGXTD0guSrlUWd5uq7ITs9XVJMyBZadDjHBsGnpNHkTn2dVXIicfmPqqoT2fTYtvOW%2FvhAeo9oZD2WW0FSXBTt%2Fui9HmrpPDL5a08Yz47SUWghRr6CyBTedwMge8du2Tsg5Qvq1QuE2eUJHZJey4db509T9WbKZLVuy3noboYn7aimuFkB9IVbcr01bf5fmMO3vrM4GOqUBTb7yA8L6cAHxu0PBIuxEPxXd1Vx3lpL51HAecs4J7zdu979aU4A05gKUoXYu7kEDppy282k4rk8olcSvGxXvN8lDJIZmjXAummiOdlX639%2FVQDxW14Yw9SXjviUzJRNLp7%2Bkjlu8h4fyx%2BmCHmM3D99QKjAPA4alaChVsJWtHyIw%2FRiuQa4W%2BgSeYdEi4oKfWpsBiGtjgdQUO86tg5%2FLzop8KOTz&X-Amz-Signature=0c94e015d78c5ba0ba2c629b5d67746069baf4f6885573be4233f0306374735a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD7EQO7G%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDtT2a1cM3pxlkGPpYeedC%2FjjOHYv%2F3f%2Bi%2BqfsfmbzEXgIgOzfXZE5Yh3rLkpn7Uenq0G1%2FUmSFdC79xGW7KIajUn4q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDOeNdq8DaHWUXSQTRCrcA8mIf7O8jEhaJ6%2FP7KJnVyFarMWT98RnKQnOylOYkNwh2dgiDhC%2FFnarGH2fSG1s6QgkoOnOi8UuYIpIk60kypYbxY69ph%2FR9uzGP%2FHU7CoHngbwxyws6h4NEO9tn%2BtxFneUXN74TPJjb1%2F62Eg02u8JWHUXZKrcwZMvoqohly45r7UPscbhNozRb%2BrIEdG9XIv6zowySX13KhC6y4gEHwT2GMX95VpoU3%2Bry3W6QVm8TcU9hXQbtzdmw0YCTY3TrTRvxlsOGAU7QmlOjK%2F7tLbUxLTYP8SvFKym8s01nZW%2FCkeZjCVIhMsSS2%2FKveP8WEYkHFtm4W8WWkDfPPuuFvaWEt1%2B1NVatAWWUtXozN%2BFjngm%2Bp25Jmc0EmAtHJOLEWrryjvqEX74VaTXtWEx62tYxtNUWvm0UrH5nDisoMYA3klnhY1KUuk5pwldnqGXTD0guSrlUWd5uq7ITs9XVJMyBZadDjHBsGnpNHkTn2dVXIicfmPqqoT2fTYtvOW%2FvhAeo9oZD2WW0FSXBTt%2Fui9HmrpPDL5a08Yz47SUWghRr6CyBTedwMge8du2Tsg5Qvq1QuE2eUJHZJey4db509T9WbKZLVuy3noboYn7aimuFkB9IVbcr01bf5fmMO3vrM4GOqUBTb7yA8L6cAHxu0PBIuxEPxXd1Vx3lpL51HAecs4J7zdu979aU4A05gKUoXYu7kEDppy282k4rk8olcSvGxXvN8lDJIZmjXAummiOdlX639%2FVQDxW14Yw9SXjviUzJRNLp7%2Bkjlu8h4fyx%2BmCHmM3D99QKjAPA4alaChVsJWtHyIw%2FRiuQa4W%2BgSeYdEi4oKfWpsBiGtjgdQUO86tg5%2FLzop8KOTz&X-Amz-Signature=e18a6b9e3820cb8f888ebf8a77a9c0e327fcb1292528e8c997731de8bc734e6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

