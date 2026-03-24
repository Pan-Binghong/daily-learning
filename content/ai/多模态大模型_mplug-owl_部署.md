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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WODAC3HR%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDci7y1jszzU7mWyg3a2%2Bxu19UWBJ%2FpaLNjqa8DnuwGAAiEA59nLk%2Bqd5BjnGMdLse5CrwUno799x5CZaUgTNPLaia8qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHHCct%2Fz6f8U2wjJ4CrcA1lNcgLk79wj3i6OdKHfAATQEd0d2d6Y6XWwApV5Z0b1QcUZwFl1TLY04KDoWrKbQQZ4R7cOYdpu%2BLNllsIw333NkGfVmZXhJ8cRZZVknZEf2DL6%2BVdrwaKVzSr4F4mef1USMJR85lYqh6ilP50imMigiwkQD6uM1J1HKRDAqze7isrI96E%2FaKJ6pg7gJDxcLSmOz%2FoCaqR3%2BrTgFW7FNC2k0aSrpBfde2Asifxz8ecEXqib6Tv%2FivFdxF8TUHyMhzxZwiKowOanj1xz5oGYX9hZ2XBGfell6kBX6aqDIp7jHvzD2YFL63%2FwUCDuevs4gtrwsPBwsm6tGdKyAwGwZcWRLD3h4y8fprYDIwh1SlEaSJ2xAc6eq3CaHV4pU9OCuhyLHVX6AjinA%2BrVICeBlmEFSESIAt5445LgG6PyOfb7Mqy8yJCNHaVhc7p7Q9M%2BiPDyyql6dCRYRfFjs5AJu%2FRRudP0HkcvUTT4lwuiNg5ziocxg%2Fb7wkJSNIGS75snsRsEu1LyOy30NUsGS410AJO%2FjEIXaKeePgqP1L%2FRb5q6j0Gjca89T1aMfwR7fRE32tiKCoPaD21Zr5ghW32HI0NclGiAfTwzuSsAunrgVMD%2BSQS0YgGgnc4DxGPtMLX0h84GOqUB7rtJp1xH6Ipde9FdGJT%2F3aoqYYy6aIjyLpBNnyDR2YNB0XVdCwiN0xsQED3O8%2FGlSBpU9mddCek4V63DOUdhlZcui9Tr6tuh2EeGFEnjTOYkAtSacZAZ4D0J8xker4K1u8bu5XIK2xMv%2FvdNK6oSzLyCP17EicMykWNn4oh5YYJiIva1HhiDl4bBN4uasm151gbACcr96iQLC698LMHY8x6I5DmN&X-Amz-Signature=0c53da95d79dd37b6eb3cb593fe131e141ed46671b50763ac7aaecffdcab8e21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WODAC3HR%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDci7y1jszzU7mWyg3a2%2Bxu19UWBJ%2FpaLNjqa8DnuwGAAiEA59nLk%2Bqd5BjnGMdLse5CrwUno799x5CZaUgTNPLaia8qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHHCct%2Fz6f8U2wjJ4CrcA1lNcgLk79wj3i6OdKHfAATQEd0d2d6Y6XWwApV5Z0b1QcUZwFl1TLY04KDoWrKbQQZ4R7cOYdpu%2BLNllsIw333NkGfVmZXhJ8cRZZVknZEf2DL6%2BVdrwaKVzSr4F4mef1USMJR85lYqh6ilP50imMigiwkQD6uM1J1HKRDAqze7isrI96E%2FaKJ6pg7gJDxcLSmOz%2FoCaqR3%2BrTgFW7FNC2k0aSrpBfde2Asifxz8ecEXqib6Tv%2FivFdxF8TUHyMhzxZwiKowOanj1xz5oGYX9hZ2XBGfell6kBX6aqDIp7jHvzD2YFL63%2FwUCDuevs4gtrwsPBwsm6tGdKyAwGwZcWRLD3h4y8fprYDIwh1SlEaSJ2xAc6eq3CaHV4pU9OCuhyLHVX6AjinA%2BrVICeBlmEFSESIAt5445LgG6PyOfb7Mqy8yJCNHaVhc7p7Q9M%2BiPDyyql6dCRYRfFjs5AJu%2FRRudP0HkcvUTT4lwuiNg5ziocxg%2Fb7wkJSNIGS75snsRsEu1LyOy30NUsGS410AJO%2FjEIXaKeePgqP1L%2FRb5q6j0Gjca89T1aMfwR7fRE32tiKCoPaD21Zr5ghW32HI0NclGiAfTwzuSsAunrgVMD%2BSQS0YgGgnc4DxGPtMLX0h84GOqUB7rtJp1xH6Ipde9FdGJT%2F3aoqYYy6aIjyLpBNnyDR2YNB0XVdCwiN0xsQED3O8%2FGlSBpU9mddCek4V63DOUdhlZcui9Tr6tuh2EeGFEnjTOYkAtSacZAZ4D0J8xker4K1u8bu5XIK2xMv%2FvdNK6oSzLyCP17EicMykWNn4oh5YYJiIva1HhiDl4bBN4uasm151gbACcr96iQLC698LMHY8x6I5DmN&X-Amz-Signature=81b462678f4b62dbc34f20c64c54d7673fb3ec3975c52f9ea25f24e0f0d4a400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

