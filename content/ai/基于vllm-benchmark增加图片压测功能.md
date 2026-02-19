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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7O3DMK3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICN%2BjtggLqQwMxRNBetzxPYvmhNTZ9LtyZ2PihFBAIaCAiB%2Be6vJZUDcvuaogtbrsQbCDN%2FSWTiogB0ePo7HYLXjKCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMnG5AIQ3dTq4%2FpWjnKtwDwT%2BYZrH%2BTP9b7UNgVT%2B7aAk39rXX8lapsQAgIrGcJDmWhGP3T8ndXiMRsT5ZHoDCPFcZ8NNrbkueQHP4qSf3osppG60y%2FUPwHjvI%2BdmBQph%2Fo4IGJncoQykyFQLm3pS2zdtkkaxBIixm1maMzT%2B5Vm7D9qmoc%2FEVGskHVLsgmqUgbFZ8%2F4JorQq8pSouGidRSerY%2BJIVOMv2Vv7dcg4DSLfQ4ZbrKhe0gmAm6hoRDNeaqbGoGD83OdEKjyZY8n1vafbqvJ2YxMf0eLocKNxvcFIN198gfnEH%2F%2Bpkypm4nv%2FtVqLBvppGZnH5MuyzOeT7ySjqp9g47ihpfe%2BUIOlsEhbiYt24IGbwbec2fxNk%2BhWwydeoY0hK3654K15sZnJQ5q4RFK9ADYc62GaVTTv%2Blwgc1IlZyB3dzRbEhKTwsR1DXEzb5Kh19wvTOD1YtRZYCpHvtWbMTrCb%2FU6Qz95ve3auDKpNVTpI2l7HrAlgpj0dTMXuYNXd4B7KXqAb2gmW%2FGje70AVoa80Q6ZONB1uhG5qwIymP%2B4Q2xrmi7VqQhbfug1EM%2FjxHlU2nbpw4soSLytj7md9cghkA%2FyJj5WAnFad0ORvqUylztmJscqdOND8Qb0ZzWSPTd3gjtwwmPHZzAY6pgFKeURNJyG6yPB2e5j4bFPk3iHXJV8DSj8heeAM%2Blip5WfIepD2Ht1%2FASSpKnSzkqEbfcwbovxOw2CiqMZtHDBE6Z%2B0MNZse7nDlkGpqVL1TasSPnsERlWT8yuYttGiNdf5nsFcjNVWIjS2Fptc1zDDSIIta8Nd7jEpg9zBjDmr9MUwKJ%2BVZVCBGVC7WVALJL87Y47pZOIRhxwm34BXR0anLqeikl89&X-Amz-Signature=0d88278ee5e7fdb8d84748dcf08f260f9aface5f4cbdf0e9fa253c389c3e676b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7O3DMK3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICN%2BjtggLqQwMxRNBetzxPYvmhNTZ9LtyZ2PihFBAIaCAiB%2Be6vJZUDcvuaogtbrsQbCDN%2FSWTiogB0ePo7HYLXjKCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMnG5AIQ3dTq4%2FpWjnKtwDwT%2BYZrH%2BTP9b7UNgVT%2B7aAk39rXX8lapsQAgIrGcJDmWhGP3T8ndXiMRsT5ZHoDCPFcZ8NNrbkueQHP4qSf3osppG60y%2FUPwHjvI%2BdmBQph%2Fo4IGJncoQykyFQLm3pS2zdtkkaxBIixm1maMzT%2B5Vm7D9qmoc%2FEVGskHVLsgmqUgbFZ8%2F4JorQq8pSouGidRSerY%2BJIVOMv2Vv7dcg4DSLfQ4ZbrKhe0gmAm6hoRDNeaqbGoGD83OdEKjyZY8n1vafbqvJ2YxMf0eLocKNxvcFIN198gfnEH%2F%2Bpkypm4nv%2FtVqLBvppGZnH5MuyzOeT7ySjqp9g47ihpfe%2BUIOlsEhbiYt24IGbwbec2fxNk%2BhWwydeoY0hK3654K15sZnJQ5q4RFK9ADYc62GaVTTv%2Blwgc1IlZyB3dzRbEhKTwsR1DXEzb5Kh19wvTOD1YtRZYCpHvtWbMTrCb%2FU6Qz95ve3auDKpNVTpI2l7HrAlgpj0dTMXuYNXd4B7KXqAb2gmW%2FGje70AVoa80Q6ZONB1uhG5qwIymP%2B4Q2xrmi7VqQhbfug1EM%2FjxHlU2nbpw4soSLytj7md9cghkA%2FyJj5WAnFad0ORvqUylztmJscqdOND8Qb0ZzWSPTd3gjtwwmPHZzAY6pgFKeURNJyG6yPB2e5j4bFPk3iHXJV8DSj8heeAM%2Blip5WfIepD2Ht1%2FASSpKnSzkqEbfcwbovxOw2CiqMZtHDBE6Z%2B0MNZse7nDlkGpqVL1TasSPnsERlWT8yuYttGiNdf5nsFcjNVWIjS2Fptc1zDDSIIta8Nd7jEpg9zBjDmr9MUwKJ%2BVZVCBGVC7WVALJL87Y47pZOIRhxwm34BXR0anLqeikl89&X-Amz-Signature=0c72d425abadf7de98b36f5d17aded30b045a0c7d3736ba69cb9e155b7320c95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7O3DMK3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICN%2BjtggLqQwMxRNBetzxPYvmhNTZ9LtyZ2PihFBAIaCAiB%2Be6vJZUDcvuaogtbrsQbCDN%2FSWTiogB0ePo7HYLXjKCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMnG5AIQ3dTq4%2FpWjnKtwDwT%2BYZrH%2BTP9b7UNgVT%2B7aAk39rXX8lapsQAgIrGcJDmWhGP3T8ndXiMRsT5ZHoDCPFcZ8NNrbkueQHP4qSf3osppG60y%2FUPwHjvI%2BdmBQph%2Fo4IGJncoQykyFQLm3pS2zdtkkaxBIixm1maMzT%2B5Vm7D9qmoc%2FEVGskHVLsgmqUgbFZ8%2F4JorQq8pSouGidRSerY%2BJIVOMv2Vv7dcg4DSLfQ4ZbrKhe0gmAm6hoRDNeaqbGoGD83OdEKjyZY8n1vafbqvJ2YxMf0eLocKNxvcFIN198gfnEH%2F%2Bpkypm4nv%2FtVqLBvppGZnH5MuyzOeT7ySjqp9g47ihpfe%2BUIOlsEhbiYt24IGbwbec2fxNk%2BhWwydeoY0hK3654K15sZnJQ5q4RFK9ADYc62GaVTTv%2Blwgc1IlZyB3dzRbEhKTwsR1DXEzb5Kh19wvTOD1YtRZYCpHvtWbMTrCb%2FU6Qz95ve3auDKpNVTpI2l7HrAlgpj0dTMXuYNXd4B7KXqAb2gmW%2FGje70AVoa80Q6ZONB1uhG5qwIymP%2B4Q2xrmi7VqQhbfug1EM%2FjxHlU2nbpw4soSLytj7md9cghkA%2FyJj5WAnFad0ORvqUylztmJscqdOND8Qb0ZzWSPTd3gjtwwmPHZzAY6pgFKeURNJyG6yPB2e5j4bFPk3iHXJV8DSj8heeAM%2Blip5WfIepD2Ht1%2FASSpKnSzkqEbfcwbovxOw2CiqMZtHDBE6Z%2B0MNZse7nDlkGpqVL1TasSPnsERlWT8yuYttGiNdf5nsFcjNVWIjS2Fptc1zDDSIIta8Nd7jEpg9zBjDmr9MUwKJ%2BVZVCBGVC7WVALJL87Y47pZOIRhxwm34BXR0anLqeikl89&X-Amz-Signature=00b8372a5d6c1eab461bfa2a2b0705c283b4f3affce1e4d44ed53a2f9b43c7a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7O3DMK3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICN%2BjtggLqQwMxRNBetzxPYvmhNTZ9LtyZ2PihFBAIaCAiB%2Be6vJZUDcvuaogtbrsQbCDN%2FSWTiogB0ePo7HYLXjKCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMnG5AIQ3dTq4%2FpWjnKtwDwT%2BYZrH%2BTP9b7UNgVT%2B7aAk39rXX8lapsQAgIrGcJDmWhGP3T8ndXiMRsT5ZHoDCPFcZ8NNrbkueQHP4qSf3osppG60y%2FUPwHjvI%2BdmBQph%2Fo4IGJncoQykyFQLm3pS2zdtkkaxBIixm1maMzT%2B5Vm7D9qmoc%2FEVGskHVLsgmqUgbFZ8%2F4JorQq8pSouGidRSerY%2BJIVOMv2Vv7dcg4DSLfQ4ZbrKhe0gmAm6hoRDNeaqbGoGD83OdEKjyZY8n1vafbqvJ2YxMf0eLocKNxvcFIN198gfnEH%2F%2Bpkypm4nv%2FtVqLBvppGZnH5MuyzOeT7ySjqp9g47ihpfe%2BUIOlsEhbiYt24IGbwbec2fxNk%2BhWwydeoY0hK3654K15sZnJQ5q4RFK9ADYc62GaVTTv%2Blwgc1IlZyB3dzRbEhKTwsR1DXEzb5Kh19wvTOD1YtRZYCpHvtWbMTrCb%2FU6Qz95ve3auDKpNVTpI2l7HrAlgpj0dTMXuYNXd4B7KXqAb2gmW%2FGje70AVoa80Q6ZONB1uhG5qwIymP%2B4Q2xrmi7VqQhbfug1EM%2FjxHlU2nbpw4soSLytj7md9cghkA%2FyJj5WAnFad0ORvqUylztmJscqdOND8Qb0ZzWSPTd3gjtwwmPHZzAY6pgFKeURNJyG6yPB2e5j4bFPk3iHXJV8DSj8heeAM%2Blip5WfIepD2Ht1%2FASSpKnSzkqEbfcwbovxOw2CiqMZtHDBE6Z%2B0MNZse7nDlkGpqVL1TasSPnsERlWT8yuYttGiNdf5nsFcjNVWIjS2Fptc1zDDSIIta8Nd7jEpg9zBjDmr9MUwKJ%2BVZVCBGVC7WVALJL87Y47pZOIRhxwm34BXR0anLqeikl89&X-Amz-Signature=123325d7736a25fc235a1259767000ed0a7d391626e33a60158dd7c6551f989b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7O3DMK3%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICN%2BjtggLqQwMxRNBetzxPYvmhNTZ9LtyZ2PihFBAIaCAiB%2Be6vJZUDcvuaogtbrsQbCDN%2FSWTiogB0ePo7HYLXjKCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMnG5AIQ3dTq4%2FpWjnKtwDwT%2BYZrH%2BTP9b7UNgVT%2B7aAk39rXX8lapsQAgIrGcJDmWhGP3T8ndXiMRsT5ZHoDCPFcZ8NNrbkueQHP4qSf3osppG60y%2FUPwHjvI%2BdmBQph%2Fo4IGJncoQykyFQLm3pS2zdtkkaxBIixm1maMzT%2B5Vm7D9qmoc%2FEVGskHVLsgmqUgbFZ8%2F4JorQq8pSouGidRSerY%2BJIVOMv2Vv7dcg4DSLfQ4ZbrKhe0gmAm6hoRDNeaqbGoGD83OdEKjyZY8n1vafbqvJ2YxMf0eLocKNxvcFIN198gfnEH%2F%2Bpkypm4nv%2FtVqLBvppGZnH5MuyzOeT7ySjqp9g47ihpfe%2BUIOlsEhbiYt24IGbwbec2fxNk%2BhWwydeoY0hK3654K15sZnJQ5q4RFK9ADYc62GaVTTv%2Blwgc1IlZyB3dzRbEhKTwsR1DXEzb5Kh19wvTOD1YtRZYCpHvtWbMTrCb%2FU6Qz95ve3auDKpNVTpI2l7HrAlgpj0dTMXuYNXd4B7KXqAb2gmW%2FGje70AVoa80Q6ZONB1uhG5qwIymP%2B4Q2xrmi7VqQhbfug1EM%2FjxHlU2nbpw4soSLytj7md9cghkA%2FyJj5WAnFad0ORvqUylztmJscqdOND8Qb0ZzWSPTd3gjtwwmPHZzAY6pgFKeURNJyG6yPB2e5j4bFPk3iHXJV8DSj8heeAM%2Blip5WfIepD2Ht1%2FASSpKnSzkqEbfcwbovxOw2CiqMZtHDBE6Z%2B0MNZse7nDlkGpqVL1TasSPnsERlWT8yuYttGiNdf5nsFcjNVWIjS2Fptc1zDDSIIta8Nd7jEpg9zBjDmr9MUwKJ%2BVZVCBGVC7WVALJL87Y47pZOIRhxwm34BXR0anLqeikl89&X-Amz-Signature=64c67aa1efa7e4af2c156280c2555c0051f5675473c49af8b01e035f50f10b9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

