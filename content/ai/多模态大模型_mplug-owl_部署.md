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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GXEQIFS%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGDZsi98ndrRAI%2BFT1i3bZ2mCi19w1U5A9GYMT0AmutwIhALG5q9mcixG59nqLD9z6yNHBYVe3M2qvRoUl37CWPJ5YKv8DCFwQABoMNjM3NDIzMTgzODA1IgzK9ViZnq7CpbOvyncq3AMuHwOCeheKu0QjLvMvMI7DHTF%2Bvb7opYZ0QGalrf0ReMpwxJshrEMngRNQLU1ygfKUVyvkuwGqXpLgLF52SM1FQI07defvELIS7t%2Fxu1y%2BvcbnY6xOyJSs4NCPzv4xzkczt6h8OI%2BmARMC8IbOPYl8WMwPnz%2F69cFeKGR1Ut6sZsgm%2BsDLJPFbDI6Y7ZGEFIU7ce6BONjKzeus6H9%2Bn%2BsTHg%2B7eNctrx2i1vKDUlOEjjhHR2RjJZw79JSUe2kUjDTTgnbKX73F9OUH1FQo9%2FIJYP9sbcJoX8PGhU5F5s7kxx6OcX8XpRvg%2BGwdi205Xhd8cooaPE9I1fBnlCvLknnXEXcJJi5E1dPGTzNnPzK74%2FNkByh%2BLO%2FC69vqYH90qtXB8uLOhcJ7TD%2FDd9dsl5DY6yuCZgd8dzunHnBdTu37fSi8THAuDnTqJ4hskwVoPHDMV%2FCcCo%2FaivcrXeOvZPME1l0mYVJqJuAGq9y38cDUbFnGMzWAaUS4vJ7rps%2BckcYIuaqKVo2zjyDYPumX7Ssioxi6b5Y65Hp1nkSSt5%2B6KBOR8KjFUe7%2Fcm0uV3bZZu%2F8zMSfbC9wjCmdtTj1E5wcwtfKIaYJmzvAMm4YoXcKfeHq5puqWQb8ZQV%2BpjDJjYPKBjqkAdWmnMuBIVSUG4LGmkB4SNRJjJSMF0XulQj9NFY8uAyFRhUJlPkUwKPK2DkBaBZrtfTFZP7NhZ%2B9AMvgGvcaY1FSzpn72fc4rdH4DAN%2Fe6dj7KReXXSbQ83VEWvATtcnpGrBoVNtAkYpVS22ElfV7GPpksavk0KCGWtWZuLJu0VZV%2BfmVFbzDQL5icvu3YRoSjChUKwiMLAN2hggbcwLhB5s6OZJ&X-Amz-Signature=50f72dea043ea6d3721a80f031568d8d13690073de41c7d16011192dade94f35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GXEQIFS%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGDZsi98ndrRAI%2BFT1i3bZ2mCi19w1U5A9GYMT0AmutwIhALG5q9mcixG59nqLD9z6yNHBYVe3M2qvRoUl37CWPJ5YKv8DCFwQABoMNjM3NDIzMTgzODA1IgzK9ViZnq7CpbOvyncq3AMuHwOCeheKu0QjLvMvMI7DHTF%2Bvb7opYZ0QGalrf0ReMpwxJshrEMngRNQLU1ygfKUVyvkuwGqXpLgLF52SM1FQI07defvELIS7t%2Fxu1y%2BvcbnY6xOyJSs4NCPzv4xzkczt6h8OI%2BmARMC8IbOPYl8WMwPnz%2F69cFeKGR1Ut6sZsgm%2BsDLJPFbDI6Y7ZGEFIU7ce6BONjKzeus6H9%2Bn%2BsTHg%2B7eNctrx2i1vKDUlOEjjhHR2RjJZw79JSUe2kUjDTTgnbKX73F9OUH1FQo9%2FIJYP9sbcJoX8PGhU5F5s7kxx6OcX8XpRvg%2BGwdi205Xhd8cooaPE9I1fBnlCvLknnXEXcJJi5E1dPGTzNnPzK74%2FNkByh%2BLO%2FC69vqYH90qtXB8uLOhcJ7TD%2FDd9dsl5DY6yuCZgd8dzunHnBdTu37fSi8THAuDnTqJ4hskwVoPHDMV%2FCcCo%2FaivcrXeOvZPME1l0mYVJqJuAGq9y38cDUbFnGMzWAaUS4vJ7rps%2BckcYIuaqKVo2zjyDYPumX7Ssioxi6b5Y65Hp1nkSSt5%2B6KBOR8KjFUe7%2Fcm0uV3bZZu%2F8zMSfbC9wjCmdtTj1E5wcwtfKIaYJmzvAMm4YoXcKfeHq5puqWQb8ZQV%2BpjDJjYPKBjqkAdWmnMuBIVSUG4LGmkB4SNRJjJSMF0XulQj9NFY8uAyFRhUJlPkUwKPK2DkBaBZrtfTFZP7NhZ%2B9AMvgGvcaY1FSzpn72fc4rdH4DAN%2Fe6dj7KReXXSbQ83VEWvATtcnpGrBoVNtAkYpVS22ElfV7GPpksavk0KCGWtWZuLJu0VZV%2BfmVFbzDQL5icvu3YRoSjChUKwiMLAN2hggbcwLhB5s6OZJ&X-Amz-Signature=dca86300f6d06a9e098ca843a695c8cb5ec71f04e631d8a510d553795c2513e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

