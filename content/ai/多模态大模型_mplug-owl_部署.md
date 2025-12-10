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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAKI55X5%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCYmkAUM43GE9vDGdFO5M%2BxY4DD1ZjuTG1K6%2BfRR8xcagIhAPIhntOoy4LiedotrGsqg%2FLxvrD9EI5%2FhVcVuK1yIATVKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwAMQW7H%2F0WZbKfIlEq3AOMhjIrmnBMtAYq%2BneinzYcTfRPMm%2BMZdNts4yijJexg9bBTfb01goqI61Fj16PQhQlPr4AnASr02T2WcV4pb3F5twGBQPv38U1tq3mFRIcj5Z5fS1LHCo%2BMDd9oETFDrdjf3lH1nLQcYGIPtbDmy9iC56jQpgthbc%2FR2uIujUfTt91Q2zcDFyt0aLyHXPrBL%2FhIyo%2BNzCZLPWTtxX1adFmJ9TvT0eBjjdPpkoBRftvA8R1gMAi%2FeVEN7uTZL6FlBmNEdvOfbUt3vyI8wx9%2BjwnBr6W091acmrE6lPA7cA9d3bjylx1dxCH5%2B%2FLKR42jH0vbGE76U%2FY%2BRmLlJM1kiDCN5ORRa8VPshKQ6Abw4KykMrB4DxevA08cL1xgdZSoByiLUwbOr7a3q1oC1NrCjdEaa737lLSiZqhA%2Bp8YcHxbnkpOAmDhA1o9zSh6FRWEGo0DoB1rZBTzbVlAgm8HWIg%2BfOUf0SzSPaM5SAzI9FVSU3a%2FloddHaVnHspzhonNgEqRNEQ2mwASJn54Rs5HA1LF8M%2FQn3aCsCQrvSWAJOMXzilYGklo6rPl3XFrc7MgfPoVnDMumbM94%2FRahV2MzQ0qsaemGGVOab2SQD1sGfM%2Fo%2B7c930KF%2FYoz%2FubTD%2BvuPJBjqkAZe6K84wSrqjIKukN7ZcehnBoZj7IalGW71ZhO3NSq1rRk05VH9TqsNjfnTc6fxFtgGZAYkwSepodm1gVECPgELqckB3mIa8Jy1Haviur4uHdZQfkBuDaRXtcjyiVSubP5uokBCrUFDc2pHpxoGki%2BT%2F%2BXlyOST6zoxC9GkhJ6timZwRJvjcOtfqJBOkdzgPybwFOcBAPqxn%2BrhFtjI5J77LFODc&X-Amz-Signature=0916f01b98f26cac34418aa880d240a4f16cd40e954a5e71f9cb50866d27b8c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAKI55X5%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCYmkAUM43GE9vDGdFO5M%2BxY4DD1ZjuTG1K6%2BfRR8xcagIhAPIhntOoy4LiedotrGsqg%2FLxvrD9EI5%2FhVcVuK1yIATVKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwAMQW7H%2F0WZbKfIlEq3AOMhjIrmnBMtAYq%2BneinzYcTfRPMm%2BMZdNts4yijJexg9bBTfb01goqI61Fj16PQhQlPr4AnASr02T2WcV4pb3F5twGBQPv38U1tq3mFRIcj5Z5fS1LHCo%2BMDd9oETFDrdjf3lH1nLQcYGIPtbDmy9iC56jQpgthbc%2FR2uIujUfTt91Q2zcDFyt0aLyHXPrBL%2FhIyo%2BNzCZLPWTtxX1adFmJ9TvT0eBjjdPpkoBRftvA8R1gMAi%2FeVEN7uTZL6FlBmNEdvOfbUt3vyI8wx9%2BjwnBr6W091acmrE6lPA7cA9d3bjylx1dxCH5%2B%2FLKR42jH0vbGE76U%2FY%2BRmLlJM1kiDCN5ORRa8VPshKQ6Abw4KykMrB4DxevA08cL1xgdZSoByiLUwbOr7a3q1oC1NrCjdEaa737lLSiZqhA%2Bp8YcHxbnkpOAmDhA1o9zSh6FRWEGo0DoB1rZBTzbVlAgm8HWIg%2BfOUf0SzSPaM5SAzI9FVSU3a%2FloddHaVnHspzhonNgEqRNEQ2mwASJn54Rs5HA1LF8M%2FQn3aCsCQrvSWAJOMXzilYGklo6rPl3XFrc7MgfPoVnDMumbM94%2FRahV2MzQ0qsaemGGVOab2SQD1sGfM%2Fo%2B7c930KF%2FYoz%2FubTD%2BvuPJBjqkAZe6K84wSrqjIKukN7ZcehnBoZj7IalGW71ZhO3NSq1rRk05VH9TqsNjfnTc6fxFtgGZAYkwSepodm1gVECPgELqckB3mIa8Jy1Haviur4uHdZQfkBuDaRXtcjyiVSubP5uokBCrUFDc2pHpxoGki%2BT%2F%2BXlyOST6zoxC9GkhJ6timZwRJvjcOtfqJBOkdzgPybwFOcBAPqxn%2BrhFtjI5J77LFODc&X-Amz-Signature=50d729f5844b842fd2b584f7dd8564c575953adaa1444ddf2bf1690155a03cdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

