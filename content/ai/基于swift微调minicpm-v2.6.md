---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7TOGEO4%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDX0QipP74QyJzLioAmFER2x%2BJreEXulv2100HAMaOSAwIgQVSkO2hkrlalHDSmVNo8iTaq8a4DwTN%2FvRLhDvC5Hg0q%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNsfHXm2qk8J4E6zvircA3v27g35gNaZhr2YkZZ6BBdsKacNpjrmvAcM1NjGzdiKwta%2FOSM%2FUh92ZajA7EPxCnVkTPwf6337SKF2l0jV8soieoBJatzJEx1%2FMF%2FjbWcPseexd8l1efqzRoSk72kuJlnclQvKYEbfegZJ%2B6cQ0foFGnmAAg7YEyHsa63ql2G1%2BKawGtrnhkU3FoHew3JHy82%2FxkmnSmDhmWJtNKQk70w0LZ15jlW%2FwdqrQ6Y%2BHf%2Ft4WN%2BXE%2B%2F2cRYo9rhEmMPJ3%2F8Ejia%2BiP8OMmQGRncvi5ZcWlqX6dt0vNdMvWUBcu8tQ1DdZZSmv%2FwDGpsTkK7PJ1s0ce0msZOKiYI%2BYfrJVu2XoZAW%2BeuqJKG%2Bt6OWfdkO9fX5r3JdBxCj0O73LOr2uHqwaBE%2BMU0k%2B42m%2BbsGpwQwoLUAb2T4%2FifpQ4TW9av1yvCzI%2FQZeoxBwjvlJv%2FDYQR%2FNQJ49Fk3bf%2BGF%2FECTlMB3ubhCqErt4bYURmqOqHaEOHJwBcB0TZVZfvB2niXJy3IXeeSV7lxPAlsDD0MAvfSs8RFtvS3xNH1%2FVxosfdwpHMAi2DbNZqii1DyHVisY%2FE8iOC2E1%2FRdZIBOuRxdfkDn1IyS5LKFd4V%2FmyJEvzfo6pUnG%2Bk0sZlIkrMMGkps8GOqUB9A1umNTZPC46%2FY2BlX%2BPatULzhpk1HHLzF3itpbs5Tpky3MxEq%2FEH62wMmNDBwKWCsNeRnX%2FTRn5QtdY55%2F99VqbbM53daJmoEciYhAv3zf5rdgsGYUAk4Oy4E4GrYIidJmkmTMC%2F2DftThhRfk2rMms6wUlbjV62IAkkNeHYOqQOf%2FCpD3OKNgOpblLbA%2BT%2Biuk2PQ3QjHPc%2BO3aXvAtEnx87i7&X-Amz-Signature=79140784286d52d266c347d4558f524dd67c9bd04d3ceb4f47d656f993f4ea28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7TOGEO4%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDX0QipP74QyJzLioAmFER2x%2BJreEXulv2100HAMaOSAwIgQVSkO2hkrlalHDSmVNo8iTaq8a4DwTN%2FvRLhDvC5Hg0q%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNsfHXm2qk8J4E6zvircA3v27g35gNaZhr2YkZZ6BBdsKacNpjrmvAcM1NjGzdiKwta%2FOSM%2FUh92ZajA7EPxCnVkTPwf6337SKF2l0jV8soieoBJatzJEx1%2FMF%2FjbWcPseexd8l1efqzRoSk72kuJlnclQvKYEbfegZJ%2B6cQ0foFGnmAAg7YEyHsa63ql2G1%2BKawGtrnhkU3FoHew3JHy82%2FxkmnSmDhmWJtNKQk70w0LZ15jlW%2FwdqrQ6Y%2BHf%2Ft4WN%2BXE%2B%2F2cRYo9rhEmMPJ3%2F8Ejia%2BiP8OMmQGRncvi5ZcWlqX6dt0vNdMvWUBcu8tQ1DdZZSmv%2FwDGpsTkK7PJ1s0ce0msZOKiYI%2BYfrJVu2XoZAW%2BeuqJKG%2Bt6OWfdkO9fX5r3JdBxCj0O73LOr2uHqwaBE%2BMU0k%2B42m%2BbsGpwQwoLUAb2T4%2FifpQ4TW9av1yvCzI%2FQZeoxBwjvlJv%2FDYQR%2FNQJ49Fk3bf%2BGF%2FECTlMB3ubhCqErt4bYURmqOqHaEOHJwBcB0TZVZfvB2niXJy3IXeeSV7lxPAlsDD0MAvfSs8RFtvS3xNH1%2FVxosfdwpHMAi2DbNZqii1DyHVisY%2FE8iOC2E1%2FRdZIBOuRxdfkDn1IyS5LKFd4V%2FmyJEvzfo6pUnG%2Bk0sZlIkrMMGkps8GOqUB9A1umNTZPC46%2FY2BlX%2BPatULzhpk1HHLzF3itpbs5Tpky3MxEq%2FEH62wMmNDBwKWCsNeRnX%2FTRn5QtdY55%2F99VqbbM53daJmoEciYhAv3zf5rdgsGYUAk4Oy4E4GrYIidJmkmTMC%2F2DftThhRfk2rMms6wUlbjV62IAkkNeHYOqQOf%2FCpD3OKNgOpblLbA%2BT%2Biuk2PQ3QjHPc%2BO3aXvAtEnx87i7&X-Amz-Signature=89aecd25950c1ae88e0b558fdc5e4842cc09c8f0b183bd600ddf4ef2ca2ad00f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7TOGEO4%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDX0QipP74QyJzLioAmFER2x%2BJreEXulv2100HAMaOSAwIgQVSkO2hkrlalHDSmVNo8iTaq8a4DwTN%2FvRLhDvC5Hg0q%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNsfHXm2qk8J4E6zvircA3v27g35gNaZhr2YkZZ6BBdsKacNpjrmvAcM1NjGzdiKwta%2FOSM%2FUh92ZajA7EPxCnVkTPwf6337SKF2l0jV8soieoBJatzJEx1%2FMF%2FjbWcPseexd8l1efqzRoSk72kuJlnclQvKYEbfegZJ%2B6cQ0foFGnmAAg7YEyHsa63ql2G1%2BKawGtrnhkU3FoHew3JHy82%2FxkmnSmDhmWJtNKQk70w0LZ15jlW%2FwdqrQ6Y%2BHf%2Ft4WN%2BXE%2B%2F2cRYo9rhEmMPJ3%2F8Ejia%2BiP8OMmQGRncvi5ZcWlqX6dt0vNdMvWUBcu8tQ1DdZZSmv%2FwDGpsTkK7PJ1s0ce0msZOKiYI%2BYfrJVu2XoZAW%2BeuqJKG%2Bt6OWfdkO9fX5r3JdBxCj0O73LOr2uHqwaBE%2BMU0k%2B42m%2BbsGpwQwoLUAb2T4%2FifpQ4TW9av1yvCzI%2FQZeoxBwjvlJv%2FDYQR%2FNQJ49Fk3bf%2BGF%2FECTlMB3ubhCqErt4bYURmqOqHaEOHJwBcB0TZVZfvB2niXJy3IXeeSV7lxPAlsDD0MAvfSs8RFtvS3xNH1%2FVxosfdwpHMAi2DbNZqii1DyHVisY%2FE8iOC2E1%2FRdZIBOuRxdfkDn1IyS5LKFd4V%2FmyJEvzfo6pUnG%2Bk0sZlIkrMMGkps8GOqUB9A1umNTZPC46%2FY2BlX%2BPatULzhpk1HHLzF3itpbs5Tpky3MxEq%2FEH62wMmNDBwKWCsNeRnX%2FTRn5QtdY55%2F99VqbbM53daJmoEciYhAv3zf5rdgsGYUAk4Oy4E4GrYIidJmkmTMC%2F2DftThhRfk2rMms6wUlbjV62IAkkNeHYOqQOf%2FCpD3OKNgOpblLbA%2BT%2Biuk2PQ3QjHPc%2BO3aXvAtEnx87i7&X-Amz-Signature=251824bfc5e9c113fb4f80b52317fe9aba34e46bae380cde62ea25f2cfc95626&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

