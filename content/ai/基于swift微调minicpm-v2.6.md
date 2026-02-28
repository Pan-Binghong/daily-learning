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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OJAFIXY%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGbxXooEMemiYiRfiuEIbKzWegbPnvFUQcvYThvVQ%2FxjAiA0jwHLvojAmgT%2FooM0dL4P4HDUwsCObGj%2FdqUccgBDyyr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMJrU9VX%2FNVOU9%2Fui0KtwDF%2BvM%2FA%2BlEGwhlaWXtgXYWOWgTuLWExrv%2Bb6wM5JLmJFltD9NSJh4xufEmIOKMtzbHFBwnh0f6Z5awQXK%2ByS31GZnMQdEjkCPUotEoeJlhVsPEGhIQBPmMyb2riP50a%2B%2B8xqJnlwUybpQtvWSg9nbGd3oJXnnwsbZw02hzsW%2BZt8%2FcE%2BuX9Qd%2BV%2BiUpMziDAa2nwPJXYGJLmc9BqrJgAwJKjC7Xz4x%2BV4Xtc3FEUxBwyaj%2BuZEsCWKAtlwuzNhR7S5zmFirqXIwB9jekfM%2Bbcmk%2Bd0%2FDuGWFiXiRcQ49bpXj%2F%2FfkLUywR7Yfdzik%2B3QcXx7t8Z7A8z45wm%2BzdvG0xy3B5bX3PTWRDkGZLva6HBCm6vQDLpxCO9ysUdiX5Ex0zyna5dy76TjKfQixm%2BS6klEz8Z7LpSGgwm6ok2a%2Bm5farolNgBjhUbARjrlQg3lQy5yh%2F1qxIoUGekgS1wxUJP5Tep8qobA5bRwyT5%2Fax5yj%2Ff7euFWep3RtxZiS2wxyecfqT5zqslaYoR9%2F%2Bq3s1QlZmr98wGounVv1ihly0Y2KZvVM9btJkFYD0iacVuEbcVBVLg8xVQJ84KhWA2YPDZg6BbQl%2FB4vi5hIG856kUqUp1bzFytyJp57%2Fuu0wgpaJzQY6pgEBp8MfskbSLjsE7nVlOqaV6qs7%2BL1PFrEt%2BL8h%2Fo4t6zdOjgyTMckPHYf9a5ce6HKft8eNVL0%2Fhyd1rEfL6LILAoZ0Ymsorae6rlnGoZ20YsP0dL1RBVGZRP70fyrlA0lMkWXGVuwas5tAM2oN6Ml16lBJQAaj5ts2A0jElAisiwpp3cKI9P9iniBk0Uac5jEW8eR7qH0oGdmKO6OVi2XGKjmEeaku&X-Amz-Signature=11aeabedcc209228790407a0cf52578e7f3b8d877279e45af5f4c4610bcf346a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OJAFIXY%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGbxXooEMemiYiRfiuEIbKzWegbPnvFUQcvYThvVQ%2FxjAiA0jwHLvojAmgT%2FooM0dL4P4HDUwsCObGj%2FdqUccgBDyyr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMJrU9VX%2FNVOU9%2Fui0KtwDF%2BvM%2FA%2BlEGwhlaWXtgXYWOWgTuLWExrv%2Bb6wM5JLmJFltD9NSJh4xufEmIOKMtzbHFBwnh0f6Z5awQXK%2ByS31GZnMQdEjkCPUotEoeJlhVsPEGhIQBPmMyb2riP50a%2B%2B8xqJnlwUybpQtvWSg9nbGd3oJXnnwsbZw02hzsW%2BZt8%2FcE%2BuX9Qd%2BV%2BiUpMziDAa2nwPJXYGJLmc9BqrJgAwJKjC7Xz4x%2BV4Xtc3FEUxBwyaj%2BuZEsCWKAtlwuzNhR7S5zmFirqXIwB9jekfM%2Bbcmk%2Bd0%2FDuGWFiXiRcQ49bpXj%2F%2FfkLUywR7Yfdzik%2B3QcXx7t8Z7A8z45wm%2BzdvG0xy3B5bX3PTWRDkGZLva6HBCm6vQDLpxCO9ysUdiX5Ex0zyna5dy76TjKfQixm%2BS6klEz8Z7LpSGgwm6ok2a%2Bm5farolNgBjhUbARjrlQg3lQy5yh%2F1qxIoUGekgS1wxUJP5Tep8qobA5bRwyT5%2Fax5yj%2Ff7euFWep3RtxZiS2wxyecfqT5zqslaYoR9%2F%2Bq3s1QlZmr98wGounVv1ihly0Y2KZvVM9btJkFYD0iacVuEbcVBVLg8xVQJ84KhWA2YPDZg6BbQl%2FB4vi5hIG856kUqUp1bzFytyJp57%2Fuu0wgpaJzQY6pgEBp8MfskbSLjsE7nVlOqaV6qs7%2BL1PFrEt%2BL8h%2Fo4t6zdOjgyTMckPHYf9a5ce6HKft8eNVL0%2Fhyd1rEfL6LILAoZ0Ymsorae6rlnGoZ20YsP0dL1RBVGZRP70fyrlA0lMkWXGVuwas5tAM2oN6Ml16lBJQAaj5ts2A0jElAisiwpp3cKI9P9iniBk0Uac5jEW8eR7qH0oGdmKO6OVi2XGKjmEeaku&X-Amz-Signature=2c699c35fc7559ca2fce250a7d673127a0b5fe36ac1dbcfaa7799783fd72f434&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OJAFIXY%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGbxXooEMemiYiRfiuEIbKzWegbPnvFUQcvYThvVQ%2FxjAiA0jwHLvojAmgT%2FooM0dL4P4HDUwsCObGj%2FdqUccgBDyyr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMJrU9VX%2FNVOU9%2Fui0KtwDF%2BvM%2FA%2BlEGwhlaWXtgXYWOWgTuLWExrv%2Bb6wM5JLmJFltD9NSJh4xufEmIOKMtzbHFBwnh0f6Z5awQXK%2ByS31GZnMQdEjkCPUotEoeJlhVsPEGhIQBPmMyb2riP50a%2B%2B8xqJnlwUybpQtvWSg9nbGd3oJXnnwsbZw02hzsW%2BZt8%2FcE%2BuX9Qd%2BV%2BiUpMziDAa2nwPJXYGJLmc9BqrJgAwJKjC7Xz4x%2BV4Xtc3FEUxBwyaj%2BuZEsCWKAtlwuzNhR7S5zmFirqXIwB9jekfM%2Bbcmk%2Bd0%2FDuGWFiXiRcQ49bpXj%2F%2FfkLUywR7Yfdzik%2B3QcXx7t8Z7A8z45wm%2BzdvG0xy3B5bX3PTWRDkGZLva6HBCm6vQDLpxCO9ysUdiX5Ex0zyna5dy76TjKfQixm%2BS6klEz8Z7LpSGgwm6ok2a%2Bm5farolNgBjhUbARjrlQg3lQy5yh%2F1qxIoUGekgS1wxUJP5Tep8qobA5bRwyT5%2Fax5yj%2Ff7euFWep3RtxZiS2wxyecfqT5zqslaYoR9%2F%2Bq3s1QlZmr98wGounVv1ihly0Y2KZvVM9btJkFYD0iacVuEbcVBVLg8xVQJ84KhWA2YPDZg6BbQl%2FB4vi5hIG856kUqUp1bzFytyJp57%2Fuu0wgpaJzQY6pgEBp8MfskbSLjsE7nVlOqaV6qs7%2BL1PFrEt%2BL8h%2Fo4t6zdOjgyTMckPHYf9a5ce6HKft8eNVL0%2Fhyd1rEfL6LILAoZ0Ymsorae6rlnGoZ20YsP0dL1RBVGZRP70fyrlA0lMkWXGVuwas5tAM2oN6Ml16lBJQAaj5ts2A0jElAisiwpp3cKI9P9iniBk0Uac5jEW8eR7qH0oGdmKO6OVi2XGKjmEeaku&X-Amz-Signature=0980c685d86bf257bca7f38093cb790e7164ecc55cb5010ac3540bdab74307f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

