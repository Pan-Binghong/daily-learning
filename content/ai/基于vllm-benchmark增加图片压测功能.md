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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT2HXN2%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCZlvs%2BMSvaKN1zizBVwmICHYLwAWL%2FiyCFMYG6%2F8tWpAIgTXbxDfgsyDVKf28MWhTJGg9VKQdn2hmHD2uo2412sNsq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPUhzKOisF06jMSs%2FCrcA8vH%2FwyNIsuykWcoIF6an4r3y6bjbzzrFbLkGwbL9MFa%2BVBA5i90QzF2YRL624kTmkRnMY%2F4fo3I70eUt4JGxuHIYfMkzG6fntyX6DZ8KwKXvol%2FH0NKhSC2sfyB3c1AXWx6C3MklG1sPr7n08ppI75ZDreYuQ1txoYFqawIRJU%2FQbHx%2B1VoLKA2XRfA7PeXYRAvfmf6KD7qaDlgUJglOZxkXKCPFbIZAy3Uyd4AbztC6LANneIyVmVYXBH6ext4ZVe66QdIgKHm5m%2B0LgPrnqFIanWPEV9BH2MU4hEC3u2Fi61ubPC5x%2FzqSrz7BmTy9bwx88n9dR6wNvEd6LDgdg%2BM69c3EccezAxFxJlEnhytlZbI4HqR7YFBe2a8xhNXH0RSmKKMX3btCMMnIGRmnH%2B9vHxhVxXsd3Kfhu7TeTd2fi9Zxnhtgq%2F%2BUC9DXBJYB91hvpHpIiosBGbOhWgEP5UQmcaX5xs5kmLxvgXCXUWnW7oVGrb9sgGwPAgZIEtRTSHTf6wCJPIpTxGJW1%2BE59bWnnPM01MY3uJ%2FEjumhzgPmaXoMPvFK4vs3tvoiSd6E%2B2%2BiefJUyqppBqdkcEh4Nc6nadIK1xuwq1Tx%2Bq%2FFh3kqf97RZ5YX%2B4fcO3DMJfG4c4GOqUBr2WwdGZWHAFRhPPurAe17GnzSUf%2FbAOi9ylAyUJuMxChw5cSLzVteGo88aBm%2BAvoQwMBgvF9DIdsf%2BA1UV5iVLrKW8zhw96Qz9HV%2F5SAcqYm9m85lTrPNENx1quMYAVw7jU%2BTVSRA3nARQFxi5hPUSa5SxMWen0wwhqSMSPMFdeDcY84BG%2F3APHtN8NMbRWCNNoGxyvrEjob6k0tlGzBytWZfaw8&X-Amz-Signature=b1f1129cd2259010a49d2d77c20253f344fe794a16312c4a58b036940bc1778a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT2HXN2%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCZlvs%2BMSvaKN1zizBVwmICHYLwAWL%2FiyCFMYG6%2F8tWpAIgTXbxDfgsyDVKf28MWhTJGg9VKQdn2hmHD2uo2412sNsq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPUhzKOisF06jMSs%2FCrcA8vH%2FwyNIsuykWcoIF6an4r3y6bjbzzrFbLkGwbL9MFa%2BVBA5i90QzF2YRL624kTmkRnMY%2F4fo3I70eUt4JGxuHIYfMkzG6fntyX6DZ8KwKXvol%2FH0NKhSC2sfyB3c1AXWx6C3MklG1sPr7n08ppI75ZDreYuQ1txoYFqawIRJU%2FQbHx%2B1VoLKA2XRfA7PeXYRAvfmf6KD7qaDlgUJglOZxkXKCPFbIZAy3Uyd4AbztC6LANneIyVmVYXBH6ext4ZVe66QdIgKHm5m%2B0LgPrnqFIanWPEV9BH2MU4hEC3u2Fi61ubPC5x%2FzqSrz7BmTy9bwx88n9dR6wNvEd6LDgdg%2BM69c3EccezAxFxJlEnhytlZbI4HqR7YFBe2a8xhNXH0RSmKKMX3btCMMnIGRmnH%2B9vHxhVxXsd3Kfhu7TeTd2fi9Zxnhtgq%2F%2BUC9DXBJYB91hvpHpIiosBGbOhWgEP5UQmcaX5xs5kmLxvgXCXUWnW7oVGrb9sgGwPAgZIEtRTSHTf6wCJPIpTxGJW1%2BE59bWnnPM01MY3uJ%2FEjumhzgPmaXoMPvFK4vs3tvoiSd6E%2B2%2BiefJUyqppBqdkcEh4Nc6nadIK1xuwq1Tx%2Bq%2FFh3kqf97RZ5YX%2B4fcO3DMJfG4c4GOqUBr2WwdGZWHAFRhPPurAe17GnzSUf%2FbAOi9ylAyUJuMxChw5cSLzVteGo88aBm%2BAvoQwMBgvF9DIdsf%2BA1UV5iVLrKW8zhw96Qz9HV%2F5SAcqYm9m85lTrPNENx1quMYAVw7jU%2BTVSRA3nARQFxi5hPUSa5SxMWen0wwhqSMSPMFdeDcY84BG%2F3APHtN8NMbRWCNNoGxyvrEjob6k0tlGzBytWZfaw8&X-Amz-Signature=8f9be4b0fed083646589b5aeeea5647e8750c759899a21cfa7974d6b52ce797d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT2HXN2%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCZlvs%2BMSvaKN1zizBVwmICHYLwAWL%2FiyCFMYG6%2F8tWpAIgTXbxDfgsyDVKf28MWhTJGg9VKQdn2hmHD2uo2412sNsq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPUhzKOisF06jMSs%2FCrcA8vH%2FwyNIsuykWcoIF6an4r3y6bjbzzrFbLkGwbL9MFa%2BVBA5i90QzF2YRL624kTmkRnMY%2F4fo3I70eUt4JGxuHIYfMkzG6fntyX6DZ8KwKXvol%2FH0NKhSC2sfyB3c1AXWx6C3MklG1sPr7n08ppI75ZDreYuQ1txoYFqawIRJU%2FQbHx%2B1VoLKA2XRfA7PeXYRAvfmf6KD7qaDlgUJglOZxkXKCPFbIZAy3Uyd4AbztC6LANneIyVmVYXBH6ext4ZVe66QdIgKHm5m%2B0LgPrnqFIanWPEV9BH2MU4hEC3u2Fi61ubPC5x%2FzqSrz7BmTy9bwx88n9dR6wNvEd6LDgdg%2BM69c3EccezAxFxJlEnhytlZbI4HqR7YFBe2a8xhNXH0RSmKKMX3btCMMnIGRmnH%2B9vHxhVxXsd3Kfhu7TeTd2fi9Zxnhtgq%2F%2BUC9DXBJYB91hvpHpIiosBGbOhWgEP5UQmcaX5xs5kmLxvgXCXUWnW7oVGrb9sgGwPAgZIEtRTSHTf6wCJPIpTxGJW1%2BE59bWnnPM01MY3uJ%2FEjumhzgPmaXoMPvFK4vs3tvoiSd6E%2B2%2BiefJUyqppBqdkcEh4Nc6nadIK1xuwq1Tx%2Bq%2FFh3kqf97RZ5YX%2B4fcO3DMJfG4c4GOqUBr2WwdGZWHAFRhPPurAe17GnzSUf%2FbAOi9ylAyUJuMxChw5cSLzVteGo88aBm%2BAvoQwMBgvF9DIdsf%2BA1UV5iVLrKW8zhw96Qz9HV%2F5SAcqYm9m85lTrPNENx1quMYAVw7jU%2BTVSRA3nARQFxi5hPUSa5SxMWen0wwhqSMSPMFdeDcY84BG%2F3APHtN8NMbRWCNNoGxyvrEjob6k0tlGzBytWZfaw8&X-Amz-Signature=f8e7184add0768f64425e91f28d36a85070af95a9958d0728a4096d35208d378&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT2HXN2%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCZlvs%2BMSvaKN1zizBVwmICHYLwAWL%2FiyCFMYG6%2F8tWpAIgTXbxDfgsyDVKf28MWhTJGg9VKQdn2hmHD2uo2412sNsq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPUhzKOisF06jMSs%2FCrcA8vH%2FwyNIsuykWcoIF6an4r3y6bjbzzrFbLkGwbL9MFa%2BVBA5i90QzF2YRL624kTmkRnMY%2F4fo3I70eUt4JGxuHIYfMkzG6fntyX6DZ8KwKXvol%2FH0NKhSC2sfyB3c1AXWx6C3MklG1sPr7n08ppI75ZDreYuQ1txoYFqawIRJU%2FQbHx%2B1VoLKA2XRfA7PeXYRAvfmf6KD7qaDlgUJglOZxkXKCPFbIZAy3Uyd4AbztC6LANneIyVmVYXBH6ext4ZVe66QdIgKHm5m%2B0LgPrnqFIanWPEV9BH2MU4hEC3u2Fi61ubPC5x%2FzqSrz7BmTy9bwx88n9dR6wNvEd6LDgdg%2BM69c3EccezAxFxJlEnhytlZbI4HqR7YFBe2a8xhNXH0RSmKKMX3btCMMnIGRmnH%2B9vHxhVxXsd3Kfhu7TeTd2fi9Zxnhtgq%2F%2BUC9DXBJYB91hvpHpIiosBGbOhWgEP5UQmcaX5xs5kmLxvgXCXUWnW7oVGrb9sgGwPAgZIEtRTSHTf6wCJPIpTxGJW1%2BE59bWnnPM01MY3uJ%2FEjumhzgPmaXoMPvFK4vs3tvoiSd6E%2B2%2BiefJUyqppBqdkcEh4Nc6nadIK1xuwq1Tx%2Bq%2FFh3kqf97RZ5YX%2B4fcO3DMJfG4c4GOqUBr2WwdGZWHAFRhPPurAe17GnzSUf%2FbAOi9ylAyUJuMxChw5cSLzVteGo88aBm%2BAvoQwMBgvF9DIdsf%2BA1UV5iVLrKW8zhw96Qz9HV%2F5SAcqYm9m85lTrPNENx1quMYAVw7jU%2BTVSRA3nARQFxi5hPUSa5SxMWen0wwhqSMSPMFdeDcY84BG%2F3APHtN8NMbRWCNNoGxyvrEjob6k0tlGzBytWZfaw8&X-Amz-Signature=5a5bee2a466bcee646cba9aaf0e1e3d9a83ec15ffa82467a4f0a47863aabde2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT2HXN2%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCZlvs%2BMSvaKN1zizBVwmICHYLwAWL%2FiyCFMYG6%2F8tWpAIgTXbxDfgsyDVKf28MWhTJGg9VKQdn2hmHD2uo2412sNsq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPUhzKOisF06jMSs%2FCrcA8vH%2FwyNIsuykWcoIF6an4r3y6bjbzzrFbLkGwbL9MFa%2BVBA5i90QzF2YRL624kTmkRnMY%2F4fo3I70eUt4JGxuHIYfMkzG6fntyX6DZ8KwKXvol%2FH0NKhSC2sfyB3c1AXWx6C3MklG1sPr7n08ppI75ZDreYuQ1txoYFqawIRJU%2FQbHx%2B1VoLKA2XRfA7PeXYRAvfmf6KD7qaDlgUJglOZxkXKCPFbIZAy3Uyd4AbztC6LANneIyVmVYXBH6ext4ZVe66QdIgKHm5m%2B0LgPrnqFIanWPEV9BH2MU4hEC3u2Fi61ubPC5x%2FzqSrz7BmTy9bwx88n9dR6wNvEd6LDgdg%2BM69c3EccezAxFxJlEnhytlZbI4HqR7YFBe2a8xhNXH0RSmKKMX3btCMMnIGRmnH%2B9vHxhVxXsd3Kfhu7TeTd2fi9Zxnhtgq%2F%2BUC9DXBJYB91hvpHpIiosBGbOhWgEP5UQmcaX5xs5kmLxvgXCXUWnW7oVGrb9sgGwPAgZIEtRTSHTf6wCJPIpTxGJW1%2BE59bWnnPM01MY3uJ%2FEjumhzgPmaXoMPvFK4vs3tvoiSd6E%2B2%2BiefJUyqppBqdkcEh4Nc6nadIK1xuwq1Tx%2Bq%2FFh3kqf97RZ5YX%2B4fcO3DMJfG4c4GOqUBr2WwdGZWHAFRhPPurAe17GnzSUf%2FbAOi9ylAyUJuMxChw5cSLzVteGo88aBm%2BAvoQwMBgvF9DIdsf%2BA1UV5iVLrKW8zhw96Qz9HV%2F5SAcqYm9m85lTrPNENx1quMYAVw7jU%2BTVSRA3nARQFxi5hPUSa5SxMWen0wwhqSMSPMFdeDcY84BG%2F3APHtN8NMbRWCNNoGxyvrEjob6k0tlGzBytWZfaw8&X-Amz-Signature=6e28483456f2d7775fce2662fad7c24464fd042b9427952cbc228e09d9ffeba6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

