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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CARX7WW%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFP0YS3D9hR9BxVnE6WkyWp7Iz%2F%2BEaIEYKrdDuvpRrIdAiAoakc0KemnzPGGslDk7JHYXpsmVhHpnVhBG3Z%2BMQLg6ir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMQjWfypytwumtTB1OKtwD%2FyDFE1NmrPw5QUSggqu5g3w3Xbuce4L83gAJ7FjPGE%2BMPk%2B7iC4mCT4gIBqZWyr9Km3%2FsTJO6UuuEVAbbPQSNyQsVdK05srkhiohSG3Mguu3z4T9kkqT4QZR7HA0OwZQLHo7rc69PSeQkgHPbKHvA6%2BP1La0sTL1R22d6loaIkw3sa1%2B63VeawL7YLzyMS%2B8ygD5cqq0h3y05GNiyRcfepE2rLFyrhW4XNoHrXPv%2FCAaPdMGAv3q31mMlolP%2Bu67keKTmtr1%2F5lkU7oOKW60G4aD53La%2BulUhngjfmxCfTdlABOGJVOg%2Bb%2BkQVUTSQmgdFR%2FB4pnqWTLIxqiFXi5rS4XdkzuWYqKY52G6Wm2t2jc2klbGsDHUbVgiuJWH33CHNg0au0NYbK%2FTQM8WmQalZE1nx6vkPQuZ36x9WSHTGX%2F6TuxNqn4%2BVxktgzI0xj2LR588yYNSMLYp%2BRUkeyT0j3F0me2%2BdX4JDycyRkOsrdaHY43FpGhPA07b3LULgYRxrIq5VhhdEBeVxbvFDZMV3%2BT3PuX53WotacoxzK9huXZIrvEpjatWLcSP1Esx9L2iugsJEkgPxy%2FS3khjzmKju7Imy4n63hr6MTkPmAVgLsAasabfGl28DWmMUYwn%2FLZzAY6pgEx4akjksJ1nB3%2Fi%2BqOevkUw56P4En6%2FAn%2Fmr8AkaGmi8pCsKqLQicK3Q8uA3zD4n5tVNaPn2OvlO%2Bd5sx%2F4RCwNDw0V68YNsxDIpvLweqso3V%2B%2BNOx0hfcyE1KBARts%2FR5%2BEELGQeH4KdeyvYk7gbXMn2ALbW4YgW9BltBdHJ%2BxCwXU%2FXlGcZI9Jgk8Y8fik99cel7AT6MEKfwDmkJ3FlCqzoJ%2BaMr&X-Amz-Signature=f49e748227ab3dbbc65b19e1673f23da58bb3cdcb1aa1cc70b36695b6f7cbbdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CARX7WW%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFP0YS3D9hR9BxVnE6WkyWp7Iz%2F%2BEaIEYKrdDuvpRrIdAiAoakc0KemnzPGGslDk7JHYXpsmVhHpnVhBG3Z%2BMQLg6ir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMQjWfypytwumtTB1OKtwD%2FyDFE1NmrPw5QUSggqu5g3w3Xbuce4L83gAJ7FjPGE%2BMPk%2B7iC4mCT4gIBqZWyr9Km3%2FsTJO6UuuEVAbbPQSNyQsVdK05srkhiohSG3Mguu3z4T9kkqT4QZR7HA0OwZQLHo7rc69PSeQkgHPbKHvA6%2BP1La0sTL1R22d6loaIkw3sa1%2B63VeawL7YLzyMS%2B8ygD5cqq0h3y05GNiyRcfepE2rLFyrhW4XNoHrXPv%2FCAaPdMGAv3q31mMlolP%2Bu67keKTmtr1%2F5lkU7oOKW60G4aD53La%2BulUhngjfmxCfTdlABOGJVOg%2Bb%2BkQVUTSQmgdFR%2FB4pnqWTLIxqiFXi5rS4XdkzuWYqKY52G6Wm2t2jc2klbGsDHUbVgiuJWH33CHNg0au0NYbK%2FTQM8WmQalZE1nx6vkPQuZ36x9WSHTGX%2F6TuxNqn4%2BVxktgzI0xj2LR588yYNSMLYp%2BRUkeyT0j3F0me2%2BdX4JDycyRkOsrdaHY43FpGhPA07b3LULgYRxrIq5VhhdEBeVxbvFDZMV3%2BT3PuX53WotacoxzK9huXZIrvEpjatWLcSP1Esx9L2iugsJEkgPxy%2FS3khjzmKju7Imy4n63hr6MTkPmAVgLsAasabfGl28DWmMUYwn%2FLZzAY6pgEx4akjksJ1nB3%2Fi%2BqOevkUw56P4En6%2FAn%2Fmr8AkaGmi8pCsKqLQicK3Q8uA3zD4n5tVNaPn2OvlO%2Bd5sx%2F4RCwNDw0V68YNsxDIpvLweqso3V%2B%2BNOx0hfcyE1KBARts%2FR5%2BEELGQeH4KdeyvYk7gbXMn2ALbW4YgW9BltBdHJ%2BxCwXU%2FXlGcZI9Jgk8Y8fik99cel7AT6MEKfwDmkJ3FlCqzoJ%2BaMr&X-Amz-Signature=4fd43d31db89340cc31cb8bc8d2da5cd9a2d455d37c124340908db7d4de56da7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

