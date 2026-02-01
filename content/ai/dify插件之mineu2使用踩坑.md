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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKKZLFYP%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG9QB8gQYBCR7DJHSQ5%2BYnON6EYlXextGmWCeENhKYPfAiEAi6NaRZAXa10%2Bp%2FLdDQuZii6npdMYLLx7tYMADrGmZ0sqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3Y55aJfxwHEAGlFircA0rRnB4bm83%2B0nt9OSEufi4FOnx5rTERDotMPZBplNtzxaTNWW%2Fb6wNKPLcw2uA6OPxokR%2BG%2FQw5%2BZQsV3bxr4GjpcP3MPtqCZ%2FVMxJ1bc6VaHgi16thqXCOzyY7PYy%2BtQb%2B5JSGPoudEiHDWqeE9rxNJP%2B80%2F9zaawbLe9L1lVpETNycXCXvyV5t7WKX9VzeyFE%2BouEd%2B85zF5ParGyJRi%2BjdKpY7%2Fz6JTk3WIeI3SU4WkqnZZcLmG%2B81RfkLiFPaOB%2B2pZMeH4M9vFHlsNqfuaRVlu71496Ua%2BtYOfgqJ8uIKqhou5QsVnoPSGRlWf%2FoDypOU%2BK1Nbx33b3Ywc8odatBH%2FXWpufD8UJ8mhd4TYkGCj8amtFILhcYCLCLrhCM1pq5FMlWV5TXSLz9rzPemdsHSYbbPInbc%2BevGvElmi3awE3gnsInOYFItN04KeLsA%2BU%2B9jup4JcE8LChlVc2M4koU0sJ4b1lI9USrzU7lL1aNYho96d1lFGYnrlG87du5ecG94k%2FpLzGL8PLSzoX01eG5eRkyag4QtXnVMKHyKp52IuouRzorI74wT2Wtq2GlZ%2BehLHPliyFh7DWM4RG4cGPXfNGWJmEsNQvTzp8g%2Bh6kLFYNAnYcIi0ZYMMiO%2B8sGOqUBUzvGUpP13hkyKIjg5Ci9oIc39uyhZeCkroaFNMPAPFlevifcnswUQUHo2LqRvnAfEe2%2BuXO5pIR%2BOnAFdStDto%2BCGbD6NdjNXhgKeI0uKEz7u0ciDKyeS%2B96cEhagwmr3uME%2FNId3DagXi6q488Z8doDo3Vk0BCdSu%2FnUB%2BwtPqHNVNF3i5JaBbst4KLe2sIEsF%2FgcZ45Vm6kNSwMknokjFnuyyH&X-Amz-Signature=e9b083cd7a1bb8e24dd0d5f78c615c03fed7ddce9cfc60d5f5d042987615c3af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKKZLFYP%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG9QB8gQYBCR7DJHSQ5%2BYnON6EYlXextGmWCeENhKYPfAiEAi6NaRZAXa10%2Bp%2FLdDQuZii6npdMYLLx7tYMADrGmZ0sqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3Y55aJfxwHEAGlFircA0rRnB4bm83%2B0nt9OSEufi4FOnx5rTERDotMPZBplNtzxaTNWW%2Fb6wNKPLcw2uA6OPxokR%2BG%2FQw5%2BZQsV3bxr4GjpcP3MPtqCZ%2FVMxJ1bc6VaHgi16thqXCOzyY7PYy%2BtQb%2B5JSGPoudEiHDWqeE9rxNJP%2B80%2F9zaawbLe9L1lVpETNycXCXvyV5t7WKX9VzeyFE%2BouEd%2B85zF5ParGyJRi%2BjdKpY7%2Fz6JTk3WIeI3SU4WkqnZZcLmG%2B81RfkLiFPaOB%2B2pZMeH4M9vFHlsNqfuaRVlu71496Ua%2BtYOfgqJ8uIKqhou5QsVnoPSGRlWf%2FoDypOU%2BK1Nbx33b3Ywc8odatBH%2FXWpufD8UJ8mhd4TYkGCj8amtFILhcYCLCLrhCM1pq5FMlWV5TXSLz9rzPemdsHSYbbPInbc%2BevGvElmi3awE3gnsInOYFItN04KeLsA%2BU%2B9jup4JcE8LChlVc2M4koU0sJ4b1lI9USrzU7lL1aNYho96d1lFGYnrlG87du5ecG94k%2FpLzGL8PLSzoX01eG5eRkyag4QtXnVMKHyKp52IuouRzorI74wT2Wtq2GlZ%2BehLHPliyFh7DWM4RG4cGPXfNGWJmEsNQvTzp8g%2Bh6kLFYNAnYcIi0ZYMMiO%2B8sGOqUBUzvGUpP13hkyKIjg5Ci9oIc39uyhZeCkroaFNMPAPFlevifcnswUQUHo2LqRvnAfEe2%2BuXO5pIR%2BOnAFdStDto%2BCGbD6NdjNXhgKeI0uKEz7u0ciDKyeS%2B96cEhagwmr3uME%2FNId3DagXi6q488Z8doDo3Vk0BCdSu%2FnUB%2BwtPqHNVNF3i5JaBbst4KLe2sIEsF%2FgcZ45Vm6kNSwMknokjFnuyyH&X-Amz-Signature=a19cda8831c82aa74e9528123dadd8f974208ec0391d1300356566c51f56e7c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



