---
title: 基于vllm benchmark增加图片压测功能
date: '2025-04-27T06:59:00.000Z'
lastmod: '2025-04-27T08:25:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 根据业务需求，想要在性能压测的原模式中，增加多模态模型的压测能力。以下记录修改代码的全过程以及踩坑记录。

---

# 1. 代码对比

原始代码为vllm开源仓库内/benckmarks/backend_request_func.py 和 /benchmarks/benchmark_serving.py ，主要修改部分为：

benckmark_serving.py

1. parser中新增参数 image-url
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BSL2BNC%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRDKe3bHqQtjbI%2BFgczfYp0GS38h2%2FIu5xEooQRPsSiAIhALjR2pZrLBJ9vpdzwkhEPQ57FT7Aoafpj%2BvlslWOFOo6Kv8DCGQQABoMNjM3NDIzMTgzODA1IgxFNbOC3g%2BkM5mIuG4q3APAQ4m60L3ybaZVKWCqWe20TfHvkKTsAM2kRU04JYVEm5OXC%2B%2FrDk6fDKfHv%2BuWE4nOTzxcH3kG%2FdmcuGpqNa8XNB1Z9pPpUo48PG6xtxOA42Bk%2BSH07KsNWYO2GytVIUO4BSSHIcUFAeRCKTBlpxqpUgllO4gx7St4lWXzfO9x5NUHtR2aiGas%2B1pxHWCa9vxpebmSBVlYBuVXQrWNpZt3WUVBzP0FBXsp3TrxChBIoneCZHt1oY96RM1cvdBkFm0Rw8elFlp7afhavhfpwv7fy6fcj7Aaark1PJDyhgPMjlnuWunmwQ6lqxQ5li%2BM20WeK0xvxl2a1KyKZyRLIdXW7ioEszl10tQNBlCGPHLxqL9gw3SEClH8Ck5V2jIbKn9s8TWMp4hiz1zI5hvSf0HPj9Mj79WdTob92ewlwZe%2FrGqdX6E9D%2BbX2j5TnDftoyoCe2JlmyrIWlivnAPA94gBNTx%2BKaRL4cGcfrk2zA7jwgQ2IMFa5sjj6CONWbYkfrKz4WvviqveK88ihfYLQhX3%2FmmSxgT5dDy5wbm%2FJsRIObNMovB%2Fz4yaVnBTM3B8Ky%2BbQc2nmJDl5GegzvvQtRx30GNhvCQ%2Flepvf6xRAuZ8aTpd%2B3E1msT9pvuIFzC%2FrpTJBjqkAaYVeG7BWkf%2FprOLM4TxpinEjFm2EYsOtx7Kq5BGCP7f34BPQX8c5I98VQ45acv%2F5qnExIyAoyvRZqYNRYja751fREOQi8R0D%2FSWttL2f%2BPj%2F%2B8ijmtcMP2vAuSgeXelEb18iAvq8TNfth2t7MIa6b8GH267dgge%2F2TPF4Kyv%2F9C0j%2FfqDLK3owhRGTZmEsNIvBbaj%2Bl29MHJ2iUCbQqHl%2F6zoeP&X-Amz-Signature=f65450d2fb5522910e2136c4e435cf526120fa61115a2f99205fb780ca58f2cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
parser.add_argument(
        "--image-url",
        type=str,
        default=None,
        help="URL of a fixed image to be included in every request when using --dataset-name random."
    )
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BSL2BNC%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRDKe3bHqQtjbI%2BFgczfYp0GS38h2%2FIu5xEooQRPsSiAIhALjR2pZrLBJ9vpdzwkhEPQ57FT7Aoafpj%2BvlslWOFOo6Kv8DCGQQABoMNjM3NDIzMTgzODA1IgxFNbOC3g%2BkM5mIuG4q3APAQ4m60L3ybaZVKWCqWe20TfHvkKTsAM2kRU04JYVEm5OXC%2B%2FrDk6fDKfHv%2BuWE4nOTzxcH3kG%2FdmcuGpqNa8XNB1Z9pPpUo48PG6xtxOA42Bk%2BSH07KsNWYO2GytVIUO4BSSHIcUFAeRCKTBlpxqpUgllO4gx7St4lWXzfO9x5NUHtR2aiGas%2B1pxHWCa9vxpebmSBVlYBuVXQrWNpZt3WUVBzP0FBXsp3TrxChBIoneCZHt1oY96RM1cvdBkFm0Rw8elFlp7afhavhfpwv7fy6fcj7Aaark1PJDyhgPMjlnuWunmwQ6lqxQ5li%2BM20WeK0xvxl2a1KyKZyRLIdXW7ioEszl10tQNBlCGPHLxqL9gw3SEClH8Ck5V2jIbKn9s8TWMp4hiz1zI5hvSf0HPj9Mj79WdTob92ewlwZe%2FrGqdX6E9D%2BbX2j5TnDftoyoCe2JlmyrIWlivnAPA94gBNTx%2BKaRL4cGcfrk2zA7jwgQ2IMFa5sjj6CONWbYkfrKz4WvviqveK88ihfYLQhX3%2FmmSxgT5dDy5wbm%2FJsRIObNMovB%2Fz4yaVnBTM3B8Ky%2BbQc2nmJDl5GegzvvQtRx30GNhvCQ%2Flepvf6xRAuZ8aTpd%2B3E1msT9pvuIFzC%2FrpTJBjqkAaYVeG7BWkf%2FprOLM4TxpinEjFm2EYsOtx7Kq5BGCP7f34BPQX8c5I98VQ45acv%2F5qnExIyAoyvRZqYNRYja751fREOQi8R0D%2FSWttL2f%2BPj%2F%2B8ijmtcMP2vAuSgeXelEb18iAvq8TNfth2t7MIa6b8GH267dgge%2F2TPF4Kyv%2F9C0j%2FfqDLK3owhRGTZmEsNIvBbaj%2Bl29MHJ2iUCbQqHl%2F6zoeP&X-Amz-Signature=2d95015ccdb198d00667c0d437ab9c9f2ce35bb7c8b2df584670ad6af9499cff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BSL2BNC%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRDKe3bHqQtjbI%2BFgczfYp0GS38h2%2FIu5xEooQRPsSiAIhALjR2pZrLBJ9vpdzwkhEPQ57FT7Aoafpj%2BvlslWOFOo6Kv8DCGQQABoMNjM3NDIzMTgzODA1IgxFNbOC3g%2BkM5mIuG4q3APAQ4m60L3ybaZVKWCqWe20TfHvkKTsAM2kRU04JYVEm5OXC%2B%2FrDk6fDKfHv%2BuWE4nOTzxcH3kG%2FdmcuGpqNa8XNB1Z9pPpUo48PG6xtxOA42Bk%2BSH07KsNWYO2GytVIUO4BSSHIcUFAeRCKTBlpxqpUgllO4gx7St4lWXzfO9x5NUHtR2aiGas%2B1pxHWCa9vxpebmSBVlYBuVXQrWNpZt3WUVBzP0FBXsp3TrxChBIoneCZHt1oY96RM1cvdBkFm0Rw8elFlp7afhavhfpwv7fy6fcj7Aaark1PJDyhgPMjlnuWunmwQ6lqxQ5li%2BM20WeK0xvxl2a1KyKZyRLIdXW7ioEszl10tQNBlCGPHLxqL9gw3SEClH8Ck5V2jIbKn9s8TWMp4hiz1zI5hvSf0HPj9Mj79WdTob92ewlwZe%2FrGqdX6E9D%2BbX2j5TnDftoyoCe2JlmyrIWlivnAPA94gBNTx%2BKaRL4cGcfrk2zA7jwgQ2IMFa5sjj6CONWbYkfrKz4WvviqveK88ihfYLQhX3%2FmmSxgT5dDy5wbm%2FJsRIObNMovB%2Fz4yaVnBTM3B8Ky%2BbQc2nmJDl5GegzvvQtRx30GNhvCQ%2Flepvf6xRAuZ8aTpd%2B3E1msT9pvuIFzC%2FrpTJBjqkAaYVeG7BWkf%2FprOLM4TxpinEjFm2EYsOtx7Kq5BGCP7f34BPQX8c5I98VQ45acv%2F5qnExIyAoyvRZqYNRYja751fREOQi8R0D%2FSWttL2f%2BPj%2F%2B8ijmtcMP2vAuSgeXelEb18iAvq8TNfth2t7MIa6b8GH267dgge%2F2TPF4Kyv%2F9C0j%2FfqDLK3owhRGTZmEsNIvBbaj%2Bl29MHJ2iUCbQqHl%2F6zoeP&X-Amz-Signature=493029bc290c897bd318b9112ed357ab738eef5be8a01fd2b7869c8968e09853&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    elif args.dataset_name == "random":
        input_requests = sample_random_requests(
            prefix_len=args.random_prefix_len,
            input_len=args.random_input_len,
            output_len=args.random_output_len,
            num_prompts=args.num_prompts,
            range_ratio=args.random_range_ratio,
            tokenizer=tokenizer,
            image_url=args.image_url,
        )
        # Add check: if image_url is used, backend must support multi-modal
        if args.image_url and args.backend not in ("openai-chat", ):
             raise ValueError(
                f"Using --image-url requires a multi-modal backend ('openai-chat' or 'openai-image'), but got {args.backend}."
            )

    else:
        raise ValueError(f"Unknown dataset: {args.dataset_name}")
