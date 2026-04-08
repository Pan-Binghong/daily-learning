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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6WREAR6%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIGlHZywOUrrgfPqO8zp6RtaQ8R%2Bp4t34LsDmM7lgktpxAiEA2wUA7nEmMEa2rywZ6oUkwwgD6vugG4Uzu0COEVAULMwqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKNLrHzw2EVZhl5SCrcA71cAD5jYUvqPMoWhXlMzVihe37m7EGDvk9TlEkd4RJtRvztZYdpxPHWXThoKiPke53t5%2BqSTQLafH2zoFNIUvVKychGR6C7t44m2uQUX1Xiqw5%2FwjfqW5lTJfg3NHtviwvP%2FQNt9X4Eiasyoy4%2FEZLr5j8gZn42lmNr%2FXXRHTyIFRbQ3JZrvRqT5YFCSrLXmhDzWrQfC0iWe7FNRTWZBax6AHiIw%2F7VdYdYhF%2BLON4FPak4wbcwg%2BYpmJdVDxdEzzy4Er5pCo%2Bbd5O%2FHBW%2BvVnt3AwfxVfmYNrtnc3XobyjXlAo2WSsi%2FHpow1gbBdaSzi%2BZ6K7zguEzRZuQloYBbd7ZE%2FYfnIIYgvJXCB9lgCJ%2B0KhaMEyHQt3eZMFjGTe96a2%2F6U9eTqN5WSQN7%2FjBdcG%2BRRbEQ4Vrxhcm5JtkKeh%2FiSmrgh63z%2FaRIT7Ijv5ZVTbYaGTnpR7PD1MOGanoaDo1Ot6VhlHaIli%2FgBtnizQCNbgHkMo3V3fBmyJzBoTyD4gCdhNrBoT06DdRQnMdr2fnJlSXND7CaEPyrtKYdOt16EOGd0dRerLiQm2NdYMX8YmBPefChuHk2swHpAPOOsetRZD1RoZWvpheNl8PEWChkup0MuMCKHIFCcvMLeH184GOqUB%2FDAvRibmhniYwyqd2LI1ofGNpq93raMj%2FkQDaWc1QqIDQAmT3c7oe5e%2B79c05p%2BLUKFLUts%2B%2B1JqQL4ZbSpIFMlMMsYD3H15gkvfr092XOHwZRISHABYayGJXYr6JXZEdX1dPOUp6PPnOW%2Fal0VEjhDr1mCUpXHKcwOVC%2FrR%2BqcGQ1zdMwGfkbGPS9yHrE2PFrVh4Aq1YVcgeU8eHQUtnSqn5OOb&X-Amz-Signature=008a484a2fe7657f4c44094fcae8d929cbace823d9612d5976baa1de26ccbd34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6WREAR6%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIGlHZywOUrrgfPqO8zp6RtaQ8R%2Bp4t34LsDmM7lgktpxAiEA2wUA7nEmMEa2rywZ6oUkwwgD6vugG4Uzu0COEVAULMwqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKNLrHzw2EVZhl5SCrcA71cAD5jYUvqPMoWhXlMzVihe37m7EGDvk9TlEkd4RJtRvztZYdpxPHWXThoKiPke53t5%2BqSTQLafH2zoFNIUvVKychGR6C7t44m2uQUX1Xiqw5%2FwjfqW5lTJfg3NHtviwvP%2FQNt9X4Eiasyoy4%2FEZLr5j8gZn42lmNr%2FXXRHTyIFRbQ3JZrvRqT5YFCSrLXmhDzWrQfC0iWe7FNRTWZBax6AHiIw%2F7VdYdYhF%2BLON4FPak4wbcwg%2BYpmJdVDxdEzzy4Er5pCo%2Bbd5O%2FHBW%2BvVnt3AwfxVfmYNrtnc3XobyjXlAo2WSsi%2FHpow1gbBdaSzi%2BZ6K7zguEzRZuQloYBbd7ZE%2FYfnIIYgvJXCB9lgCJ%2B0KhaMEyHQt3eZMFjGTe96a2%2F6U9eTqN5WSQN7%2FjBdcG%2BRRbEQ4Vrxhcm5JtkKeh%2FiSmrgh63z%2FaRIT7Ijv5ZVTbYaGTnpR7PD1MOGanoaDo1Ot6VhlHaIli%2FgBtnizQCNbgHkMo3V3fBmyJzBoTyD4gCdhNrBoT06DdRQnMdr2fnJlSXND7CaEPyrtKYdOt16EOGd0dRerLiQm2NdYMX8YmBPefChuHk2swHpAPOOsetRZD1RoZWvpheNl8PEWChkup0MuMCKHIFCcvMLeH184GOqUB%2FDAvRibmhniYwyqd2LI1ofGNpq93raMj%2FkQDaWc1QqIDQAmT3c7oe5e%2B79c05p%2BLUKFLUts%2B%2B1JqQL4ZbSpIFMlMMsYD3H15gkvfr092XOHwZRISHABYayGJXYr6JXZEdX1dPOUp6PPnOW%2Fal0VEjhDr1mCUpXHKcwOVC%2FrR%2BqcGQ1zdMwGfkbGPS9yHrE2PFrVh4Aq1YVcgeU8eHQUtnSqn5OOb&X-Amz-Signature=822ae8ed004bfaa31e791c1521d5983540ae17718dab9f7449eeb3e331e501bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6WREAR6%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIGlHZywOUrrgfPqO8zp6RtaQ8R%2Bp4t34LsDmM7lgktpxAiEA2wUA7nEmMEa2rywZ6oUkwwgD6vugG4Uzu0COEVAULMwqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKNLrHzw2EVZhl5SCrcA71cAD5jYUvqPMoWhXlMzVihe37m7EGDvk9TlEkd4RJtRvztZYdpxPHWXThoKiPke53t5%2BqSTQLafH2zoFNIUvVKychGR6C7t44m2uQUX1Xiqw5%2FwjfqW5lTJfg3NHtviwvP%2FQNt9X4Eiasyoy4%2FEZLr5j8gZn42lmNr%2FXXRHTyIFRbQ3JZrvRqT5YFCSrLXmhDzWrQfC0iWe7FNRTWZBax6AHiIw%2F7VdYdYhF%2BLON4FPak4wbcwg%2BYpmJdVDxdEzzy4Er5pCo%2Bbd5O%2FHBW%2BvVnt3AwfxVfmYNrtnc3XobyjXlAo2WSsi%2FHpow1gbBdaSzi%2BZ6K7zguEzRZuQloYBbd7ZE%2FYfnIIYgvJXCB9lgCJ%2B0KhaMEyHQt3eZMFjGTe96a2%2F6U9eTqN5WSQN7%2FjBdcG%2BRRbEQ4Vrxhcm5JtkKeh%2FiSmrgh63z%2FaRIT7Ijv5ZVTbYaGTnpR7PD1MOGanoaDo1Ot6VhlHaIli%2FgBtnizQCNbgHkMo3V3fBmyJzBoTyD4gCdhNrBoT06DdRQnMdr2fnJlSXND7CaEPyrtKYdOt16EOGd0dRerLiQm2NdYMX8YmBPefChuHk2swHpAPOOsetRZD1RoZWvpheNl8PEWChkup0MuMCKHIFCcvMLeH184GOqUB%2FDAvRibmhniYwyqd2LI1ofGNpq93raMj%2FkQDaWc1QqIDQAmT3c7oe5e%2B79c05p%2BLUKFLUts%2B%2B1JqQL4ZbSpIFMlMMsYD3H15gkvfr092XOHwZRISHABYayGJXYr6JXZEdX1dPOUp6PPnOW%2Fal0VEjhDr1mCUpXHKcwOVC%2FrR%2BqcGQ1zdMwGfkbGPS9yHrE2PFrVh4Aq1YVcgeU8eHQUtnSqn5OOb&X-Amz-Signature=10b5c96142f29e682384958aaf9d42708983e14ef47e0e1e4aec90cc39d86e70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

