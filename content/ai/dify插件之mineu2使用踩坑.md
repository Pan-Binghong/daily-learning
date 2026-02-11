---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA7KRKLB%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGwxt75hPHJmLYw2jr8ENnuu3Jd6Bm2WVyRVzCZycHU6AiEApz%2B1hIo8Qycb6YYesDlEtrKN%2B%2BOfeiFVuyKf1y35Dr8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP0emY8%2BXV4uZqtoKircA6MRj2WWOzFw9b%2Fvy7HYDMYrd2ieWZACH4eml7vi9OAmRnfNc3hK%2B3d62qcnK7324o%2FCDL7ygZdaoMum82GTg3b4h1XGCKBTZbC5ZeOENCz%2Fzivw0%2FqUoQrmbyGXyBgcdqp0dS5cktWrKPCYqhII6vh6cGAfP2ul4UZV%2Beo6jBeYjzHpLA3rAiIhRhkwITxSqeENZ1g7h3i8Iwxih%2Fofam5gVqNml23AJ8jUMlyP11USVQuztz1R4Nv9kN8wMOLsq8nUdS2B8zysx0%2F5RvfFhaVHH9j5zv2bD3%2Btn%2FD48%2FJdFwy5yXD66ofwXV6%2FybmvXWUGI0ARxEU3EzSVHRIuORfZkK%2FL8EwGvQOIkvpRzOVOZEu9D8kL6aPFakOqTxok7KcIcTp2H3Cwr2fwQM4nxynsJ3ljfGD3MeXsLkxQcV5OUanIx0Oh6Wdwm7NfjS1xnQQEBc%2FMWM2HDkeDt7yMGFKl2q7SXSuoX4yQuO%2FopcXlVaWijySTkgc2DStDxY2NnZ826EYxNi84nUT2jXgzW0SL%2FbHVnKEnqixJQc2xSBJxO%2B%2FqKmm5G19xOLhSIz7WqwhlqpBw%2FSLbgcMR0vjyxjGm0c3dmVhpkrtDTAyokSCRtdVsy0xBUJczj%2BAOMMPLr8wGOqUBV%2BIbNsGrQSRN%2F27vpf64rRbut6chJiSjIGFeEus%2Bcmn0QdJSd5QOjgeLlTOt5ls1%2BnkBPsJ3WKj3I1dzjSsviPtFRPPXqssie75eHA2b1fFu5gdDi43U3mXV3k77AvOrWbkulsa62WPjxHUpxtaUP2pTvCEQ8UqW9gjS78lflm7FRrNBYW%2FOZfHNz6V8Gglihy4A7CKRZPzpOx32G%2FtFCu8EO34K&X-Amz-Signature=370165931e243b5eebe8b498cfc7aa5e239910226048cf08258d052c699840cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA7KRKLB%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGwxt75hPHJmLYw2jr8ENnuu3Jd6Bm2WVyRVzCZycHU6AiEApz%2B1hIo8Qycb6YYesDlEtrKN%2B%2BOfeiFVuyKf1y35Dr8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP0emY8%2BXV4uZqtoKircA6MRj2WWOzFw9b%2Fvy7HYDMYrd2ieWZACH4eml7vi9OAmRnfNc3hK%2B3d62qcnK7324o%2FCDL7ygZdaoMum82GTg3b4h1XGCKBTZbC5ZeOENCz%2Fzivw0%2FqUoQrmbyGXyBgcdqp0dS5cktWrKPCYqhII6vh6cGAfP2ul4UZV%2Beo6jBeYjzHpLA3rAiIhRhkwITxSqeENZ1g7h3i8Iwxih%2Fofam5gVqNml23AJ8jUMlyP11USVQuztz1R4Nv9kN8wMOLsq8nUdS2B8zysx0%2F5RvfFhaVHH9j5zv2bD3%2Btn%2FD48%2FJdFwy5yXD66ofwXV6%2FybmvXWUGI0ARxEU3EzSVHRIuORfZkK%2FL8EwGvQOIkvpRzOVOZEu9D8kL6aPFakOqTxok7KcIcTp2H3Cwr2fwQM4nxynsJ3ljfGD3MeXsLkxQcV5OUanIx0Oh6Wdwm7NfjS1xnQQEBc%2FMWM2HDkeDt7yMGFKl2q7SXSuoX4yQuO%2FopcXlVaWijySTkgc2DStDxY2NnZ826EYxNi84nUT2jXgzW0SL%2FbHVnKEnqixJQc2xSBJxO%2B%2FqKmm5G19xOLhSIz7WqwhlqpBw%2FSLbgcMR0vjyxjGm0c3dmVhpkrtDTAyokSCRtdVsy0xBUJczj%2BAOMMPLr8wGOqUBV%2BIbNsGrQSRN%2F27vpf64rRbut6chJiSjIGFeEus%2Bcmn0QdJSd5QOjgeLlTOt5ls1%2BnkBPsJ3WKj3I1dzjSsviPtFRPPXqssie75eHA2b1fFu5gdDi43U3mXV3k77AvOrWbkulsa62WPjxHUpxtaUP2pTvCEQ8UqW9gjS78lflm7FRrNBYW%2FOZfHNz6V8Gglihy4A7CKRZPzpOx32G%2FtFCu8EO34K&X-Amz-Signature=1d78720ad1c59d8515a39a6ffef537e414e323e31e49f2a2b3def5703fe6f0a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



