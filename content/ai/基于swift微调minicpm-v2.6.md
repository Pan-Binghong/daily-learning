---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTBWTXLO%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxyV3dFrnT791VlauHuGrmbyCECoPwstBYN2AxN%2BuzrwIhAJFtgADCOEc7SSxSDU1zHSchg%2Fr7CgTfgzZSksMnKYA%2BKv8DCEwQABoMNjM3NDIzMTgzODA1IgyzLUIzp0Kgo%2BjS%2BmQq3APq7s%2BegMnBfxgRYyuOqafIBSQMwFcdmVkZZJhDOBWZ6qd%2FUF9K2R6wU%2Bcsu6qPDlLqTrWZERNXvbsZ24T6Xs6pAFtDj4s2S7%2BI3rjjry84BUFEqLnm84PN0VU5Eglxa%2BejFLctuFnOFEqo%2FXqyPCRfjH4QAR%2BeLi3N%2FYh3QoQKiJo9Fij2LxxVr8oyHYAU8ZzUsqLGEfES9%2Bcb%2FRyYPN3vnJ7dmQrVKEjQyZTp8q4GmifNgomQkHA%2FRcBZkPyqxSb0j6fihyM7WKDlt2Gl23QqnczYRYhd6cD0MnJZCTbhIwl60nJjC%2BfKxpjjwkYg3Y3mJJ0xMmxdUcoX3Hj4iScDGlSg4dQM4y2wyViCOLjT8TmXE8%2BgKVcMrNq3sHxWpM%2F%2B4bJKUOfFQ%2BSGFC34QdN6Mxcy4tZcwSnl%2FBRJuH8rsMsg27LjOqA2BFpd0iiA1INvKAW74rPwkRpEiTY2fqWQ1zkAfalIUD1%2BU5rSri74SuK2b59TemfM%2F7p0QNlpL2zrsyX3Xe%2BgZ%2FMvO1DSoOSb1vLKf3sRxO%2BZrCBW5C5rOa4BlqgdS%2BoNioTwfgNHq3VXe1M7a4pVGNFqtXyaUMUoChAdjCGQRFbfwPldXl1kma23cJtrQ%2BiNs1ncszCy0uDLBjqkAZtDuhl1ainA1rxz0C4B2friNe5EomMSulJiVBqX0oJDwPfMvLOL6L8Qm%2BQd%2Bdlyrlmqlw6NHgXmbAVnWHLn5ijJ7riFE0StjkL%2FpWj%2Fj9nHd0tngGI7gKmGG7IyfrLOPURkjL6IJoQbyyAJPXp9kUraB5CQkuz8oZUeMYN0fIyDt%2FABoTM23xxhOuOAbymq0%2BXGoBBU3k1UwWCxPDwvQhsiAe2M&X-Amz-Signature=3a962004ccc9a6b087a9aaac6c773c86a74917e91057636f972c7873c92d944e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTBWTXLO%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxyV3dFrnT791VlauHuGrmbyCECoPwstBYN2AxN%2BuzrwIhAJFtgADCOEc7SSxSDU1zHSchg%2Fr7CgTfgzZSksMnKYA%2BKv8DCEwQABoMNjM3NDIzMTgzODA1IgyzLUIzp0Kgo%2BjS%2BmQq3APq7s%2BegMnBfxgRYyuOqafIBSQMwFcdmVkZZJhDOBWZ6qd%2FUF9K2R6wU%2Bcsu6qPDlLqTrWZERNXvbsZ24T6Xs6pAFtDj4s2S7%2BI3rjjry84BUFEqLnm84PN0VU5Eglxa%2BejFLctuFnOFEqo%2FXqyPCRfjH4QAR%2BeLi3N%2FYh3QoQKiJo9Fij2LxxVr8oyHYAU8ZzUsqLGEfES9%2Bcb%2FRyYPN3vnJ7dmQrVKEjQyZTp8q4GmifNgomQkHA%2FRcBZkPyqxSb0j6fihyM7WKDlt2Gl23QqnczYRYhd6cD0MnJZCTbhIwl60nJjC%2BfKxpjjwkYg3Y3mJJ0xMmxdUcoX3Hj4iScDGlSg4dQM4y2wyViCOLjT8TmXE8%2BgKVcMrNq3sHxWpM%2F%2B4bJKUOfFQ%2BSGFC34QdN6Mxcy4tZcwSnl%2FBRJuH8rsMsg27LjOqA2BFpd0iiA1INvKAW74rPwkRpEiTY2fqWQ1zkAfalIUD1%2BU5rSri74SuK2b59TemfM%2F7p0QNlpL2zrsyX3Xe%2BgZ%2FMvO1DSoOSb1vLKf3sRxO%2BZrCBW5C5rOa4BlqgdS%2BoNioTwfgNHq3VXe1M7a4pVGNFqtXyaUMUoChAdjCGQRFbfwPldXl1kma23cJtrQ%2BiNs1ncszCy0uDLBjqkAZtDuhl1ainA1rxz0C4B2friNe5EomMSulJiVBqX0oJDwPfMvLOL6L8Qm%2BQd%2Bdlyrlmqlw6NHgXmbAVnWHLn5ijJ7riFE0StjkL%2FpWj%2Fj9nHd0tngGI7gKmGG7IyfrLOPURkjL6IJoQbyyAJPXp9kUraB5CQkuz8oZUeMYN0fIyDt%2FABoTM23xxhOuOAbymq0%2BXGoBBU3k1UwWCxPDwvQhsiAe2M&X-Amz-Signature=524cb001a3adc52b9fcea8a4dce22c4ca4fda9440b26153b2ccc83aa6736f58e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTBWTXLO%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxyV3dFrnT791VlauHuGrmbyCECoPwstBYN2AxN%2BuzrwIhAJFtgADCOEc7SSxSDU1zHSchg%2Fr7CgTfgzZSksMnKYA%2BKv8DCEwQABoMNjM3NDIzMTgzODA1IgyzLUIzp0Kgo%2BjS%2BmQq3APq7s%2BegMnBfxgRYyuOqafIBSQMwFcdmVkZZJhDOBWZ6qd%2FUF9K2R6wU%2Bcsu6qPDlLqTrWZERNXvbsZ24T6Xs6pAFtDj4s2S7%2BI3rjjry84BUFEqLnm84PN0VU5Eglxa%2BejFLctuFnOFEqo%2FXqyPCRfjH4QAR%2BeLi3N%2FYh3QoQKiJo9Fij2LxxVr8oyHYAU8ZzUsqLGEfES9%2Bcb%2FRyYPN3vnJ7dmQrVKEjQyZTp8q4GmifNgomQkHA%2FRcBZkPyqxSb0j6fihyM7WKDlt2Gl23QqnczYRYhd6cD0MnJZCTbhIwl60nJjC%2BfKxpjjwkYg3Y3mJJ0xMmxdUcoX3Hj4iScDGlSg4dQM4y2wyViCOLjT8TmXE8%2BgKVcMrNq3sHxWpM%2F%2B4bJKUOfFQ%2BSGFC34QdN6Mxcy4tZcwSnl%2FBRJuH8rsMsg27LjOqA2BFpd0iiA1INvKAW74rPwkRpEiTY2fqWQ1zkAfalIUD1%2BU5rSri74SuK2b59TemfM%2F7p0QNlpL2zrsyX3Xe%2BgZ%2FMvO1DSoOSb1vLKf3sRxO%2BZrCBW5C5rOa4BlqgdS%2BoNioTwfgNHq3VXe1M7a4pVGNFqtXyaUMUoChAdjCGQRFbfwPldXl1kma23cJtrQ%2BiNs1ncszCy0uDLBjqkAZtDuhl1ainA1rxz0C4B2friNe5EomMSulJiVBqX0oJDwPfMvLOL6L8Qm%2BQd%2Bdlyrlmqlw6NHgXmbAVnWHLn5ijJ7riFE0StjkL%2FpWj%2Fj9nHd0tngGI7gKmGG7IyfrLOPURkjL6IJoQbyyAJPXp9kUraB5CQkuz8oZUeMYN0fIyDt%2FABoTM23xxhOuOAbymq0%2BXGoBBU3k1UwWCxPDwvQhsiAe2M&X-Amz-Signature=c5ee038654e9181c45b0a937085dedf54e3b48570015a6a197ec97ec2c51f23c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

