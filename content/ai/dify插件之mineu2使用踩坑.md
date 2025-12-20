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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIHKIHCR%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FZ8FdPwJvt%2Fz3st5yFAS5JIS0CuKZpW%2Ba2%2BFOU7B4tAIgObvroJaKzv6YRemV8G7Q0qhcFQVemXoS8CdbNN4f4iIqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2FSKpd%2FYqKyVY%2BiircA2ojQYCjtqeh6%2FmJ4CI898qOe%2BuCPR1sN5M7aRGBdG4l7rkDstkBa1FCz6%2BPZh%2BNTynh9kpghyXJ9CMxcxE%2FnwQUrp0j4NRts1X8qNNOC40An4qa8WLbJJfbnCp0YQaVCaYupjdjF3LM9%2Bjrfi359roEKoSWBiUu5QyCgsUHiPuu9xgiynZ4jKgxV4GPD%2B%2BQ2L5NKf8RymnQ4zOwGWbnNyNmxyoixkasRnWv6Gh4SHkPSyC%2B0i0%2BQyTzh3QJ4BKLYVPLriLZ4JqE9ZdFzJ%2FiUc5yZJHOPWQv7HIYnyrH0Q1ZcNUAY%2F4ApIsqGrYRWEP1mULyDqsGO2rhj3T%2FjfWLrwzHfFX8YVabLULA%2B%2FJ2JrteAIf7DgiYqhoNMHf0aC5U1AX8%2BRGTqZby1d5l7unZlluANTUDSgtKvqpiUm9umfAiz8Hi%2FosXeR3g5wOsGKKdodoH4Lt6PU5ixZA5aGsrPwcQFosHlG2jz8i1%2FCDimt0FGSrAcGC1Omzs4bfuj1%2BziKmnW3t%2F%2BRYAFuvRJMOv7gJJ9WgeZUffRcDOeg%2FHb95fsP3h7ge%2FAfhRO%2Bdyjo4b%2BLR%2BWPKHebtmt46dWAA2BobJiucXAF99TkfRvezZKQs%2F959NN31MvVbc1w5OMMqFmMoGOqUBvNOxJ7UVqWUYPIavq8pEPbJRGShKsmA2i7SY3qvXNm1RI7kyf%2Bn%2BQnWHzbQAsouE64L9fCAU7%2B9fNWVx9TbVgdBmwTzR6PmR0tszQveMp4Ixd3grXOgii%2FCPPSd2oNUvmwUmOB%2F0%2FVz6W6q4%2BKlBIATqBsKdkDSHir2%2F9qYnWtstjJcJesYKuIzk7ew%2Fjc%2FA8it3MUqu4Hjx0JtO3Ebb%2FLrdf354&X-Amz-Signature=47eb0e5773ed7c1151440ea8ec6cf9b3178cf5b6a608fa7ddda3d1e475f58618&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIHKIHCR%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FZ8FdPwJvt%2Fz3st5yFAS5JIS0CuKZpW%2Ba2%2BFOU7B4tAIgObvroJaKzv6YRemV8G7Q0qhcFQVemXoS8CdbNN4f4iIqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2FSKpd%2FYqKyVY%2BiircA2ojQYCjtqeh6%2FmJ4CI898qOe%2BuCPR1sN5M7aRGBdG4l7rkDstkBa1FCz6%2BPZh%2BNTynh9kpghyXJ9CMxcxE%2FnwQUrp0j4NRts1X8qNNOC40An4qa8WLbJJfbnCp0YQaVCaYupjdjF3LM9%2Bjrfi359roEKoSWBiUu5QyCgsUHiPuu9xgiynZ4jKgxV4GPD%2B%2BQ2L5NKf8RymnQ4zOwGWbnNyNmxyoixkasRnWv6Gh4SHkPSyC%2B0i0%2BQyTzh3QJ4BKLYVPLriLZ4JqE9ZdFzJ%2FiUc5yZJHOPWQv7HIYnyrH0Q1ZcNUAY%2F4ApIsqGrYRWEP1mULyDqsGO2rhj3T%2FjfWLrwzHfFX8YVabLULA%2B%2FJ2JrteAIf7DgiYqhoNMHf0aC5U1AX8%2BRGTqZby1d5l7unZlluANTUDSgtKvqpiUm9umfAiz8Hi%2FosXeR3g5wOsGKKdodoH4Lt6PU5ixZA5aGsrPwcQFosHlG2jz8i1%2FCDimt0FGSrAcGC1Omzs4bfuj1%2BziKmnW3t%2F%2BRYAFuvRJMOv7gJJ9WgeZUffRcDOeg%2FHb95fsP3h7ge%2FAfhRO%2Bdyjo4b%2BLR%2BWPKHebtmt46dWAA2BobJiucXAF99TkfRvezZKQs%2F959NN31MvVbc1w5OMMqFmMoGOqUBvNOxJ7UVqWUYPIavq8pEPbJRGShKsmA2i7SY3qvXNm1RI7kyf%2Bn%2BQnWHzbQAsouE64L9fCAU7%2B9fNWVx9TbVgdBmwTzR6PmR0tszQveMp4Ixd3grXOgii%2FCPPSd2oNUvmwUmOB%2F0%2FVz6W6q4%2BKlBIATqBsKdkDSHir2%2F9qYnWtstjJcJesYKuIzk7ew%2Fjc%2FA8it3MUqu4Hjx0JtO3Ebb%2FLrdf354&X-Amz-Signature=45d282b9b1622ac2fe59f09ac9067545405cc8d9339afec7dd6f51417e759fb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



