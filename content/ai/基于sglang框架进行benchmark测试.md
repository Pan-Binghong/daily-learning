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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z76VLRZQ%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIHZVZ78z63YvehD2BnsgH%2F8BgwNrxbAUmRp2y1Vki74aAiEA%2F%2B4UrE7UvN%2BV1ZF9a6XJ%2BoL%2F3FJX7KoE%2BP%2BpAd4LLUkq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDLw44bxumE7lHCQ0%2BCrcA3qVYzvd4tKbh%2FKAqeozuhjNkM9anpCAgAWJDL4QKOwC8mYG6de%2BU4OP6JvSZYFrisCljdTEXeNptAt6f6RXLZi5TB00ZQFTl0XHA8ESBCMUjv6%2FwdR7EP6hyc7mbhX%2B%2BOoQvXI4CQwloCRv0VgHQ3OxL73XFWj7tilE1QX0Ivafr6RFA63iPvQQqHOfzkC8egd%2FCNLY4vA%2F3ILZ%2BW%2FgP2S9%2BiMZELXAlhQYYU0JM0pVq%2FD5W8WSCEYTmxFVCsMZLc2HAFWTTAXUNIPWGC6WJ3slEcTQCDKTX%2FDcEy9tgl8IhSqj0eavK5I%2FVgSu8WtYMkbLK3ufiKyEYJbGB7fMNMUMJVllNwsHkcK7UM8UYCEmadrPKtuenDQFgzRYL6eavgjFaIgJTWwEa44JzR8VP4hlGP4geC7HU6Cy%2BCFEMHQJptE4CmnNMJcQwLzcdwCzqH0vy7YDfciWzVl06pAknDPAMRaBLq4BArr6gf0zrc1rtsluB9e%2FuK86tl%2FfSAHUDsoFldz9NURcltmhIA5WppAXcvqproO56Uy1rc8wvU7OXvcCpiIRTqqLgFKA5wSSbjfmkInHhcxCBAwFaXwU7RRO5qbNEvNqKalQxfsbka9UQFFxfa4sl82V5KjLMLP8p8oGOqUBRy%2BnMUATJX7%2FR47jxxSx77Axc1lXhvQ2tIWWPHkyCr%2FcIWSPBJTCt2JxebPJufNi14LvdkpHPI81AMz6Xx8kcvuZirTwlP1nq9rfBH00NlXqonLsG96LqoPUeXdfN4irFQFIFsk3J5H0Y2iJmKQgHkTLESqPEQy%2BVwzICH8PbdoMeGvhvGth1m7eTWmYdvabogpXoWTK7qYY%2BtYey%2FaGZUk6SO3T&X-Amz-Signature=257c8e3ad22d96cf36a08150e160455b752103ee4c0b595674358bd7623a69f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z76VLRZQ%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIHZVZ78z63YvehD2BnsgH%2F8BgwNrxbAUmRp2y1Vki74aAiEA%2F%2B4UrE7UvN%2BV1ZF9a6XJ%2BoL%2F3FJX7KoE%2BP%2BpAd4LLUkq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDLw44bxumE7lHCQ0%2BCrcA3qVYzvd4tKbh%2FKAqeozuhjNkM9anpCAgAWJDL4QKOwC8mYG6de%2BU4OP6JvSZYFrisCljdTEXeNptAt6f6RXLZi5TB00ZQFTl0XHA8ESBCMUjv6%2FwdR7EP6hyc7mbhX%2B%2BOoQvXI4CQwloCRv0VgHQ3OxL73XFWj7tilE1QX0Ivafr6RFA63iPvQQqHOfzkC8egd%2FCNLY4vA%2F3ILZ%2BW%2FgP2S9%2BiMZELXAlhQYYU0JM0pVq%2FD5W8WSCEYTmxFVCsMZLc2HAFWTTAXUNIPWGC6WJ3slEcTQCDKTX%2FDcEy9tgl8IhSqj0eavK5I%2FVgSu8WtYMkbLK3ufiKyEYJbGB7fMNMUMJVllNwsHkcK7UM8UYCEmadrPKtuenDQFgzRYL6eavgjFaIgJTWwEa44JzR8VP4hlGP4geC7HU6Cy%2BCFEMHQJptE4CmnNMJcQwLzcdwCzqH0vy7YDfciWzVl06pAknDPAMRaBLq4BArr6gf0zrc1rtsluB9e%2FuK86tl%2FfSAHUDsoFldz9NURcltmhIA5WppAXcvqproO56Uy1rc8wvU7OXvcCpiIRTqqLgFKA5wSSbjfmkInHhcxCBAwFaXwU7RRO5qbNEvNqKalQxfsbka9UQFFxfa4sl82V5KjLMLP8p8oGOqUBRy%2BnMUATJX7%2FR47jxxSx77Axc1lXhvQ2tIWWPHkyCr%2FcIWSPBJTCt2JxebPJufNi14LvdkpHPI81AMz6Xx8kcvuZirTwlP1nq9rfBH00NlXqonLsG96LqoPUeXdfN4irFQFIFsk3J5H0Y2iJmKQgHkTLESqPEQy%2BVwzICH8PbdoMeGvhvGth1m7eTWmYdvabogpXoWTK7qYY%2BtYey%2FaGZUk6SO3T&X-Amz-Signature=4041f4aa9ac84c055a074d1c85ff526d2921815088482d43f086eab1f6719fae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

