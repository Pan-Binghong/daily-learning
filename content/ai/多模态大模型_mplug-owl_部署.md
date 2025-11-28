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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XDLASFG%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEuWjxOKVPR32gpGJl3E9ZIoPgka5D0gpXLhGtW%2BJd9%2BAiEA%2FPnn9SEcAorgjoyHdmw3tnaYaxOWYd8YYv44X9Za%2FjQqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7jd%2Fxd3H78m1QXMSrcAwWSn52sbnxEAYUwmt7dVmXQYRbaoQir63rRdvEjcbtFT%2FsiZ%2BKH1covmCR4tAhHe%2B5P%2FWm9Te%2BlUxMj4GlSEQ0FtIsdrY8ihsjFDaVPCKVdwKZJZ7th1AwNHmKUa54W0GueSJnwHmU%2BBgd91K7tSJb6lQSaaOLOu0YDBV%2F5e00lezYmCGvI6CBNoxNTkRXnmk5u8%2FNrVG70t1RB5NDLFsg2BM4QJXq%2FEtDWRQApwhf6EqHOgKHqgNZcvX5ffCn6spHLr0VN4tcKmca8OPr%2FBloCN5W4jc5jUGewA7XnAbmRhliOZYt1S5tqdr6KOKvqNvaBofuqGNaxZsZpmqG0%2FunqbDbXwB7MvuWMMKYGuJ2WX3N4j2o0CPuliCxfOVrDa5sN05lg%2BFxdJFyq1r9WaeNUgsWSp%2BVMmKkwjVmPvUCdAgZ2Y5zhLsvqCvbPjQQF%2BO%2FHmgX9rGhGBotACdXyvJ9yyfHa9LdlO0dRfU7xYqsNBuqehjI1GIHiELA2SkebJ%2Bb3%2FchprF3z%2BTuh6Az3eDjyiX2Wq4m263Y23lPlqtgDiGrPGOKnuDDKCLs%2F4jKi%2B5GhVr2nOQnibWCwv0hyQgBfCfsMqK0N32EznX%2BRr6iglesAsKbYXSkKWsUVMIn0o8kGOqUBcGHtPOY5tc0%2Bmk8T1N9y4DuA2FdPAcOZpQr5BlGyk98%2B0s2wuzH%2B3McUgJs3rabZqg5ND0DGY%2BTEXhXnebay56Xc1aBdT0ySPA7mFo56kwUazPUvBH0ccYZ%2B0pXOLAjB%2FhplpZDHxXAMsAyHqJUZ%2BvmbsQ3NCn3R6PbjVFk0NUbuYnpxz7tcJdy5ciQJJkci1m9pKa%2BuN%2ByQQVqSnzkpcRHaYExC&X-Amz-Signature=537b59c564c9e1b02fcbbff2d07d5a7f5ea35ee3f2f6b1e35a225273e7d301b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XDLASFG%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEuWjxOKVPR32gpGJl3E9ZIoPgka5D0gpXLhGtW%2BJd9%2BAiEA%2FPnn9SEcAorgjoyHdmw3tnaYaxOWYd8YYv44X9Za%2FjQqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7jd%2Fxd3H78m1QXMSrcAwWSn52sbnxEAYUwmt7dVmXQYRbaoQir63rRdvEjcbtFT%2FsiZ%2BKH1covmCR4tAhHe%2B5P%2FWm9Te%2BlUxMj4GlSEQ0FtIsdrY8ihsjFDaVPCKVdwKZJZ7th1AwNHmKUa54W0GueSJnwHmU%2BBgd91K7tSJb6lQSaaOLOu0YDBV%2F5e00lezYmCGvI6CBNoxNTkRXnmk5u8%2FNrVG70t1RB5NDLFsg2BM4QJXq%2FEtDWRQApwhf6EqHOgKHqgNZcvX5ffCn6spHLr0VN4tcKmca8OPr%2FBloCN5W4jc5jUGewA7XnAbmRhliOZYt1S5tqdr6KOKvqNvaBofuqGNaxZsZpmqG0%2FunqbDbXwB7MvuWMMKYGuJ2WX3N4j2o0CPuliCxfOVrDa5sN05lg%2BFxdJFyq1r9WaeNUgsWSp%2BVMmKkwjVmPvUCdAgZ2Y5zhLsvqCvbPjQQF%2BO%2FHmgX9rGhGBotACdXyvJ9yyfHa9LdlO0dRfU7xYqsNBuqehjI1GIHiELA2SkebJ%2Bb3%2FchprF3z%2BTuh6Az3eDjyiX2Wq4m263Y23lPlqtgDiGrPGOKnuDDKCLs%2F4jKi%2B5GhVr2nOQnibWCwv0hyQgBfCfsMqK0N32EznX%2BRr6iglesAsKbYXSkKWsUVMIn0o8kGOqUBcGHtPOY5tc0%2Bmk8T1N9y4DuA2FdPAcOZpQr5BlGyk98%2B0s2wuzH%2B3McUgJs3rabZqg5ND0DGY%2BTEXhXnebay56Xc1aBdT0ySPA7mFo56kwUazPUvBH0ccYZ%2B0pXOLAjB%2FhplpZDHxXAMsAyHqJUZ%2BvmbsQ3NCn3R6PbjVFk0NUbuYnpxz7tcJdy5ciQJJkci1m9pKa%2BuN%2ByQQVqSnzkpcRHaYExC&X-Amz-Signature=0af9f1240113c34800c9819e8890d9b69e0026107848d2de016f9200692ba0de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

