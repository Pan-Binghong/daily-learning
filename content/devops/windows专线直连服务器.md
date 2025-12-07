---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVZGKYVV%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDH6sOSs4Tb5lwcgFt9xUO4FTlDyKAHC58LzkAlywNLUAiEAinlvPLDcBo0gHGPGHKbps4%2Bn%2B8eAflAGyBGRkibwDCUqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD4J73cpFQ3moOSwWircA4A4WmKYbaBXXLBC7ZuWLEjGTZGvl4sqvmmZwvnq5mUYqclD4b6LCZJXPVzIEPNBDYTENgQO0qlJJqXBVbylcFmw%2FxqGOMsBdTNcoVrsvqyuliRHMKvZcdcyLvRzbbvNnB2XaqDkYEZS%2BH6zchbIWJ2RCauVR%2ByLw%2BdgyXS38TlwrCvec4qBZrVb%2FKeUrlYEpG7O%2FNUpVKE%2BIDoxm7WIxxI4%2FHpPc6kvKaIxcA8wis1k7JjbxArvP5icGbCm%2FcrFvKBoRFcmiZQxUKQ7Qp7NJtdyvNrdHM%2BoxACW1eRcqOCbIfKiWJeG3WYIPda6lpbPSvCXx2VMzNWL3TGxgtlb7neeOCiMOdhNQqS3DHgv8XNJhBzx4sWJQPtjmTBaSL2OqYG5suGjj7x%2B5eoXZb5sj99l6VGHADTd697vGFDcVbFPrctAiHgowVrc3E2DY3pqkXm5WlUZ7bBBGSL5ERyOpQBC0cdYLUO0EgiBYHnHWI%2FDqXIrEEsmqTyGKSWwyidbVRwYfLT9AHChkbDcWSe6P7HvIQU0aLERSJChucbVLqCDbwrFP3Fe1ZOPgKkHkKk6KuZp8QU512%2B8QJuiFIeOF%2B4GwAHDSRxRuam7IDknosBWaN5OWeQHoWY5Kh4lMNj90skGOqUB7NTdkTzW8Pux2xH%2FEHjkIFwUW2%2FCyj0UoVosf9Fga196p2lvS4pnnDhjUsmPpO%2BVw1o3msfHUD6EBIXHnHewX0yR4%2Bjh8Xv9GjXSh2g9wyImHvw9Vab%2B77cqAnDe4Y0NO1TE1olJcMiwJgRCu5nHE9q0Q8Sw0Th%2BGa1E18UtMee28MxQQRV2mJS7FARt%2Fo6BLMGR6irnkSKgkoVWaIZej5XCLWO0&X-Amz-Signature=6a98f9fb6fc19392f8ba8f7a6f69a832b6260917b026099bd7b95f793d41a435&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

