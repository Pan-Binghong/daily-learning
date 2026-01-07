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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JVSR4AQ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6M4G0dlaoqGsPYeQHrvvyZToPmKOOQhX76kcCg585QwIgID%2F9cS6VaNjPg4qpVSrrOKnz5xaxdbvRCZUDW6vcP7Eq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDBD0zMVbgz6zcw9YgSrcA6bFmfx%2BoOhXlWpJej88W4RWStF7xRqZfOGTlvE20%2B76Gf69GbCNJJ3FN3p9pI3DlqWKl9%2Bb8WS%2B%2Fi4hrb6rwBDqZse2Z8l2H5mY8omr68eZ6p0urVUs9BORXm6v6u05P5cnTVti2lYVxDaFLiV7U03eRNffUyZuPnX2552g38VwqeCQl7CBb47v6T%2BeRCSQhKeSREmplE5IQBddy%2F4bg8FApvrlvvSpv5TdwSFKiXjtBztEl7qvKvYCUNzLmnvYQqsuG4s4H5PAzWy3MT9SsJ3yD6fpuHVLg64ubBVqsCEh6X1j%2BB%2FwF1gtahye9rqDGjSlT6l%2BqoCQF9yA8dbINWQ4bPriJjuYUPrdlFEIrnvqbvS3XV5MqA1%2BmGkOVPw6kWhFEChtAewesEiiptq3ovDXjeLPeBFbXSGO2eao1mwRF5hYI63vxjV1ofmZSQM6%2BOv33CWoPB96J09iGLPdin7NCykwzScZ9%2FF4kux5tF04Ox4SNNL0iL%2B2d%2Fdt35XVovOMUfpfRpYqVoyA%2BWjYPJxJxQplRbN19t%2FRAdKJkzg%2B1fgBbyBeRaWKEomgKp%2BJ9k1DlrqIM7YMwEVXFRJbctN4MZgm2rfHQ6VtPbOfCITHgFjcXo%2BkxWfLgkcAMOGP98oGOqUBTrl3DRwB6T9e7dcJ2Rvw5OclI1T6g92FyndmhGtMKhaDgaVQpC7Jx8vBrsEK%2FBeGXcleC6Kxb%2BqKF%2FChLgKr22jvB34bGrjGtMRyhtUEiElIj6q9YUiuj6Oorpn2w470c9ZixtWZGvn24YLgkxfvgB2LRYsfYIU448JYPZPCOgQ6%2BAQnqdQdhYEilbSy8Ktg3BwOuAKGy1dJ%2FIgkmekuwudYgfn%2F&X-Amz-Signature=cfdf92ca55053ce782e35b7c4a43b6ff7d09f9d78ef88fe2e11e21b19555a73c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JVSR4AQ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6M4G0dlaoqGsPYeQHrvvyZToPmKOOQhX76kcCg585QwIgID%2F9cS6VaNjPg4qpVSrrOKnz5xaxdbvRCZUDW6vcP7Eq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDBD0zMVbgz6zcw9YgSrcA6bFmfx%2BoOhXlWpJej88W4RWStF7xRqZfOGTlvE20%2B76Gf69GbCNJJ3FN3p9pI3DlqWKl9%2Bb8WS%2B%2Fi4hrb6rwBDqZse2Z8l2H5mY8omr68eZ6p0urVUs9BORXm6v6u05P5cnTVti2lYVxDaFLiV7U03eRNffUyZuPnX2552g38VwqeCQl7CBb47v6T%2BeRCSQhKeSREmplE5IQBddy%2F4bg8FApvrlvvSpv5TdwSFKiXjtBztEl7qvKvYCUNzLmnvYQqsuG4s4H5PAzWy3MT9SsJ3yD6fpuHVLg64ubBVqsCEh6X1j%2BB%2FwF1gtahye9rqDGjSlT6l%2BqoCQF9yA8dbINWQ4bPriJjuYUPrdlFEIrnvqbvS3XV5MqA1%2BmGkOVPw6kWhFEChtAewesEiiptq3ovDXjeLPeBFbXSGO2eao1mwRF5hYI63vxjV1ofmZSQM6%2BOv33CWoPB96J09iGLPdin7NCykwzScZ9%2FF4kux5tF04Ox4SNNL0iL%2B2d%2Fdt35XVovOMUfpfRpYqVoyA%2BWjYPJxJxQplRbN19t%2FRAdKJkzg%2B1fgBbyBeRaWKEomgKp%2BJ9k1DlrqIM7YMwEVXFRJbctN4MZgm2rfHQ6VtPbOfCITHgFjcXo%2BkxWfLgkcAMOGP98oGOqUBTrl3DRwB6T9e7dcJ2Rvw5OclI1T6g92FyndmhGtMKhaDgaVQpC7Jx8vBrsEK%2FBeGXcleC6Kxb%2BqKF%2FChLgKr22jvB34bGrjGtMRyhtUEiElIj6q9YUiuj6Oorpn2w470c9ZixtWZGvn24YLgkxfvgB2LRYsfYIU448JYPZPCOgQ6%2BAQnqdQdhYEilbSy8Ktg3BwOuAKGy1dJ%2FIgkmekuwudYgfn%2F&X-Amz-Signature=c8f9f849f7d714ef10fb9ad466c08ab86a8978e21ffae25458eaf88ac191eb03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JVSR4AQ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6M4G0dlaoqGsPYeQHrvvyZToPmKOOQhX76kcCg585QwIgID%2F9cS6VaNjPg4qpVSrrOKnz5xaxdbvRCZUDW6vcP7Eq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDBD0zMVbgz6zcw9YgSrcA6bFmfx%2BoOhXlWpJej88W4RWStF7xRqZfOGTlvE20%2B76Gf69GbCNJJ3FN3p9pI3DlqWKl9%2Bb8WS%2B%2Fi4hrb6rwBDqZse2Z8l2H5mY8omr68eZ6p0urVUs9BORXm6v6u05P5cnTVti2lYVxDaFLiV7U03eRNffUyZuPnX2552g38VwqeCQl7CBb47v6T%2BeRCSQhKeSREmplE5IQBddy%2F4bg8FApvrlvvSpv5TdwSFKiXjtBztEl7qvKvYCUNzLmnvYQqsuG4s4H5PAzWy3MT9SsJ3yD6fpuHVLg64ubBVqsCEh6X1j%2BB%2FwF1gtahye9rqDGjSlT6l%2BqoCQF9yA8dbINWQ4bPriJjuYUPrdlFEIrnvqbvS3XV5MqA1%2BmGkOVPw6kWhFEChtAewesEiiptq3ovDXjeLPeBFbXSGO2eao1mwRF5hYI63vxjV1ofmZSQM6%2BOv33CWoPB96J09iGLPdin7NCykwzScZ9%2FF4kux5tF04Ox4SNNL0iL%2B2d%2Fdt35XVovOMUfpfRpYqVoyA%2BWjYPJxJxQplRbN19t%2FRAdKJkzg%2B1fgBbyBeRaWKEomgKp%2BJ9k1DlrqIM7YMwEVXFRJbctN4MZgm2rfHQ6VtPbOfCITHgFjcXo%2BkxWfLgkcAMOGP98oGOqUBTrl3DRwB6T9e7dcJ2Rvw5OclI1T6g92FyndmhGtMKhaDgaVQpC7Jx8vBrsEK%2FBeGXcleC6Kxb%2BqKF%2FChLgKr22jvB34bGrjGtMRyhtUEiElIj6q9YUiuj6Oorpn2w470c9ZixtWZGvn24YLgkxfvgB2LRYsfYIU448JYPZPCOgQ6%2BAQnqdQdhYEilbSy8Ktg3BwOuAKGy1dJ%2FIgkmekuwudYgfn%2F&X-Amz-Signature=678a4242df04266f3d1ac735bb791bd2b4395e01b321885a204ad6af07939f3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

