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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFEGXSLC%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIHnsG77435fgctdhj4oGkXhdG9gGeURyDNsHC4jFp%2FLbAiEA6rnTG7mvXSAg2pYj89G3xgSiBtwovjFjwHlNYCM7CFsqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGqBc%2BdP5GOTCOO83SrcA9vZjlF%2B%2BUKeCP18KYr5yA4ho5Sry5eeCvoR8Mcz%2FAGx5zWVswwifJCpKWx6EQjzJlJhxoWCl%2F%2BFk%2BVsoiRCzjEpBh7MTZu0NGCa1dVuzjsYTgADBpCLVMvaAWMyKJS8AjaaYf4mZ9e7nhFvuGJbI8r2MRWcsURUhBi68q9stMY2yLz3KgxsKD6R6oRPgn%2FZGYCp7RkChBdlhhcRR3JpqBfBb7g%2BLSbmPvSixJz%2FG%2FVvPnZ6B7dhTQEerAVdmUWY34QAM4hoSAvtyJLmoFNAPyD%2B2kh5mhTFYPNkBARb0PTws0cIe1E%2BjExlIrorDTw%2BrqsfMN8bmzzNddUxtju7vi4YdQVg8ayzo%2BXmdzRmMSB9TStBjzK5jyF0QHeB%2F%2FrALW8MCRn64KMJswKx7FUBLTFYV29RqHFHD4PKi0HEY41TCu%2B7WWufnyM4pr1jRDJ%2BIsFl2Wwln2CHFlc0Lvtlt09Oeu%2BKsROrApAHiGJ7sTJnAZ6qKbCfM0aRkzIKsQVlm%2BYFzugN3ljSOmoNsQN%2BG8bpvS9N%2BZhMomtAh%2BctfHnvCwsfYdnM9gJc5Q%2FTkHMoxkkIGgzml3qtne%2FXfAVXHtgQqPulWeiFLX76q0vn2OpU9Hv0D7141kqK6r0CMI2m6M0GOqUBv7m3VzZzZpx7QwGHNZW2OMKGSP1RHieP1fbcfuLBx3%2FoPT0YzoA9W2N%2BfEAbeTUVdsRKxo%2FZ4agLKCsrcohaDQeqjDCKNxTZwC0UvahflaDlNhFmji7JZwqF3F6K9iyT78aT%2FJiD9p8x4IpLkBHJAlD2lURyxOXpKeqL1oDaYFetvIOWA96pUAhzoy6FM3UqWbbzyd7UlkUgzHv4lpxIDZjAe3YW&X-Amz-Signature=7b3caac3854b890ddc2686cf64832c1eb932ced64cb7fd23a92feebeaf4d8e68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFEGXSLC%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIHnsG77435fgctdhj4oGkXhdG9gGeURyDNsHC4jFp%2FLbAiEA6rnTG7mvXSAg2pYj89G3xgSiBtwovjFjwHlNYCM7CFsqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGqBc%2BdP5GOTCOO83SrcA9vZjlF%2B%2BUKeCP18KYr5yA4ho5Sry5eeCvoR8Mcz%2FAGx5zWVswwifJCpKWx6EQjzJlJhxoWCl%2F%2BFk%2BVsoiRCzjEpBh7MTZu0NGCa1dVuzjsYTgADBpCLVMvaAWMyKJS8AjaaYf4mZ9e7nhFvuGJbI8r2MRWcsURUhBi68q9stMY2yLz3KgxsKD6R6oRPgn%2FZGYCp7RkChBdlhhcRR3JpqBfBb7g%2BLSbmPvSixJz%2FG%2FVvPnZ6B7dhTQEerAVdmUWY34QAM4hoSAvtyJLmoFNAPyD%2B2kh5mhTFYPNkBARb0PTws0cIe1E%2BjExlIrorDTw%2BrqsfMN8bmzzNddUxtju7vi4YdQVg8ayzo%2BXmdzRmMSB9TStBjzK5jyF0QHeB%2F%2FrALW8MCRn64KMJswKx7FUBLTFYV29RqHFHD4PKi0HEY41TCu%2B7WWufnyM4pr1jRDJ%2BIsFl2Wwln2CHFlc0Lvtlt09Oeu%2BKsROrApAHiGJ7sTJnAZ6qKbCfM0aRkzIKsQVlm%2BYFzugN3ljSOmoNsQN%2BG8bpvS9N%2BZhMomtAh%2BctfHnvCwsfYdnM9gJc5Q%2FTkHMoxkkIGgzml3qtne%2FXfAVXHtgQqPulWeiFLX76q0vn2OpU9Hv0D7141kqK6r0CMI2m6M0GOqUBv7m3VzZzZpx7QwGHNZW2OMKGSP1RHieP1fbcfuLBx3%2FoPT0YzoA9W2N%2BfEAbeTUVdsRKxo%2FZ4agLKCsrcohaDQeqjDCKNxTZwC0UvahflaDlNhFmji7JZwqF3F6K9iyT78aT%2FJiD9p8x4IpLkBHJAlD2lURyxOXpKeqL1oDaYFetvIOWA96pUAhzoy6FM3UqWbbzyd7UlkUgzHv4lpxIDZjAe3YW&X-Amz-Signature=998e4af1ac9a5f284133ea603bf22567f81fae8564326b8775c61c78fb6a8527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









