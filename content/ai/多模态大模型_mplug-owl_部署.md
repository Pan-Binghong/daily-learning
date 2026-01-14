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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQAJSDAN%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIDgkNsFTKGohooAVuJxBfCCo8L0pkvQPrrHQItKnmg8%2FAiEAyDtVhCibuER1Rdw%2BWqBowGLEcPCRljmKUVgWv96ozIkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDGJtpz9D1FbvMngdiircAy2eO6t5MMcaq8c0uaTTKypRIEWK0Hp2qPT7rIrIlA3V8gYF6T5pBcPQSXKyU3MFYrxDVa07xYWY2t6yftZTRfZja1IzWHl%2FCYDYpK%2Bkd7B%2BSBI3cp8wGyOWPzhc61vX8U77QATkRjaa7%2Fg3PggNoxwHxBVQdnIO29jy%2BqXKxGIaMqFla3T0Ia7bCqp7cVorP2TQdeylyNwIYvubyY0%2BOs0ijD721D3Pzy0gP0ScTBsIEQkSf5ch4LxzRpSKXuenV8sPKW0J%2FD12ulETgeAHBieHs99zP%2BiVhh6gLPZ2lyMzSu7EycvnGfiGyvrrErvc9zxgSIygL9Z99MWcVdhVUpLkwkrvZm2GltLpLc%2Fb5u06UXhOsNYrrsvEFjiIsmxNdoyAclQYlM4OjlY%2BUGoqhFkla23P%2B7hSgkpGSWJerqYuiPPvtb6r1dQBQ7YOPqIsLb8iJOsRJ8%2FKyqTH496xs5w6q5W%2BcMJA45l%2Bg%2F4lFFHXlx2LRnaUGRAwlGheOVLXS%2BZiK1BY0rkkBnVsG59UWL6lg0%2B0pEi8CUcgpmGVp8YdprBLYyrvoT0BDB0rkT3oJwOkeHXvX6WhKKYkQSLQuJH0djiNSavMvUJBC4eQvhnO3Sk%2Bk%2BTPLXK1KlHJMI%2Fum8sGOqUBkjHb1%2BeQb7zSsDo6wHETzVXAdx8ZzEZBzZu6gjN4X4y1HAf4cqgrYbb0LDkkJgJgN%2FEENG2fR8ebrb4rsgcjudqigXCXu0xPQ1O9W6ZvQmyg0SYRvo2xiy%2Bhtg%2BsYatUD9WbED7eetoMppgXIHnqyQLYg%2BtkN%2BeZOSGiGA%2Fk%2FzgJQ0k126V29GNNuurrhYVWrkj4MZ0zr4pxC7AMTO8HE0t%2BX%2Fev&X-Amz-Signature=195f5727b0086d5e2109363b069de7386ebea402fce2aef56b363cadf237be1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQAJSDAN%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIDgkNsFTKGohooAVuJxBfCCo8L0pkvQPrrHQItKnmg8%2FAiEAyDtVhCibuER1Rdw%2BWqBowGLEcPCRljmKUVgWv96ozIkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDGJtpz9D1FbvMngdiircAy2eO6t5MMcaq8c0uaTTKypRIEWK0Hp2qPT7rIrIlA3V8gYF6T5pBcPQSXKyU3MFYrxDVa07xYWY2t6yftZTRfZja1IzWHl%2FCYDYpK%2Bkd7B%2BSBI3cp8wGyOWPzhc61vX8U77QATkRjaa7%2Fg3PggNoxwHxBVQdnIO29jy%2BqXKxGIaMqFla3T0Ia7bCqp7cVorP2TQdeylyNwIYvubyY0%2BOs0ijD721D3Pzy0gP0ScTBsIEQkSf5ch4LxzRpSKXuenV8sPKW0J%2FD12ulETgeAHBieHs99zP%2BiVhh6gLPZ2lyMzSu7EycvnGfiGyvrrErvc9zxgSIygL9Z99MWcVdhVUpLkwkrvZm2GltLpLc%2Fb5u06UXhOsNYrrsvEFjiIsmxNdoyAclQYlM4OjlY%2BUGoqhFkla23P%2B7hSgkpGSWJerqYuiPPvtb6r1dQBQ7YOPqIsLb8iJOsRJ8%2FKyqTH496xs5w6q5W%2BcMJA45l%2Bg%2F4lFFHXlx2LRnaUGRAwlGheOVLXS%2BZiK1BY0rkkBnVsG59UWL6lg0%2B0pEi8CUcgpmGVp8YdprBLYyrvoT0BDB0rkT3oJwOkeHXvX6WhKKYkQSLQuJH0djiNSavMvUJBC4eQvhnO3Sk%2Bk%2BTPLXK1KlHJMI%2Fum8sGOqUBkjHb1%2BeQb7zSsDo6wHETzVXAdx8ZzEZBzZu6gjN4X4y1HAf4cqgrYbb0LDkkJgJgN%2FEENG2fR8ebrb4rsgcjudqigXCXu0xPQ1O9W6ZvQmyg0SYRvo2xiy%2Bhtg%2BsYatUD9WbED7eetoMppgXIHnqyQLYg%2BtkN%2BeZOSGiGA%2Fk%2FzgJQ0k126V29GNNuurrhYVWrkj4MZ0zr4pxC7AMTO8HE0t%2BX%2Fev&X-Amz-Signature=7b14516fd9db5cc635a3e3dcf1a2f620fce6e83d205074c559b063d297edf4d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

