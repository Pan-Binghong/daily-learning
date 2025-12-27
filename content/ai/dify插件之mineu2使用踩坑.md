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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHUTV2V2%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEedVA4FAsUhUI17zP%2BNb%2BAw4fPgnVc%2Bh8JKIRA6PIk8AiBPxuXa2FUZYH8nR%2BTAfGLlJyLANZPjyLEs6FwOW0GOpSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIML4mbGVbHhKdpnhUdKtwDBW46m1U%2BTqexu0yU2hfPxIoE0BNu4iAcJk%2F4PqQvw2%2FhxjUWJ9efZF1PeDj9uUITp4L9tzE8yTIvYxEHoDkLZhjO0vmNGoG9m3U4FtnU6IZNg5uHSVjidDBoxGMONjo%2FUyrZzd%2FMqeeagk9geLXmQGAQ2LljKcF3NpcCBmTnnhCPi2R4lhnOLzIaLKCy2HlDOSQcCqps3CZ99mQLsc2wgqPxS2BgOj869ojRj42eNllI9wwzNTls4ch8HuVHqowFYVf%2BmSvP6R%2B%2Bpu%2BNaH%2F7ruvmla44jkQGk5aOwRcKDXsQxrU3t%2B4x7BxEa%2F1NHSWh7X7m%2FaqmqJe3BCtm2dmqZ1odsZxUqRfRq%2FtIZrtSDm16liPvtUEXVQhBOIYmp4wqxgQOpWMngZAraUuDIYiVkCzII0P0hXCTLbQ5ilihKlU5D1jn9oiDwrCPE9XBZiXHWkbARBaQzuDiYIAEYwCv3wajK8T2x9PHOhw23bIWzRXdErmh%2Bzi5f2s%2FBjjp7x3v2uWUhM8OZkB0gVv1oM7zQLsfd2ssAW23%2FjtoVv5bZAqr74X3mAaONVlDWMC42ZrS8eMS3vfnWvdrygsZr2yOWEYMMdC7vGmtM8crYKxp05aC3USW1E3UrjlxDx8w6%2By8ygY6pgG8nlaJ7sHxh2ZfQWon4R%2FNNlNQ7n4JjrooZO14cB1HqKiw6HetWLEfRv8qcDpGmLHNJ8NXfkMoK3spgiP5MkC1DVQvCNK5qwzCQrOOGheE%2Fzm7g0cUVNjWpS3FORDIpIpx6ivfGhpq37HWaJ6ROqoeEh6hjtk%2Fs77dwc6CLscRWXU5i9ZX65fBBOxZcXm4TOKwB0j9fqy8NaaRYjXS5wfgB2k1D7nz&X-Amz-Signature=ddaff93df49d94c056ab3ff0753533fe28981baa083f0b8e8ebef17677e9dd99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHUTV2V2%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEedVA4FAsUhUI17zP%2BNb%2BAw4fPgnVc%2Bh8JKIRA6PIk8AiBPxuXa2FUZYH8nR%2BTAfGLlJyLANZPjyLEs6FwOW0GOpSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIML4mbGVbHhKdpnhUdKtwDBW46m1U%2BTqexu0yU2hfPxIoE0BNu4iAcJk%2F4PqQvw2%2FhxjUWJ9efZF1PeDj9uUITp4L9tzE8yTIvYxEHoDkLZhjO0vmNGoG9m3U4FtnU6IZNg5uHSVjidDBoxGMONjo%2FUyrZzd%2FMqeeagk9geLXmQGAQ2LljKcF3NpcCBmTnnhCPi2R4lhnOLzIaLKCy2HlDOSQcCqps3CZ99mQLsc2wgqPxS2BgOj869ojRj42eNllI9wwzNTls4ch8HuVHqowFYVf%2BmSvP6R%2B%2Bpu%2BNaH%2F7ruvmla44jkQGk5aOwRcKDXsQxrU3t%2B4x7BxEa%2F1NHSWh7X7m%2FaqmqJe3BCtm2dmqZ1odsZxUqRfRq%2FtIZrtSDm16liPvtUEXVQhBOIYmp4wqxgQOpWMngZAraUuDIYiVkCzII0P0hXCTLbQ5ilihKlU5D1jn9oiDwrCPE9XBZiXHWkbARBaQzuDiYIAEYwCv3wajK8T2x9PHOhw23bIWzRXdErmh%2Bzi5f2s%2FBjjp7x3v2uWUhM8OZkB0gVv1oM7zQLsfd2ssAW23%2FjtoVv5bZAqr74X3mAaONVlDWMC42ZrS8eMS3vfnWvdrygsZr2yOWEYMMdC7vGmtM8crYKxp05aC3USW1E3UrjlxDx8w6%2By8ygY6pgG8nlaJ7sHxh2ZfQWon4R%2FNNlNQ7n4JjrooZO14cB1HqKiw6HetWLEfRv8qcDpGmLHNJ8NXfkMoK3spgiP5MkC1DVQvCNK5qwzCQrOOGheE%2Fzm7g0cUVNjWpS3FORDIpIpx6ivfGhpq37HWaJ6ROqoeEh6hjtk%2Fs77dwc6CLscRWXU5i9ZX65fBBOxZcXm4TOKwB0j9fqy8NaaRYjXS5wfgB2k1D7nz&X-Amz-Signature=f409a203780268f93459afcaa4bbef61c009a8bdf9451a68dab3905a8416adde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



