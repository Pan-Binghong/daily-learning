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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653N4SNVY%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDBX1Pw4Zaw3VwWmlB69avYPsu3oQp49U3c36nx41zUWwIgUTLwdM1xdNfcQBK2DG0bON7%2B3p4zAyTvH6WqC7FvpWMqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHQSVUM8qIfgekDblircAxECuDf2tQKgekp35WAO2lJX4zy2mcmUUnHHLKq5f5U3rPPj5a0yT9SC1dW9VZjgYYby6wiSySq00zGgMLbLpJ5T2nsZXUL5ShmMjLHcsNlp%2Bfry92o%2Fi%2FxRCDYwsDsyHfkzz8totkgigHLasuj8P6prVIkBN%2B%2BjstneZ9bfmHEKAPduQx%2FZYgGQa6AWluGSnq8d0DHiLsn%2Bci8fzGIUwyZDk7xC638RYVffkC5t8Nm80wc32ZlV18HDbGlFGsEtf7qzLq3OP7u837qvyUPkgzs%2BpexbYjVBsPdj33uJT8JwaLz%2FBCj9AlwFe6LF5phOEaCe1EWmvv8zIeevbTU15oeO1OrQpdLNy8iemgBvrkyACuXSvQaVCD681ECnmM1%2FhzUJdLczjVNtXclBuuWENBOfzb9WqoHPgbeXtvEWA98mmnXR6owR0XgLn%2FKPKKQk1SoFv4pGHFiXzGA5pULXu%2BqAaJIWqzkt%2FGeOekK2hgPr2YlbWXG0XL01CchevLY67dU6mGtJtkjqaV7FMlX8m6BLhj%2BWGn3NDmTDBcjRhB6R06QCTi42Vl%2BTtZGo8tP1Bo6RZsIrR%2F8KDx0Qj8Ho6NIuDW02ob5%2Bfsx26F1cqvitU%2Bv8pBmY7fFXeo%2BAMJmIgMwGOqUBm5x%2BH2Mrb%2FECXVmX%2ByHmNEzCjPLvK2rUjW8mNG1zUPGoECDJGRe8hQjGesGFDeaXyKAhARZivp9%2Fl3fL7ZfPHUD%2BK5DN1LvQYtoEvv6xilJSrraHXW56KInDSlyujK567ZH6mMRbII6ch2H4acmICjfbSK8JGJvnuq5b8Mkwa6xnLWRRN3ysgsggAUVETpD4bdpCrgKXk48WESTiZfghJLQhZCsr&X-Amz-Signature=d3931b6e49b08a9ebcacb9c9e78d0ee9d00d0a11f5571202e0632dc27244fd56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653N4SNVY%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDBX1Pw4Zaw3VwWmlB69avYPsu3oQp49U3c36nx41zUWwIgUTLwdM1xdNfcQBK2DG0bON7%2B3p4zAyTvH6WqC7FvpWMqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHQSVUM8qIfgekDblircAxECuDf2tQKgekp35WAO2lJX4zy2mcmUUnHHLKq5f5U3rPPj5a0yT9SC1dW9VZjgYYby6wiSySq00zGgMLbLpJ5T2nsZXUL5ShmMjLHcsNlp%2Bfry92o%2Fi%2FxRCDYwsDsyHfkzz8totkgigHLasuj8P6prVIkBN%2B%2BjstneZ9bfmHEKAPduQx%2FZYgGQa6AWluGSnq8d0DHiLsn%2Bci8fzGIUwyZDk7xC638RYVffkC5t8Nm80wc32ZlV18HDbGlFGsEtf7qzLq3OP7u837qvyUPkgzs%2BpexbYjVBsPdj33uJT8JwaLz%2FBCj9AlwFe6LF5phOEaCe1EWmvv8zIeevbTU15oeO1OrQpdLNy8iemgBvrkyACuXSvQaVCD681ECnmM1%2FhzUJdLczjVNtXclBuuWENBOfzb9WqoHPgbeXtvEWA98mmnXR6owR0XgLn%2FKPKKQk1SoFv4pGHFiXzGA5pULXu%2BqAaJIWqzkt%2FGeOekK2hgPr2YlbWXG0XL01CchevLY67dU6mGtJtkjqaV7FMlX8m6BLhj%2BWGn3NDmTDBcjRhB6R06QCTi42Vl%2BTtZGo8tP1Bo6RZsIrR%2F8KDx0Qj8Ho6NIuDW02ob5%2Bfsx26F1cqvitU%2Bv8pBmY7fFXeo%2BAMJmIgMwGOqUBm5x%2BH2Mrb%2FECXVmX%2ByHmNEzCjPLvK2rUjW8mNG1zUPGoECDJGRe8hQjGesGFDeaXyKAhARZivp9%2Fl3fL7ZfPHUD%2BK5DN1LvQYtoEvv6xilJSrraHXW56KInDSlyujK567ZH6mMRbII6ch2H4acmICjfbSK8JGJvnuq5b8Mkwa6xnLWRRN3ysgsggAUVETpD4bdpCrgKXk48WESTiZfghJLQhZCsr&X-Amz-Signature=c5c66f5a8d31c7e31a494028dbea841012913ebafb7d7e9a72f0044b32282ce4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



