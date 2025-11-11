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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V35S244M%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIB2ItRSkXWA1WUNPiRkmD%2Bgm9lakHYgGJ4U%2FPB%2B4%2BXJBAiBs9yN%2BrnEoaO4lbgk7Nm1L2dS9O8SQLSJ7DErtRSlX3Sr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIM%2FEsInr%2F4GGN5NuDyKtwDt4h%2FCpDTXX7cKMZilqRM7c%2FFKFbGQhOa9DGGZKM578fPcOs5D5Pra7CxGVuraZwYNkvOUyufyt0yQU4p%2BPTAP%2FIMAED5ZGF52OAEP6RIxsdNfIkwPWDUEHb4IAg4qfvszi6LPcIkIcT0HJuXwjIzSOjuFm1mWLGdURj86otI1o9PDXMB0%2FRN45B8cTO04gDLNfqiZfHxD6c4mjIO7c1Pq6NYj6uVTOBrkamAmqF3phg5ojbiNmO1kJqXJwM72FvQ3RdElmuwrF9QAviVlu5sWFQ%2FUTShnH0rNomp7GRokqakrEdd8UpiHN8Wvjg2wxqwB%2BaJxRyREKYvOxhLs%2BII4zI8DRV7wF3OtNCa1BBlMeY91bro89NaQBcCyE%2BdEYo5Lq98Rggq5raSpv%2FHTEU6gRK8z6E6vdXA%2FpTK8JuhpfiPWnWO35Gir%2F4wZ42LH2lpWl5m4H4%2Fe%2FEWpyrIUtG8hHd5L3uHBlIu1Dw1JcHQFs7pPGHGGTzIGO5iiBWhNjdPwfW2hjHpOxYqB2j4Bki%2F7EhEuTU7XKUYuf%2FiBHxjGu3a33u1xEXcqeEI5zdnNYI02uJHT9hZyzf0wvJ0X5jcBCrYregkV0%2BNadDfWPiyHOrzB846GcDtGv6lswMwwb3KyAY6pgF6OKJDL9YUC1k%2BXF8I%2BNfkicvgNQL2HeH1JfUuJqAoYnzBbTkbNxbmOicUwDiOfjl47ltPVxa5ZSUWTqJhFgcNJ%2B48VPvITNsb39JnOGAraf1MkI4iDUPC8KZhvJBTq32tzrWrsBSaeLpgz9DHgg0%2FJMbt8JCsEQz3gd5mRFP4ccM4ZPOArPjgcqjX%2FwPPliu6ywldiAomn%2Fy2h4UH83l8Ln47tlHD&X-Amz-Signature=d945b9983353ed6b3c62ca6f936d8fde60bfceb3b5f879718233d47059f748e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V35S244M%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIB2ItRSkXWA1WUNPiRkmD%2Bgm9lakHYgGJ4U%2FPB%2B4%2BXJBAiBs9yN%2BrnEoaO4lbgk7Nm1L2dS9O8SQLSJ7DErtRSlX3Sr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIM%2FEsInr%2F4GGN5NuDyKtwDt4h%2FCpDTXX7cKMZilqRM7c%2FFKFbGQhOa9DGGZKM578fPcOs5D5Pra7CxGVuraZwYNkvOUyufyt0yQU4p%2BPTAP%2FIMAED5ZGF52OAEP6RIxsdNfIkwPWDUEHb4IAg4qfvszi6LPcIkIcT0HJuXwjIzSOjuFm1mWLGdURj86otI1o9PDXMB0%2FRN45B8cTO04gDLNfqiZfHxD6c4mjIO7c1Pq6NYj6uVTOBrkamAmqF3phg5ojbiNmO1kJqXJwM72FvQ3RdElmuwrF9QAviVlu5sWFQ%2FUTShnH0rNomp7GRokqakrEdd8UpiHN8Wvjg2wxqwB%2BaJxRyREKYvOxhLs%2BII4zI8DRV7wF3OtNCa1BBlMeY91bro89NaQBcCyE%2BdEYo5Lq98Rggq5raSpv%2FHTEU6gRK8z6E6vdXA%2FpTK8JuhpfiPWnWO35Gir%2F4wZ42LH2lpWl5m4H4%2Fe%2FEWpyrIUtG8hHd5L3uHBlIu1Dw1JcHQFs7pPGHGGTzIGO5iiBWhNjdPwfW2hjHpOxYqB2j4Bki%2F7EhEuTU7XKUYuf%2FiBHxjGu3a33u1xEXcqeEI5zdnNYI02uJHT9hZyzf0wvJ0X5jcBCrYregkV0%2BNadDfWPiyHOrzB846GcDtGv6lswMwwb3KyAY6pgF6OKJDL9YUC1k%2BXF8I%2BNfkicvgNQL2HeH1JfUuJqAoYnzBbTkbNxbmOicUwDiOfjl47ltPVxa5ZSUWTqJhFgcNJ%2B48VPvITNsb39JnOGAraf1MkI4iDUPC8KZhvJBTq32tzrWrsBSaeLpgz9DHgg0%2FJMbt8JCsEQz3gd5mRFP4ccM4ZPOArPjgcqjX%2FwPPliu6ywldiAomn%2Fy2h4UH83l8Ln47tlHD&X-Amz-Signature=5ee16c8cca45a2a2999c6da2686c3b60d9d7a126e8dd0edb574d93bd1788153d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

