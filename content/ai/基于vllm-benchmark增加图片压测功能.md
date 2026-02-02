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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DFBJOOZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQC6ipSoB8QUyx8dzpwWi4zA0R1qwKIzXDZBD6QOYtHp9wIhAKZJGyKuy2uoEz%2BWv8YwT8WnyuGDKVBKOcx9tKbrLFhzKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGFObFe6RgsFK7a7Uq3ANZ7wO2QuUdMEEU%2Bqn50RXvcH5J%2FseY3xRnqOV4lhv22oFRMpCXDYj7RI6K1gJ2QA76QplCLVt8v2bRDyfDR67AGhRaNJJne5ZgX11NjGSKI89W60%2BnMNRvzhaJlu%2FbGxrV%2B51xTJcWTR3Pwq%2F7vXpkY6Hjk2p3qO%2BjzZIJS3iqZR5X%2Bbqw9yeaSqdu1KL%2BA9FXaN0yDtS74v0fmN%2Fl%2F3XJ21Axp8yMXJ94QIqDjRV79QN8WZoot5nvGOZHosVUxFNpRs1xYlhVB%2FjHTN7l3UIimDivSIt1bYGEdkfRCd7kdsqgyHKx23x8tDMtlsNfRA6k1QSFTEnY2HIssaOgB4zuRj46kL0nme4wl1y6r5DIuhr%2BMYUW9B7ApQOtTgTUzdVb2ZjR2MnkhXJxKFdfaCzJ%2BIO%2BN%2BpMultHhNBPMywrMfCGnvD1dP3MJMwmhWuBhtB6bxTtxWqz8GXCmKeCGTFh03E%2B3r5VNBsdsI%2B9uXvdHHEp9o6Kjs%2B8xQy5l4z75BWXP88yq3Wgwdhyyydk8ioIdAwbrn8URrFEJDrohPl4Ox6%2FK3ybWWPThkTxhdc2YLmBLMN5SMyTHmZaIu1hAywl6bMTmiEqagMEFmRKWpGqmepLXS2jcGAJrS0mPzDGhoDMBjqkAcYO3hxF6WkTmW12MMwdr9RqD5%2F3C%2FdCQJyXl3TN7sGXN10hAbltw1%2F55xNW5ciWoQ%2FNqTAtHsQIOtUXVFa%2FNs%2FNdbtUwJ9C0RnANAOnnbJusjE23NdCAaChWnaKHNaFXH%2FdJ7xxyBpnZbfmdzKkjG3xBxS3RUu%2FFzZUtTH4Jz1EVg05A%2B7nZdVWpsJ8KhQNyKBhZDCZp0xkwyGkBAZWBj73GHlR&X-Amz-Signature=202cd1619e00b44430c6630fa64a1c4de54c20b64d70807663e6bdfe0e65c4d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DFBJOOZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQC6ipSoB8QUyx8dzpwWi4zA0R1qwKIzXDZBD6QOYtHp9wIhAKZJGyKuy2uoEz%2BWv8YwT8WnyuGDKVBKOcx9tKbrLFhzKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGFObFe6RgsFK7a7Uq3ANZ7wO2QuUdMEEU%2Bqn50RXvcH5J%2FseY3xRnqOV4lhv22oFRMpCXDYj7RI6K1gJ2QA76QplCLVt8v2bRDyfDR67AGhRaNJJne5ZgX11NjGSKI89W60%2BnMNRvzhaJlu%2FbGxrV%2B51xTJcWTR3Pwq%2F7vXpkY6Hjk2p3qO%2BjzZIJS3iqZR5X%2Bbqw9yeaSqdu1KL%2BA9FXaN0yDtS74v0fmN%2Fl%2F3XJ21Axp8yMXJ94QIqDjRV79QN8WZoot5nvGOZHosVUxFNpRs1xYlhVB%2FjHTN7l3UIimDivSIt1bYGEdkfRCd7kdsqgyHKx23x8tDMtlsNfRA6k1QSFTEnY2HIssaOgB4zuRj46kL0nme4wl1y6r5DIuhr%2BMYUW9B7ApQOtTgTUzdVb2ZjR2MnkhXJxKFdfaCzJ%2BIO%2BN%2BpMultHhNBPMywrMfCGnvD1dP3MJMwmhWuBhtB6bxTtxWqz8GXCmKeCGTFh03E%2B3r5VNBsdsI%2B9uXvdHHEp9o6Kjs%2B8xQy5l4z75BWXP88yq3Wgwdhyyydk8ioIdAwbrn8URrFEJDrohPl4Ox6%2FK3ybWWPThkTxhdc2YLmBLMN5SMyTHmZaIu1hAywl6bMTmiEqagMEFmRKWpGqmepLXS2jcGAJrS0mPzDGhoDMBjqkAcYO3hxF6WkTmW12MMwdr9RqD5%2F3C%2FdCQJyXl3TN7sGXN10hAbltw1%2F55xNW5ciWoQ%2FNqTAtHsQIOtUXVFa%2FNs%2FNdbtUwJ9C0RnANAOnnbJusjE23NdCAaChWnaKHNaFXH%2FdJ7xxyBpnZbfmdzKkjG3xBxS3RUu%2FFzZUtTH4Jz1EVg05A%2B7nZdVWpsJ8KhQNyKBhZDCZp0xkwyGkBAZWBj73GHlR&X-Amz-Signature=c8d0376bfbad05fd8d8c444b8e7cd9569c47cd843b8aa1c97709007cba4e7c41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DFBJOOZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQC6ipSoB8QUyx8dzpwWi4zA0R1qwKIzXDZBD6QOYtHp9wIhAKZJGyKuy2uoEz%2BWv8YwT8WnyuGDKVBKOcx9tKbrLFhzKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGFObFe6RgsFK7a7Uq3ANZ7wO2QuUdMEEU%2Bqn50RXvcH5J%2FseY3xRnqOV4lhv22oFRMpCXDYj7RI6K1gJ2QA76QplCLVt8v2bRDyfDR67AGhRaNJJne5ZgX11NjGSKI89W60%2BnMNRvzhaJlu%2FbGxrV%2B51xTJcWTR3Pwq%2F7vXpkY6Hjk2p3qO%2BjzZIJS3iqZR5X%2Bbqw9yeaSqdu1KL%2BA9FXaN0yDtS74v0fmN%2Fl%2F3XJ21Axp8yMXJ94QIqDjRV79QN8WZoot5nvGOZHosVUxFNpRs1xYlhVB%2FjHTN7l3UIimDivSIt1bYGEdkfRCd7kdsqgyHKx23x8tDMtlsNfRA6k1QSFTEnY2HIssaOgB4zuRj46kL0nme4wl1y6r5DIuhr%2BMYUW9B7ApQOtTgTUzdVb2ZjR2MnkhXJxKFdfaCzJ%2BIO%2BN%2BpMultHhNBPMywrMfCGnvD1dP3MJMwmhWuBhtB6bxTtxWqz8GXCmKeCGTFh03E%2B3r5VNBsdsI%2B9uXvdHHEp9o6Kjs%2B8xQy5l4z75BWXP88yq3Wgwdhyyydk8ioIdAwbrn8URrFEJDrohPl4Ox6%2FK3ybWWPThkTxhdc2YLmBLMN5SMyTHmZaIu1hAywl6bMTmiEqagMEFmRKWpGqmepLXS2jcGAJrS0mPzDGhoDMBjqkAcYO3hxF6WkTmW12MMwdr9RqD5%2F3C%2FdCQJyXl3TN7sGXN10hAbltw1%2F55xNW5ciWoQ%2FNqTAtHsQIOtUXVFa%2FNs%2FNdbtUwJ9C0RnANAOnnbJusjE23NdCAaChWnaKHNaFXH%2FdJ7xxyBpnZbfmdzKkjG3xBxS3RUu%2FFzZUtTH4Jz1EVg05A%2B7nZdVWpsJ8KhQNyKBhZDCZp0xkwyGkBAZWBj73GHlR&X-Amz-Signature=fc53015dea938eba91655a5fee373e78b265673e1c042fe1eef018a0578c30c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DFBJOOZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQC6ipSoB8QUyx8dzpwWi4zA0R1qwKIzXDZBD6QOYtHp9wIhAKZJGyKuy2uoEz%2BWv8YwT8WnyuGDKVBKOcx9tKbrLFhzKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGFObFe6RgsFK7a7Uq3ANZ7wO2QuUdMEEU%2Bqn50RXvcH5J%2FseY3xRnqOV4lhv22oFRMpCXDYj7RI6K1gJ2QA76QplCLVt8v2bRDyfDR67AGhRaNJJne5ZgX11NjGSKI89W60%2BnMNRvzhaJlu%2FbGxrV%2B51xTJcWTR3Pwq%2F7vXpkY6Hjk2p3qO%2BjzZIJS3iqZR5X%2Bbqw9yeaSqdu1KL%2BA9FXaN0yDtS74v0fmN%2Fl%2F3XJ21Axp8yMXJ94QIqDjRV79QN8WZoot5nvGOZHosVUxFNpRs1xYlhVB%2FjHTN7l3UIimDivSIt1bYGEdkfRCd7kdsqgyHKx23x8tDMtlsNfRA6k1QSFTEnY2HIssaOgB4zuRj46kL0nme4wl1y6r5DIuhr%2BMYUW9B7ApQOtTgTUzdVb2ZjR2MnkhXJxKFdfaCzJ%2BIO%2BN%2BpMultHhNBPMywrMfCGnvD1dP3MJMwmhWuBhtB6bxTtxWqz8GXCmKeCGTFh03E%2B3r5VNBsdsI%2B9uXvdHHEp9o6Kjs%2B8xQy5l4z75BWXP88yq3Wgwdhyyydk8ioIdAwbrn8URrFEJDrohPl4Ox6%2FK3ybWWPThkTxhdc2YLmBLMN5SMyTHmZaIu1hAywl6bMTmiEqagMEFmRKWpGqmepLXS2jcGAJrS0mPzDGhoDMBjqkAcYO3hxF6WkTmW12MMwdr9RqD5%2F3C%2FdCQJyXl3TN7sGXN10hAbltw1%2F55xNW5ciWoQ%2FNqTAtHsQIOtUXVFa%2FNs%2FNdbtUwJ9C0RnANAOnnbJusjE23NdCAaChWnaKHNaFXH%2FdJ7xxyBpnZbfmdzKkjG3xBxS3RUu%2FFzZUtTH4Jz1EVg05A%2B7nZdVWpsJ8KhQNyKBhZDCZp0xkwyGkBAZWBj73GHlR&X-Amz-Signature=de853a261f72aee865745c4dc6c4776e3b8acadbaf36836ea1318f58721ab878&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DFBJOOZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQC6ipSoB8QUyx8dzpwWi4zA0R1qwKIzXDZBD6QOYtHp9wIhAKZJGyKuy2uoEz%2BWv8YwT8WnyuGDKVBKOcx9tKbrLFhzKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGFObFe6RgsFK7a7Uq3ANZ7wO2QuUdMEEU%2Bqn50RXvcH5J%2FseY3xRnqOV4lhv22oFRMpCXDYj7RI6K1gJ2QA76QplCLVt8v2bRDyfDR67AGhRaNJJne5ZgX11NjGSKI89W60%2BnMNRvzhaJlu%2FbGxrV%2B51xTJcWTR3Pwq%2F7vXpkY6Hjk2p3qO%2BjzZIJS3iqZR5X%2Bbqw9yeaSqdu1KL%2BA9FXaN0yDtS74v0fmN%2Fl%2F3XJ21Axp8yMXJ94QIqDjRV79QN8WZoot5nvGOZHosVUxFNpRs1xYlhVB%2FjHTN7l3UIimDivSIt1bYGEdkfRCd7kdsqgyHKx23x8tDMtlsNfRA6k1QSFTEnY2HIssaOgB4zuRj46kL0nme4wl1y6r5DIuhr%2BMYUW9B7ApQOtTgTUzdVb2ZjR2MnkhXJxKFdfaCzJ%2BIO%2BN%2BpMultHhNBPMywrMfCGnvD1dP3MJMwmhWuBhtB6bxTtxWqz8GXCmKeCGTFh03E%2B3r5VNBsdsI%2B9uXvdHHEp9o6Kjs%2B8xQy5l4z75BWXP88yq3Wgwdhyyydk8ioIdAwbrn8URrFEJDrohPl4Ox6%2FK3ybWWPThkTxhdc2YLmBLMN5SMyTHmZaIu1hAywl6bMTmiEqagMEFmRKWpGqmepLXS2jcGAJrS0mPzDGhoDMBjqkAcYO3hxF6WkTmW12MMwdr9RqD5%2F3C%2FdCQJyXl3TN7sGXN10hAbltw1%2F55xNW5ciWoQ%2FNqTAtHsQIOtUXVFa%2FNs%2FNdbtUwJ9C0RnANAOnnbJusjE23NdCAaChWnaKHNaFXH%2FdJ7xxyBpnZbfmdzKkjG3xBxS3RUu%2FFzZUtTH4Jz1EVg05A%2B7nZdVWpsJ8KhQNyKBhZDCZp0xkwyGkBAZWBj73GHlR&X-Amz-Signature=7177f67bdd80c6c0b0781ddc188ace84fdf3e1877005e065a40b541822e6020c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

