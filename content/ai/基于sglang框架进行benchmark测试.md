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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ME6HZGF%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhTx5Lj4kJJcWWDQImqU6EREsaiceOYr%2BNwgRABNnDTAIgG4E9gbEnqZ78kbjpIZUtynSfBKk5K9dPQLBDJ0xpCbcqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFGHpngX5E3GYXKhDCrcA4PsA%2BW3nlrZDgSJHkX7zvUxm8r7HAXMyUcp7IkRonrtea0f7oARLXA44qnLBfxqUjp64fYY1FFR%2FD%2FA3W8%2BHvVRdRzTWtOAdEts5vVRNbQD1xmy%2FGk%2BSs8r%2FN97nAL6cK0wkJEg38mcZfh3uorWj%2F0NcY2sLE28Xc1nJclTC4QBnxvezoMNHkr7wpW9S1GL90RH6nVTqSNFZJ1cxhZ8RlnB8C4d3BWlHVU9ecnAlyU%2B9akg3WyviizOoWz9fTmkUYdpEGsPVLZUcRQJLFF7cux8hJShw08h%2Fl3%2F6iWL7SqQ3C8sOxVAbhaZ6mSwEASbn7NSOr3aHH8XTSnnV3ZYIEOpvqz4CAcVSXsQem%2BmnXymZIy6WW4hBdsDTOj%2F60VVJ4qBeTLdPc2JjRjBe3DRXA0oBU0%2FXZ83bsMFy32y%2F%2Fi3nloDyHv45rR%2FexhV6OU53azKWd7Ce0%2BprkFHIQnuhIQXxNWmy395fWL7v0h8gwp2o6BSwZ%2B%2F%2FUxfArtxoCY12it2Wq8o4iF%2FgFG3tHou%2FWUo084EfdnxxzAOPF7oobpEMuGT291DIcTg5ED5nuBLvXhtXbm%2FJbdLMfh2oKZ0qOgQdUtgNpxhRNp7FU5zSwO42E61LU6qlsSkzrDyMOrlwc4GOqUBn15cGyfPV2c2ou%2FX9VnswUF0ARXJG04614qZ1s5fI6fYqazhyYOHVqBF9WUekk8xRuA51t1zOojjGSRFpcJpNSPy0exYzxV3aTlvGNotxZd6RqAJ3I%2BdbtYhJzpUMZOlWiMfYbATgrfqm7wiNUbi8TgytsFnDFQRQg2WujzU0JrcVh5pkCz3FgHCkFMCbyvLafnWH81Wn7G9n0vui1Oi5%2BdMN1ID&X-Amz-Signature=73011d36dda00d707b07d64a348e0d69a6e7b8a490108ac0a091c25f1113c082&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ME6HZGF%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhTx5Lj4kJJcWWDQImqU6EREsaiceOYr%2BNwgRABNnDTAIgG4E9gbEnqZ78kbjpIZUtynSfBKk5K9dPQLBDJ0xpCbcqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFGHpngX5E3GYXKhDCrcA4PsA%2BW3nlrZDgSJHkX7zvUxm8r7HAXMyUcp7IkRonrtea0f7oARLXA44qnLBfxqUjp64fYY1FFR%2FD%2FA3W8%2BHvVRdRzTWtOAdEts5vVRNbQD1xmy%2FGk%2BSs8r%2FN97nAL6cK0wkJEg38mcZfh3uorWj%2F0NcY2sLE28Xc1nJclTC4QBnxvezoMNHkr7wpW9S1GL90RH6nVTqSNFZJ1cxhZ8RlnB8C4d3BWlHVU9ecnAlyU%2B9akg3WyviizOoWz9fTmkUYdpEGsPVLZUcRQJLFF7cux8hJShw08h%2Fl3%2F6iWL7SqQ3C8sOxVAbhaZ6mSwEASbn7NSOr3aHH8XTSnnV3ZYIEOpvqz4CAcVSXsQem%2BmnXymZIy6WW4hBdsDTOj%2F60VVJ4qBeTLdPc2JjRjBe3DRXA0oBU0%2FXZ83bsMFy32y%2F%2Fi3nloDyHv45rR%2FexhV6OU53azKWd7Ce0%2BprkFHIQnuhIQXxNWmy395fWL7v0h8gwp2o6BSwZ%2B%2F%2FUxfArtxoCY12it2Wq8o4iF%2FgFG3tHou%2FWUo084EfdnxxzAOPF7oobpEMuGT291DIcTg5ED5nuBLvXhtXbm%2FJbdLMfh2oKZ0qOgQdUtgNpxhRNp7FU5zSwO42E61LU6qlsSkzrDyMOrlwc4GOqUBn15cGyfPV2c2ou%2FX9VnswUF0ARXJG04614qZ1s5fI6fYqazhyYOHVqBF9WUekk8xRuA51t1zOojjGSRFpcJpNSPy0exYzxV3aTlvGNotxZd6RqAJ3I%2BdbtYhJzpUMZOlWiMfYbATgrfqm7wiNUbi8TgytsFnDFQRQg2WujzU0JrcVh5pkCz3FgHCkFMCbyvLafnWH81Wn7G9n0vui1Oi5%2BdMN1ID&X-Amz-Signature=b519cb1f71d6974afcdea375c33ad15874e6d7c62e683e3f38011ea03b5cc30f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

