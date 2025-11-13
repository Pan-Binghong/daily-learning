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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIFK53TZ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQCZPmWJC8N6Boldo9fF6e5DrEJTQ4OC7KEwkyqFFnSJuwIhANsrtPelBQ9TzlIv2hUCwROvuO1QjuYmBFzQF7kj%2F4jnKv8DCEMQABoMNjM3NDIzMTgzODA1IgwRBgPgBk%2B0iGCUrI4q3AOSq0t7jL8z7Fm7Zd2%2FknKsEnQ7O6KpfPsr5106977TfvHc9YL%2BZ9VP6v5sAPzLteiynI0J3Dkl32iv150GuqJcAynM97NhaMynHGuILpTcmZtF%2FzlMpQxhkHFpxM4dPla1ER%2F18grUYwizgwNjQ8HF8CT6ul4aCEhIerKibXIDMHBpmZyQtVcl5ST6FlPyJz6l0wn4VLw2%2Bo28FkJIl%2FhQCweo6WDAXsYneCIwZ7iuewbaf9XfThUgs7ygxU9KZtFk1%2BStLTnvqXyzM0wIjqxySvnnCufJRpwPOBTXjdVcpc2FJmWpH5oBKBXtCtvBvF0n06YVRrZ2HF33URmtfjTM3I8jDJB1SQzZEYguaqnYgdEcQ%2B9Picbq9lQh77aFM%2B9fNzgA5IoYGbcKi7CqsJOCLcCToJxce4gL0wd89GIZ3%2BKRx2rHy8kFuhM%2BLf3KOWlMGkUbzZOcD%2FaJxaz8VLW63ow%2FS87ZdaO5W6EVW9AB%2B99ustFAFg3Wr%2BeXPneiz1LnKPEvgtwc5Z%2FmHJ%2Bwhh6EGusc5jXJAnIf5wcDW3NXalvuWdw9yrbxJ21jDCOPDEnfeL5bJ4bm046InJ0%2FyTKP5cl66qfkfbB0caxptkhugZShY7qHkSxtB3%2FIJTD979TIBjqkAS3S6MO6eRpPYynX50nwJfE5lfjXr7iPSe%2BtirWPQ4Cwd9NaSzy3XzW7qXFgIoiAeQ1fQ3NbbuyKwOKzi%2FAvi8oxDN8Jh%2BssLq33vuc8Y0keEe8SDoPKlB6Tfg%2FsGOiu%2FUVZ9AMr%2Fzw%2FNsQUD0%2FjMQG3mFrFnj5OMDx0Ix9kMhcr4wQqeHifndiVgms0b9TKJxz%2FA4dAsROAGwLEeS4cwFyzO1IK&X-Amz-Signature=960dae980d23aadb24025b21fc47cfffa074e14fe2743e9a9c6bd096bd6a885d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIFK53TZ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQCZPmWJC8N6Boldo9fF6e5DrEJTQ4OC7KEwkyqFFnSJuwIhANsrtPelBQ9TzlIv2hUCwROvuO1QjuYmBFzQF7kj%2F4jnKv8DCEMQABoMNjM3NDIzMTgzODA1IgwRBgPgBk%2B0iGCUrI4q3AOSq0t7jL8z7Fm7Zd2%2FknKsEnQ7O6KpfPsr5106977TfvHc9YL%2BZ9VP6v5sAPzLteiynI0J3Dkl32iv150GuqJcAynM97NhaMynHGuILpTcmZtF%2FzlMpQxhkHFpxM4dPla1ER%2F18grUYwizgwNjQ8HF8CT6ul4aCEhIerKibXIDMHBpmZyQtVcl5ST6FlPyJz6l0wn4VLw2%2Bo28FkJIl%2FhQCweo6WDAXsYneCIwZ7iuewbaf9XfThUgs7ygxU9KZtFk1%2BStLTnvqXyzM0wIjqxySvnnCufJRpwPOBTXjdVcpc2FJmWpH5oBKBXtCtvBvF0n06YVRrZ2HF33URmtfjTM3I8jDJB1SQzZEYguaqnYgdEcQ%2B9Picbq9lQh77aFM%2B9fNzgA5IoYGbcKi7CqsJOCLcCToJxce4gL0wd89GIZ3%2BKRx2rHy8kFuhM%2BLf3KOWlMGkUbzZOcD%2FaJxaz8VLW63ow%2FS87ZdaO5W6EVW9AB%2B99ustFAFg3Wr%2BeXPneiz1LnKPEvgtwc5Z%2FmHJ%2Bwhh6EGusc5jXJAnIf5wcDW3NXalvuWdw9yrbxJ21jDCOPDEnfeL5bJ4bm046InJ0%2FyTKP5cl66qfkfbB0caxptkhugZShY7qHkSxtB3%2FIJTD979TIBjqkAS3S6MO6eRpPYynX50nwJfE5lfjXr7iPSe%2BtirWPQ4Cwd9NaSzy3XzW7qXFgIoiAeQ1fQ3NbbuyKwOKzi%2FAvi8oxDN8Jh%2BssLq33vuc8Y0keEe8SDoPKlB6Tfg%2FsGOiu%2FUVZ9AMr%2Fzw%2FNsQUD0%2FjMQG3mFrFnj5OMDx0Ix9kMhcr4wQqeHifndiVgms0b9TKJxz%2FA4dAsROAGwLEeS4cwFyzO1IK&X-Amz-Signature=46b127e6acb979745655e424a5789261012c3da26a38ca0794b219ec4cbc4bec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIFK53TZ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQCZPmWJC8N6Boldo9fF6e5DrEJTQ4OC7KEwkyqFFnSJuwIhANsrtPelBQ9TzlIv2hUCwROvuO1QjuYmBFzQF7kj%2F4jnKv8DCEMQABoMNjM3NDIzMTgzODA1IgwRBgPgBk%2B0iGCUrI4q3AOSq0t7jL8z7Fm7Zd2%2FknKsEnQ7O6KpfPsr5106977TfvHc9YL%2BZ9VP6v5sAPzLteiynI0J3Dkl32iv150GuqJcAynM97NhaMynHGuILpTcmZtF%2FzlMpQxhkHFpxM4dPla1ER%2F18grUYwizgwNjQ8HF8CT6ul4aCEhIerKibXIDMHBpmZyQtVcl5ST6FlPyJz6l0wn4VLw2%2Bo28FkJIl%2FhQCweo6WDAXsYneCIwZ7iuewbaf9XfThUgs7ygxU9KZtFk1%2BStLTnvqXyzM0wIjqxySvnnCufJRpwPOBTXjdVcpc2FJmWpH5oBKBXtCtvBvF0n06YVRrZ2HF33URmtfjTM3I8jDJB1SQzZEYguaqnYgdEcQ%2B9Picbq9lQh77aFM%2B9fNzgA5IoYGbcKi7CqsJOCLcCToJxce4gL0wd89GIZ3%2BKRx2rHy8kFuhM%2BLf3KOWlMGkUbzZOcD%2FaJxaz8VLW63ow%2FS87ZdaO5W6EVW9AB%2B99ustFAFg3Wr%2BeXPneiz1LnKPEvgtwc5Z%2FmHJ%2Bwhh6EGusc5jXJAnIf5wcDW3NXalvuWdw9yrbxJ21jDCOPDEnfeL5bJ4bm046InJ0%2FyTKP5cl66qfkfbB0caxptkhugZShY7qHkSxtB3%2FIJTD979TIBjqkAS3S6MO6eRpPYynX50nwJfE5lfjXr7iPSe%2BtirWPQ4Cwd9NaSzy3XzW7qXFgIoiAeQ1fQ3NbbuyKwOKzi%2FAvi8oxDN8Jh%2BssLq33vuc8Y0keEe8SDoPKlB6Tfg%2FsGOiu%2FUVZ9AMr%2Fzw%2FNsQUD0%2FjMQG3mFrFnj5OMDx0Ix9kMhcr4wQqeHifndiVgms0b9TKJxz%2FA4dAsROAGwLEeS4cwFyzO1IK&X-Amz-Signature=4a377dad542d600f67e1b53b5b740e7aa9135fce8fd6c44b7f5a5ec2f14ea597&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIFK53TZ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQCZPmWJC8N6Boldo9fF6e5DrEJTQ4OC7KEwkyqFFnSJuwIhANsrtPelBQ9TzlIv2hUCwROvuO1QjuYmBFzQF7kj%2F4jnKv8DCEMQABoMNjM3NDIzMTgzODA1IgwRBgPgBk%2B0iGCUrI4q3AOSq0t7jL8z7Fm7Zd2%2FknKsEnQ7O6KpfPsr5106977TfvHc9YL%2BZ9VP6v5sAPzLteiynI0J3Dkl32iv150GuqJcAynM97NhaMynHGuILpTcmZtF%2FzlMpQxhkHFpxM4dPla1ER%2F18grUYwizgwNjQ8HF8CT6ul4aCEhIerKibXIDMHBpmZyQtVcl5ST6FlPyJz6l0wn4VLw2%2Bo28FkJIl%2FhQCweo6WDAXsYneCIwZ7iuewbaf9XfThUgs7ygxU9KZtFk1%2BStLTnvqXyzM0wIjqxySvnnCufJRpwPOBTXjdVcpc2FJmWpH5oBKBXtCtvBvF0n06YVRrZ2HF33URmtfjTM3I8jDJB1SQzZEYguaqnYgdEcQ%2B9Picbq9lQh77aFM%2B9fNzgA5IoYGbcKi7CqsJOCLcCToJxce4gL0wd89GIZ3%2BKRx2rHy8kFuhM%2BLf3KOWlMGkUbzZOcD%2FaJxaz8VLW63ow%2FS87ZdaO5W6EVW9AB%2B99ustFAFg3Wr%2BeXPneiz1LnKPEvgtwc5Z%2FmHJ%2Bwhh6EGusc5jXJAnIf5wcDW3NXalvuWdw9yrbxJ21jDCOPDEnfeL5bJ4bm046InJ0%2FyTKP5cl66qfkfbB0caxptkhugZShY7qHkSxtB3%2FIJTD979TIBjqkAS3S6MO6eRpPYynX50nwJfE5lfjXr7iPSe%2BtirWPQ4Cwd9NaSzy3XzW7qXFgIoiAeQ1fQ3NbbuyKwOKzi%2FAvi8oxDN8Jh%2BssLq33vuc8Y0keEe8SDoPKlB6Tfg%2FsGOiu%2FUVZ9AMr%2Fzw%2FNsQUD0%2FjMQG3mFrFnj5OMDx0Ix9kMhcr4wQqeHifndiVgms0b9TKJxz%2FA4dAsROAGwLEeS4cwFyzO1IK&X-Amz-Signature=1ad88918831e0ab6d74f86b40afbe1c7f89b5ac5c87f7783f343b05a26320e0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIFK53TZ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQCZPmWJC8N6Boldo9fF6e5DrEJTQ4OC7KEwkyqFFnSJuwIhANsrtPelBQ9TzlIv2hUCwROvuO1QjuYmBFzQF7kj%2F4jnKv8DCEMQABoMNjM3NDIzMTgzODA1IgwRBgPgBk%2B0iGCUrI4q3AOSq0t7jL8z7Fm7Zd2%2FknKsEnQ7O6KpfPsr5106977TfvHc9YL%2BZ9VP6v5sAPzLteiynI0J3Dkl32iv150GuqJcAynM97NhaMynHGuILpTcmZtF%2FzlMpQxhkHFpxM4dPla1ER%2F18grUYwizgwNjQ8HF8CT6ul4aCEhIerKibXIDMHBpmZyQtVcl5ST6FlPyJz6l0wn4VLw2%2Bo28FkJIl%2FhQCweo6WDAXsYneCIwZ7iuewbaf9XfThUgs7ygxU9KZtFk1%2BStLTnvqXyzM0wIjqxySvnnCufJRpwPOBTXjdVcpc2FJmWpH5oBKBXtCtvBvF0n06YVRrZ2HF33URmtfjTM3I8jDJB1SQzZEYguaqnYgdEcQ%2B9Picbq9lQh77aFM%2B9fNzgA5IoYGbcKi7CqsJOCLcCToJxce4gL0wd89GIZ3%2BKRx2rHy8kFuhM%2BLf3KOWlMGkUbzZOcD%2FaJxaz8VLW63ow%2FS87ZdaO5W6EVW9AB%2B99ustFAFg3Wr%2BeXPneiz1LnKPEvgtwc5Z%2FmHJ%2Bwhh6EGusc5jXJAnIf5wcDW3NXalvuWdw9yrbxJ21jDCOPDEnfeL5bJ4bm046InJ0%2FyTKP5cl66qfkfbB0caxptkhugZShY7qHkSxtB3%2FIJTD979TIBjqkAS3S6MO6eRpPYynX50nwJfE5lfjXr7iPSe%2BtirWPQ4Cwd9NaSzy3XzW7qXFgIoiAeQ1fQ3NbbuyKwOKzi%2FAvi8oxDN8Jh%2BssLq33vuc8Y0keEe8SDoPKlB6Tfg%2FsGOiu%2FUVZ9AMr%2Fzw%2FNsQUD0%2FjMQG3mFrFnj5OMDx0Ix9kMhcr4wQqeHifndiVgms0b9TKJxz%2FA4dAsROAGwLEeS4cwFyzO1IK&X-Amz-Signature=9691a6a995667c26c0457fbd47e4ce051cd11487bae6279eab99c7d8c6f36de5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

