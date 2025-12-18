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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWFBUEJQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc3oTsM6KiiTZasIo6qFSLawxQCKqztEoagsacr6UT4gIhAKnLRBwtoS3joraSPoy7C3Gw6vszsvvDa7t%2FOXRqm5LzKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFDk5ylfIO1KX3Racq3AM6MuDUjRSiGq6O7AuhdVXrLgPMnfpXE8F59NdqCLPsxoYmc%2FQDvSDrKnL%2FsPQCKJLfK%2FiG35eW3fMJwqZci3RkEeqojrVmN42fnOl%2BA3nL5eY91E1w2fpc0fU25JminzNW27hzXO%2FUjc4fyJunhPxoC89kv8XvlUy0Opy5rPqmUq6CwzV5rZjyO7%2BXjbanpjmxEMcwBKuOtLXCLjPB2M9UL%2FCI0hDYb2Td0mEzXEzONQRp7LjIGRFRuFZ4VPUcMEBD8YL4i%2BVxGVxp50DuSlfsKSEhSp%2FBmd%2Bz7Twp%2F5lqBl60V3deSk%2B%2Bb%2BDczmK6FyzRE%2F%2FDCnUAT4RRQAaS%2BSC5MgicXRfVHC5s5%2BiTdAFSivSB9zBwrzzPzeA8bsrkJUiSw1xj%2BfJvEfqBzpEnHwSlkke2ooZCzDwCAJ0FYnoCnU8pZwhpjUipBiB0S8eur4vpcGkZGhUClp%2FFWF3EFJr5UXCVn%2FZDR1EgOy%2BmsU3Yx4p1rH81jmuooOBpHA%2Bc2CDBW1B6ffyfbP2qEmZfFc%2F3HVNUjkBOduQoiFYSJ3CzmWScSiO%2BDTV0wfuETjOK0Z96ywb3VFGGqZ6%2Bb5q8coczxJ%2BKMiQW8Pg2Zc6392uhu8DMhS3MEFHMzV0rTzC1yo3KBjqkAdBT%2BLH21OvvJE3O%2B7EKkCLlJ5pQyXHYHVK1qYdzZ1XbrG7HXPIK3QQxYPi%2BxYRGq5lp%2B50tl91YrbOeIKh2E6eGwdwsoNiKWS5qsPJ%2B1NHseyL%2F2AR4qn1dz%2BKUYV1AUvi2twEq5uhV2LvNIu%2B59nz1MSLvgNu4NhkI4x9VJOjGOMIwMhbXosAzTMmu%2FTsfH2dal2x01qoPjikBrcM5qnDUgOsv&X-Amz-Signature=141cacaf9c6bebe3ba5fb1567708242df69add01756f1ac058b792d1a9421fbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWFBUEJQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc3oTsM6KiiTZasIo6qFSLawxQCKqztEoagsacr6UT4gIhAKnLRBwtoS3joraSPoy7C3Gw6vszsvvDa7t%2FOXRqm5LzKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFDk5ylfIO1KX3Racq3AM6MuDUjRSiGq6O7AuhdVXrLgPMnfpXE8F59NdqCLPsxoYmc%2FQDvSDrKnL%2FsPQCKJLfK%2FiG35eW3fMJwqZci3RkEeqojrVmN42fnOl%2BA3nL5eY91E1w2fpc0fU25JminzNW27hzXO%2FUjc4fyJunhPxoC89kv8XvlUy0Opy5rPqmUq6CwzV5rZjyO7%2BXjbanpjmxEMcwBKuOtLXCLjPB2M9UL%2FCI0hDYb2Td0mEzXEzONQRp7LjIGRFRuFZ4VPUcMEBD8YL4i%2BVxGVxp50DuSlfsKSEhSp%2FBmd%2Bz7Twp%2F5lqBl60V3deSk%2B%2Bb%2BDczmK6FyzRE%2F%2FDCnUAT4RRQAaS%2BSC5MgicXRfVHC5s5%2BiTdAFSivSB9zBwrzzPzeA8bsrkJUiSw1xj%2BfJvEfqBzpEnHwSlkke2ooZCzDwCAJ0FYnoCnU8pZwhpjUipBiB0S8eur4vpcGkZGhUClp%2FFWF3EFJr5UXCVn%2FZDR1EgOy%2BmsU3Yx4p1rH81jmuooOBpHA%2Bc2CDBW1B6ffyfbP2qEmZfFc%2F3HVNUjkBOduQoiFYSJ3CzmWScSiO%2BDTV0wfuETjOK0Z96ywb3VFGGqZ6%2Bb5q8coczxJ%2BKMiQW8Pg2Zc6392uhu8DMhS3MEFHMzV0rTzC1yo3KBjqkAdBT%2BLH21OvvJE3O%2B7EKkCLlJ5pQyXHYHVK1qYdzZ1XbrG7HXPIK3QQxYPi%2BxYRGq5lp%2B50tl91YrbOeIKh2E6eGwdwsoNiKWS5qsPJ%2B1NHseyL%2F2AR4qn1dz%2BKUYV1AUvi2twEq5uhV2LvNIu%2B59nz1MSLvgNu4NhkI4x9VJOjGOMIwMhbXosAzTMmu%2FTsfH2dal2x01qoPjikBrcM5qnDUgOsv&X-Amz-Signature=ea3a601ccbdec41ef7262e9c2f71cf0b6d5792c1c0ec0a80022c94756fe44e6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWFBUEJQ%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc3oTsM6KiiTZasIo6qFSLawxQCKqztEoagsacr6UT4gIhAKnLRBwtoS3joraSPoy7C3Gw6vszsvvDa7t%2FOXRqm5LzKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFDk5ylfIO1KX3Racq3AM6MuDUjRSiGq6O7AuhdVXrLgPMnfpXE8F59NdqCLPsxoYmc%2FQDvSDrKnL%2FsPQCKJLfK%2FiG35eW3fMJwqZci3RkEeqojrVmN42fnOl%2BA3nL5eY91E1w2fpc0fU25JminzNW27hzXO%2FUjc4fyJunhPxoC89kv8XvlUy0Opy5rPqmUq6CwzV5rZjyO7%2BXjbanpjmxEMcwBKuOtLXCLjPB2M9UL%2FCI0hDYb2Td0mEzXEzONQRp7LjIGRFRuFZ4VPUcMEBD8YL4i%2BVxGVxp50DuSlfsKSEhSp%2FBmd%2Bz7Twp%2F5lqBl60V3deSk%2B%2Bb%2BDczmK6FyzRE%2F%2FDCnUAT4RRQAaS%2BSC5MgicXRfVHC5s5%2BiTdAFSivSB9zBwrzzPzeA8bsrkJUiSw1xj%2BfJvEfqBzpEnHwSlkke2ooZCzDwCAJ0FYnoCnU8pZwhpjUipBiB0S8eur4vpcGkZGhUClp%2FFWF3EFJr5UXCVn%2FZDR1EgOy%2BmsU3Yx4p1rH81jmuooOBpHA%2Bc2CDBW1B6ffyfbP2qEmZfFc%2F3HVNUjkBOduQoiFYSJ3CzmWScSiO%2BDTV0wfuETjOK0Z96ywb3VFGGqZ6%2Bb5q8coczxJ%2BKMiQW8Pg2Zc6392uhu8DMhS3MEFHMzV0rTzC1yo3KBjqkAdBT%2BLH21OvvJE3O%2B7EKkCLlJ5pQyXHYHVK1qYdzZ1XbrG7HXPIK3QQxYPi%2BxYRGq5lp%2B50tl91YrbOeIKh2E6eGwdwsoNiKWS5qsPJ%2B1NHseyL%2F2AR4qn1dz%2BKUYV1AUvi2twEq5uhV2LvNIu%2B59nz1MSLvgNu4NhkI4x9VJOjGOMIwMhbXosAzTMmu%2FTsfH2dal2x01qoPjikBrcM5qnDUgOsv&X-Amz-Signature=86274115d8bff6b831a0a1315959a39c3c817f85340575faff35c07446955c62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

