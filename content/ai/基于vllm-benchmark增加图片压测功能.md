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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS2NTRSQ%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBiPjtPOYrnBrJ8ksrOEJVFnv1KWF4qECprxfMUTVkt0AiEAsbt15fpa2Ru0Og4NEvRd1WHWSU0DDcSXmlVD%2BnxMOrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDN2z8n6Duo%2BN3ucoWSrcA5tHAbUsb16j0r0TUfwtJI%2Fn4%2BODDPJpuUftjgzth%2FxxVEbmSq27MDWd8%2BDx630h0rBipadT1OaYkld4%2Bye7H%2Ft3xNZEGhz6YhBJ58jK1Bogu9B6aqsHyHKz0rsYowTsiE4hplP0dEVe7qI5laAwycZnYcagu2queuK%2BHC%2FSOVIidi5oIWq%2BcAaiJEK3IIxxI90x92%2Bvlcbcwk7ly%2Fq68kg6hhRkXMaG8qZ118lQWpAkfJNdeBSYe4HdUqm6ULCJ8Wt4y1KgKG%2Bu5T4fzcB%2FBcNakA91ypNdj8C0lGB9WUjq1AQXDpjbWcN1tT4A2akB4IVFEEjhkjDYzhxyhPZsI9WoWJ0uXXXNpE8kcni7cvq3yHEa1s%2FwFacKZnUqNmJF%2BBEj8LGKEd5ZK54Cjwch7q%2FlUTIkzXBij3roc0%2FHTuXJDTdGxJFOhwG4km2yK%2BpmSIueiFoXHFSDuZn4DDDymJ8TyoqenQ18jAjHV5t2Dc40BB%2FHXDpCzEtIV9%2B2KqJfVRIu%2BviOLGQQ2YWekAyU3f6H%2FRbWoGP3BXty2iErgzIJeGkHqatR150uBZFUiDQfH5TeCGBsrltbkwDuE7foSboY%2BtaTaKLg2ezeUjd4PuWqxNwbbAiFrKwSBKa6MJKxmckGOqUBBnu3e6e5QlFX3hCAHtLU4Y76jVHxM33zGwaI4mKNW6uTSO2QTUomZRp9gIeTVbaVSLRPzhFXary5KLONM%2FqtqnFfbEj6GVhdiSD81Gg03D9Mp8VSCw5ycgv0TDiJ30e4xvRnq4CEdIzGybRCEmv%2Fm1wgJUkC40KXr9RbLmtfcyivxfLzvTUyF22CIFaViL%2Br4uJXNz9N%2BkVz9HSPMI3JAwn%2Bv3Ng&X-Amz-Signature=a6615ce7058e6564d51e769cbc7ddc869cd56a89618f5612da5fd08f8afb3fa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS2NTRSQ%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBiPjtPOYrnBrJ8ksrOEJVFnv1KWF4qECprxfMUTVkt0AiEAsbt15fpa2Ru0Og4NEvRd1WHWSU0DDcSXmlVD%2BnxMOrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDN2z8n6Duo%2BN3ucoWSrcA5tHAbUsb16j0r0TUfwtJI%2Fn4%2BODDPJpuUftjgzth%2FxxVEbmSq27MDWd8%2BDx630h0rBipadT1OaYkld4%2Bye7H%2Ft3xNZEGhz6YhBJ58jK1Bogu9B6aqsHyHKz0rsYowTsiE4hplP0dEVe7qI5laAwycZnYcagu2queuK%2BHC%2FSOVIidi5oIWq%2BcAaiJEK3IIxxI90x92%2Bvlcbcwk7ly%2Fq68kg6hhRkXMaG8qZ118lQWpAkfJNdeBSYe4HdUqm6ULCJ8Wt4y1KgKG%2Bu5T4fzcB%2FBcNakA91ypNdj8C0lGB9WUjq1AQXDpjbWcN1tT4A2akB4IVFEEjhkjDYzhxyhPZsI9WoWJ0uXXXNpE8kcni7cvq3yHEa1s%2FwFacKZnUqNmJF%2BBEj8LGKEd5ZK54Cjwch7q%2FlUTIkzXBij3roc0%2FHTuXJDTdGxJFOhwG4km2yK%2BpmSIueiFoXHFSDuZn4DDDymJ8TyoqenQ18jAjHV5t2Dc40BB%2FHXDpCzEtIV9%2B2KqJfVRIu%2BviOLGQQ2YWekAyU3f6H%2FRbWoGP3BXty2iErgzIJeGkHqatR150uBZFUiDQfH5TeCGBsrltbkwDuE7foSboY%2BtaTaKLg2ezeUjd4PuWqxNwbbAiFrKwSBKa6MJKxmckGOqUBBnu3e6e5QlFX3hCAHtLU4Y76jVHxM33zGwaI4mKNW6uTSO2QTUomZRp9gIeTVbaVSLRPzhFXary5KLONM%2FqtqnFfbEj6GVhdiSD81Gg03D9Mp8VSCw5ycgv0TDiJ30e4xvRnq4CEdIzGybRCEmv%2Fm1wgJUkC40KXr9RbLmtfcyivxfLzvTUyF22CIFaViL%2Br4uJXNz9N%2BkVz9HSPMI3JAwn%2Bv3Ng&X-Amz-Signature=3e9f87bb8782e5d0637ac985e684f129d2906ce295ec9fd496ae49251d5efab9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS2NTRSQ%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBiPjtPOYrnBrJ8ksrOEJVFnv1KWF4qECprxfMUTVkt0AiEAsbt15fpa2Ru0Og4NEvRd1WHWSU0DDcSXmlVD%2BnxMOrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDN2z8n6Duo%2BN3ucoWSrcA5tHAbUsb16j0r0TUfwtJI%2Fn4%2BODDPJpuUftjgzth%2FxxVEbmSq27MDWd8%2BDx630h0rBipadT1OaYkld4%2Bye7H%2Ft3xNZEGhz6YhBJ58jK1Bogu9B6aqsHyHKz0rsYowTsiE4hplP0dEVe7qI5laAwycZnYcagu2queuK%2BHC%2FSOVIidi5oIWq%2BcAaiJEK3IIxxI90x92%2Bvlcbcwk7ly%2Fq68kg6hhRkXMaG8qZ118lQWpAkfJNdeBSYe4HdUqm6ULCJ8Wt4y1KgKG%2Bu5T4fzcB%2FBcNakA91ypNdj8C0lGB9WUjq1AQXDpjbWcN1tT4A2akB4IVFEEjhkjDYzhxyhPZsI9WoWJ0uXXXNpE8kcni7cvq3yHEa1s%2FwFacKZnUqNmJF%2BBEj8LGKEd5ZK54Cjwch7q%2FlUTIkzXBij3roc0%2FHTuXJDTdGxJFOhwG4km2yK%2BpmSIueiFoXHFSDuZn4DDDymJ8TyoqenQ18jAjHV5t2Dc40BB%2FHXDpCzEtIV9%2B2KqJfVRIu%2BviOLGQQ2YWekAyU3f6H%2FRbWoGP3BXty2iErgzIJeGkHqatR150uBZFUiDQfH5TeCGBsrltbkwDuE7foSboY%2BtaTaKLg2ezeUjd4PuWqxNwbbAiFrKwSBKa6MJKxmckGOqUBBnu3e6e5QlFX3hCAHtLU4Y76jVHxM33zGwaI4mKNW6uTSO2QTUomZRp9gIeTVbaVSLRPzhFXary5KLONM%2FqtqnFfbEj6GVhdiSD81Gg03D9Mp8VSCw5ycgv0TDiJ30e4xvRnq4CEdIzGybRCEmv%2Fm1wgJUkC40KXr9RbLmtfcyivxfLzvTUyF22CIFaViL%2Br4uJXNz9N%2BkVz9HSPMI3JAwn%2Bv3Ng&X-Amz-Signature=33eaeff12e5d868e770de040f51cb733296e1c06294c7aa2363a80cbed459357&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS2NTRSQ%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBiPjtPOYrnBrJ8ksrOEJVFnv1KWF4qECprxfMUTVkt0AiEAsbt15fpa2Ru0Og4NEvRd1WHWSU0DDcSXmlVD%2BnxMOrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDN2z8n6Duo%2BN3ucoWSrcA5tHAbUsb16j0r0TUfwtJI%2Fn4%2BODDPJpuUftjgzth%2FxxVEbmSq27MDWd8%2BDx630h0rBipadT1OaYkld4%2Bye7H%2Ft3xNZEGhz6YhBJ58jK1Bogu9B6aqsHyHKz0rsYowTsiE4hplP0dEVe7qI5laAwycZnYcagu2queuK%2BHC%2FSOVIidi5oIWq%2BcAaiJEK3IIxxI90x92%2Bvlcbcwk7ly%2Fq68kg6hhRkXMaG8qZ118lQWpAkfJNdeBSYe4HdUqm6ULCJ8Wt4y1KgKG%2Bu5T4fzcB%2FBcNakA91ypNdj8C0lGB9WUjq1AQXDpjbWcN1tT4A2akB4IVFEEjhkjDYzhxyhPZsI9WoWJ0uXXXNpE8kcni7cvq3yHEa1s%2FwFacKZnUqNmJF%2BBEj8LGKEd5ZK54Cjwch7q%2FlUTIkzXBij3roc0%2FHTuXJDTdGxJFOhwG4km2yK%2BpmSIueiFoXHFSDuZn4DDDymJ8TyoqenQ18jAjHV5t2Dc40BB%2FHXDpCzEtIV9%2B2KqJfVRIu%2BviOLGQQ2YWekAyU3f6H%2FRbWoGP3BXty2iErgzIJeGkHqatR150uBZFUiDQfH5TeCGBsrltbkwDuE7foSboY%2BtaTaKLg2ezeUjd4PuWqxNwbbAiFrKwSBKa6MJKxmckGOqUBBnu3e6e5QlFX3hCAHtLU4Y76jVHxM33zGwaI4mKNW6uTSO2QTUomZRp9gIeTVbaVSLRPzhFXary5KLONM%2FqtqnFfbEj6GVhdiSD81Gg03D9Mp8VSCw5ycgv0TDiJ30e4xvRnq4CEdIzGybRCEmv%2Fm1wgJUkC40KXr9RbLmtfcyivxfLzvTUyF22CIFaViL%2Br4uJXNz9N%2BkVz9HSPMI3JAwn%2Bv3Ng&X-Amz-Signature=f6c30b191917c7312df230fdcc52d91a7d52d2e526c9b20ccdd3695bbd906f90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS2NTRSQ%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBiPjtPOYrnBrJ8ksrOEJVFnv1KWF4qECprxfMUTVkt0AiEAsbt15fpa2Ru0Og4NEvRd1WHWSU0DDcSXmlVD%2BnxMOrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDN2z8n6Duo%2BN3ucoWSrcA5tHAbUsb16j0r0TUfwtJI%2Fn4%2BODDPJpuUftjgzth%2FxxVEbmSq27MDWd8%2BDx630h0rBipadT1OaYkld4%2Bye7H%2Ft3xNZEGhz6YhBJ58jK1Bogu9B6aqsHyHKz0rsYowTsiE4hplP0dEVe7qI5laAwycZnYcagu2queuK%2BHC%2FSOVIidi5oIWq%2BcAaiJEK3IIxxI90x92%2Bvlcbcwk7ly%2Fq68kg6hhRkXMaG8qZ118lQWpAkfJNdeBSYe4HdUqm6ULCJ8Wt4y1KgKG%2Bu5T4fzcB%2FBcNakA91ypNdj8C0lGB9WUjq1AQXDpjbWcN1tT4A2akB4IVFEEjhkjDYzhxyhPZsI9WoWJ0uXXXNpE8kcni7cvq3yHEa1s%2FwFacKZnUqNmJF%2BBEj8LGKEd5ZK54Cjwch7q%2FlUTIkzXBij3roc0%2FHTuXJDTdGxJFOhwG4km2yK%2BpmSIueiFoXHFSDuZn4DDDymJ8TyoqenQ18jAjHV5t2Dc40BB%2FHXDpCzEtIV9%2B2KqJfVRIu%2BviOLGQQ2YWekAyU3f6H%2FRbWoGP3BXty2iErgzIJeGkHqatR150uBZFUiDQfH5TeCGBsrltbkwDuE7foSboY%2BtaTaKLg2ezeUjd4PuWqxNwbbAiFrKwSBKa6MJKxmckGOqUBBnu3e6e5QlFX3hCAHtLU4Y76jVHxM33zGwaI4mKNW6uTSO2QTUomZRp9gIeTVbaVSLRPzhFXary5KLONM%2FqtqnFfbEj6GVhdiSD81Gg03D9Mp8VSCw5ycgv0TDiJ30e4xvRnq4CEdIzGybRCEmv%2Fm1wgJUkC40KXr9RbLmtfcyivxfLzvTUyF22CIFaViL%2Br4uJXNz9N%2BkVz9HSPMI3JAwn%2Bv3Ng&X-Amz-Signature=8d45ee44d8d12ed07a58964e396c4a782b5ac466fae32bded87bbf74b38e17b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

