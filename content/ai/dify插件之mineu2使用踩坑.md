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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJWUSYHD%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQCOQ5d%2BmbFfzdd7ghsDCr%2FQeifdBknXf7MUVOkr%2BmCzRwIhALFrrHKxrznkZT%2BTdQDD4COCrz537Ocv529Y1MDLplP%2FKv8DCDAQABoMNjM3NDIzMTgzODA1Igx8vrMV%2BfqQqixvZ9Uq3AMva6h4bAePQGgECoIT1EycJRYgFygZWHtERszjbgfjbuUFRr6vy40LqU9%2BfVJQ2Mipzb77FU5Ftu%2BoAIAu29a%2Bu5MIJ9gXWCzFBEqkbYB4UZSFNhsAMeRZJM1gqnJkJO267HgskXpfNwc6jaFb6z7N6OgMTkLScAD6JJjzwUws8UFqnGB5ZQcUa4Ko%2BywvMxg0I2fAxXOWuN7s07jtk9zqLaTAwZIy1jfObaM5ySQ5ajP3BzZpMAJuIMxtl3SsgEhwTIVNXiRTxNLS8nNn6b4uUxsvppGaSly65%2FDt0Ji6icqRWM6uTYgBKM3Rqz2aGXdndQPlYZ71m6HuV%2BjmtGT%2BQAFkORQj99WIzWRqlSnMy4%2F%2F%2FMmotOo%2B65Rd8SgAtY0Od3hRRkaqIG0O7Sizav8JRj%2FDaAM2aT%2FxVNLBRDVlHqhVQUg71qyFKIQwu%2FKL6r6jBYv6s9kSAHlqsCoheEpDsOcaRha1%2BIoD1v18WMlkb2bL7vmAb0kwltWBr2zSiugVlbEu4w5GDUOIfYLIHQOnVAi6bcnUjPrMeXkQjiLhtv6N9LmXOTvq5UkLfLLgcaeR8isJ%2BMaZOojq84d7PP7orKQsiShkNyoYvrXJf3mbPZtRFE9CXtXp0OkvrTCZsdrLBjqkASif2hsqny%2FWDaWt1keSf5IvyeVBdVtK6FWHMi6m7qOuxyF3UjviaSP24m6BDAVLB8tS0OgOO%2FinQQCzKGi0qt%2FGgNpK%2B%2BFUkF4yeRJVzSkjENqQKCGjPSX5BMt3s%2FGzgFOwmBc7VwUdQn4ghlalP%2BNkq4AaM7s%2FoDdQzeU7tkPiknGeD1G7mhXqI3QtD6q6i17300jMlVj2y5Ym22%2BL12VFQQpJ&X-Amz-Signature=2902425ac36f13b91fcbad90374ee55ff43b1586424f37f3a6542e6af2990e98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJWUSYHD%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQCOQ5d%2BmbFfzdd7ghsDCr%2FQeifdBknXf7MUVOkr%2BmCzRwIhALFrrHKxrznkZT%2BTdQDD4COCrz537Ocv529Y1MDLplP%2FKv8DCDAQABoMNjM3NDIzMTgzODA1Igx8vrMV%2BfqQqixvZ9Uq3AMva6h4bAePQGgECoIT1EycJRYgFygZWHtERszjbgfjbuUFRr6vy40LqU9%2BfVJQ2Mipzb77FU5Ftu%2BoAIAu29a%2Bu5MIJ9gXWCzFBEqkbYB4UZSFNhsAMeRZJM1gqnJkJO267HgskXpfNwc6jaFb6z7N6OgMTkLScAD6JJjzwUws8UFqnGB5ZQcUa4Ko%2BywvMxg0I2fAxXOWuN7s07jtk9zqLaTAwZIy1jfObaM5ySQ5ajP3BzZpMAJuIMxtl3SsgEhwTIVNXiRTxNLS8nNn6b4uUxsvppGaSly65%2FDt0Ji6icqRWM6uTYgBKM3Rqz2aGXdndQPlYZ71m6HuV%2BjmtGT%2BQAFkORQj99WIzWRqlSnMy4%2F%2F%2FMmotOo%2B65Rd8SgAtY0Od3hRRkaqIG0O7Sizav8JRj%2FDaAM2aT%2FxVNLBRDVlHqhVQUg71qyFKIQwu%2FKL6r6jBYv6s9kSAHlqsCoheEpDsOcaRha1%2BIoD1v18WMlkb2bL7vmAb0kwltWBr2zSiugVlbEu4w5GDUOIfYLIHQOnVAi6bcnUjPrMeXkQjiLhtv6N9LmXOTvq5UkLfLLgcaeR8isJ%2BMaZOojq84d7PP7orKQsiShkNyoYvrXJf3mbPZtRFE9CXtXp0OkvrTCZsdrLBjqkASif2hsqny%2FWDaWt1keSf5IvyeVBdVtK6FWHMi6m7qOuxyF3UjviaSP24m6BDAVLB8tS0OgOO%2FinQQCzKGi0qt%2FGgNpK%2B%2BFUkF4yeRJVzSkjENqQKCGjPSX5BMt3s%2FGzgFOwmBc7VwUdQn4ghlalP%2BNkq4AaM7s%2FoDdQzeU7tkPiknGeD1G7mhXqI3QtD6q6i17300jMlVj2y5Ym22%2BL12VFQQpJ&X-Amz-Signature=4fc5967cbb9cd4682491c2f535497be60666053e7b40ada448acbf027251b9a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



