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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MSRT4ID%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHRC%2BZ0R0pnOoipuxt68JCJp7cJEsIMH6pJs7rBGFOEgIhAJoJmYqk%2BAp3YNrZ86tk4W8O15QivKLJ7KRYgRUxQ8TSKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNeB6uU05715hVjpIq3AMUouyDE6zw2X98OZ8egho5Dpzb6KWoflxWYSzIZ931wBEkvB3inmPFX2V9%2BygyG1LDzXqcwDJCYVz3mD1RhrBjifCBgpEWybmCaMgK54dv5CrBHXhXzwbDPseZsGJ%2BrFkiGr9zBKjVqh1KoJa%2BpwauUr%2FNjW%2BEG%2BwKXrqUQr%2Fi8neF4uDADo31MJS%2B9RzSq%2B2lWgCVOmTP9V7kZQqaNzf5wYS9otcTMLDHiwCZ2gO72SCG69%2F2ESN2NPFCna%2BgMELJTPiavvtQC%2FX5rF%2FRj226G6vP2QhvWdiX0f0Gn2AhxG5G4uE49%2B%2FJgG4CpPNdiWBD%2FCM2NX8dx%2BAvLQ25Ro4UBu1z8u%2FR8b0t9osP6ZFlEeO%2B15I818YFAG557BlqGDO%2Bb%2F8PU0kARONqA6klH7tY3v7a7xqqURzoXmtkBIH0GdKf4%2FRKECMK4%2Btgz%2B4W49EyHpoCvmaaa%2BQbtkqzow%2F834J%2BIbrIE4DCIzOte95cmQJkviVQLbWfSwbG%2FBqmjn494wYJKyp%2BN%2BdXFjpblVe6iZ5kVLUgrqbzK%2BiQGWtW8zbVjVYKcLwiCPyCj3RsDJWlCmmJaQnHPs7ATQjfMCJaIWpo2y9QhX463jKcA2iNPmI2hJ8C5vy6d1A0UzCwjt7JBjqkAQoUNCb5Z9ePnuLZDrQT1fLnfJduYJvelRX1goxHL6w6McRbQMFvlNtsGrDpeObAFyaZi092KSiXtThsdhgyPsGV3S38%2F5AnReZigvyydR%2BGurRpPQ933huWlZwZLcWFwjEQaYB%2FoTtpVdXcEEUrWq4mFnqb4Rvimwl9nCib6Vtg6vgsGpVoqAXVsS%2FvVmCMh%2F1UdCoStAtGx5QUCA5M1fSnCjVf&X-Amz-Signature=6b3eac7527df377242de9ba465e283b846f76f9e81d80230ea09869f6a31ba3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MSRT4ID%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHRC%2BZ0R0pnOoipuxt68JCJp7cJEsIMH6pJs7rBGFOEgIhAJoJmYqk%2BAp3YNrZ86tk4W8O15QivKLJ7KRYgRUxQ8TSKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNeB6uU05715hVjpIq3AMUouyDE6zw2X98OZ8egho5Dpzb6KWoflxWYSzIZ931wBEkvB3inmPFX2V9%2BygyG1LDzXqcwDJCYVz3mD1RhrBjifCBgpEWybmCaMgK54dv5CrBHXhXzwbDPseZsGJ%2BrFkiGr9zBKjVqh1KoJa%2BpwauUr%2FNjW%2BEG%2BwKXrqUQr%2Fi8neF4uDADo31MJS%2B9RzSq%2B2lWgCVOmTP9V7kZQqaNzf5wYS9otcTMLDHiwCZ2gO72SCG69%2F2ESN2NPFCna%2BgMELJTPiavvtQC%2FX5rF%2FRj226G6vP2QhvWdiX0f0Gn2AhxG5G4uE49%2B%2FJgG4CpPNdiWBD%2FCM2NX8dx%2BAvLQ25Ro4UBu1z8u%2FR8b0t9osP6ZFlEeO%2B15I818YFAG557BlqGDO%2Bb%2F8PU0kARONqA6klH7tY3v7a7xqqURzoXmtkBIH0GdKf4%2FRKECMK4%2Btgz%2B4W49EyHpoCvmaaa%2BQbtkqzow%2F834J%2BIbrIE4DCIzOte95cmQJkviVQLbWfSwbG%2FBqmjn494wYJKyp%2BN%2BdXFjpblVe6iZ5kVLUgrqbzK%2BiQGWtW8zbVjVYKcLwiCPyCj3RsDJWlCmmJaQnHPs7ATQjfMCJaIWpo2y9QhX463jKcA2iNPmI2hJ8C5vy6d1A0UzCwjt7JBjqkAQoUNCb5Z9ePnuLZDrQT1fLnfJduYJvelRX1goxHL6w6McRbQMFvlNtsGrDpeObAFyaZi092KSiXtThsdhgyPsGV3S38%2F5AnReZigvyydR%2BGurRpPQ933huWlZwZLcWFwjEQaYB%2FoTtpVdXcEEUrWq4mFnqb4Rvimwl9nCib6Vtg6vgsGpVoqAXVsS%2FvVmCMh%2F1UdCoStAtGx5QUCA5M1fSnCjVf&X-Amz-Signature=3b27df208898130f01aaabf0dc53e6a75e35989a12aeeed85f4cf3a29eb37544&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MSRT4ID%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHRC%2BZ0R0pnOoipuxt68JCJp7cJEsIMH6pJs7rBGFOEgIhAJoJmYqk%2BAp3YNrZ86tk4W8O15QivKLJ7KRYgRUxQ8TSKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNeB6uU05715hVjpIq3AMUouyDE6zw2X98OZ8egho5Dpzb6KWoflxWYSzIZ931wBEkvB3inmPFX2V9%2BygyG1LDzXqcwDJCYVz3mD1RhrBjifCBgpEWybmCaMgK54dv5CrBHXhXzwbDPseZsGJ%2BrFkiGr9zBKjVqh1KoJa%2BpwauUr%2FNjW%2BEG%2BwKXrqUQr%2Fi8neF4uDADo31MJS%2B9RzSq%2B2lWgCVOmTP9V7kZQqaNzf5wYS9otcTMLDHiwCZ2gO72SCG69%2F2ESN2NPFCna%2BgMELJTPiavvtQC%2FX5rF%2FRj226G6vP2QhvWdiX0f0Gn2AhxG5G4uE49%2B%2FJgG4CpPNdiWBD%2FCM2NX8dx%2BAvLQ25Ro4UBu1z8u%2FR8b0t9osP6ZFlEeO%2B15I818YFAG557BlqGDO%2Bb%2F8PU0kARONqA6klH7tY3v7a7xqqURzoXmtkBIH0GdKf4%2FRKECMK4%2Btgz%2B4W49EyHpoCvmaaa%2BQbtkqzow%2F834J%2BIbrIE4DCIzOte95cmQJkviVQLbWfSwbG%2FBqmjn494wYJKyp%2BN%2BdXFjpblVe6iZ5kVLUgrqbzK%2BiQGWtW8zbVjVYKcLwiCPyCj3RsDJWlCmmJaQnHPs7ATQjfMCJaIWpo2y9QhX463jKcA2iNPmI2hJ8C5vy6d1A0UzCwjt7JBjqkAQoUNCb5Z9ePnuLZDrQT1fLnfJduYJvelRX1goxHL6w6McRbQMFvlNtsGrDpeObAFyaZi092KSiXtThsdhgyPsGV3S38%2F5AnReZigvyydR%2BGurRpPQ933huWlZwZLcWFwjEQaYB%2FoTtpVdXcEEUrWq4mFnqb4Rvimwl9nCib6Vtg6vgsGpVoqAXVsS%2FvVmCMh%2F1UdCoStAtGx5QUCA5M1fSnCjVf&X-Amz-Signature=ca1ad2a28b4d1464f24bcfb42b21405944e546a7ad704f11f6ef3b80202f7f40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

