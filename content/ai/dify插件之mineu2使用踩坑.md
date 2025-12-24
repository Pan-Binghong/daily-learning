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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4BBHTLI%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCGt0ESdYEPy9RasaUHrX1%2BfxiNd43nEGvjagaJ3TvgcwIgX%2F%2FPkO7%2B5y8rsXdkKGUcmhXZhHDFO6fhii9S0kNT89Uq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDGzo5emVB6XlXFdjYircA4hCPfdigSSKIDbRtpXgD9q1PjM3BroAziYEpjoiyLLf9WeZeX5j5Qk%2Bhy5NozZpTQFtA9RsaWNW5M1DHRoDZ9pRY3utx%2Fr%2BrExzGC3MqrqNhDHQ%2B7IhLuJOOnFOfpuWmmhPI4Xvnj4GnQkISiMqctnos2D81nZrdyUopxXu9Bg0m%2BBGydRHKoMV7tjAtwYqSntbKOjkgspbpMYFaCEoVPuHTgiAvS8Ns0jOID2ZGkLT1wgQUF9nZ8tnLsENRf0pImq6knypIIVuyTFOz348hsN9ByC2NnQ82PGTUSX6n9eFrekaXEJ62KvJP9Lx5HkTQ1poHhgnBDQuYfVR%2BZux9RBnDN%2B2qL%2FaK%2B2uKAAlF%2B%2B9OLGFTnnXGInSmdgqyoqc1S8y3OamvGDzW%2FQmnBMa24MJzmF4WpxMD%2FGPRzMvaDyhfBpdc93u2jtll6mNtYjSnx3tIO3AjU7sax3Pkg7KRz1EyVdt7vUdyy2lr3F3cEmFKdkDAeu0Gc%2BZKcsbnmnk%2BzPaSvFLuiwIlOEYD46oZnN2fUqEk9xpFfnBONXfaXNwzXaVbWkeFFSa6a%2BzfKHyeO%2BdFrMWjhRJVD5WEN1oQ%2B0qh3V9Udsh5YhIDstLEvNuCQsIbWwhnLnx0XjUMK3hrMoGOqUBiaUGLLz4xY14OCRYKEddhSve%2FJXWvc8moCFCbfvKg1zwQeJSdjxd3DMfO9vSl9RTFdnCy1ZFILv4BBkZocL1NsnJB4pM8eHPWDwmxAJS0zjFgEruoDyPUYfnoF8V%2Fem5ZFBsfBydsm1CxPzsWCLLThk7U3qlg0BYxGB9XUykUZ7Y2khtGAjii9hss%2FK5oB3zr97XsZ7JEqt%2BbXMCZC1HDmrwghGA&X-Amz-Signature=799d34cde716fed429a6c43c02fee75c87ba5db09e4e84502f53c7aa015ecf57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4BBHTLI%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCGt0ESdYEPy9RasaUHrX1%2BfxiNd43nEGvjagaJ3TvgcwIgX%2F%2FPkO7%2B5y8rsXdkKGUcmhXZhHDFO6fhii9S0kNT89Uq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDGzo5emVB6XlXFdjYircA4hCPfdigSSKIDbRtpXgD9q1PjM3BroAziYEpjoiyLLf9WeZeX5j5Qk%2Bhy5NozZpTQFtA9RsaWNW5M1DHRoDZ9pRY3utx%2Fr%2BrExzGC3MqrqNhDHQ%2B7IhLuJOOnFOfpuWmmhPI4Xvnj4GnQkISiMqctnos2D81nZrdyUopxXu9Bg0m%2BBGydRHKoMV7tjAtwYqSntbKOjkgspbpMYFaCEoVPuHTgiAvS8Ns0jOID2ZGkLT1wgQUF9nZ8tnLsENRf0pImq6knypIIVuyTFOz348hsN9ByC2NnQ82PGTUSX6n9eFrekaXEJ62KvJP9Lx5HkTQ1poHhgnBDQuYfVR%2BZux9RBnDN%2B2qL%2FaK%2B2uKAAlF%2B%2B9OLGFTnnXGInSmdgqyoqc1S8y3OamvGDzW%2FQmnBMa24MJzmF4WpxMD%2FGPRzMvaDyhfBpdc93u2jtll6mNtYjSnx3tIO3AjU7sax3Pkg7KRz1EyVdt7vUdyy2lr3F3cEmFKdkDAeu0Gc%2BZKcsbnmnk%2BzPaSvFLuiwIlOEYD46oZnN2fUqEk9xpFfnBONXfaXNwzXaVbWkeFFSa6a%2BzfKHyeO%2BdFrMWjhRJVD5WEN1oQ%2B0qh3V9Udsh5YhIDstLEvNuCQsIbWwhnLnx0XjUMK3hrMoGOqUBiaUGLLz4xY14OCRYKEddhSve%2FJXWvc8moCFCbfvKg1zwQeJSdjxd3DMfO9vSl9RTFdnCy1ZFILv4BBkZocL1NsnJB4pM8eHPWDwmxAJS0zjFgEruoDyPUYfnoF8V%2Fem5ZFBsfBydsm1CxPzsWCLLThk7U3qlg0BYxGB9XUykUZ7Y2khtGAjii9hss%2FK5oB3zr97XsZ7JEqt%2BbXMCZC1HDmrwghGA&X-Amz-Signature=6f1233182afcfff4d35d47156716e69609b8816a1d33032349424a65c589a712&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



