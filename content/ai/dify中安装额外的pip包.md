---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBLSTUQD%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIHOiJ0LnB5Zkh0E1KIkzie4vJIF0oF9Dq5Ias%2Fcxo2DHAiBMNX%2BwablBAXCUcPE7ebaMMQW9PYThj5ieKm1frA%2BWxiqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7ec50es7FUW94FbHKtwDf4GFl6rDaJoAsEoWbFqUT93ZKvyLTCqKKtIg%2F5uAx1DPLs4S7XqvjvVn67RpBLi8fcwAmOLtqoK6KBQ0cydKdQZrUQ4qZ6xMKk1573NJBPEG1MCyHH0aNLZW11U59K2hC0OZ1lD6VVsUHr6vYXtNnGKamKZGVliPYtBlsnFEx6o3KHKKZe7o5WXttZLB7S6DECCiFnVfpukTgdcGDDf6VRfisP%2Fg44G7CvHJthhz54J1d2podfkGPtFtKOrCEE9aX%2BVyPL%2FYtQCVQOdWR72kMZfC8I%2Fnr3aWKVOmUjyZLXN%2FuKAhIPCqPQ5652rafGa13tMF4qG9kD%2F0Es%2F6Xp1dm8rxniWb03N7%2Bpx%2BodS%2B2hmQF6qQE7tWm2a6X1o1Q7MXoLhCRAeajNEpwr2qeE3B%2FHj0T39kqHm5BEIfN3LniPx1CQEvonvOEpH2TDVzXE1i%2FgSXDGiN1qRxGB%2Fm74TlDegIo4PGT3VqXotVP%2BLKOnfWsbfabmq%2F077H3J0YndeyEpRdYEGC7hT0bWTID7r1wC5uB3%2BXeDNgHkd9Xe5WCk5tzVAUN2PGJFRQ%2B9HYNSibmZ2Zh2WppURzHqqu2Sdf54%2FF0CYrWSBMEtDQBc6JkLjz%2F4x23OxFgmMrwqIw09iFzAY6pgH5YfboabEltp7wzhEiI3rsNDuh0GLa04ZreBckAzsF6Xs6fswwg2VVqsDfzVVpT90W5EXv5Sl9OEBGFnBF4sAqy%2B%2FDzML3BCkVC9ON3PdoJdMwxHsyr3zA0gXyh5g9WhJkuRDgwan1FC8Vos6nWROAr%2F6t26hV10F3XK76wojCmrYzBdx4AyH1N6D9qk1qkLx8GLsCYxe1ih6kYd4Fv2LTB%2FL6C7iK&X-Amz-Signature=58b013912199cffd437ec483a17233f82503812def81beee5a64df36144f55d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

