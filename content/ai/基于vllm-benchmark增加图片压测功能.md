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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OAXW3RS%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCICEvkskBjtCNUtSKjGVv430L%2FsOBqlyEGTvXGPeeJqjiAiBNXO6bA6HCT8a48kufbgTnY0M%2FrsmhliyUqpqk5k2dtCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy0NYhOHv5ObEm7DaKtwD%2FIlw2bPpBMDk%2F5r1N6QY8FTVyywWRbK3IcrYWrEXmqbAmPPTjLhjtX7hoiqC43Pv049vDOKoVSCmc3%2BZ0XZ142DRmbR48tp3a4R11RSGQ%2B%2FIpDj3kbmyQ9gegibAYB2rKpm9rBqb9l6m4gFTmEjd13RJfMx0Zhfs4OErGKyFz5gyuxbL8kSrVBcRrV1%2FoPv3oXYTaxbNEa7swnQ1S%2FWj4ivk9efYAdP12TDO5pb4J4v87YPJJJN60brMNNSCQ3mHsCM8%2FZsKztCfyXq1M%2BnQtxur9wzqkeEW0I1xsx%2BYO6M8X8Km6C8nd%2FSnpzRaN2xJcy%2Bwa48Hlgk7YJfd802knxX5SdceBSUB%2F31i1vy9%2FNaktiCL5r54pTW3XgGQqugcqWnN8balA1qecz4nUrSw4kjggfq8FxPhi8XnOxPNJ%2F%2FbGxN%2BCsDsgARl266CDuNUeCmTU847JKYYJokhGl02IY6VBPiQUm6HoLpaw5fMtMSCYeF0kuch7e7WmGniqW56rSiF%2B%2FgliIqYm2nr8gt%2BopWCP%2FXVHc%2Bukw9SyaltHkw%2FnVwrqcItxzN42B%2BVDl%2FCQDHV9M6h%2FVT8%2BZ0wSQG955FDTsNAwtJrzYF2PFtEQkt8mp6NtJohqhAYw8Qw87%2FjyQY6pgEQhUXOIOWh6Y%2F6stgUUB6uZlqRxM8s%2F%2FhkfmcNtKAc8%2FKN14myL54wsEjbKD4aLHzRZv9te%2BQ%2FY5RvwAw0enatTIf2NgfyCyHSupHQlPr8gg3nYP90XoNhdw82vHtC2x7X%2BMkKL1VpVxhWuxHkjUZyTIfAc7lqabnnnIDTQZQ%2FelGwojmcJQ1pfJNQEwxGaUuHyz9JtaB1NzOmVBmgKQW5csCRyos8&X-Amz-Signature=737c08e0b7c18edc531c27faca9f1403badbe9bc24dc4d84348d98b5df4d94e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OAXW3RS%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCICEvkskBjtCNUtSKjGVv430L%2FsOBqlyEGTvXGPeeJqjiAiBNXO6bA6HCT8a48kufbgTnY0M%2FrsmhliyUqpqk5k2dtCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy0NYhOHv5ObEm7DaKtwD%2FIlw2bPpBMDk%2F5r1N6QY8FTVyywWRbK3IcrYWrEXmqbAmPPTjLhjtX7hoiqC43Pv049vDOKoVSCmc3%2BZ0XZ142DRmbR48tp3a4R11RSGQ%2B%2FIpDj3kbmyQ9gegibAYB2rKpm9rBqb9l6m4gFTmEjd13RJfMx0Zhfs4OErGKyFz5gyuxbL8kSrVBcRrV1%2FoPv3oXYTaxbNEa7swnQ1S%2FWj4ivk9efYAdP12TDO5pb4J4v87YPJJJN60brMNNSCQ3mHsCM8%2FZsKztCfyXq1M%2BnQtxur9wzqkeEW0I1xsx%2BYO6M8X8Km6C8nd%2FSnpzRaN2xJcy%2Bwa48Hlgk7YJfd802knxX5SdceBSUB%2F31i1vy9%2FNaktiCL5r54pTW3XgGQqugcqWnN8balA1qecz4nUrSw4kjggfq8FxPhi8XnOxPNJ%2F%2FbGxN%2BCsDsgARl266CDuNUeCmTU847JKYYJokhGl02IY6VBPiQUm6HoLpaw5fMtMSCYeF0kuch7e7WmGniqW56rSiF%2B%2FgliIqYm2nr8gt%2BopWCP%2FXVHc%2Bukw9SyaltHkw%2FnVwrqcItxzN42B%2BVDl%2FCQDHV9M6h%2FVT8%2BZ0wSQG955FDTsNAwtJrzYF2PFtEQkt8mp6NtJohqhAYw8Qw87%2FjyQY6pgEQhUXOIOWh6Y%2F6stgUUB6uZlqRxM8s%2F%2FhkfmcNtKAc8%2FKN14myL54wsEjbKD4aLHzRZv9te%2BQ%2FY5RvwAw0enatTIf2NgfyCyHSupHQlPr8gg3nYP90XoNhdw82vHtC2x7X%2BMkKL1VpVxhWuxHkjUZyTIfAc7lqabnnnIDTQZQ%2FelGwojmcJQ1pfJNQEwxGaUuHyz9JtaB1NzOmVBmgKQW5csCRyos8&X-Amz-Signature=997ba9aae8c43570d06b9942f3b7077fc55c58a2c6708f02529ccce3b6d5b677&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OAXW3RS%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCICEvkskBjtCNUtSKjGVv430L%2FsOBqlyEGTvXGPeeJqjiAiBNXO6bA6HCT8a48kufbgTnY0M%2FrsmhliyUqpqk5k2dtCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy0NYhOHv5ObEm7DaKtwD%2FIlw2bPpBMDk%2F5r1N6QY8FTVyywWRbK3IcrYWrEXmqbAmPPTjLhjtX7hoiqC43Pv049vDOKoVSCmc3%2BZ0XZ142DRmbR48tp3a4R11RSGQ%2B%2FIpDj3kbmyQ9gegibAYB2rKpm9rBqb9l6m4gFTmEjd13RJfMx0Zhfs4OErGKyFz5gyuxbL8kSrVBcRrV1%2FoPv3oXYTaxbNEa7swnQ1S%2FWj4ivk9efYAdP12TDO5pb4J4v87YPJJJN60brMNNSCQ3mHsCM8%2FZsKztCfyXq1M%2BnQtxur9wzqkeEW0I1xsx%2BYO6M8X8Km6C8nd%2FSnpzRaN2xJcy%2Bwa48Hlgk7YJfd802knxX5SdceBSUB%2F31i1vy9%2FNaktiCL5r54pTW3XgGQqugcqWnN8balA1qecz4nUrSw4kjggfq8FxPhi8XnOxPNJ%2F%2FbGxN%2BCsDsgARl266CDuNUeCmTU847JKYYJokhGl02IY6VBPiQUm6HoLpaw5fMtMSCYeF0kuch7e7WmGniqW56rSiF%2B%2FgliIqYm2nr8gt%2BopWCP%2FXVHc%2Bukw9SyaltHkw%2FnVwrqcItxzN42B%2BVDl%2FCQDHV9M6h%2FVT8%2BZ0wSQG955FDTsNAwtJrzYF2PFtEQkt8mp6NtJohqhAYw8Qw87%2FjyQY6pgEQhUXOIOWh6Y%2F6stgUUB6uZlqRxM8s%2F%2FhkfmcNtKAc8%2FKN14myL54wsEjbKD4aLHzRZv9te%2BQ%2FY5RvwAw0enatTIf2NgfyCyHSupHQlPr8gg3nYP90XoNhdw82vHtC2x7X%2BMkKL1VpVxhWuxHkjUZyTIfAc7lqabnnnIDTQZQ%2FelGwojmcJQ1pfJNQEwxGaUuHyz9JtaB1NzOmVBmgKQW5csCRyos8&X-Amz-Signature=b5389d3aca18262674bf948579b86b31c75dcc40147a2b21e0ab678d27724692&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OAXW3RS%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCICEvkskBjtCNUtSKjGVv430L%2FsOBqlyEGTvXGPeeJqjiAiBNXO6bA6HCT8a48kufbgTnY0M%2FrsmhliyUqpqk5k2dtCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy0NYhOHv5ObEm7DaKtwD%2FIlw2bPpBMDk%2F5r1N6QY8FTVyywWRbK3IcrYWrEXmqbAmPPTjLhjtX7hoiqC43Pv049vDOKoVSCmc3%2BZ0XZ142DRmbR48tp3a4R11RSGQ%2B%2FIpDj3kbmyQ9gegibAYB2rKpm9rBqb9l6m4gFTmEjd13RJfMx0Zhfs4OErGKyFz5gyuxbL8kSrVBcRrV1%2FoPv3oXYTaxbNEa7swnQ1S%2FWj4ivk9efYAdP12TDO5pb4J4v87YPJJJN60brMNNSCQ3mHsCM8%2FZsKztCfyXq1M%2BnQtxur9wzqkeEW0I1xsx%2BYO6M8X8Km6C8nd%2FSnpzRaN2xJcy%2Bwa48Hlgk7YJfd802knxX5SdceBSUB%2F31i1vy9%2FNaktiCL5r54pTW3XgGQqugcqWnN8balA1qecz4nUrSw4kjggfq8FxPhi8XnOxPNJ%2F%2FbGxN%2BCsDsgARl266CDuNUeCmTU847JKYYJokhGl02IY6VBPiQUm6HoLpaw5fMtMSCYeF0kuch7e7WmGniqW56rSiF%2B%2FgliIqYm2nr8gt%2BopWCP%2FXVHc%2Bukw9SyaltHkw%2FnVwrqcItxzN42B%2BVDl%2FCQDHV9M6h%2FVT8%2BZ0wSQG955FDTsNAwtJrzYF2PFtEQkt8mp6NtJohqhAYw8Qw87%2FjyQY6pgEQhUXOIOWh6Y%2F6stgUUB6uZlqRxM8s%2F%2FhkfmcNtKAc8%2FKN14myL54wsEjbKD4aLHzRZv9te%2BQ%2FY5RvwAw0enatTIf2NgfyCyHSupHQlPr8gg3nYP90XoNhdw82vHtC2x7X%2BMkKL1VpVxhWuxHkjUZyTIfAc7lqabnnnIDTQZQ%2FelGwojmcJQ1pfJNQEwxGaUuHyz9JtaB1NzOmVBmgKQW5csCRyos8&X-Amz-Signature=d49c4d1c00c40dc57103050d2bc35ce2e9a95dc4dbb8bfef552fb5efe497bec5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OAXW3RS%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCICEvkskBjtCNUtSKjGVv430L%2FsOBqlyEGTvXGPeeJqjiAiBNXO6bA6HCT8a48kufbgTnY0M%2FrsmhliyUqpqk5k2dtCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy0NYhOHv5ObEm7DaKtwD%2FIlw2bPpBMDk%2F5r1N6QY8FTVyywWRbK3IcrYWrEXmqbAmPPTjLhjtX7hoiqC43Pv049vDOKoVSCmc3%2BZ0XZ142DRmbR48tp3a4R11RSGQ%2B%2FIpDj3kbmyQ9gegibAYB2rKpm9rBqb9l6m4gFTmEjd13RJfMx0Zhfs4OErGKyFz5gyuxbL8kSrVBcRrV1%2FoPv3oXYTaxbNEa7swnQ1S%2FWj4ivk9efYAdP12TDO5pb4J4v87YPJJJN60brMNNSCQ3mHsCM8%2FZsKztCfyXq1M%2BnQtxur9wzqkeEW0I1xsx%2BYO6M8X8Km6C8nd%2FSnpzRaN2xJcy%2Bwa48Hlgk7YJfd802knxX5SdceBSUB%2F31i1vy9%2FNaktiCL5r54pTW3XgGQqugcqWnN8balA1qecz4nUrSw4kjggfq8FxPhi8XnOxPNJ%2F%2FbGxN%2BCsDsgARl266CDuNUeCmTU847JKYYJokhGl02IY6VBPiQUm6HoLpaw5fMtMSCYeF0kuch7e7WmGniqW56rSiF%2B%2FgliIqYm2nr8gt%2BopWCP%2FXVHc%2Bukw9SyaltHkw%2FnVwrqcItxzN42B%2BVDl%2FCQDHV9M6h%2FVT8%2BZ0wSQG955FDTsNAwtJrzYF2PFtEQkt8mp6NtJohqhAYw8Qw87%2FjyQY6pgEQhUXOIOWh6Y%2F6stgUUB6uZlqRxM8s%2F%2FhkfmcNtKAc8%2FKN14myL54wsEjbKD4aLHzRZv9te%2BQ%2FY5RvwAw0enatTIf2NgfyCyHSupHQlPr8gg3nYP90XoNhdw82vHtC2x7X%2BMkKL1VpVxhWuxHkjUZyTIfAc7lqabnnnIDTQZQ%2FelGwojmcJQ1pfJNQEwxGaUuHyz9JtaB1NzOmVBmgKQW5csCRyos8&X-Amz-Signature=6b7d682f4b18968440860593a42a835e6575e035bdb9713b5f79ab8fed0a527a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

