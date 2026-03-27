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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KDMZFVA%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHiO7MY630wtFyKELWHkVH2K%2B6eLJwh3okEs9xwa7UrgAiEAgE1%2BclTt5OTl%2BI9ORB6Yulgw39ugXr1TA1mrvFf3EUsqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCjIQMW5pDW%2B%2FQnkYCrcA4te1gZoBbYB6dpQetMOQktgtyNa4NEfnBt3zXYCa3Cc24QVqTvQy978I5FX%2BC2tOngMlcngaj7TD%2Bwz%2Bs29TqGCFmltRuaApc8NNzDTSy373f3inAA98UQaLpKqJwcPWsnSjgFnQvsmr4aAbWv42obkG5sEhWDXV3kqK1qbgTqICrZ1iGn5QjrXZ7l7z669%2BYfgiX8NWXV2DUGT%2BCDF%2BxFe21h3PjyMRQ1f%2F5DqPYYVH0jixBWhPwYNuePy%2Bg8LWUaFf%2F%2BQj92WWaMU%2Bpwleknm%2BP1igGGkhgZ2RQW3OVAxcG01%2BVI5ptZJo3H41wm3KhLOJdOa2IknpUp%2FcL7cqy2Rgv40k71i0fB1Vfiz6HlrEQxvt8INeaQXMn%2FyRP%2BsQKkPmKPHOkP%2BgUohNOn0%2FMSXpCdifusEPnJmM1zcIz%2FXjHJrOfTEdBq%2B0Xs3%2BmlZa7oXPKaWXFEivEAqtd3DrcS3aFB7WEn8IRE2iKaDuubtXX43k0Qc8z4SCMUeOj8aQWW4%2Bsh5stGfZ6rrwC8RlY3p%2FuuhsVT9Q8bbEg5fZOcyZtqCZ4wPc%2BwIbPTUgYL7rEkP%2F77IEyK5aNWS82ielJ1hlNdGMrlDiuaMWgSlcMGlYR7XkhlzlbMXAUXAML7qls4GOqUBb1ZKIvXpcFzISsiW1H39FkbXAXL0fLfCEiY%2BJ9uNx4m5cCRQcxDmY19j8PLD79kfOjf7dXkNvpzRrqtn0XU33bH8s9n5Apg61E%2BC5Dau%2FO3l0xGleEi5nCVQ3tk2W3AAnkFUchuqvEai%2B15neZg%2BgdFM3QI1wpnHEw%2BvCgxr%2Ftu3IkPZWfGb3ToV9ffObSbSeKDi%2Bajw%2BQp%2B5E7TM1VodrZmyj7V&X-Amz-Signature=ef9224a6f2ae19dfd5de99ebbd4e2981e76f6fcf82318ecd07bcd1d4c4cec7bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KDMZFVA%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHiO7MY630wtFyKELWHkVH2K%2B6eLJwh3okEs9xwa7UrgAiEAgE1%2BclTt5OTl%2BI9ORB6Yulgw39ugXr1TA1mrvFf3EUsqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCjIQMW5pDW%2B%2FQnkYCrcA4te1gZoBbYB6dpQetMOQktgtyNa4NEfnBt3zXYCa3Cc24QVqTvQy978I5FX%2BC2tOngMlcngaj7TD%2Bwz%2Bs29TqGCFmltRuaApc8NNzDTSy373f3inAA98UQaLpKqJwcPWsnSjgFnQvsmr4aAbWv42obkG5sEhWDXV3kqK1qbgTqICrZ1iGn5QjrXZ7l7z669%2BYfgiX8NWXV2DUGT%2BCDF%2BxFe21h3PjyMRQ1f%2F5DqPYYVH0jixBWhPwYNuePy%2Bg8LWUaFf%2F%2BQj92WWaMU%2Bpwleknm%2BP1igGGkhgZ2RQW3OVAxcG01%2BVI5ptZJo3H41wm3KhLOJdOa2IknpUp%2FcL7cqy2Rgv40k71i0fB1Vfiz6HlrEQxvt8INeaQXMn%2FyRP%2BsQKkPmKPHOkP%2BgUohNOn0%2FMSXpCdifusEPnJmM1zcIz%2FXjHJrOfTEdBq%2B0Xs3%2BmlZa7oXPKaWXFEivEAqtd3DrcS3aFB7WEn8IRE2iKaDuubtXX43k0Qc8z4SCMUeOj8aQWW4%2Bsh5stGfZ6rrwC8RlY3p%2FuuhsVT9Q8bbEg5fZOcyZtqCZ4wPc%2BwIbPTUgYL7rEkP%2F77IEyK5aNWS82ielJ1hlNdGMrlDiuaMWgSlcMGlYR7XkhlzlbMXAUXAML7qls4GOqUBb1ZKIvXpcFzISsiW1H39FkbXAXL0fLfCEiY%2BJ9uNx4m5cCRQcxDmY19j8PLD79kfOjf7dXkNvpzRrqtn0XU33bH8s9n5Apg61E%2BC5Dau%2FO3l0xGleEi5nCVQ3tk2W3AAnkFUchuqvEai%2B15neZg%2BgdFM3QI1wpnHEw%2BvCgxr%2Ftu3IkPZWfGb3ToV9ffObSbSeKDi%2Bajw%2BQp%2B5E7TM1VodrZmyj7V&X-Amz-Signature=33d3adb6979c4b114f32f891bef448f997ee78bfb18991ae0aa7458ef7a9007e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

