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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YL5J5ZKZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCuQ30z%2FWGlBBop0GdAcVAciKEJxwzNXl%2FHDX7bKHvfnQIgKeC0w1AzOz2msGKgp0cExzFIjkvsxfTbo48W%2FEMjR6wqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJv81cgvMr1jLGFRjyrcA05kzKs14vEfWPmFn6FokLfuezrlJ6lHxx%2BbAA33D1U8GJX9wp8PBEPekMPsaZoXi7a3QKlh5jC9qK8%2BaQleBoTUz%2BhsZG0wgjxuP%2B2OW%2BmGU4czK0uGZPyRjV7G9LXWreCkrlYEi74JKaEfINkPvVdzuNRwWtyq1rAs50IwwJ1%2B3T8ikO5%2B3UCAamUup%2FcrL5kU8XMkYSANgPkIVGlqdxwQ7WkecV%2B5uy3yXXinESEvZ6okCFR8M6yK42uMhI47IefgsC6CbCeET%2BogEPpJuV3QvCqZ7DPcga%2FDkYGIt3VmpxWLyyH%2Bf2rdWLj5iAlBd94goNq0wz6dtwd9hlSsIzElu12DAHTf1u8hujkNJ8n%2BCm4%2FxEBVLK6E8N7kAV6yNPPPK7lmh0kEuuSi37LarrSCJXwYLGj6RJykuHLT95iBhTjIUgCsVCYk%2BIGqafH%2FmI7krV%2FkB00qPG9RbnMGqHPkjC%2FcafQUY%2BCHWwd13%2BEtVIGsi7ulObQPSO5WbYsYEOobxoyudorAtOwQUjsjL%2F%2F5GxtNSKvaXoV8g8oXJp6MsAqzFopPQkA1UKiV77vBMHU9WWmjP3v3aBoaT0Q5py%2Faj7820Sa9l2GVK9qb7wvssDOq6qFw63Z43gDmML28xMgGOqUBev6l7HMdus2pkCOVmHEWGMJVqnY795IvDcnwGd0JS0ILfAsoiJDDERXowzhYN4Dcc8d%2BTNhZYzlFD0TM2dDsY2rHJi4JrIjJ45fhY1%2BArS0A2wcrIchQ0I1NWSZhGFJPkR4gpQdlhLIiXDjRuGnmsc1B1sqG%2BOc4ck4SfDCHeXvjkH%2FkWepl%2BTUmfHaLDnAkigdyvb6urSng0uZVsFnmOy7sQioT&X-Amz-Signature=e5cf30761f14be7d762a18f51bac3888722336b73994691c173f6efa8d9a6e06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

