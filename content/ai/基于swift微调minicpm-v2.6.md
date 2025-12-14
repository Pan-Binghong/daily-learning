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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662PNULFM%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIFG8lz3jMsW%2FROJfuoCTiq8s6Fhy8%2BXFzEUSTAw1eD9iAiBwFPC4VjXxhLXUCBgY7N2qj25Xl4%2Fj8CTtuQ6sMcodGyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMN6Qwg40z7UatBB9sKtwDAyNl9XBBF1%2FQwlfFGkzaqieBDi7104ATmqwSj3iVzQoCzTSS1KXnX5%2FpVtFXNCljkHbwhPmJpxC%2FvPbmjs00BzNUMNXPjeaSUOMklWP59TRuZQ4fC3s5eVuvkLR3czw6smhTtNbW9ZwfV%2Fdxmzac%2FQ5cyjD85OzqzphNCB7Z7ner7SiC1MpeUEx%2FtJLgQ5Og5tiKe970AlTmdtBz%2FAp5JM%2B0OCx%2BVS%2FebufeI%2FNDVRmoOdjabNHzAd9QucgVYei0bnAYkgx2MPJroz%2FJoHRKgCWcaw1Qacx%2BAf0wvQjOU4pcV2WwMndANKmQYsGhUdwheMvdizmhb5IigV5bYEoRizoNKNED1faCedULucxBj5RzZ1%2F3FG56%2B3JuIsr90KBw9Bns7zHnZfvUZYO2TD15Kza9%2F2Gn5GJIRFMnavIKTaGjN7Ac6igEcOVH%2F2L5XtGQBj2GalDWCuBGDJZTju%2F9FM8ON7fJpnDea1%2FCQ2gcakNlj59PpgTSK5fmEw9fiWzyMKzvqFDvda5IPfwR8riv9Hu7rV4zyqV3TPlN5SI8Xnm1ywkBbbwAThyrVw58Wlxd5eAIFwU1XLgol%2Fd8Tu2TZ0bojWeAK%2FOx4KucLkImhohAaIBS0f%2B3lsDz0mIw%2FK%2F4yQY6pgHsZZ57AYrnUJnaExL6%2Bbo7o4Oz5tXNlNeS7QBUz%2FoBRTW7P7LzKl8mw4nT%2BHj8qeIwSom%2BomozXnjpcZAhjKbHbEF8wy5rGfJVIX%2F930JXGSvNLutS6sp40R%2FCi9qzSPkbSiYoWsgp8m2snxWhIh7cMpc1a0Z4BWZXktuyAhw3QVIdGwPxppgyCistj8eFYBfP8aXQuMVnOgZce830BIcFXxyKFT2r&X-Amz-Signature=f92c95f81c19d9d150d295ee5f3ae947237266c1b9a058de6c86887052623b1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662PNULFM%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIFG8lz3jMsW%2FROJfuoCTiq8s6Fhy8%2BXFzEUSTAw1eD9iAiBwFPC4VjXxhLXUCBgY7N2qj25Xl4%2Fj8CTtuQ6sMcodGyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMN6Qwg40z7UatBB9sKtwDAyNl9XBBF1%2FQwlfFGkzaqieBDi7104ATmqwSj3iVzQoCzTSS1KXnX5%2FpVtFXNCljkHbwhPmJpxC%2FvPbmjs00BzNUMNXPjeaSUOMklWP59TRuZQ4fC3s5eVuvkLR3czw6smhTtNbW9ZwfV%2Fdxmzac%2FQ5cyjD85OzqzphNCB7Z7ner7SiC1MpeUEx%2FtJLgQ5Og5tiKe970AlTmdtBz%2FAp5JM%2B0OCx%2BVS%2FebufeI%2FNDVRmoOdjabNHzAd9QucgVYei0bnAYkgx2MPJroz%2FJoHRKgCWcaw1Qacx%2BAf0wvQjOU4pcV2WwMndANKmQYsGhUdwheMvdizmhb5IigV5bYEoRizoNKNED1faCedULucxBj5RzZ1%2F3FG56%2B3JuIsr90KBw9Bns7zHnZfvUZYO2TD15Kza9%2F2Gn5GJIRFMnavIKTaGjN7Ac6igEcOVH%2F2L5XtGQBj2GalDWCuBGDJZTju%2F9FM8ON7fJpnDea1%2FCQ2gcakNlj59PpgTSK5fmEw9fiWzyMKzvqFDvda5IPfwR8riv9Hu7rV4zyqV3TPlN5SI8Xnm1ywkBbbwAThyrVw58Wlxd5eAIFwU1XLgol%2Fd8Tu2TZ0bojWeAK%2FOx4KucLkImhohAaIBS0f%2B3lsDz0mIw%2FK%2F4yQY6pgHsZZ57AYrnUJnaExL6%2Bbo7o4Oz5tXNlNeS7QBUz%2FoBRTW7P7LzKl8mw4nT%2BHj8qeIwSom%2BomozXnjpcZAhjKbHbEF8wy5rGfJVIX%2F930JXGSvNLutS6sp40R%2FCi9qzSPkbSiYoWsgp8m2snxWhIh7cMpc1a0Z4BWZXktuyAhw3QVIdGwPxppgyCistj8eFYBfP8aXQuMVnOgZce830BIcFXxyKFT2r&X-Amz-Signature=a1b7bb26702ee05a8df9e816d2a8b76cf9cde6b3e650287c9be4598ef2b63196&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662PNULFM%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIFG8lz3jMsW%2FROJfuoCTiq8s6Fhy8%2BXFzEUSTAw1eD9iAiBwFPC4VjXxhLXUCBgY7N2qj25Xl4%2Fj8CTtuQ6sMcodGyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMN6Qwg40z7UatBB9sKtwDAyNl9XBBF1%2FQwlfFGkzaqieBDi7104ATmqwSj3iVzQoCzTSS1KXnX5%2FpVtFXNCljkHbwhPmJpxC%2FvPbmjs00BzNUMNXPjeaSUOMklWP59TRuZQ4fC3s5eVuvkLR3czw6smhTtNbW9ZwfV%2Fdxmzac%2FQ5cyjD85OzqzphNCB7Z7ner7SiC1MpeUEx%2FtJLgQ5Og5tiKe970AlTmdtBz%2FAp5JM%2B0OCx%2BVS%2FebufeI%2FNDVRmoOdjabNHzAd9QucgVYei0bnAYkgx2MPJroz%2FJoHRKgCWcaw1Qacx%2BAf0wvQjOU4pcV2WwMndANKmQYsGhUdwheMvdizmhb5IigV5bYEoRizoNKNED1faCedULucxBj5RzZ1%2F3FG56%2B3JuIsr90KBw9Bns7zHnZfvUZYO2TD15Kza9%2F2Gn5GJIRFMnavIKTaGjN7Ac6igEcOVH%2F2L5XtGQBj2GalDWCuBGDJZTju%2F9FM8ON7fJpnDea1%2FCQ2gcakNlj59PpgTSK5fmEw9fiWzyMKzvqFDvda5IPfwR8riv9Hu7rV4zyqV3TPlN5SI8Xnm1ywkBbbwAThyrVw58Wlxd5eAIFwU1XLgol%2Fd8Tu2TZ0bojWeAK%2FOx4KucLkImhohAaIBS0f%2B3lsDz0mIw%2FK%2F4yQY6pgHsZZ57AYrnUJnaExL6%2Bbo7o4Oz5tXNlNeS7QBUz%2FoBRTW7P7LzKl8mw4nT%2BHj8qeIwSom%2BomozXnjpcZAhjKbHbEF8wy5rGfJVIX%2F930JXGSvNLutS6sp40R%2FCi9qzSPkbSiYoWsgp8m2snxWhIh7cMpc1a0Z4BWZXktuyAhw3QVIdGwPxppgyCistj8eFYBfP8aXQuMVnOgZce830BIcFXxyKFT2r&X-Amz-Signature=5ad876a81e5fe4b23928e1224aa5c28c2847bb29b4efe6b3f5eb2cd4bb5c84ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

