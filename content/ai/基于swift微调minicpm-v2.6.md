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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBBANXLV%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6pt4aI%2FfxQISxEY1fZNWERmO935ksrp1QcQEn4yscFgIgUZRlvTkr9a3qIWprplHm4M1OHwEB0wrub9KvVkq4EYkq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDCkqoM04bX7QmPkK1ircA2qcl5%2FR3kL4ZoFdh6AOby9b1AjzGbdkgr5PT2c8Ct3G2rYRQujnCIwy8ellJ7CY9a1yiSn6bVcLRDTxg05p2lE1x%2F51ReIuQIY0CziL5pG%2FtkHkcjjh51Sog597AskyCMVkv%2B6j0HG%2FFVwO4fyNw5%2B5dybUm1mFagJ7EIob6w5rwmYUQrRaNHDKtvegz04KgkfeSce%2BSWQ%2FUnRiGErD5NMU1F3mucbAfDqvgijajCe24C3wcB%2BAIaLWDtgUMgtXNxJFoCzOPXh%2FLa63UFVFgWsqz%2FvsOafyNf%2FOZgHaJAkL5L8G1nCCe7ocK82bZKNfHkMVpgLf57CTUzCjJwZargE3uLTWgpe%2FkIJ5PDcl%2FoVxViAkK3I%2BlIRymJrTp1KJvNFQ8DF0rZvY9Us3%2FfxBXbv2hAGsvjCgQzp1fRf8MAb3s8ecP3usbx%2FCYewDwzR8gOcKI6bhM7OEWuL047VVh8Z9%2BPVSfsiEhm4KMlh6adXryBFJu7HMgrdWbQdhRZ0RwkIKetTvI6qivYN8sUvtNETJUErzc%2F9Z8jQsYphxDg10Wc6w%2BXEORql50YRh%2FT95sGqJSW8pW8yn9c2Lz%2FcAQ0i4QGpkQBgh35kyF%2Bxo2tuTjUQeOvCM8MXPJwr8MIGNoMwGOqUBZ10nMltCNWuZDghC6w20u%2FNWnHY9J031IO9d6XbFsqznQAvPZxPIWwPh1TElY7qjJw221pAMOqq%2FcM1XuJOiGyPy0%2B6GGLQnJkZVUgW0OpbkJWPkjdMdxxGrIa421Pdx6ZClp7dfrTjULrgSU2aQfbSUp9pVpwFwdDJ%2BtbdFQMFHIay7fDvWPIaX3xQSqLRSiVIGosov0Y7py1zyMSFFIhddge%2Ft&X-Amz-Signature=b84ff0b1451a59b50f74f9a68b7ffe1ded18222320f9c659b616c3748e17f019&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBBANXLV%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6pt4aI%2FfxQISxEY1fZNWERmO935ksrp1QcQEn4yscFgIgUZRlvTkr9a3qIWprplHm4M1OHwEB0wrub9KvVkq4EYkq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDCkqoM04bX7QmPkK1ircA2qcl5%2FR3kL4ZoFdh6AOby9b1AjzGbdkgr5PT2c8Ct3G2rYRQujnCIwy8ellJ7CY9a1yiSn6bVcLRDTxg05p2lE1x%2F51ReIuQIY0CziL5pG%2FtkHkcjjh51Sog597AskyCMVkv%2B6j0HG%2FFVwO4fyNw5%2B5dybUm1mFagJ7EIob6w5rwmYUQrRaNHDKtvegz04KgkfeSce%2BSWQ%2FUnRiGErD5NMU1F3mucbAfDqvgijajCe24C3wcB%2BAIaLWDtgUMgtXNxJFoCzOPXh%2FLa63UFVFgWsqz%2FvsOafyNf%2FOZgHaJAkL5L8G1nCCe7ocK82bZKNfHkMVpgLf57CTUzCjJwZargE3uLTWgpe%2FkIJ5PDcl%2FoVxViAkK3I%2BlIRymJrTp1KJvNFQ8DF0rZvY9Us3%2FfxBXbv2hAGsvjCgQzp1fRf8MAb3s8ecP3usbx%2FCYewDwzR8gOcKI6bhM7OEWuL047VVh8Z9%2BPVSfsiEhm4KMlh6adXryBFJu7HMgrdWbQdhRZ0RwkIKetTvI6qivYN8sUvtNETJUErzc%2F9Z8jQsYphxDg10Wc6w%2BXEORql50YRh%2FT95sGqJSW8pW8yn9c2Lz%2FcAQ0i4QGpkQBgh35kyF%2Bxo2tuTjUQeOvCM8MXPJwr8MIGNoMwGOqUBZ10nMltCNWuZDghC6w20u%2FNWnHY9J031IO9d6XbFsqznQAvPZxPIWwPh1TElY7qjJw221pAMOqq%2FcM1XuJOiGyPy0%2B6GGLQnJkZVUgW0OpbkJWPkjdMdxxGrIa421Pdx6ZClp7dfrTjULrgSU2aQfbSUp9pVpwFwdDJ%2BtbdFQMFHIay7fDvWPIaX3xQSqLRSiVIGosov0Y7py1zyMSFFIhddge%2Ft&X-Amz-Signature=3e666416132dcb42efe482692312968e7849ec838c56942894bebb12d38bfbbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBBANXLV%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6pt4aI%2FfxQISxEY1fZNWERmO935ksrp1QcQEn4yscFgIgUZRlvTkr9a3qIWprplHm4M1OHwEB0wrub9KvVkq4EYkq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDCkqoM04bX7QmPkK1ircA2qcl5%2FR3kL4ZoFdh6AOby9b1AjzGbdkgr5PT2c8Ct3G2rYRQujnCIwy8ellJ7CY9a1yiSn6bVcLRDTxg05p2lE1x%2F51ReIuQIY0CziL5pG%2FtkHkcjjh51Sog597AskyCMVkv%2B6j0HG%2FFVwO4fyNw5%2B5dybUm1mFagJ7EIob6w5rwmYUQrRaNHDKtvegz04KgkfeSce%2BSWQ%2FUnRiGErD5NMU1F3mucbAfDqvgijajCe24C3wcB%2BAIaLWDtgUMgtXNxJFoCzOPXh%2FLa63UFVFgWsqz%2FvsOafyNf%2FOZgHaJAkL5L8G1nCCe7ocK82bZKNfHkMVpgLf57CTUzCjJwZargE3uLTWgpe%2FkIJ5PDcl%2FoVxViAkK3I%2BlIRymJrTp1KJvNFQ8DF0rZvY9Us3%2FfxBXbv2hAGsvjCgQzp1fRf8MAb3s8ecP3usbx%2FCYewDwzR8gOcKI6bhM7OEWuL047VVh8Z9%2BPVSfsiEhm4KMlh6adXryBFJu7HMgrdWbQdhRZ0RwkIKetTvI6qivYN8sUvtNETJUErzc%2F9Z8jQsYphxDg10Wc6w%2BXEORql50YRh%2FT95sGqJSW8pW8yn9c2Lz%2FcAQ0i4QGpkQBgh35kyF%2Bxo2tuTjUQeOvCM8MXPJwr8MIGNoMwGOqUBZ10nMltCNWuZDghC6w20u%2FNWnHY9J031IO9d6XbFsqznQAvPZxPIWwPh1TElY7qjJw221pAMOqq%2FcM1XuJOiGyPy0%2B6GGLQnJkZVUgW0OpbkJWPkjdMdxxGrIa421Pdx6ZClp7dfrTjULrgSU2aQfbSUp9pVpwFwdDJ%2BtbdFQMFHIay7fDvWPIaX3xQSqLRSiVIGosov0Y7py1zyMSFFIhddge%2Ft&X-Amz-Signature=efc9bf980ee328d881c261166521ca8f942e59c8fb87f6ac87d13f1ce1fdc431&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

