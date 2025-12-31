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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4BB7WC2%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEfBscW1Ju24j3wZ3imOl8WJX0nMLByB6PkUUN8VLjq3AiEA4%2BeT%2FtDp2hmQ7V9IuR7G3wHzyCKtzT9fe0JJkDhn038qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDKfw8kxjScMe9ErVCrcA%2FxsztP0yg3A64t7GeYircR9Z4wGFNALl6HywAMbxuRm36E1%2BGYqEwOmBgPOquoGEayNXCDORbyjr%2FLPgJBr432Am9LfMVZRRID7hXfowmfqWtCZg5yxBccoZRsKcJRDyZBbZ219B6ev9SNem14YKZPuEBNNs3jA060WtLghlk14rzel0bmyB4J0ZhtQHJ4WbwHd%2BDnB3%2FParnIT2Gf22p7J3B3sGmNIHygvmhpsH%2Bf8As3OiN7464L%2FT7hQ4q22xNaAMrwGoerQHbLc8cYYBdhVBkQe1%2BL%2BEeV6pTMXN2axpSnmMX3UlUFvruZatJpOjh59%2B4PVvSRzWTEVJzqbeQUqEc9I5obos94f7Yh9HSCY0U9ue2CWuZKw9TI8aJ0BqifaGQfqzlZNBbxCl%2FAJ7JhyJxBqPWAkjbS7nyYVrVx9rq3W%2BKMfiwoEq0zOuGTzXIBXt7jAg%2FXNM2oMtGQkdVVgFxCkyBW%2BFS6AYf5DjP7YCBByQPYe3y%2BeJ2HC0KScLiq8hUSuWMcrJP7CXo3SfbMzxEB38SZfUkiYNzgVxR3Vf4UJkUJ78wJm4WVrqz0PMiYKSPqh3GJsqo%2FtQIJzNCKBfkaGT6cXWn85By6yyR004cdEsJaLcvXjB%2FhmMI330coGOqUBpBmiYUa9rod7DKgWytMs3IOekpc1Ip%2F4pXvnXstwO1EFwElc5bZhaGlyJuPCmAdttsaWvIkZVC1wynkllEab4rYcIGkf%2FUhNJXamZmWKHRSwh9eaMVYjXbpaFmEFNW6O1LOaA52vgo7Zxw9NSF84QViss3xj62FnWeMTQNgKOKm3qx3QptpNA63JytZq3KcANbpcQnqHKeqUJe%2FZKxmR0tQnQFBx&X-Amz-Signature=48fb2676eeaeaeabee1345662bb7e55b21e72ece07374a57715146f9ab6bd94b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4BB7WC2%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEfBscW1Ju24j3wZ3imOl8WJX0nMLByB6PkUUN8VLjq3AiEA4%2BeT%2FtDp2hmQ7V9IuR7G3wHzyCKtzT9fe0JJkDhn038qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDKfw8kxjScMe9ErVCrcA%2FxsztP0yg3A64t7GeYircR9Z4wGFNALl6HywAMbxuRm36E1%2BGYqEwOmBgPOquoGEayNXCDORbyjr%2FLPgJBr432Am9LfMVZRRID7hXfowmfqWtCZg5yxBccoZRsKcJRDyZBbZ219B6ev9SNem14YKZPuEBNNs3jA060WtLghlk14rzel0bmyB4J0ZhtQHJ4WbwHd%2BDnB3%2FParnIT2Gf22p7J3B3sGmNIHygvmhpsH%2Bf8As3OiN7464L%2FT7hQ4q22xNaAMrwGoerQHbLc8cYYBdhVBkQe1%2BL%2BEeV6pTMXN2axpSnmMX3UlUFvruZatJpOjh59%2B4PVvSRzWTEVJzqbeQUqEc9I5obos94f7Yh9HSCY0U9ue2CWuZKw9TI8aJ0BqifaGQfqzlZNBbxCl%2FAJ7JhyJxBqPWAkjbS7nyYVrVx9rq3W%2BKMfiwoEq0zOuGTzXIBXt7jAg%2FXNM2oMtGQkdVVgFxCkyBW%2BFS6AYf5DjP7YCBByQPYe3y%2BeJ2HC0KScLiq8hUSuWMcrJP7CXo3SfbMzxEB38SZfUkiYNzgVxR3Vf4UJkUJ78wJm4WVrqz0PMiYKSPqh3GJsqo%2FtQIJzNCKBfkaGT6cXWn85By6yyR004cdEsJaLcvXjB%2FhmMI330coGOqUBpBmiYUa9rod7DKgWytMs3IOekpc1Ip%2F4pXvnXstwO1EFwElc5bZhaGlyJuPCmAdttsaWvIkZVC1wynkllEab4rYcIGkf%2FUhNJXamZmWKHRSwh9eaMVYjXbpaFmEFNW6O1LOaA52vgo7Zxw9NSF84QViss3xj62FnWeMTQNgKOKm3qx3QptpNA63JytZq3KcANbpcQnqHKeqUJe%2FZKxmR0tQnQFBx&X-Amz-Signature=b57e22386293ad1ac0b431ba063261c7a44be5333d0a846789af899f89c80782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



