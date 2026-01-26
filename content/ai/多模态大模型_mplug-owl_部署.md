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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6L6T54X%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQDTsHYn8e3IrFAYtD%2BIfpMOSE8HUREh8iuK2R7xUcBWEgIhAPtIOqvyKz6GsYIZuTvZI1EXh%2FRtM5MM2MFRl53CzoQkKv8DCDAQABoMNjM3NDIzMTgzODA1IgzEO8VDqgkMmI5ciKoq3ANmiY2mYAgBBx6kHKDmF%2B43XhXehvnzTIpim44hdQ25D%2Bzj9yC2Qvoj7DX%2BZNS7k4kdZtIv9uZXz%2FdWmFDYMVEMGtbynlrikF%2B4F6OLzGY6KaiPlsk4pV%2Bd16SMFT9Y42MVEEuJ81EhB450lLMCgZRYGBEBkbwxpipcnzRFglW0wUmGD76mnpD8hJ%2FqfXzY9NODLoH0MpnVzmvhVAXfXipBowOydiA0iZRhA%2FMLznWYV1ysoNGeGzxvxlLvvxN0bacxZvtFT17oWKOHh7NHMY3hqGOhAUfGjfhuslU85kpGEJdNvbxM8F61mVzGkVzoefmzzN65yYap25c0mFSIQdS9aA56KAgGKo0E574cDs3cx%2FF5vqbvgFcofAUa6lt3RVJKWaV%2BIpKGpfSSbNG5jg77xhP2NjRgvjzqpgfOzXtj8gsGVh2MK0s9kR0tqMBtL19gO2%2FHe8dMd9aIl0OS7hkWrgP8Qj1LlBuXHwkv%2Fbols7%2Bt2mOJ25wRXIsG8hqHY0sdb9%2BJbdi6U7ch7dYN9pU2JHsDdAv7I67vipS2moq2JUikTvBc6uvtYIXgmcWgI8Cp50l42QWu1SI%2FCa6Ub5vQPy%2FnpsUcnj7NUbT0HB6JI%2FlUroUlu6PMadbtnjDVsNrLBjqkAQ1unPyE74K3JUXo0w81Xs9JuVHwado2t%2BF5C8cLi3asML0VE%2Fm0mpZNZPVNmEdqhboB4poC9qgIhQVQeYPsPCh4pJY0LOQ%2FayxTWPsAH6a2LieI3iXwrMnyaNOHYZC7yFiWCf1gqSbSW0v%2F42xxOFhLSc9ALcxQOG3kb%2FwkN1z3hvmYTjZ3vRt9k7V2AxhtaVg%2F538%2BdMBbvuVtKDp5J5qtb8gF&X-Amz-Signature=c06cda4b7dc8b11b98140431253c3dd9919a0aee8d494850c26d624e5792d612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6L6T54X%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQDTsHYn8e3IrFAYtD%2BIfpMOSE8HUREh8iuK2R7xUcBWEgIhAPtIOqvyKz6GsYIZuTvZI1EXh%2FRtM5MM2MFRl53CzoQkKv8DCDAQABoMNjM3NDIzMTgzODA1IgzEO8VDqgkMmI5ciKoq3ANmiY2mYAgBBx6kHKDmF%2B43XhXehvnzTIpim44hdQ25D%2Bzj9yC2Qvoj7DX%2BZNS7k4kdZtIv9uZXz%2FdWmFDYMVEMGtbynlrikF%2B4F6OLzGY6KaiPlsk4pV%2Bd16SMFT9Y42MVEEuJ81EhB450lLMCgZRYGBEBkbwxpipcnzRFglW0wUmGD76mnpD8hJ%2FqfXzY9NODLoH0MpnVzmvhVAXfXipBowOydiA0iZRhA%2FMLznWYV1ysoNGeGzxvxlLvvxN0bacxZvtFT17oWKOHh7NHMY3hqGOhAUfGjfhuslU85kpGEJdNvbxM8F61mVzGkVzoefmzzN65yYap25c0mFSIQdS9aA56KAgGKo0E574cDs3cx%2FF5vqbvgFcofAUa6lt3RVJKWaV%2BIpKGpfSSbNG5jg77xhP2NjRgvjzqpgfOzXtj8gsGVh2MK0s9kR0tqMBtL19gO2%2FHe8dMd9aIl0OS7hkWrgP8Qj1LlBuXHwkv%2Fbols7%2Bt2mOJ25wRXIsG8hqHY0sdb9%2BJbdi6U7ch7dYN9pU2JHsDdAv7I67vipS2moq2JUikTvBc6uvtYIXgmcWgI8Cp50l42QWu1SI%2FCa6Ub5vQPy%2FnpsUcnj7NUbT0HB6JI%2FlUroUlu6PMadbtnjDVsNrLBjqkAQ1unPyE74K3JUXo0w81Xs9JuVHwado2t%2BF5C8cLi3asML0VE%2Fm0mpZNZPVNmEdqhboB4poC9qgIhQVQeYPsPCh4pJY0LOQ%2FayxTWPsAH6a2LieI3iXwrMnyaNOHYZC7yFiWCf1gqSbSW0v%2F42xxOFhLSc9ALcxQOG3kb%2FwkN1z3hvmYTjZ3vRt9k7V2AxhtaVg%2F538%2BdMBbvuVtKDp5J5qtb8gF&X-Amz-Signature=6b8b429498a1d1692d7a4778eed0b555d57cf47b8dbc7fbaafa36e9af8aa77e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

