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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4FEJSS%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArlckDvUB7TeweoCawrMuYyOhYlrrOiUw8PXNRKhwXPAiAId6gyEbDiBD1cz64xWTe72mRN5r%2BwXAMHELkyy%2BemGSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMGfwd1eSd3bHMXCU5KtwDVgJlZgOoc4Cax%2BbNJfRNXt7AOMeVRYdj92efJZI4pNo8zeqKuheKWASht8UZyh877EyZu2wgbHR6hu9kgjekiEMkCaxxZAHT0C1Mh52DEqkwfv3DsH6F9tgqlOGgJPBV0VZ2lAxl44NH5SbTyMrt7S4%2BCLzc0XXE1YrUade09OjiHfKERm1MX40qD32LlZF2S4AveL93gzY%2Fs2CwGFzX0esQSsczA6rM%2FLGWLNOGMgjMW3Ft3E9s8rLYQZ69ZO3n2NBLD%2BGZJCyxwlAf2j0LmqbT49qLSEZet1hN3GrdZFSVp9rlbM9W4%2Ban0xkLbRTb3gBmMw9Ek%2Ftp%2BaIfAMdxPR08uJM1ecda3EIMuKnrS1BVSvh%2FoX7PxYNyz3JJVOCrMzPRl%2BTJ%2B6jj3cuBMbIlw3KIAVD%2F9iwFj%2F3RFHfHHLuztyPdO1gzRdQ3rGZ0uDY6cuGPjPFPdRQbiuHrScN5WjUevPpNyYeyqyW3x2thkPJcercZ62qPxuRwla7ns5qUn9tMP4hEIVptHBjTbDyXrSsF7n5ITsD8ZwxNq3lkUp5OCwHS6n%2FKiFfm2Pw5Vx9il36HpFAL9BnFqgQUHDhdlmzUieWSwm2KfnKkJfT%2FM6R%2FeWYxIu5x%2B8%2BGrQswp6LrywY6pgGZeTiwz5gYkcWai4fDDTkYvCs4vYhi4sGQgdE9ucPLFdg8eEMH8VInrTPiaRNXoqC395AyxQK9PuXwMP%2BTZu2uy85uriK3iNC93pQfzxYa41utwa%2BMtwpX8QDazF2UKRim%2FCmT6MZYEMzYUysz2GyfMwSGjyPcmjQYWVRGdYx0SpVh05LYr6NMp%2FA%2FGMXPIU%2FXBii0wjEe0JwQD75RN9Z1lHJ5YNOg&X-Amz-Signature=43c6b52b9646489cbf19be20d3e1c587c283abbebf394d559d58e04bf74e69b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4FEJSS%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArlckDvUB7TeweoCawrMuYyOhYlrrOiUw8PXNRKhwXPAiAId6gyEbDiBD1cz64xWTe72mRN5r%2BwXAMHELkyy%2BemGSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMGfwd1eSd3bHMXCU5KtwDVgJlZgOoc4Cax%2BbNJfRNXt7AOMeVRYdj92efJZI4pNo8zeqKuheKWASht8UZyh877EyZu2wgbHR6hu9kgjekiEMkCaxxZAHT0C1Mh52DEqkwfv3DsH6F9tgqlOGgJPBV0VZ2lAxl44NH5SbTyMrt7S4%2BCLzc0XXE1YrUade09OjiHfKERm1MX40qD32LlZF2S4AveL93gzY%2Fs2CwGFzX0esQSsczA6rM%2FLGWLNOGMgjMW3Ft3E9s8rLYQZ69ZO3n2NBLD%2BGZJCyxwlAf2j0LmqbT49qLSEZet1hN3GrdZFSVp9rlbM9W4%2Ban0xkLbRTb3gBmMw9Ek%2Ftp%2BaIfAMdxPR08uJM1ecda3EIMuKnrS1BVSvh%2FoX7PxYNyz3JJVOCrMzPRl%2BTJ%2B6jj3cuBMbIlw3KIAVD%2F9iwFj%2F3RFHfHHLuztyPdO1gzRdQ3rGZ0uDY6cuGPjPFPdRQbiuHrScN5WjUevPpNyYeyqyW3x2thkPJcercZ62qPxuRwla7ns5qUn9tMP4hEIVptHBjTbDyXrSsF7n5ITsD8ZwxNq3lkUp5OCwHS6n%2FKiFfm2Pw5Vx9il36HpFAL9BnFqgQUHDhdlmzUieWSwm2KfnKkJfT%2FM6R%2FeWYxIu5x%2B8%2BGrQswp6LrywY6pgGZeTiwz5gYkcWai4fDDTkYvCs4vYhi4sGQgdE9ucPLFdg8eEMH8VInrTPiaRNXoqC395AyxQK9PuXwMP%2BTZu2uy85uriK3iNC93pQfzxYa41utwa%2BMtwpX8QDazF2UKRim%2FCmT6MZYEMzYUysz2GyfMwSGjyPcmjQYWVRGdYx0SpVh05LYr6NMp%2FA%2FGMXPIU%2FXBii0wjEe0JwQD75RN9Z1lHJ5YNOg&X-Amz-Signature=0920716717e87c386df473885b35ec7e70a238ac7cc948bf873becac257aaaef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4FEJSS%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArlckDvUB7TeweoCawrMuYyOhYlrrOiUw8PXNRKhwXPAiAId6gyEbDiBD1cz64xWTe72mRN5r%2BwXAMHELkyy%2BemGSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMGfwd1eSd3bHMXCU5KtwDVgJlZgOoc4Cax%2BbNJfRNXt7AOMeVRYdj92efJZI4pNo8zeqKuheKWASht8UZyh877EyZu2wgbHR6hu9kgjekiEMkCaxxZAHT0C1Mh52DEqkwfv3DsH6F9tgqlOGgJPBV0VZ2lAxl44NH5SbTyMrt7S4%2BCLzc0XXE1YrUade09OjiHfKERm1MX40qD32LlZF2S4AveL93gzY%2Fs2CwGFzX0esQSsczA6rM%2FLGWLNOGMgjMW3Ft3E9s8rLYQZ69ZO3n2NBLD%2BGZJCyxwlAf2j0LmqbT49qLSEZet1hN3GrdZFSVp9rlbM9W4%2Ban0xkLbRTb3gBmMw9Ek%2Ftp%2BaIfAMdxPR08uJM1ecda3EIMuKnrS1BVSvh%2FoX7PxYNyz3JJVOCrMzPRl%2BTJ%2B6jj3cuBMbIlw3KIAVD%2F9iwFj%2F3RFHfHHLuztyPdO1gzRdQ3rGZ0uDY6cuGPjPFPdRQbiuHrScN5WjUevPpNyYeyqyW3x2thkPJcercZ62qPxuRwla7ns5qUn9tMP4hEIVptHBjTbDyXrSsF7n5ITsD8ZwxNq3lkUp5OCwHS6n%2FKiFfm2Pw5Vx9il36HpFAL9BnFqgQUHDhdlmzUieWSwm2KfnKkJfT%2FM6R%2FeWYxIu5x%2B8%2BGrQswp6LrywY6pgGZeTiwz5gYkcWai4fDDTkYvCs4vYhi4sGQgdE9ucPLFdg8eEMH8VInrTPiaRNXoqC395AyxQK9PuXwMP%2BTZu2uy85uriK3iNC93pQfzxYa41utwa%2BMtwpX8QDazF2UKRim%2FCmT6MZYEMzYUysz2GyfMwSGjyPcmjQYWVRGdYx0SpVh05LYr6NMp%2FA%2FGMXPIU%2FXBii0wjEe0JwQD75RN9Z1lHJ5YNOg&X-Amz-Signature=135d08557da519afac4d9711820090bbb92b154a12ee5432471d6bf9af0a2ced&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4FEJSS%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArlckDvUB7TeweoCawrMuYyOhYlrrOiUw8PXNRKhwXPAiAId6gyEbDiBD1cz64xWTe72mRN5r%2BwXAMHELkyy%2BemGSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMGfwd1eSd3bHMXCU5KtwDVgJlZgOoc4Cax%2BbNJfRNXt7AOMeVRYdj92efJZI4pNo8zeqKuheKWASht8UZyh877EyZu2wgbHR6hu9kgjekiEMkCaxxZAHT0C1Mh52DEqkwfv3DsH6F9tgqlOGgJPBV0VZ2lAxl44NH5SbTyMrt7S4%2BCLzc0XXE1YrUade09OjiHfKERm1MX40qD32LlZF2S4AveL93gzY%2Fs2CwGFzX0esQSsczA6rM%2FLGWLNOGMgjMW3Ft3E9s8rLYQZ69ZO3n2NBLD%2BGZJCyxwlAf2j0LmqbT49qLSEZet1hN3GrdZFSVp9rlbM9W4%2Ban0xkLbRTb3gBmMw9Ek%2Ftp%2BaIfAMdxPR08uJM1ecda3EIMuKnrS1BVSvh%2FoX7PxYNyz3JJVOCrMzPRl%2BTJ%2B6jj3cuBMbIlw3KIAVD%2F9iwFj%2F3RFHfHHLuztyPdO1gzRdQ3rGZ0uDY6cuGPjPFPdRQbiuHrScN5WjUevPpNyYeyqyW3x2thkPJcercZ62qPxuRwla7ns5qUn9tMP4hEIVptHBjTbDyXrSsF7n5ITsD8ZwxNq3lkUp5OCwHS6n%2FKiFfm2Pw5Vx9il36HpFAL9BnFqgQUHDhdlmzUieWSwm2KfnKkJfT%2FM6R%2FeWYxIu5x%2B8%2BGrQswp6LrywY6pgGZeTiwz5gYkcWai4fDDTkYvCs4vYhi4sGQgdE9ucPLFdg8eEMH8VInrTPiaRNXoqC395AyxQK9PuXwMP%2BTZu2uy85uriK3iNC93pQfzxYa41utwa%2BMtwpX8QDazF2UKRim%2FCmT6MZYEMzYUysz2GyfMwSGjyPcmjQYWVRGdYx0SpVh05LYr6NMp%2FA%2FGMXPIU%2FXBii0wjEe0JwQD75RN9Z1lHJ5YNOg&X-Amz-Signature=0cac650dffcd12b9c54e9cce88ab62542ef0125eb50a8b83d39808d65343ae59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4FEJSS%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArlckDvUB7TeweoCawrMuYyOhYlrrOiUw8PXNRKhwXPAiAId6gyEbDiBD1cz64xWTe72mRN5r%2BwXAMHELkyy%2BemGSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMGfwd1eSd3bHMXCU5KtwDVgJlZgOoc4Cax%2BbNJfRNXt7AOMeVRYdj92efJZI4pNo8zeqKuheKWASht8UZyh877EyZu2wgbHR6hu9kgjekiEMkCaxxZAHT0C1Mh52DEqkwfv3DsH6F9tgqlOGgJPBV0VZ2lAxl44NH5SbTyMrt7S4%2BCLzc0XXE1YrUade09OjiHfKERm1MX40qD32LlZF2S4AveL93gzY%2Fs2CwGFzX0esQSsczA6rM%2FLGWLNOGMgjMW3Ft3E9s8rLYQZ69ZO3n2NBLD%2BGZJCyxwlAf2j0LmqbT49qLSEZet1hN3GrdZFSVp9rlbM9W4%2Ban0xkLbRTb3gBmMw9Ek%2Ftp%2BaIfAMdxPR08uJM1ecda3EIMuKnrS1BVSvh%2FoX7PxYNyz3JJVOCrMzPRl%2BTJ%2B6jj3cuBMbIlw3KIAVD%2F9iwFj%2F3RFHfHHLuztyPdO1gzRdQ3rGZ0uDY6cuGPjPFPdRQbiuHrScN5WjUevPpNyYeyqyW3x2thkPJcercZ62qPxuRwla7ns5qUn9tMP4hEIVptHBjTbDyXrSsF7n5ITsD8ZwxNq3lkUp5OCwHS6n%2FKiFfm2Pw5Vx9il36HpFAL9BnFqgQUHDhdlmzUieWSwm2KfnKkJfT%2FM6R%2FeWYxIu5x%2B8%2BGrQswp6LrywY6pgGZeTiwz5gYkcWai4fDDTkYvCs4vYhi4sGQgdE9ucPLFdg8eEMH8VInrTPiaRNXoqC395AyxQK9PuXwMP%2BTZu2uy85uriK3iNC93pQfzxYa41utwa%2BMtwpX8QDazF2UKRim%2FCmT6MZYEMzYUysz2GyfMwSGjyPcmjQYWVRGdYx0SpVh05LYr6NMp%2FA%2FGMXPIU%2FXBii0wjEe0JwQD75RN9Z1lHJ5YNOg&X-Amz-Signature=dfaf99065687ba4896b7913da0e82b20cd242446a88d9ac3e491537b4dc77e34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

