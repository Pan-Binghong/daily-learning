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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YL5J5ZKZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCuQ30z%2FWGlBBop0GdAcVAciKEJxwzNXl%2FHDX7bKHvfnQIgKeC0w1AzOz2msGKgp0cExzFIjkvsxfTbo48W%2FEMjR6wqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJv81cgvMr1jLGFRjyrcA05kzKs14vEfWPmFn6FokLfuezrlJ6lHxx%2BbAA33D1U8GJX9wp8PBEPekMPsaZoXi7a3QKlh5jC9qK8%2BaQleBoTUz%2BhsZG0wgjxuP%2B2OW%2BmGU4czK0uGZPyRjV7G9LXWreCkrlYEi74JKaEfINkPvVdzuNRwWtyq1rAs50IwwJ1%2B3T8ikO5%2B3UCAamUup%2FcrL5kU8XMkYSANgPkIVGlqdxwQ7WkecV%2B5uy3yXXinESEvZ6okCFR8M6yK42uMhI47IefgsC6CbCeET%2BogEPpJuV3QvCqZ7DPcga%2FDkYGIt3VmpxWLyyH%2Bf2rdWLj5iAlBd94goNq0wz6dtwd9hlSsIzElu12DAHTf1u8hujkNJ8n%2BCm4%2FxEBVLK6E8N7kAV6yNPPPK7lmh0kEuuSi37LarrSCJXwYLGj6RJykuHLT95iBhTjIUgCsVCYk%2BIGqafH%2FmI7krV%2FkB00qPG9RbnMGqHPkjC%2FcafQUY%2BCHWwd13%2BEtVIGsi7ulObQPSO5WbYsYEOobxoyudorAtOwQUjsjL%2F%2F5GxtNSKvaXoV8g8oXJp6MsAqzFopPQkA1UKiV77vBMHU9WWmjP3v3aBoaT0Q5py%2Faj7820Sa9l2GVK9qb7wvssDOq6qFw63Z43gDmML28xMgGOqUBev6l7HMdus2pkCOVmHEWGMJVqnY795IvDcnwGd0JS0ILfAsoiJDDERXowzhYN4Dcc8d%2BTNhZYzlFD0TM2dDsY2rHJi4JrIjJ45fhY1%2BArS0A2wcrIchQ0I1NWSZhGFJPkR4gpQdlhLIiXDjRuGnmsc1B1sqG%2BOc4ck4SfDCHeXvjkH%2FkWepl%2BTUmfHaLDnAkigdyvb6urSng0uZVsFnmOy7sQioT&X-Amz-Signature=19d62b1f98312b080afc473397c554d714f680cc88c5eddb45e77f4faa095ba3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

