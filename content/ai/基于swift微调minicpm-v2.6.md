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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUEOXCFV%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPTAgGOxcLb8KUkizlj4rfXWXlEXkMIXF8eLeaYOKD%2BQIgJp%2BXe%2BRGiyQOFbMcPP1CdzADvfpKfI09Oh8p%2F8G%2BVGQq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDKrz%2BoSRp7qTNMzUIircA%2Bmr5pxQ20FrKACugDfEUvM66qVgPvOP8LSvRjZ7yGUJDqpUu%2B0qKYto4MoLFIay356lL7aRIf8Ja4nF%2B7ipJk7XKAaooR%2FvrZVXIEgW9NlwIuV8yUD0D0wWCQWk15d6eocqmQi%2FchJW8u6Lmd67FQl664IYzYvr%2B1TaTRqJwIeOpgh9iPqFDQAWeL32GepNlCnuDv%2FqTAFRQEdMMfbrMfMUDR1%2FatryWzjj5hSwWmYH6NlpL6dBYKIgGODZtY9XHnHgnzFIArTTiRBVP8MljCJQXyzE0UC6iiz54%2BXHufbXMLgVTMtVyvqcwemd9edArW4jyfk86V%2B43RCAh6tmSKH83BOwV%2Fu9AeYKbx%2BZuk0Hx%2F5t31CL8GL7D3QOG703CxuW0fcsyxdsunnZws%2FFsA2chTl3hAPxTMMAuhc7Y9Q43QXw9rWS9hN2ti0AfrGQPGXx1xzcNtMwXNZ3HuBLLE4BH8sH%2Bpcq1VoltnxI5zF1I1bY9MZiROzeIGS92UfqT%2BeeCgX3C8GZdTFxZ9N%2FlS3O0baEBBYCGoTG8XpnUlw3WuC8lEEm8GykkyltDw1aLWsIk2b75t9DhPLIbwkDwrNN%2FaN1jmJVvPviVTD5xc8hEQuwTj9HOp4GUfgqMNqH7M4GOqUBMN%2BlU2Ru0r6kldAgKzoONg45iOHAB%2Bf5izuvVBni3P51shrAinFa5QMienTfhVIyBw1ulBV0PMA9VspK9S3hyOQoZXIc14Gx2bZ37bhXMGVNsCekVKe7OZiaCbROfEX9BS7E3kFEZY3lPnM7z0dh8i9DBAd%2BhFtKjkAkGmzkWHxKyt%2FngTUithZmf%2BjB0axrzhRSEoiPduDpt6dq4cqjTEf2CnWz&X-Amz-Signature=1b65fa9e224e4d9ad4278ba99d287ca28406bcf080281c6aada9931736aedd98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUEOXCFV%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPTAgGOxcLb8KUkizlj4rfXWXlEXkMIXF8eLeaYOKD%2BQIgJp%2BXe%2BRGiyQOFbMcPP1CdzADvfpKfI09Oh8p%2F8G%2BVGQq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDKrz%2BoSRp7qTNMzUIircA%2Bmr5pxQ20FrKACugDfEUvM66qVgPvOP8LSvRjZ7yGUJDqpUu%2B0qKYto4MoLFIay356lL7aRIf8Ja4nF%2B7ipJk7XKAaooR%2FvrZVXIEgW9NlwIuV8yUD0D0wWCQWk15d6eocqmQi%2FchJW8u6Lmd67FQl664IYzYvr%2B1TaTRqJwIeOpgh9iPqFDQAWeL32GepNlCnuDv%2FqTAFRQEdMMfbrMfMUDR1%2FatryWzjj5hSwWmYH6NlpL6dBYKIgGODZtY9XHnHgnzFIArTTiRBVP8MljCJQXyzE0UC6iiz54%2BXHufbXMLgVTMtVyvqcwemd9edArW4jyfk86V%2B43RCAh6tmSKH83BOwV%2Fu9AeYKbx%2BZuk0Hx%2F5t31CL8GL7D3QOG703CxuW0fcsyxdsunnZws%2FFsA2chTl3hAPxTMMAuhc7Y9Q43QXw9rWS9hN2ti0AfrGQPGXx1xzcNtMwXNZ3HuBLLE4BH8sH%2Bpcq1VoltnxI5zF1I1bY9MZiROzeIGS92UfqT%2BeeCgX3C8GZdTFxZ9N%2FlS3O0baEBBYCGoTG8XpnUlw3WuC8lEEm8GykkyltDw1aLWsIk2b75t9DhPLIbwkDwrNN%2FaN1jmJVvPviVTD5xc8hEQuwTj9HOp4GUfgqMNqH7M4GOqUBMN%2BlU2Ru0r6kldAgKzoONg45iOHAB%2Bf5izuvVBni3P51shrAinFa5QMienTfhVIyBw1ulBV0PMA9VspK9S3hyOQoZXIc14Gx2bZ37bhXMGVNsCekVKe7OZiaCbROfEX9BS7E3kFEZY3lPnM7z0dh8i9DBAd%2BhFtKjkAkGmzkWHxKyt%2FngTUithZmf%2BjB0axrzhRSEoiPduDpt6dq4cqjTEf2CnWz&X-Amz-Signature=783c87dddc570ec122ef825234c9bf0e890898c7b4f3d534b99f46e2c7ae0c63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUEOXCFV%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPTAgGOxcLb8KUkizlj4rfXWXlEXkMIXF8eLeaYOKD%2BQIgJp%2BXe%2BRGiyQOFbMcPP1CdzADvfpKfI09Oh8p%2F8G%2BVGQq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDKrz%2BoSRp7qTNMzUIircA%2Bmr5pxQ20FrKACugDfEUvM66qVgPvOP8LSvRjZ7yGUJDqpUu%2B0qKYto4MoLFIay356lL7aRIf8Ja4nF%2B7ipJk7XKAaooR%2FvrZVXIEgW9NlwIuV8yUD0D0wWCQWk15d6eocqmQi%2FchJW8u6Lmd67FQl664IYzYvr%2B1TaTRqJwIeOpgh9iPqFDQAWeL32GepNlCnuDv%2FqTAFRQEdMMfbrMfMUDR1%2FatryWzjj5hSwWmYH6NlpL6dBYKIgGODZtY9XHnHgnzFIArTTiRBVP8MljCJQXyzE0UC6iiz54%2BXHufbXMLgVTMtVyvqcwemd9edArW4jyfk86V%2B43RCAh6tmSKH83BOwV%2Fu9AeYKbx%2BZuk0Hx%2F5t31CL8GL7D3QOG703CxuW0fcsyxdsunnZws%2FFsA2chTl3hAPxTMMAuhc7Y9Q43QXw9rWS9hN2ti0AfrGQPGXx1xzcNtMwXNZ3HuBLLE4BH8sH%2Bpcq1VoltnxI5zF1I1bY9MZiROzeIGS92UfqT%2BeeCgX3C8GZdTFxZ9N%2FlS3O0baEBBYCGoTG8XpnUlw3WuC8lEEm8GykkyltDw1aLWsIk2b75t9DhPLIbwkDwrNN%2FaN1jmJVvPviVTD5xc8hEQuwTj9HOp4GUfgqMNqH7M4GOqUBMN%2BlU2Ru0r6kldAgKzoONg45iOHAB%2Bf5izuvVBni3P51shrAinFa5QMienTfhVIyBw1ulBV0PMA9VspK9S3hyOQoZXIc14Gx2bZ37bhXMGVNsCekVKe7OZiaCbROfEX9BS7E3kFEZY3lPnM7z0dh8i9DBAd%2BhFtKjkAkGmzkWHxKyt%2FngTUithZmf%2BjB0axrzhRSEoiPduDpt6dq4cqjTEf2CnWz&X-Amz-Signature=9905550487b72353b5cdc8759e4fc7459f6e605dd18bd3904d6472be4169a0a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

