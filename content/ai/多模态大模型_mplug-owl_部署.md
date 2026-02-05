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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNTJ54N5%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIBESYggU0GCfvLe9%2BrMhwzb8%2FT8Q8I6UfN3A4jOxDXqdAiBOXp3CbaxVkfn12OZfZCNwCCGTIbbfpMbx6VPrh8AN%2Byr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMGhBv2dlTjHG%2FlcmCKtwDMvjn5XYcYk1TyAHJoyCJQ5IqsgjwIkNohL63rmTnFDfnSDbvBXXNvfqHJXYkAU%2FvtTVhU5v%2FJsjssB0xJ9ZkNvOcJFnf6KAImp8M0S8diivExxwFxUueT7V12oGfFrZu71lTWQzNHLwRUYSzfr0c3gzCmTUZUks%2B5kYv344axyxxVWPB5iZoeIFyOW4Gho4%2FVEnNwTGcwOT81hxb021k%2BE3DNxXYkYMxli99Btdc8saAjLazRx%2BXsjATycyGvDs76ldDli5y8iPk1ReBxr02GQhYpfxpvvgoepz%2BhiewfvmfpiyN0IA1hq36Jv1a2EwcDEXZKgAaPt%2BipjFI%2FaCUl1r7fexx4OsAsYHCwgDmpfKzILVVRYeHVVlM%2FuX92QoN0GzvZEeHmSEuuMm0iM3u45db9M5%2BXuQHNLYclLsQ71tYJM5iVxB%2BLbm6ukbnjQrlTth2Rh426Hd4iVAQQiSz%2F148szLHAXQmgwk%2FkunExX3vlqH8Lls5fcMZl6%2BCRkuLmV4whKawlYW7HPSZSDMtCSkUID6QPCSFybZRQNbCrXa916aQoVmRLfiBOIAav6uOJyD5MXsMRtLfof%2FlSDc3FkQm9ocvqEGy8mRO6Hz1oeJIfdi8DkVCnHvXv2Yw5ZOQzAY6pgFTtW%2FkRWSFJfkjAbD0APpyOVbO5o2j%2FyLQ0jOOXJspsOxSZQFV5VgcYTkJwLUMvJNMj%2Fn4jki4Z4ZPUKcYDeLTc5RDAG0B3KTyh2ogItiBpT3rH8JX9gL3OReSB0nxuyBoVZd6uPyday%2BOJ4J4rdTJ1FqnWVdAQ%2BZv%2FaB8Ggq6WArBcttebm0rWSyIf35cD9HXD8zgl%2FFpwTFtWLovflkJU5Dtw2Bk&X-Amz-Signature=5b110a360d826587ca8f5102f3fad79c5cef364fc601828789bb9166a31a49d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNTJ54N5%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIBESYggU0GCfvLe9%2BrMhwzb8%2FT8Q8I6UfN3A4jOxDXqdAiBOXp3CbaxVkfn12OZfZCNwCCGTIbbfpMbx6VPrh8AN%2Byr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMGhBv2dlTjHG%2FlcmCKtwDMvjn5XYcYk1TyAHJoyCJQ5IqsgjwIkNohL63rmTnFDfnSDbvBXXNvfqHJXYkAU%2FvtTVhU5v%2FJsjssB0xJ9ZkNvOcJFnf6KAImp8M0S8diivExxwFxUueT7V12oGfFrZu71lTWQzNHLwRUYSzfr0c3gzCmTUZUks%2B5kYv344axyxxVWPB5iZoeIFyOW4Gho4%2FVEnNwTGcwOT81hxb021k%2BE3DNxXYkYMxli99Btdc8saAjLazRx%2BXsjATycyGvDs76ldDli5y8iPk1ReBxr02GQhYpfxpvvgoepz%2BhiewfvmfpiyN0IA1hq36Jv1a2EwcDEXZKgAaPt%2BipjFI%2FaCUl1r7fexx4OsAsYHCwgDmpfKzILVVRYeHVVlM%2FuX92QoN0GzvZEeHmSEuuMm0iM3u45db9M5%2BXuQHNLYclLsQ71tYJM5iVxB%2BLbm6ukbnjQrlTth2Rh426Hd4iVAQQiSz%2F148szLHAXQmgwk%2FkunExX3vlqH8Lls5fcMZl6%2BCRkuLmV4whKawlYW7HPSZSDMtCSkUID6QPCSFybZRQNbCrXa916aQoVmRLfiBOIAav6uOJyD5MXsMRtLfof%2FlSDc3FkQm9ocvqEGy8mRO6Hz1oeJIfdi8DkVCnHvXv2Yw5ZOQzAY6pgFTtW%2FkRWSFJfkjAbD0APpyOVbO5o2j%2FyLQ0jOOXJspsOxSZQFV5VgcYTkJwLUMvJNMj%2Fn4jki4Z4ZPUKcYDeLTc5RDAG0B3KTyh2ogItiBpT3rH8JX9gL3OReSB0nxuyBoVZd6uPyday%2BOJ4J4rdTJ1FqnWVdAQ%2BZv%2FaB8Ggq6WArBcttebm0rWSyIf35cD9HXD8zgl%2FFpwTFtWLovflkJU5Dtw2Bk&X-Amz-Signature=341973419e5255dd362d28c8dbe3a014932e8bf51dee9439ca544da33e8c1d53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

