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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLC22BH2%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQC5KgbAGXc8kl49RJ1Z8uBGrOAokvGI08YLlGtm3VjSFgIgWTnSdWkuDH6XIx0s8cQrwRIkKfpkZe3%2BJ%2F1EhP5RUV0q%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDBRPw3Yy1hlyBgccrircA54UBxCJSC2ATnXYBA2BJUnk4LB6Of1X0OAhdiLjw3QDi9b%2F70tn2wSKz3%2BmYhU3VmFdSMosvGT4gVx2x5mIwl8jjQEYZqLwPTg619wf5QeTyUGGdFtkPNPWU6spCzUf%2FK8jlzityW9EKQ7E4cxInk1AH1DboWtdvOHYKjHXgBpYUP%2BO0YEKrDk%2FdjDhzVX%2F5VFb9oSHjercEPYtiq2fRvIh%2FLQNHvveNwiBgBq4NM6sjGIA09mffefi%2BMIFhNGXKXKSLkSpAKZyNoUB1raFKTPlmPuRgfHSNZ1nqVAD96aXz5lq3KDMUbUYB3R294OpD6BZEKtADb3PdS%2BHvMkEcjxq7U3dKrDOdPJ8SeBpQptDJFYJ7%2FRYERaAK1n7dvwTwPWuf7r6iiAaNzIGeW22JuRhTB%2Fy0ZUNxPrmP5036UOQV2rGBbMlxdOZOEPyuJ4Y4hnfqHuGkjqWAtYCNC4C5tR7yXqa51%2FnCkdo1DdJ7xOxqxDeXcHf%2Bobg%2Fq6dCTM%2FjcYeK5UQvxbwYboetMem76uXsr8AFvdXA1AEdaTEy%2BplT%2BtdD%2FpLzg%2FLJLZ3EZMADlkhy2yirMrefWgACjr28IyE%2BXZ1JlkOY0vjPbpl3kq1igzLAFl7qG2Z4U3FMKKd4coGOqUB0RSMHaHv13TR1h%2FYTWYGLh4df%2BB5C6llA380TsDDfi2ofWt%2BKq0Fd9WyHa2tMPfZpMVyQIur29GQSi21jm%2B9%2Fz2Eif9XnZdp1UguT69DlGA5S5yA1hNNlbrpKtP%2FJqA42iut%2BMknXGNKPP4KmuniriQDID3StYhMRfi4b%2F%2FPxxx0MwWKjOZMU8SbEGfv4Uss7p1ZOoQYxt6XRx03cTTj%2Bg2jHjEz&X-Amz-Signature=072ec682cc0b9f35d6da10a74204b744f426fe26dffdda528f25474a80d8fb99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLC22BH2%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQC5KgbAGXc8kl49RJ1Z8uBGrOAokvGI08YLlGtm3VjSFgIgWTnSdWkuDH6XIx0s8cQrwRIkKfpkZe3%2BJ%2F1EhP5RUV0q%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDBRPw3Yy1hlyBgccrircA54UBxCJSC2ATnXYBA2BJUnk4LB6Of1X0OAhdiLjw3QDi9b%2F70tn2wSKz3%2BmYhU3VmFdSMosvGT4gVx2x5mIwl8jjQEYZqLwPTg619wf5QeTyUGGdFtkPNPWU6spCzUf%2FK8jlzityW9EKQ7E4cxInk1AH1DboWtdvOHYKjHXgBpYUP%2BO0YEKrDk%2FdjDhzVX%2F5VFb9oSHjercEPYtiq2fRvIh%2FLQNHvveNwiBgBq4NM6sjGIA09mffefi%2BMIFhNGXKXKSLkSpAKZyNoUB1raFKTPlmPuRgfHSNZ1nqVAD96aXz5lq3KDMUbUYB3R294OpD6BZEKtADb3PdS%2BHvMkEcjxq7U3dKrDOdPJ8SeBpQptDJFYJ7%2FRYERaAK1n7dvwTwPWuf7r6iiAaNzIGeW22JuRhTB%2Fy0ZUNxPrmP5036UOQV2rGBbMlxdOZOEPyuJ4Y4hnfqHuGkjqWAtYCNC4C5tR7yXqa51%2FnCkdo1DdJ7xOxqxDeXcHf%2Bobg%2Fq6dCTM%2FjcYeK5UQvxbwYboetMem76uXsr8AFvdXA1AEdaTEy%2BplT%2BtdD%2FpLzg%2FLJLZ3EZMADlkhy2yirMrefWgACjr28IyE%2BXZ1JlkOY0vjPbpl3kq1igzLAFl7qG2Z4U3FMKKd4coGOqUB0RSMHaHv13TR1h%2FYTWYGLh4df%2BB5C6llA380TsDDfi2ofWt%2BKq0Fd9WyHa2tMPfZpMVyQIur29GQSi21jm%2B9%2Fz2Eif9XnZdp1UguT69DlGA5S5yA1hNNlbrpKtP%2FJqA42iut%2BMknXGNKPP4KmuniriQDID3StYhMRfi4b%2F%2FPxxx0MwWKjOZMU8SbEGfv4Uss7p1ZOoQYxt6XRx03cTTj%2Bg2jHjEz&X-Amz-Signature=719ed9d65df6e9de1fa816dc909348dbb28ba019070531985ba17a325585d5a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



