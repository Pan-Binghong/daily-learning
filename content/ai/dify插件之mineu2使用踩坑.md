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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEG5FVAN%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOzmT1YddEzXvZWzwWxHeT777nrJp7R2wXJx2NgTcsgAIgfH%2FTpgth0wGqLMTGJ3jqf4H%2B2ZVm0pG51sVVeWQhtToqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCloilv0YygSXiI1oircA5b0ACgDRp7GOTC%2FYLodMg7n%2FM0ZrXJgBpWebisRDjFHHVaAa8ZYxzZ%2FZbP9CaBts7vfMztGneYMy6WSF7Gz59Ubh5QJE797lWQO42%2BkiOq%2FsnqJXqLxm0BGYcb%2B5AMabIlHtsG4teA2Wqk%2FHPNhWXLPbJyIKARaqNCYm1RgWUr8UHsjYLhSEVK9xvmoVwQ4qVHbMoe38jUMIh5VW9e%2BEFLf5R1ek2iX4BHVzqlaVJ2IFPDaqQnLd79HITXWWpa0ml%2BfG22sOgdPWB5h4Wm5n3uO50FhSSMjmjTKMFtuDiiaxG4mXNnWansugPTCHrt1YpBa1MPJeJ3i3EKNhSM%2FChjP3XHOwjKwMvUaO6xQly5CjlvFEZ%2BuMgm0BciY2I%2FD7BevcSbpXHGAvHyWPSZAifBpSzm3F9IyutA9jLsvJnnIp0jtvBpxZcU2VztJVMoRg7VZ%2Bg3%2B0M4EmN9z5neFw7PgIyO2H1fMTxQi7jWEyLcXr4RlqNjQC%2FaF0Y1RL1bICZGWePn5Wa189jA6AuT0Pjuy7usRv2frDYXhBQKryAa8SfdCtZ1yP5E0kOzgK9oUTmDfRYKtxCds%2FRaOr5NskbrZp6OOW4Ub9RILk59N6%2F6FuOnfDiKT3%2Ffcci2GMNfDgcsGOqUBrsOe%2FQVKFnNuoGGusYREw18%2Bmz5C1Aa6AGUD2HRnAtl0%2BHpzccvHGv8L3ohOcwAESkvz9GxWw5Mcxv%2FrY8UWvKoo9yLHdrkAgxJqIggl9I5YRHgvKhzdEZQQbgEM4%2F1O233twbwFhgr5C16uB%2BlPgFnEE9ifd5Zj%2FLXuHoAwqTiB1YycX0ZWzbYvagY9jWd6XBpiCw8fE3B3buiBOn0W2zOMaLcX&X-Amz-Signature=d40c0a25583ae6ad75285cebd3ddfcb2a9e6ce0707ff245392856ded0b1f5026&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEG5FVAN%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOzmT1YddEzXvZWzwWxHeT777nrJp7R2wXJx2NgTcsgAIgfH%2FTpgth0wGqLMTGJ3jqf4H%2B2ZVm0pG51sVVeWQhtToqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCloilv0YygSXiI1oircA5b0ACgDRp7GOTC%2FYLodMg7n%2FM0ZrXJgBpWebisRDjFHHVaAa8ZYxzZ%2FZbP9CaBts7vfMztGneYMy6WSF7Gz59Ubh5QJE797lWQO42%2BkiOq%2FsnqJXqLxm0BGYcb%2B5AMabIlHtsG4teA2Wqk%2FHPNhWXLPbJyIKARaqNCYm1RgWUr8UHsjYLhSEVK9xvmoVwQ4qVHbMoe38jUMIh5VW9e%2BEFLf5R1ek2iX4BHVzqlaVJ2IFPDaqQnLd79HITXWWpa0ml%2BfG22sOgdPWB5h4Wm5n3uO50FhSSMjmjTKMFtuDiiaxG4mXNnWansugPTCHrt1YpBa1MPJeJ3i3EKNhSM%2FChjP3XHOwjKwMvUaO6xQly5CjlvFEZ%2BuMgm0BciY2I%2FD7BevcSbpXHGAvHyWPSZAifBpSzm3F9IyutA9jLsvJnnIp0jtvBpxZcU2VztJVMoRg7VZ%2Bg3%2B0M4EmN9z5neFw7PgIyO2H1fMTxQi7jWEyLcXr4RlqNjQC%2FaF0Y1RL1bICZGWePn5Wa189jA6AuT0Pjuy7usRv2frDYXhBQKryAa8SfdCtZ1yP5E0kOzgK9oUTmDfRYKtxCds%2FRaOr5NskbrZp6OOW4Ub9RILk59N6%2F6FuOnfDiKT3%2Ffcci2GMNfDgcsGOqUBrsOe%2FQVKFnNuoGGusYREw18%2Bmz5C1Aa6AGUD2HRnAtl0%2BHpzccvHGv8L3ohOcwAESkvz9GxWw5Mcxv%2FrY8UWvKoo9yLHdrkAgxJqIggl9I5YRHgvKhzdEZQQbgEM4%2F1O233twbwFhgr5C16uB%2BlPgFnEE9ifd5Zj%2FLXuHoAwqTiB1YycX0ZWzbYvagY9jWd6XBpiCw8fE3B3buiBOn0W2zOMaLcX&X-Amz-Signature=13e642f22e9fb29f389039e1289ff61e986a0d5004ba5f4851b3b807fc1fed5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



