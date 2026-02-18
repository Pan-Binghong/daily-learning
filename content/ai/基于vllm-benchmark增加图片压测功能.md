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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XGU4YKG%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF807QM0duq7cVv3hWWbQ0ye0n4rmFZ8W%2Fo6cG62oysjAiEAzrX7%2B0xXHP%2Bh1vnnZPJAn%2BpouC5cMbTXeNc%2FjSvHDV4q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDnJYThEGXtbMpJ13CrcAxNO%2BYhDqD%2FHt0HH1Tw2PGd7VO%2FqDuq%2F8Jj84ObUSSG%2BqHyXi0T8z7mbLKU9F%2Fhj%2BFdJYsIhOjUiGyBidiW1Qo742p1xV8RXvCISn%2F%2F%2FL1uluIH%2BDsmXaXhx81hPDPLXwNUZJ258nG1zChHK1szPvi7EHp1nIUjCf%2BEwRwB%2B6ME1JAJDcFqq4xoBj%2B43iA2xovwWD59XIkcjXHrvKDM1dl%2FCCtayBLik0MKb6cD6GhIBGHROOwEjG1qNR0ZIEbwP48MJGGTt%2BVZs3oktc%2F7ccVmjtVtlpHzXpDolCXyX3grYm8tVQp468BQ89HcRJGDGg%2Bnlislufd3qZLIkadtiKwrY9bwuk8o8bw4I2iGUW5mHTupPRrLyqYBHPb90VUccwcugNzwTdGezibdyu3C3Asb2hnJmjg60BY9S3lmFRFEsnu1R63tJWq0TpL3WXwOz%2BWdcLG8YYr0k4P%2FMHtt2%2Fkm44LLimeO5hVEa4fU9qIOMNRAfUZVJg%2B4EQ2Xfh87VksitvQeOniUa2HkjNfXk2tHYRvkoUmD9c1RYJ%2B9pv0ZFweCXFa9Kf9Ol8I7BVmwTb1lbEx%2F9POOAyUyoNIBl39ku6ogkDBtgMQ4mTKYvlu4hTHzTeIlrS503O%2Bc8MJ%2Bf1MwGOqUBf67T80pELTC%2BCvJmY2N76xWDg3dF8mRzHcqHLvfuiypN4%2FIw3RAuUyVeFg6K%2FyszoCDNapEb9T%2FpeIcK9FKnMwu4qgtyRx2qMOF0AhD0bQ9D0pn9TRhK%2F8r%2BQXLz0lK1S9K86CJig4%2BA1AAtSLHNMCOSS%2BlNdRxdwM4n4v3uc2yEE%2Fv%2FfI8Ye8KfwQD10DjjdY%2F0vpXV9D4NE6ggQ8M269gNTFel&X-Amz-Signature=451321f0ee7e9d8e587c9d382f25715ba067b655742e6018544c741ccfc2f6eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XGU4YKG%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF807QM0duq7cVv3hWWbQ0ye0n4rmFZ8W%2Fo6cG62oysjAiEAzrX7%2B0xXHP%2Bh1vnnZPJAn%2BpouC5cMbTXeNc%2FjSvHDV4q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDnJYThEGXtbMpJ13CrcAxNO%2BYhDqD%2FHt0HH1Tw2PGd7VO%2FqDuq%2F8Jj84ObUSSG%2BqHyXi0T8z7mbLKU9F%2Fhj%2BFdJYsIhOjUiGyBidiW1Qo742p1xV8RXvCISn%2F%2F%2FL1uluIH%2BDsmXaXhx81hPDPLXwNUZJ258nG1zChHK1szPvi7EHp1nIUjCf%2BEwRwB%2B6ME1JAJDcFqq4xoBj%2B43iA2xovwWD59XIkcjXHrvKDM1dl%2FCCtayBLik0MKb6cD6GhIBGHROOwEjG1qNR0ZIEbwP48MJGGTt%2BVZs3oktc%2F7ccVmjtVtlpHzXpDolCXyX3grYm8tVQp468BQ89HcRJGDGg%2Bnlislufd3qZLIkadtiKwrY9bwuk8o8bw4I2iGUW5mHTupPRrLyqYBHPb90VUccwcugNzwTdGezibdyu3C3Asb2hnJmjg60BY9S3lmFRFEsnu1R63tJWq0TpL3WXwOz%2BWdcLG8YYr0k4P%2FMHtt2%2Fkm44LLimeO5hVEa4fU9qIOMNRAfUZVJg%2B4EQ2Xfh87VksitvQeOniUa2HkjNfXk2tHYRvkoUmD9c1RYJ%2B9pv0ZFweCXFa9Kf9Ol8I7BVmwTb1lbEx%2F9POOAyUyoNIBl39ku6ogkDBtgMQ4mTKYvlu4hTHzTeIlrS503O%2Bc8MJ%2Bf1MwGOqUBf67T80pELTC%2BCvJmY2N76xWDg3dF8mRzHcqHLvfuiypN4%2FIw3RAuUyVeFg6K%2FyszoCDNapEb9T%2FpeIcK9FKnMwu4qgtyRx2qMOF0AhD0bQ9D0pn9TRhK%2F8r%2BQXLz0lK1S9K86CJig4%2BA1AAtSLHNMCOSS%2BlNdRxdwM4n4v3uc2yEE%2Fv%2FfI8Ye8KfwQD10DjjdY%2F0vpXV9D4NE6ggQ8M269gNTFel&X-Amz-Signature=a85e2fa0cb8f3e6c2b6adf0314ea2a80d0434e0485d2dbfe12db3207211deee4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XGU4YKG%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF807QM0duq7cVv3hWWbQ0ye0n4rmFZ8W%2Fo6cG62oysjAiEAzrX7%2B0xXHP%2Bh1vnnZPJAn%2BpouC5cMbTXeNc%2FjSvHDV4q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDnJYThEGXtbMpJ13CrcAxNO%2BYhDqD%2FHt0HH1Tw2PGd7VO%2FqDuq%2F8Jj84ObUSSG%2BqHyXi0T8z7mbLKU9F%2Fhj%2BFdJYsIhOjUiGyBidiW1Qo742p1xV8RXvCISn%2F%2F%2FL1uluIH%2BDsmXaXhx81hPDPLXwNUZJ258nG1zChHK1szPvi7EHp1nIUjCf%2BEwRwB%2B6ME1JAJDcFqq4xoBj%2B43iA2xovwWD59XIkcjXHrvKDM1dl%2FCCtayBLik0MKb6cD6GhIBGHROOwEjG1qNR0ZIEbwP48MJGGTt%2BVZs3oktc%2F7ccVmjtVtlpHzXpDolCXyX3grYm8tVQp468BQ89HcRJGDGg%2Bnlislufd3qZLIkadtiKwrY9bwuk8o8bw4I2iGUW5mHTupPRrLyqYBHPb90VUccwcugNzwTdGezibdyu3C3Asb2hnJmjg60BY9S3lmFRFEsnu1R63tJWq0TpL3WXwOz%2BWdcLG8YYr0k4P%2FMHtt2%2Fkm44LLimeO5hVEa4fU9qIOMNRAfUZVJg%2B4EQ2Xfh87VksitvQeOniUa2HkjNfXk2tHYRvkoUmD9c1RYJ%2B9pv0ZFweCXFa9Kf9Ol8I7BVmwTb1lbEx%2F9POOAyUyoNIBl39ku6ogkDBtgMQ4mTKYvlu4hTHzTeIlrS503O%2Bc8MJ%2Bf1MwGOqUBf67T80pELTC%2BCvJmY2N76xWDg3dF8mRzHcqHLvfuiypN4%2FIw3RAuUyVeFg6K%2FyszoCDNapEb9T%2FpeIcK9FKnMwu4qgtyRx2qMOF0AhD0bQ9D0pn9TRhK%2F8r%2BQXLz0lK1S9K86CJig4%2BA1AAtSLHNMCOSS%2BlNdRxdwM4n4v3uc2yEE%2Fv%2FfI8Ye8KfwQD10DjjdY%2F0vpXV9D4NE6ggQ8M269gNTFel&X-Amz-Signature=f2d1c0938b75e2f745c621d87c962134b0691eaf63e2e71f87c8853e38d3189c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XGU4YKG%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF807QM0duq7cVv3hWWbQ0ye0n4rmFZ8W%2Fo6cG62oysjAiEAzrX7%2B0xXHP%2Bh1vnnZPJAn%2BpouC5cMbTXeNc%2FjSvHDV4q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDnJYThEGXtbMpJ13CrcAxNO%2BYhDqD%2FHt0HH1Tw2PGd7VO%2FqDuq%2F8Jj84ObUSSG%2BqHyXi0T8z7mbLKU9F%2Fhj%2BFdJYsIhOjUiGyBidiW1Qo742p1xV8RXvCISn%2F%2F%2FL1uluIH%2BDsmXaXhx81hPDPLXwNUZJ258nG1zChHK1szPvi7EHp1nIUjCf%2BEwRwB%2B6ME1JAJDcFqq4xoBj%2B43iA2xovwWD59XIkcjXHrvKDM1dl%2FCCtayBLik0MKb6cD6GhIBGHROOwEjG1qNR0ZIEbwP48MJGGTt%2BVZs3oktc%2F7ccVmjtVtlpHzXpDolCXyX3grYm8tVQp468BQ89HcRJGDGg%2Bnlislufd3qZLIkadtiKwrY9bwuk8o8bw4I2iGUW5mHTupPRrLyqYBHPb90VUccwcugNzwTdGezibdyu3C3Asb2hnJmjg60BY9S3lmFRFEsnu1R63tJWq0TpL3WXwOz%2BWdcLG8YYr0k4P%2FMHtt2%2Fkm44LLimeO5hVEa4fU9qIOMNRAfUZVJg%2B4EQ2Xfh87VksitvQeOniUa2HkjNfXk2tHYRvkoUmD9c1RYJ%2B9pv0ZFweCXFa9Kf9Ol8I7BVmwTb1lbEx%2F9POOAyUyoNIBl39ku6ogkDBtgMQ4mTKYvlu4hTHzTeIlrS503O%2Bc8MJ%2Bf1MwGOqUBf67T80pELTC%2BCvJmY2N76xWDg3dF8mRzHcqHLvfuiypN4%2FIw3RAuUyVeFg6K%2FyszoCDNapEb9T%2FpeIcK9FKnMwu4qgtyRx2qMOF0AhD0bQ9D0pn9TRhK%2F8r%2BQXLz0lK1S9K86CJig4%2BA1AAtSLHNMCOSS%2BlNdRxdwM4n4v3uc2yEE%2Fv%2FfI8Ye8KfwQD10DjjdY%2F0vpXV9D4NE6ggQ8M269gNTFel&X-Amz-Signature=e3dfe51cd4356be936024b249aa8a3701617f3e387daad869866fdf0fae7fb1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XGU4YKG%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF807QM0duq7cVv3hWWbQ0ye0n4rmFZ8W%2Fo6cG62oysjAiEAzrX7%2B0xXHP%2Bh1vnnZPJAn%2BpouC5cMbTXeNc%2FjSvHDV4q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDnJYThEGXtbMpJ13CrcAxNO%2BYhDqD%2FHt0HH1Tw2PGd7VO%2FqDuq%2F8Jj84ObUSSG%2BqHyXi0T8z7mbLKU9F%2Fhj%2BFdJYsIhOjUiGyBidiW1Qo742p1xV8RXvCISn%2F%2F%2FL1uluIH%2BDsmXaXhx81hPDPLXwNUZJ258nG1zChHK1szPvi7EHp1nIUjCf%2BEwRwB%2B6ME1JAJDcFqq4xoBj%2B43iA2xovwWD59XIkcjXHrvKDM1dl%2FCCtayBLik0MKb6cD6GhIBGHROOwEjG1qNR0ZIEbwP48MJGGTt%2BVZs3oktc%2F7ccVmjtVtlpHzXpDolCXyX3grYm8tVQp468BQ89HcRJGDGg%2Bnlislufd3qZLIkadtiKwrY9bwuk8o8bw4I2iGUW5mHTupPRrLyqYBHPb90VUccwcugNzwTdGezibdyu3C3Asb2hnJmjg60BY9S3lmFRFEsnu1R63tJWq0TpL3WXwOz%2BWdcLG8YYr0k4P%2FMHtt2%2Fkm44LLimeO5hVEa4fU9qIOMNRAfUZVJg%2B4EQ2Xfh87VksitvQeOniUa2HkjNfXk2tHYRvkoUmD9c1RYJ%2B9pv0ZFweCXFa9Kf9Ol8I7BVmwTb1lbEx%2F9POOAyUyoNIBl39ku6ogkDBtgMQ4mTKYvlu4hTHzTeIlrS503O%2Bc8MJ%2Bf1MwGOqUBf67T80pELTC%2BCvJmY2N76xWDg3dF8mRzHcqHLvfuiypN4%2FIw3RAuUyVeFg6K%2FyszoCDNapEb9T%2FpeIcK9FKnMwu4qgtyRx2qMOF0AhD0bQ9D0pn9TRhK%2F8r%2BQXLz0lK1S9K86CJig4%2BA1AAtSLHNMCOSS%2BlNdRxdwM4n4v3uc2yEE%2Fv%2FfI8Ye8KfwQD10DjjdY%2F0vpXV9D4NE6ggQ8M269gNTFel&X-Amz-Signature=3c3eed20cd044d433e0ab015ff5a84f83dc563e2ef2688a2e5058c8c6b0f79f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

