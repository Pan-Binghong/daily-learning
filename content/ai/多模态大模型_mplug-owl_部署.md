---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4AZIF2R%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB7mOEy4CUsJMqTzB31M%2BsQ3exRKr15Y53q6md9EavrTAiEA%2BUfOatuMPoOf9AUsPTYGjMh0JgkERNDC7Joa%2BHCJ4ZIqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdv1UNgNj7AB4dpYyrcA38TwwUDaGwBIPeX7MwDvdioJRggY10PJM%2FcXIRl%2FuLaPbrVrNMjlI7uQTiKwYFpSkijAZRATrgNufjC%2FWA%2FQnRLr3tBdjy8zcsFGtioQ7M3CQUexHGRSgKxb6WKpw4RsZblDhlJURWZAmNsWVGF7UIJENuu6T8eSMYMI2I8nGrasOGVxcTRBXAw20nyEP9wYG781zO0SXzbfMyEnj1f0QUXjA7G9qcW%2BDtaEN0GuJohL1Cep1U8PSY3bl0OhinCAp7XMCqhczj6ROAZzlUTO2clTVwI%2F3LIke0kdtlmdnE0TmU8DqTkotEyW0gBvN8%2B9OSLBmhW%2FgzQ0DIurhw94LmM06Ois3Y952xAjvFm9iTty7x6TYVHg8BDXK3%2BNTia9J1qKWg5tJyVhc3VOWeec73apt023n7eamH09yStXmYD3SHEvkLphEdRz6cE3PkAPq0WWe6XrwNZU6pKuBqru%2Bx9f2u0DmHdV%2BMDlDksNOgfzeGtbF6S4fVN4%2BGtWCprg29w8x%2FexZnStNk%2BGN8Fn9%2BV0siVaoux07JaWq1IvyfNR2xyyKefza3HYRRztxPwhAKs9dM2sgFnEA%2BHBGFT0LV9%2FmPrXenQMM8iAV%2Fpkx8k237fKhNIWPba0TIZMOaYns0GOqUBY4F1%2FLzGa3yQfbBWpIS3zH3gHmbX3ki4IND5uEtBLxXdZrZ%2F%2Bl%2FXXtv1NRD%2FT7ImaoQflkKQct2s2kPOGxVwG2IBckgtPyV%2BgCgAFSh8G13KWi6%2FoV%2B7Z7I2%2FMurNm1sJ9kr1CI8QuqRkbmx8cptsgoMoucs0nf4EilkP2rbEkuqiwajSvaM8QHt8lqHAtgRD9olRfDn653xpnwtXF1xvc1j5qOo&X-Amz-Signature=826e8e3baba24fe24faaf2950e17845de202e6dca85c2ab05320ca33f78852bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4AZIF2R%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB7mOEy4CUsJMqTzB31M%2BsQ3exRKr15Y53q6md9EavrTAiEA%2BUfOatuMPoOf9AUsPTYGjMh0JgkERNDC7Joa%2BHCJ4ZIqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdv1UNgNj7AB4dpYyrcA38TwwUDaGwBIPeX7MwDvdioJRggY10PJM%2FcXIRl%2FuLaPbrVrNMjlI7uQTiKwYFpSkijAZRATrgNufjC%2FWA%2FQnRLr3tBdjy8zcsFGtioQ7M3CQUexHGRSgKxb6WKpw4RsZblDhlJURWZAmNsWVGF7UIJENuu6T8eSMYMI2I8nGrasOGVxcTRBXAw20nyEP9wYG781zO0SXzbfMyEnj1f0QUXjA7G9qcW%2BDtaEN0GuJohL1Cep1U8PSY3bl0OhinCAp7XMCqhczj6ROAZzlUTO2clTVwI%2F3LIke0kdtlmdnE0TmU8DqTkotEyW0gBvN8%2B9OSLBmhW%2FgzQ0DIurhw94LmM06Ois3Y952xAjvFm9iTty7x6TYVHg8BDXK3%2BNTia9J1qKWg5tJyVhc3VOWeec73apt023n7eamH09yStXmYD3SHEvkLphEdRz6cE3PkAPq0WWe6XrwNZU6pKuBqru%2Bx9f2u0DmHdV%2BMDlDksNOgfzeGtbF6S4fVN4%2BGtWCprg29w8x%2FexZnStNk%2BGN8Fn9%2BV0siVaoux07JaWq1IvyfNR2xyyKefza3HYRRztxPwhAKs9dM2sgFnEA%2BHBGFT0LV9%2FmPrXenQMM8iAV%2Fpkx8k237fKhNIWPba0TIZMOaYns0GOqUBY4F1%2FLzGa3yQfbBWpIS3zH3gHmbX3ki4IND5uEtBLxXdZrZ%2F%2Bl%2FXXtv1NRD%2FT7ImaoQflkKQct2s2kPOGxVwG2IBckgtPyV%2BgCgAFSh8G13KWi6%2FoV%2B7Z7I2%2FMurNm1sJ9kr1CI8QuqRkbmx8cptsgoMoucs0nf4EilkP2rbEkuqiwajSvaM8QHt8lqHAtgRD9olRfDn653xpnwtXF1xvc1j5qOo&X-Amz-Signature=4afd1de91017bd0c4f221696a5b7fd23f678fe5e1ac22191dfbf6924e0ca7ae0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

