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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZHXPLMM%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIHcmTPpJ%2BUMDA8K9eYhZ5OiffA278rzH%2BBFipD3%2BmQQjAiBEZXkip9mbgT7OLC4barEmI02O1Lyu5PkHlTL3HC2lYiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM13ncPiSNbxSg%2FUWqKtwD1Y0e9NOu2fvxobK2PzoFN8o0zkMrN93jBhnLgXEy7g7coW6gHBDEZqXPNj86Hk5OVKy9JDX%2FuodxtR%2BJKsSLH60Tj2DfXNopeUpnu8sVDPWHsvXxMolylvMv9BMtWLOidRUIm189WRgnGl4P4XfwYRHWQzFJRu%2BarPKia6zhI9WRmptbggejPMWgyXoEcUFKEp2PoyHvgMufBxLs4V%2BuVH%2BTegfz8ew5xlds9n8PGcLE3Qkz%2BYmj%2BLbjL8rBCvRzeDUjeHrtzyTkllp%2F0tEvFi7q7xMI9%2FY8kPPHW1Vy7UCECLYdAed%2F6Kvr83uOss7GNlUJWtewVQUvrXaZhQO282IwC5TvrmAR1M%2FFlZgf18DU1H724%2FOHZN8DaRMpRxKQMFksCzk0xf0v4CTYSgivDd90RmFi3Rs5ZnhhhOWcT0Cdzb7xXY%2FwMJgkrgMQxNyP%2F%2Fl2uvj%2BoFPubaih7usugsriuIeaJ6J6PogioTB7tvS4IGpijQvN9c4nbmSKTsFOkhX1PCWg9RB%2BnjgMBIUxKhg%2Fj8rCiB0YYHl60nfimsPV1%2FM%2BE6u7jj0lfWIr%2FI%2BzqDuvpadfcVstDjcNgmUERDhsq8HGU0dS68M9lGL4GFALA6Ro85xL%2BYSSz2MwtsutyQY6pgEUgKhFa3IaTdWXtZPkB5G5OP4bJONlxaazHSMsZzzIUQVyb7khkv4t1F4XObedPGYZUx2Z%2BXy3ypL1XG6IVIaIl3mJEucPBPpKZxROIrmsHnUaKGdKh0Ywq%2FWfXzuKGVijtkZ%2BXFgBYvPwReCMDZxBR3W3h7vMU21esWjzqMHvKsVkBQe13sXzZCx9Mcfezi3CSAOtjTOSItnopMd2YDpGxs17PVJn&X-Amz-Signature=2a619c30ed88a41317df208a0f456c0814523656c41e63f035006d7feec02255&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZHXPLMM%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIHcmTPpJ%2BUMDA8K9eYhZ5OiffA278rzH%2BBFipD3%2BmQQjAiBEZXkip9mbgT7OLC4barEmI02O1Lyu5PkHlTL3HC2lYiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM13ncPiSNbxSg%2FUWqKtwD1Y0e9NOu2fvxobK2PzoFN8o0zkMrN93jBhnLgXEy7g7coW6gHBDEZqXPNj86Hk5OVKy9JDX%2FuodxtR%2BJKsSLH60Tj2DfXNopeUpnu8sVDPWHsvXxMolylvMv9BMtWLOidRUIm189WRgnGl4P4XfwYRHWQzFJRu%2BarPKia6zhI9WRmptbggejPMWgyXoEcUFKEp2PoyHvgMufBxLs4V%2BuVH%2BTegfz8ew5xlds9n8PGcLE3Qkz%2BYmj%2BLbjL8rBCvRzeDUjeHrtzyTkllp%2F0tEvFi7q7xMI9%2FY8kPPHW1Vy7UCECLYdAed%2F6Kvr83uOss7GNlUJWtewVQUvrXaZhQO282IwC5TvrmAR1M%2FFlZgf18DU1H724%2FOHZN8DaRMpRxKQMFksCzk0xf0v4CTYSgivDd90RmFi3Rs5ZnhhhOWcT0Cdzb7xXY%2FwMJgkrgMQxNyP%2F%2Fl2uvj%2BoFPubaih7usugsriuIeaJ6J6PogioTB7tvS4IGpijQvN9c4nbmSKTsFOkhX1PCWg9RB%2BnjgMBIUxKhg%2Fj8rCiB0YYHl60nfimsPV1%2FM%2BE6u7jj0lfWIr%2FI%2BzqDuvpadfcVstDjcNgmUERDhsq8HGU0dS68M9lGL4GFALA6Ro85xL%2BYSSz2MwtsutyQY6pgEUgKhFa3IaTdWXtZPkB5G5OP4bJONlxaazHSMsZzzIUQVyb7khkv4t1F4XObedPGYZUx2Z%2BXy3ypL1XG6IVIaIl3mJEucPBPpKZxROIrmsHnUaKGdKh0Ywq%2FWfXzuKGVijtkZ%2BXFgBYvPwReCMDZxBR3W3h7vMU21esWjzqMHvKsVkBQe13sXzZCx9Mcfezi3CSAOtjTOSItnopMd2YDpGxs17PVJn&X-Amz-Signature=fb602e7fd2bb702b3618e7c50faf5bd9393764e40d23bf8ec4e92d6361c11b28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZHXPLMM%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIHcmTPpJ%2BUMDA8K9eYhZ5OiffA278rzH%2BBFipD3%2BmQQjAiBEZXkip9mbgT7OLC4barEmI02O1Lyu5PkHlTL3HC2lYiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM13ncPiSNbxSg%2FUWqKtwD1Y0e9NOu2fvxobK2PzoFN8o0zkMrN93jBhnLgXEy7g7coW6gHBDEZqXPNj86Hk5OVKy9JDX%2FuodxtR%2BJKsSLH60Tj2DfXNopeUpnu8sVDPWHsvXxMolylvMv9BMtWLOidRUIm189WRgnGl4P4XfwYRHWQzFJRu%2BarPKia6zhI9WRmptbggejPMWgyXoEcUFKEp2PoyHvgMufBxLs4V%2BuVH%2BTegfz8ew5xlds9n8PGcLE3Qkz%2BYmj%2BLbjL8rBCvRzeDUjeHrtzyTkllp%2F0tEvFi7q7xMI9%2FY8kPPHW1Vy7UCECLYdAed%2F6Kvr83uOss7GNlUJWtewVQUvrXaZhQO282IwC5TvrmAR1M%2FFlZgf18DU1H724%2FOHZN8DaRMpRxKQMFksCzk0xf0v4CTYSgivDd90RmFi3Rs5ZnhhhOWcT0Cdzb7xXY%2FwMJgkrgMQxNyP%2F%2Fl2uvj%2BoFPubaih7usugsriuIeaJ6J6PogioTB7tvS4IGpijQvN9c4nbmSKTsFOkhX1PCWg9RB%2BnjgMBIUxKhg%2Fj8rCiB0YYHl60nfimsPV1%2FM%2BE6u7jj0lfWIr%2FI%2BzqDuvpadfcVstDjcNgmUERDhsq8HGU0dS68M9lGL4GFALA6Ro85xL%2BYSSz2MwtsutyQY6pgEUgKhFa3IaTdWXtZPkB5G5OP4bJONlxaazHSMsZzzIUQVyb7khkv4t1F4XObedPGYZUx2Z%2BXy3ypL1XG6IVIaIl3mJEucPBPpKZxROIrmsHnUaKGdKh0Ywq%2FWfXzuKGVijtkZ%2BXFgBYvPwReCMDZxBR3W3h7vMU21esWjzqMHvKsVkBQe13sXzZCx9Mcfezi3CSAOtjTOSItnopMd2YDpGxs17PVJn&X-Amz-Signature=e708d07ac0c55042ffe77fd2a337dbd9f64a4c85966501fd4d40568af95842a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

