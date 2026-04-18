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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S66QGGGO%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCZRSKzPA%2BefZuZkmP4azj3qs%2Fd4AuTowA37Nm0j3QzTQIgNp0AddAEjGnUgR3LawMnSEvksTfhj10cHHlLU63kR2kqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhXk5gb0y7vohWshyrcA9PcXHqSS1FkgQ0FeN%2FPdykuvvemIHAgN4BgF5GbiBGAq6Jp%2FLKG59ekUXYpGIKkMuHyN0md6oGGd9GyeqfN13K6rMchYECTy2uONeHNCRrEay%2B0PeOD2VU%2FumWSO0GvG73EPWpAvE6XbhqhPSi0jT3lbmokb4NgzYopJ%2B8qoNib9wZ7LpsWSnP20uPYWMKjUEhtHMuf207gElJ3nLrRoFy6s%2B5bwVA6g3Qi5IUtqcvtGdj%2BhpinUEOLiSPwrYPwhG3VgzcvWT7YQgBxPVhyOlim%2Btcr%2F%2F%2FaCznEsJkFajPmmM%2FU4E7Z4yNGiwkDJKqBS%2BIseD4ifD2dUdYjTYz9qEI44m5OcHwdnnPcyJpgiQKIqWwBjfvGqCod7xAXTffL5AOa65iSGaecrkHzDsRnAycdND1suMz4J%2BaMX6dHsXcsPxsZ0QTgSo6PCAZrhSQ%2BeRE%2FewK1fSLDT1eEB66fpEQYPsrFu7xCSudc7vMbS%2BYOuOjA%2Bauo1FECynLpktMuCuJWhRluFUUIX0Q5Y697a9zeO4rC4dnUzLtjvNaUqd3CWAzS7v4yEDEVULl45nNRvcfNiASCxhvh3TsI%2FBslABT5Ou74goLWc2QZTvOpqvI2WIY72cyX6K3mgQgYMJKvi88GOqUBibz%2FUNdcaYoDk5j1rlsO6ZRm5fIFkL%2F0vJM4wjia0%2FonMmHnEMpuCPE00rAmFoSsVXzwd2C2Qat9ELth3njxqi9%2FxWdHyYShgZuccXcORGXPYuZjGptyRDsVUN4uuaX1qBtQ8ZBOWBFyVnWZr62qHNel5p88tZXfFZ9Rhr%2B3CCTuyrOx5NgkfILbJeH4M8CO2wNMczX9%2FHinRqXlhljXSipBshwq&X-Amz-Signature=25b167a9c57f22efb5c2a7136fc14607df728801dc125c7b67a0e6d0088109c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S66QGGGO%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCZRSKzPA%2BefZuZkmP4azj3qs%2Fd4AuTowA37Nm0j3QzTQIgNp0AddAEjGnUgR3LawMnSEvksTfhj10cHHlLU63kR2kqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhXk5gb0y7vohWshyrcA9PcXHqSS1FkgQ0FeN%2FPdykuvvemIHAgN4BgF5GbiBGAq6Jp%2FLKG59ekUXYpGIKkMuHyN0md6oGGd9GyeqfN13K6rMchYECTy2uONeHNCRrEay%2B0PeOD2VU%2FumWSO0GvG73EPWpAvE6XbhqhPSi0jT3lbmokb4NgzYopJ%2B8qoNib9wZ7LpsWSnP20uPYWMKjUEhtHMuf207gElJ3nLrRoFy6s%2B5bwVA6g3Qi5IUtqcvtGdj%2BhpinUEOLiSPwrYPwhG3VgzcvWT7YQgBxPVhyOlim%2Btcr%2F%2F%2FaCznEsJkFajPmmM%2FU4E7Z4yNGiwkDJKqBS%2BIseD4ifD2dUdYjTYz9qEI44m5OcHwdnnPcyJpgiQKIqWwBjfvGqCod7xAXTffL5AOa65iSGaecrkHzDsRnAycdND1suMz4J%2BaMX6dHsXcsPxsZ0QTgSo6PCAZrhSQ%2BeRE%2FewK1fSLDT1eEB66fpEQYPsrFu7xCSudc7vMbS%2BYOuOjA%2Bauo1FECynLpktMuCuJWhRluFUUIX0Q5Y697a9zeO4rC4dnUzLtjvNaUqd3CWAzS7v4yEDEVULl45nNRvcfNiASCxhvh3TsI%2FBslABT5Ou74goLWc2QZTvOpqvI2WIY72cyX6K3mgQgYMJKvi88GOqUBibz%2FUNdcaYoDk5j1rlsO6ZRm5fIFkL%2F0vJM4wjia0%2FonMmHnEMpuCPE00rAmFoSsVXzwd2C2Qat9ELth3njxqi9%2FxWdHyYShgZuccXcORGXPYuZjGptyRDsVUN4uuaX1qBtQ8ZBOWBFyVnWZr62qHNel5p88tZXfFZ9Rhr%2B3CCTuyrOx5NgkfILbJeH4M8CO2wNMczX9%2FHinRqXlhljXSipBshwq&X-Amz-Signature=4ad9b219574e8794e4d9cb479a8b0fa14ed96f00fe3caf0835f07d15e901c89c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



