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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTX5W64%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpCEHyeaK86%2BtvrZGpU6FzHzYzrTxvNcR7w%2Be6drFtMgIgAYkglPp2JYQor0n%2BQubgZsuoz35i%2Fx7etGXiaP2j72Eq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDBZzzchOCmR7qk4arircA7QFWZ9fcWU6mP17kyNaRkMAlqg%2B7ffgM076KhOKPbzSgdPjAVbpBhHNicxww2kA07Ey6blA%2FPcaMijsY1OApV%2BUHXIurlxWXJGpxgLlXyXggsc%2BWZsBwPB%2FMcgqwvLyQG8nP8j7U2Cn0PPOC17rQJHMy8sDzQJ7vIiuoL3vBZs%2FdMauBb%2BYUQZczpdO72%2FDYIWHvsOg1EzBybem%2FXtg5u%2FRhlUt6hlBnFI57tiPqCgDdeukOWqFvq9bMc31b95FBRnCg4k8X4qrKwOEBIf39PljTMtp1UPOpVr5uOLclpxibE7XNBvb2D4VbMgQzatYNC41F7hxW3dAyycw0z3OJFUCL3NrczEsWWoE9RT4EgDSLjNOmdq6ZRPCJRBnaf1fJAx8z55wdKU0058MSb3kWCWN3rsygK1wS%2FBH88xbczIdwwZ1R%2FhVfznI%2FpynSWfS4BpPpj0aza9tZxQE6Be%2BrMa%2F%2FBAfMU2O%2F0I1hY8XxzyQdrWFy0jx7RPldhin9g2zWMUswxN6fJopJ5nLn8TCgX1KhTAcr99QBxCwL0S52kcxR4ciICRQlk8Q32J1VhHeGgAROXX4nI2BcGzyyL1iXHETYT9Ln38fmht3j6N%2B6ciqRRY6xneIr3DGIrkVMJGWic0GOqUB3n2txLnQcBGv7Xr6S6eajaj%2FJjrRkKjwM6BG9KUkaogFtNenTz2xy6xlxZ172XOUdOiMMho3dhG9QxnDxLaClrOTSbjF2E4PnMz%2BXS6GMHcYO3oNY%2BtGYPyXUsrnj%2BaL7g4qdhq0CAuL0G05iLROqHzIYpv6d1dALFLICXuaKWMFPskI6i0zk3Q2JLvzC6OcFNicD7dqimPxCg1uKJl%2B3x%2FVa8Gs&X-Amz-Signature=69eec92d90cf0a0ceb592ecc2f9154d0c0280edeac6d3335f652422c1941d633&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTX5W64%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpCEHyeaK86%2BtvrZGpU6FzHzYzrTxvNcR7w%2Be6drFtMgIgAYkglPp2JYQor0n%2BQubgZsuoz35i%2Fx7etGXiaP2j72Eq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDBZzzchOCmR7qk4arircA7QFWZ9fcWU6mP17kyNaRkMAlqg%2B7ffgM076KhOKPbzSgdPjAVbpBhHNicxww2kA07Ey6blA%2FPcaMijsY1OApV%2BUHXIurlxWXJGpxgLlXyXggsc%2BWZsBwPB%2FMcgqwvLyQG8nP8j7U2Cn0PPOC17rQJHMy8sDzQJ7vIiuoL3vBZs%2FdMauBb%2BYUQZczpdO72%2FDYIWHvsOg1EzBybem%2FXtg5u%2FRhlUt6hlBnFI57tiPqCgDdeukOWqFvq9bMc31b95FBRnCg4k8X4qrKwOEBIf39PljTMtp1UPOpVr5uOLclpxibE7XNBvb2D4VbMgQzatYNC41F7hxW3dAyycw0z3OJFUCL3NrczEsWWoE9RT4EgDSLjNOmdq6ZRPCJRBnaf1fJAx8z55wdKU0058MSb3kWCWN3rsygK1wS%2FBH88xbczIdwwZ1R%2FhVfznI%2FpynSWfS4BpPpj0aza9tZxQE6Be%2BrMa%2F%2FBAfMU2O%2F0I1hY8XxzyQdrWFy0jx7RPldhin9g2zWMUswxN6fJopJ5nLn8TCgX1KhTAcr99QBxCwL0S52kcxR4ciICRQlk8Q32J1VhHeGgAROXX4nI2BcGzyyL1iXHETYT9Ln38fmht3j6N%2B6ciqRRY6xneIr3DGIrkVMJGWic0GOqUB3n2txLnQcBGv7Xr6S6eajaj%2FJjrRkKjwM6BG9KUkaogFtNenTz2xy6xlxZ172XOUdOiMMho3dhG9QxnDxLaClrOTSbjF2E4PnMz%2BXS6GMHcYO3oNY%2BtGYPyXUsrnj%2BaL7g4qdhq0CAuL0G05iLROqHzIYpv6d1dALFLICXuaKWMFPskI6i0zk3Q2JLvzC6OcFNicD7dqimPxCg1uKJl%2B3x%2FVa8Gs&X-Amz-Signature=953baa80195f03b1510dd6375ae14727498fb2501a670550fdd69479c3574125&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



