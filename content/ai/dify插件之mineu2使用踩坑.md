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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X62SPWSX%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDApK395EWC%2FxCEDqIxExHrNmLWjoOnOwz04mpp8eif7AIhAP%2FmU04gN3p5%2FyWoV1hOmDbQVClNsklHAfsaWz65rPIuKv8DCFMQABoMNjM3NDIzMTgzODA1Igyh7BhrHg4wg%2FLzfrcq3AMhaJhwrsMTSp4zNuwY6t6mGvHScOPrOOyaZO6f8gms8pWQEA0BQJybaKb%2BtCCz%2Fsr7xNR%2Bey%2FTDblXM12NeR7NJ4YphMTs4Yv7%2FGPmX06fR4xr0j4K4N%2F%2BqQ5wUAcaTka2S6digjL%2Fx1FzFtOtss65ioO5ewH%2FPR5G2ufq1FkAapxxAlB%2FplLFhtepJxhMSGHzQ89jpyIy46P3Isc10VtM0GU2Ub4PkvgVF%2FJ5QN1WAlIZpRRj7%2BdGqW3ovNjJLTRGvCd6pfySlWWzQFwyL%2B8B3Kj1wQVxqlAkbwxrWold7wFe54ddidppuWlpausqGiIkWXJZox52b7F%2ByLdUsocKs4VcbbTrY1g8%2FbRRqsdI0mqEwl8TXS5q4wJrZ%2B0W12gAOJvPVSvYraMmnrcfJMw3pCea1dZctfqP6ndjNINVwkg1IcwwJIdhuHsMi%2Fkri3Wh%2FZDxP4o2S26wL7YAhXtHBdJYFL5JZa24vFqdlhiqtlenOIw88oxcMrqgXI%2BeLltPxAUAaMHXWWsWPJrXngBmqsIfcP5QJXhgLOMcDyNR3GFbuihBf80P5IvJpRufvFIVJKgf7OdC2JgxB8jeUN%2BKsV1gAx1girKvv0h4p4m5HXlsdgh7YyNM%2Bl9StTDf5fHKBjqkAUY%2FXGbw5CRFcZHlmjxHoxX%2B4pPMOeCedIFcP6kslJi1khIZVQ5fwSJZRA6wDZjl2txrdlpyxbs15FiMrJFXPfzR8IW9uGCBVUi3sa05Az6E3Auo%2BWUXIQi0X1%2FjR6EXmPq98jIFwANNrFwEsxuqKntomAUi1dblqem0lgfKN2ocm71qDUMYBm1qWiVE%2FhyB733h3174wjKBa18U93WLZ2gIuZJa&X-Amz-Signature=e95242ca38b6f41c2cecf3e534c67093f6e93ddded43852f9a71455345f392c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X62SPWSX%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDApK395EWC%2FxCEDqIxExHrNmLWjoOnOwz04mpp8eif7AIhAP%2FmU04gN3p5%2FyWoV1hOmDbQVClNsklHAfsaWz65rPIuKv8DCFMQABoMNjM3NDIzMTgzODA1Igyh7BhrHg4wg%2FLzfrcq3AMhaJhwrsMTSp4zNuwY6t6mGvHScOPrOOyaZO6f8gms8pWQEA0BQJybaKb%2BtCCz%2Fsr7xNR%2Bey%2FTDblXM12NeR7NJ4YphMTs4Yv7%2FGPmX06fR4xr0j4K4N%2F%2BqQ5wUAcaTka2S6digjL%2Fx1FzFtOtss65ioO5ewH%2FPR5G2ufq1FkAapxxAlB%2FplLFhtepJxhMSGHzQ89jpyIy46P3Isc10VtM0GU2Ub4PkvgVF%2FJ5QN1WAlIZpRRj7%2BdGqW3ovNjJLTRGvCd6pfySlWWzQFwyL%2B8B3Kj1wQVxqlAkbwxrWold7wFe54ddidppuWlpausqGiIkWXJZox52b7F%2ByLdUsocKs4VcbbTrY1g8%2FbRRqsdI0mqEwl8TXS5q4wJrZ%2B0W12gAOJvPVSvYraMmnrcfJMw3pCea1dZctfqP6ndjNINVwkg1IcwwJIdhuHsMi%2Fkri3Wh%2FZDxP4o2S26wL7YAhXtHBdJYFL5JZa24vFqdlhiqtlenOIw88oxcMrqgXI%2BeLltPxAUAaMHXWWsWPJrXngBmqsIfcP5QJXhgLOMcDyNR3GFbuihBf80P5IvJpRufvFIVJKgf7OdC2JgxB8jeUN%2BKsV1gAx1girKvv0h4p4m5HXlsdgh7YyNM%2Bl9StTDf5fHKBjqkAUY%2FXGbw5CRFcZHlmjxHoxX%2B4pPMOeCedIFcP6kslJi1khIZVQ5fwSJZRA6wDZjl2txrdlpyxbs15FiMrJFXPfzR8IW9uGCBVUi3sa05Az6E3Auo%2BWUXIQi0X1%2FjR6EXmPq98jIFwANNrFwEsxuqKntomAUi1dblqem0lgfKN2ocm71qDUMYBm1qWiVE%2FhyB733h3174wjKBa18U93WLZ2gIuZJa&X-Amz-Signature=686e81d4a46f8f13bc3c1c4756cfe4954e029411e9ef396dd26af399e4739008&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



