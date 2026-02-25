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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5S5V6MR%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQDe0%2BT6Fw1Bp0Uto0RI7%2FO%2BY5a32V0FHAAxSCMONlfq9gIhAPZdEaFgTFr%2FPsQJKTEL3ydNldcoQ0gahcu7SQxjhUnwKv8DCAIQABoMNjM3NDIzMTgzODA1IgwBtTv4JSRR4Ej%2BYzMq3AOxvfPPUG4fEH1wqfn8pMSCK4EP4SdnCTHeJvceJJT5lehlRNoYxP1DwTU8mJN%2B0B5EmYN8vj5fbdtNkz1UoPyjmwPWYWTsY%2Bg%2FXbEfZ7iKa2C9mTn4rkt50mBTGOiD6I9llYbQaqDGwNCuS7IRgpqg%2FUhU%2BCJurW7gvqjw1PuTl082n29%2Bs%2BnasUgw%2FTl6PRADAMip9nCjc17WeBcX5lUIIdLi278jAp%2BcS8lavFqPOvYYw9AAQL6dz70XabiFQ9cEu7esbLa9dD9PGn0mZpvJg5uzUM1%2BzPRsNRVPtyuO34QEzKK0sN9%2FgZnibgeY8dGC%2Bwyy50cObmR9jrRjNfABbTmfOgU7klEj7zGW3MABuPoYlRKUkUMbynlJx2vuk2PiRAPPewY6hk%2FdiLUPI%2FerQgibo0xoJMMCg4gR8Gb4UxbgxFoL2aT%2FsvC69nmC4mUPA95KHVyKrUtTajvQv5GePov6CUNg6ksoYY%2B7x8MAXqV448ik8L%2B%2FYDDv277hLzXU%2FOJsLQZ0Q5A9TH2waMtEV5aMNDVOvprTDYpEAuONEtjsAE8qRxEXAJoC1a%2Bl11q%2Bhlb6918zaYKKaYlKY%2B4Kk6Iwf5ZnP4xywew9F30Wi6WCmKpzvDKOHAkEsjC9g%2FnMBjqkAbRXuN4OxjRw0APZ8A4s80d6gH9dBOTj6%2F0pddaVwJM7UaGkTpwBhfw7iKP6zjrrQBym31f7RvGQIepNHNY1WZTN2C2kuK93t5Lm3GJLuqLSu6mY0LLw5CQDw%2BQmfwz%2FBinlEE6FrV38ey4RyyIryAyqO7r5n%2BXFcVTkHxRMdUSdpCIbX8c8gevEsQ1TzZSUo1MGjxAd3aUcOiaKWlEEEyy791Dg&X-Amz-Signature=8141850f3176e742cce53e2a9d60e8ede85221c9b371ae9c2f36e9504c5eecfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5S5V6MR%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQDe0%2BT6Fw1Bp0Uto0RI7%2FO%2BY5a32V0FHAAxSCMONlfq9gIhAPZdEaFgTFr%2FPsQJKTEL3ydNldcoQ0gahcu7SQxjhUnwKv8DCAIQABoMNjM3NDIzMTgzODA1IgwBtTv4JSRR4Ej%2BYzMq3AOxvfPPUG4fEH1wqfn8pMSCK4EP4SdnCTHeJvceJJT5lehlRNoYxP1DwTU8mJN%2B0B5EmYN8vj5fbdtNkz1UoPyjmwPWYWTsY%2Bg%2FXbEfZ7iKa2C9mTn4rkt50mBTGOiD6I9llYbQaqDGwNCuS7IRgpqg%2FUhU%2BCJurW7gvqjw1PuTl082n29%2Bs%2BnasUgw%2FTl6PRADAMip9nCjc17WeBcX5lUIIdLi278jAp%2BcS8lavFqPOvYYw9AAQL6dz70XabiFQ9cEu7esbLa9dD9PGn0mZpvJg5uzUM1%2BzPRsNRVPtyuO34QEzKK0sN9%2FgZnibgeY8dGC%2Bwyy50cObmR9jrRjNfABbTmfOgU7klEj7zGW3MABuPoYlRKUkUMbynlJx2vuk2PiRAPPewY6hk%2FdiLUPI%2FerQgibo0xoJMMCg4gR8Gb4UxbgxFoL2aT%2FsvC69nmC4mUPA95KHVyKrUtTajvQv5GePov6CUNg6ksoYY%2B7x8MAXqV448ik8L%2B%2FYDDv277hLzXU%2FOJsLQZ0Q5A9TH2waMtEV5aMNDVOvprTDYpEAuONEtjsAE8qRxEXAJoC1a%2Bl11q%2Bhlb6918zaYKKaYlKY%2B4Kk6Iwf5ZnP4xywew9F30Wi6WCmKpzvDKOHAkEsjC9g%2FnMBjqkAbRXuN4OxjRw0APZ8A4s80d6gH9dBOTj6%2F0pddaVwJM7UaGkTpwBhfw7iKP6zjrrQBym31f7RvGQIepNHNY1WZTN2C2kuK93t5Lm3GJLuqLSu6mY0LLw5CQDw%2BQmfwz%2FBinlEE6FrV38ey4RyyIryAyqO7r5n%2BXFcVTkHxRMdUSdpCIbX8c8gevEsQ1TzZSUo1MGjxAd3aUcOiaKWlEEEyy791Dg&X-Amz-Signature=2f51874c5cb42d4aac0b8491d708dd60442c0e45f888797fca3b2a969c4db4fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

