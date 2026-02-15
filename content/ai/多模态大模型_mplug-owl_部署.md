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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOMLA76Z%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDaocyb098AQInaoQwVvatPN62ujx7ifp%2FCIFgUps827AIgeNf7%2FXzRlY1ygPfwdY9ne7h%2B%2FwlWf9IY0QDo6kuqqd0q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDCgYgqfNMQVJkBF1iSrcA7vUR%2F3mOB3%2FSfvhTL1lImMd%2FQ6Z1xh50EMsliFk1OhjolrHB5kFY%2FDj17DEkapv09A2DWiLISvI9piHLFkn5Z1%2F68tHcf8iqX0U%2BMieA6uUJ7XIG1plVFnOY9UQi%2FB8Qdxyj6laHPqPOK%2F0gL2pbGSomzaOyW2finfSE6eZSRd4cyGY0RxlS5YpWm3yyg2xoXy8TbpnYlR38kGSKkUnYYMw0NnV6l30DuJngjBMZ%2BlHUPqsntoieGHfzW5FXAFlvK%2FJ3Jw714wUEAooHohJbEavLcgf6qwdESCMMX28lGoShMuTdOdg95KvhPksz5i0DeFs3MkbiSpyo7UeFu2T39e5uSEJd9M%2BUp4XbgViqge4rykojgqeHR59uBd0UQhZYXR6gmn0ndnYVNCGLcLDZK4Epgqvnox81KUkzyf8gtMJTMTMuhibvZiLX5yslsxRT0NgfBKokdF%2BlZSCqLenXDgf0nt4AirDeBJutzd%2BxWgf8um19zdQbwU%2F1HgR5xwiHqROriezQ9zjxSk%2Fya%2BUqFA1x9PWOed%2BB8eftqjMg%2Bukd4wzNYNlAfbACaEZhF%2BoOMkkLUwc5xvv7qQVSJP0jYV%2BRGw6Sa5%2BBdB3%2BljfR%2F8RAmv70gqtH3Ro2AM4MISexMwGOqUBjy1gkw1y3WlaKm55Pa6ZOs8AQfOWSsWQR1AN7J%2FdK%2FF5BtQMNdcz6wcI%2FHQGSy2W1Z98I97GNqPAaiLPV1Qf3PC9YeDxCXdyBpWi8insvMqK6hDxzy1XAgwSim%2Fbl2wCa5PEt9zANu0kVhovTOwMaFZ8YU1lwwIzrjfvxvgwIjQvMl71gDQeY1TryUiDm4F%2B5YG8D6KNNvuMYTmJOWORppiBSYdm&X-Amz-Signature=0e3fbcbd83e3cc5e42214fc5e29c68aa2eb45bc070edc23f82676b3c60501276&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOMLA76Z%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDaocyb098AQInaoQwVvatPN62ujx7ifp%2FCIFgUps827AIgeNf7%2FXzRlY1ygPfwdY9ne7h%2B%2FwlWf9IY0QDo6kuqqd0q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDCgYgqfNMQVJkBF1iSrcA7vUR%2F3mOB3%2FSfvhTL1lImMd%2FQ6Z1xh50EMsliFk1OhjolrHB5kFY%2FDj17DEkapv09A2DWiLISvI9piHLFkn5Z1%2F68tHcf8iqX0U%2BMieA6uUJ7XIG1plVFnOY9UQi%2FB8Qdxyj6laHPqPOK%2F0gL2pbGSomzaOyW2finfSE6eZSRd4cyGY0RxlS5YpWm3yyg2xoXy8TbpnYlR38kGSKkUnYYMw0NnV6l30DuJngjBMZ%2BlHUPqsntoieGHfzW5FXAFlvK%2FJ3Jw714wUEAooHohJbEavLcgf6qwdESCMMX28lGoShMuTdOdg95KvhPksz5i0DeFs3MkbiSpyo7UeFu2T39e5uSEJd9M%2BUp4XbgViqge4rykojgqeHR59uBd0UQhZYXR6gmn0ndnYVNCGLcLDZK4Epgqvnox81KUkzyf8gtMJTMTMuhibvZiLX5yslsxRT0NgfBKokdF%2BlZSCqLenXDgf0nt4AirDeBJutzd%2BxWgf8um19zdQbwU%2F1HgR5xwiHqROriezQ9zjxSk%2Fya%2BUqFA1x9PWOed%2BB8eftqjMg%2Bukd4wzNYNlAfbACaEZhF%2BoOMkkLUwc5xvv7qQVSJP0jYV%2BRGw6Sa5%2BBdB3%2BljfR%2F8RAmv70gqtH3Ro2AM4MISexMwGOqUBjy1gkw1y3WlaKm55Pa6ZOs8AQfOWSsWQR1AN7J%2FdK%2FF5BtQMNdcz6wcI%2FHQGSy2W1Z98I97GNqPAaiLPV1Qf3PC9YeDxCXdyBpWi8insvMqK6hDxzy1XAgwSim%2Fbl2wCa5PEt9zANu0kVhovTOwMaFZ8YU1lwwIzrjfvxvgwIjQvMl71gDQeY1TryUiDm4F%2B5YG8D6KNNvuMYTmJOWORppiBSYdm&X-Amz-Signature=662098c2439c0051bc80f33cfb8b23d626f2532b102c3078a90ad2bf4b4444ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

