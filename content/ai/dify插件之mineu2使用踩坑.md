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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4I2KHOX%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDSxCIGlQCJvY700MGySQfNTJSb8kguIuyNbzfMDQ4mtwIhAIyfJvZO8tVHD0lnbKig5cpXChByNKZhTcXAb7%2BFYRppKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxaThiRFBhhIuJY9WEq3AOXfNxLUmIyTYxzveuzco2XYfFkzMxroIOo%2Bl3UHCzE71o3p4tnWnM5z6oukh3oTsSggq2RUN9jMw%2Fmgk8vMC4jMZ362aPiWCVburIuR2r%2FWnXEE%2B0r7OKo6UsgfcYV9v%2BZLdQ051wGDFhOXRtFQrc6ffkYjp%2B3lM0xXdBIopilPjGX4bkfLzEjtpP2sWnqUEUmGRzaI%2F4A54pJ%2B4h6NTiPbjp4%2FxuXlrzL4T6Uo%2FL0rVrfJ%2FoJlQeA5IHK6rc7MSquc2%2Bp2pXZJ5wWg3GcAdHzW5yBtYxTEHhKXFEYpIm9uS43LpLT8uZWZsRXdj3ixyTJ4NGRJuUiKVEGqO3SVkUlLQ0s4T7FRchcT4yRHo7oLpmr3MqxngyK%2FASlaTl1woyKsFZ0tXCbqHOUt51a%2BOfNPggVW9LvFssSdk7bQ9n18hUDZMJb%2FlA%2FjdtUOueMA6sAXFiF9fuWzsSovvJEetc0oN4QPE29a5TjIhL%2B2bBy3o9Qyqf8W5Epo9o2230H6yrsBdWEfnOcBlsXAD6LrNlQhs2etycXQX9KsfqYLbcG66Cpaa7hthPBDmM0kBiNtUeUYG0r2tMN3voOXQcwF1ppy%2B8Wb1pDOpW1LLqG%2FqLx4F01L5ZmMp6kJ2ZN4zC7ttbKBjqkAaKzh%2F6NR16k0MIVOGNBynfm7D4%2B%2BQuF5Uc9ZAUPRBrEoONEGZMgrbd0VxozTq2otIWdqfw1n1dvUuG5zNccgflWvESl%2Bh%2BHS1TT8VlD1JWyiyg%2B4YSDy5VN3Rs63md6wpPLcQBuGvvEci%2Bs1HxRkHaQSsvh0n9IRLR4%2BGYyHJqMCrXN1OhA5o8hAtT5fw1Su0W%2BRXVQQGVvmPW2Ae7CPP2%2FootH&X-Amz-Signature=624faafb5ad5ad628208bce583b42b74b82925ce1d9c99bcecb63b48347da048&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4I2KHOX%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDSxCIGlQCJvY700MGySQfNTJSb8kguIuyNbzfMDQ4mtwIhAIyfJvZO8tVHD0lnbKig5cpXChByNKZhTcXAb7%2BFYRppKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxaThiRFBhhIuJY9WEq3AOXfNxLUmIyTYxzveuzco2XYfFkzMxroIOo%2Bl3UHCzE71o3p4tnWnM5z6oukh3oTsSggq2RUN9jMw%2Fmgk8vMC4jMZ362aPiWCVburIuR2r%2FWnXEE%2B0r7OKo6UsgfcYV9v%2BZLdQ051wGDFhOXRtFQrc6ffkYjp%2B3lM0xXdBIopilPjGX4bkfLzEjtpP2sWnqUEUmGRzaI%2F4A54pJ%2B4h6NTiPbjp4%2FxuXlrzL4T6Uo%2FL0rVrfJ%2FoJlQeA5IHK6rc7MSquc2%2Bp2pXZJ5wWg3GcAdHzW5yBtYxTEHhKXFEYpIm9uS43LpLT8uZWZsRXdj3ixyTJ4NGRJuUiKVEGqO3SVkUlLQ0s4T7FRchcT4yRHo7oLpmr3MqxngyK%2FASlaTl1woyKsFZ0tXCbqHOUt51a%2BOfNPggVW9LvFssSdk7bQ9n18hUDZMJb%2FlA%2FjdtUOueMA6sAXFiF9fuWzsSovvJEetc0oN4QPE29a5TjIhL%2B2bBy3o9Qyqf8W5Epo9o2230H6yrsBdWEfnOcBlsXAD6LrNlQhs2etycXQX9KsfqYLbcG66Cpaa7hthPBDmM0kBiNtUeUYG0r2tMN3voOXQcwF1ppy%2B8Wb1pDOpW1LLqG%2FqLx4F01L5ZmMp6kJ2ZN4zC7ttbKBjqkAaKzh%2F6NR16k0MIVOGNBynfm7D4%2B%2BQuF5Uc9ZAUPRBrEoONEGZMgrbd0VxozTq2otIWdqfw1n1dvUuG5zNccgflWvESl%2Bh%2BHS1TT8VlD1JWyiyg%2B4YSDy5VN3Rs63md6wpPLcQBuGvvEci%2Bs1HxRkHaQSsvh0n9IRLR4%2BGYyHJqMCrXN1OhA5o8hAtT5fw1Su0W%2BRXVQQGVvmPW2Ae7CPP2%2FootH&X-Amz-Signature=40839da400fc4197194db184b74dbafc909a7e15b60161d6651d4ffee2a7c5f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



