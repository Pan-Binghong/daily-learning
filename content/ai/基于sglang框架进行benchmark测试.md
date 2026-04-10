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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NBHPGD4%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIB%2FLuvPweaw8CGywrJudpLIiYkmC49XAjjbHaGgW03joAiEA7UB3iwZKYF%2B9hUjt%2FQNrpHGX1tENn%2Bq4be6xLIhHBBgq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDLXY3D617j7QL1r1cCrcA9a1yr3RC7OQX0sRQrT8Wd5CYtKJsDXxpmTNHjYVi06n%2FnRIoIaXqcYn9HsIeuXgtGVaK4vj0AIw0Fp%2Fwlrq%2FryuMO3ci8eSghn62eLn1qbQ%2B%2BwGv%2BR31%2F5xh24mQDMw0hHq3C4%2BFhJSue0BDqEQPbYSIEVICCWIDEnrv43wRN1NYLgygpgSOUSVtA2p7KsJFjNSduNK9McPGTz0XaZCQowmwhjB8aD28TYRkdOOFC2uMBL6uwC0HsWLts%2BGOdTSx2%2BnHqbBYZBejGBX%2Fhr1GDr5kaVyTrxKuFcuIPUnRSN2hzC6xjnRAXgOJfiQsYL%2BK6XtYEFLIfxDZqNKTx7jzUipVaqb6TSZEBT9pMkZ6rM08Q1lwBoLYv9DYiUrXQwzmCCuQQQ27F55mPi%2FKnvbAJyN801iL58Jmn%2FaBQJPSJ5vnb9Zi3i5y8%2BF9q33kRoGyL1zplccP8BgNd4c21BH4vVZ%2B1LE%2BOVNowfHwoHDNaSNBwWzP%2FYMtNOYN2zFkiZZX1CtoF73YV%2BPJag6MB1WFlAWn4CV4KF2jz0qaTybUat9q%2Bdvsc7emz2hVcFO%2FJjWnoWgREACKQUJddOwBVIGF5%2FDTXWhZoBAmHTvUrYchDDMy975v%2BfOY7PA2psJMO7E4c4GOqUBoH8QhjUVbt6iTlbaHELdcciJqCaAcRpyqiooJcNsdsSNumi%2BHSG8lXkaPBFQiIMOyWIHKVM3pvDMrU1LeCsBGRDuJg1Xlls8Jht9S%2Bt2wnpsv2onpBfU6JtRAusgzT2swORikmuJJRQUeDrE2EZFuy%2F3Fo7u%2BF%2FVpSrWaDBu4Meh6InG2HkFlGHut6yzekcf7z7avPNZg96xUXE3bV%2B0tWMlCVmq&X-Amz-Signature=4d450f30314f3426b712f5e9088ecc89bdda1814aacc953f11d109c61a502cdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NBHPGD4%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIB%2FLuvPweaw8CGywrJudpLIiYkmC49XAjjbHaGgW03joAiEA7UB3iwZKYF%2B9hUjt%2FQNrpHGX1tENn%2Bq4be6xLIhHBBgq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDLXY3D617j7QL1r1cCrcA9a1yr3RC7OQX0sRQrT8Wd5CYtKJsDXxpmTNHjYVi06n%2FnRIoIaXqcYn9HsIeuXgtGVaK4vj0AIw0Fp%2Fwlrq%2FryuMO3ci8eSghn62eLn1qbQ%2B%2BwGv%2BR31%2F5xh24mQDMw0hHq3C4%2BFhJSue0BDqEQPbYSIEVICCWIDEnrv43wRN1NYLgygpgSOUSVtA2p7KsJFjNSduNK9McPGTz0XaZCQowmwhjB8aD28TYRkdOOFC2uMBL6uwC0HsWLts%2BGOdTSx2%2BnHqbBYZBejGBX%2Fhr1GDr5kaVyTrxKuFcuIPUnRSN2hzC6xjnRAXgOJfiQsYL%2BK6XtYEFLIfxDZqNKTx7jzUipVaqb6TSZEBT9pMkZ6rM08Q1lwBoLYv9DYiUrXQwzmCCuQQQ27F55mPi%2FKnvbAJyN801iL58Jmn%2FaBQJPSJ5vnb9Zi3i5y8%2BF9q33kRoGyL1zplccP8BgNd4c21BH4vVZ%2B1LE%2BOVNowfHwoHDNaSNBwWzP%2FYMtNOYN2zFkiZZX1CtoF73YV%2BPJag6MB1WFlAWn4CV4KF2jz0qaTybUat9q%2Bdvsc7emz2hVcFO%2FJjWnoWgREACKQUJddOwBVIGF5%2FDTXWhZoBAmHTvUrYchDDMy975v%2BfOY7PA2psJMO7E4c4GOqUBoH8QhjUVbt6iTlbaHELdcciJqCaAcRpyqiooJcNsdsSNumi%2BHSG8lXkaPBFQiIMOyWIHKVM3pvDMrU1LeCsBGRDuJg1Xlls8Jht9S%2Bt2wnpsv2onpBfU6JtRAusgzT2swORikmuJJRQUeDrE2EZFuy%2F3Fo7u%2BF%2FVpSrWaDBu4Meh6InG2HkFlGHut6yzekcf7z7avPNZg96xUXE3bV%2B0tWMlCVmq&X-Amz-Signature=0934be360ada144a84e533b1cb514dc81fbf4c778ac7870ab545956e64449219&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

