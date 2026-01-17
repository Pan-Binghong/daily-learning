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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f57591c1-c453-4035-b53d-bd5c2ed85fea/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRL5K4FS%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMUfa2sjJeGzhbjrtj0PuUi%2BtzTJAxLZGk%2FtIBVMfNcAIhAPz9vmF1d3tND27yXCc%2FsHDdZ38EWkbsNSPQMuL1C%2FNpKv8DCFsQABoMNjM3NDIzMTgzODA1IgyG4NjcQyQpIJjtJmoq3AN9h%2BDzW1uVptKQm7oaqH9%2BhIhJ8iuDrDEoRRbiN2maB3jf1hkMCS75sYsgyMys119jBvRv1gAfg4Jbx6I7xgk6KTfZE2QgpjzHhNSFynLSvzbb%2BtQZgrb%2FVqUtpy4S%2BLV7VRlarwA66blvC5aiDdT8WPHUhZ7Nc6t%2B3%2FjbHczD%2BxlwXPpwkLq1LvGNw6P2fpDhoiIeOYp%2FEdQVDa32PTQxLoBayDDUUoYdoYgqbpAz4g0bYM3mYKc3OPejpUW6FLwJPFDq9fiEilkr22yUTHx%2F4549f%2BeAL43ZhdnL74EVsLSYMOTWiDkRR%2F4sjFPeO7zHBEIoQgaiwf3WM5X%2BUar6PZyQS089CQmdx51xILmBlGW69JrANGCxe0ptcPZnD1D66G0tzT%2Bz%2FLA9gQnJ1Vz7mTousYPKxAsKuTKIqvTmyfJ5com047URs4jBi2hXKzA58wbBsS4OaTBZE8iseN4ccHxrOIg5JduzmQ7fTEK4Smul6Xwy6hGgIP%2BD5Oldzrn6iIN5Ft6YZZZjis%2FdBBpv3rpx%2F%2Bl2Q%2F%2FUcc%2BgZS3ATaxnNFj%2B1H%2F%2FMWylmESX1fTt0neoD0DbzQ%2FOETVwKgT%2FaaoiscpVudwdghcXrhLc1LBKVMQ10ep7s6jxVDD30avLBjqkARU5FvCqvE85VNketwqGFEP4Mo11aryloXTexiHWkdzwnBXd%2FeuFUkyHwhFmSXUMQR4c3lJ8Kc1jitYia09qwjg%2F7AxKAB2srvO0Gihu5VAyuubANlOxmLsQPfCIAtR84CSOd4n3f%2BrwsRnHwe6Dcm4tT1SRgEOz%2Fa05udHJFs%2BAfJAqKgcDHu19MFT2MVtc67DCHCZ45M0iCqrtljUAUWUsCW3E&X-Amz-Signature=212d7696bcaf00accb9a21218c14fc0c2b097065818b2b51136a7ee42d9600e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/acb00a08-4664-4f18-be40-28c21ebba87e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRL5K4FS%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMUfa2sjJeGzhbjrtj0PuUi%2BtzTJAxLZGk%2FtIBVMfNcAIhAPz9vmF1d3tND27yXCc%2FsHDdZ38EWkbsNSPQMuL1C%2FNpKv8DCFsQABoMNjM3NDIzMTgzODA1IgyG4NjcQyQpIJjtJmoq3AN9h%2BDzW1uVptKQm7oaqH9%2BhIhJ8iuDrDEoRRbiN2maB3jf1hkMCS75sYsgyMys119jBvRv1gAfg4Jbx6I7xgk6KTfZE2QgpjzHhNSFynLSvzbb%2BtQZgrb%2FVqUtpy4S%2BLV7VRlarwA66blvC5aiDdT8WPHUhZ7Nc6t%2B3%2FjbHczD%2BxlwXPpwkLq1LvGNw6P2fpDhoiIeOYp%2FEdQVDa32PTQxLoBayDDUUoYdoYgqbpAz4g0bYM3mYKc3OPejpUW6FLwJPFDq9fiEilkr22yUTHx%2F4549f%2BeAL43ZhdnL74EVsLSYMOTWiDkRR%2F4sjFPeO7zHBEIoQgaiwf3WM5X%2BUar6PZyQS089CQmdx51xILmBlGW69JrANGCxe0ptcPZnD1D66G0tzT%2Bz%2FLA9gQnJ1Vz7mTousYPKxAsKuTKIqvTmyfJ5com047URs4jBi2hXKzA58wbBsS4OaTBZE8iseN4ccHxrOIg5JduzmQ7fTEK4Smul6Xwy6hGgIP%2BD5Oldzrn6iIN5Ft6YZZZjis%2FdBBpv3rpx%2F%2Bl2Q%2F%2FUcc%2BgZS3ATaxnNFj%2B1H%2F%2FMWylmESX1fTt0neoD0DbzQ%2FOETVwKgT%2FaaoiscpVudwdghcXrhLc1LBKVMQ10ep7s6jxVDD30avLBjqkARU5FvCqvE85VNketwqGFEP4Mo11aryloXTexiHWkdzwnBXd%2FeuFUkyHwhFmSXUMQR4c3lJ8Kc1jitYia09qwjg%2F7AxKAB2srvO0Gihu5VAyuubANlOxmLsQPfCIAtR84CSOd4n3f%2BrwsRnHwe6Dcm4tT1SRgEOz%2Fa05udHJFs%2BAfJAqKgcDHu19MFT2MVtc67DCHCZ45M0iCqrtljUAUWUsCW3E&X-Amz-Signature=4f6357a9fbe77b64b83d078d9f920df94524a1b58662f3fc63fdba343c8888da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    endpoint = args.endpoint
    if endpoint == parser.get_default("endpoint") and backend in ("openai-chat-vl" ):
        endpoint = "/v1/chat/completions"
        print(f"Using default endpoint for {backend}: {endpoint}")
