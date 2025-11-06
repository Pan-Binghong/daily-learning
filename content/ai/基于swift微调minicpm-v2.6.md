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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF522R7V%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjpG5ZX07bPlSEc%2F3uYa2ctsHIdhwPSMR44Qw9VFCtwAiEAuVakE1kLfqt4naV3f1hMMbO%2FQa0vg3eXz4wPMhLH1VoqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsiIf6mdCq9DJCjOircA%2Bvls2YECNXV9ncd%2FQann2%2FatpHO37YsemxVeT2%2FnwK5BnBx2dLKxT6FOhwfthOLLLOcloXKDkQhjHwaD6cBr2%2BlB9q2BDRdYGo3lbwIu9sxJZX%2Ff0UvOxWIn4%2FHiEWJpyk5CdysTazVMO6UYTWFULDvwv8BgvskHWhm610AAX1ytL917NbHLrmT1LAquqTrPm4Gx%2BZrpqFTPo6Yp9o52NJuzar%2FlNpryx7ll8HK41Q2q0YrnrAiJxrUaXo1oNSMePURlLl9Hhotmyo9JLXgpqlzcwZvWPqyW6G0mbqgA%2FL7KoZ2Y7kUlHl8ft%2FyJn02WECNrL5urLd%2BJGRaneChoT3DT5pli5bye7%2FH2NBn2ANP42s0pTwXXY2Kk2c34Ho3%2FwtixpTqVyWpITPDFEXf8%2BqoXxbkMh4DMYfCjCsPGPBRDB5w4JJmig9mFuKt1XZD4fitKmGwjByWioYcgh47crNAFnlU6YQfxBAe4dVaQvsc3EUeLx0c9lXF%2B5rRCoDmBqm2dIRQD8gp%2FcIA5PsdWXQKjc5XJXsF328Pby1cYzxGX6EC5RwEzTX8b9HVLBpsJq9njlLzDpC%2B7DBVkKZujls68nL8hoQX5GDTi5NiRDZ0%2BMdARhWSHkZ8PkrxMPDxr8gGOqUBBT9ANNat%2FCtFeHpHzuiqDHWg6r4LlbeBA1iyN9xQbYPjLu9W6if2UiWCT9dnAPOYsKW5Is9B%2FQXAcUYDAwBt76jU%2BCzuu9PLuaAt%2F7F%2B7%2BPwxh%2Fl9p0fXkSB4oMRtUmpx38%2Bpb7VAo5SJTSQIJmGZ%2FhdZo%2BS4Mg0luAoUO1EgeUVQf92CNuuw2vP%2Fhv9f0MLbajW66IESB4PN5qXFCrX7Vpb63Lq&X-Amz-Signature=bbe69a363e9b37f8e7b78e0a9d692be6ab9100887e12ae01692030736c0b570e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF522R7V%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjpG5ZX07bPlSEc%2F3uYa2ctsHIdhwPSMR44Qw9VFCtwAiEAuVakE1kLfqt4naV3f1hMMbO%2FQa0vg3eXz4wPMhLH1VoqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsiIf6mdCq9DJCjOircA%2Bvls2YECNXV9ncd%2FQann2%2FatpHO37YsemxVeT2%2FnwK5BnBx2dLKxT6FOhwfthOLLLOcloXKDkQhjHwaD6cBr2%2BlB9q2BDRdYGo3lbwIu9sxJZX%2Ff0UvOxWIn4%2FHiEWJpyk5CdysTazVMO6UYTWFULDvwv8BgvskHWhm610AAX1ytL917NbHLrmT1LAquqTrPm4Gx%2BZrpqFTPo6Yp9o52NJuzar%2FlNpryx7ll8HK41Q2q0YrnrAiJxrUaXo1oNSMePURlLl9Hhotmyo9JLXgpqlzcwZvWPqyW6G0mbqgA%2FL7KoZ2Y7kUlHl8ft%2FyJn02WECNrL5urLd%2BJGRaneChoT3DT5pli5bye7%2FH2NBn2ANP42s0pTwXXY2Kk2c34Ho3%2FwtixpTqVyWpITPDFEXf8%2BqoXxbkMh4DMYfCjCsPGPBRDB5w4JJmig9mFuKt1XZD4fitKmGwjByWioYcgh47crNAFnlU6YQfxBAe4dVaQvsc3EUeLx0c9lXF%2B5rRCoDmBqm2dIRQD8gp%2FcIA5PsdWXQKjc5XJXsF328Pby1cYzxGX6EC5RwEzTX8b9HVLBpsJq9njlLzDpC%2B7DBVkKZujls68nL8hoQX5GDTi5NiRDZ0%2BMdARhWSHkZ8PkrxMPDxr8gGOqUBBT9ANNat%2FCtFeHpHzuiqDHWg6r4LlbeBA1iyN9xQbYPjLu9W6if2UiWCT9dnAPOYsKW5Is9B%2FQXAcUYDAwBt76jU%2BCzuu9PLuaAt%2F7F%2B7%2BPwxh%2Fl9p0fXkSB4oMRtUmpx38%2Bpb7VAo5SJTSQIJmGZ%2FhdZo%2BS4Mg0luAoUO1EgeUVQf92CNuuw2vP%2Fhv9f0MLbajW66IESB4PN5qXFCrX7Vpb63Lq&X-Amz-Signature=3df711a2cfe38a7cdacd50944460390a73c3ccd07a7cd1a87271e8e3d6d306e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF522R7V%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjpG5ZX07bPlSEc%2F3uYa2ctsHIdhwPSMR44Qw9VFCtwAiEAuVakE1kLfqt4naV3f1hMMbO%2FQa0vg3eXz4wPMhLH1VoqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsiIf6mdCq9DJCjOircA%2Bvls2YECNXV9ncd%2FQann2%2FatpHO37YsemxVeT2%2FnwK5BnBx2dLKxT6FOhwfthOLLLOcloXKDkQhjHwaD6cBr2%2BlB9q2BDRdYGo3lbwIu9sxJZX%2Ff0UvOxWIn4%2FHiEWJpyk5CdysTazVMO6UYTWFULDvwv8BgvskHWhm610AAX1ytL917NbHLrmT1LAquqTrPm4Gx%2BZrpqFTPo6Yp9o52NJuzar%2FlNpryx7ll8HK41Q2q0YrnrAiJxrUaXo1oNSMePURlLl9Hhotmyo9JLXgpqlzcwZvWPqyW6G0mbqgA%2FL7KoZ2Y7kUlHl8ft%2FyJn02WECNrL5urLd%2BJGRaneChoT3DT5pli5bye7%2FH2NBn2ANP42s0pTwXXY2Kk2c34Ho3%2FwtixpTqVyWpITPDFEXf8%2BqoXxbkMh4DMYfCjCsPGPBRDB5w4JJmig9mFuKt1XZD4fitKmGwjByWioYcgh47crNAFnlU6YQfxBAe4dVaQvsc3EUeLx0c9lXF%2B5rRCoDmBqm2dIRQD8gp%2FcIA5PsdWXQKjc5XJXsF328Pby1cYzxGX6EC5RwEzTX8b9HVLBpsJq9njlLzDpC%2B7DBVkKZujls68nL8hoQX5GDTi5NiRDZ0%2BMdARhWSHkZ8PkrxMPDxr8gGOqUBBT9ANNat%2FCtFeHpHzuiqDHWg6r4LlbeBA1iyN9xQbYPjLu9W6if2UiWCT9dnAPOYsKW5Is9B%2FQXAcUYDAwBt76jU%2BCzuu9PLuaAt%2F7F%2B7%2BPwxh%2Fl9p0fXkSB4oMRtUmpx38%2Bpb7VAo5SJTSQIJmGZ%2FhdZo%2BS4Mg0luAoUO1EgeUVQf92CNuuw2vP%2Fhv9f0MLbajW66IESB4PN5qXFCrX7Vpb63Lq&X-Amz-Signature=f9693b86eded701f679c10f56decc1cf779a021ea6a57dd97e9b7dfa01e7a9ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

