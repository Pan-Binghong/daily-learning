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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRW24574%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG8s2iC8LUemxG96Q99dcjY%2FoTQMsi2d29ukVCgSsplsAiAKmhCqVMTsDLivYciDcPUxg93afqkxnHOB0K7PWyOCDiqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTvotHhryCAGmY8IFKtwDfJaZ6vMB4I%2F9j16%2FufVXrAHz9e%2Bw1%2FFqIuJvpQOtRZMMH6ILdzmaluu5UEuG%2FK54viBDGpn%2B1Anl0DzvCt5EEUn1dO9K1WtVWQkEhojWQajmQ5HFCt8jLTSGnzoDdcaTBkJ%2BCrmT3h6%2F9UL63PLPbDEpWJaPcwOdkCTu6y2Cs0rNMEegtDU3QBe2qLujKaK2x2peA9lgRLN7%2Ff%2BspfL279JGXV7DMG1rO7YqV6vyNT3KlpnQHdsqdxPvju%2B2lXBtadbH5pNCO5kPlDMxXtizIGIQm5ja0uPdmgRINTkpj9S6bRrmAK2gJD%2BpEi8tl5J7PwpiP6ev0BwUvBzm1eiPwAt8Jpt1%2Fi%2Bbgxu0EaRXJ6oSpyuTGuFqMgPMSZTDpFUcCUGmmwon2bLFGpq36CCWfLlDPTcPLQ23eDBD63tTeEkxMBHRKmrq4XrnMhGRrZb48R2Ew4n7S9SFULx4W7GwHDNBvcVR0a3jy6PXKU3v5wCDfOYZQOFL6Wdz1pC8hVkr%2BhQjC6kj81BMxe7wtDnsNRQ7HwkznSEBNtrz9eTdJNGmVGaeINxOgDifB0ZKIa6MfTqNeWtj%2FIvwmgOSRpcjinz67u42tyXb%2F9n66iEo9Z%2FF6ahva92G3TW143Qw7fGvyAY6pgFuQ%2BX93E35pB6SRYvQpvoq5KqInv2875Yd7wW3P2%2Fc8pe6cZeObrefMZsYLukHa68UkKg%2FXbMEbQvE9a57ld7Fh9LbglKAllDe%2BZMnVjM6moCq67S9vFPgMIkIRIrs0yHCJ49p2kd41TL1yIkX2jGQasw4ICeI8u4QyG0y%2Bi7YOh0wMPF%2BhmSe8S%2Be%2F3O%2B3hgOJT4DqeIVClcxkF8yoFEFyC7Xtn6Z&X-Amz-Signature=d8c04937761396aa9d06982db3e4b7532ccd9faffaa17b9ab542b625a4cbd713&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRW24574%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG8s2iC8LUemxG96Q99dcjY%2FoTQMsi2d29ukVCgSsplsAiAKmhCqVMTsDLivYciDcPUxg93afqkxnHOB0K7PWyOCDiqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTvotHhryCAGmY8IFKtwDfJaZ6vMB4I%2F9j16%2FufVXrAHz9e%2Bw1%2FFqIuJvpQOtRZMMH6ILdzmaluu5UEuG%2FK54viBDGpn%2B1Anl0DzvCt5EEUn1dO9K1WtVWQkEhojWQajmQ5HFCt8jLTSGnzoDdcaTBkJ%2BCrmT3h6%2F9UL63PLPbDEpWJaPcwOdkCTu6y2Cs0rNMEegtDU3QBe2qLujKaK2x2peA9lgRLN7%2Ff%2BspfL279JGXV7DMG1rO7YqV6vyNT3KlpnQHdsqdxPvju%2B2lXBtadbH5pNCO5kPlDMxXtizIGIQm5ja0uPdmgRINTkpj9S6bRrmAK2gJD%2BpEi8tl5J7PwpiP6ev0BwUvBzm1eiPwAt8Jpt1%2Fi%2Bbgxu0EaRXJ6oSpyuTGuFqMgPMSZTDpFUcCUGmmwon2bLFGpq36CCWfLlDPTcPLQ23eDBD63tTeEkxMBHRKmrq4XrnMhGRrZb48R2Ew4n7S9SFULx4W7GwHDNBvcVR0a3jy6PXKU3v5wCDfOYZQOFL6Wdz1pC8hVkr%2BhQjC6kj81BMxe7wtDnsNRQ7HwkznSEBNtrz9eTdJNGmVGaeINxOgDifB0ZKIa6MfTqNeWtj%2FIvwmgOSRpcjinz67u42tyXb%2F9n66iEo9Z%2FF6ahva92G3TW143Qw7fGvyAY6pgFuQ%2BX93E35pB6SRYvQpvoq5KqInv2875Yd7wW3P2%2Fc8pe6cZeObrefMZsYLukHa68UkKg%2FXbMEbQvE9a57ld7Fh9LbglKAllDe%2BZMnVjM6moCq67S9vFPgMIkIRIrs0yHCJ49p2kd41TL1yIkX2jGQasw4ICeI8u4QyG0y%2Bi7YOh0wMPF%2BhmSe8S%2Be%2F3O%2B3hgOJT4DqeIVClcxkF8yoFEFyC7Xtn6Z&X-Amz-Signature=ae9f22b5f56e8976986b74683b8294e2bceca3a67b0aa11f8e738d5f35014108&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRW24574%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG8s2iC8LUemxG96Q99dcjY%2FoTQMsi2d29ukVCgSsplsAiAKmhCqVMTsDLivYciDcPUxg93afqkxnHOB0K7PWyOCDiqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTvotHhryCAGmY8IFKtwDfJaZ6vMB4I%2F9j16%2FufVXrAHz9e%2Bw1%2FFqIuJvpQOtRZMMH6ILdzmaluu5UEuG%2FK54viBDGpn%2B1Anl0DzvCt5EEUn1dO9K1WtVWQkEhojWQajmQ5HFCt8jLTSGnzoDdcaTBkJ%2BCrmT3h6%2F9UL63PLPbDEpWJaPcwOdkCTu6y2Cs0rNMEegtDU3QBe2qLujKaK2x2peA9lgRLN7%2Ff%2BspfL279JGXV7DMG1rO7YqV6vyNT3KlpnQHdsqdxPvju%2B2lXBtadbH5pNCO5kPlDMxXtizIGIQm5ja0uPdmgRINTkpj9S6bRrmAK2gJD%2BpEi8tl5J7PwpiP6ev0BwUvBzm1eiPwAt8Jpt1%2Fi%2Bbgxu0EaRXJ6oSpyuTGuFqMgPMSZTDpFUcCUGmmwon2bLFGpq36CCWfLlDPTcPLQ23eDBD63tTeEkxMBHRKmrq4XrnMhGRrZb48R2Ew4n7S9SFULx4W7GwHDNBvcVR0a3jy6PXKU3v5wCDfOYZQOFL6Wdz1pC8hVkr%2BhQjC6kj81BMxe7wtDnsNRQ7HwkznSEBNtrz9eTdJNGmVGaeINxOgDifB0ZKIa6MfTqNeWtj%2FIvwmgOSRpcjinz67u42tyXb%2F9n66iEo9Z%2FF6ahva92G3TW143Qw7fGvyAY6pgFuQ%2BX93E35pB6SRYvQpvoq5KqInv2875Yd7wW3P2%2Fc8pe6cZeObrefMZsYLukHa68UkKg%2FXbMEbQvE9a57ld7Fh9LbglKAllDe%2BZMnVjM6moCq67S9vFPgMIkIRIrs0yHCJ49p2kd41TL1yIkX2jGQasw4ICeI8u4QyG0y%2Bi7YOh0wMPF%2BhmSe8S%2Be%2F3O%2B3hgOJT4DqeIVClcxkF8yoFEFyC7Xtn6Z&X-Amz-Signature=dd9a42ad2be3976f115d3522aa2bba5b4e5671df9f375fc72b070b0dfcda03ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

