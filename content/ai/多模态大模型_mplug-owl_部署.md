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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRIUQ6FM%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWRXV6zMFLi9aNNFg%2FPoEGhAeDYJ2qpitUBrDNhN5jYQIhAN6su11CrnyqLv4lfeJ8hFVWXKkN4myC1Ra5J06X1criKv8DCFsQABoMNjM3NDIzMTgzODA1IgxRcu5oJxt4EmLIFy8q3AMQmwVlhEdo5z%2BD53OgkeE6alurVy54zkeor%2Fpqc17zi48Es69uDb0yhbYEEhHZYAv4EqloLWEq03iVliclnn3nuhMT%2BD1W%2FxG1HUVbXg6Da7USpy3EosAtjIjYt8QgtynARnve03xpFE8XjLtefxNp13C%2BTYLYQ8zsVp6gSebyV8Sw3d8gLu1tpDQ74y3sy3%2FlIwREOV2KXx7Zn9MSpCT5gzuJZ%2BrCL66%2BvC7UQZ3xEmyVORaO3xdxOfjgN9iREQ5U%2FUMhawMJDEd%2BayzGHilslwMOME55f%2FENoAEdCB4gaoqwG%2FInoFH1yruBDqKeqGXS%2FDvrCSPRqRdRkXG65TvAyKI%2BH748q6uecbufj6EQ1sPbtOfSihfFpl4JqVGQrAPrjfiKYzxFt2WxaIGYn6AMGt0WlKgj64pQ7OPvxmz%2BgSIxmh0Vf%2BYvqd3ldqqyInIxrjpeV5xiXkAVhlf%2Bd4UMxdMmpCFdz0uvpJqz6Myvk1osnWDfHnmTxGpIh9gAgzWW1nqRSmjrt50JpftwUB8Tf3%2FUgEfbf4smmUJRI5Qd9CWQVc5jzLvQHN3%2BqZh98GmsThg8ZvNvWVPq3gaSHRS6ZzTE3sCwOC6GExqP%2BNdp2wu3%2FQI1fp2bLXda7zCv0avLBjqkARDyS4mszgMJtRFPOf0B7kWN8wLGgc%2B0eEyQgUaNG2DbKUhXvmeDsPpn9%2BlWX5iUH1SaIs3yChG%2BivgpMMVtNyBwv5%2BEVdTl6HX%2FF5SpfVLwIfPco%2B8jTk7kCorxDdc8pS9yjerx4sGfbznsjKTz%2Feruh%2Bf1GAPPtWl0sgzYbUGmd6l6VWLCfwUqHZI5UEXRoaPKsmcY8HMPaeBAms6H1SMBSk35&X-Amz-Signature=bf4ce9c2a535e49c4ebdbb5f2920177bfe60f56c68e883bf559ba6a0358d472c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRIUQ6FM%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWRXV6zMFLi9aNNFg%2FPoEGhAeDYJ2qpitUBrDNhN5jYQIhAN6su11CrnyqLv4lfeJ8hFVWXKkN4myC1Ra5J06X1criKv8DCFsQABoMNjM3NDIzMTgzODA1IgxRcu5oJxt4EmLIFy8q3AMQmwVlhEdo5z%2BD53OgkeE6alurVy54zkeor%2Fpqc17zi48Es69uDb0yhbYEEhHZYAv4EqloLWEq03iVliclnn3nuhMT%2BD1W%2FxG1HUVbXg6Da7USpy3EosAtjIjYt8QgtynARnve03xpFE8XjLtefxNp13C%2BTYLYQ8zsVp6gSebyV8Sw3d8gLu1tpDQ74y3sy3%2FlIwREOV2KXx7Zn9MSpCT5gzuJZ%2BrCL66%2BvC7UQZ3xEmyVORaO3xdxOfjgN9iREQ5U%2FUMhawMJDEd%2BayzGHilslwMOME55f%2FENoAEdCB4gaoqwG%2FInoFH1yruBDqKeqGXS%2FDvrCSPRqRdRkXG65TvAyKI%2BH748q6uecbufj6EQ1sPbtOfSihfFpl4JqVGQrAPrjfiKYzxFt2WxaIGYn6AMGt0WlKgj64pQ7OPvxmz%2BgSIxmh0Vf%2BYvqd3ldqqyInIxrjpeV5xiXkAVhlf%2Bd4UMxdMmpCFdz0uvpJqz6Myvk1osnWDfHnmTxGpIh9gAgzWW1nqRSmjrt50JpftwUB8Tf3%2FUgEfbf4smmUJRI5Qd9CWQVc5jzLvQHN3%2BqZh98GmsThg8ZvNvWVPq3gaSHRS6ZzTE3sCwOC6GExqP%2BNdp2wu3%2FQI1fp2bLXda7zCv0avLBjqkARDyS4mszgMJtRFPOf0B7kWN8wLGgc%2B0eEyQgUaNG2DbKUhXvmeDsPpn9%2BlWX5iUH1SaIs3yChG%2BivgpMMVtNyBwv5%2BEVdTl6HX%2FF5SpfVLwIfPco%2B8jTk7kCorxDdc8pS9yjerx4sGfbznsjKTz%2Feruh%2Bf1GAPPtWl0sgzYbUGmd6l6VWLCfwUqHZI5UEXRoaPKsmcY8HMPaeBAms6H1SMBSk35&X-Amz-Signature=37441d7810456df009aeea3e6ee50a39a4470fb27379af0f5e841c880de74799&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