```

---

1. main函数处新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa27d276-9e28-452c-a670-22cf34290262/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRL5K4FS%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMUfa2sjJeGzhbjrtj0PuUi%2BtzTJAxLZGk%2FtIBVMfNcAIhAPz9vmF1d3tND27yXCc%2FsHDdZ38EWkbsNSPQMuL1C%2FNpKv8DCFsQABoMNjM3NDIzMTgzODA1IgyG4NjcQyQpIJjtJmoq3AN9h%2BDzW1uVptKQm7oaqH9%2BhIhJ8iuDrDEoRRbiN2maB3jf1hkMCS75sYsgyMys119jBvRv1gAfg4Jbx6I7xgk6KTfZE2QgpjzHhNSFynLSvzbb%2BtQZgrb%2FVqUtpy4S%2BLV7VRlarwA66blvC5aiDdT8WPHUhZ7Nc6t%2B3%2FjbHczD%2BxlwXPpwkLq1LvGNw6P2fpDhoiIeOYp%2FEdQVDa32PTQxLoBayDDUUoYdoYgqbpAz4g0bYM3mYKc3OPejpUW6FLwJPFDq9fiEilkr22yUTHx%2F4549f%2BeAL43ZhdnL74EVsLSYMOTWiDkRR%2F4sjFPeO7zHBEIoQgaiwf3WM5X%2BUar6PZyQS089CQmdx51xILmBlGW69JrANGCxe0ptcPZnD1D66G0tzT%2Bz%2FLA9gQnJ1Vz7mTousYPKxAsKuTKIqvTmyfJ5com047URs4jBi2hXKzA58wbBsS4OaTBZE8iseN4ccHxrOIg5JduzmQ7fTEK4Smul6Xwy6hGgIP%2BD5Oldzrn6iIN5Ft6YZZZjis%2FdBBpv3rpx%2F%2Bl2Q%2F%2FUcc%2BgZS3ATaxnNFj%2B1H%2F%2FMWylmESX1fTt0neoD0DbzQ%2FOETVwKgT%2FaaoiscpVudwdghcXrhLc1LBKVMQ10ep7s6jxVDD30avLBjqkARU5FvCqvE85VNketwqGFEP4Mo11aryloXTexiHWkdzwnBXd%2FeuFUkyHwhFmSXUMQR4c3lJ8Kc1jitYia09qwjg%2F7AxKAB2srvO0Gihu5VAyuubANlOxmLsQPfCIAtR84CSOd4n3f%2BrwsRnHwe6Dcm4tT1SRgEOz%2Fa05udHJFs%2BAfJAqKgcDHu19MFT2MVtc67DCHCZ45M0iCqrtljUAUWUsCW3E&X-Amz-Signature=8d1da3e70d726272da3e789f6f5bb5b6e353b0ba36309de91ca37d87188c132e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/793411c7-f33d-42fb-832b-f81f2e6ac060/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRL5K4FS%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMUfa2sjJeGzhbjrtj0PuUi%2BtzTJAxLZGk%2FtIBVMfNcAIhAPz9vmF1d3tND27yXCc%2FsHDdZ38EWkbsNSPQMuL1C%2FNpKv8DCFsQABoMNjM3NDIzMTgzODA1IgyG4NjcQyQpIJjtJmoq3AN9h%2BDzW1uVptKQm7oaqH9%2BhIhJ8iuDrDEoRRbiN2maB3jf1hkMCS75sYsgyMys119jBvRv1gAfg4Jbx6I7xgk6KTfZE2QgpjzHhNSFynLSvzbb%2BtQZgrb%2FVqUtpy4S%2BLV7VRlarwA66blvC5aiDdT8WPHUhZ7Nc6t%2B3%2FjbHczD%2BxlwXPpwkLq1LvGNw6P2fpDhoiIeOYp%2FEdQVDa32PTQxLoBayDDUUoYdoYgqbpAz4g0bYM3mYKc3OPejpUW6FLwJPFDq9fiEilkr22yUTHx%2F4549f%2BeAL43ZhdnL74EVsLSYMOTWiDkRR%2F4sjFPeO7zHBEIoQgaiwf3WM5X%2BUar6PZyQS089CQmdx51xILmBlGW69JrANGCxe0ptcPZnD1D66G0tzT%2Bz%2FLA9gQnJ1Vz7mTousYPKxAsKuTKIqvTmyfJ5com047URs4jBi2hXKzA58wbBsS4OaTBZE8iseN4ccHxrOIg5JduzmQ7fTEK4Smul6Xwy6hGgIP%2BD5Oldzrn6iIN5Ft6YZZZjis%2FdBBpv3rpx%2F%2Bl2Q%2F%2FUcc%2BgZS3ATaxnNFj%2B1H%2F%2FMWylmESX1fTt0neoD0DbzQ%2FOETVwKgT%2FaaoiscpVudwdghcXrhLc1LBKVMQ10ep7s6jxVDD30avLBjqkARU5FvCqvE85VNketwqGFEP4Mo11aryloXTexiHWkdzwnBXd%2FeuFUkyHwhFmSXUMQR4c3lJ8Kc1jitYia09qwjg%2F7AxKAB2srvO0Gihu5VAyuubANlOxmLsQPfCIAtR84CSOd4n3f%2BrwsRnHwe6Dcm4tT1SRgEOz%2Fa05udHJFs%2BAfJAqKgcDHu19MFT2MVtc67DCHCZ45M0iCqrtljUAUWUsCW3E&X-Amz-Signature=eb87ae6f2bca8d1dc0e018302b2c95f8f5df961cb81a67e4745c963b8bce8246&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
    if backend not in ("openai-chat-vl" ) and test_mm_content is not None:
        raise ValueError(
            f"Multi-modal content is only supported on 'openai-chat' or 'openai-image' backend, but got {backend}."
        )
```

