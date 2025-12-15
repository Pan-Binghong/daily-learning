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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666Z3OTFY%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCJS%2B%2FVwquodZ8Gec7q%2F819h%2F3ohHLqAjtT5OFvGCnx5gIgLYjDzbfdkrSqprpepnQu9eAjuQIjLIruFk7qXgNiedgq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDIvZlDfd%2FuIwbgE%2BsircA6r8i3Hn2ULzDHvs%2BfaMzB5CsT3fiovI1Sw6f7Gkr%2BNDNsuUYgBMmrvY5M0VlZSiYXkcXNy9f1gd%2BvPMtlmXgNy0MNIkcA%2FOZL3FXOWPDYT29NnuWFlMLdhfhlITWxxHbxBYcLTJQnuq6DETLuw4VSMHnkSxlHoNzqIrhizUmI7TjAcJgAr8Tn4aOJBt68FtlZVfnm%2BYYVXPOAkLBA4Cci8qV%2F5zk8pOXNdcXmlk%2BhTkAmCjFY4fK5NSONUHv4miHaanP0Q6h%2BYM3o%2BXpdEhDQXf9x2ZQQO%2BXsv7omNB%2FB%2Ft95O%2BbTo33RkjJ4h2mBXT%2Bezrf51wMN0PE0haqIiaTPhh6nSz8voqRJ7MNyQlWUaLYXNYX1utPT3IJ8JSruAh4iPw6s%2BY0EA3cIYIpxcqHjW6s2oHv%2FyUlCWeCGjuyIKcS%2BNZBoH0hTDlNKZipXIk0K6p3AQ9XL8%2Bq7icJE%2Foxdrztz23Ys%2F85lup0gkfYoinyuWz0qMWPxGG1sUWPDt9Kzla8jrc32OnvZReXywo9trM5Btl%2B7mNonHORp2h9YmaAHU2QFlEnrVy3FIEcN8oCGRFyTCOqzPrtkprthcXWu8e0FbqtSfvQUlJXV41HY2YqWc6zd6Gk%2BTSTDscMPna%2FMkGOqUB5PC%2B%2FEUTSxn5yFn0TcdXXvRBHWtCrayb2Sxa%2FKh4x6XQnA1OQ9yTeSEO2qbPA0n7ruWZXbxw1iKVh8zfVcgbNygeVVyHs6xzg6kCrHiOnLDbYTo%2F2fYbwGs9tSJFc2cyOVzG7gvd043WAyh0oCqR4rzrDI%2FVHS3QwX4gPqM24CpxqlqklR5IWGKJsIo7NStXo2yspaYEx5vspfnzh0fGbqUMVJ3U&X-Amz-Signature=8717a6642d63dec1965f5a40317841f629c4182f85d1949219a99566dbd8dcd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666Z3OTFY%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCJS%2B%2FVwquodZ8Gec7q%2F819h%2F3ohHLqAjtT5OFvGCnx5gIgLYjDzbfdkrSqprpepnQu9eAjuQIjLIruFk7qXgNiedgq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDIvZlDfd%2FuIwbgE%2BsircA6r8i3Hn2ULzDHvs%2BfaMzB5CsT3fiovI1Sw6f7Gkr%2BNDNsuUYgBMmrvY5M0VlZSiYXkcXNy9f1gd%2BvPMtlmXgNy0MNIkcA%2FOZL3FXOWPDYT29NnuWFlMLdhfhlITWxxHbxBYcLTJQnuq6DETLuw4VSMHnkSxlHoNzqIrhizUmI7TjAcJgAr8Tn4aOJBt68FtlZVfnm%2BYYVXPOAkLBA4Cci8qV%2F5zk8pOXNdcXmlk%2BhTkAmCjFY4fK5NSONUHv4miHaanP0Q6h%2BYM3o%2BXpdEhDQXf9x2ZQQO%2BXsv7omNB%2FB%2Ft95O%2BbTo33RkjJ4h2mBXT%2Bezrf51wMN0PE0haqIiaTPhh6nSz8voqRJ7MNyQlWUaLYXNYX1utPT3IJ8JSruAh4iPw6s%2BY0EA3cIYIpxcqHjW6s2oHv%2FyUlCWeCGjuyIKcS%2BNZBoH0hTDlNKZipXIk0K6p3AQ9XL8%2Bq7icJE%2Foxdrztz23Ys%2F85lup0gkfYoinyuWz0qMWPxGG1sUWPDt9Kzla8jrc32OnvZReXywo9trM5Btl%2B7mNonHORp2h9YmaAHU2QFlEnrVy3FIEcN8oCGRFyTCOqzPrtkprthcXWu8e0FbqtSfvQUlJXV41HY2YqWc6zd6Gk%2BTSTDscMPna%2FMkGOqUB5PC%2B%2FEUTSxn5yFn0TcdXXvRBHWtCrayb2Sxa%2FKh4x6XQnA1OQ9yTeSEO2qbPA0n7ruWZXbxw1iKVh8zfVcgbNygeVVyHs6xzg6kCrHiOnLDbYTo%2F2fYbwGs9tSJFc2cyOVzG7gvd043WAyh0oCqR4rzrDI%2FVHS3QwX4gPqM24CpxqlqklR5IWGKJsIo7NStXo2yspaYEx5vspfnzh0fGbqUMVJ3U&X-Amz-Signature=46620b70b578031537329917849d8d4c4ea8f00c2975f7b4ca1a9c324484b4a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



