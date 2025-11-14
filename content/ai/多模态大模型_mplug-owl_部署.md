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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTALIIU6%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFXYByPIOm7R%2BfJgy6eHlSWO4nQA2JbLN0r0mQ6fUhEQIhAJHpCnCacTs9e1F7RkJS5Im5DvNsvyAhJbuZZLwPnUNYKv8DCFoQABoMNjM3NDIzMTgzODA1Igw%2FQ589JFpbCurMjfwq3AO06ePbPzQW%2BK%2Bv8GJqQ2BNCb4FEvFDtAcFTyE%2B2L7OHnsK0H5hzlv4hexYkYjybHIHjIIQU7x4Ge3vP4LXM1Q3QXyXdeC0qKxaTMkrAm%2Fa6JwKsuK1ONwPX7K9ze344od83v47BlZklcpm1kqSUsyfO9bD4X6htrOJkqGBq24BRmFQy9slRKCyer4OHOmcrEH0%2F8m5hy3lxbC4mMJ9R4umVhNxOQvgPBWohq2Z2QiUEaP1EQJrGX3LyEGE6PAOI4zNYCUXzrXTxvy2NIlB9g2Xlg3SWZNte8VT%2FaW8FH%2FJ4GTiVh16e36cFKSoKd3mBn8mQyL2EzpwfKyk%2FblHpSd%2BG7gmjsMwrRkVL7IuX7lW2s72rUCUIcM8dx5roWWzQJYPIHUkz3Nk8bJY9cUOMTkJSqetUjA2Pu6uvGWfFEXstjyL%2Bs8ATT%2B9zmmUvn4Pver42tsMWE0CAThMQXABPvb67o%2BxV8wHD8UiQN%2FoyskeoXy4dDzOzObQDCq%2BM1fih5u1AxTgy0aJpr73E5m7pxXlzbkoYSkRD0S%2FrSAvdnk1Xjr0RB0%2FBYf%2BzWPGBSX3sjha0a6WFTtaIVpmv%2FRsf6Oe8Hi1zfnQq1OddGtb%2Ft4U%2BBz6Wmjd51Yhy%2Bm%2F%2FzDOidrIBjqkATBO%2BBrAqz947jv8aYh7nbUW9or3J4EPg8%2FALPcP9TcIwTG59wnFji3JbBNkXe4RPalmZ7EJ39mmbizEavjhPHVhRVcpAkKbY0uy06X%2Fg9zh6TY4LFR89uwiTx2JjXi03e9D2yzvQkyEMOaARnqOixqHf5I9uBMWVJxHf9UUuaC6u529nRCzx6DLdrW2Rt8%2BMc9fnm4Zw1uyoJK9PuSl1g8OgFnX&X-Amz-Signature=31e9581b77609e1b9d16e82b129c5f0a35fb5630e85dd8f599a0cbdd3eeb611c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTALIIU6%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFXYByPIOm7R%2BfJgy6eHlSWO4nQA2JbLN0r0mQ6fUhEQIhAJHpCnCacTs9e1F7RkJS5Im5DvNsvyAhJbuZZLwPnUNYKv8DCFoQABoMNjM3NDIzMTgzODA1Igw%2FQ589JFpbCurMjfwq3AO06ePbPzQW%2BK%2Bv8GJqQ2BNCb4FEvFDtAcFTyE%2B2L7OHnsK0H5hzlv4hexYkYjybHIHjIIQU7x4Ge3vP4LXM1Q3QXyXdeC0qKxaTMkrAm%2Fa6JwKsuK1ONwPX7K9ze344od83v47BlZklcpm1kqSUsyfO9bD4X6htrOJkqGBq24BRmFQy9slRKCyer4OHOmcrEH0%2F8m5hy3lxbC4mMJ9R4umVhNxOQvgPBWohq2Z2QiUEaP1EQJrGX3LyEGE6PAOI4zNYCUXzrXTxvy2NIlB9g2Xlg3SWZNte8VT%2FaW8FH%2FJ4GTiVh16e36cFKSoKd3mBn8mQyL2EzpwfKyk%2FblHpSd%2BG7gmjsMwrRkVL7IuX7lW2s72rUCUIcM8dx5roWWzQJYPIHUkz3Nk8bJY9cUOMTkJSqetUjA2Pu6uvGWfFEXstjyL%2Bs8ATT%2B9zmmUvn4Pver42tsMWE0CAThMQXABPvb67o%2BxV8wHD8UiQN%2FoyskeoXy4dDzOzObQDCq%2BM1fih5u1AxTgy0aJpr73E5m7pxXlzbkoYSkRD0S%2FrSAvdnk1Xjr0RB0%2FBYf%2BzWPGBSX3sjha0a6WFTtaIVpmv%2FRsf6Oe8Hi1zfnQq1OddGtb%2Ft4U%2BBz6Wmjd51Yhy%2Bm%2F%2FzDOidrIBjqkATBO%2BBrAqz947jv8aYh7nbUW9or3J4EPg8%2FALPcP9TcIwTG59wnFji3JbBNkXe4RPalmZ7EJ39mmbizEavjhPHVhRVcpAkKbY0uy06X%2Fg9zh6TY4LFR89uwiTx2JjXi03e9D2yzvQkyEMOaARnqOixqHf5I9uBMWVJxHf9UUuaC6u529nRCzx6DLdrW2Rt8%2BMc9fnm4Zw1uyoJK9PuSl1g8OgFnX&X-Amz-Signature=4b3b1d4a0556a59a6f233afa286a687e317f7cae4294d79ccd9dcaa54a66e627&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

