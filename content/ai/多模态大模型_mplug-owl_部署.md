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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y22OIIBE%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmNX0C8gVxHqU6Yp6MYnMWkXg6nKsKfX58oLz067OCJAIhAKaPCoNOHdspO2Os3ZlxxwBrNJSixqs5%2F%2BpkJvV096t8KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrNSs6NTJdxhgulTsq3AMcU8D3oD8ND2fMnlehY37EYDNCrQ%2FbR1PUriBz2hbIkcJzQYhnSxvWGfYvVzl%2FAJZXQfwpbc5T3cz%2BLTq0rkHshxDo7vqktKab5sN6uap99K78MKS%2BNrHrIdNE3TRi9pC2fInT1Ig5aY3AEcSyAbxIZ0EY5%2FXbPlt20vkKYZ8YHai6IWNbXB0yM7FJH7U2xtyK2DekYnNDmLMgv9IELXIZKT4qJtr78qlu8ff9D%2FYUlbB3U9pc3grfPGeIIDJxC58J4DT8ntYZjXAWehdHdM2yhvOMg2mAeJ617emxsKylk12bHRN1IywyEoOSF93OItlnSHQXetsuvGzwK3Krqyc66OhZxota5frY56d%2FHWz2kWI7IX8vS%2FujEUkY77tGzAHc8%2FZNBXBbSc%2Fs2YzULZwE%2FwS2N8ZR9Xrxn1Hb6hNy8bu81OylQQMpMcWvIWXSmUYvmgP1v7nmk16DFNWdKnZHxKY6S2rYOIdn%2FL%2Fe28l%2BuDtk%2BY0gbOh%2BvbI5MH5GyYi%2BiBsQVJE5tjX%2Blb8vVyeKPY%2BGEUQM4C7wtxwriHHbOL4crsRs5wkt%2F%2F%2BIL3%2FRPo4TDmzL9q%2BTj%2FOuDYby%2Ft8mgEBqHberfyw73Yx5FZmLp%2Fxe84t25UvU2sLETzCOjd7JBjqkATaKn82HAZtq2DdO0pAf5BgxCqAqEpRuZogvPkWnrRy50z7wrzjtbMeqMuG%2B5KjJ9xgVt3ghBEMYr2bo7UdMHmUgibJCvnWfqCvHFkRcISfcs%2FfzApYJtLnpfXeHQpTEmJQtgPr0joCMh%2B%2FgG5c%2BfWhl%2B6GaY4iUXJO0D6LGfwfvwOD3ttZP%2B4yY%2Bv%2FIX%2BU9kVR01R7qIRzASo1jwdWmk95dV69e&X-Amz-Signature=9a5006dc557947290b5050f52515d7111e03cc895ef376221859fbe4c9070fcb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y22OIIBE%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmNX0C8gVxHqU6Yp6MYnMWkXg6nKsKfX58oLz067OCJAIhAKaPCoNOHdspO2Os3ZlxxwBrNJSixqs5%2F%2BpkJvV096t8KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrNSs6NTJdxhgulTsq3AMcU8D3oD8ND2fMnlehY37EYDNCrQ%2FbR1PUriBz2hbIkcJzQYhnSxvWGfYvVzl%2FAJZXQfwpbc5T3cz%2BLTq0rkHshxDo7vqktKab5sN6uap99K78MKS%2BNrHrIdNE3TRi9pC2fInT1Ig5aY3AEcSyAbxIZ0EY5%2FXbPlt20vkKYZ8YHai6IWNbXB0yM7FJH7U2xtyK2DekYnNDmLMgv9IELXIZKT4qJtr78qlu8ff9D%2FYUlbB3U9pc3grfPGeIIDJxC58J4DT8ntYZjXAWehdHdM2yhvOMg2mAeJ617emxsKylk12bHRN1IywyEoOSF93OItlnSHQXetsuvGzwK3Krqyc66OhZxota5frY56d%2FHWz2kWI7IX8vS%2FujEUkY77tGzAHc8%2FZNBXBbSc%2Fs2YzULZwE%2FwS2N8ZR9Xrxn1Hb6hNy8bu81OylQQMpMcWvIWXSmUYvmgP1v7nmk16DFNWdKnZHxKY6S2rYOIdn%2FL%2Fe28l%2BuDtk%2BY0gbOh%2BvbI5MH5GyYi%2BiBsQVJE5tjX%2Blb8vVyeKPY%2BGEUQM4C7wtxwriHHbOL4crsRs5wkt%2F%2F%2BIL3%2FRPo4TDmzL9q%2BTj%2FOuDYby%2Ft8mgEBqHberfyw73Yx5FZmLp%2Fxe84t25UvU2sLETzCOjd7JBjqkATaKn82HAZtq2DdO0pAf5BgxCqAqEpRuZogvPkWnrRy50z7wrzjtbMeqMuG%2B5KjJ9xgVt3ghBEMYr2bo7UdMHmUgibJCvnWfqCvHFkRcISfcs%2FfzApYJtLnpfXeHQpTEmJQtgPr0joCMh%2B%2FgG5c%2BfWhl%2B6GaY4iUXJO0D6LGfwfvwOD3ttZP%2B4yY%2Bv%2FIX%2BU9kVR01R7qIRzASo1jwdWmk95dV69e&X-Amz-Signature=93a70836a400b5fd02a597cff618db054a758488f959509b3b5f7ac8eabfecca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

