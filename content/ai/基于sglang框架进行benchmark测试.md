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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CRLG3KU%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQD5%2FN00WrU7pSbGVcGzewYrgiUMT7y%2BWu0UzfaeIy7%2BLwIhAKwhzBUbpkrG8cbSMgsZl1SVMyTmZYPKXzkSh4%2B5tguMKv8DCAIQABoMNjM3NDIzMTgzODA1IgzbltGK4%2FwzwM0mZCgq3AM%2FEXqWHJPJ35YUQjOvo%2BY1swGPTIgYopZFdfDqeAoyTN1AM%2B86y6nOrUkOkp1K5VPHoeeuK%2BNSwD1RSi5O7lUlcbsuxdzuMtHJporuAEafsDbkfHDyTnR62daZpMZzsEJmd6zdLjFDJIauhpRZmNeCuWbe70fmfd10S72A%2FsQzwKmEk36f%2F%2Fb7Cqo%2Fdul2SkS05%2BzrBC34LfqgQqBaJHQP%2BbVh1c60uuHe9kE12aH0bjrzpD1D8QawBFjKDnG7GJfSYhN%2BJtBn0KJO8SRi9fYUZgHUlU3Jn1auRQcBMnIogdlGNuE1xSwROlxo%2BdHnX1rTWcyWTUfmk%2BJn%2BzJUcuilDCFvlQZ1ZmoetMKsgo%2FhNYNp%2BndCCs33imNXmQ7RVOsp8%2BWRKoVWq5yhkPaO9SL%2BJ8XvwF2JkdbQd0OaMLHwQLTuWdlI0lcZDDINuYg7gsgbJS0p8c%2BeCnXI69PNDXbJHcgCPQmggCd74C55%2BiOtLliE8zcui1UIOumEhqY0XjNy3mwzWDj9ePjKkbvi5xpdKF9lbdA4rdXATbWomahhE9o88pUXJ8JxPxw3lPUa2yHfFEf1MShplaerdswmh7JCZBYAoV7r2y4AKVU22E7rObOSjPm8U2%2FbwwmLijC6hPnMBjqkASHFUC9mZyuivFbjsC7DfN71JMTrzthdGrWJCLtvC%2FnE0kfEHOblorEWUi2wXQkfmotLxRW6qL0T7g6TfIrE90lu3ug1sssgMbZYCMPZf7DiZvn2GKf5JYbBN1HxXWsCaW5WbiboJSJdj7SvJCxPazvhiQdYsjWOKTuzDm7qXXSz156LYHonG9YBnnh73NTnaYWEDaX5VgRCfYkeiJIywxdkFEvD&X-Amz-Signature=ede64e9fdd715fa727434873836b9fe99bc196fb06f3be0c761552a09021df1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CRLG3KU%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQD5%2FN00WrU7pSbGVcGzewYrgiUMT7y%2BWu0UzfaeIy7%2BLwIhAKwhzBUbpkrG8cbSMgsZl1SVMyTmZYPKXzkSh4%2B5tguMKv8DCAIQABoMNjM3NDIzMTgzODA1IgzbltGK4%2FwzwM0mZCgq3AM%2FEXqWHJPJ35YUQjOvo%2BY1swGPTIgYopZFdfDqeAoyTN1AM%2B86y6nOrUkOkp1K5VPHoeeuK%2BNSwD1RSi5O7lUlcbsuxdzuMtHJporuAEafsDbkfHDyTnR62daZpMZzsEJmd6zdLjFDJIauhpRZmNeCuWbe70fmfd10S72A%2FsQzwKmEk36f%2F%2Fb7Cqo%2Fdul2SkS05%2BzrBC34LfqgQqBaJHQP%2BbVh1c60uuHe9kE12aH0bjrzpD1D8QawBFjKDnG7GJfSYhN%2BJtBn0KJO8SRi9fYUZgHUlU3Jn1auRQcBMnIogdlGNuE1xSwROlxo%2BdHnX1rTWcyWTUfmk%2BJn%2BzJUcuilDCFvlQZ1ZmoetMKsgo%2FhNYNp%2BndCCs33imNXmQ7RVOsp8%2BWRKoVWq5yhkPaO9SL%2BJ8XvwF2JkdbQd0OaMLHwQLTuWdlI0lcZDDINuYg7gsgbJS0p8c%2BeCnXI69PNDXbJHcgCPQmggCd74C55%2BiOtLliE8zcui1UIOumEhqY0XjNy3mwzWDj9ePjKkbvi5xpdKF9lbdA4rdXATbWomahhE9o88pUXJ8JxPxw3lPUa2yHfFEf1MShplaerdswmh7JCZBYAoV7r2y4AKVU22E7rObOSjPm8U2%2FbwwmLijC6hPnMBjqkASHFUC9mZyuivFbjsC7DfN71JMTrzthdGrWJCLtvC%2FnE0kfEHOblorEWUi2wXQkfmotLxRW6qL0T7g6TfIrE90lu3ug1sssgMbZYCMPZf7DiZvn2GKf5JYbBN1HxXWsCaW5WbiboJSJdj7SvJCxPazvhiQdYsjWOKTuzDm7qXXSz156LYHonG9YBnnh73NTnaYWEDaX5VgRCfYkeiJIywxdkFEvD&X-Amz-Signature=f37325de045d75ee950b175e458679bb4fe523ddde811c88ed60c598fd86520c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

