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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOJJXHCO%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7f7YTh8w2%2BULNBjmP3rs%2BDhf%2BEgJi5pqMYMfNL8uGmAIhAKYCNWNKiALHtVtCN9LwWv60RnTLCF5mVJWFM1oUAqV5Kv8DCH8QABoMNjM3NDIzMTgzODA1IgyvbJC2Sn9jZ4O2jhYq3APi5NWiywRHyChMl94obJoKOhE9XGiTQL0vAJE%2BV5SiRIjDyKLa7opkMMu8YGmvW2GGOd82CdJBDQG44uLgUbTD7ql5g%2Ff%2Fcl8X0WTvO3C5E%2FDZ9Zg3is1Z7MwddV5xx%2FOHfPzlNMAvJoLIGlYxjOxjzBNfSmKDS4VTp0qhha%2Ff%2F%2FLvr69g6SFgCpMSxRWsUNOR4DOuPrSzB%2FyFz%2BZaSWJKjcHcGOPZLA%2BTwq4AQZ0c9TkXPXRrOc%2Bl7Ek3haN04hkLrPqO4v5hNzPArkBHhn8KIqQIW%2FEHPE8Iv8vnigj6WJCxh%2B4pSIwgiWnUZdHOWekdyDgpzDZ8UA1R7WTUuJuVxbe%2Bzj56W76Wflv5bHl%2B8Pd67OmIzwMlWkt%2B2HHgbtsv8ZBRyyNuys7A4507fspB7%2FgA82SiRUTMs9qHRrHb4WxXPbWNBeZzUjxSKsVOWsEn1rZvJDb%2FANEqdDFq8Vc8GlaSPRkeULqwhoay2FnygItOLZnaFGvBVBu6RUbGZavSQ0mnz1y1KztYQU3UVT2cMHAHH6FfsYIlc8tB8sf7Hcz6d6a7OfgEMlX6QQpkHyRz%2F42wnZHj5JUBKn8SqL%2BjlTiLRe31krvKexk3%2BgcMFiRCUOitVUqA7yvuuDCNr73OBjqkAZrtdzCr%2Bvqg1FZ8IF0qfudmvStyXtAqgwtN9lj%2B4p9FDrdE2MaAiHUaVhYVqeHqBsXVCFG9ofrDQjW0GR3CQ4MlVbGUJMpcONZfSgh5LOtwft%2BRu5qgxTDC%2By9xcwunSlUc9jDW9Ks%2Bivx0iA9ertyWAh6enhI0dlF8Z0eeiIdz6iBCyWnnA8DbjWctp0zrFTMB5%2B5Z7O0sbLdbAPL%2FOKuEfw01&X-Amz-Signature=4f74cf2fd7e861fd5fdfbc7392026cf758b2f3ecbc4777dc4680d3ef95e242e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOJJXHCO%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7f7YTh8w2%2BULNBjmP3rs%2BDhf%2BEgJi5pqMYMfNL8uGmAIhAKYCNWNKiALHtVtCN9LwWv60RnTLCF5mVJWFM1oUAqV5Kv8DCH8QABoMNjM3NDIzMTgzODA1IgyvbJC2Sn9jZ4O2jhYq3APi5NWiywRHyChMl94obJoKOhE9XGiTQL0vAJE%2BV5SiRIjDyKLa7opkMMu8YGmvW2GGOd82CdJBDQG44uLgUbTD7ql5g%2Ff%2Fcl8X0WTvO3C5E%2FDZ9Zg3is1Z7MwddV5xx%2FOHfPzlNMAvJoLIGlYxjOxjzBNfSmKDS4VTp0qhha%2Ff%2F%2FLvr69g6SFgCpMSxRWsUNOR4DOuPrSzB%2FyFz%2BZaSWJKjcHcGOPZLA%2BTwq4AQZ0c9TkXPXRrOc%2Bl7Ek3haN04hkLrPqO4v5hNzPArkBHhn8KIqQIW%2FEHPE8Iv8vnigj6WJCxh%2B4pSIwgiWnUZdHOWekdyDgpzDZ8UA1R7WTUuJuVxbe%2Bzj56W76Wflv5bHl%2B8Pd67OmIzwMlWkt%2B2HHgbtsv8ZBRyyNuys7A4507fspB7%2FgA82SiRUTMs9qHRrHb4WxXPbWNBeZzUjxSKsVOWsEn1rZvJDb%2FANEqdDFq8Vc8GlaSPRkeULqwhoay2FnygItOLZnaFGvBVBu6RUbGZavSQ0mnz1y1KztYQU3UVT2cMHAHH6FfsYIlc8tB8sf7Hcz6d6a7OfgEMlX6QQpkHyRz%2F42wnZHj5JUBKn8SqL%2BjlTiLRe31krvKexk3%2BgcMFiRCUOitVUqA7yvuuDCNr73OBjqkAZrtdzCr%2Bvqg1FZ8IF0qfudmvStyXtAqgwtN9lj%2B4p9FDrdE2MaAiHUaVhYVqeHqBsXVCFG9ofrDQjW0GR3CQ4MlVbGUJMpcONZfSgh5LOtwft%2BRu5qgxTDC%2By9xcwunSlUc9jDW9Ks%2Bivx0iA9ertyWAh6enhI0dlF8Z0eeiIdz6iBCyWnnA8DbjWctp0zrFTMB5%2B5Z7O0sbLdbAPL%2FOKuEfw01&X-Amz-Signature=2572ad7be76c84c809ba2b5cec2caca5dc69862369846cd2d3de82c32618a57b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOJJXHCO%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7f7YTh8w2%2BULNBjmP3rs%2BDhf%2BEgJi5pqMYMfNL8uGmAIhAKYCNWNKiALHtVtCN9LwWv60RnTLCF5mVJWFM1oUAqV5Kv8DCH8QABoMNjM3NDIzMTgzODA1IgyvbJC2Sn9jZ4O2jhYq3APi5NWiywRHyChMl94obJoKOhE9XGiTQL0vAJE%2BV5SiRIjDyKLa7opkMMu8YGmvW2GGOd82CdJBDQG44uLgUbTD7ql5g%2Ff%2Fcl8X0WTvO3C5E%2FDZ9Zg3is1Z7MwddV5xx%2FOHfPzlNMAvJoLIGlYxjOxjzBNfSmKDS4VTp0qhha%2Ff%2F%2FLvr69g6SFgCpMSxRWsUNOR4DOuPrSzB%2FyFz%2BZaSWJKjcHcGOPZLA%2BTwq4AQZ0c9TkXPXRrOc%2Bl7Ek3haN04hkLrPqO4v5hNzPArkBHhn8KIqQIW%2FEHPE8Iv8vnigj6WJCxh%2B4pSIwgiWnUZdHOWekdyDgpzDZ8UA1R7WTUuJuVxbe%2Bzj56W76Wflv5bHl%2B8Pd67OmIzwMlWkt%2B2HHgbtsv8ZBRyyNuys7A4507fspB7%2FgA82SiRUTMs9qHRrHb4WxXPbWNBeZzUjxSKsVOWsEn1rZvJDb%2FANEqdDFq8Vc8GlaSPRkeULqwhoay2FnygItOLZnaFGvBVBu6RUbGZavSQ0mnz1y1KztYQU3UVT2cMHAHH6FfsYIlc8tB8sf7Hcz6d6a7OfgEMlX6QQpkHyRz%2F42wnZHj5JUBKn8SqL%2BjlTiLRe31krvKexk3%2BgcMFiRCUOitVUqA7yvuuDCNr73OBjqkAZrtdzCr%2Bvqg1FZ8IF0qfudmvStyXtAqgwtN9lj%2B4p9FDrdE2MaAiHUaVhYVqeHqBsXVCFG9ofrDQjW0GR3CQ4MlVbGUJMpcONZfSgh5LOtwft%2BRu5qgxTDC%2By9xcwunSlUc9jDW9Ks%2Bivx0iA9ertyWAh6enhI0dlF8Z0eeiIdz6iBCyWnnA8DbjWctp0zrFTMB5%2B5Z7O0sbLdbAPL%2FOKuEfw01&X-Amz-Signature=44861f7ec3f56840cdb2aede52f15e447a855662b0bd2c9f5165f4ad61edbb69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

