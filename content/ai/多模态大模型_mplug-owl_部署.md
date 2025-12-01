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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667PCJLVV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQC2QMYg4oMt0U7jiJTCZHwX8QrMjA92xSiYzkCtenc3zgIhAJBaD8bXZHXTuk8grPpHIwqW1DXeYTglsKRxYYcpgXLdKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbCQn5v38Gv3EwYywq3AOCEAIxIGaNPUDwQRj8oxX0MJ3BYw3I2WbgWWfM654dz6iW%2FSN7K7SOhYF4NKpHPMCfo%2BGyf9MZc9GAa3hkjPhsIfl5GYXqL5yn8OUuvvdPDYxawNGvWvagcOx%2FFK7yu2oMuEBdYEnzA3Hta7leIifFtxShIJmyi4FC5rUQqSw2DwxorFaQfk7NHo2rSxk36CGuGO4jZ9m2vlPTx8trkAXtYKe8cFAmVaDAK4jlyj8iuLzIcdRW2fqqqml3wlBFmqjjvkHyXh%2F8W4Kl0lFn2XA31LULRGxdDfFmuqxRKJDSizSnI3US5NaN0%2Finrrq763UxXndtva7tfaeDFsU9mAOfX3Rd8pFQYE5g2N0XF7qtxBQcVHpfethBJOJ8aCGIrp%2FzG3Ao%2BauS%2FC%2BSc1Ys909WJ5nVm7Ld9mB8jUMhAEPy09JsyIVDyUtcFucv6cXiDDMgKnbFdYKPM4bi8Yj94nJpplYmyR5nWTpHe1odI78uZbN2qSZGi1ToyCX5N9KAVtoAUPVrfwVJhgTmyCOSZA7f7UJBEx%2BrS15Y967QluPBdRy%2B%2FWO60lSMPGTgtfJwmSpcxz2zEi8WdZz%2FvPz%2FZlwFUetLZz2%2F6AwmmwcCuPBNLP7Z3gvK8%2FKfwdHwmjDl%2BbLJBjqkAR0OyN86B%2FXqg9SHpdgKegiL0%2Fw3UAA1BdC2OuEEWI7pN%2Br7b5aQhfwiOoojPZj9xhVHYtmoYhJJBDI39JIQSmZbNsEVxdSSXDVj7ZdPi2X3WQRXNNLjA0LZiFtcmxpK%2BPmFxQNTt2V0MaYOXcqNzDndm96N7u9xEub45Epx5UTNnPByqW8XR70D2GQ23io4giUulKVxPD57eGSyGWG%2B9aNtlBE4&X-Amz-Signature=0e2d998d20289fb2767b00c5c99dafcfdf875a3528e1516853f6efd5570f92ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667PCJLVV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQC2QMYg4oMt0U7jiJTCZHwX8QrMjA92xSiYzkCtenc3zgIhAJBaD8bXZHXTuk8grPpHIwqW1DXeYTglsKRxYYcpgXLdKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbCQn5v38Gv3EwYywq3AOCEAIxIGaNPUDwQRj8oxX0MJ3BYw3I2WbgWWfM654dz6iW%2FSN7K7SOhYF4NKpHPMCfo%2BGyf9MZc9GAa3hkjPhsIfl5GYXqL5yn8OUuvvdPDYxawNGvWvagcOx%2FFK7yu2oMuEBdYEnzA3Hta7leIifFtxShIJmyi4FC5rUQqSw2DwxorFaQfk7NHo2rSxk36CGuGO4jZ9m2vlPTx8trkAXtYKe8cFAmVaDAK4jlyj8iuLzIcdRW2fqqqml3wlBFmqjjvkHyXh%2F8W4Kl0lFn2XA31LULRGxdDfFmuqxRKJDSizSnI3US5NaN0%2Finrrq763UxXndtva7tfaeDFsU9mAOfX3Rd8pFQYE5g2N0XF7qtxBQcVHpfethBJOJ8aCGIrp%2FzG3Ao%2BauS%2FC%2BSc1Ys909WJ5nVm7Ld9mB8jUMhAEPy09JsyIVDyUtcFucv6cXiDDMgKnbFdYKPM4bi8Yj94nJpplYmyR5nWTpHe1odI78uZbN2qSZGi1ToyCX5N9KAVtoAUPVrfwVJhgTmyCOSZA7f7UJBEx%2BrS15Y967QluPBdRy%2B%2FWO60lSMPGTgtfJwmSpcxz2zEi8WdZz%2FvPz%2FZlwFUetLZz2%2F6AwmmwcCuPBNLP7Z3gvK8%2FKfwdHwmjDl%2BbLJBjqkAR0OyN86B%2FXqg9SHpdgKegiL0%2Fw3UAA1BdC2OuEEWI7pN%2Br7b5aQhfwiOoojPZj9xhVHYtmoYhJJBDI39JIQSmZbNsEVxdSSXDVj7ZdPi2X3WQRXNNLjA0LZiFtcmxpK%2BPmFxQNTt2V0MaYOXcqNzDndm96N7u9xEub45Epx5UTNnPByqW8XR70D2GQ23io4giUulKVxPD57eGSyGWG%2B9aNtlBE4&X-Amz-Signature=cb8d68654aaed50bed909f243d0479e0e57b22d9c78a801413c09cdee84519ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

