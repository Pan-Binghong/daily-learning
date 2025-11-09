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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JQCPUFG%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDUZLWcR8tb5KFTVc8%2Fes4wAcj%2FVRZk2uplwmKe5E134AIhAMoQmVT4PtHlAMlY1DGARSmnlEFFoZed0rWpcTrUHiMIKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU6%2Fjc4iGej4rShcEq3APVnvWkTXgcDq7Z8rbHcVQDxjrQapEXOrjcgGBOthqjy88MDxxviV0MpDcWlJNzxB02VRkhU3ghQxEf%2FR8ZfxdoVQlQRcb6mi0ShtC5VUXEcq6%2FkxDXGD9j5Fy5yhDf%2FehEAd2RcQH3oKRcyEGZxlGyUzsX2CHs4HX%2BtGNU7Te3TQvM%2FjOMxt%2FIsS0Iv27OAwleFVuBur7dRE6MzrLYnB7a9R9ZOAh0tWLY6FgEN04kjqukOh5B%2BL951Yr0X2VlYTCNVNvN88qaPYbGQip1HEWGdB1%2Bt%2BctMPd0rxB%2BYyu774vD2PVhwsCuXZRf%2FHt6LdruEI6f9OiuHVU2A7Cxw1BtOKx7lulAe3DHbTlUb3IeRXhU9OMl9V6hfWDUaBsPr1pVqKrlqSt3c1ZrfHUgJVdzrM8dDFOODe0l8nr%2BCH4093KsAKPCgFyhaeH5LafGwnYc0rWF10ECp%2BdTX4x%2BGwIkZMMtwtKFae%2F9y5xm4JXczyvCtI0E1645gmaGA5Ih3SklHtHlMaNwnSejI3XxER2fpG0yDWkh1fzBGZqToGVfHj8XJyRkTovII5MJ7xvOH38cxTs7yPgAkTpzSSfUzr40E%2FkBFc9xyBF5Al2FZiw9lmkFufCL73WIoLykjTCjt7%2FIBjqkAUQT3RPgEly6S8%2BNvvrkjMcEtOr8aa2lN%2BYXv9TZxuninaPqqxN%2FieF663J%2BHBtJnQxN%2BbnIGIkgUJ%2Fysus1Dwniz%2FUX2VceGiD9YVb%2Fso5eueFlihTTvxb3GdsRYsl2qoKY6L%2BlB0S0M0CH2%2FQ86yEjyh%2FgTBEnce4%2F3YpXq5Nnv9JEaos2Da01zJ31nLOy8Y1fhJ0euSCF5tM9oA2Xr0Yg493m&X-Amz-Signature=f35d368768caf9e8699d6624e03ddfd4ea500be0e09f0da3a71c19d862cf490b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JQCPUFG%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDUZLWcR8tb5KFTVc8%2Fes4wAcj%2FVRZk2uplwmKe5E134AIhAMoQmVT4PtHlAMlY1DGARSmnlEFFoZed0rWpcTrUHiMIKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU6%2Fjc4iGej4rShcEq3APVnvWkTXgcDq7Z8rbHcVQDxjrQapEXOrjcgGBOthqjy88MDxxviV0MpDcWlJNzxB02VRkhU3ghQxEf%2FR8ZfxdoVQlQRcb6mi0ShtC5VUXEcq6%2FkxDXGD9j5Fy5yhDf%2FehEAd2RcQH3oKRcyEGZxlGyUzsX2CHs4HX%2BtGNU7Te3TQvM%2FjOMxt%2FIsS0Iv27OAwleFVuBur7dRE6MzrLYnB7a9R9ZOAh0tWLY6FgEN04kjqukOh5B%2BL951Yr0X2VlYTCNVNvN88qaPYbGQip1HEWGdB1%2Bt%2BctMPd0rxB%2BYyu774vD2PVhwsCuXZRf%2FHt6LdruEI6f9OiuHVU2A7Cxw1BtOKx7lulAe3DHbTlUb3IeRXhU9OMl9V6hfWDUaBsPr1pVqKrlqSt3c1ZrfHUgJVdzrM8dDFOODe0l8nr%2BCH4093KsAKPCgFyhaeH5LafGwnYc0rWF10ECp%2BdTX4x%2BGwIkZMMtwtKFae%2F9y5xm4JXczyvCtI0E1645gmaGA5Ih3SklHtHlMaNwnSejI3XxER2fpG0yDWkh1fzBGZqToGVfHj8XJyRkTovII5MJ7xvOH38cxTs7yPgAkTpzSSfUzr40E%2FkBFc9xyBF5Al2FZiw9lmkFufCL73WIoLykjTCjt7%2FIBjqkAUQT3RPgEly6S8%2BNvvrkjMcEtOr8aa2lN%2BYXv9TZxuninaPqqxN%2FieF663J%2BHBtJnQxN%2BbnIGIkgUJ%2Fysus1Dwniz%2FUX2VceGiD9YVb%2Fso5eueFlihTTvxb3GdsRYsl2qoKY6L%2BlB0S0M0CH2%2FQ86yEjyh%2FgTBEnce4%2F3YpXq5Nnv9JEaos2Da01zJ31nLOy8Y1fhJ0euSCF5tM9oA2Xr0Yg493m&X-Amz-Signature=c2ec92ac14c42e44d1f7bca231bfde48d43fbefd6b279dfff6c5c35c17fcff6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

