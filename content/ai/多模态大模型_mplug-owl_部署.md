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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TPHI6VC%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDALiaLn4jFn0zdsw1uCmuV8BkKUuoXci4zym9WuQtDgwIgL60v%2F2d%2B%2BlX7UUdSZWbAfc0DmLvyB%2F5Oa%2F311RA5i4sqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA32jtiYbfYbTm1fZyrcAx9YXTQZntdg9k%2BkoJH9%2Fgogk%2BtSpctUO0LhuWLhE22XVQTzHmryYi6tvd7ttlQQHfbqrmtR9ofM8USIf6z7uIAQ%2FOFNzrgXLZHVdMMbJ%2BgjhBogLgwoeCW8r2kKaumvSd49Z6ZQ6oT0Xl6w6zUq3kS6ZhHjC6WBSH93gtOJsuj8wV%2FY%2BvN99I6Lhys1p6g5iNfGK%2FNfgHEKsmkvKcuzCzz3cd6pqmsIt8wKGxUremaQihGoBkKJJwwJLDzj91giWx1DAlAk004XDOTWeKVjL9Q0YZTJLSLElLnWWbKUP0Pl%2BOC1jwm5T41gadloI%2FLNb1K%2B7LVefM%2F%2FDxqrI8lCghmu97NKQNetogdEq%2F9TxedY2VPmy85ssirvwijgrVMxr7ewz7Ys%2FNphBevC5ceOgpGaTtSPv4Aygm1vTTCZOZ1PLjsLqYN%2B%2FIacRFvtp0U9Ee2CCBJSVZf7d7Z%2FNsh16HkQEu3yevRRobp2orsBznLhIQr9sk%2BaWmnV8glnnzhfvWWc3qD8n3wV2W1GZnR7m3KlaYC9IETBbhkGkvhwcD5PR54GGcVYixRtK6cc4S61%2Fkp8WFa55czCrRhcJ0thggAyP7ldjcrLhXxJtln7VV3qwU639pNpdgxdmEb%2BMI3f9s4GOqUBHJsIm9%2FD4OnsTX6M8J5iC0EcC2UISd00cqFWkd02qQ6xpCMylFzwlYvPEcupc3%2BfgMm%2BbnXU3FyZlrUsCVbTDTDiNOi6QZddRY55OKw6wzxhllRd6zb6blnNMFdZehkUn%2B3fToZA0rYn4745vZsgF0N241EbckJyV343GDcK2zNknTrvOcYVp3J5X8oEJ5C%2Fd5t%2BzL%2FU%2FjupbFUTHEDI7L46UCPy&X-Amz-Signature=a09973fd15ac5a6fdff80789856cf638c358795d5d5f4eecdc7a930bd984d3b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TPHI6VC%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDALiaLn4jFn0zdsw1uCmuV8BkKUuoXci4zym9WuQtDgwIgL60v%2F2d%2B%2BlX7UUdSZWbAfc0DmLvyB%2F5Oa%2F311RA5i4sqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA32jtiYbfYbTm1fZyrcAx9YXTQZntdg9k%2BkoJH9%2Fgogk%2BtSpctUO0LhuWLhE22XVQTzHmryYi6tvd7ttlQQHfbqrmtR9ofM8USIf6z7uIAQ%2FOFNzrgXLZHVdMMbJ%2BgjhBogLgwoeCW8r2kKaumvSd49Z6ZQ6oT0Xl6w6zUq3kS6ZhHjC6WBSH93gtOJsuj8wV%2FY%2BvN99I6Lhys1p6g5iNfGK%2FNfgHEKsmkvKcuzCzz3cd6pqmsIt8wKGxUremaQihGoBkKJJwwJLDzj91giWx1DAlAk004XDOTWeKVjL9Q0YZTJLSLElLnWWbKUP0Pl%2BOC1jwm5T41gadloI%2FLNb1K%2B7LVefM%2F%2FDxqrI8lCghmu97NKQNetogdEq%2F9TxedY2VPmy85ssirvwijgrVMxr7ewz7Ys%2FNphBevC5ceOgpGaTtSPv4Aygm1vTTCZOZ1PLjsLqYN%2B%2FIacRFvtp0U9Ee2CCBJSVZf7d7Z%2FNsh16HkQEu3yevRRobp2orsBznLhIQr9sk%2BaWmnV8glnnzhfvWWc3qD8n3wV2W1GZnR7m3KlaYC9IETBbhkGkvhwcD5PR54GGcVYixRtK6cc4S61%2Fkp8WFa55czCrRhcJ0thggAyP7ldjcrLhXxJtln7VV3qwU639pNpdgxdmEb%2BMI3f9s4GOqUBHJsIm9%2FD4OnsTX6M8J5iC0EcC2UISd00cqFWkd02qQ6xpCMylFzwlYvPEcupc3%2BfgMm%2BbnXU3FyZlrUsCVbTDTDiNOi6QZddRY55OKw6wzxhllRd6zb6blnNMFdZehkUn%2B3fToZA0rYn4745vZsgF0N241EbckJyV343GDcK2zNknTrvOcYVp3J5X8oEJ5C%2Fd5t%2BzL%2FU%2FjupbFUTHEDI7L46UCPy&X-Amz-Signature=cea6f0ac765be749b03c4dd95f286617fce10da0bed465485d21f15c247438fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

