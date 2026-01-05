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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NBRS5P3%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIFcmf1gvcZCVtOZkE9Qdb7HMw3Ogl3h9MjwgfEYfLMAbAiAHHr55%2FbSxioiGuFMlo0xxoMumT7XjLjfSBF2IMcaA6yr%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIMPa050oTMeJ67lLEfKtwDrOgscHWxbEpTSj4z%2FqPinT1zKHfI7gyV1f4eBvLRG6eOLaLArKzcXvS7zVQAPit9M2wutJ4NhTfOh24naJnGiyLGUl3BFv8snMt8kFuGYAYIlectxIXvzLx2C%2BO%2FZuz4Auji0L7KGA0YErUATKZGFlzAsCmpxAuEHr9aJdblQstzXDdI7tx03bvnhTJenjA2w%2F79q%2FiP%2FCigShjB%2BO6ULD9ArRDDIMZyn0%2FklRxE2%2Bm5gNT1GPN87cFPiZahKvlYf19OboAYAPFVeRgr6ohJNXmjoUVMmT4YCVcF2xG5A0Z%2BZybzqbs2%2BP6ohu4jHs%2BaZfslu%2FXcuxgQUy9%2Ba0bdkfEkYJSRan1bVXSMxo5cFk6dtoSPGl4Zad63IC7S4m9SAQCo%2BbnLWLVKYra4%2FkHscLNQ%2FTlV8r%2BLU78PehJtvO1CDlcMdEA1n7YVJ6zGjUzf2QdAUQYW2UbnnUNShI183SQuFV7HP6ZmycocX63CvMLvZ0RZqS3gK8LEKqyrEgs9nkUVJ67Mqh0HcRwzowerYVQvXmFz4ed0LGc1O8enzi%2BYACUdyLWEAXF9BkllazFodHNww5fbo9TKKxDpmEsbnA3tFSrMs0saZeUe9KJOOoA%2FmeYp7RXBdOK4ntwwmqHsygY6pgHSdn14PnOGB2F1hwk4xgVaq68nsalV4RRloIKbI7dqcUz55FckJ%2FaQVQivQcutyIbV3vNtEK16EzvlJPBrnRuS60xeftEOxk7k8I3wHuw6S4V8puwaz1GxDGAcQspC6Th%2BJt3ZmD2XUbYbtka%2Fq3U%2B5YwUAOMBB7bBYeRjdTti0bsR1OyiM2d9PqTblLWsWmd%2F7gJvJaARIwLYXo2%2F43NGnpvnOA3%2B&X-Amz-Signature=b73c55cc9293c02d666176c7ec0cb0d66cab63c82e32a9a751fbdadfb3616259&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NBRS5P3%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIFcmf1gvcZCVtOZkE9Qdb7HMw3Ogl3h9MjwgfEYfLMAbAiAHHr55%2FbSxioiGuFMlo0xxoMumT7XjLjfSBF2IMcaA6yr%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIMPa050oTMeJ67lLEfKtwDrOgscHWxbEpTSj4z%2FqPinT1zKHfI7gyV1f4eBvLRG6eOLaLArKzcXvS7zVQAPit9M2wutJ4NhTfOh24naJnGiyLGUl3BFv8snMt8kFuGYAYIlectxIXvzLx2C%2BO%2FZuz4Auji0L7KGA0YErUATKZGFlzAsCmpxAuEHr9aJdblQstzXDdI7tx03bvnhTJenjA2w%2F79q%2FiP%2FCigShjB%2BO6ULD9ArRDDIMZyn0%2FklRxE2%2Bm5gNT1GPN87cFPiZahKvlYf19OboAYAPFVeRgr6ohJNXmjoUVMmT4YCVcF2xG5A0Z%2BZybzqbs2%2BP6ohu4jHs%2BaZfslu%2FXcuxgQUy9%2Ba0bdkfEkYJSRan1bVXSMxo5cFk6dtoSPGl4Zad63IC7S4m9SAQCo%2BbnLWLVKYra4%2FkHscLNQ%2FTlV8r%2BLU78PehJtvO1CDlcMdEA1n7YVJ6zGjUzf2QdAUQYW2UbnnUNShI183SQuFV7HP6ZmycocX63CvMLvZ0RZqS3gK8LEKqyrEgs9nkUVJ67Mqh0HcRwzowerYVQvXmFz4ed0LGc1O8enzi%2BYACUdyLWEAXF9BkllazFodHNww5fbo9TKKxDpmEsbnA3tFSrMs0saZeUe9KJOOoA%2FmeYp7RXBdOK4ntwwmqHsygY6pgHSdn14PnOGB2F1hwk4xgVaq68nsalV4RRloIKbI7dqcUz55FckJ%2FaQVQivQcutyIbV3vNtEK16EzvlJPBrnRuS60xeftEOxk7k8I3wHuw6S4V8puwaz1GxDGAcQspC6Th%2BJt3ZmD2XUbYbtka%2Fq3U%2B5YwUAOMBB7bBYeRjdTti0bsR1OyiM2d9PqTblLWsWmd%2F7gJvJaARIwLYXo2%2F43NGnpvnOA3%2B&X-Amz-Signature=e41d38cfd16606659ee63b43ea097e7e15ec2be5dbd3e388ca98e13d57465ec9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

