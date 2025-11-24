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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MQW65NU%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCLhTJgDNhuYHlOryRwOCSvIha%2F1ylaIf57IG137GV%2FYwIfMowZkh8jOb4kNI06SjX0hzCw5bHoufncEIYTa0XOZCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMxGFppnfGnqXAHNfaKtwDrPPM323PGLcr4aliKd4NGy9%2BpAhtTQYFUzHL2%2ByuErYfFS%2BsnyE8A%2BRgUO47e6ZbNKOfu8ExNosXQnFN2cqUyoDqU%2BQWmVOXImj4Cp61A2HNnSd%2BOPHUoTmk54SZPyp18mWAaV6TbT%2FEDaWHh5scEdSf2DSss%2Bk0VCcdV%2BuhjGVQZNUVYs%2F6Z5FW%2FsdLEmFn4nX32M8PMp75acYeDZvBi7snKyFPt6jajBikyvvg5Wvvc21DtEoSdFdtaMfw4PvyLITiWy5XXChZrG9o%2FHyQ1ECxK7kbE2qMPK2MMsHgRwDoe3xujp392y0%2Bm3eD%2BnRNmup7py3eYE%2FSBuvxbA02HSNDuMzPkQ9Nq1P%2BhYqnq%2FfEHkShTcfoZB7tLi0ZBYuz9OSjJ1ZUZQyDnElBERrDhwP9z7o7p0Hsibofq0hmaNMl63283rcQseG2SQg7%2B6msFC81jw119TRgHV8HqLZEaVzidKj1w8NdK7OfnhsHGk53mC61ULLpW%2BwgRwmUdaZLMBi4zJ5KS0tq%2BLnPadFKX6KtCjdET1BhOMVt9UTBwTG9EDOFezNo5xr776ctk8AnMIJGqK56oK064uMBJygAZnbiHADyW8JZHBfeL5Y%2Bl1LrNR1is0gNvU98%2Flwwx9yOyQY6pgH9s7L6f%2FjacK54yXqci4Qx5NrBvyw0Vq74%2Fdfa1QcrmYeSQxCZ8puvWl5uWE2kSvgW4lirOxXecxAdWwXwoCuhi9a%2Fz79c8j3h7f8tQaL0m5HV9I8ieP3WJDDvjXSGzsAWSIX%2FuDBAd0qIBEAz1jUTshuLTHXzvHfOBpxq2QSj4UjxKQ3D1Wd752SEa2OnrdKHbxr0BPgiIkfXNMlKAPe9zHiOvg71&X-Amz-Signature=6b81ae6597565c6c2960a48d31563753e27ff7cd782a0983d346a3e06f9e4a86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MQW65NU%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCLhTJgDNhuYHlOryRwOCSvIha%2F1ylaIf57IG137GV%2FYwIfMowZkh8jOb4kNI06SjX0hzCw5bHoufncEIYTa0XOZCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMxGFppnfGnqXAHNfaKtwDrPPM323PGLcr4aliKd4NGy9%2BpAhtTQYFUzHL2%2ByuErYfFS%2BsnyE8A%2BRgUO47e6ZbNKOfu8ExNosXQnFN2cqUyoDqU%2BQWmVOXImj4Cp61A2HNnSd%2BOPHUoTmk54SZPyp18mWAaV6TbT%2FEDaWHh5scEdSf2DSss%2Bk0VCcdV%2BuhjGVQZNUVYs%2F6Z5FW%2FsdLEmFn4nX32M8PMp75acYeDZvBi7snKyFPt6jajBikyvvg5Wvvc21DtEoSdFdtaMfw4PvyLITiWy5XXChZrG9o%2FHyQ1ECxK7kbE2qMPK2MMsHgRwDoe3xujp392y0%2Bm3eD%2BnRNmup7py3eYE%2FSBuvxbA02HSNDuMzPkQ9Nq1P%2BhYqnq%2FfEHkShTcfoZB7tLi0ZBYuz9OSjJ1ZUZQyDnElBERrDhwP9z7o7p0Hsibofq0hmaNMl63283rcQseG2SQg7%2B6msFC81jw119TRgHV8HqLZEaVzidKj1w8NdK7OfnhsHGk53mC61ULLpW%2BwgRwmUdaZLMBi4zJ5KS0tq%2BLnPadFKX6KtCjdET1BhOMVt9UTBwTG9EDOFezNo5xr776ctk8AnMIJGqK56oK064uMBJygAZnbiHADyW8JZHBfeL5Y%2Bl1LrNR1is0gNvU98%2Flwwx9yOyQY6pgH9s7L6f%2FjacK54yXqci4Qx5NrBvyw0Vq74%2Fdfa1QcrmYeSQxCZ8puvWl5uWE2kSvgW4lirOxXecxAdWwXwoCuhi9a%2Fz79c8j3h7f8tQaL0m5HV9I8ieP3WJDDvjXSGzsAWSIX%2FuDBAd0qIBEAz1jUTshuLTHXzvHfOBpxq2QSj4UjxKQ3D1Wd752SEa2OnrdKHbxr0BPgiIkfXNMlKAPe9zHiOvg71&X-Amz-Signature=868df4a2f881771173a0679c2adcde00d1527cc1efd2bef2fbe42bf5b7ee8c6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MQW65NU%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCLhTJgDNhuYHlOryRwOCSvIha%2F1ylaIf57IG137GV%2FYwIfMowZkh8jOb4kNI06SjX0hzCw5bHoufncEIYTa0XOZCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMxGFppnfGnqXAHNfaKtwDrPPM323PGLcr4aliKd4NGy9%2BpAhtTQYFUzHL2%2ByuErYfFS%2BsnyE8A%2BRgUO47e6ZbNKOfu8ExNosXQnFN2cqUyoDqU%2BQWmVOXImj4Cp61A2HNnSd%2BOPHUoTmk54SZPyp18mWAaV6TbT%2FEDaWHh5scEdSf2DSss%2Bk0VCcdV%2BuhjGVQZNUVYs%2F6Z5FW%2FsdLEmFn4nX32M8PMp75acYeDZvBi7snKyFPt6jajBikyvvg5Wvvc21DtEoSdFdtaMfw4PvyLITiWy5XXChZrG9o%2FHyQ1ECxK7kbE2qMPK2MMsHgRwDoe3xujp392y0%2Bm3eD%2BnRNmup7py3eYE%2FSBuvxbA02HSNDuMzPkQ9Nq1P%2BhYqnq%2FfEHkShTcfoZB7tLi0ZBYuz9OSjJ1ZUZQyDnElBERrDhwP9z7o7p0Hsibofq0hmaNMl63283rcQseG2SQg7%2B6msFC81jw119TRgHV8HqLZEaVzidKj1w8NdK7OfnhsHGk53mC61ULLpW%2BwgRwmUdaZLMBi4zJ5KS0tq%2BLnPadFKX6KtCjdET1BhOMVt9UTBwTG9EDOFezNo5xr776ctk8AnMIJGqK56oK064uMBJygAZnbiHADyW8JZHBfeL5Y%2Bl1LrNR1is0gNvU98%2Flwwx9yOyQY6pgH9s7L6f%2FjacK54yXqci4Qx5NrBvyw0Vq74%2Fdfa1QcrmYeSQxCZ8puvWl5uWE2kSvgW4lirOxXecxAdWwXwoCuhi9a%2Fz79c8j3h7f8tQaL0m5HV9I8ieP3WJDDvjXSGzsAWSIX%2FuDBAd0qIBEAz1jUTshuLTHXzvHfOBpxq2QSj4UjxKQ3D1Wd752SEa2OnrdKHbxr0BPgiIkfXNMlKAPe9zHiOvg71&X-Amz-Signature=595282ce89995bac49ac6778d9ac8e427cee95545a080982c8b07be9f27027ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

