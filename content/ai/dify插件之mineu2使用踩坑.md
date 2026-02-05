---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTPCIAYQ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIDW5kIICfbfkb%2BQhivVLCDhoD9r5NUyrFvGn3%2BkJM9lnAiA1OiriXRTU7ROJydkMmzm5QOt8MrM3VaOPH7YlIgq%2Bkyr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMRKIY6eEBGaSzspvvKtwD6womImw91z%2F1jIBTHzqSjoWclvDt8WwINi7tQ404gkWH%2Bj2OmCrpS2g1fu8oQIbGroW5zZbTMiCgBH%2Bh%2BsETaHh9WCTTKTHbkUiiChF%2BTd4FzWqLUWYDuOacFVketq2%2F7mcJpmu8UX5ygQM%2BcBkQ7V0Dqq0RQRhTR2XgFcGoU6LZT8BmxFuf%2FcoOk8k3iSZAfX29OALQpXwXFHJudb9TADjlTpKlCRkGFnnNtm%2ByWxGir5xO7hMj9UWwo4L%2FwsDKIs%2FSgFUdDPDcwRLLBQZqSyjrJK6p2fKKnlqRgm3zDJRWVEUxzpJRiho2CJYO8VHfdILGaQouFDWafTBRs2TshwREEv9BnCijY5BvD5KoRaWYPFcEOvPttjy4e9K9KIKlqDJP5Khe8FzcRbnU2VNIQzdyCROXIt7nojS8dYflY4eLA3H6ELtHbrWDAP0mS7Fj%2BKTr6KkWwQaR2X9Ia2T78uZv8wLOrV0BCWlGQDHARHO4xiOSebykoeQ1ymKa534igp46xkVQS0pv9xulYZPRrAKFIsBwYm6%2F3UE5%2BcsilZSj%2BdzapfVOX29UZiX7eKmNz6Ji%2BXn5katoIqnHABnuEv47dYFhKO%2FSHgkOKOicx8EQ1apX02soP0ECzSIw7ZKQzAY6pgH3pIvQ8%2FAAQpa%2FXXIUhzL4SNjzorFX9tR2FfarEzf%2FPDGrwS0Ba1m1u9VjKmCO67Ke4EFcGabWAehLfezd%2B3sHorYZSk6po2XERJcg%2BouqdVz1mn3qSCyUn27Z1O0HlhGsigZijwieBBZzWcQvu3IUGx%2FmsUWN%2BQID%2FErfy3eraia2rtuyEHglNAj%2B61ippUb3BAnb9JIx24YbolWpDdkwTDbkzdiu&X-Amz-Signature=642920cc40657e6b689277cdf5a917d4cda4b539e03bc977063cff28f14e94ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTPCIAYQ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIDW5kIICfbfkb%2BQhivVLCDhoD9r5NUyrFvGn3%2BkJM9lnAiA1OiriXRTU7ROJydkMmzm5QOt8MrM3VaOPH7YlIgq%2Bkyr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMRKIY6eEBGaSzspvvKtwD6womImw91z%2F1jIBTHzqSjoWclvDt8WwINi7tQ404gkWH%2Bj2OmCrpS2g1fu8oQIbGroW5zZbTMiCgBH%2Bh%2BsETaHh9WCTTKTHbkUiiChF%2BTd4FzWqLUWYDuOacFVketq2%2F7mcJpmu8UX5ygQM%2BcBkQ7V0Dqq0RQRhTR2XgFcGoU6LZT8BmxFuf%2FcoOk8k3iSZAfX29OALQpXwXFHJudb9TADjlTpKlCRkGFnnNtm%2ByWxGir5xO7hMj9UWwo4L%2FwsDKIs%2FSgFUdDPDcwRLLBQZqSyjrJK6p2fKKnlqRgm3zDJRWVEUxzpJRiho2CJYO8VHfdILGaQouFDWafTBRs2TshwREEv9BnCijY5BvD5KoRaWYPFcEOvPttjy4e9K9KIKlqDJP5Khe8FzcRbnU2VNIQzdyCROXIt7nojS8dYflY4eLA3H6ELtHbrWDAP0mS7Fj%2BKTr6KkWwQaR2X9Ia2T78uZv8wLOrV0BCWlGQDHARHO4xiOSebykoeQ1ymKa534igp46xkVQS0pv9xulYZPRrAKFIsBwYm6%2F3UE5%2BcsilZSj%2BdzapfVOX29UZiX7eKmNz6Ji%2BXn5katoIqnHABnuEv47dYFhKO%2FSHgkOKOicx8EQ1apX02soP0ECzSIw7ZKQzAY6pgH3pIvQ8%2FAAQpa%2FXXIUhzL4SNjzorFX9tR2FfarEzf%2FPDGrwS0Ba1m1u9VjKmCO67Ke4EFcGabWAehLfezd%2B3sHorYZSk6po2XERJcg%2BouqdVz1mn3qSCyUn27Z1O0HlhGsigZijwieBBZzWcQvu3IUGx%2FmsUWN%2BQID%2FErfy3eraia2rtuyEHglNAj%2B61ippUb3BAnb9JIx24YbolWpDdkwTDbkzdiu&X-Amz-Signature=2b208d47f7578d7975a2db788fcaa5656f093588389b992066777464f0981ce1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



