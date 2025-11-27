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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSX2EF4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs4jIue7plG50VyixNTKaMTYZXigegYCFd8DC2dQqX%2FgIhANHOhbIZWotS1%2BA7H4jGVobdeA9aoDV26XkFYVD0WsAdKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B6Jta6raowhM9nL8q3APYXNnY0LzPtSC%2FYCoCuMccEMjfkes19OMZ0SOeVdwqISKrwmXhLux2a%2BZm3V99e4dRKeqTXr1LNSigBATWhxzzkswHcyIMcifsFl%2BVQy0aoGi%2FO3yaWiFxWH5SAgzDtNvST5EM%2BgQTuYG0JdLySl0rbM2TZGuykLcsy8T40mfAVb3DyXF3AYrQB5wefi7yjFr%2BomxmGbIEGP1WQYL%2Bcwlw3Tkws0e7Jhmh2vfuRprgJiHouVpZBXaY8UoKZlNaEH%2BWyvgjFaERP6zUZEfQ%2F32g59MbriTCSFGQBeqmtO1cvqzhWWvH88dinpQkq6eTuj8yTVhHNsW4rNcmzjLnUIMLFQtCw3rc82LjgoFx%2FDQwu7wb4mhIRB9F4dc0jIWc7y0sdX%2BWTTjTfSaQwdXW2D1WQNhHR5E%2BE5CyjV7UzgBuJcmCifShdQO9JbOAVS7%2Bz%2BDDAb%2F5ZwYZPojpVgK1phio3JyuONCLohM90txlx1lRZvcffU8TCShPY7MFe%2BEOgxBgwa1NcJEA2r1tbYQ61gUz6ruoLk8XEh43w0n4w9xPjiIbEXNRF%2FGZ8Yqmk1ozEGwnFFADtW8bfSV37pZIGgAEdOWfDb8t7By26bbEOC%2BGUjDaZERgGuHozop0LjDGzJ7JBjqkAeFmHF86khXkwiRlFssfGroe6G7jtAc4ySCOtlBqxvRsP%2B4ovC99Ps4OKbVR8Wm3zC%2BbaUw5sTBzV243m1qZ1EQeCFwXl9JaRw5L3lKY%2BkySYOR4rF%2BfkxTCZYa%2FKdifgkD5Ba4z1LArhsyr%2FttfNZJR8OyjMJIQR9GTjOFEja4aedqaF6H39FkrDghaVjA4udmcQoIJz%2FNiosdTNvSIgaMgKrRB&X-Amz-Signature=8ec50a706606108de8a155f57a1c22d6a81a810fd4f15e44f33875cbcf680f4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSX2EF4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs4jIue7plG50VyixNTKaMTYZXigegYCFd8DC2dQqX%2FgIhANHOhbIZWotS1%2BA7H4jGVobdeA9aoDV26XkFYVD0WsAdKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B6Jta6raowhM9nL8q3APYXNnY0LzPtSC%2FYCoCuMccEMjfkes19OMZ0SOeVdwqISKrwmXhLux2a%2BZm3V99e4dRKeqTXr1LNSigBATWhxzzkswHcyIMcifsFl%2BVQy0aoGi%2FO3yaWiFxWH5SAgzDtNvST5EM%2BgQTuYG0JdLySl0rbM2TZGuykLcsy8T40mfAVb3DyXF3AYrQB5wefi7yjFr%2BomxmGbIEGP1WQYL%2Bcwlw3Tkws0e7Jhmh2vfuRprgJiHouVpZBXaY8UoKZlNaEH%2BWyvgjFaERP6zUZEfQ%2F32g59MbriTCSFGQBeqmtO1cvqzhWWvH88dinpQkq6eTuj8yTVhHNsW4rNcmzjLnUIMLFQtCw3rc82LjgoFx%2FDQwu7wb4mhIRB9F4dc0jIWc7y0sdX%2BWTTjTfSaQwdXW2D1WQNhHR5E%2BE5CyjV7UzgBuJcmCifShdQO9JbOAVS7%2Bz%2BDDAb%2F5ZwYZPojpVgK1phio3JyuONCLohM90txlx1lRZvcffU8TCShPY7MFe%2BEOgxBgwa1NcJEA2r1tbYQ61gUz6ruoLk8XEh43w0n4w9xPjiIbEXNRF%2FGZ8Yqmk1ozEGwnFFADtW8bfSV37pZIGgAEdOWfDb8t7By26bbEOC%2BGUjDaZERgGuHozop0LjDGzJ7JBjqkAeFmHF86khXkwiRlFssfGroe6G7jtAc4ySCOtlBqxvRsP%2B4ovC99Ps4OKbVR8Wm3zC%2BbaUw5sTBzV243m1qZ1EQeCFwXl9JaRw5L3lKY%2BkySYOR4rF%2BfkxTCZYa%2FKdifgkD5Ba4z1LArhsyr%2FttfNZJR8OyjMJIQR9GTjOFEja4aedqaF6H39FkrDghaVjA4udmcQoIJz%2FNiosdTNvSIgaMgKrRB&X-Amz-Signature=474cb4f5ada4998d87ab4ef06928d87aa297d9ebbe1aa3ed409a17b8eb41c0ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

