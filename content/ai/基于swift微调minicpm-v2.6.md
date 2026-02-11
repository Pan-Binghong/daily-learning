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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR75X7NP%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnkMFiZpb33RKHJBX5dhpSvbo%2BcLH67S29FhtHCc2GSwIgFJHacEqLLpwzz0QRuhyMaZil6cyFlLzLZ5P0xRYzHBsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcaRGnenLJk9JGLFSrcAwrF4ybfBVNSnRj7QnEfDdlW4Qd88IJmPLjn8flgmug6DUarJdwnkx%2FbfSzC0S7NE%2FJ34snYpUrRWeja9jH99Z0xklA%2F42OD%2FE%2BwJHQy%2FFzeDg2xcRgf61f8vgrAERHZSbrcuc9LA9MWm93e%2BgKmTxQL6pSiB8XTQqCWC2Ytt2qyb6VN8pvejzQR75IcZp%2FAh3DpdumYjSfSOUdjcHmHpQj%2B1Z4RjoueTxB4SijxTgibosOexmoWzjYSkXh2vFRQgoGS4zPPrbdJNUSYAT51GO4jcPNy9WojC5eCdtcVMYI1BnvA9kXfXMEq7FovFLH8wp9rlU7X04%2FpOrW3VrADfkbzEydralucDhXqQ%2BoAQ4c2WgpvVQhZNJhPmT%2F26eIy%2BNESI9QvKz0henfri9ntBjmk%2Fk1Qrvbln963KvDAEg8Sp0p1C0BQDVZGt19JQ36WT0Lf3eaPFOt0hOh5U1u4xe94w2kugkeSm2ee0P4aCiJH41RQJsVFsSkaFncNdsrt5FHElHjY3ajd1ivGwn7abLU4%2BBEy2GaBTQ8XcV4MYVVijDySDNh3J1xkFlaBvmiZ3JH7S73O1YeQuL51h5vXmT9m%2BzpjRBdnOqcvX%2F93ZFYP9mUaWK5FQAt2AzCdMKPLr8wGOqUBXBF3DeI%2BFvkr6gAA1kJJ%2BOq%2BlGtuuGzOCEnHROh%2FJbkLt2U6oUPDK30NZYkcfBs3gzmZtrKVx8oLLMhUvF%2BVrQ4Ep6%2FtF0UN4MN89mnd%2FbndzJhM7hd4gJ7gitiUZKaX2z%2FXjvEE5axFNvLgCTgSW3%2BMQzMVHt6H4Jl9IhMaONt3Rq6KSk56WdI0uvQyhYbqpG6mu%2B4MZA0bPLSV7Q8prVCeMHb6&X-Amz-Signature=2d0b2ca7c627bbd515704cf2f7060928be333c3b828e1b82705f6a789637b9ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR75X7NP%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnkMFiZpb33RKHJBX5dhpSvbo%2BcLH67S29FhtHCc2GSwIgFJHacEqLLpwzz0QRuhyMaZil6cyFlLzLZ5P0xRYzHBsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcaRGnenLJk9JGLFSrcAwrF4ybfBVNSnRj7QnEfDdlW4Qd88IJmPLjn8flgmug6DUarJdwnkx%2FbfSzC0S7NE%2FJ34snYpUrRWeja9jH99Z0xklA%2F42OD%2FE%2BwJHQy%2FFzeDg2xcRgf61f8vgrAERHZSbrcuc9LA9MWm93e%2BgKmTxQL6pSiB8XTQqCWC2Ytt2qyb6VN8pvejzQR75IcZp%2FAh3DpdumYjSfSOUdjcHmHpQj%2B1Z4RjoueTxB4SijxTgibosOexmoWzjYSkXh2vFRQgoGS4zPPrbdJNUSYAT51GO4jcPNy9WojC5eCdtcVMYI1BnvA9kXfXMEq7FovFLH8wp9rlU7X04%2FpOrW3VrADfkbzEydralucDhXqQ%2BoAQ4c2WgpvVQhZNJhPmT%2F26eIy%2BNESI9QvKz0henfri9ntBjmk%2Fk1Qrvbln963KvDAEg8Sp0p1C0BQDVZGt19JQ36WT0Lf3eaPFOt0hOh5U1u4xe94w2kugkeSm2ee0P4aCiJH41RQJsVFsSkaFncNdsrt5FHElHjY3ajd1ivGwn7abLU4%2BBEy2GaBTQ8XcV4MYVVijDySDNh3J1xkFlaBvmiZ3JH7S73O1YeQuL51h5vXmT9m%2BzpjRBdnOqcvX%2F93ZFYP9mUaWK5FQAt2AzCdMKPLr8wGOqUBXBF3DeI%2BFvkr6gAA1kJJ%2BOq%2BlGtuuGzOCEnHROh%2FJbkLt2U6oUPDK30NZYkcfBs3gzmZtrKVx8oLLMhUvF%2BVrQ4Ep6%2FtF0UN4MN89mnd%2FbndzJhM7hd4gJ7gitiUZKaX2z%2FXjvEE5axFNvLgCTgSW3%2BMQzMVHt6H4Jl9IhMaONt3Rq6KSk56WdI0uvQyhYbqpG6mu%2B4MZA0bPLSV7Q8prVCeMHb6&X-Amz-Signature=80cd4ec34049b6ecc9ea99e01ffe013ddb93698ba3ee67609c45faf494395beb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR75X7NP%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnkMFiZpb33RKHJBX5dhpSvbo%2BcLH67S29FhtHCc2GSwIgFJHacEqLLpwzz0QRuhyMaZil6cyFlLzLZ5P0xRYzHBsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcaRGnenLJk9JGLFSrcAwrF4ybfBVNSnRj7QnEfDdlW4Qd88IJmPLjn8flgmug6DUarJdwnkx%2FbfSzC0S7NE%2FJ34snYpUrRWeja9jH99Z0xklA%2F42OD%2FE%2BwJHQy%2FFzeDg2xcRgf61f8vgrAERHZSbrcuc9LA9MWm93e%2BgKmTxQL6pSiB8XTQqCWC2Ytt2qyb6VN8pvejzQR75IcZp%2FAh3DpdumYjSfSOUdjcHmHpQj%2B1Z4RjoueTxB4SijxTgibosOexmoWzjYSkXh2vFRQgoGS4zPPrbdJNUSYAT51GO4jcPNy9WojC5eCdtcVMYI1BnvA9kXfXMEq7FovFLH8wp9rlU7X04%2FpOrW3VrADfkbzEydralucDhXqQ%2BoAQ4c2WgpvVQhZNJhPmT%2F26eIy%2BNESI9QvKz0henfri9ntBjmk%2Fk1Qrvbln963KvDAEg8Sp0p1C0BQDVZGt19JQ36WT0Lf3eaPFOt0hOh5U1u4xe94w2kugkeSm2ee0P4aCiJH41RQJsVFsSkaFncNdsrt5FHElHjY3ajd1ivGwn7abLU4%2BBEy2GaBTQ8XcV4MYVVijDySDNh3J1xkFlaBvmiZ3JH7S73O1YeQuL51h5vXmT9m%2BzpjRBdnOqcvX%2F93ZFYP9mUaWK5FQAt2AzCdMKPLr8wGOqUBXBF3DeI%2BFvkr6gAA1kJJ%2BOq%2BlGtuuGzOCEnHROh%2FJbkLt2U6oUPDK30NZYkcfBs3gzmZtrKVx8oLLMhUvF%2BVrQ4Ep6%2FtF0UN4MN89mnd%2FbndzJhM7hd4gJ7gitiUZKaX2z%2FXjvEE5axFNvLgCTgSW3%2BMQzMVHt6H4Jl9IhMaONt3Rq6KSk56WdI0uvQyhYbqpG6mu%2B4MZA0bPLSV7Q8prVCeMHb6&X-Amz-Signature=0354888052de7ae2d8d5fc75e69b04858404ff9a30602b5bf5a533e90f6dec6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

