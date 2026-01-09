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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMNITOYA%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T025954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZxv3l1y51oMMD0AGWhekYNq4JpxYNt%2BOEBDZn5GKYmAiEA40FD71tJHV1E0tTbLscNhhsJP7L%2FZJ0W%2FL3SNmxAm60qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIovq32HyW8APcqnXCrcA2TrFCwFfC4JrKajkf1ZSE8fgdagU7efv6k%2B9Lk%2FhzyUA6DNnnP71oPfSQeAvKrjZHLN0H%2FLdNdxFlmGca5qdVQVGe%2BesKDxC%2BlZCouMWuoKv2ducY1ZHiBDRhyfsGqIGUS8TIuP7n6yecbw8FZVfOI91hyDb4Eqpq5buTv98MfcBlbhIZEerd1WqBEluNPg%2B4KBEWwuz0zcWjsSv%2F98%2FyJu%2F0R2%2FLaS9lqLPqdGCESm%2BkEQ0jgaewrk6pDTU5JoGoVa6Fba23t9%2BMnmtq2H2%2B6PskN%2F8q0u2akIJLPwCL0ytV1VCxGAR6COVNfx4flxOfO%2FJGmfxGi0IvgD843bJ%2FetOuavdh%2FeSfyEQi2WQUFMhztZaekdu%2BL1boE%2F45x9aayGgPEuBhtxRdaE2NMWrbGbhZTEUQfA4OIyDzNOSWK0KueKLmGG3R%2B0o8qFO4mKVD3SWNX6tTH1YaMJecFnfHBBZa36xEjt3Z8fvLxIbXwT8wzBWmrt6r4Lh0Rhm%2FAxUS6QNqabwCefeKdG9YL5ZIBQ4kZRaUBxw3%2FtvGLtS2%2FITrlNi3rvb7V4sFqFk1jJGVLxEzGM%2Bh1UOMw3sksO8qg86qjKH6k8bii6cQH2nIhq1WrLHXl9OYACGGVCMJLFgcsGOqUBmNxH%2BtXDiCDXor68xBqi7fxO1g1YPBa4Bi%2BKvfXGmKgc%2FhBaaSLyAtas2CBy9%2Bw3qVW0ajrMw%2BmHNy6jrH6lsSBKe8EAkEKZ864LCHRvCmNH3UMli9RMnzbfcDIwCsZl3ZK%2BJ%2FzPA619Q20p5kUgZp56F2Nn0eUdK8gm8kdM8S5wUGLCa3qZQ1WkxMvwC5pm%2FbflJHGD1jw8alKfll2U0SJCNXTM&X-Amz-Signature=c388945b6bf7eb8d47e6d2327b312ef32302988977133cd6c141d9df03d1a230&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMNITOYA%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T025954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZxv3l1y51oMMD0AGWhekYNq4JpxYNt%2BOEBDZn5GKYmAiEA40FD71tJHV1E0tTbLscNhhsJP7L%2FZJ0W%2FL3SNmxAm60qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIovq32HyW8APcqnXCrcA2TrFCwFfC4JrKajkf1ZSE8fgdagU7efv6k%2B9Lk%2FhzyUA6DNnnP71oPfSQeAvKrjZHLN0H%2FLdNdxFlmGca5qdVQVGe%2BesKDxC%2BlZCouMWuoKv2ducY1ZHiBDRhyfsGqIGUS8TIuP7n6yecbw8FZVfOI91hyDb4Eqpq5buTv98MfcBlbhIZEerd1WqBEluNPg%2B4KBEWwuz0zcWjsSv%2F98%2FyJu%2F0R2%2FLaS9lqLPqdGCESm%2BkEQ0jgaewrk6pDTU5JoGoVa6Fba23t9%2BMnmtq2H2%2B6PskN%2F8q0u2akIJLPwCL0ytV1VCxGAR6COVNfx4flxOfO%2FJGmfxGi0IvgD843bJ%2FetOuavdh%2FeSfyEQi2WQUFMhztZaekdu%2BL1boE%2F45x9aayGgPEuBhtxRdaE2NMWrbGbhZTEUQfA4OIyDzNOSWK0KueKLmGG3R%2B0o8qFO4mKVD3SWNX6tTH1YaMJecFnfHBBZa36xEjt3Z8fvLxIbXwT8wzBWmrt6r4Lh0Rhm%2FAxUS6QNqabwCefeKdG9YL5ZIBQ4kZRaUBxw3%2FtvGLtS2%2FITrlNi3rvb7V4sFqFk1jJGVLxEzGM%2Bh1UOMw3sksO8qg86qjKH6k8bii6cQH2nIhq1WrLHXl9OYACGGVCMJLFgcsGOqUBmNxH%2BtXDiCDXor68xBqi7fxO1g1YPBa4Bi%2BKvfXGmKgc%2FhBaaSLyAtas2CBy9%2Bw3qVW0ajrMw%2BmHNy6jrH6lsSBKe8EAkEKZ864LCHRvCmNH3UMli9RMnzbfcDIwCsZl3ZK%2BJ%2FzPA619Q20p5kUgZp56F2Nn0eUdK8gm8kdM8S5wUGLCa3qZQ1WkxMvwC5pm%2FbflJHGD1jw8alKfll2U0SJCNXTM&X-Amz-Signature=a0298f485693e1d4ac07cc1fe2125469b2d0eb3bcd952cae6a5d4367fe8283bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMNITOYA%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T025954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZxv3l1y51oMMD0AGWhekYNq4JpxYNt%2BOEBDZn5GKYmAiEA40FD71tJHV1E0tTbLscNhhsJP7L%2FZJ0W%2FL3SNmxAm60qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIovq32HyW8APcqnXCrcA2TrFCwFfC4JrKajkf1ZSE8fgdagU7efv6k%2B9Lk%2FhzyUA6DNnnP71oPfSQeAvKrjZHLN0H%2FLdNdxFlmGca5qdVQVGe%2BesKDxC%2BlZCouMWuoKv2ducY1ZHiBDRhyfsGqIGUS8TIuP7n6yecbw8FZVfOI91hyDb4Eqpq5buTv98MfcBlbhIZEerd1WqBEluNPg%2B4KBEWwuz0zcWjsSv%2F98%2FyJu%2F0R2%2FLaS9lqLPqdGCESm%2BkEQ0jgaewrk6pDTU5JoGoVa6Fba23t9%2BMnmtq2H2%2B6PskN%2F8q0u2akIJLPwCL0ytV1VCxGAR6COVNfx4flxOfO%2FJGmfxGi0IvgD843bJ%2FetOuavdh%2FeSfyEQi2WQUFMhztZaekdu%2BL1boE%2F45x9aayGgPEuBhtxRdaE2NMWrbGbhZTEUQfA4OIyDzNOSWK0KueKLmGG3R%2B0o8qFO4mKVD3SWNX6tTH1YaMJecFnfHBBZa36xEjt3Z8fvLxIbXwT8wzBWmrt6r4Lh0Rhm%2FAxUS6QNqabwCefeKdG9YL5ZIBQ4kZRaUBxw3%2FtvGLtS2%2FITrlNi3rvb7V4sFqFk1jJGVLxEzGM%2Bh1UOMw3sksO8qg86qjKH6k8bii6cQH2nIhq1WrLHXl9OYACGGVCMJLFgcsGOqUBmNxH%2BtXDiCDXor68xBqi7fxO1g1YPBa4Bi%2BKvfXGmKgc%2FhBaaSLyAtas2CBy9%2Bw3qVW0ajrMw%2BmHNy6jrH6lsSBKe8EAkEKZ864LCHRvCmNH3UMli9RMnzbfcDIwCsZl3ZK%2BJ%2FzPA619Q20p5kUgZp56F2Nn0eUdK8gm8kdM8S5wUGLCa3qZQ1WkxMvwC5pm%2FbflJHGD1jw8alKfll2U0SJCNXTM&X-Amz-Signature=8ed52ae88220ac098c9ee2bb881c0f49a0f024fc396998e9af2a97dcd607d4e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

