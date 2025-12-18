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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636BFMDSC%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS0S9yMwhCn80rd5lDxzeKHIRpX%2FHnNXaMULg%2BJOxYIAIhAKVyTKg07lFyTmsFC6fnPF9BEnuOmTnBt%2B4RxxaIDQp2KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZROnFjvB4IP15GOwq3AMa1C%2BUHfYpXIosy1%2F3KnGLd40INadQTUrSJuPHcQKhqjHvrbuce5zoNp7CI4F8zB%2BE0b7jqHWZq8BfOIsW006X1mU1qYHonrB%2F6Fq6Xnzbre3lVEN88z3clCQN4eymj3RIYAGCl0dgiPv4Ezsen6BFunr2RIPIaA%2F92wTycT%2FRicAKgtneuxOPoacF%2Bail7E6Vyn%2FtK2Mx8LICq%2FtTUn8OUNK3ac%2FUE7nWMB7ImoQr2zbBezl0N55F9EFM0XFA90qS46cL2W3YkxPqG9agZKAfqtvbRbWfSiqduxvyXRgBJiD%2BHUSbWW5PfulLbQm8QG23%2BOsBKIGG%2FqAPO78xRhgnYJ53lXL%2FeUYeJFFcZDhm5UJmEByyNf1VecJeGGKz6V8YtmCjazLGBmo2mmAgpvsCP%2Fm82DuyyPSbbEF0EKjDwl4ZhbxA9W2tu8E3a%2BVcsGIPWHcjWswhw%2FRuVUZ2w68%2BSzsXviQZe%2BAYWm%2BHdprtiqwrfCOkWCEyXbnO%2F7Hrnuh%2FItEkEtwutuVEj3e2%2F7jxK3Njz2OI%2BCK6Dnkx9Evdtj%2FoNH61PUemkPy%2Bhn5ykHpMQUQ76vTIBkT8pAEKa0MnZgfUqPFAHRRGW8ZTxaAFepKDtP3%2B8YMMAcWu7jCwyo3KBjqkAfj2oMegM6IPn8OYSgZekq7TnGGAdfO%2BCWsDIzPea%2FgWkA92MUfuDq9lx1S3htIbpLH5Y4pUkiiws6m0%2F4b%2BxV%2FQHFGL329awvioAgjBn0k%2Bf0gQX4btMT89JF%2BGCpNuEUZ7Jpe315FmeWq404mrq2vkK2BugUl5hm5x3nSzilomWI2Lb%2F%2F8eNWRWXvMWwj3pUOuULN%2FskmN88BaFsjMrd1mwGot&X-Amz-Signature=664b2643e0defe184646e5cc79c64c143c54784bd874ed78af2ea4a3fb325ef8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636BFMDSC%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS0S9yMwhCn80rd5lDxzeKHIRpX%2FHnNXaMULg%2BJOxYIAIhAKVyTKg07lFyTmsFC6fnPF9BEnuOmTnBt%2B4RxxaIDQp2KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZROnFjvB4IP15GOwq3AMa1C%2BUHfYpXIosy1%2F3KnGLd40INadQTUrSJuPHcQKhqjHvrbuce5zoNp7CI4F8zB%2BE0b7jqHWZq8BfOIsW006X1mU1qYHonrB%2F6Fq6Xnzbre3lVEN88z3clCQN4eymj3RIYAGCl0dgiPv4Ezsen6BFunr2RIPIaA%2F92wTycT%2FRicAKgtneuxOPoacF%2Bail7E6Vyn%2FtK2Mx8LICq%2FtTUn8OUNK3ac%2FUE7nWMB7ImoQr2zbBezl0N55F9EFM0XFA90qS46cL2W3YkxPqG9agZKAfqtvbRbWfSiqduxvyXRgBJiD%2BHUSbWW5PfulLbQm8QG23%2BOsBKIGG%2FqAPO78xRhgnYJ53lXL%2FeUYeJFFcZDhm5UJmEByyNf1VecJeGGKz6V8YtmCjazLGBmo2mmAgpvsCP%2Fm82DuyyPSbbEF0EKjDwl4ZhbxA9W2tu8E3a%2BVcsGIPWHcjWswhw%2FRuVUZ2w68%2BSzsXviQZe%2BAYWm%2BHdprtiqwrfCOkWCEyXbnO%2F7Hrnuh%2FItEkEtwutuVEj3e2%2F7jxK3Njz2OI%2BCK6Dnkx9Evdtj%2FoNH61PUemkPy%2Bhn5ykHpMQUQ76vTIBkT8pAEKa0MnZgfUqPFAHRRGW8ZTxaAFepKDtP3%2B8YMMAcWu7jCwyo3KBjqkAfj2oMegM6IPn8OYSgZekq7TnGGAdfO%2BCWsDIzPea%2FgWkA92MUfuDq9lx1S3htIbpLH5Y4pUkiiws6m0%2F4b%2BxV%2FQHFGL329awvioAgjBn0k%2Bf0gQX4btMT89JF%2BGCpNuEUZ7Jpe315FmeWq404mrq2vkK2BugUl5hm5x3nSzilomWI2Lb%2F%2F8eNWRWXvMWwj3pUOuULN%2FskmN88BaFsjMrd1mwGot&X-Amz-Signature=120a9f457ea0587af9f2b542b57d04b0f79a754f75a029201d8011d0d1b78268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636BFMDSC%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS0S9yMwhCn80rd5lDxzeKHIRpX%2FHnNXaMULg%2BJOxYIAIhAKVyTKg07lFyTmsFC6fnPF9BEnuOmTnBt%2B4RxxaIDQp2KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZROnFjvB4IP15GOwq3AMa1C%2BUHfYpXIosy1%2F3KnGLd40INadQTUrSJuPHcQKhqjHvrbuce5zoNp7CI4F8zB%2BE0b7jqHWZq8BfOIsW006X1mU1qYHonrB%2F6Fq6Xnzbre3lVEN88z3clCQN4eymj3RIYAGCl0dgiPv4Ezsen6BFunr2RIPIaA%2F92wTycT%2FRicAKgtneuxOPoacF%2Bail7E6Vyn%2FtK2Mx8LICq%2FtTUn8OUNK3ac%2FUE7nWMB7ImoQr2zbBezl0N55F9EFM0XFA90qS46cL2W3YkxPqG9agZKAfqtvbRbWfSiqduxvyXRgBJiD%2BHUSbWW5PfulLbQm8QG23%2BOsBKIGG%2FqAPO78xRhgnYJ53lXL%2FeUYeJFFcZDhm5UJmEByyNf1VecJeGGKz6V8YtmCjazLGBmo2mmAgpvsCP%2Fm82DuyyPSbbEF0EKjDwl4ZhbxA9W2tu8E3a%2BVcsGIPWHcjWswhw%2FRuVUZ2w68%2BSzsXviQZe%2BAYWm%2BHdprtiqwrfCOkWCEyXbnO%2F7Hrnuh%2FItEkEtwutuVEj3e2%2F7jxK3Njz2OI%2BCK6Dnkx9Evdtj%2FoNH61PUemkPy%2Bhn5ykHpMQUQ76vTIBkT8pAEKa0MnZgfUqPFAHRRGW8ZTxaAFepKDtP3%2B8YMMAcWu7jCwyo3KBjqkAfj2oMegM6IPn8OYSgZekq7TnGGAdfO%2BCWsDIzPea%2FgWkA92MUfuDq9lx1S3htIbpLH5Y4pUkiiws6m0%2F4b%2BxV%2FQHFGL329awvioAgjBn0k%2Bf0gQX4btMT89JF%2BGCpNuEUZ7Jpe315FmeWq404mrq2vkK2BugUl5hm5x3nSzilomWI2Lb%2F%2F8eNWRWXvMWwj3pUOuULN%2FskmN88BaFsjMrd1mwGot&X-Amz-Signature=1e80c7fb714f6e4abec7756a9804d1d5a78d9487584c782adfaf824cbbda4a2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636BFMDSC%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS0S9yMwhCn80rd5lDxzeKHIRpX%2FHnNXaMULg%2BJOxYIAIhAKVyTKg07lFyTmsFC6fnPF9BEnuOmTnBt%2B4RxxaIDQp2KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZROnFjvB4IP15GOwq3AMa1C%2BUHfYpXIosy1%2F3KnGLd40INadQTUrSJuPHcQKhqjHvrbuce5zoNp7CI4F8zB%2BE0b7jqHWZq8BfOIsW006X1mU1qYHonrB%2F6Fq6Xnzbre3lVEN88z3clCQN4eymj3RIYAGCl0dgiPv4Ezsen6BFunr2RIPIaA%2F92wTycT%2FRicAKgtneuxOPoacF%2Bail7E6Vyn%2FtK2Mx8LICq%2FtTUn8OUNK3ac%2FUE7nWMB7ImoQr2zbBezl0N55F9EFM0XFA90qS46cL2W3YkxPqG9agZKAfqtvbRbWfSiqduxvyXRgBJiD%2BHUSbWW5PfulLbQm8QG23%2BOsBKIGG%2FqAPO78xRhgnYJ53lXL%2FeUYeJFFcZDhm5UJmEByyNf1VecJeGGKz6V8YtmCjazLGBmo2mmAgpvsCP%2Fm82DuyyPSbbEF0EKjDwl4ZhbxA9W2tu8E3a%2BVcsGIPWHcjWswhw%2FRuVUZ2w68%2BSzsXviQZe%2BAYWm%2BHdprtiqwrfCOkWCEyXbnO%2F7Hrnuh%2FItEkEtwutuVEj3e2%2F7jxK3Njz2OI%2BCK6Dnkx9Evdtj%2FoNH61PUemkPy%2Bhn5ykHpMQUQ76vTIBkT8pAEKa0MnZgfUqPFAHRRGW8ZTxaAFepKDtP3%2B8YMMAcWu7jCwyo3KBjqkAfj2oMegM6IPn8OYSgZekq7TnGGAdfO%2BCWsDIzPea%2FgWkA92MUfuDq9lx1S3htIbpLH5Y4pUkiiws6m0%2F4b%2BxV%2FQHFGL329awvioAgjBn0k%2Bf0gQX4btMT89JF%2BGCpNuEUZ7Jpe315FmeWq404mrq2vkK2BugUl5hm5x3nSzilomWI2Lb%2F%2F8eNWRWXvMWwj3pUOuULN%2FskmN88BaFsjMrd1mwGot&X-Amz-Signature=a48fad45897ae6a40e1945c992a447087c00fb09f6d371105942598cad76d734&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636BFMDSC%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS0S9yMwhCn80rd5lDxzeKHIRpX%2FHnNXaMULg%2BJOxYIAIhAKVyTKg07lFyTmsFC6fnPF9BEnuOmTnBt%2B4RxxaIDQp2KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZROnFjvB4IP15GOwq3AMa1C%2BUHfYpXIosy1%2F3KnGLd40INadQTUrSJuPHcQKhqjHvrbuce5zoNp7CI4F8zB%2BE0b7jqHWZq8BfOIsW006X1mU1qYHonrB%2F6Fq6Xnzbre3lVEN88z3clCQN4eymj3RIYAGCl0dgiPv4Ezsen6BFunr2RIPIaA%2F92wTycT%2FRicAKgtneuxOPoacF%2Bail7E6Vyn%2FtK2Mx8LICq%2FtTUn8OUNK3ac%2FUE7nWMB7ImoQr2zbBezl0N55F9EFM0XFA90qS46cL2W3YkxPqG9agZKAfqtvbRbWfSiqduxvyXRgBJiD%2BHUSbWW5PfulLbQm8QG23%2BOsBKIGG%2FqAPO78xRhgnYJ53lXL%2FeUYeJFFcZDhm5UJmEByyNf1VecJeGGKz6V8YtmCjazLGBmo2mmAgpvsCP%2Fm82DuyyPSbbEF0EKjDwl4ZhbxA9W2tu8E3a%2BVcsGIPWHcjWswhw%2FRuVUZ2w68%2BSzsXviQZe%2BAYWm%2BHdprtiqwrfCOkWCEyXbnO%2F7Hrnuh%2FItEkEtwutuVEj3e2%2F7jxK3Njz2OI%2BCK6Dnkx9Evdtj%2FoNH61PUemkPy%2Bhn5ykHpMQUQ76vTIBkT8pAEKa0MnZgfUqPFAHRRGW8ZTxaAFepKDtP3%2B8YMMAcWu7jCwyo3KBjqkAfj2oMegM6IPn8OYSgZekq7TnGGAdfO%2BCWsDIzPea%2FgWkA92MUfuDq9lx1S3htIbpLH5Y4pUkiiws6m0%2F4b%2BxV%2FQHFGL329awvioAgjBn0k%2Bf0gQX4btMT89JF%2BGCpNuEUZ7Jpe315FmeWq404mrq2vkK2BugUl5hm5x3nSzilomWI2Lb%2F%2F8eNWRWXvMWwj3pUOuULN%2FskmN88BaFsjMrd1mwGot&X-Amz-Signature=94e3b371726e68364788a3ac2f6ff2ff06b5d9fc99fd9409972640faf2037195&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

