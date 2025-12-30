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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QRY4UGG%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1EL56gvMIK22ggnzkRxlaprmQAAntmQ2DLCaJrc06zgIgX2HHxZPR8fkfGZK%2FSXmsCjeE8HYtg5fH2Q%2BeoD3zK1EqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJbf5BHG4q%2BtMuzUircA4Pz6DiB76z5FmG4tREr5O8nkCw9QHwmRXbzxXqGgvzA9HO0%2BH0%2Bd%2Fp5II2GJBMY%2FJpRSrgo0tbZDFsOZskKJlVs99jw0iuJc%2FjG35CkH%2FuOov%2B3rcqVEqXbAfVK60RvhhrBuzIqmrjNW1Ac8wWrRCN7I7gMp%2B7uAFI1RqCI%2FmVxzSmGgAL6WF1yCCKq8wl2TAhwLnPUsfNPIKjDN08dkjHQgCBM0%2BZK1MGQglvXERTvbtBmXLAT30lueZQHk%2BMcxsOJhiCx6fHDSoJqA0mPAxiC9Zlw4ePlTW3IceOA3VDqT3p2akJ0QgUq6pS8v5%2FmX2ZYPMi68WXEGvhz8%2F%2BSxnHMNfqdUsnqbbXVPZ5m8Q36T1PtLn26vOerIaEHuwm6HLlEKPPBIYkU2Pgal6xhXjOvireUWlEBHLEALa7A7FsCxLTumGTtlbcLBF6vrmi8C0hh9qopMK7cYZTflEEgxfoWi0gjwOqUKq75BS0BQQy6Xgr2b8ZNNyva42NUqhOY4LqL12MVF%2BCNlqvo2afTZi0XUlmze7WRwU2ymglJwDS%2ByYtlaruQk7oAEs8Gu4b9jyV9Nz6A%2FAamn0RtRAu0bDRnUbzSOkx83mtrBrP7dJFxkQdqU0qXDcxPEBR4MODZzMoGOqUBm9ihZ9YIDmWz5rYGwUIIa2ZMK0z333EHXrIzWUdmBjr6UlzyNuG2tKpL7z7ZpULnmYzjAswbke7eYA0r6BZkR9SEhRkD1Gh4QVv4OkXt%2FyXbmPG9Vl309UcfcYl0nsMZjr1touVmvDgT4c41BvqxSSOBzmBtScwXJnugowzlBveuRG0%2B3tWxYfm%2BvPsk4Lm9f4PebS6fEZut1LDPZGZWdl8NGHZU&X-Amz-Signature=343a76d1c828dbf5f38a340a641bead55b7c90e4ef6d1cfaff4a6017c82e6902&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QRY4UGG%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1EL56gvMIK22ggnzkRxlaprmQAAntmQ2DLCaJrc06zgIgX2HHxZPR8fkfGZK%2FSXmsCjeE8HYtg5fH2Q%2BeoD3zK1EqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJbf5BHG4q%2BtMuzUircA4Pz6DiB76z5FmG4tREr5O8nkCw9QHwmRXbzxXqGgvzA9HO0%2BH0%2Bd%2Fp5II2GJBMY%2FJpRSrgo0tbZDFsOZskKJlVs99jw0iuJc%2FjG35CkH%2FuOov%2B3rcqVEqXbAfVK60RvhhrBuzIqmrjNW1Ac8wWrRCN7I7gMp%2B7uAFI1RqCI%2FmVxzSmGgAL6WF1yCCKq8wl2TAhwLnPUsfNPIKjDN08dkjHQgCBM0%2BZK1MGQglvXERTvbtBmXLAT30lueZQHk%2BMcxsOJhiCx6fHDSoJqA0mPAxiC9Zlw4ePlTW3IceOA3VDqT3p2akJ0QgUq6pS8v5%2FmX2ZYPMi68WXEGvhz8%2F%2BSxnHMNfqdUsnqbbXVPZ5m8Q36T1PtLn26vOerIaEHuwm6HLlEKPPBIYkU2Pgal6xhXjOvireUWlEBHLEALa7A7FsCxLTumGTtlbcLBF6vrmi8C0hh9qopMK7cYZTflEEgxfoWi0gjwOqUKq75BS0BQQy6Xgr2b8ZNNyva42NUqhOY4LqL12MVF%2BCNlqvo2afTZi0XUlmze7WRwU2ymglJwDS%2ByYtlaruQk7oAEs8Gu4b9jyV9Nz6A%2FAamn0RtRAu0bDRnUbzSOkx83mtrBrP7dJFxkQdqU0qXDcxPEBR4MODZzMoGOqUBm9ihZ9YIDmWz5rYGwUIIa2ZMK0z333EHXrIzWUdmBjr6UlzyNuG2tKpL7z7ZpULnmYzjAswbke7eYA0r6BZkR9SEhRkD1Gh4QVv4OkXt%2FyXbmPG9Vl309UcfcYl0nsMZjr1touVmvDgT4c41BvqxSSOBzmBtScwXJnugowzlBveuRG0%2B3tWxYfm%2BvPsk4Lm9f4PebS6fEZut1LDPZGZWdl8NGHZU&X-Amz-Signature=d43712b68c79e778d3acd1bb599e79d574eff0ab93bb4ffc8ee160b1b21fd6cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



