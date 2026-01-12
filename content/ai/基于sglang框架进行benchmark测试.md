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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6AZN6FE%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCRIw7MeOG97tYxY7ys9UFx6WGZWDcwRsEoCaw07b4kdAIhAPaeAabCorpeTx7nzQuXxZ8dBtmRdut0r5Nk6RtYntQLKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKSu%2F2j0%2FwDxW6Y4oq3ANKCtOZSZbV6T%2BMwai8Zp8IfKCREeRf2VMlIfpChk2GLKLXuceKqeqiRdoPSd31XF2CQqXBtZHSjSHLzYoLpJvaGFHrmzfbaI8z49p64loYoqN%2ByCTzCH9Ccvw6Pee3ldN%2F577g01ueKGTujpECsZBmK8L6D7MOCaMPgMo4PtPr2l6x%2BDRJoaFa3fAn1EpgLPgb1tW4I2yA4tNjPmks%2BLcVe%2Bz9Jt6fDTZ7F4HEE4o0YD8IcqybiGsM3kBreC6hsKpmFJLIKU9%2F8WOuvy5XJ8T5FPC8AYPI1RKgbjVGrnYI8EjWC%2BcW6v3N7%2Bd50wEzmQBqz74wADSnLLbCf3QH64TjHKu01a1zAMOercG%2Ffq6g0yr2mQTHgpy4SgcaRx%2BCTKH1OYll055fsKQvwzbI9JLeXP%2Fwzax6kukbA7Ao7I6xmo8Cr%2FZjQD9rw5eWUtVj1mPxXWz0pOb9%2F4xW%2BAT8Cyhp6gB8IHLPhi16kDiLSZ%2BHnZod99Dm6kx7HJI2BR7JWqPZAS8WdZIxrfT1cwz9im7K2CnGh4gyeKnS4VpFWfA%2BXefUhs3IWfdcFfnLKZWBG4OX50yW9nP7eGeHyh%2FGL4Y%2BKHwYzuKvIBbzOtHOcmHert1jgjSPW5d3%2F6BPFzCa95DLBjqkASH%2BSGeOLdMdiSlvogozL450gV8hQurKLFDeJuJBZgYWNgGgq8NW8ANz%2Fur0KJINUZ85vyc0SXWceL%2Bvr7I4nvy%2BGL2VILfkADAnIy0DKZt%2BdkxdYBY1wUDP%2F74i8PqopdsuXfrbAZ4Iu1wlesQh%2FjymUsdNf9LCidLte2L2OWLxft2IgJaqYcra4uHRVDT%2Fo0EZ8h%2FnjuAsPbFwxr%2Fq1imxwU1t&X-Amz-Signature=ed0f8bc5d3d8fb85a88814e3111214528fe600e65dc7e7dcbf7e0b3f2b2f4fbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6AZN6FE%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCRIw7MeOG97tYxY7ys9UFx6WGZWDcwRsEoCaw07b4kdAIhAPaeAabCorpeTx7nzQuXxZ8dBtmRdut0r5Nk6RtYntQLKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKSu%2F2j0%2FwDxW6Y4oq3ANKCtOZSZbV6T%2BMwai8Zp8IfKCREeRf2VMlIfpChk2GLKLXuceKqeqiRdoPSd31XF2CQqXBtZHSjSHLzYoLpJvaGFHrmzfbaI8z49p64loYoqN%2ByCTzCH9Ccvw6Pee3ldN%2F577g01ueKGTujpECsZBmK8L6D7MOCaMPgMo4PtPr2l6x%2BDRJoaFa3fAn1EpgLPgb1tW4I2yA4tNjPmks%2BLcVe%2Bz9Jt6fDTZ7F4HEE4o0YD8IcqybiGsM3kBreC6hsKpmFJLIKU9%2F8WOuvy5XJ8T5FPC8AYPI1RKgbjVGrnYI8EjWC%2BcW6v3N7%2Bd50wEzmQBqz74wADSnLLbCf3QH64TjHKu01a1zAMOercG%2Ffq6g0yr2mQTHgpy4SgcaRx%2BCTKH1OYll055fsKQvwzbI9JLeXP%2Fwzax6kukbA7Ao7I6xmo8Cr%2FZjQD9rw5eWUtVj1mPxXWz0pOb9%2F4xW%2BAT8Cyhp6gB8IHLPhi16kDiLSZ%2BHnZod99Dm6kx7HJI2BR7JWqPZAS8WdZIxrfT1cwz9im7K2CnGh4gyeKnS4VpFWfA%2BXefUhs3IWfdcFfnLKZWBG4OX50yW9nP7eGeHyh%2FGL4Y%2BKHwYzuKvIBbzOtHOcmHert1jgjSPW5d3%2F6BPFzCa95DLBjqkASH%2BSGeOLdMdiSlvogozL450gV8hQurKLFDeJuJBZgYWNgGgq8NW8ANz%2Fur0KJINUZ85vyc0SXWceL%2Bvr7I4nvy%2BGL2VILfkADAnIy0DKZt%2BdkxdYBY1wUDP%2F74i8PqopdsuXfrbAZ4Iu1wlesQh%2FjymUsdNf9LCidLte2L2OWLxft2IgJaqYcra4uHRVDT%2Fo0EZ8h%2FnjuAsPbFwxr%2Fq1imxwU1t&X-Amz-Signature=cb1833bdba533a25b6825ef070fbd7f7fbc0c7771068cf832833e452ad139bfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

