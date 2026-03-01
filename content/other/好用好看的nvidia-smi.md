---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QREYRF3Q%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJfqIM9MWgi9MKkbufJnNopBWCyUp%2FVU9cPBIdKhF7BgIhAKBskIvxIzDbxHBRfFGIUuIVeDaTY1ffaqsLkqBdMY0MKv8DCGQQABoMNjM3NDIzMTgzODA1IgwvXTQNzdTkDkYKU4Mq3ANjxllhNxcypBC8sxELDOMvLaA%2Fa1FKi%2FwIit%2BJwRTMJecJ5twqZJFITpM0eH2WjtzQ67pyMziKVdJqfDCmRQB9ZobMT9pptbdINL837Ngl%2FIKdiE40qe2rthmAyxrh71R8dyKdZNykEZk1z%2BWOxNw60a%2BJcffsxl%2FIRrycACGrTmQOD9fULKTN5%2FkSqaQCkc7yw%2FIEfATrm2RHImviQXdn81XL2XX79nn3Y%2BT%2B70CX%2BiS1Hv1Bs9dxAVsfADsViDVjJkMaJiBm6%2FnPoWFE5B8S%2BrUwtiUSo9IruRSqlSGCbO%2BLpMbofpkE2td0QepaSTiOMhLwnZdnrX2G95M0MsIjQ5P0fwfsBFEaVwtxgFp03G9ROrV5OBwBs%2F9NtYAj0HEO%2BUejE3IZyV6Sz51wu727xvhpV6Drnot4ct%2B7gcEOe6mjMEWec2HdUMPqkG7%2BDpYXnxNNkEeD0JoN7atFur2uob9wKte8MoiwNeYRPWAw2B30dONSckU1ei2FhWAWm%2BZPlQhw8jjjyohvx557fuz0iwHcwhMFsaWafPbBVMVAIvZfvLOOXKNSs0mguVH%2FZ%2FdA%2BBSgxvufBf9Vm%2F1WrwPi6X0x%2FLGYJX457sHSne%2Fhz7SSjII4KkJKHaScoTDDzY7NBjqkAdqnkRuDQcyayDMOhCoev8rU1aFluNZe%2FNuWY0JwnAC5mRCjYJQ%2FVZ0RRXlP7qsJXUU46SOXl2JF9h3%2F1prYXnGFe6gH%2Bl0MBkJyUBeI2tYZ1Fp82n2SICE8zPGzv5uoj%2FotGmvUOqS7s8hUEOTw1In3ZODYN6G6XOG7jwljSd%2Fsi4jRmQgr%2FpNRQShT5LpSjEKUQ2aOYxOG3b%2FaVOTiB6lTylLD&X-Amz-Signature=43fe1d9b26500d1b3b7de84a55006ee1bfedefa1759af346a7170b9cb8eb3cd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QREYRF3Q%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJfqIM9MWgi9MKkbufJnNopBWCyUp%2FVU9cPBIdKhF7BgIhAKBskIvxIzDbxHBRfFGIUuIVeDaTY1ffaqsLkqBdMY0MKv8DCGQQABoMNjM3NDIzMTgzODA1IgwvXTQNzdTkDkYKU4Mq3ANjxllhNxcypBC8sxELDOMvLaA%2Fa1FKi%2FwIit%2BJwRTMJecJ5twqZJFITpM0eH2WjtzQ67pyMziKVdJqfDCmRQB9ZobMT9pptbdINL837Ngl%2FIKdiE40qe2rthmAyxrh71R8dyKdZNykEZk1z%2BWOxNw60a%2BJcffsxl%2FIRrycACGrTmQOD9fULKTN5%2FkSqaQCkc7yw%2FIEfATrm2RHImviQXdn81XL2XX79nn3Y%2BT%2B70CX%2BiS1Hv1Bs9dxAVsfADsViDVjJkMaJiBm6%2FnPoWFE5B8S%2BrUwtiUSo9IruRSqlSGCbO%2BLpMbofpkE2td0QepaSTiOMhLwnZdnrX2G95M0MsIjQ5P0fwfsBFEaVwtxgFp03G9ROrV5OBwBs%2F9NtYAj0HEO%2BUejE3IZyV6Sz51wu727xvhpV6Drnot4ct%2B7gcEOe6mjMEWec2HdUMPqkG7%2BDpYXnxNNkEeD0JoN7atFur2uob9wKte8MoiwNeYRPWAw2B30dONSckU1ei2FhWAWm%2BZPlQhw8jjjyohvx557fuz0iwHcwhMFsaWafPbBVMVAIvZfvLOOXKNSs0mguVH%2FZ%2FdA%2BBSgxvufBf9Vm%2F1WrwPi6X0x%2FLGYJX457sHSne%2Fhz7SSjII4KkJKHaScoTDDzY7NBjqkAdqnkRuDQcyayDMOhCoev8rU1aFluNZe%2FNuWY0JwnAC5mRCjYJQ%2FVZ0RRXlP7qsJXUU46SOXl2JF9h3%2F1prYXnGFe6gH%2Bl0MBkJyUBeI2tYZ1Fp82n2SICE8zPGzv5uoj%2FotGmvUOqS7s8hUEOTw1In3ZODYN6G6XOG7jwljSd%2Fsi4jRmQgr%2FpNRQShT5LpSjEKUQ2aOYxOG3b%2FaVOTiB6lTylLD&X-Amz-Signature=8573496ed2a3b8a13cf472a5f64f8e47dbc10d9a5ae9cd203720147016fb65c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









