---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662J45PCMZ%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAYukfBupwhwEDB7m6V%2BxvD8YKYBHxPqG9pgrOxye%2BLCAiBF92f467TOrapc7n2j61GWWoPA7uT2zQfenALKl5OE3iqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2Nf33IpqHGRg%2BmxrKtwD90OTEb%2Bq28QHopDulldBlF9vtAU42lLkKR8MAI8zJhB94GzHo3oi4WTLa5oYHPb321f1GYxU4xJv30UD1%2BSuSkPmuMOg%2BK4RpYLYKGzrIPbg6tcWR3oYuSVImah6QNdmpGkpMCYSWvgT6ZCdNZvZ4zhu1xOcaGocBK9vHMCL1tI78gIl3g9zvNl3GGh9Q%2BRutKh6yldIhOPY2wBzPJHP5P7W9x1ySUps21YzBgS7IATX1nsGXiGr4uWS1IqhQnnILLG%2FG8mA0%2FreYmnfoy%2B%2BTtiT5QQLnLK9Qf5AJHiaZot7iv4oihHGyQ%2F2rJhTI0lbYduttIcGFHMUA%2FENP2IepJeXPxgdqRkPdz8%2BVuw8nMMrtVPRbqiGtdCYi7h2zUQgbfLMbkjPT14oMxBhvo9p7mKBDGMwkrdeYhGZ6cCGWY%2B%2BYChun670K89XcNEV0USkGyNVubPCJw57zyxrmyTTioyfgRGdLvL6RC3towATTwuG9C8TFaQWemtsLKWyiqqcH10CwzpDf8TCYVpDpoIYem3EGP0W0BtQZZOAtrnVkf3MWwklOQUYF5Ft2%2FHFpcbWvy6bUO3r3mHT320oYsQNMRBHGlDzfGjJw1KwmfdFUnu4vHyZ2MwJKsoVIEUwh8OqzAY6pgGLiTAtS7mMGTcblRv%2BvR3GI%2FaL5iQZVLihVO%2BhxHdiaKKY1Cnssq%2FWf9QyCka3pjr%2B13H0YszIt7s5tB9phla6SXczzf6G69lK2yd75JSjo3fuoace2z6xh1WiPhLg%2F4mem3O2clbkMN6nmdkU1hVoQzLzbpYFslCNwr7H%2Fjz2FNGWPAeS5BeT8Y2fJYjPWfVL75JSb1Gqr1dyftaozkGS6QGDohKD&X-Amz-Signature=64f5bb1176383fa80d91c864e296fea4da6aef4dcbfe664368e94b75f1c3f933&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662J45PCMZ%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAYukfBupwhwEDB7m6V%2BxvD8YKYBHxPqG9pgrOxye%2BLCAiBF92f467TOrapc7n2j61GWWoPA7uT2zQfenALKl5OE3iqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2Nf33IpqHGRg%2BmxrKtwD90OTEb%2Bq28QHopDulldBlF9vtAU42lLkKR8MAI8zJhB94GzHo3oi4WTLa5oYHPb321f1GYxU4xJv30UD1%2BSuSkPmuMOg%2BK4RpYLYKGzrIPbg6tcWR3oYuSVImah6QNdmpGkpMCYSWvgT6ZCdNZvZ4zhu1xOcaGocBK9vHMCL1tI78gIl3g9zvNl3GGh9Q%2BRutKh6yldIhOPY2wBzPJHP5P7W9x1ySUps21YzBgS7IATX1nsGXiGr4uWS1IqhQnnILLG%2FG8mA0%2FreYmnfoy%2B%2BTtiT5QQLnLK9Qf5AJHiaZot7iv4oihHGyQ%2F2rJhTI0lbYduttIcGFHMUA%2FENP2IepJeXPxgdqRkPdz8%2BVuw8nMMrtVPRbqiGtdCYi7h2zUQgbfLMbkjPT14oMxBhvo9p7mKBDGMwkrdeYhGZ6cCGWY%2B%2BYChun670K89XcNEV0USkGyNVubPCJw57zyxrmyTTioyfgRGdLvL6RC3towATTwuG9C8TFaQWemtsLKWyiqqcH10CwzpDf8TCYVpDpoIYem3EGP0W0BtQZZOAtrnVkf3MWwklOQUYF5Ft2%2FHFpcbWvy6bUO3r3mHT320oYsQNMRBHGlDzfGjJw1KwmfdFUnu4vHyZ2MwJKsoVIEUwh8OqzAY6pgGLiTAtS7mMGTcblRv%2BvR3GI%2FaL5iQZVLihVO%2BhxHdiaKKY1Cnssq%2FWf9QyCka3pjr%2B13H0YszIt7s5tB9phla6SXczzf6G69lK2yd75JSjo3fuoace2z6xh1WiPhLg%2F4mem3O2clbkMN6nmdkU1hVoQzLzbpYFslCNwr7H%2Fjz2FNGWPAeS5BeT8Y2fJYjPWfVL75JSb1Gqr1dyftaozkGS6QGDohKD&X-Amz-Signature=68548e0a22a3ce2eb4b5bb1cda65b69be15cecf15eb8b5cfeae83d10688b9175&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



