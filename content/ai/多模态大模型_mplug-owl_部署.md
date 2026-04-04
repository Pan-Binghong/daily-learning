---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665JN4FKP%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3LOoFSDsid5ZbK8bpyJhriix1scZfuLlq9B1%2ByeAgZAIgTrDj1WHRKZeiIRQbKFuylHYJ4J5d5LwIq7BC%2FZYuoT4qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCukoyaoY9PSIJEaoCrcA%2FjUJwakkCtcHj5oqx1aGR%2BqFcknieT30n85jGBlfny%2FYMz4oxSozr87xawb%2BJtp4sVUzDT3Wqc5DOrSRAkii18%2BnulJuy%2Fgpjsr7OmLvpqQoJ%2FVSwToexuoIGMARG1S1ByS7sa8iepHUPWuuu7u3WxMf5LgA4e30uoLu0FyDFyOmVbPMKyAR9Lucl2OPWG24yErTto1YhE9LVQ4byu5IXaPmmw7ynUlwZw8dcVordSERJNZi7TvixvVchPHFSVbur9RgNytissB%2FI0DElnmxTwaB1JVTzfWOKC9QygxsVXaxISOKMtFgpHQidiwo7RLh%2FNLd1yQwhLPMQrfYUIzNRkQSCovceNSOX2j47qeI%2F8%2FAgt2hRVLOqZ2OurOPzOk1ULhxmRnFN09COFW69vOpHunmPVwlrR%2FDxqi9guzPSorM%2B2zATwr6szNGSl%2BRvOcfUKOZERoLnYpOb5EO1YMnFwNYa3w656fl4TH2zE0Ql934y5ZQ%2B8U7rUCowfWqy4OFp2X2apYo1fgh7h8yhH76MWMXXwbViaaMunRS5%2FmHgNVM%2Bb2QxMY9jpH6eoff%2FFYC5z%2BSIRiupK3GHfkTl70m86gZ3%2Fr6%2FGqZzBZntse3xX0PCc38aHRaOxOd2JJMKDlwc4GOqUB6p7FyBy0MC%2BPj4xAjPkg6twPD4ITzvg7GXOozyA%2FTAGZkJgRM3MakcIL6GhzDuvd%2FkVTIyNMerPIWnITPcKKDqdquxK%2BJ1fzvypWS42%2F956i1z6ySF3P1afhkyllqyk9ULM8dqkhJ5kAlYCV%2BfRwy2QiWITvxs8QYMNnWMbjP1ud%2Beyb9xeOPx9rFTuwTnqaUg6ws8xDUrviwYAvN1OKlsIC6oHU&X-Amz-Signature=3532751a4e14df35e4f1fb869037d991154b99c89796569b832d2d5cc9dd2791&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665JN4FKP%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3LOoFSDsid5ZbK8bpyJhriix1scZfuLlq9B1%2ByeAgZAIgTrDj1WHRKZeiIRQbKFuylHYJ4J5d5LwIq7BC%2FZYuoT4qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCukoyaoY9PSIJEaoCrcA%2FjUJwakkCtcHj5oqx1aGR%2BqFcknieT30n85jGBlfny%2FYMz4oxSozr87xawb%2BJtp4sVUzDT3Wqc5DOrSRAkii18%2BnulJuy%2Fgpjsr7OmLvpqQoJ%2FVSwToexuoIGMARG1S1ByS7sa8iepHUPWuuu7u3WxMf5LgA4e30uoLu0FyDFyOmVbPMKyAR9Lucl2OPWG24yErTto1YhE9LVQ4byu5IXaPmmw7ynUlwZw8dcVordSERJNZi7TvixvVchPHFSVbur9RgNytissB%2FI0DElnmxTwaB1JVTzfWOKC9QygxsVXaxISOKMtFgpHQidiwo7RLh%2FNLd1yQwhLPMQrfYUIzNRkQSCovceNSOX2j47qeI%2F8%2FAgt2hRVLOqZ2OurOPzOk1ULhxmRnFN09COFW69vOpHunmPVwlrR%2FDxqi9guzPSorM%2B2zATwr6szNGSl%2BRvOcfUKOZERoLnYpOb5EO1YMnFwNYa3w656fl4TH2zE0Ql934y5ZQ%2B8U7rUCowfWqy4OFp2X2apYo1fgh7h8yhH76MWMXXwbViaaMunRS5%2FmHgNVM%2Bb2QxMY9jpH6eoff%2FFYC5z%2BSIRiupK3GHfkTl70m86gZ3%2Fr6%2FGqZzBZntse3xX0PCc38aHRaOxOd2JJMKDlwc4GOqUB6p7FyBy0MC%2BPj4xAjPkg6twPD4ITzvg7GXOozyA%2FTAGZkJgRM3MakcIL6GhzDuvd%2FkVTIyNMerPIWnITPcKKDqdquxK%2BJ1fzvypWS42%2F956i1z6ySF3P1afhkyllqyk9ULM8dqkhJ5kAlYCV%2BfRwy2QiWITvxs8QYMNnWMbjP1ud%2Beyb9xeOPx9rFTuwTnqaUg6ws8xDUrviwYAvN1OKlsIC6oHU&X-Amz-Signature=184e4fbcb12ea0627733e7b5b9c3ea020b7b01dda742c5aa712e5ded1417004d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

