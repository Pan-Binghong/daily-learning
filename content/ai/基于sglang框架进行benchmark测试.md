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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGKJPKP%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FvcHYwjSFRlWcz93DcJWWkZsHOSTd%2BRWiLQh4UQzKDAiBplOwTMRyjI6DDnXUXa%2BYG96h0Unyr1HclngVz0LrvASqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe9%2FfXOKzGSmyELxpKtwD%2BZOuK46ez6YMOomhEMNoSU2tmzv9Hzq2rSfKjtkc9kx6Ms8alJWFZRZxmHSuUfsJrvRGrxeIlMn9pbiAFHHLoaeoIcS6J0zyqoJYat3%2BzUeUSyzyWiYjLR6fyoJKUClKZJuunowqYoA0nvTv4nPFsUFrq3%2FC6xILxBaVLvdUQ%2Bm6KhN13%2BFZ81E9ljD4Xs9XBFpzt2j9JxDhMjrXu1nn2JfaiCkTyEhIKkDiAgPmdOuLeAqjR4acuCufcP%2FJjNwJeZcQflAmaRL3mAzFE29j6Yv6A1kBuDgLT8olpUy%2Bq2632TRnTUG0ZH1MHicSWdrDak1G%2FxTxgITJW5a%2BX1eBHVcU1TZmsKniC8g5n%2F1TlX4MXeUxNercaQLB4rtjWOyAmAz6TVmtLbBSdeb3hRFMFpADvrwEai0uoWrWflmDItQcCijI0koF%2F5tozEKRYQOjZyQ59SmmGMS6LAREznYA0F2qn91mzwSJLUbCsLue%2BNC1aHYgD3E8hPHynfPWE%2FIvbg7ZGOjRhmVlIYI6myqiGxMJYsbwG5qqYzDhOu13vCx5AsnmBHafc%2FWMVokZPQbItjcumxxZNPPltF8156CYPHJJ1esAvfHVCiiacSCrhhGto2A0%2BKYBI0cJ9%2BswrOSeyQY6pgEyaEpUiiW24m3tw%2Fv0K0EYJG6vaLjibwICAhP7E5n438o8Bdrrmyb6sxjmLBYKigtU%2BLCL%2BWDdOaDg3u5NP7ug0IqHsxKwWK6EIovDriHnkylzW1X1itqB%2B2YsKar8eyxtia%2Br0s14LO0Okjana6EqZu1FN1ogJw18ClLyxWEtgGBene0czTvtFnRHGtz7L9IGknsXTKVcBMkh6huHUtjthVqYoGZX&X-Amz-Signature=ae9752f8a3adb55ba657fdb9e9d3b4f3bfacec7a7f87d5223b7b16e3b30bc425&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UGKJPKP%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FvcHYwjSFRlWcz93DcJWWkZsHOSTd%2BRWiLQh4UQzKDAiBplOwTMRyjI6DDnXUXa%2BYG96h0Unyr1HclngVz0LrvASqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe9%2FfXOKzGSmyELxpKtwD%2BZOuK46ez6YMOomhEMNoSU2tmzv9Hzq2rSfKjtkc9kx6Ms8alJWFZRZxmHSuUfsJrvRGrxeIlMn9pbiAFHHLoaeoIcS6J0zyqoJYat3%2BzUeUSyzyWiYjLR6fyoJKUClKZJuunowqYoA0nvTv4nPFsUFrq3%2FC6xILxBaVLvdUQ%2Bm6KhN13%2BFZ81E9ljD4Xs9XBFpzt2j9JxDhMjrXu1nn2JfaiCkTyEhIKkDiAgPmdOuLeAqjR4acuCufcP%2FJjNwJeZcQflAmaRL3mAzFE29j6Yv6A1kBuDgLT8olpUy%2Bq2632TRnTUG0ZH1MHicSWdrDak1G%2FxTxgITJW5a%2BX1eBHVcU1TZmsKniC8g5n%2F1TlX4MXeUxNercaQLB4rtjWOyAmAz6TVmtLbBSdeb3hRFMFpADvrwEai0uoWrWflmDItQcCijI0koF%2F5tozEKRYQOjZyQ59SmmGMS6LAREznYA0F2qn91mzwSJLUbCsLue%2BNC1aHYgD3E8hPHynfPWE%2FIvbg7ZGOjRhmVlIYI6myqiGxMJYsbwG5qqYzDhOu13vCx5AsnmBHafc%2FWMVokZPQbItjcumxxZNPPltF8156CYPHJJ1esAvfHVCiiacSCrhhGto2A0%2BKYBI0cJ9%2BswrOSeyQY6pgEyaEpUiiW24m3tw%2Fv0K0EYJG6vaLjibwICAhP7E5n438o8Bdrrmyb6sxjmLBYKigtU%2BLCL%2BWDdOaDg3u5NP7ug0IqHsxKwWK6EIovDriHnkylzW1X1itqB%2B2YsKar8eyxtia%2Br0s14LO0Okjana6EqZu1FN1ogJw18ClLyxWEtgGBene0czTvtFnRHGtz7L9IGknsXTKVcBMkh6huHUtjthVqYoGZX&X-Amz-Signature=504ab4d0713e6049d5900c643274bd26c743ab360439a421e55a82a2aadb3df1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