```

---

1. 在benchmark函数处修改
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BSL2BNC%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRDKe3bHqQtjbI%2BFgczfYp0GS38h2%2FIu5xEooQRPsSiAIhALjR2pZrLBJ9vpdzwkhEPQ57FT7Aoafpj%2BvlslWOFOo6Kv8DCGQQABoMNjM3NDIzMTgzODA1IgxFNbOC3g%2BkM5mIuG4q3APAQ4m60L3ybaZVKWCqWe20TfHvkKTsAM2kRU04JYVEm5OXC%2B%2FrDk6fDKfHv%2BuWE4nOTzxcH3kG%2FdmcuGpqNa8XNB1Z9pPpUo48PG6xtxOA42Bk%2BSH07KsNWYO2GytVIUO4BSSHIcUFAeRCKTBlpxqpUgllO4gx7St4lWXzfO9x5NUHtR2aiGas%2B1pxHWCa9vxpebmSBVlYBuVXQrWNpZt3WUVBzP0FBXsp3TrxChBIoneCZHt1oY96RM1cvdBkFm0Rw8elFlp7afhavhfpwv7fy6fcj7Aaark1PJDyhgPMjlnuWunmwQ6lqxQ5li%2BM20WeK0xvxl2a1KyKZyRLIdXW7ioEszl10tQNBlCGPHLxqL9gw3SEClH8Ck5V2jIbKn9s8TWMp4hiz1zI5hvSf0HPj9Mj79WdTob92ewlwZe%2FrGqdX6E9D%2BbX2j5TnDftoyoCe2JlmyrIWlivnAPA94gBNTx%2BKaRL4cGcfrk2zA7jwgQ2IMFa5sjj6CONWbYkfrKz4WvviqveK88ihfYLQhX3%2FmmSxgT5dDy5wbm%2FJsRIObNMovB%2Fz4yaVnBTM3B8Ky%2BbQc2nmJDl5GegzvvQtRx30GNhvCQ%2Flepvf6xRAuZ8aTpd%2B3E1msT9pvuIFzC%2FrpTJBjqkAaYVeG7BWkf%2FprOLM4TxpinEjFm2EYsOtx7Kq5BGCP7f34BPQX8c5I98VQ45acv%2F5qnExIyAoyvRZqYNRYja751fREOQi8R0D%2FSWttL2f%2BPj%2F%2B8ijmtcMP2vAuSgeXelEb18iAvq8TNfth2t7MIa6b8GH267dgge%2F2TPF4Kyv%2F9C0j%2FfqDLK3owhRGTZmEsNIvBbaj%2Bl29MHJ2iUCbQqHl%2F6zoeP&X-Amz-Signature=82a350eba048877723f8867bfb30b6be7dea0627f0abbb14f6fbd6d0a05805eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BSL2BNC%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRDKe3bHqQtjbI%2BFgczfYp0GS38h2%2FIu5xEooQRPsSiAIhALjR2pZrLBJ9vpdzwkhEPQ57FT7Aoafpj%2BvlslWOFOo6Kv8DCGQQABoMNjM3NDIzMTgzODA1IgxFNbOC3g%2BkM5mIuG4q3APAQ4m60L3ybaZVKWCqWe20TfHvkKTsAM2kRU04JYVEm5OXC%2B%2FrDk6fDKfHv%2BuWE4nOTzxcH3kG%2FdmcuGpqNa8XNB1Z9pPpUo48PG6xtxOA42Bk%2BSH07KsNWYO2GytVIUO4BSSHIcUFAeRCKTBlpxqpUgllO4gx7St4lWXzfO9x5NUHtR2aiGas%2B1pxHWCa9vxpebmSBVlYBuVXQrWNpZt3WUVBzP0FBXsp3TrxChBIoneCZHt1oY96RM1cvdBkFm0Rw8elFlp7afhavhfpwv7fy6fcj7Aaark1PJDyhgPMjlnuWunmwQ6lqxQ5li%2BM20WeK0xvxl2a1KyKZyRLIdXW7ioEszl10tQNBlCGPHLxqL9gw3SEClH8Ck5V2jIbKn9s8TWMp4hiz1zI5hvSf0HPj9Mj79WdTob92ewlwZe%2FrGqdX6E9D%2BbX2j5TnDftoyoCe2JlmyrIWlivnAPA94gBNTx%2BKaRL4cGcfrk2zA7jwgQ2IMFa5sjj6CONWbYkfrKz4WvviqveK88ihfYLQhX3%2FmmSxgT5dDy5wbm%2FJsRIObNMovB%2Fz4yaVnBTM3B8Ky%2BbQc2nmJDl5GegzvvQtRx30GNhvCQ%2Flepvf6xRAuZ8aTpd%2B3E1msT9pvuIFzC%2FrpTJBjqkAaYVeG7BWkf%2FprOLM4TxpinEjFm2EYsOtx7Kq5BGCP7f34BPQX8c5I98VQ45acv%2F5qnExIyAoyvRZqYNRYja751fREOQi8R0D%2FSWttL2f%2BPj%2F%2B8ijmtcMP2vAuSgeXelEb18iAvq8TNfth2t7MIa6b8GH267dgge%2F2TPF4Kyv%2F9C0j%2FfqDLK3owhRGTZmEsNIvBbaj%2Bl29MHJ2iUCbQqHl%2F6zoeP&X-Amz-Signature=016ed193687ace70564b49749698c6a4af0b1a48c533a49807951a7bf3ec8fb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
def sample_random_requests(
    prefix_len: int,
    input_len: int,
    output_len: int,
    num_prompts: int,
    range_ratio: float,
    tokenizer: PreTrainedTokenizerBase,
    image_url: Optional[str] = None,
) -> List[Tuple[str, int, int, Optional[Dict[str, Collection[str]]]]]:
    prefix_token_ids = np.random.randint(0,
                                         tokenizer.vocab_size,
                                         size=prefix_len).tolist()

    # range_ratio 用于控制生成的随机输入长度的范围
    # 例如 input_len=100, range_ratio=0.8 时:
    # 生成的随机长度范围为 [80, 100]
    # 这样可以产生一定变化范围的输入长度,而不是固定长度
    input_lens = np.random.randint(
        int(input_len * range_ratio),  # 下限是 input_len * range_ratio
        input_len + 1,                 # 上限是 input_len
        size=num_prompts,              # 生成 num_prompts 个随机长度
    )
    output_lens = np.random.randint(
        int(output_len * range_ratio),
        output_len + 1,
        size=num_prompts,
    )
    offsets = np.random.randint(0, tokenizer.vocab_size, size=num_prompts)
    input_requests = []
    
    # Prepare mm_content if image_url is provided
    mm_content = None
    if image_url:
        mm_content = {
            "type": "image_url",
            "image_url": {
                "url": image_url
            },
        }
        
    for i in range(num_prompts):
        # 生成随机token序列:
        # 1. 先添加固定的prefix_token_ids
        # 2. 再添加随机生成的token_ids:
        #    - 从offset[i]开始
        #    - 每个位置j增加i+j
        #    - 对vocab_size取模确保在词表范围内
        token_ids = prefix_token_ids + [(offsets[i] + i + j) % tokenizer.vocab_size 
                                      for j in range(input_lens[i])]
        # 3. 解码成文本
        prompt = tokenizer.decode(token_ids, skip_special_tokens=True)
        # 4. 重新编码并截断到指定长度
        prompt = tokenizer.decode(
            tokenizer.encode(prompt, truncation=True, max_length=input_lens[i]),
            skip_special_tokens=True
        )
        prompt_len = len(tokenizer.encode(prompt))

        input_requests.append((prompt, prompt_len,
                             int(output_lens[i]), mm_content))
        
        # 打印每行的长度
        print(f"Request {i}: Input length = {prompt_len}, Output length = {output_lens[i]}")

    return input_requests
```

---

backend_request_func.py 主要修改部分为：

1. 在ASYNC_REQUEST_FUNCS处修改名称
1. async_request_openai_chat_completions函数修改
---

# 2. 坑

多模态模型调用模型服务时，需要上传图片。vllm启动的服务endpoint有：

1. chat/completions
1. v1/completions
这两种服务接口参数不一致，当需要输入图片时，只能使用chat/completions 

## 接口案例

---

# 3. 代码分享

---

> References

