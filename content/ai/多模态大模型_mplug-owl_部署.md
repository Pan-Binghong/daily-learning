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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTQ4F65O%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIElB5aQmF%2Fbyz%2BujmYXlWMdKkE9aTSRs6CkdJ%2Faz7He7AiEA1FDBlhnEUi5dk7wW%2FybVuQxpmm2VslsH8SY4khxJIm4q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDLeqO%2BxntNm5%2BUVhiircA93suHp%2BiBQncV3FDJ5N%2BvGNHK4VbDtD2S9Fb1XIisSnxxwPjCQqIQ9Ah7aH0mqxFC78m9lQRXbGkPXpRYueWq2g%2B2SurrnoLJe%2FpxagiS2TCRRfLSF56L3Ena7cthEBkONCLave7%2Fg1AYG1sl1z9VdaUow4VGzQUFErS%2Ff9zLPxVaCmSlu3EDOKbyKXJKxEUjA%2B3v5jnBxF%2FvjLNUxzVnT8sT9BMkZUKmA%2B4a9sJq0jXPOO8F7mMab3%2F219JNUNN3GPX%2FMsQWY14ATNakcOtXTACf07RNzOtGkL%2BoWPhQm1Fg1GAp6kjRlcqkolCHNIIirSOo7Sgc9Ff0B%2Bc63GEGgS1suvdiK%2FO3SO3QjMH0RzpWld6fBxZoQKczG%2FlOmNcxec1FISC%2F7bFDSaeSDS1in0D3XP3qfvCCUSC7OU4cDFykjTyy5VYEvttLKaM2Y7k9OC3vf2%2FXvn6GHuUb5QkIGkx9xk7GiYqtu9v2HvRoxIBzE4VL%2Bc4MxG2UFk6oju1hTlPT%2BwhJ8jo%2FmSF2IV96kc5IWhHfvKfbbbV5yqxSE%2BIJpZa9J%2FL54KsjnCx2YkkT%2FZiI2pLLG%2Fu1PFqabcly%2BJLOp44chTRw1Tmwj6mDusci6k7Wqy2aupVWknMOae%2F8gGOqUB7I2KUHxfG4106l1JLXwaG4GjY%2Bdt4sqohwJXIfZNza7V3mrArqU0ZZ3r6OOzHPmdNAUIOcO9cRnxhIdf678eztKaz%2BqQVw0MsEUE9vmvRGMhSxbxJgrgbXsH9NtI2hxwbMn%2BP85jnn5pWCeAyjUthr8mfBJ6%2BBwD1fIFGlXfn5tO%2F3wSScurk3jcxT79nyPwZAEhS3m5USp6cY913V17Jg8xif8J&X-Amz-Signature=7ffcd6ce45bfa2c1f1c3ff4c28b2520a8203d64f12428c8991408bce87fddf7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTQ4F65O%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIElB5aQmF%2Fbyz%2BujmYXlWMdKkE9aTSRs6CkdJ%2Faz7He7AiEA1FDBlhnEUi5dk7wW%2FybVuQxpmm2VslsH8SY4khxJIm4q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDLeqO%2BxntNm5%2BUVhiircA93suHp%2BiBQncV3FDJ5N%2BvGNHK4VbDtD2S9Fb1XIisSnxxwPjCQqIQ9Ah7aH0mqxFC78m9lQRXbGkPXpRYueWq2g%2B2SurrnoLJe%2FpxagiS2TCRRfLSF56L3Ena7cthEBkONCLave7%2Fg1AYG1sl1z9VdaUow4VGzQUFErS%2Ff9zLPxVaCmSlu3EDOKbyKXJKxEUjA%2B3v5jnBxF%2FvjLNUxzVnT8sT9BMkZUKmA%2B4a9sJq0jXPOO8F7mMab3%2F219JNUNN3GPX%2FMsQWY14ATNakcOtXTACf07RNzOtGkL%2BoWPhQm1Fg1GAp6kjRlcqkolCHNIIirSOo7Sgc9Ff0B%2Bc63GEGgS1suvdiK%2FO3SO3QjMH0RzpWld6fBxZoQKczG%2FlOmNcxec1FISC%2F7bFDSaeSDS1in0D3XP3qfvCCUSC7OU4cDFykjTyy5VYEvttLKaM2Y7k9OC3vf2%2FXvn6GHuUb5QkIGkx9xk7GiYqtu9v2HvRoxIBzE4VL%2Bc4MxG2UFk6oju1hTlPT%2BwhJ8jo%2FmSF2IV96kc5IWhHfvKfbbbV5yqxSE%2BIJpZa9J%2FL54KsjnCx2YkkT%2FZiI2pLLG%2Fu1PFqabcly%2BJLOp44chTRw1Tmwj6mDusci6k7Wqy2aupVWknMOae%2F8gGOqUB7I2KUHxfG4106l1JLXwaG4GjY%2Bdt4sqohwJXIfZNza7V3mrArqU0ZZ3r6OOzHPmdNAUIOcO9cRnxhIdf678eztKaz%2BqQVw0MsEUE9vmvRGMhSxbxJgrgbXsH9NtI2hxwbMn%2BP85jnn5pWCeAyjUthr8mfBJ6%2BBwD1fIFGlXfn5tO%2F3wSScurk3jcxT79nyPwZAEhS3m5USp6cY913V17Jg8xif8J&X-Amz-Signature=9f509db45ca4dc46cc194799824308778458f742ba66a67998b67da1b3940595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

