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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZGELFBB%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCycOZZIXWQPmTL4C4i%2B53QBj8shl5NvjA%2FrWa9m9bBwwIhAMWWMaRmLxGoA%2BZBfijA98gxcZma7Rn8Ln%2B5R5g%2BsLQdKv8DCEMQABoMNjM3NDIzMTgzODA1IgwN%2B%2B9SEiygJFsyeooq3APjlOlg4Rs%2Bg3OSNI0r8PmtX9o8P4s8xjO6pP8DiSqPuDu8%2BDJyrQjXzbbGlaY2xcXDjbyjdY2v6%2FTwJrW1by5SFE%2BghZSDuR1U2xlKukJ986eypWstXbzRQ0IMByVeklp%2Btjws4D4LG5CyMAZZLDWtZ3XXD8VWZnGSSyEroB3DbpPr2T74ju4To7PXifJ6C887WczbceiYGjCb%2Bs1rz1cq5TMAc3xzPiIPM7qPw5GUClpv2QStLqR3Ex%2Fn%2F%2BqFT9cHIO1Pefjl4CDk%2B%2FLV5bb36sJcQg5S1D70EDDHB5hXcPt%2FqtZBuSJYYQoHUQleU8Pq1BgyXzbYHAoZrITDoXmg5QVpz1BUZqE%2FGIuF2nIy3g4TNaaObQQJj8kuIyLC8jG2VB7icXlZdUm3K%2Bo5bW5cVE%2FP2N%2B2Kg4CC0HxuJU3ff0KIvE7HHxGf8ns8DcnywlN05MkTQQuNkKWCf%2BI08kkVJjy7q1GTNRdexjJcDW%2Bs8hkths5taetYv98Yqtji2HyFA0ZPWXMxPyAZAUKQKho%2FBrIJM%2BY%2Bgb28UGx62fv3wBzl71HC1iREJe%2Fj9n0t5MMK1gAxI8CpJX5iqvGUm6CycgTFiJcxJ71OADPdgsbC5P4%2FWWZpTA3Wgh2ODD%2Bv6bLBjqkAQcC5QMnjaLstvp2gkxkipuMRabdJsumtfTTwZiHOJ0AtcOBSWjUkq7UDCNlX8QW%2FqBLcwyQmmTMzIAo86Ekb99HMDb%2BQ7cF%2B4cHod5SZ7gNNaH9WI1tMPDqULDrVtkRm9Rc0BLZdHBj8Ao2C3gY6kKPNgiUNs%2Bq5K7llCjdyiFdYv5DJeyING4FpPrV0q3KnbBwSD2NL9KL%2BkTZ91zhPn5HVtdm&X-Amz-Signature=a618f7ceb59a9d21bc3e6b262c03f4f5e80d1c2196ac08ec363dcf50af996fca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZGELFBB%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCycOZZIXWQPmTL4C4i%2B53QBj8shl5NvjA%2FrWa9m9bBwwIhAMWWMaRmLxGoA%2BZBfijA98gxcZma7Rn8Ln%2B5R5g%2BsLQdKv8DCEMQABoMNjM3NDIzMTgzODA1IgwN%2B%2B9SEiygJFsyeooq3APjlOlg4Rs%2Bg3OSNI0r8PmtX9o8P4s8xjO6pP8DiSqPuDu8%2BDJyrQjXzbbGlaY2xcXDjbyjdY2v6%2FTwJrW1by5SFE%2BghZSDuR1U2xlKukJ986eypWstXbzRQ0IMByVeklp%2Btjws4D4LG5CyMAZZLDWtZ3XXD8VWZnGSSyEroB3DbpPr2T74ju4To7PXifJ6C887WczbceiYGjCb%2Bs1rz1cq5TMAc3xzPiIPM7qPw5GUClpv2QStLqR3Ex%2Fn%2F%2BqFT9cHIO1Pefjl4CDk%2B%2FLV5bb36sJcQg5S1D70EDDHB5hXcPt%2FqtZBuSJYYQoHUQleU8Pq1BgyXzbYHAoZrITDoXmg5QVpz1BUZqE%2FGIuF2nIy3g4TNaaObQQJj8kuIyLC8jG2VB7icXlZdUm3K%2Bo5bW5cVE%2FP2N%2B2Kg4CC0HxuJU3ff0KIvE7HHxGf8ns8DcnywlN05MkTQQuNkKWCf%2BI08kkVJjy7q1GTNRdexjJcDW%2Bs8hkths5taetYv98Yqtji2HyFA0ZPWXMxPyAZAUKQKho%2FBrIJM%2BY%2Bgb28UGx62fv3wBzl71HC1iREJe%2Fj9n0t5MMK1gAxI8CpJX5iqvGUm6CycgTFiJcxJ71OADPdgsbC5P4%2FWWZpTA3Wgh2ODD%2Bv6bLBjqkAQcC5QMnjaLstvp2gkxkipuMRabdJsumtfTTwZiHOJ0AtcOBSWjUkq7UDCNlX8QW%2FqBLcwyQmmTMzIAo86Ekb99HMDb%2BQ7cF%2B4cHod5SZ7gNNaH9WI1tMPDqULDrVtkRm9Rc0BLZdHBj8Ao2C3gY6kKPNgiUNs%2Bq5K7llCjdyiFdYv5DJeyING4FpPrV0q3KnbBwSD2NL9KL%2BkTZ91zhPn5HVtdm&X-Amz-Signature=40944ccc4349acccc54ec3b3a50a96d71bd4526564957c8cc291b83bd2df6f89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

