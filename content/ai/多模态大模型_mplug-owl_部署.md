---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
标签:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7E7BZCK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUa6nIwcsX5sH%2F1IfO2LIXRqyvK0J1kLSGe7bPqoU4iAiBrO3Yb%2FmVY%2FvAVYW%2BY%2F6EoEzMHHmdDDnyLjXtK%2Ffdb8CqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUyJOQQdXWX1oaVQ%2BKtwDpnbWnnc88wurE7f5Ws16iQkGyStU%2FusOXFQ%2FSPQGqcorPh9gJOKDXv90dAJzaD9csYUBbuxDTNo4IjyRqBl%2B%2F5z5YSN0hF3gQN7hwLg5P7POQSJNP48q3xyrXaauycblYmBv87QA951ov4hK%2Fj7S412jjdwetZVom9szKrrijt%2FZLtstmRR68gMh45pCVdxXeJTJGaolQaM3xpjg93OcNlnxJcqwvjjEJQplZ0doifuYLFbxzc%2B5nfd5Vxb1mM6Iv4jvy%2FaI6Z6DdEFHU3JmMrcYvlRaVZv%2B4ie1C4DwiSom3W7etN4eH6E%2BWQeN9WO4ddIBY74L5JAguwH2plYIHC13bDYfCLlwvAPTm%2BPhKt4viegArvVZ32KVawyxhZyTWvok8sllKpnVbQeQ2do%2FiUyexfqtFloZlNObT56RjfAe7hBfWKODAqFcZtAMF3ONsNPU90TKo8YLCTkEWZ5mDiJL5bumwGT0QdZe8YiuJhojk%2Br5suKWLf2jKl4K4g8svoSayAQs%2BY1a%2FG04AkCMc7LAhZreXxdLVeboprXHnQctVho6LiJ%2BujCCywguCRDIt8wXIVzkH9zfg250KLUPuLAD4Viv8zPxv3%2BLZYnajRyb8VOqXCvCmKxKZggw76KsyAY6pgF9MFBRNiUZ05kwQ%2Bxec4ZJhbggVAPDJj3KRHHa72%2FBzWoj4XwRr1SwYw7hj5%2FtlUsaQOeLn5trz6Y2M27r7KKq1%2F%2BWGRkhSqel7NeL1cBXSLr3rEDpKF8Eg%2F1TcF1DWbb8PS%2FTj4ksKpyD7%2ByyCKDgihgl8IjVP9v0WnTmVq44k26k99O%2BnR2vdWqtBZCHgynyngXFFGJWVCGLZqk4LUJ%2Byk3MWiTw&X-Amz-Signature=1082be1c8894faeae215a9043a3e2ca93bca2759f04c903cff11637fb4fa8838&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7E7BZCK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUa6nIwcsX5sH%2F1IfO2LIXRqyvK0J1kLSGe7bPqoU4iAiBrO3Yb%2FmVY%2FvAVYW%2BY%2F6EoEzMHHmdDDnyLjXtK%2Ffdb8CqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUyJOQQdXWX1oaVQ%2BKtwDpnbWnnc88wurE7f5Ws16iQkGyStU%2FusOXFQ%2FSPQGqcorPh9gJOKDXv90dAJzaD9csYUBbuxDTNo4IjyRqBl%2B%2F5z5YSN0hF3gQN7hwLg5P7POQSJNP48q3xyrXaauycblYmBv87QA951ov4hK%2Fj7S412jjdwetZVom9szKrrijt%2FZLtstmRR68gMh45pCVdxXeJTJGaolQaM3xpjg93OcNlnxJcqwvjjEJQplZ0doifuYLFbxzc%2B5nfd5Vxb1mM6Iv4jvy%2FaI6Z6DdEFHU3JmMrcYvlRaVZv%2B4ie1C4DwiSom3W7etN4eH6E%2BWQeN9WO4ddIBY74L5JAguwH2plYIHC13bDYfCLlwvAPTm%2BPhKt4viegArvVZ32KVawyxhZyTWvok8sllKpnVbQeQ2do%2FiUyexfqtFloZlNObT56RjfAe7hBfWKODAqFcZtAMF3ONsNPU90TKo8YLCTkEWZ5mDiJL5bumwGT0QdZe8YiuJhojk%2Br5suKWLf2jKl4K4g8svoSayAQs%2BY1a%2FG04AkCMc7LAhZreXxdLVeboprXHnQctVho6LiJ%2BujCCywguCRDIt8wXIVzkH9zfg250KLUPuLAD4Viv8zPxv3%2BLZYnajRyb8VOqXCvCmKxKZggw76KsyAY6pgF9MFBRNiUZ05kwQ%2Bxec4ZJhbggVAPDJj3KRHHa72%2FBzWoj4XwRr1SwYw7hj5%2FtlUsaQOeLn5trz6Y2M27r7KKq1%2F%2BWGRkhSqel7NeL1cBXSLr3rEDpKF8Eg%2F1TcF1DWbb8PS%2FTj4ksKpyD7%2ByyCKDgihgl8IjVP9v0WnTmVq44k26k99O%2BnR2vdWqtBZCHgynyngXFFGJWVCGLZqk4LUJ%2Byk3MWiTw&X-Amz-Signature=8669da52c5bcc23a268941e5d804201cde9a8584f1ea843727300b391ecc82c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

