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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6FWA6KR%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQC865BYGeCBGJfKThqSq007RBh5ULzo6CRoZSj7KjFTyAIgCVeLQ8js%2B372%2BEsVRJnxZIvm1j0b%2BCoT9jXXtzmrSnEqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXMzkNHoKChgIF22yrcA9NQBFMQVRfr9Q7DIpQHGXiRuw1muoTHlB3A3%2B%2FUYDtanFuDkwe2ZVPKHdmt%2FqXL83qLGE5q2op%2BTrvsiGoxeaz3VXeq8LV3Xup2e97N11vzB3P84OF3l%2BoxYmmR6nCOD7OhiyeP7fpJoXmOowYYpov%2BCYV4vLwfvUeCIJxtetepMWSHa63B2HvlJePVzu35oLV%2F8xRuJs8akFSzYnHOp8JhkaYe9dAa90vHyNfuKmSUcUWWTpiH6bEPmRbmA5FqYz1F%2Fz5I0PfGzhzNZdz77OBihKSObGBMGhiXYG9Y4MslMJtL7UlIfSV9%2BmR4VLK%2FgKBq3JtbA9Pd%2BtSOQ1gAli21SEU2YHiH6eFbASFjod421B9fq%2BVbSk8IWUf9dljepqxoBz6t8wSdcDZDaldIMxMbXiVyoOKSMo%2B9FgGlpacl3JxX6XWCCVy1RNVuzXGptAFTLMrzc3c1hNHoOWpIuKfbTx5xM8w5Yf%2BtO4YsZhCTgsZA9YyFE%2BOGSk3Jtb%2BwJOwRmi7k12xnhbS07FcLaVOOOTWzU3%2FMg04iRlHEaRo6tlS9LLxP%2BPvy31k5mOE%2B4otzh2ZvTiMBtFrFUyc71VMsGakmSQgjH3ob77ckRIticM0UyNpywqRMH033MKqU78wGOqUBqh2Z4iGNlX5oya1fm%2BjtgaCRjbHZ7fRXOq4SF%2FFVWRCPsFmgXnUVk8gBs7d%2B7ybaH99PrvVHFGrSAtE6sUlUeuU%2Fp9bR%2FWyuOdXLqnTeo4QVZtZ7JLU30bmZ8GFpLOCAgiS7vcAH784Maf65pvOTfk%2BgdEYPy0E9pIale4ay0oWDjbRCD0DbkuSiT1qVr2az56sfqCmIEhUR38wMzYDazoYFlJH9&X-Amz-Signature=bea58e3447342bdadc9cbebd96b39b75f80b66a7b1f5c67130bfba561abfc0e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6FWA6KR%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQC865BYGeCBGJfKThqSq007RBh5ULzo6CRoZSj7KjFTyAIgCVeLQ8js%2B372%2BEsVRJnxZIvm1j0b%2BCoT9jXXtzmrSnEqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXMzkNHoKChgIF22yrcA9NQBFMQVRfr9Q7DIpQHGXiRuw1muoTHlB3A3%2B%2FUYDtanFuDkwe2ZVPKHdmt%2FqXL83qLGE5q2op%2BTrvsiGoxeaz3VXeq8LV3Xup2e97N11vzB3P84OF3l%2BoxYmmR6nCOD7OhiyeP7fpJoXmOowYYpov%2BCYV4vLwfvUeCIJxtetepMWSHa63B2HvlJePVzu35oLV%2F8xRuJs8akFSzYnHOp8JhkaYe9dAa90vHyNfuKmSUcUWWTpiH6bEPmRbmA5FqYz1F%2Fz5I0PfGzhzNZdz77OBihKSObGBMGhiXYG9Y4MslMJtL7UlIfSV9%2BmR4VLK%2FgKBq3JtbA9Pd%2BtSOQ1gAli21SEU2YHiH6eFbASFjod421B9fq%2BVbSk8IWUf9dljepqxoBz6t8wSdcDZDaldIMxMbXiVyoOKSMo%2B9FgGlpacl3JxX6XWCCVy1RNVuzXGptAFTLMrzc3c1hNHoOWpIuKfbTx5xM8w5Yf%2BtO4YsZhCTgsZA9YyFE%2BOGSk3Jtb%2BwJOwRmi7k12xnhbS07FcLaVOOOTWzU3%2FMg04iRlHEaRo6tlS9LLxP%2BPvy31k5mOE%2B4otzh2ZvTiMBtFrFUyc71VMsGakmSQgjH3ob77ckRIticM0UyNpywqRMH033MKqU78wGOqUBqh2Z4iGNlX5oya1fm%2BjtgaCRjbHZ7fRXOq4SF%2FFVWRCPsFmgXnUVk8gBs7d%2B7ybaH99PrvVHFGrSAtE6sUlUeuU%2Fp9bR%2FWyuOdXLqnTeo4QVZtZ7JLU30bmZ8GFpLOCAgiS7vcAH784Maf65pvOTfk%2BgdEYPy0E9pIale4ay0oWDjbRCD0DbkuSiT1qVr2az56sfqCmIEhUR38wMzYDazoYFlJH9&X-Amz-Signature=c364b6bdaef18842bf993c835312b5a929601103e1e82a9440144f261f432260&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6FWA6KR%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQC865BYGeCBGJfKThqSq007RBh5ULzo6CRoZSj7KjFTyAIgCVeLQ8js%2B372%2BEsVRJnxZIvm1j0b%2BCoT9jXXtzmrSnEqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXMzkNHoKChgIF22yrcA9NQBFMQVRfr9Q7DIpQHGXiRuw1muoTHlB3A3%2B%2FUYDtanFuDkwe2ZVPKHdmt%2FqXL83qLGE5q2op%2BTrvsiGoxeaz3VXeq8LV3Xup2e97N11vzB3P84OF3l%2BoxYmmR6nCOD7OhiyeP7fpJoXmOowYYpov%2BCYV4vLwfvUeCIJxtetepMWSHa63B2HvlJePVzu35oLV%2F8xRuJs8akFSzYnHOp8JhkaYe9dAa90vHyNfuKmSUcUWWTpiH6bEPmRbmA5FqYz1F%2Fz5I0PfGzhzNZdz77OBihKSObGBMGhiXYG9Y4MslMJtL7UlIfSV9%2BmR4VLK%2FgKBq3JtbA9Pd%2BtSOQ1gAli21SEU2YHiH6eFbASFjod421B9fq%2BVbSk8IWUf9dljepqxoBz6t8wSdcDZDaldIMxMbXiVyoOKSMo%2B9FgGlpacl3JxX6XWCCVy1RNVuzXGptAFTLMrzc3c1hNHoOWpIuKfbTx5xM8w5Yf%2BtO4YsZhCTgsZA9YyFE%2BOGSk3Jtb%2BwJOwRmi7k12xnhbS07FcLaVOOOTWzU3%2FMg04iRlHEaRo6tlS9LLxP%2BPvy31k5mOE%2B4otzh2ZvTiMBtFrFUyc71VMsGakmSQgjH3ob77ckRIticM0UyNpywqRMH033MKqU78wGOqUBqh2Z4iGNlX5oya1fm%2BjtgaCRjbHZ7fRXOq4SF%2FFVWRCPsFmgXnUVk8gBs7d%2B7ybaH99PrvVHFGrSAtE6sUlUeuU%2Fp9bR%2FWyuOdXLqnTeo4QVZtZ7JLU30bmZ8GFpLOCAgiS7vcAH784Maf65pvOTfk%2BgdEYPy0E9pIale4ay0oWDjbRCD0DbkuSiT1qVr2az56sfqCmIEhUR38wMzYDazoYFlJH9&X-Amz-Signature=37ff3e5efb2da3760b60b5b1fbd0039ab53ed65f6742c1afd4d22fedf01b660c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

