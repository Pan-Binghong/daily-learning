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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJTDTLN%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGjMnDruiuaA1VRqW7eq6rQUrxrpCG7fdEpSLJyWdivgIhALQc44cT%2BRC4CJ1qWyz0fLwg4seonAacBEI%2BXybSluXvKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVowTbgItVDcHj1TYq3AOWznBwin29FVIPa%2Bo8%2Fs1im1Hck309XDPyDTMxUy6mym88epneZJ%2FK%2B%2Boe4WaVQ%2By888mYLhSmNuwB2xZD1aRaCUD3l97NOmdsu2xtH5s2LnXUoIJqgsRynm9k47cpJ1HSl3lC7pqy84gemhE7VtzdT6zPrA8OXdv90RssZNSm1kRsM6mTgNKrIGOQIBR8DowIl%2Bu6ZwLvjkrGH7o5%2F9YipMwuabjoRNkTWJqISrPvan4cIWGOEvI%2F4IAS1hNrN60aCrSu%2FyUjFGZCJhsXmSTu2D66%2Bf8czRG5MpTUHts9nU3Q0BdZjz2FBnqP04AF6O4qcF5SS1FTGqLLADqPjknDw8V1Usu9Ygj%2FgWwDvndV5IjsZJK7mCZaHoF0lyjFG%2BzOeoScRncy7LtZxAhG3lrO69bm7qgwc%2Fw8hwyCB1wbbnkgLFMcAvPRTh22Ig96vwB53k3VKdFJHSJRt%2Bn3uI0wKE8NnRlXLtbumnYNNzo7u8rR0cdtzH86B67%2BevHUXwOHAhZtgSLDBU9EI56rb2Q21JuGE7KDL7ww%2FIpUlMJUbVmVQxuMrl%2B9I%2F4Ztk3bvA1z5JM3hfjsKfpmf6WB5ZgFxiwKpw6ySDEwQh4s05P0dG1fBbVcA0vtBIn0ITCE9brLBjqkAXfa0YFpo3UwhEdA4zJwB%2Fe1soUfUi%2FmqhZ2wfzIpYdVkHB6FdeRYyYKe3BNSCqnXfZT3zWikTvwraqRagzbG%2Big3iKhAOTzQ2gmvvZ06q2tc1W0lL2RObKPt0cklaIVs3hg1vrfpi3TmpDS6E56CTvwMuiP%2F3sCoJ0VeAf%2B%2BodqHRKaVS4dRIXU1TO%2BemFGdIuiJl99sS55ezvRJjRG42rXP%2BW7&X-Amz-Signature=5ba4764d33641b4a0aa68be8118c947d7313146a185dc6e9d86841d61200ad20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJTDTLN%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGjMnDruiuaA1VRqW7eq6rQUrxrpCG7fdEpSLJyWdivgIhALQc44cT%2BRC4CJ1qWyz0fLwg4seonAacBEI%2BXybSluXvKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVowTbgItVDcHj1TYq3AOWznBwin29FVIPa%2Bo8%2Fs1im1Hck309XDPyDTMxUy6mym88epneZJ%2FK%2B%2Boe4WaVQ%2By888mYLhSmNuwB2xZD1aRaCUD3l97NOmdsu2xtH5s2LnXUoIJqgsRynm9k47cpJ1HSl3lC7pqy84gemhE7VtzdT6zPrA8OXdv90RssZNSm1kRsM6mTgNKrIGOQIBR8DowIl%2Bu6ZwLvjkrGH7o5%2F9YipMwuabjoRNkTWJqISrPvan4cIWGOEvI%2F4IAS1hNrN60aCrSu%2FyUjFGZCJhsXmSTu2D66%2Bf8czRG5MpTUHts9nU3Q0BdZjz2FBnqP04AF6O4qcF5SS1FTGqLLADqPjknDw8V1Usu9Ygj%2FgWwDvndV5IjsZJK7mCZaHoF0lyjFG%2BzOeoScRncy7LtZxAhG3lrO69bm7qgwc%2Fw8hwyCB1wbbnkgLFMcAvPRTh22Ig96vwB53k3VKdFJHSJRt%2Bn3uI0wKE8NnRlXLtbumnYNNzo7u8rR0cdtzH86B67%2BevHUXwOHAhZtgSLDBU9EI56rb2Q21JuGE7KDL7ww%2FIpUlMJUbVmVQxuMrl%2B9I%2F4Ztk3bvA1z5JM3hfjsKfpmf6WB5ZgFxiwKpw6ySDEwQh4s05P0dG1fBbVcA0vtBIn0ITCE9brLBjqkAXfa0YFpo3UwhEdA4zJwB%2Fe1soUfUi%2FmqhZ2wfzIpYdVkHB6FdeRYyYKe3BNSCqnXfZT3zWikTvwraqRagzbG%2Big3iKhAOTzQ2gmvvZ06q2tc1W0lL2RObKPt0cklaIVs3hg1vrfpi3TmpDS6E56CTvwMuiP%2F3sCoJ0VeAf%2B%2BodqHRKaVS4dRIXU1TO%2BemFGdIuiJl99sS55ezvRJjRG42rXP%2BW7&X-Amz-Signature=eb1d937d1d1ecb97e384e4d1c03c910b92be06b2349a9773003f42c937456aae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PJTDTLN%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGjMnDruiuaA1VRqW7eq6rQUrxrpCG7fdEpSLJyWdivgIhALQc44cT%2BRC4CJ1qWyz0fLwg4seonAacBEI%2BXybSluXvKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVowTbgItVDcHj1TYq3AOWznBwin29FVIPa%2Bo8%2Fs1im1Hck309XDPyDTMxUy6mym88epneZJ%2FK%2B%2Boe4WaVQ%2By888mYLhSmNuwB2xZD1aRaCUD3l97NOmdsu2xtH5s2LnXUoIJqgsRynm9k47cpJ1HSl3lC7pqy84gemhE7VtzdT6zPrA8OXdv90RssZNSm1kRsM6mTgNKrIGOQIBR8DowIl%2Bu6ZwLvjkrGH7o5%2F9YipMwuabjoRNkTWJqISrPvan4cIWGOEvI%2F4IAS1hNrN60aCrSu%2FyUjFGZCJhsXmSTu2D66%2Bf8czRG5MpTUHts9nU3Q0BdZjz2FBnqP04AF6O4qcF5SS1FTGqLLADqPjknDw8V1Usu9Ygj%2FgWwDvndV5IjsZJK7mCZaHoF0lyjFG%2BzOeoScRncy7LtZxAhG3lrO69bm7qgwc%2Fw8hwyCB1wbbnkgLFMcAvPRTh22Ig96vwB53k3VKdFJHSJRt%2Bn3uI0wKE8NnRlXLtbumnYNNzo7u8rR0cdtzH86B67%2BevHUXwOHAhZtgSLDBU9EI56rb2Q21JuGE7KDL7ww%2FIpUlMJUbVmVQxuMrl%2B9I%2F4Ztk3bvA1z5JM3hfjsKfpmf6WB5ZgFxiwKpw6ySDEwQh4s05P0dG1fBbVcA0vtBIn0ITCE9brLBjqkAXfa0YFpo3UwhEdA4zJwB%2Fe1soUfUi%2FmqhZ2wfzIpYdVkHB6FdeRYyYKe3BNSCqnXfZT3zWikTvwraqRagzbG%2Big3iKhAOTzQ2gmvvZ06q2tc1W0lL2RObKPt0cklaIVs3hg1vrfpi3TmpDS6E56CTvwMuiP%2F3sCoJ0VeAf%2B%2BodqHRKaVS4dRIXU1TO%2BemFGdIuiJl99sS55ezvRJjRG42rXP%2BW7&X-Amz-Signature=bb00b31ce7741852b27019f12373b75a034af10c2cbbba6315b0987fd55c4e81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

