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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWEYFR2P%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDlRkXl9sDkvPGugVjDfmjThb6rudtqiE503bEQvopb7AiEAmWZtas5nIatWvl5v1yUF6SfU70TzM6BTdZJmTM1nH50q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOjiG7zPcQAg2FfFqircA7sg0lP8XvFQdfJQ2mTpprX9eR0whtQZjuDHqx%2BytVZI2d3XJMabqZGxsnFCDSXaCxqMI6aWxcTvYsUhZfchIVwagcSAnV8pg7Pwp8bgIrwyKIeaEVpe%2FXK7gbXBHBO%2B83WyEJqcL2%2BiukO0oGiM4CpL0Ux89IQObM%2F6IwCUFWsd7kGx5dSZbXdG4Ixggw%2Fh9J93IfuW9ok0hicbjPUOSlR1MLciHJiztHoSor8yabTKVwvV6GQY8u0hBIJWgpf%2Fk%2BkStFKBCSFK9uH3pKBescvVZK3eSSdDaOkxibWfzgOU49OlkSqhW%2BS5sZtqAh%2FFnVCCYxTXqP2LhLrgNlWmD7dKk5pJF3L9yKCdleMINl5qiU%2FcFXedjTex3psHuzz4ElwSblwED64hWdgtqF1%2BY9e3aty%2BK7wEJtolVb6T6qSwS0lig%2BKGEhFlO6QoPJKQFjkCmVbUhG44uz4M6BfymU%2FkpvX%2F4PfVDvo6AzcBy62l0Ws5OUwzD9MD8l%2BJnPTIXuEWR59NQp201cMU%2F9wF0GyIx4tPpXUnD7rOCvIf14WejoJVKint6hC%2Fz3uWk%2F4KkYR%2FfMW%2FtzS7fqeE7ocs8UBqyeDSy%2B5ERhmWcMccfXKJ01RHQ9kSw5U9%2BO7MMKysvc4GOqUBUvHmmNMurxv1mmxhKSRPQzaUX9kwDNTlmafigIIMd2BRepTyO9MtntLaNKtMRuEO%2F%2BpRWT3o8SQl7XOpLMqwYmPS4lK8lFEPejq%2BZ6pPwUEkMo3yh%2Fg6fu9Bgv6fFUkH3H%2BKgBYw5yL9CQWmwfAcYg83%2FHly%2BSkdtgpSv3HUCx4yIy7owrC4ClnZMhzwX%2BTCEDjyWGWADHtt%2FBxiXQRV7iVAy2iI&X-Amz-Signature=614d508c20064860b726a5e38d0df54bca1a9b8b3fcd89cf5a980240acc4e88c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWEYFR2P%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDlRkXl9sDkvPGugVjDfmjThb6rudtqiE503bEQvopb7AiEAmWZtas5nIatWvl5v1yUF6SfU70TzM6BTdZJmTM1nH50q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOjiG7zPcQAg2FfFqircA7sg0lP8XvFQdfJQ2mTpprX9eR0whtQZjuDHqx%2BytVZI2d3XJMabqZGxsnFCDSXaCxqMI6aWxcTvYsUhZfchIVwagcSAnV8pg7Pwp8bgIrwyKIeaEVpe%2FXK7gbXBHBO%2B83WyEJqcL2%2BiukO0oGiM4CpL0Ux89IQObM%2F6IwCUFWsd7kGx5dSZbXdG4Ixggw%2Fh9J93IfuW9ok0hicbjPUOSlR1MLciHJiztHoSor8yabTKVwvV6GQY8u0hBIJWgpf%2Fk%2BkStFKBCSFK9uH3pKBescvVZK3eSSdDaOkxibWfzgOU49OlkSqhW%2BS5sZtqAh%2FFnVCCYxTXqP2LhLrgNlWmD7dKk5pJF3L9yKCdleMINl5qiU%2FcFXedjTex3psHuzz4ElwSblwED64hWdgtqF1%2BY9e3aty%2BK7wEJtolVb6T6qSwS0lig%2BKGEhFlO6QoPJKQFjkCmVbUhG44uz4M6BfymU%2FkpvX%2F4PfVDvo6AzcBy62l0Ws5OUwzD9MD8l%2BJnPTIXuEWR59NQp201cMU%2F9wF0GyIx4tPpXUnD7rOCvIf14WejoJVKint6hC%2Fz3uWk%2F4KkYR%2FfMW%2FtzS7fqeE7ocs8UBqyeDSy%2B5ERhmWcMccfXKJ01RHQ9kSw5U9%2BO7MMKysvc4GOqUBUvHmmNMurxv1mmxhKSRPQzaUX9kwDNTlmafigIIMd2BRepTyO9MtntLaNKtMRuEO%2F%2BpRWT3o8SQl7XOpLMqwYmPS4lK8lFEPejq%2BZ6pPwUEkMo3yh%2Fg6fu9Bgv6fFUkH3H%2BKgBYw5yL9CQWmwfAcYg83%2FHly%2BSkdtgpSv3HUCx4yIy7owrC4ClnZMhzwX%2BTCEDjyWGWADHtt%2FBxiXQRV7iVAy2iI&X-Amz-Signature=adfce08bbdad924f062c64f3c9f973e1addff26e80b98f11d997138e31f863ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

