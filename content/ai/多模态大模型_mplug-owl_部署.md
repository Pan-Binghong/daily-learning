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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HTUORXG%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDN9FVPn62cFtk69QOY9Bf9Tnqgl%2FIkNeD7DZvAaAd3uAIgJpIoVNAnP7fG06nd%2B1BevEjlDoiNweFY1ZA5Rb5niUgq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDHkb9pL%2Bp7C1MQgFoSrcA%2Bf9Ewa1%2FC7r18qCDA47oRaIjpUHnulRriOCp6tQ04q1Y559Kh3NAjeGSKVTyfEeNzu3Tw9Z3y4%2FyynBh7ssVwJP0dqmV1hh9YH15iz2mKY%2FJYtgLVum%2F6Ad2sHMgy8BQz2EwlYJLDr1oEpF84UxLwUZn1Z3b4Bc21yL5uRqzc%2FfU3%2B1d5OfGsHN3n51%2FJidHjK80yTS781gUlQA3llZRC1kAUcnXdgQmCgjpsOPQN8OiE%2F6gRyvUltZXEykrI5drC0E6hdpJZIZUEzT0jdKNbhdXkjVul58lAq24545YOiMcRMGbZOx2BzFeN7HTSALrFaa%2F8vtPHssSItXB3FbqzTB2Tf5Ff2t6NGwXBmRYOiApuVPS%2FhohCIg8aZTvNUJL%2BnLaGVF1g9LpbzU%2BlXn%2Bh0ku08mztDQluir9WmDSSHhu0ffGY2oHL6i%2B2Dr3Hdd0qn26idhAkn9NVNYK%2F8YuTDKe09gMQeP4C6DBeadbJ2UMyNzYeZbNzkfcKofftYimYJJaXDWCxD5ES%2B9Hpm374F%2Bi4FdhndvYk7t%2Fi0QYsvvz51ivK5ywWET7pWsJP%2B3WTVzWCyvNwXRI%2BUhOa8%2FS4o%2FsHgWjxxCFNAuv5neI7%2F6GD73ChusioORMfutMLuVic0GOqUBEOPhYZ3tjrFTJwoLuIgdvFe2bQn9JPD%2FhsT%2Frqu1XZAQYLDPAk0qGuPjnOYi6Q0MeqL7BqRS9%2FHuD6FaJplCV3vZFfXuGYUI1aSuuSBz502AgmUKnnGTqExd1B0lfevyDWfKguOYjFl%2F%2F85FgJgf7VCK4wPQoaZFjrfLdXNARROjd75xKE8a437hp7yD1ExF9YlXTG0e7PopzOpLawxqZSs9AI1b&X-Amz-Signature=740f373a544c32083072447731199dcc18b3f612d1107156cfd1a6e43c1e03b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HTUORXG%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDN9FVPn62cFtk69QOY9Bf9Tnqgl%2FIkNeD7DZvAaAd3uAIgJpIoVNAnP7fG06nd%2B1BevEjlDoiNweFY1ZA5Rb5niUgq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDHkb9pL%2Bp7C1MQgFoSrcA%2Bf9Ewa1%2FC7r18qCDA47oRaIjpUHnulRriOCp6tQ04q1Y559Kh3NAjeGSKVTyfEeNzu3Tw9Z3y4%2FyynBh7ssVwJP0dqmV1hh9YH15iz2mKY%2FJYtgLVum%2F6Ad2sHMgy8BQz2EwlYJLDr1oEpF84UxLwUZn1Z3b4Bc21yL5uRqzc%2FfU3%2B1d5OfGsHN3n51%2FJidHjK80yTS781gUlQA3llZRC1kAUcnXdgQmCgjpsOPQN8OiE%2F6gRyvUltZXEykrI5drC0E6hdpJZIZUEzT0jdKNbhdXkjVul58lAq24545YOiMcRMGbZOx2BzFeN7HTSALrFaa%2F8vtPHssSItXB3FbqzTB2Tf5Ff2t6NGwXBmRYOiApuVPS%2FhohCIg8aZTvNUJL%2BnLaGVF1g9LpbzU%2BlXn%2Bh0ku08mztDQluir9WmDSSHhu0ffGY2oHL6i%2B2Dr3Hdd0qn26idhAkn9NVNYK%2F8YuTDKe09gMQeP4C6DBeadbJ2UMyNzYeZbNzkfcKofftYimYJJaXDWCxD5ES%2B9Hpm374F%2Bi4FdhndvYk7t%2Fi0QYsvvz51ivK5ywWET7pWsJP%2B3WTVzWCyvNwXRI%2BUhOa8%2FS4o%2FsHgWjxxCFNAuv5neI7%2F6GD73ChusioORMfutMLuVic0GOqUBEOPhYZ3tjrFTJwoLuIgdvFe2bQn9JPD%2FhsT%2Frqu1XZAQYLDPAk0qGuPjnOYi6Q0MeqL7BqRS9%2FHuD6FaJplCV3vZFfXuGYUI1aSuuSBz502AgmUKnnGTqExd1B0lfevyDWfKguOYjFl%2F%2F85FgJgf7VCK4wPQoaZFjrfLdXNARROjd75xKE8a437hp7yD1ExF9YlXTG0e7PopzOpLawxqZSs9AI1b&X-Amz-Signature=a32dd4d24df377842f798ec7ec03c60e8937e402e4e56b74adbf73e55af231a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