---

1. 在sample_random_requests新增
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/42ca8958-3d13-4ea5-b1d2-f9d85d351904/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRL5K4FS%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMUfa2sjJeGzhbjrtj0PuUi%2BtzTJAxLZGk%2FtIBVMfNcAIhAPz9vmF1d3tND27yXCc%2FsHDdZ38EWkbsNSPQMuL1C%2FNpKv8DCFsQABoMNjM3NDIzMTgzODA1IgyG4NjcQyQpIJjtJmoq3AN9h%2BDzW1uVptKQm7oaqH9%2BhIhJ8iuDrDEoRRbiN2maB3jf1hkMCS75sYsgyMys119jBvRv1gAfg4Jbx6I7xgk6KTfZE2QgpjzHhNSFynLSvzbb%2BtQZgrb%2FVqUtpy4S%2BLV7VRlarwA66blvC5aiDdT8WPHUhZ7Nc6t%2B3%2FjbHczD%2BxlwXPpwkLq1LvGNw6P2fpDhoiIeOYp%2FEdQVDa32PTQxLoBayDDUUoYdoYgqbpAz4g0bYM3mYKc3OPejpUW6FLwJPFDq9fiEilkr22yUTHx%2F4549f%2BeAL43ZhdnL74EVsLSYMOTWiDkRR%2F4sjFPeO7zHBEIoQgaiwf3WM5X%2BUar6PZyQS089CQmdx51xILmBlGW69JrANGCxe0ptcPZnD1D66G0tzT%2Bz%2FLA9gQnJ1Vz7mTousYPKxAsKuTKIqvTmyfJ5com047URs4jBi2hXKzA58wbBsS4OaTBZE8iseN4ccHxrOIg5JduzmQ7fTEK4Smul6Xwy6hGgIP%2BD5Oldzrn6iIN5Ft6YZZZjis%2FdBBpv3rpx%2F%2Bl2Q%2F%2FUcc%2BgZS3ATaxnNFj%2B1H%2F%2FMWylmESX1fTt0neoD0DbzQ%2FOETVwKgT%2FaaoiscpVudwdghcXrhLc1LBKVMQ10ep7s6jxVDD30avLBjqkARU5FvCqvE85VNketwqGFEP4Mo11aryloXTexiHWkdzwnBXd%2FeuFUkyHwhFmSXUMQR4c3lJ8Kc1jitYia09qwjg%2F7AxKAB2srvO0Gihu5VAyuubANlOxmLsQPfCIAtR84CSOd4n3f%2BrwsRnHwe6Dcm4tT1SRgEOz%2Fa05udHJFs%2BAfJAqKgcDHu19MFT2MVtc67DCHCZ45M0iCqrtljUAUWUsCW3E&X-Amz-Signature=0f1db65ed6bf75a606669cd641a0c9115c022ee127978ec1727024e177149628&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

