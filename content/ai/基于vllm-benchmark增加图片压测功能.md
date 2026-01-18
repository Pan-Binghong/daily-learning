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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RIZLMKO%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz5cW6LP%2FVLunL%2FhTo%2BT8enCyG7qEMW9ATKQi7GAVR6QIhAN5hSrievGDM%2BPRyoC1JsJg8NUwlf6dLH2zRc3q38xuYKv8DCHMQABoMNjM3NDIzMTgzODA1IgxeZpWEBlQzb%2Fd9tNgq3APLgFSfdGwtI89cZzNq9HSp6zRkU5OLhGo%2BM9ykW03cjfc43dSRmZ8kYqS%2F6%2Fcq%2BKc1fvsw%2Bz%2BIibJG%2BiS9zgIPRAEerQ7zyOIaaPpjUSa8eJWZS50ODpT3EySOGPh7%2BxSU6v%2BPQtO7n%2FhoTqNyMW5HFInti%2FUC9fDGVk%2F94gIhVgAocqeD%2B2kjHzdf1%2FeAr2UGs2SG8n9V7k3gx6mtZC82Ym3UgGTt6sq2rS5SJ1XX2jINgeMi8sdvPrPHxxU82d0ew14gNS5EniLsf%2BpS7E2aQEVVW8yjgPaK5dsA3KnN40SGCvGzFQKJ0FIP8bIyFACr0p8B0GUMIMDXmbjSPyzWMdTPrY354xGnA4oYU8V4MdgckqCr%2F4KugPea4G0KfcnPeIc5Fp0dVJ33UVVWhJO%2FJ%2BpKeB7RP0QfPcp2EyeJIpn1vSpe4V9ahPfWDSbccR3UaKWJrlnX3u5YUyFrlRZcQVEU4jtzv%2B2AP6sj6kKZzVqPnXQEkla%2BOQJssrF37VrnOy1kVHCPIEqxDYf4NBY6M%2FcCggCw56xBM%2BMpFiSNOCNmBmw6CvvBWD8asqN4D3WQcey0hfyB0iUDj7owoRyXW7wbJPqvzVq%2Fml1FInD7thXEF0pJQGGBqs2MjTCUgrHLBjqkAV2T29wK46MpbK35t3lI98nl7MdyfQKsIs0O6Ztau%2FNc05ip0g5xGdVZ6yiSle%2Fr1DBZz6lsQwdf90K8v7%2BYW3UTbjUtfHjz0Myflm4kziwcYHDZLRApP0I0s2DMxD%2F265umcFJl649lUmD0TAadZrORvujTRhK55%2BlsEuNV3E9YQ4MHoz9fR%2B5wI7imci867pBxcrFtM4NYF0O3KUOnGOWdlkPb&X-Amz-Signature=68e267fb524e71da9127c31d38d034fa126a69de226e0ff0019ed9c3d7686c73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RIZLMKO%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz5cW6LP%2FVLunL%2FhTo%2BT8enCyG7qEMW9ATKQi7GAVR6QIhAN5hSrievGDM%2BPRyoC1JsJg8NUwlf6dLH2zRc3q38xuYKv8DCHMQABoMNjM3NDIzMTgzODA1IgxeZpWEBlQzb%2Fd9tNgq3APLgFSfdGwtI89cZzNq9HSp6zRkU5OLhGo%2BM9ykW03cjfc43dSRmZ8kYqS%2F6%2Fcq%2BKc1fvsw%2Bz%2BIibJG%2BiS9zgIPRAEerQ7zyOIaaPpjUSa8eJWZS50ODpT3EySOGPh7%2BxSU6v%2BPQtO7n%2FhoTqNyMW5HFInti%2FUC9fDGVk%2F94gIhVgAocqeD%2B2kjHzdf1%2FeAr2UGs2SG8n9V7k3gx6mtZC82Ym3UgGTt6sq2rS5SJ1XX2jINgeMi8sdvPrPHxxU82d0ew14gNS5EniLsf%2BpS7E2aQEVVW8yjgPaK5dsA3KnN40SGCvGzFQKJ0FIP8bIyFACr0p8B0GUMIMDXmbjSPyzWMdTPrY354xGnA4oYU8V4MdgckqCr%2F4KugPea4G0KfcnPeIc5Fp0dVJ33UVVWhJO%2FJ%2BpKeB7RP0QfPcp2EyeJIpn1vSpe4V9ahPfWDSbccR3UaKWJrlnX3u5YUyFrlRZcQVEU4jtzv%2B2AP6sj6kKZzVqPnXQEkla%2BOQJssrF37VrnOy1kVHCPIEqxDYf4NBY6M%2FcCggCw56xBM%2BMpFiSNOCNmBmw6CvvBWD8asqN4D3WQcey0hfyB0iUDj7owoRyXW7wbJPqvzVq%2Fml1FInD7thXEF0pJQGGBqs2MjTCUgrHLBjqkAV2T29wK46MpbK35t3lI98nl7MdyfQKsIs0O6Ztau%2FNc05ip0g5xGdVZ6yiSle%2Fr1DBZz6lsQwdf90K8v7%2BYW3UTbjUtfHjz0Myflm4kziwcYHDZLRApP0I0s2DMxD%2F265umcFJl649lUmD0TAadZrORvujTRhK55%2BlsEuNV3E9YQ4MHoz9fR%2B5wI7imci867pBxcrFtM4NYF0O3KUOnGOWdlkPb&X-Amz-Signature=777142a445a82ddc9de34480c1fc23f506ce65fbecfd97960069bbff7fcb586c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RIZLMKO%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz5cW6LP%2FVLunL%2FhTo%2BT8enCyG7qEMW9ATKQi7GAVR6QIhAN5hSrievGDM%2BPRyoC1JsJg8NUwlf6dLH2zRc3q38xuYKv8DCHMQABoMNjM3NDIzMTgzODA1IgxeZpWEBlQzb%2Fd9tNgq3APLgFSfdGwtI89cZzNq9HSp6zRkU5OLhGo%2BM9ykW03cjfc43dSRmZ8kYqS%2F6%2Fcq%2BKc1fvsw%2Bz%2BIibJG%2BiS9zgIPRAEerQ7zyOIaaPpjUSa8eJWZS50ODpT3EySOGPh7%2BxSU6v%2BPQtO7n%2FhoTqNyMW5HFInti%2FUC9fDGVk%2F94gIhVgAocqeD%2B2kjHzdf1%2FeAr2UGs2SG8n9V7k3gx6mtZC82Ym3UgGTt6sq2rS5SJ1XX2jINgeMi8sdvPrPHxxU82d0ew14gNS5EniLsf%2BpS7E2aQEVVW8yjgPaK5dsA3KnN40SGCvGzFQKJ0FIP8bIyFACr0p8B0GUMIMDXmbjSPyzWMdTPrY354xGnA4oYU8V4MdgckqCr%2F4KugPea4G0KfcnPeIc5Fp0dVJ33UVVWhJO%2FJ%2BpKeB7RP0QfPcp2EyeJIpn1vSpe4V9ahPfWDSbccR3UaKWJrlnX3u5YUyFrlRZcQVEU4jtzv%2B2AP6sj6kKZzVqPnXQEkla%2BOQJssrF37VrnOy1kVHCPIEqxDYf4NBY6M%2FcCggCw56xBM%2BMpFiSNOCNmBmw6CvvBWD8asqN4D3WQcey0hfyB0iUDj7owoRyXW7wbJPqvzVq%2Fml1FInD7thXEF0pJQGGBqs2MjTCUgrHLBjqkAV2T29wK46MpbK35t3lI98nl7MdyfQKsIs0O6Ztau%2FNc05ip0g5xGdVZ6yiSle%2Fr1DBZz6lsQwdf90K8v7%2BYW3UTbjUtfHjz0Myflm4kziwcYHDZLRApP0I0s2DMxD%2F265umcFJl649lUmD0TAadZrORvujTRhK55%2BlsEuNV3E9YQ4MHoz9fR%2B5wI7imci867pBxcrFtM4NYF0O3KUOnGOWdlkPb&X-Amz-Signature=e8c427912cd7908333d8412089be6fedc4a28abc4ee132639f98b57b4bc67a2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RIZLMKO%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz5cW6LP%2FVLunL%2FhTo%2BT8enCyG7qEMW9ATKQi7GAVR6QIhAN5hSrievGDM%2BPRyoC1JsJg8NUwlf6dLH2zRc3q38xuYKv8DCHMQABoMNjM3NDIzMTgzODA1IgxeZpWEBlQzb%2Fd9tNgq3APLgFSfdGwtI89cZzNq9HSp6zRkU5OLhGo%2BM9ykW03cjfc43dSRmZ8kYqS%2F6%2Fcq%2BKc1fvsw%2Bz%2BIibJG%2BiS9zgIPRAEerQ7zyOIaaPpjUSa8eJWZS50ODpT3EySOGPh7%2BxSU6v%2BPQtO7n%2FhoTqNyMW5HFInti%2FUC9fDGVk%2F94gIhVgAocqeD%2B2kjHzdf1%2FeAr2UGs2SG8n9V7k3gx6mtZC82Ym3UgGTt6sq2rS5SJ1XX2jINgeMi8sdvPrPHxxU82d0ew14gNS5EniLsf%2BpS7E2aQEVVW8yjgPaK5dsA3KnN40SGCvGzFQKJ0FIP8bIyFACr0p8B0GUMIMDXmbjSPyzWMdTPrY354xGnA4oYU8V4MdgckqCr%2F4KugPea4G0KfcnPeIc5Fp0dVJ33UVVWhJO%2FJ%2BpKeB7RP0QfPcp2EyeJIpn1vSpe4V9ahPfWDSbccR3UaKWJrlnX3u5YUyFrlRZcQVEU4jtzv%2B2AP6sj6kKZzVqPnXQEkla%2BOQJssrF37VrnOy1kVHCPIEqxDYf4NBY6M%2FcCggCw56xBM%2BMpFiSNOCNmBmw6CvvBWD8asqN4D3WQcey0hfyB0iUDj7owoRyXW7wbJPqvzVq%2Fml1FInD7thXEF0pJQGGBqs2MjTCUgrHLBjqkAV2T29wK46MpbK35t3lI98nl7MdyfQKsIs0O6Ztau%2FNc05ip0g5xGdVZ6yiSle%2Fr1DBZz6lsQwdf90K8v7%2BYW3UTbjUtfHjz0Myflm4kziwcYHDZLRApP0I0s2DMxD%2F265umcFJl649lUmD0TAadZrORvujTRhK55%2BlsEuNV3E9YQ4MHoz9fR%2B5wI7imci867pBxcrFtM4NYF0O3KUOnGOWdlkPb&X-Amz-Signature=0609139684d3a3a9a687aeb61a7075f6b1c92842b3cdee9508cff16e187ec5d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RIZLMKO%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz5cW6LP%2FVLunL%2FhTo%2BT8enCyG7qEMW9ATKQi7GAVR6QIhAN5hSrievGDM%2BPRyoC1JsJg8NUwlf6dLH2zRc3q38xuYKv8DCHMQABoMNjM3NDIzMTgzODA1IgxeZpWEBlQzb%2Fd9tNgq3APLgFSfdGwtI89cZzNq9HSp6zRkU5OLhGo%2BM9ykW03cjfc43dSRmZ8kYqS%2F6%2Fcq%2BKc1fvsw%2Bz%2BIibJG%2BiS9zgIPRAEerQ7zyOIaaPpjUSa8eJWZS50ODpT3EySOGPh7%2BxSU6v%2BPQtO7n%2FhoTqNyMW5HFInti%2FUC9fDGVk%2F94gIhVgAocqeD%2B2kjHzdf1%2FeAr2UGs2SG8n9V7k3gx6mtZC82Ym3UgGTt6sq2rS5SJ1XX2jINgeMi8sdvPrPHxxU82d0ew14gNS5EniLsf%2BpS7E2aQEVVW8yjgPaK5dsA3KnN40SGCvGzFQKJ0FIP8bIyFACr0p8B0GUMIMDXmbjSPyzWMdTPrY354xGnA4oYU8V4MdgckqCr%2F4KugPea4G0KfcnPeIc5Fp0dVJ33UVVWhJO%2FJ%2BpKeB7RP0QfPcp2EyeJIpn1vSpe4V9ahPfWDSbccR3UaKWJrlnX3u5YUyFrlRZcQVEU4jtzv%2B2AP6sj6kKZzVqPnXQEkla%2BOQJssrF37VrnOy1kVHCPIEqxDYf4NBY6M%2FcCggCw56xBM%2BMpFiSNOCNmBmw6CvvBWD8asqN4D3WQcey0hfyB0iUDj7owoRyXW7wbJPqvzVq%2Fml1FInD7thXEF0pJQGGBqs2MjTCUgrHLBjqkAV2T29wK46MpbK35t3lI98nl7MdyfQKsIs0O6Ztau%2FNc05ip0g5xGdVZ6yiSle%2Fr1DBZz6lsQwdf90K8v7%2BYW3UTbjUtfHjz0Myflm4kziwcYHDZLRApP0I0s2DMxD%2F265umcFJl649lUmD0TAadZrORvujTRhK55%2BlsEuNV3E9YQ4MHoz9fR%2B5wI7imci867pBxcrFtM4NYF0O3KUOnGOWdlkPb&X-Amz-Signature=fb46faa4fbb9081526f902ec783b4a46d4450f1a42e31dd099161213cdc46ca4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

