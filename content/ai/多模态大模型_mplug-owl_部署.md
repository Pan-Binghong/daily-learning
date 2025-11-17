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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675L7YFQE%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxhCzrZ6r%2FwwtJFIJSmgFqGDUW93dp9aB9NKHfYpYWogIhAKhWWr7PhNW3UbBae94IyFPvpu%2FU%2BIMPNej%2BluULi4OOKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2JfFaG9DhOTetA9sq3AOCLvlsBV%2FNWeO9WtBNQ9NRn0Uzls1y9OG6%2FfQGnkZ7ahdJWIA2iQFl6UdUl%2B6%2BA%2BRsxe0kiwC2XUmBIPbjF6eB%2BOUJ53JC%2FuCyBZ0PC6HchOS%2FgWpzudR1MuRizWmQgYtDI15B%2BmrdG5ooQJbQKMQparb%2FIIDBAHX7kDdcC5xwe5KpQmrq7ZEZ%2BCthrFq7ojBFDKmv1C5u5LEGZ0N3K49CxXCP7Cr%2FJnlnqlplH8vaIOleL4JPxNSP1M7U76XrbMmmKQO0jQUX9yuPQriZ10%2FSp9kZ%2BKMKzRTUJsmFfaAyIDP8aJqLxXmP1QspmMxEfe70HH%2FPdiMTk00tqU%2FcL4CA3w%2Fj8eUaOJRv7jmc8hgEIU1iQrzPgcbw6ySNxhYjy9sLqsroDoJRXWdMNMLE9p0Sua5Ra5RsvGUZDhTPqzZNr%2FSawERtQU%2B6Nf5j7J89DgRt7ger8dvMZnSKmjSaZpVqIqdQsoTqpUf6jJX4tCp8bLc5uqmKjw5f8q9Y%2FOo3eXkyYhXxIgXJyWXTxMymDCn8Er2%2Ffob16LRrk%2FUeTZKO5olV0S983QsqC%2FPX5iq8vEcqYu6WTj1DBQ4lThImRZtvpDvSbJlxtzEAMsGHz1MZrIv1Ggx%2FwoWMnKCsHjDSherIBjqkARAy1ZPDlAF5%2B%2BzVwHA3gpuMblvcijuNr%2FNSofP6niZozDwuwRDyoyT0%2BQWQPMyq20aksLvDIAjZ%2FTVHF54yhOSVi9IEg9M1iradQ4TNUn4Et6G2zbBORPE5tALDqJgToYF1O3798dyjYUNW9Cqs5vx3KpmZzQn13o7riFEJqu5Vlfz3d1IOFfaA3uUbc8lGMSfQksWdVpVYByGUk1aUmxBplb5Y&X-Amz-Signature=70c9397c60cdf6a11b96b570ef5c3ae4ea81f1d234f79d5a42b54a7d44a3fe71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675L7YFQE%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxhCzrZ6r%2FwwtJFIJSmgFqGDUW93dp9aB9NKHfYpYWogIhAKhWWr7PhNW3UbBae94IyFPvpu%2FU%2BIMPNej%2BluULi4OOKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2JfFaG9DhOTetA9sq3AOCLvlsBV%2FNWeO9WtBNQ9NRn0Uzls1y9OG6%2FfQGnkZ7ahdJWIA2iQFl6UdUl%2B6%2BA%2BRsxe0kiwC2XUmBIPbjF6eB%2BOUJ53JC%2FuCyBZ0PC6HchOS%2FgWpzudR1MuRizWmQgYtDI15B%2BmrdG5ooQJbQKMQparb%2FIIDBAHX7kDdcC5xwe5KpQmrq7ZEZ%2BCthrFq7ojBFDKmv1C5u5LEGZ0N3K49CxXCP7Cr%2FJnlnqlplH8vaIOleL4JPxNSP1M7U76XrbMmmKQO0jQUX9yuPQriZ10%2FSp9kZ%2BKMKzRTUJsmFfaAyIDP8aJqLxXmP1QspmMxEfe70HH%2FPdiMTk00tqU%2FcL4CA3w%2Fj8eUaOJRv7jmc8hgEIU1iQrzPgcbw6ySNxhYjy9sLqsroDoJRXWdMNMLE9p0Sua5Ra5RsvGUZDhTPqzZNr%2FSawERtQU%2B6Nf5j7J89DgRt7ger8dvMZnSKmjSaZpVqIqdQsoTqpUf6jJX4tCp8bLc5uqmKjw5f8q9Y%2FOo3eXkyYhXxIgXJyWXTxMymDCn8Er2%2Ffob16LRrk%2FUeTZKO5olV0S983QsqC%2FPX5iq8vEcqYu6WTj1DBQ4lThImRZtvpDvSbJlxtzEAMsGHz1MZrIv1Ggx%2FwoWMnKCsHjDSherIBjqkARAy1ZPDlAF5%2B%2BzVwHA3gpuMblvcijuNr%2FNSofP6niZozDwuwRDyoyT0%2BQWQPMyq20aksLvDIAjZ%2FTVHF54yhOSVi9IEg9M1iradQ4TNUn4Et6G2zbBORPE5tALDqJgToYF1O3798dyjYUNW9Cqs5vx3KpmZzQn13o7riFEJqu5Vlfz3d1IOFfaA3uUbc8lGMSfQksWdVpVYByGUk1aUmxBplb5Y&X-Amz-Signature=3f0d2795183d17ba6c7c7cc45adc4ae4cf33dbc2f6b2ce6f03854b6fb28e34a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

