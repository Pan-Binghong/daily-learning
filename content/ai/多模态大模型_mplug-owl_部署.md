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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRXBLR2%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHHh01uQRV8gMrDyiqZ05urqa5AMaMT8Mgzbx%2FlcMja8AiBx%2BEiSOWo8SquMTpbuUzF3kN3XvyqS0Zj1OjUJ4iootyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMql3vLmZ8u3IY8h4PKtwDVh%2Fqgi7RzFdAE3p68XLEMo%2Fi6ulxyu1r2x06BuwrAp5%2BDhQYuPTN92NMbCfE8c9Bq6V0ZX4kmg3tz9hv7h6sALurTbo%2FO3xYoT5Zn5E2bID5ZRjSSVrdVnX8nOSo0cwRMvYDQkWWmfedcXi1t2vZpx%2FW%2F6Wux1xiukFRju9ig5uzYcELU%2BqY%2BytmjxaQ480lZfAFhOaWTxa8j4F8%2BRIq6wyYZil4qFq6dqg75zzMhMZZCSpG3MTh2VzOQMb0i%2FvDFiTqQMxEuleyExz4WPlROEVVy%2BwvjwD0v2mtQdbKmnJiEyOM3aVFKxi4CuLIL9O9rige1AK5z4cNVAmjLB9d0COzrWi5HNSZxE0Scf%2FFzedOFPr26hmwpD9%2FYr6H7aP%2BoolLJa1Hwyl7559U6YICWLc3uVOcQqVmTZEvE6LteJc58UO4zSRC68TYAdshps5qskc%2BIKNd0kSjVTnxKMx6bv2erob%2Ft13aWWUUGF%2BBt9XY9D5O446DSjnRTDpcjO8DNFrjw2Hi338ygbj7sXcq2UioFDgnVQBzEw2j%2BFHVYfVMRF%2FXWkbV4BOS9OUnk8j7SG%2B5V1qdzBgHoaa4%2B88ihgvb7CF%2FwrH8Sr3tQmiomgH2b0qGVxOTkX0VKyIw2PKvyAY6pgE%2FlpiSs%2FzsPW14RAP8tBNt3CE2XUdhIVbUQU%2B5hqYiQFge7YUAjcfsu4JXNOBaAOFVppoGpn5KewNh1QCWSkIAC%2BKJ5hfcRnCEDGppmapC%2BFqij8yNnHyuMrCjbDELcm967rzUxEydHYiHqUPUIBxFYIC5s83TyFAZWvw2tvIWL4u4lgjNsDA8UYAw1bNuJJEnkwUdZh6Hx5TAsM2qGuwfF05JA8pH&X-Amz-Signature=f37ee2b44d6655348734043124dcbf975dcf060965ee0d9079352b4278c15e45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRXBLR2%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHHh01uQRV8gMrDyiqZ05urqa5AMaMT8Mgzbx%2FlcMja8AiBx%2BEiSOWo8SquMTpbuUzF3kN3XvyqS0Zj1OjUJ4iootyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMql3vLmZ8u3IY8h4PKtwDVh%2Fqgi7RzFdAE3p68XLEMo%2Fi6ulxyu1r2x06BuwrAp5%2BDhQYuPTN92NMbCfE8c9Bq6V0ZX4kmg3tz9hv7h6sALurTbo%2FO3xYoT5Zn5E2bID5ZRjSSVrdVnX8nOSo0cwRMvYDQkWWmfedcXi1t2vZpx%2FW%2F6Wux1xiukFRju9ig5uzYcELU%2BqY%2BytmjxaQ480lZfAFhOaWTxa8j4F8%2BRIq6wyYZil4qFq6dqg75zzMhMZZCSpG3MTh2VzOQMb0i%2FvDFiTqQMxEuleyExz4WPlROEVVy%2BwvjwD0v2mtQdbKmnJiEyOM3aVFKxi4CuLIL9O9rige1AK5z4cNVAmjLB9d0COzrWi5HNSZxE0Scf%2FFzedOFPr26hmwpD9%2FYr6H7aP%2BoolLJa1Hwyl7559U6YICWLc3uVOcQqVmTZEvE6LteJc58UO4zSRC68TYAdshps5qskc%2BIKNd0kSjVTnxKMx6bv2erob%2Ft13aWWUUGF%2BBt9XY9D5O446DSjnRTDpcjO8DNFrjw2Hi338ygbj7sXcq2UioFDgnVQBzEw2j%2BFHVYfVMRF%2FXWkbV4BOS9OUnk8j7SG%2B5V1qdzBgHoaa4%2B88ihgvb7CF%2FwrH8Sr3tQmiomgH2b0qGVxOTkX0VKyIw2PKvyAY6pgE%2FlpiSs%2FzsPW14RAP8tBNt3CE2XUdhIVbUQU%2B5hqYiQFge7YUAjcfsu4JXNOBaAOFVppoGpn5KewNh1QCWSkIAC%2BKJ5hfcRnCEDGppmapC%2BFqij8yNnHyuMrCjbDELcm967rzUxEydHYiHqUPUIBxFYIC5s83TyFAZWvw2tvIWL4u4lgjNsDA8UYAw1bNuJJEnkwUdZh6Hx5TAsM2qGuwfF05JA8pH&X-Amz-Signature=24396f1cdbaf4cc831d0f4efaae335cbef8d117901e492f1afb5cd9857d5dd11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

