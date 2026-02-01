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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVWQ32HK%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCKYTaxyqdXL1Tjb%2FA3JPeqbnsVF4B2eSCYPmRQlkY6AIhAKGQUvKyVtGlfgDohn8PUXzOxAEIOfZWDzpx%2Bkty9pEVKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwKsnVeZEK2oJgD7VEq3AMO91LybU5AOXHphpqJ1wRsWCfJVL5YEKOo7gaPN80LwO9A7uKCTFN%2F9xF2mCbUhwzZzyRE1EDUZ4bpBbN6Ju7JrHrT1gWocpBaWhS3yMKgL4an8B8AOATShu172nxPhSsXJa5Ta%2F2EkxiswTsjSGljXece9vj%2BF3ln2ztI7TdI1nsZwckCd5bT40h99Vr5kTkInsFqOtkL%2FcpsJfmyXTAWHhR4wZ6pOmhBp%2FGpaRrsE2pt0OSwQuRo1p1OPR%2BVxvBt%2Bp%2FVebl1UYmv0x9ZCk%2FVdgJnuP9a7MMwJBR67b6JCgXrRJ%2FtTNqbdOC7rHpeniI9ZCIOcOaw2M0U9pnXeGvcqkpSF0vW5OXJ1bMSKxQjhmvoK7iJQ%2FF8I03PsB8nFrWfiIQK%2Fc6cfVW2U%2BEFC25tHalbmTZHJPpFMi0pclqOkA%2FbmButgEoV%2F%2FAnS1F8XYNvcFHzGebMrizHCjxDHBGLPGZ%2BybBiElJMfjtOt%2Fnxjs2cMU9q8mlaNT%2FJfj7nWBPemii%2BjJwlYJy9rO4G2ZmWdeNiAbj7QOS06oq%2BXGHU3wcZwSh%2FapanZjkduJlaIk2KwP%2Buv5QawMyGsGRpp5nrLiEWSInLPtQUawX%2Fv8OvnNB7iURubtCZtTsx2DDWjPvLBjqkAVj8Y6SBfImST4MMXv8opAdS23BzGd4JPCleTguC0YEVM%2B14QI0Dw64EDXz0a%2BNfzBGAkdi4RzucAKSWZS2ousE5Kz1MdVRwW0ADKw3s2Qwk3VTKZTORK8cBT1ZTCur6ndhgcAu4q50ro6F1G0ObjPhoAHoqX1fNftYqpB7waDgvVePVm9gu8yaeuNZoKbANqJyy%2F3rjPEHuTKcYH4E6Z%2F7Gltgv&X-Amz-Signature=ca942d74ec8fd50fd3f1ea76aaf7de85efbef9691ea146b041a6d29d20ccb673&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVWQ32HK%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCKYTaxyqdXL1Tjb%2FA3JPeqbnsVF4B2eSCYPmRQlkY6AIhAKGQUvKyVtGlfgDohn8PUXzOxAEIOfZWDzpx%2Bkty9pEVKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwKsnVeZEK2oJgD7VEq3AMO91LybU5AOXHphpqJ1wRsWCfJVL5YEKOo7gaPN80LwO9A7uKCTFN%2F9xF2mCbUhwzZzyRE1EDUZ4bpBbN6Ju7JrHrT1gWocpBaWhS3yMKgL4an8B8AOATShu172nxPhSsXJa5Ta%2F2EkxiswTsjSGljXece9vj%2BF3ln2ztI7TdI1nsZwckCd5bT40h99Vr5kTkInsFqOtkL%2FcpsJfmyXTAWHhR4wZ6pOmhBp%2FGpaRrsE2pt0OSwQuRo1p1OPR%2BVxvBt%2Bp%2FVebl1UYmv0x9ZCk%2FVdgJnuP9a7MMwJBR67b6JCgXrRJ%2FtTNqbdOC7rHpeniI9ZCIOcOaw2M0U9pnXeGvcqkpSF0vW5OXJ1bMSKxQjhmvoK7iJQ%2FF8I03PsB8nFrWfiIQK%2Fc6cfVW2U%2BEFC25tHalbmTZHJPpFMi0pclqOkA%2FbmButgEoV%2F%2FAnS1F8XYNvcFHzGebMrizHCjxDHBGLPGZ%2BybBiElJMfjtOt%2Fnxjs2cMU9q8mlaNT%2FJfj7nWBPemii%2BjJwlYJy9rO4G2ZmWdeNiAbj7QOS06oq%2BXGHU3wcZwSh%2FapanZjkduJlaIk2KwP%2Buv5QawMyGsGRpp5nrLiEWSInLPtQUawX%2Fv8OvnNB7iURubtCZtTsx2DDWjPvLBjqkAVj8Y6SBfImST4MMXv8opAdS23BzGd4JPCleTguC0YEVM%2B14QI0Dw64EDXz0a%2BNfzBGAkdi4RzucAKSWZS2ousE5Kz1MdVRwW0ADKw3s2Qwk3VTKZTORK8cBT1ZTCur6ndhgcAu4q50ro6F1G0ObjPhoAHoqX1fNftYqpB7waDgvVePVm9gu8yaeuNZoKbANqJyy%2F3rjPEHuTKcYH4E6Z%2F7Gltgv&X-Amz-Signature=c2cce681c068dc29de11336a2df433de1351f9fe8b12c23abccae4956c5b5206&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVWQ32HK%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCKYTaxyqdXL1Tjb%2FA3JPeqbnsVF4B2eSCYPmRQlkY6AIhAKGQUvKyVtGlfgDohn8PUXzOxAEIOfZWDzpx%2Bkty9pEVKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwKsnVeZEK2oJgD7VEq3AMO91LybU5AOXHphpqJ1wRsWCfJVL5YEKOo7gaPN80LwO9A7uKCTFN%2F9xF2mCbUhwzZzyRE1EDUZ4bpBbN6Ju7JrHrT1gWocpBaWhS3yMKgL4an8B8AOATShu172nxPhSsXJa5Ta%2F2EkxiswTsjSGljXece9vj%2BF3ln2ztI7TdI1nsZwckCd5bT40h99Vr5kTkInsFqOtkL%2FcpsJfmyXTAWHhR4wZ6pOmhBp%2FGpaRrsE2pt0OSwQuRo1p1OPR%2BVxvBt%2Bp%2FVebl1UYmv0x9ZCk%2FVdgJnuP9a7MMwJBR67b6JCgXrRJ%2FtTNqbdOC7rHpeniI9ZCIOcOaw2M0U9pnXeGvcqkpSF0vW5OXJ1bMSKxQjhmvoK7iJQ%2FF8I03PsB8nFrWfiIQK%2Fc6cfVW2U%2BEFC25tHalbmTZHJPpFMi0pclqOkA%2FbmButgEoV%2F%2FAnS1F8XYNvcFHzGebMrizHCjxDHBGLPGZ%2BybBiElJMfjtOt%2Fnxjs2cMU9q8mlaNT%2FJfj7nWBPemii%2BjJwlYJy9rO4G2ZmWdeNiAbj7QOS06oq%2BXGHU3wcZwSh%2FapanZjkduJlaIk2KwP%2Buv5QawMyGsGRpp5nrLiEWSInLPtQUawX%2Fv8OvnNB7iURubtCZtTsx2DDWjPvLBjqkAVj8Y6SBfImST4MMXv8opAdS23BzGd4JPCleTguC0YEVM%2B14QI0Dw64EDXz0a%2BNfzBGAkdi4RzucAKSWZS2ousE5Kz1MdVRwW0ADKw3s2Qwk3VTKZTORK8cBT1ZTCur6ndhgcAu4q50ro6F1G0ObjPhoAHoqX1fNftYqpB7waDgvVePVm9gu8yaeuNZoKbANqJyy%2F3rjPEHuTKcYH4E6Z%2F7Gltgv&X-Amz-Signature=880bf885166163a07a82d258a3c9bbc0487fa033e51f13a56310b70dc5f4aefd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

