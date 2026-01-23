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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT7WKEW%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIGPtYtGJb0mDzPbgOY0E3q4rw89PkMaYJXaiCskiM5fLAiAFdFmwmYc4Vw7NGC4vd5vmFSOJX2b15E2AITE21ZnPXiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJnMshnCVPl%2F4E95BKtwDgeEw1eWlcrh3NsKYISyRO7JPHui6I9Y36ID4VzEi5t%2B7PiZfNUdWrPMuzb5wZVaU5evksFDwUvTHBSDt4q0%2FbEkh9lKObIONJkJ88blaywV8MHzY1Ni2izDMOkvA%2FW8CQHgeJiLN3cnJo89xfnl5b6WV5CMU%2BGnoMVZlKSrdH7hW6k4U%2BSGcfHGiFg26kMcsXsgpeaLimLrDDfi8P9WiRJ7JZOLksh4zhTFR4u3QjAJkptbUsgoqIC4%2F1bYc9%2FAqoEXwPw6thwUHfQ4oYRj68GiKzTZ%2F8d1IMSVxuxexAzdF1csUos24f4I21AtPbNwBQPfOFiLpO8i1CqSD4gA2KiLIB7s4DbYQsIlDga0gxnnmn2VW2Tm%2FwY33TX8kIEOOtaat5s8drf43a1creEJeu6YD%2Fh0dvAnyJN%2BpEAFfo%2Boptb9xaZtJfEqKMKRrje7UxChg1QDVAOW5UuD5l10Pk9S08qcvS5CC5MaXofH%2Bct0YDqhaWLTIL7Fc%2FVaQ3MkYF3135dnPVLIuQBGmhplGyXFwSar3rhYFnLAjF%2F%2BA5umCgT3n65dGCCI5u5guhCEzxNWh9IhHguvhVghUUeMr26l2fWq4%2B85Icvqs43hr5Q%2BkLUrES1R%2BX69ZXJ0w5q7LywY6pgHgu1gl%2BPFawANXFR9kDRViF77Uhpz7FRrMwrhCdVgDgiHpJ%2BHEPqaZHLnBLJ8XjlRVxFwgV%2FvbMnHZMejcXPdaaIX6VgD8tlUwh86mbfTqahKs6NLWEjqzkHu8Vw0OEZmZume7%2BGE8IQDWdF5RrTCuPumoWpK%2Bp5dFBmIUuxs%2FLh0xOGzOre%2BKa4PyYrf0e2VVaPxq6FbUPF5s60khhZnAbADKT2Kz&X-Amz-Signature=a2bba02669c6cd39b3ececc1b1d1b07cc3fc063b4429c1fb680cab6a51b6f335&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT7WKEW%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIGPtYtGJb0mDzPbgOY0E3q4rw89PkMaYJXaiCskiM5fLAiAFdFmwmYc4Vw7NGC4vd5vmFSOJX2b15E2AITE21ZnPXiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJnMshnCVPl%2F4E95BKtwDgeEw1eWlcrh3NsKYISyRO7JPHui6I9Y36ID4VzEi5t%2B7PiZfNUdWrPMuzb5wZVaU5evksFDwUvTHBSDt4q0%2FbEkh9lKObIONJkJ88blaywV8MHzY1Ni2izDMOkvA%2FW8CQHgeJiLN3cnJo89xfnl5b6WV5CMU%2BGnoMVZlKSrdH7hW6k4U%2BSGcfHGiFg26kMcsXsgpeaLimLrDDfi8P9WiRJ7JZOLksh4zhTFR4u3QjAJkptbUsgoqIC4%2F1bYc9%2FAqoEXwPw6thwUHfQ4oYRj68GiKzTZ%2F8d1IMSVxuxexAzdF1csUos24f4I21AtPbNwBQPfOFiLpO8i1CqSD4gA2KiLIB7s4DbYQsIlDga0gxnnmn2VW2Tm%2FwY33TX8kIEOOtaat5s8drf43a1creEJeu6YD%2Fh0dvAnyJN%2BpEAFfo%2Boptb9xaZtJfEqKMKRrje7UxChg1QDVAOW5UuD5l10Pk9S08qcvS5CC5MaXofH%2Bct0YDqhaWLTIL7Fc%2FVaQ3MkYF3135dnPVLIuQBGmhplGyXFwSar3rhYFnLAjF%2F%2BA5umCgT3n65dGCCI5u5guhCEzxNWh9IhHguvhVghUUeMr26l2fWq4%2B85Icvqs43hr5Q%2BkLUrES1R%2BX69ZXJ0w5q7LywY6pgHgu1gl%2BPFawANXFR9kDRViF77Uhpz7FRrMwrhCdVgDgiHpJ%2BHEPqaZHLnBLJ8XjlRVxFwgV%2FvbMnHZMejcXPdaaIX6VgD8tlUwh86mbfTqahKs6NLWEjqzkHu8Vw0OEZmZume7%2BGE8IQDWdF5RrTCuPumoWpK%2Bp5dFBmIUuxs%2FLh0xOGzOre%2BKa4PyYrf0e2VVaPxq6FbUPF5s60khhZnAbADKT2Kz&X-Amz-Signature=921f38ab94d7bad4874e96483ffc91d3f3b8a76969fbecca0cb604e822ddc3fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

