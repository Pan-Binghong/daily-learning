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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIM5M5UV%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYScEX%2BcfAFLrJ4fkEAD7FWBlEMEMGyYCv7FkU2aOBNgIhANzIh9ItfKHgsnRW3NNwDxoLy%2BkmVu%2FZd1iWm1AbLO2cKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAbwYJ6V1FtqzrT9Uq3APqIS8PglGaeQNJYcbOV9VdYUg7ihDMaSAkRuK2Xmog7z4chpI%2BgEqlYxtS7lQygS%2BymEJH6edHgDt6TTxBLDDwj4XeOe%2B4Ld58mjKqK6Z5fvdPMvCeHO%2FhF0g%2Bu6KswrW8zLOeaIa1KdZpLElct7r9YUuEoctgr%2BO5XdsZOZoc0oudQLrIGciD8KVCynG8vT4Mn2VjKwObvJlsjx%2Fu0IpQZwHpMTOTvCTpML803fcfDtspp%2FlupCpeybC1m84t8JsKfuIFYfGB6edAWm9Z4Q8X%2Bv7jonEmCZFWzthHoIiZmvvIungQcdATScN0%2BMaO8167MYaTTtnm51fMc6MoIOjshS6fScdviQtgN6jD8rR3C4Vqz3JHZPwYsBZdUeLq%2BkYHsYXhAN%2Boqa5N7xH8FKDsMYOPcwHj9D3T3HPDODcIJFy2pYoD0Jxf8sj79f26%2BMW86vrh1jiEZfom7Kxc2KpGgCGAGWc3MU%2BUmmuIdenMiquJ6kfFLMDfpxdHltqXWkvF8cWCU7ZOAavke3JYX0lzoI3ztRuf3YtTHjkaV55YCSqicWdfCZfVXMQnEPvzJF5KbMHTsuGOyhsBjaWHl9MqrIVXU33kN%2BpR5nmzo66g5s75jdtqvJFEzMBT6DCBpo3OBjqkAXcuJzkQFJMpEoDhqIx1P1S3Zp1RuFaO0%2Bv6bRtp9Dkvu2DuOMzIYeLPaBBGHsM1KaOfCs1o7HJX7tG5ZEXKOiVNAWN1ampfQVnylUMCdn7vD8hQspTvZfwgzRTS%2Bh24HlUWHmVOwA5%2FC9FrLza%2FlAXh9RfO5I173GArZdez%2BhbFTQ7nzud%2Frup9FIbBMWm9RzrazZxbEiavuAoHhW5MgIVM%2Fj4o&X-Amz-Signature=29dc211156e0e5111e11015dc646f57ec88050340ad888335d26cd9beaa20d10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIM5M5UV%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYScEX%2BcfAFLrJ4fkEAD7FWBlEMEMGyYCv7FkU2aOBNgIhANzIh9ItfKHgsnRW3NNwDxoLy%2BkmVu%2FZd1iWm1AbLO2cKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAbwYJ6V1FtqzrT9Uq3APqIS8PglGaeQNJYcbOV9VdYUg7ihDMaSAkRuK2Xmog7z4chpI%2BgEqlYxtS7lQygS%2BymEJH6edHgDt6TTxBLDDwj4XeOe%2B4Ld58mjKqK6Z5fvdPMvCeHO%2FhF0g%2Bu6KswrW8zLOeaIa1KdZpLElct7r9YUuEoctgr%2BO5XdsZOZoc0oudQLrIGciD8KVCynG8vT4Mn2VjKwObvJlsjx%2Fu0IpQZwHpMTOTvCTpML803fcfDtspp%2FlupCpeybC1m84t8JsKfuIFYfGB6edAWm9Z4Q8X%2Bv7jonEmCZFWzthHoIiZmvvIungQcdATScN0%2BMaO8167MYaTTtnm51fMc6MoIOjshS6fScdviQtgN6jD8rR3C4Vqz3JHZPwYsBZdUeLq%2BkYHsYXhAN%2Boqa5N7xH8FKDsMYOPcwHj9D3T3HPDODcIJFy2pYoD0Jxf8sj79f26%2BMW86vrh1jiEZfom7Kxc2KpGgCGAGWc3MU%2BUmmuIdenMiquJ6kfFLMDfpxdHltqXWkvF8cWCU7ZOAavke3JYX0lzoI3ztRuf3YtTHjkaV55YCSqicWdfCZfVXMQnEPvzJF5KbMHTsuGOyhsBjaWHl9MqrIVXU33kN%2BpR5nmzo66g5s75jdtqvJFEzMBT6DCBpo3OBjqkAXcuJzkQFJMpEoDhqIx1P1S3Zp1RuFaO0%2Bv6bRtp9Dkvu2DuOMzIYeLPaBBGHsM1KaOfCs1o7HJX7tG5ZEXKOiVNAWN1ampfQVnylUMCdn7vD8hQspTvZfwgzRTS%2Bh24HlUWHmVOwA5%2FC9FrLza%2FlAXh9RfO5I173GArZdez%2BhbFTQ7nzud%2Frup9FIbBMWm9RzrazZxbEiavuAoHhW5MgIVM%2Fj4o&X-Amz-Signature=242e99e8a85bd02e8b64bdca0e2947bb1f3d91470c24f0ebb3c6ff7c5b6abf46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIM5M5UV%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYScEX%2BcfAFLrJ4fkEAD7FWBlEMEMGyYCv7FkU2aOBNgIhANzIh9ItfKHgsnRW3NNwDxoLy%2BkmVu%2FZd1iWm1AbLO2cKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAbwYJ6V1FtqzrT9Uq3APqIS8PglGaeQNJYcbOV9VdYUg7ihDMaSAkRuK2Xmog7z4chpI%2BgEqlYxtS7lQygS%2BymEJH6edHgDt6TTxBLDDwj4XeOe%2B4Ld58mjKqK6Z5fvdPMvCeHO%2FhF0g%2Bu6KswrW8zLOeaIa1KdZpLElct7r9YUuEoctgr%2BO5XdsZOZoc0oudQLrIGciD8KVCynG8vT4Mn2VjKwObvJlsjx%2Fu0IpQZwHpMTOTvCTpML803fcfDtspp%2FlupCpeybC1m84t8JsKfuIFYfGB6edAWm9Z4Q8X%2Bv7jonEmCZFWzthHoIiZmvvIungQcdATScN0%2BMaO8167MYaTTtnm51fMc6MoIOjshS6fScdviQtgN6jD8rR3C4Vqz3JHZPwYsBZdUeLq%2BkYHsYXhAN%2Boqa5N7xH8FKDsMYOPcwHj9D3T3HPDODcIJFy2pYoD0Jxf8sj79f26%2BMW86vrh1jiEZfom7Kxc2KpGgCGAGWc3MU%2BUmmuIdenMiquJ6kfFLMDfpxdHltqXWkvF8cWCU7ZOAavke3JYX0lzoI3ztRuf3YtTHjkaV55YCSqicWdfCZfVXMQnEPvzJF5KbMHTsuGOyhsBjaWHl9MqrIVXU33kN%2BpR5nmzo66g5s75jdtqvJFEzMBT6DCBpo3OBjqkAXcuJzkQFJMpEoDhqIx1P1S3Zp1RuFaO0%2Bv6bRtp9Dkvu2DuOMzIYeLPaBBGHsM1KaOfCs1o7HJX7tG5ZEXKOiVNAWN1ampfQVnylUMCdn7vD8hQspTvZfwgzRTS%2Bh24HlUWHmVOwA5%2FC9FrLza%2FlAXh9RfO5I173GArZdez%2BhbFTQ7nzud%2Frup9FIbBMWm9RzrazZxbEiavuAoHhW5MgIVM%2Fj4o&X-Amz-Signature=4c996968cdbde41f3b6f1a1d74eb6d27b350b1415ac02d018a834684080250be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

