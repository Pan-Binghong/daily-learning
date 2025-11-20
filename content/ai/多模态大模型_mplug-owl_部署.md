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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DI77I6P%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDZjetNo1fRnDuOqu2qPK0VTjpEGHAKHQLAmGWLZ2TFzwIhAPLs%2FoNeebRXaqwTRC2CXL9EnrqUZ2NutwO%2B0aX9b4NJKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlpZE32rOVAi29RQoq3AMFBIdMaXpW3TusFqDKfhmVvFjKaSEtCgfQxygVkIrNdKUm%2B%2FaYi43DcZvYVaCZrxs0eY2t9V%2B113Rvfox5ySZZj%2FY6%2BZx4k7%2Fu1%2BrxSm%2FbhaD0tmeJwy0Sd8mowbr2VradAZi3%2B7OeAfSP%2B%2B7nJuXhjaDxtNeyHpw1TGSRcAe3zda5Z2ryQsOcvs4dHoOoaKCZ9e8AFhgqwcyKI1p8ncE1QQR46bwSV8b%2Fnet%2FPbsDE8MpxNxhrUA76GknQZWSBjbOBTgP6GQ%2Fa5snJY0FXjdSG5fKYPhIkbtxgxA09fd2AFR6EusrzQpYOiSCiHmn3uEPrCsPkBjT%2BFVLpFduZD8BDYOiDl3YYJIqsyWkJ%2Boou62eFNIK36TZN4GRxVVIVtUd1aO2yMx0dV4agdrrYwa%2F4nKbJyUqMnApqBFCW67BAxayOtuV6jq%2BtIVd2Gv6G3b%2FGiV3EliIg%2B80xGKasEECS%2BEkRzpn3iYTaVBNRiNj3wSqpWZ8mKVePBo11ndJ8XaVnl1%2BApQbCj9MJ6OLXmpvmLmhB3MyxBhajrfCouCNEIAQbFYd6wzcqPOVF7IBNS2CywDv%2B2%2FXQWH5FVcthbv%2BuKvsgyrMwxV5obWDdPdoAPIAG0kAfHkO7oNFGTDo6vnIBjqkAXG8zoOS%2BhsFIJwidVQO8N%2B9bmFI%2FAqYfPNWrDwwvoqHTh57jdNx1mgmvkORkad%2BlKEnxzNej%2BCtthhCZuKgzHAEbTEWCdHnpDqyWJ2gdHnyBh1DqKLsYsC8jw0CT4AJppzL0Qi8lMLx8p1AB%2FTWd%2FbM0F9Zr5seylopHhkZQ4gOaBESjYRlOuR7FVQZXrehM9y3f9jJxNHnlwwVx6u0oD5W5jih&X-Amz-Signature=8a000392f838f524eaa3f68647fd73a01504716be470eb8f2842947a96a71b16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DI77I6P%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDZjetNo1fRnDuOqu2qPK0VTjpEGHAKHQLAmGWLZ2TFzwIhAPLs%2FoNeebRXaqwTRC2CXL9EnrqUZ2NutwO%2B0aX9b4NJKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlpZE32rOVAi29RQoq3AMFBIdMaXpW3TusFqDKfhmVvFjKaSEtCgfQxygVkIrNdKUm%2B%2FaYi43DcZvYVaCZrxs0eY2t9V%2B113Rvfox5ySZZj%2FY6%2BZx4k7%2Fu1%2BrxSm%2FbhaD0tmeJwy0Sd8mowbr2VradAZi3%2B7OeAfSP%2B%2B7nJuXhjaDxtNeyHpw1TGSRcAe3zda5Z2ryQsOcvs4dHoOoaKCZ9e8AFhgqwcyKI1p8ncE1QQR46bwSV8b%2Fnet%2FPbsDE8MpxNxhrUA76GknQZWSBjbOBTgP6GQ%2Fa5snJY0FXjdSG5fKYPhIkbtxgxA09fd2AFR6EusrzQpYOiSCiHmn3uEPrCsPkBjT%2BFVLpFduZD8BDYOiDl3YYJIqsyWkJ%2Boou62eFNIK36TZN4GRxVVIVtUd1aO2yMx0dV4agdrrYwa%2F4nKbJyUqMnApqBFCW67BAxayOtuV6jq%2BtIVd2Gv6G3b%2FGiV3EliIg%2B80xGKasEECS%2BEkRzpn3iYTaVBNRiNj3wSqpWZ8mKVePBo11ndJ8XaVnl1%2BApQbCj9MJ6OLXmpvmLmhB3MyxBhajrfCouCNEIAQbFYd6wzcqPOVF7IBNS2CywDv%2B2%2FXQWH5FVcthbv%2BuKvsgyrMwxV5obWDdPdoAPIAG0kAfHkO7oNFGTDo6vnIBjqkAXG8zoOS%2BhsFIJwidVQO8N%2B9bmFI%2FAqYfPNWrDwwvoqHTh57jdNx1mgmvkORkad%2BlKEnxzNej%2BCtthhCZuKgzHAEbTEWCdHnpDqyWJ2gdHnyBh1DqKLsYsC8jw0CT4AJppzL0Qi8lMLx8p1AB%2FTWd%2FbM0F9Zr5seylopHhkZQ4gOaBESjYRlOuR7FVQZXrehM9y3f9jJxNHnlwwVx6u0oD5W5jih&X-Amz-Signature=881be7fb9f437fa2f4eeba57fdcf78f4efabb0655d522d31c64a2205b37937b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

