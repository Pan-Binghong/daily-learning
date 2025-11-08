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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDK5CLL4%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDpesqmbfkJNzusSjUqhr6pYInSLuK9gmrJIuPOz82d5AiEAlqBC0RKvdjpN%2Bwo%2FJZULVFzbBDh%2Bg8bPHOr4OpjVEc4qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNR03jEdvEWH3HDYwCrcA6LX55zykhJMhe7bLN8Ts%2BN2nWIT0gEaUK1ykK6Lx5%2FFx17QNDspQ4jIf08OE4ciSaDkZ%2BOmnacikGGY7jy9elXC9IybBJddhzFCS8FMaWXPsPDb7rBsWie%2FWJHg4XJpufiIFxXa6C3WEgFVG6FrcIePG9Bx5YOLl%2BcvLJwm6rYyZNN3FTfHjiOztj6VyqIrpAHov7uwv1en6u1cMt7Mk4YYhHy3g2WkbpfKeP7ghJ0rCDOMRsHFILCuKswgTayXh4LLojHSgGbwtbilLjluPklvcjGqKL%2FMllhxTj43Zf3gwv5cBAC%2FlzBdcuc6z8wRxyQetJcPxH2ig9PUcENSRYLbqtbzX2NQNOfarNzydYCxEYb7py18Lq1LpxdC3pQSwPW2O8wD2mIlxo06gjAGyI6vfIx5mTN0arJEYEnVeBb84zFll9AvMyyT3nIDf9dEjHQcKTpm2cSNfFyTF%2BKCQlJFHrRh3HzW5lmdl8O9jzPOJWfAZEItM96JYAfK91qOyD30Nj4OsPyCc0qy1xHZFwjXdIBAVkgExxG4A3%2BhVn47JbY9nzuRj3IejyFccK%2B%2Fuvu89KRuIFgUhZGAD6WSIkYSSl4A7oXoPJt2LphBbyQkXwHEvwelKRK7hOKVMLbQusgGOqUB6XNr5K%2F7OpyH5QqL4lacVkRlnfdbWbl5GiLrFHUdh0hAqnqaJujgJeJSLvf4rKvjfvCyNPOLzms7i7WnKpc8Ah4s%2BCeXyIx%2B9UkKTRW0rw0uV5xQxABv4T9dtoVLUgQu2gWn3ZEUUPeydRwHZnr5L2wJ4etrcf%2FigZFi5GIpYGyK2C2rZBi%2B%2FKsmIU3qCNkokC0ILGdBNxbrN5UFKCpzU4L%2Bnurj&X-Amz-Signature=5452203ec4005789fe23daf548bb931c64c10f012798b208be2fc74df156b999&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDK5CLL4%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDpesqmbfkJNzusSjUqhr6pYInSLuK9gmrJIuPOz82d5AiEAlqBC0RKvdjpN%2Bwo%2FJZULVFzbBDh%2Bg8bPHOr4OpjVEc4qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNR03jEdvEWH3HDYwCrcA6LX55zykhJMhe7bLN8Ts%2BN2nWIT0gEaUK1ykK6Lx5%2FFx17QNDspQ4jIf08OE4ciSaDkZ%2BOmnacikGGY7jy9elXC9IybBJddhzFCS8FMaWXPsPDb7rBsWie%2FWJHg4XJpufiIFxXa6C3WEgFVG6FrcIePG9Bx5YOLl%2BcvLJwm6rYyZNN3FTfHjiOztj6VyqIrpAHov7uwv1en6u1cMt7Mk4YYhHy3g2WkbpfKeP7ghJ0rCDOMRsHFILCuKswgTayXh4LLojHSgGbwtbilLjluPklvcjGqKL%2FMllhxTj43Zf3gwv5cBAC%2FlzBdcuc6z8wRxyQetJcPxH2ig9PUcENSRYLbqtbzX2NQNOfarNzydYCxEYb7py18Lq1LpxdC3pQSwPW2O8wD2mIlxo06gjAGyI6vfIx5mTN0arJEYEnVeBb84zFll9AvMyyT3nIDf9dEjHQcKTpm2cSNfFyTF%2BKCQlJFHrRh3HzW5lmdl8O9jzPOJWfAZEItM96JYAfK91qOyD30Nj4OsPyCc0qy1xHZFwjXdIBAVkgExxG4A3%2BhVn47JbY9nzuRj3IejyFccK%2B%2Fuvu89KRuIFgUhZGAD6WSIkYSSl4A7oXoPJt2LphBbyQkXwHEvwelKRK7hOKVMLbQusgGOqUB6XNr5K%2F7OpyH5QqL4lacVkRlnfdbWbl5GiLrFHUdh0hAqnqaJujgJeJSLvf4rKvjfvCyNPOLzms7i7WnKpc8Ah4s%2BCeXyIx%2B9UkKTRW0rw0uV5xQxABv4T9dtoVLUgQu2gWn3ZEUUPeydRwHZnr5L2wJ4etrcf%2FigZFi5GIpYGyK2C2rZBi%2B%2FKsmIU3qCNkokC0ILGdBNxbrN5UFKCpzU4L%2Bnurj&X-Amz-Signature=08e5ca71302e063af8df1f1638d571912a4ef9db992f6be29b5b0dd517a157ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



