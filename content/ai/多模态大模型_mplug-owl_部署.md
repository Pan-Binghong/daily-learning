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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6HFGUIL%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQD2NjaEO6Cf3avmAzP4qhjBkBPoYj8qzkl9rxttjmU7rQIhAOfaC4xNftAotrDoA6RsFG89rysBjhof%2BC0j11woLjYuKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp2XwZG9iZN0E4i7cq3AO0Ossbu1HDS0A0sc6FNrGKdPUdCOQsIf9ceeX6TjukxUMXWGgHCe%2F1yLjq9UAGe06LUx9twA0Qf7WfTq6T43bYtUpVHUl8fl1P3EylxwQBmgHnimTGsERKszPFzrZ3nzjFi1Nx%2B%2BaanVrbg2z9ViF1hEkivAb4HVWic%2Fc%2F8CN8itCmo%2BvGEStjYGVogGPbv2OEWGp6IR%2BAnpWIMCQ9iKEZiYV9%2FShi3qeUS3xRksbD9snzj4z1wMg%2FmcrbOiktA9WTay%2B0HL9C9jYhZQyR0AyM60E2U2BNQQtm8FiiW9gk1CsY9giymmSxlPb5Z92S2TKF9dLwqgnD2g3T1RMp9LjqsKZFTd74ZoN7ixf2MUMHv3eFk59I63S23cTusOfGwHsPWkPUWFpLGDRpGIo6sf1BvnGC%2FT3lhKQA%2FZsLPbGg%2Bne%2F0isYCN97auCv0lSto8fYsuEfat7jGEzlfa0TSFkSbEru6aFUq16vXnSC9cZ9o0YrtTnpKYKW5ayRgkSZAnm%2FsxieDb3uDPITwKct6fjSAXK0dKuzXGE9uPFsGmrJtQdmqennGioYzPTxZGiUcsoSCtRg%2By8CbKx%2FuTGVT%2FLy83EyjrAZz0uFsVFE0D24QST%2FyAenliPRGWbjEjCk0LrIBjqkAQil4Fzr%2FIvle82HkFR2t6qhPhc%2FdUtUlK%2FniO1lMtN2rCuGdWlb2LBstTnC14drpFzxE3nFfGfVdvyEhFNCWHt8bTO%2BvyePnE4aTVQkz%2B0SstT64cMRN9IW%2BCEdgKRzWYuiYWMFl%2B%2FOhfECR56xJwC3c56Klgk1S0cuzT6GGP9zRSm2uBwY4J%2FuUXXcEKMnlBpcoFtYFJbtB7hC7%2BT8W0NHM7ma&X-Amz-Signature=fee2568a02a5d0b54ad2a5ef9ab75ed47853527907ff1d882f1e3e484fa345cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6HFGUIL%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQD2NjaEO6Cf3avmAzP4qhjBkBPoYj8qzkl9rxttjmU7rQIhAOfaC4xNftAotrDoA6RsFG89rysBjhof%2BC0j11woLjYuKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp2XwZG9iZN0E4i7cq3AO0Ossbu1HDS0A0sc6FNrGKdPUdCOQsIf9ceeX6TjukxUMXWGgHCe%2F1yLjq9UAGe06LUx9twA0Qf7WfTq6T43bYtUpVHUl8fl1P3EylxwQBmgHnimTGsERKszPFzrZ3nzjFi1Nx%2B%2BaanVrbg2z9ViF1hEkivAb4HVWic%2Fc%2F8CN8itCmo%2BvGEStjYGVogGPbv2OEWGp6IR%2BAnpWIMCQ9iKEZiYV9%2FShi3qeUS3xRksbD9snzj4z1wMg%2FmcrbOiktA9WTay%2B0HL9C9jYhZQyR0AyM60E2U2BNQQtm8FiiW9gk1CsY9giymmSxlPb5Z92S2TKF9dLwqgnD2g3T1RMp9LjqsKZFTd74ZoN7ixf2MUMHv3eFk59I63S23cTusOfGwHsPWkPUWFpLGDRpGIo6sf1BvnGC%2FT3lhKQA%2FZsLPbGg%2Bne%2F0isYCN97auCv0lSto8fYsuEfat7jGEzlfa0TSFkSbEru6aFUq16vXnSC9cZ9o0YrtTnpKYKW5ayRgkSZAnm%2FsxieDb3uDPITwKct6fjSAXK0dKuzXGE9uPFsGmrJtQdmqennGioYzPTxZGiUcsoSCtRg%2By8CbKx%2FuTGVT%2FLy83EyjrAZz0uFsVFE0D24QST%2FyAenliPRGWbjEjCk0LrIBjqkAQil4Fzr%2FIvle82HkFR2t6qhPhc%2FdUtUlK%2FniO1lMtN2rCuGdWlb2LBstTnC14drpFzxE3nFfGfVdvyEhFNCWHt8bTO%2BvyePnE4aTVQkz%2B0SstT64cMRN9IW%2BCEdgKRzWYuiYWMFl%2B%2FOhfECR56xJwC3c56Klgk1S0cuzT6GGP9zRSm2uBwY4J%2FuUXXcEKMnlBpcoFtYFJbtB7hC7%2BT8W0NHM7ma&X-Amz-Signature=89d6dfd33459ffeecb2633fdd953832288e54ac9e4f12463a1dfdebd3a914d66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

