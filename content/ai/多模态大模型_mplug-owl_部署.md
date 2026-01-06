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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVDQPR42%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6olStj0pxjrcKxgFbH%2Bg75gqzbeRE5Leo81S1kCxZ5AiBFvnSwmWWphyPCGS6tE8LSInQojRUg%2FTMN6FY9QnbRBCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMU3Vyoq7HqYcGid0kKtwDKaxlABHcTQdplcbH6P7QGnJxpDucqYKY3meOTSjN7Vgib1SOY8Ya3Z76Dw1UMVcF0Of2j%2FKA3IVoodwy9u9RFVzKwddJzy1fRYwA09fc%2BUYfppwIvmXK5o4fU%2FSQgHRj8TNX3AXLL%2BhvI%2BnyzHd90ZhAUZgVhAPKybtrr1hcnJExsT1SSGddBWt%2FlQfz1y%2Fvki5H8Akvo%2BBdTjULQMy9ay7hlMjCSvcRsMmB5uRAa8UQbUPHDvR%2FRVjFrfh4djnPUZ51%2FXBnawRCNH5ZWTZ1GRMOVjKF2BrYHQHaa7K9qgHHg7gfgxrijq4zuti3pIhEH0wKU7yWGZmU4K9Q1d7mTM1mZUYT0Ooy6%2F0vV2hlvcFN%2BGMtafJpxSmL7LGkAQ5eKuuo9ET%2FID%2BEtlvNsB2t6voZ2P36Q1oAceoFPKyX5t6vWd2AdEFsgMwmPpalRcv6DHhpfejvQfOm6iwIP8jiVbRU%2B0SdgXWPQAUtSJp80WrfPa0L2UgGcPdcEZpyrWtsgEnuw%2FL8ZxKh9iAGRBHtv8Ptu%2BXaqPLxV1ez1hpojwUiKHUvwNJ5UxVVgMWQ933rvb86j0fkQ3lUyB0w%2B5NEKNsFKItQ5WBWRwOUIcNG1b6oKlpAUDXDwSdt0n4w%2BOXxygY6pgFRX6nT3meZFF69EVp4gm5tbt5%2BZguWPJO35x7F65X0FkkVBaotntXkXZj47kcIWQMg8CycTzyCz%2BormLkwIt2Jqmsei346DZwUmAXREmu4J9atLKT2Y9NFFD1IKf7hHhbNoYtNy33H5b%2FA3ZaFEvRoQMCHdoAXfRghR8DgP5hRm4Bwy0aKz9YQq7IvwTKM1ki7EqQCV40jZ9OaBMPlQ2gTb5yAHLft&X-Amz-Signature=95d3ec3cf44be85f6d7cfb1ed0118ff05e2590c0f61bb181ee1ad68105a394e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVDQPR42%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6olStj0pxjrcKxgFbH%2Bg75gqzbeRE5Leo81S1kCxZ5AiBFvnSwmWWphyPCGS6tE8LSInQojRUg%2FTMN6FY9QnbRBCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMU3Vyoq7HqYcGid0kKtwDKaxlABHcTQdplcbH6P7QGnJxpDucqYKY3meOTSjN7Vgib1SOY8Ya3Z76Dw1UMVcF0Of2j%2FKA3IVoodwy9u9RFVzKwddJzy1fRYwA09fc%2BUYfppwIvmXK5o4fU%2FSQgHRj8TNX3AXLL%2BhvI%2BnyzHd90ZhAUZgVhAPKybtrr1hcnJExsT1SSGddBWt%2FlQfz1y%2Fvki5H8Akvo%2BBdTjULQMy9ay7hlMjCSvcRsMmB5uRAa8UQbUPHDvR%2FRVjFrfh4djnPUZ51%2FXBnawRCNH5ZWTZ1GRMOVjKF2BrYHQHaa7K9qgHHg7gfgxrijq4zuti3pIhEH0wKU7yWGZmU4K9Q1d7mTM1mZUYT0Ooy6%2F0vV2hlvcFN%2BGMtafJpxSmL7LGkAQ5eKuuo9ET%2FID%2BEtlvNsB2t6voZ2P36Q1oAceoFPKyX5t6vWd2AdEFsgMwmPpalRcv6DHhpfejvQfOm6iwIP8jiVbRU%2B0SdgXWPQAUtSJp80WrfPa0L2UgGcPdcEZpyrWtsgEnuw%2FL8ZxKh9iAGRBHtv8Ptu%2BXaqPLxV1ez1hpojwUiKHUvwNJ5UxVVgMWQ933rvb86j0fkQ3lUyB0w%2B5NEKNsFKItQ5WBWRwOUIcNG1b6oKlpAUDXDwSdt0n4w%2BOXxygY6pgFRX6nT3meZFF69EVp4gm5tbt5%2BZguWPJO35x7F65X0FkkVBaotntXkXZj47kcIWQMg8CycTzyCz%2BormLkwIt2Jqmsei346DZwUmAXREmu4J9atLKT2Y9NFFD1IKf7hHhbNoYtNy33H5b%2FA3ZaFEvRoQMCHdoAXfRghR8DgP5hRm4Bwy0aKz9YQq7IvwTKM1ki7EqQCV40jZ9OaBMPlQ2gTb5yAHLft&X-Amz-Signature=df9b936f19078dfa1e5cecc74121d5e460711d9582ee6f98d7f40ea51e217c78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

