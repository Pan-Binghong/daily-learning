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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANCMMTV%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5UZCvEsJ1TvM92vsyqvWg6XdVm%2FR2ah6j7v9peMDKJAIhANBNMI8zizVQe1geIGOi9%2FuRPYgt%2BMZHxeBQE4S0CcDxKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjGVAVxAUmaqD6e0Qq3AOqH%2FeJNceNdoKlkMz8MrVHBc4lkmYvtBxl%2F7Zlfu05Sj4TBISreNFuXmGShuQfOvlw9DBbPQAIuRegRNMPNKooq86nQrCqn5EZOTgZKWlr%2FQHRN%2FHn6QonZImHJg1soE6Zru7fotIN44JWbFoDgx4oy9m5pvNGflp%2BgoX%2B00a3QMEqX9ywfTcI6dqdPBfrl36fkOQfv3SOvR5MB0hlfgsre9ARWVxZhQ%2FAIUl7sd7B5VvA32NgM923q5GDBKSQxqdItKzLd72bz0rdUfy1SXUB0t2xDXIBuvz9AMXnYgutP9Fy1Ve1pF3fNRxtzjQx8Pt5fbPmVXf2hXPnBpjXVTgwVDjmDgCVADK3ibIMLRLZL%2BY7PGS2s7hpqz1O0dc3ISlb8oR%2FxG8vlSELZuhrj32LVgsApeuKYSFrECKoqKQnegKo4HBIqKOgPuSEZg2Kq7%2BRlOoOIg5YGAkKJY4BDBjralGnqCrVMAVPxQTxwCoNURQcx7BD%2BsDdZ8SfOjKLiHnjWeFeM0UpLoClbWedki%2FiqNzCEDNQqYTMVp12jt7NaeeV451k%2BD0VFkPqkFe2l71FiwZm8klKlIOAS7UKnfMQvrNEHMC82W4w1BdJs8ZI6XZmLTwyoG%2FLdTkIEjDI4OTIBjqkATAaSEGiB6GqaSsBdVwAfzMg88YdnWdnEMOBlRKiuBmBk1CLi4Ovt9JHooUVPSo1lnW8uIl4WZJRWJDFjSkXCLdwL%2BAcqPXnP4gifpRiQYnk2Af3%2F1Z28W%2F1M%2BQ1A1zAZHuBzjSnEfmp4jM1HWWl7n3YZDjXYuVrmGbPwHuSayzXfEYTr%2BKUkTGdTLQ0tscFB4xbet3u3LYJMyRLgCBzp8f0Ouqq&X-Amz-Signature=80798a72b013c17faa9c6580d19c7b6e2001469df885db2c0a47c158d9928c83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANCMMTV%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5UZCvEsJ1TvM92vsyqvWg6XdVm%2FR2ah6j7v9peMDKJAIhANBNMI8zizVQe1geIGOi9%2FuRPYgt%2BMZHxeBQE4S0CcDxKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjGVAVxAUmaqD6e0Qq3AOqH%2FeJNceNdoKlkMz8MrVHBc4lkmYvtBxl%2F7Zlfu05Sj4TBISreNFuXmGShuQfOvlw9DBbPQAIuRegRNMPNKooq86nQrCqn5EZOTgZKWlr%2FQHRN%2FHn6QonZImHJg1soE6Zru7fotIN44JWbFoDgx4oy9m5pvNGflp%2BgoX%2B00a3QMEqX9ywfTcI6dqdPBfrl36fkOQfv3SOvR5MB0hlfgsre9ARWVxZhQ%2FAIUl7sd7B5VvA32NgM923q5GDBKSQxqdItKzLd72bz0rdUfy1SXUB0t2xDXIBuvz9AMXnYgutP9Fy1Ve1pF3fNRxtzjQx8Pt5fbPmVXf2hXPnBpjXVTgwVDjmDgCVADK3ibIMLRLZL%2BY7PGS2s7hpqz1O0dc3ISlb8oR%2FxG8vlSELZuhrj32LVgsApeuKYSFrECKoqKQnegKo4HBIqKOgPuSEZg2Kq7%2BRlOoOIg5YGAkKJY4BDBjralGnqCrVMAVPxQTxwCoNURQcx7BD%2BsDdZ8SfOjKLiHnjWeFeM0UpLoClbWedki%2FiqNzCEDNQqYTMVp12jt7NaeeV451k%2BD0VFkPqkFe2l71FiwZm8klKlIOAS7UKnfMQvrNEHMC82W4w1BdJs8ZI6XZmLTwyoG%2FLdTkIEjDI4OTIBjqkATAaSEGiB6GqaSsBdVwAfzMg88YdnWdnEMOBlRKiuBmBk1CLi4Ovt9JHooUVPSo1lnW8uIl4WZJRWJDFjSkXCLdwL%2BAcqPXnP4gifpRiQYnk2Af3%2F1Z28W%2F1M%2BQ1A1zAZHuBzjSnEfmp4jM1HWWl7n3YZDjXYuVrmGbPwHuSayzXfEYTr%2BKUkTGdTLQ0tscFB4xbet3u3LYJMyRLgCBzp8f0Ouqq&X-Amz-Signature=c26ff966bc9144b7306caa0cfaef2ea63ce7119984f9878ec282f4de5d24a789&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANCMMTV%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5UZCvEsJ1TvM92vsyqvWg6XdVm%2FR2ah6j7v9peMDKJAIhANBNMI8zizVQe1geIGOi9%2FuRPYgt%2BMZHxeBQE4S0CcDxKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjGVAVxAUmaqD6e0Qq3AOqH%2FeJNceNdoKlkMz8MrVHBc4lkmYvtBxl%2F7Zlfu05Sj4TBISreNFuXmGShuQfOvlw9DBbPQAIuRegRNMPNKooq86nQrCqn5EZOTgZKWlr%2FQHRN%2FHn6QonZImHJg1soE6Zru7fotIN44JWbFoDgx4oy9m5pvNGflp%2BgoX%2B00a3QMEqX9ywfTcI6dqdPBfrl36fkOQfv3SOvR5MB0hlfgsre9ARWVxZhQ%2FAIUl7sd7B5VvA32NgM923q5GDBKSQxqdItKzLd72bz0rdUfy1SXUB0t2xDXIBuvz9AMXnYgutP9Fy1Ve1pF3fNRxtzjQx8Pt5fbPmVXf2hXPnBpjXVTgwVDjmDgCVADK3ibIMLRLZL%2BY7PGS2s7hpqz1O0dc3ISlb8oR%2FxG8vlSELZuhrj32LVgsApeuKYSFrECKoqKQnegKo4HBIqKOgPuSEZg2Kq7%2BRlOoOIg5YGAkKJY4BDBjralGnqCrVMAVPxQTxwCoNURQcx7BD%2BsDdZ8SfOjKLiHnjWeFeM0UpLoClbWedki%2FiqNzCEDNQqYTMVp12jt7NaeeV451k%2BD0VFkPqkFe2l71FiwZm8klKlIOAS7UKnfMQvrNEHMC82W4w1BdJs8ZI6XZmLTwyoG%2FLdTkIEjDI4OTIBjqkATAaSEGiB6GqaSsBdVwAfzMg88YdnWdnEMOBlRKiuBmBk1CLi4Ovt9JHooUVPSo1lnW8uIl4WZJRWJDFjSkXCLdwL%2BAcqPXnP4gifpRiQYnk2Af3%2F1Z28W%2F1M%2BQ1A1zAZHuBzjSnEfmp4jM1HWWl7n3YZDjXYuVrmGbPwHuSayzXfEYTr%2BKUkTGdTLQ0tscFB4xbet3u3LYJMyRLgCBzp8f0Ouqq&X-Amz-Signature=ce098e843d545c00999b0e813a942958e77dc28d966d2bc1575a8061f851f20b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

