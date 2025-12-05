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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOSYTOS7%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7noXqsxADHsJN1o%2BX2zP4gUPbLTX57QxC2anVlzngrwIhAJJzSRTtLZID2qmUubyq3bMs56xeLcGCUKT4fyOyigT3Kv8DCE8QABoMNjM3NDIzMTgzODA1Igzp0A%2BCBVgQQMt%2BGJsq3AOsRReTliZnTwK3rQIVWSr%2FQDBg%2B36VVhJNoqunU6Zeqoy29Lbi3SyAXvncohmPdjvH93YyjmKnM7svyQkQacUakYNdhqn8v7UgMTb%2Fqc73o8AW8Mor3qsPrNs1lcTsNqoGBCr%2FToH8l5Y60g8dsYY1Ekkn02kEdPQTJg6HXy%2FCF4PiA4%2FPs6iZ3luozBRicNsHwPxXOGQqExuyE9Cy%2BRbwY2eJEKLnpKsCW0k8BVlsvoHLgtlc8o74UObYmu8Khr3DVGzd7OtjWuKWSLRWeaWh0DPF0i7MZqsRRdZKH4zb9A%2FfICmcgnCUDoW3J8iS81YRZ4w9ttvGDi07g0duZBRt9ukPdImGkgalpzhpdStx8ePgiwDeEOH%2FDfIgqSUQqrJzCPEIC1j2vflUdCDLOOlBFEu6bnXoQU%2BJcicqev1LFLIkXQdA70Eb4JPd8Bhhoofn99%2FpJj0UKGP0juWfIQAMtnWuB57%2BU6lSnLJaOXxxuvAESHROt5WUajb7TMw8HipYu3Y%2BpaPhzLwZVkvJ04uJoTj7crwS%2FGXGljxMLT3IsA61OqfGHpM8wDXxetGcvz4Qwq1XYRkNGYwx1wV0T7NHn15JtpdyBp3GjnvygNoPmg%2Fhw3WnfMCRguYJvjCzjMjJBjqkAY%2BdM2fCU%2F1Af7dRQ3SKO3lmpSnE370ll2NfM5bVgbom31VnaL5S2v%2ByAOhxxD19bcusJoYnS2Q3OjI24thYHj8tzTUmHkjjfmruwMtfUHEiLZG%2FWUc4cJzbviOqwUcsEQx3%2BW9Z8QIqpplt6%2FAPAP7dhClu4HqKPAt5MLPODZ7ncNqiW3UvddR0H4rBjb7ZSJrNGFmfBw9MbNanH3nmvlL01vy2&X-Amz-Signature=727b94bce01f09d5a7e13c731155ef718cfa517a4d108a80b10911347b3e4b5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOSYTOS7%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7noXqsxADHsJN1o%2BX2zP4gUPbLTX57QxC2anVlzngrwIhAJJzSRTtLZID2qmUubyq3bMs56xeLcGCUKT4fyOyigT3Kv8DCE8QABoMNjM3NDIzMTgzODA1Igzp0A%2BCBVgQQMt%2BGJsq3AOsRReTliZnTwK3rQIVWSr%2FQDBg%2B36VVhJNoqunU6Zeqoy29Lbi3SyAXvncohmPdjvH93YyjmKnM7svyQkQacUakYNdhqn8v7UgMTb%2Fqc73o8AW8Mor3qsPrNs1lcTsNqoGBCr%2FToH8l5Y60g8dsYY1Ekkn02kEdPQTJg6HXy%2FCF4PiA4%2FPs6iZ3luozBRicNsHwPxXOGQqExuyE9Cy%2BRbwY2eJEKLnpKsCW0k8BVlsvoHLgtlc8o74UObYmu8Khr3DVGzd7OtjWuKWSLRWeaWh0DPF0i7MZqsRRdZKH4zb9A%2FfICmcgnCUDoW3J8iS81YRZ4w9ttvGDi07g0duZBRt9ukPdImGkgalpzhpdStx8ePgiwDeEOH%2FDfIgqSUQqrJzCPEIC1j2vflUdCDLOOlBFEu6bnXoQU%2BJcicqev1LFLIkXQdA70Eb4JPd8Bhhoofn99%2FpJj0UKGP0juWfIQAMtnWuB57%2BU6lSnLJaOXxxuvAESHROt5WUajb7TMw8HipYu3Y%2BpaPhzLwZVkvJ04uJoTj7crwS%2FGXGljxMLT3IsA61OqfGHpM8wDXxetGcvz4Qwq1XYRkNGYwx1wV0T7NHn15JtpdyBp3GjnvygNoPmg%2Fhw3WnfMCRguYJvjCzjMjJBjqkAY%2BdM2fCU%2F1Af7dRQ3SKO3lmpSnE370ll2NfM5bVgbom31VnaL5S2v%2ByAOhxxD19bcusJoYnS2Q3OjI24thYHj8tzTUmHkjjfmruwMtfUHEiLZG%2FWUc4cJzbviOqwUcsEQx3%2BW9Z8QIqpplt6%2FAPAP7dhClu4HqKPAt5MLPODZ7ncNqiW3UvddR0H4rBjb7ZSJrNGFmfBw9MbNanH3nmvlL01vy2&X-Amz-Signature=2e670ca493c9aaf7bb25cafa04058cc4c82b5c993af85be2575cafcc7fecf5cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOSYTOS7%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7noXqsxADHsJN1o%2BX2zP4gUPbLTX57QxC2anVlzngrwIhAJJzSRTtLZID2qmUubyq3bMs56xeLcGCUKT4fyOyigT3Kv8DCE8QABoMNjM3NDIzMTgzODA1Igzp0A%2BCBVgQQMt%2BGJsq3AOsRReTliZnTwK3rQIVWSr%2FQDBg%2B36VVhJNoqunU6Zeqoy29Lbi3SyAXvncohmPdjvH93YyjmKnM7svyQkQacUakYNdhqn8v7UgMTb%2Fqc73o8AW8Mor3qsPrNs1lcTsNqoGBCr%2FToH8l5Y60g8dsYY1Ekkn02kEdPQTJg6HXy%2FCF4PiA4%2FPs6iZ3luozBRicNsHwPxXOGQqExuyE9Cy%2BRbwY2eJEKLnpKsCW0k8BVlsvoHLgtlc8o74UObYmu8Khr3DVGzd7OtjWuKWSLRWeaWh0DPF0i7MZqsRRdZKH4zb9A%2FfICmcgnCUDoW3J8iS81YRZ4w9ttvGDi07g0duZBRt9ukPdImGkgalpzhpdStx8ePgiwDeEOH%2FDfIgqSUQqrJzCPEIC1j2vflUdCDLOOlBFEu6bnXoQU%2BJcicqev1LFLIkXQdA70Eb4JPd8Bhhoofn99%2FpJj0UKGP0juWfIQAMtnWuB57%2BU6lSnLJaOXxxuvAESHROt5WUajb7TMw8HipYu3Y%2BpaPhzLwZVkvJ04uJoTj7crwS%2FGXGljxMLT3IsA61OqfGHpM8wDXxetGcvz4Qwq1XYRkNGYwx1wV0T7NHn15JtpdyBp3GjnvygNoPmg%2Fhw3WnfMCRguYJvjCzjMjJBjqkAY%2BdM2fCU%2F1Af7dRQ3SKO3lmpSnE370ll2NfM5bVgbom31VnaL5S2v%2ByAOhxxD19bcusJoYnS2Q3OjI24thYHj8tzTUmHkjjfmruwMtfUHEiLZG%2FWUc4cJzbviOqwUcsEQx3%2BW9Z8QIqpplt6%2FAPAP7dhClu4HqKPAt5MLPODZ7ncNqiW3UvddR0H4rBjb7ZSJrNGFmfBw9MbNanH3nmvlL01vy2&X-Amz-Signature=e086b441b3ead9a57b9a2250e59b57a391addb564e381c9daf944f60a2662cec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

