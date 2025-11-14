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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656OXARZ3%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICqPAYB1NTZqg2orCciCSfIusw6EsiBdetV1hRwj0ex%2BAiBVERn0VUPrhe7rBSRwVFAbsIONOgLgLY9%2Bdjqj3BjViir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMMFcs2bMIDz9fBL74KtwDK%2F61%2BOUVAubMAHav%2F%2F2A2KMnW%2FstBI4Btu9Lf4rokHVkh7njrEmHnjvYIC4jUaXxGRoZ2EH%2Bn6whxN31YKAXOf16pWrfgrY5IWvqDkCh3m9Te0FqitEVhuEQEi26rjnEDgUGX8TqHXytlLmb1gFaAcJ72XKISfwXaOQ75tjnE1xJigH0DLYyXO1LRLBrhv9MtaQNfLOp4waO9thR8gt66zEVDOGHcvriHjVG4enRjniN%2FnfrOgT0XLoWoyHMC6HcaAFEYEI4Gj0mpfYPIyvCYrZ2K580C4Z9GWWgX9vpdmHkB2d3Rp4le1qFRVoswBM81jMRt0xbRNHyK897rV9UrrWmX7wszocNz%2BaDD3FWK8Yt3azyzviiBLgZd6kUV%2Bfqq9hu5Mi5GaeAYc6q0CTgx7IW1FWk6mkEULWjKDzyB5xNoqkDGeV%2BKbfq6Im7vM1yLWFKTsJOM4XFQvtGvnf%2B71aKRD975%2BfFPVC4Kb3d%2B1MVTG4UK7I7NyX55DOznsKCHOCEY4kNlpVDw71Pfkh7%2Bj0zrfyXXG%2BxFtvydowZotfc0SJMletvr4%2FIcwJ7qPFqdlOly3T%2BYBxS7qF7UxE%2BlGTwQeH3ae9Km27CiPgnOHNPsYeLBBQ8i0rrP%2BowhorayAY6pgHVL4mTd6k3G93T6C4zyeu8uGhxmCXJjonBWBsTqL1JUZcdANnS4%2FpEIKlpaJ62ba62ehomof9aeJBJeY4fpl7jd0WdOoKsWWT%2Fkw3iPxgF69SGcgRdzklZGN4dmbXx%2BhiIll8%2FhkCJv4NLP3%2F%2B8wI4Q8k0FBQ4%2BuSMLeXolTkRfDni3mkfRjqVrr7%2FtzH8mpCENLyigLBrCdrDFMuOD4YtAeFSd6V1&X-Amz-Signature=4c97cc7ef636ed40f650080a4f5c4a13c2e70aec8944b23ea8a6f19a59df239c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656OXARZ3%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICqPAYB1NTZqg2orCciCSfIusw6EsiBdetV1hRwj0ex%2BAiBVERn0VUPrhe7rBSRwVFAbsIONOgLgLY9%2Bdjqj3BjViir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMMFcs2bMIDz9fBL74KtwDK%2F61%2BOUVAubMAHav%2F%2F2A2KMnW%2FstBI4Btu9Lf4rokHVkh7njrEmHnjvYIC4jUaXxGRoZ2EH%2Bn6whxN31YKAXOf16pWrfgrY5IWvqDkCh3m9Te0FqitEVhuEQEi26rjnEDgUGX8TqHXytlLmb1gFaAcJ72XKISfwXaOQ75tjnE1xJigH0DLYyXO1LRLBrhv9MtaQNfLOp4waO9thR8gt66zEVDOGHcvriHjVG4enRjniN%2FnfrOgT0XLoWoyHMC6HcaAFEYEI4Gj0mpfYPIyvCYrZ2K580C4Z9GWWgX9vpdmHkB2d3Rp4le1qFRVoswBM81jMRt0xbRNHyK897rV9UrrWmX7wszocNz%2BaDD3FWK8Yt3azyzviiBLgZd6kUV%2Bfqq9hu5Mi5GaeAYc6q0CTgx7IW1FWk6mkEULWjKDzyB5xNoqkDGeV%2BKbfq6Im7vM1yLWFKTsJOM4XFQvtGvnf%2B71aKRD975%2BfFPVC4Kb3d%2B1MVTG4UK7I7NyX55DOznsKCHOCEY4kNlpVDw71Pfkh7%2Bj0zrfyXXG%2BxFtvydowZotfc0SJMletvr4%2FIcwJ7qPFqdlOly3T%2BYBxS7qF7UxE%2BlGTwQeH3ae9Km27CiPgnOHNPsYeLBBQ8i0rrP%2BowhorayAY6pgHVL4mTd6k3G93T6C4zyeu8uGhxmCXJjonBWBsTqL1JUZcdANnS4%2FpEIKlpaJ62ba62ehomof9aeJBJeY4fpl7jd0WdOoKsWWT%2Fkw3iPxgF69SGcgRdzklZGN4dmbXx%2BhiIll8%2FhkCJv4NLP3%2F%2B8wI4Q8k0FBQ4%2BuSMLeXolTkRfDni3mkfRjqVrr7%2FtzH8mpCENLyigLBrCdrDFMuOD4YtAeFSd6V1&X-Amz-Signature=c31284e5aa97a5dec855e06c3ddc22e8d771719224aa5435f15998061b89e885&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656OXARZ3%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICqPAYB1NTZqg2orCciCSfIusw6EsiBdetV1hRwj0ex%2BAiBVERn0VUPrhe7rBSRwVFAbsIONOgLgLY9%2Bdjqj3BjViir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMMFcs2bMIDz9fBL74KtwDK%2F61%2BOUVAubMAHav%2F%2F2A2KMnW%2FstBI4Btu9Lf4rokHVkh7njrEmHnjvYIC4jUaXxGRoZ2EH%2Bn6whxN31YKAXOf16pWrfgrY5IWvqDkCh3m9Te0FqitEVhuEQEi26rjnEDgUGX8TqHXytlLmb1gFaAcJ72XKISfwXaOQ75tjnE1xJigH0DLYyXO1LRLBrhv9MtaQNfLOp4waO9thR8gt66zEVDOGHcvriHjVG4enRjniN%2FnfrOgT0XLoWoyHMC6HcaAFEYEI4Gj0mpfYPIyvCYrZ2K580C4Z9GWWgX9vpdmHkB2d3Rp4le1qFRVoswBM81jMRt0xbRNHyK897rV9UrrWmX7wszocNz%2BaDD3FWK8Yt3azyzviiBLgZd6kUV%2Bfqq9hu5Mi5GaeAYc6q0CTgx7IW1FWk6mkEULWjKDzyB5xNoqkDGeV%2BKbfq6Im7vM1yLWFKTsJOM4XFQvtGvnf%2B71aKRD975%2BfFPVC4Kb3d%2B1MVTG4UK7I7NyX55DOznsKCHOCEY4kNlpVDw71Pfkh7%2Bj0zrfyXXG%2BxFtvydowZotfc0SJMletvr4%2FIcwJ7qPFqdlOly3T%2BYBxS7qF7UxE%2BlGTwQeH3ae9Km27CiPgnOHNPsYeLBBQ8i0rrP%2BowhorayAY6pgHVL4mTd6k3G93T6C4zyeu8uGhxmCXJjonBWBsTqL1JUZcdANnS4%2FpEIKlpaJ62ba62ehomof9aeJBJeY4fpl7jd0WdOoKsWWT%2Fkw3iPxgF69SGcgRdzklZGN4dmbXx%2BhiIll8%2FhkCJv4NLP3%2F%2B8wI4Q8k0FBQ4%2BuSMLeXolTkRfDni3mkfRjqVrr7%2FtzH8mpCENLyigLBrCdrDFMuOD4YtAeFSd6V1&X-Amz-Signature=005614f1f42b81319170b1c6651819257fb537da2b09bd2e50542b4311bd8bc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

