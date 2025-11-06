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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NFPGI3C%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWd7V6BxcXocJKB%2FQ1skJya7EeMkC63LqVcMnLMqvNXwIhAJP4Yhgd8Brq22TNVlBt5qtrFtWythvsaS5SDCTG56u7KogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2FuVXYOAfvApi2V80q3AMB3aIrvsZLoVf2Liq%2Fg%2FtJ%2BO2KPiNoYS8wCvfKcF5RcSkvxzaZ5IZgY%2F9ZNd7vd%2Fx7rmvT4T6VQPcNmDoaWJxaWdkMNHx4krwu0uy1chDWwl9ql4RxhCfB%2BdYkdaeme6xKWlsr5eE9ANtjbNyFvDdV5FdAtOucwMeT7dQQirFvj%2Bp5cOeIcqqEVXbFy%2FOoX9lwqJOQyP49sLGzCBRTnhebNGWBp0ZO%2B90ZeXcTuG0Hv1gxpeNnz1nU4ymMzpfazkM3r4nbSTx67OQYqeditEMQP%2BDm%2FAFHIiHRcJwf5V12imguEZqWndrjkNuI4ab7gdVmeQTFUSKKB5dD6sd2uUAJ%2BaZLSoA1Lj6NmUyaJLwSTk9XSoQmkTYV7GLz%2B66%2BpZP7JGCsY9YqT19CQIJhi6bzlkHjxDcB06ilNFtY5ruGbo5BURPmwmIM1ZTnp7NzCHkoE1BZb3yjpex3QH5c6dCFnraKkD9ikwYAgW%2FfKkrQkYYyZq6LhyO71H66d8BOi7x0Jnq%2FiAwYziOS%2BDyBnzCjKuJVdBDFi5CqhPTx2H8ReWh5%2F5Kd7WjMmUQodq219OQm7ftOZ8THX8AQ25ESCVDyp9giYNogrVOJbyMdU%2BgJ5FRVXyd7R%2FmFu3sAlTDd8a%2FIBjqkAUC9DFIzB04dxpdoj9Z8veKmShdgFK5v0wp3aSQSkcQcCA1JschpmoB8Z7SVvCf55MEN7MWo%2B8MrpIYhE8wKJTvc5sDxuLYwqyicyaZoHGXAVfNMeMWyMD%2F2fzgHCjg3w4t%2F%2FiBdUED%2F4mnnMi%2FYC6liXWDHP7MzOa9O5CgpmzgF%2B%2FYJudHyzZbi3ZjA3QGZfPl80cANay0kE5FxhEfXHePJ2fjR&X-Amz-Signature=ca21062f174fe7ac1bbf395c4d1485339159c40231763d4bc3b5b6ec866e163b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NFPGI3C%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWd7V6BxcXocJKB%2FQ1skJya7EeMkC63LqVcMnLMqvNXwIhAJP4Yhgd8Brq22TNVlBt5qtrFtWythvsaS5SDCTG56u7KogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2FuVXYOAfvApi2V80q3AMB3aIrvsZLoVf2Liq%2Fg%2FtJ%2BO2KPiNoYS8wCvfKcF5RcSkvxzaZ5IZgY%2F9ZNd7vd%2Fx7rmvT4T6VQPcNmDoaWJxaWdkMNHx4krwu0uy1chDWwl9ql4RxhCfB%2BdYkdaeme6xKWlsr5eE9ANtjbNyFvDdV5FdAtOucwMeT7dQQirFvj%2Bp5cOeIcqqEVXbFy%2FOoX9lwqJOQyP49sLGzCBRTnhebNGWBp0ZO%2B90ZeXcTuG0Hv1gxpeNnz1nU4ymMzpfazkM3r4nbSTx67OQYqeditEMQP%2BDm%2FAFHIiHRcJwf5V12imguEZqWndrjkNuI4ab7gdVmeQTFUSKKB5dD6sd2uUAJ%2BaZLSoA1Lj6NmUyaJLwSTk9XSoQmkTYV7GLz%2B66%2BpZP7JGCsY9YqT19CQIJhi6bzlkHjxDcB06ilNFtY5ruGbo5BURPmwmIM1ZTnp7NzCHkoE1BZb3yjpex3QH5c6dCFnraKkD9ikwYAgW%2FfKkrQkYYyZq6LhyO71H66d8BOi7x0Jnq%2FiAwYziOS%2BDyBnzCjKuJVdBDFi5CqhPTx2H8ReWh5%2F5Kd7WjMmUQodq219OQm7ftOZ8THX8AQ25ESCVDyp9giYNogrVOJbyMdU%2BgJ5FRVXyd7R%2FmFu3sAlTDd8a%2FIBjqkAUC9DFIzB04dxpdoj9Z8veKmShdgFK5v0wp3aSQSkcQcCA1JschpmoB8Z7SVvCf55MEN7MWo%2B8MrpIYhE8wKJTvc5sDxuLYwqyicyaZoHGXAVfNMeMWyMD%2F2fzgHCjg3w4t%2F%2FiBdUED%2F4mnnMi%2FYC6liXWDHP7MzOa9O5CgpmzgF%2B%2FYJudHyzZbi3ZjA3QGZfPl80cANay0kE5FxhEfXHePJ2fjR&X-Amz-Signature=68ac888b536192689d4df6343f3df84d11110b8abb0ee46e75c15ee97d2bdf5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

