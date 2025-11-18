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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X35IH7I%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2%2BTKP5ecN7BYMecD9IgSWw5d8pmIZ2%2FeG%2FIR2e3jJOAIhAOt%2FgmHRI3WxS4D1Ca3QzvSBbr1O8XAqJrv8eVDDBDRWKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyrsc6gyp%2BjQe1zmo4q3ANrB4QYBKQxTNkdOEvGdaasTu6WQoybfKwdX%2BTfM5TfbgUK77t5nsecf7YHfCmFmCQ73hvb9awlc5DpnDW%2BjHHXms2Oezsf7Wzx%2Bgyr5OaeffSUtqsqIhaO8vHdZOJh%2FpxOap16Cw5hHAZdhSnuAsNGIgtP1sa9mb%2FJWIqGTd9SeE2Hzp38GnlKy1Jo7xVrIwiVXyUS%2FJ1XKW%2FoQxnPcBdnQ1HVF7VCPjRSzT2j4mkLYu5eaKgo5de%2F9TVONoQ6%2Fa0pnfIYHCxqT2sznpmIt3Ir8eZRvoZNYnsrLWccnkxg%2B%2BexEi2eyKISTk4IETSX0qbx9kVNWF3wCce629ZnqdBiVP5ptDBRO580dpRGunUtl9%2F4A73eQqHM%2BWMRR0exjqrjjtBcAf5x8V5yoa%2FbT5U96MHwdQxjOFFTwqvId3PKATFVFHADx4JLrGNdHt6O0Y88TaPUpN3REQLXxE4558DmlQ1gYBtIZFf4KLpxlZIHPJPIJt3qzH%2FzIx1mg8Q2QOmuRb3y%2BGSFILEubfmbMxzHwQpWxrlQ2PmfdBMjTdD6ztwsk7xpmh5xiY6RuEbh6TVK%2BEhAks5L4IfAJbb0H1TNtttVsbnD%2F89YH6Pkh1AsqxC6t%2FCbctydlqZHXjDWmO%2FIBjqkAZvzg7MXRSh1F%2F40Gv0PYFSaD4jYoBu7A65KN%2BgbeFFZGiEx7ckBYWco4eOFcxrpsWyaX14amkb8csMR7OSGJbNLL37tYQXgRlS%2FdqDLv%2FmUHmuhEoJtzi3k5HKGtUz2dzxZMHJ3FIyWHjpNvw1qVp7csNoqvWB%2ForjxeVa%2BSTjK%2Bf9GloROxmqdWZgCAjtlkMHaw7MByexZitugmFTNkykRX50f&X-Amz-Signature=32470a27eb65df6dbc0cb7281271290d71a8b0ff46ea4db05f9ad4c536e966df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X35IH7I%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2%2BTKP5ecN7BYMecD9IgSWw5d8pmIZ2%2FeG%2FIR2e3jJOAIhAOt%2FgmHRI3WxS4D1Ca3QzvSBbr1O8XAqJrv8eVDDBDRWKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyrsc6gyp%2BjQe1zmo4q3ANrB4QYBKQxTNkdOEvGdaasTu6WQoybfKwdX%2BTfM5TfbgUK77t5nsecf7YHfCmFmCQ73hvb9awlc5DpnDW%2BjHHXms2Oezsf7Wzx%2Bgyr5OaeffSUtqsqIhaO8vHdZOJh%2FpxOap16Cw5hHAZdhSnuAsNGIgtP1sa9mb%2FJWIqGTd9SeE2Hzp38GnlKy1Jo7xVrIwiVXyUS%2FJ1XKW%2FoQxnPcBdnQ1HVF7VCPjRSzT2j4mkLYu5eaKgo5de%2F9TVONoQ6%2Fa0pnfIYHCxqT2sznpmIt3Ir8eZRvoZNYnsrLWccnkxg%2B%2BexEi2eyKISTk4IETSX0qbx9kVNWF3wCce629ZnqdBiVP5ptDBRO580dpRGunUtl9%2F4A73eQqHM%2BWMRR0exjqrjjtBcAf5x8V5yoa%2FbT5U96MHwdQxjOFFTwqvId3PKATFVFHADx4JLrGNdHt6O0Y88TaPUpN3REQLXxE4558DmlQ1gYBtIZFf4KLpxlZIHPJPIJt3qzH%2FzIx1mg8Q2QOmuRb3y%2BGSFILEubfmbMxzHwQpWxrlQ2PmfdBMjTdD6ztwsk7xpmh5xiY6RuEbh6TVK%2BEhAks5L4IfAJbb0H1TNtttVsbnD%2F89YH6Pkh1AsqxC6t%2FCbctydlqZHXjDWmO%2FIBjqkAZvzg7MXRSh1F%2F40Gv0PYFSaD4jYoBu7A65KN%2BgbeFFZGiEx7ckBYWco4eOFcxrpsWyaX14amkb8csMR7OSGJbNLL37tYQXgRlS%2FdqDLv%2FmUHmuhEoJtzi3k5HKGtUz2dzxZMHJ3FIyWHjpNvw1qVp7csNoqvWB%2ForjxeVa%2BSTjK%2Bf9GloROxmqdWZgCAjtlkMHaw7MByexZitugmFTNkykRX50f&X-Amz-Signature=dda417dfed15fbc39a78f98daf7cff67ed38d84a84c63a23ef132fd35b97426e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

