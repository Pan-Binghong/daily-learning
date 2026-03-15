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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGGEYP64%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFY09KNoCVSBBDagn%2By0d95gu8FXTLtfE6RVmdVqetMAiEAkWasul2wQUOQyCtbVI0jme8Ian1dWmRWWtgAzv4eP%2BIqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFIDzuLXtJq%2FRd2rbCrcA3rZ3ckE0jNaiUas9erAuzR%2FGBftf3pC%2FvLoYfKQ1%2BARX8vERW5%2B7c7AJdbX2ubK8P8P3sgXhrMDtKkk1umQrTRTiXNz6CciHujaY8K8gbn%2FeUmPFqP%2FnCePelGyqDMbjII%2BK078LP%2Fn9%2BNTNFS3WIziM2XozPV7gyHWPpOwXpIgjlvgewM%2FncT9hY2cI355%2BTBxRFx%2F2jkynJVhx0Cne7jxrHZYWtTJTLFAlyiU2eckEGDdxnMJPb9OI16HUftQ%2Bh4YMdzf7tdCXEGMSQNwFoyYSyEhFgdeIidtyoQ9zav1RLT%2BNxdNw9WPaMrWXS4hR4oJazSi0Le5NY1ICP6TwqLyzqeMnKk5JrGl36wY42jleX7lX7vmJbfwRsJO%2FQKQRsr3LYUYKknJeQ4XARMfHLINXQ7UTIe%2FGnGdOiuCSMFiqq0MAPK%2B1yyAZmcTk36kTpzdnAynLIHHyEYp4C1dKUgN2eSF5M4%2FnmrR1jY6ppzZXD20XTYmFjUylk1Xig8CbP7gYO3QQ1z1QhKm79nkMHwDByNcY9WPWT9KSxTTPl6OR7prUvzLbzE5aV%2F8WYDCGULuxl82MAoJEanj3Ejywy1oZrPaOpnN9Lapx%2FGbhRY08wSm86yTBbaZAIzKMLOQ2M0GOqUBss%2BJ6mYj9%2FQ3wMAaZi%2BMEgQGTy49Fg9gH7bsShftMm%2Frj42eBPnBBzXkrF41FQI4Jx3mpQOuuVKCiJHyuUgkZHwdGwCzUcMFGABoFiWCwfD2QSFyFU%2F695gfIIMAATiZrPuMc7Rj4ZQj4r2ExJ7uIr5qdbkhzoza%2BYVx5FcT%2Fm4uG%2Bs%2BoDRN1pYn6MRTgag9lucxJ1XOByRRIETun7xRgigbRB8W&X-Amz-Signature=bf62e8b80a74e92964db5a78bc00e27186996347bd2645e901ee9b5475c6b3e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGGEYP64%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFY09KNoCVSBBDagn%2By0d95gu8FXTLtfE6RVmdVqetMAiEAkWasul2wQUOQyCtbVI0jme8Ian1dWmRWWtgAzv4eP%2BIqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFIDzuLXtJq%2FRd2rbCrcA3rZ3ckE0jNaiUas9erAuzR%2FGBftf3pC%2FvLoYfKQ1%2BARX8vERW5%2B7c7AJdbX2ubK8P8P3sgXhrMDtKkk1umQrTRTiXNz6CciHujaY8K8gbn%2FeUmPFqP%2FnCePelGyqDMbjII%2BK078LP%2Fn9%2BNTNFS3WIziM2XozPV7gyHWPpOwXpIgjlvgewM%2FncT9hY2cI355%2BTBxRFx%2F2jkynJVhx0Cne7jxrHZYWtTJTLFAlyiU2eckEGDdxnMJPb9OI16HUftQ%2Bh4YMdzf7tdCXEGMSQNwFoyYSyEhFgdeIidtyoQ9zav1RLT%2BNxdNw9WPaMrWXS4hR4oJazSi0Le5NY1ICP6TwqLyzqeMnKk5JrGl36wY42jleX7lX7vmJbfwRsJO%2FQKQRsr3LYUYKknJeQ4XARMfHLINXQ7UTIe%2FGnGdOiuCSMFiqq0MAPK%2B1yyAZmcTk36kTpzdnAynLIHHyEYp4C1dKUgN2eSF5M4%2FnmrR1jY6ppzZXD20XTYmFjUylk1Xig8CbP7gYO3QQ1z1QhKm79nkMHwDByNcY9WPWT9KSxTTPl6OR7prUvzLbzE5aV%2F8WYDCGULuxl82MAoJEanj3Ejywy1oZrPaOpnN9Lapx%2FGbhRY08wSm86yTBbaZAIzKMLOQ2M0GOqUBss%2BJ6mYj9%2FQ3wMAaZi%2BMEgQGTy49Fg9gH7bsShftMm%2Frj42eBPnBBzXkrF41FQI4Jx3mpQOuuVKCiJHyuUgkZHwdGwCzUcMFGABoFiWCwfD2QSFyFU%2F695gfIIMAATiZrPuMc7Rj4ZQj4r2ExJ7uIr5qdbkhzoza%2BYVx5FcT%2Fm4uG%2Bs%2BoDRN1pYn6MRTgag9lucxJ1XOByRRIETun7xRgigbRB8W&X-Amz-Signature=cc61285c62fcb2be96c052013bfbf0231fd94fd865958eeef2e3ac60b5ddf2b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGGEYP64%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFY09KNoCVSBBDagn%2By0d95gu8FXTLtfE6RVmdVqetMAiEAkWasul2wQUOQyCtbVI0jme8Ian1dWmRWWtgAzv4eP%2BIqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFIDzuLXtJq%2FRd2rbCrcA3rZ3ckE0jNaiUas9erAuzR%2FGBftf3pC%2FvLoYfKQ1%2BARX8vERW5%2B7c7AJdbX2ubK8P8P3sgXhrMDtKkk1umQrTRTiXNz6CciHujaY8K8gbn%2FeUmPFqP%2FnCePelGyqDMbjII%2BK078LP%2Fn9%2BNTNFS3WIziM2XozPV7gyHWPpOwXpIgjlvgewM%2FncT9hY2cI355%2BTBxRFx%2F2jkynJVhx0Cne7jxrHZYWtTJTLFAlyiU2eckEGDdxnMJPb9OI16HUftQ%2Bh4YMdzf7tdCXEGMSQNwFoyYSyEhFgdeIidtyoQ9zav1RLT%2BNxdNw9WPaMrWXS4hR4oJazSi0Le5NY1ICP6TwqLyzqeMnKk5JrGl36wY42jleX7lX7vmJbfwRsJO%2FQKQRsr3LYUYKknJeQ4XARMfHLINXQ7UTIe%2FGnGdOiuCSMFiqq0MAPK%2B1yyAZmcTk36kTpzdnAynLIHHyEYp4C1dKUgN2eSF5M4%2FnmrR1jY6ppzZXD20XTYmFjUylk1Xig8CbP7gYO3QQ1z1QhKm79nkMHwDByNcY9WPWT9KSxTTPl6OR7prUvzLbzE5aV%2F8WYDCGULuxl82MAoJEanj3Ejywy1oZrPaOpnN9Lapx%2FGbhRY08wSm86yTBbaZAIzKMLOQ2M0GOqUBss%2BJ6mYj9%2FQ3wMAaZi%2BMEgQGTy49Fg9gH7bsShftMm%2Frj42eBPnBBzXkrF41FQI4Jx3mpQOuuVKCiJHyuUgkZHwdGwCzUcMFGABoFiWCwfD2QSFyFU%2F695gfIIMAATiZrPuMc7Rj4ZQj4r2ExJ7uIr5qdbkhzoza%2BYVx5FcT%2Fm4uG%2Bs%2BoDRN1pYn6MRTgag9lucxJ1XOByRRIETun7xRgigbRB8W&X-Amz-Signature=ac29e371e6750caae86a1390bbf677e3e2ebb0b41ba2377e519c3521442afaa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGGEYP64%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFY09KNoCVSBBDagn%2By0d95gu8FXTLtfE6RVmdVqetMAiEAkWasul2wQUOQyCtbVI0jme8Ian1dWmRWWtgAzv4eP%2BIqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFIDzuLXtJq%2FRd2rbCrcA3rZ3ckE0jNaiUas9erAuzR%2FGBftf3pC%2FvLoYfKQ1%2BARX8vERW5%2B7c7AJdbX2ubK8P8P3sgXhrMDtKkk1umQrTRTiXNz6CciHujaY8K8gbn%2FeUmPFqP%2FnCePelGyqDMbjII%2BK078LP%2Fn9%2BNTNFS3WIziM2XozPV7gyHWPpOwXpIgjlvgewM%2FncT9hY2cI355%2BTBxRFx%2F2jkynJVhx0Cne7jxrHZYWtTJTLFAlyiU2eckEGDdxnMJPb9OI16HUftQ%2Bh4YMdzf7tdCXEGMSQNwFoyYSyEhFgdeIidtyoQ9zav1RLT%2BNxdNw9WPaMrWXS4hR4oJazSi0Le5NY1ICP6TwqLyzqeMnKk5JrGl36wY42jleX7lX7vmJbfwRsJO%2FQKQRsr3LYUYKknJeQ4XARMfHLINXQ7UTIe%2FGnGdOiuCSMFiqq0MAPK%2B1yyAZmcTk36kTpzdnAynLIHHyEYp4C1dKUgN2eSF5M4%2FnmrR1jY6ppzZXD20XTYmFjUylk1Xig8CbP7gYO3QQ1z1QhKm79nkMHwDByNcY9WPWT9KSxTTPl6OR7prUvzLbzE5aV%2F8WYDCGULuxl82MAoJEanj3Ejywy1oZrPaOpnN9Lapx%2FGbhRY08wSm86yTBbaZAIzKMLOQ2M0GOqUBss%2BJ6mYj9%2FQ3wMAaZi%2BMEgQGTy49Fg9gH7bsShftMm%2Frj42eBPnBBzXkrF41FQI4Jx3mpQOuuVKCiJHyuUgkZHwdGwCzUcMFGABoFiWCwfD2QSFyFU%2F695gfIIMAATiZrPuMc7Rj4ZQj4r2ExJ7uIr5qdbkhzoza%2BYVx5FcT%2Fm4uG%2Bs%2BoDRN1pYn6MRTgag9lucxJ1XOByRRIETun7xRgigbRB8W&X-Amz-Signature=6f16c15e2f2b4fab12233c3542bb721b66ec284a0505d410d36ab67407621fe6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGGEYP64%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFY09KNoCVSBBDagn%2By0d95gu8FXTLtfE6RVmdVqetMAiEAkWasul2wQUOQyCtbVI0jme8Ian1dWmRWWtgAzv4eP%2BIqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFIDzuLXtJq%2FRd2rbCrcA3rZ3ckE0jNaiUas9erAuzR%2FGBftf3pC%2FvLoYfKQ1%2BARX8vERW5%2B7c7AJdbX2ubK8P8P3sgXhrMDtKkk1umQrTRTiXNz6CciHujaY8K8gbn%2FeUmPFqP%2FnCePelGyqDMbjII%2BK078LP%2Fn9%2BNTNFS3WIziM2XozPV7gyHWPpOwXpIgjlvgewM%2FncT9hY2cI355%2BTBxRFx%2F2jkynJVhx0Cne7jxrHZYWtTJTLFAlyiU2eckEGDdxnMJPb9OI16HUftQ%2Bh4YMdzf7tdCXEGMSQNwFoyYSyEhFgdeIidtyoQ9zav1RLT%2BNxdNw9WPaMrWXS4hR4oJazSi0Le5NY1ICP6TwqLyzqeMnKk5JrGl36wY42jleX7lX7vmJbfwRsJO%2FQKQRsr3LYUYKknJeQ4XARMfHLINXQ7UTIe%2FGnGdOiuCSMFiqq0MAPK%2B1yyAZmcTk36kTpzdnAynLIHHyEYp4C1dKUgN2eSF5M4%2FnmrR1jY6ppzZXD20XTYmFjUylk1Xig8CbP7gYO3QQ1z1QhKm79nkMHwDByNcY9WPWT9KSxTTPl6OR7prUvzLbzE5aV%2F8WYDCGULuxl82MAoJEanj3Ejywy1oZrPaOpnN9Lapx%2FGbhRY08wSm86yTBbaZAIzKMLOQ2M0GOqUBss%2BJ6mYj9%2FQ3wMAaZi%2BMEgQGTy49Fg9gH7bsShftMm%2Frj42eBPnBBzXkrF41FQI4Jx3mpQOuuVKCiJHyuUgkZHwdGwCzUcMFGABoFiWCwfD2QSFyFU%2F695gfIIMAATiZrPuMc7Rj4ZQj4r2ExJ7uIr5qdbkhzoza%2BYVx5FcT%2Fm4uG%2Bs%2BoDRN1pYn6MRTgag9lucxJ1XOByRRIETun7xRgigbRB8W&X-Amz-Signature=ea058a476d7f3b49d6331256ca497afe0be526d5c575b21d6aa6704a07e17f60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

