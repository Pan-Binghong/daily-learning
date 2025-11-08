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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6SBP2GO%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAVEBqgtetAlMVN26pnToRSeAa4yyOCNFLP2Eq9H9H1LAiEAqNrzgvbPs%2BwMw1taXRl3BDs9XnQv9CRwCAqp7oCOhC0qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrhJAfOUUhFB5dNzCrcA8bomFYLvU4csxOutCega9TzJ9NXt0ZT5OZcPJghVc9oVjxEw6W1ezXGZlh2uCnZUE2bGLxSfZOyvEdegO5jynTIfALoUwHAIW0u0fZlTH9i4OFr3ECwjBpSey8BPvon69uIYTAqInNCsiNVn5SfzR%2F0%2FHx5kTHWFo1d8VNwr9JYPwoKELXGkxWnE0K5AAhoGUlK63BM2ESV8Tzbf3kDs9rdK5GO5Px9YO4nEl40WdwrxSbeVQZHDzmMT1izKdEdkXqgkCjpaFgu9QIC4ntJYCK0sWYShgaW1tzZdOYqgYq26jFVcoSyI0x2OEzKRISeBShZXcF7n6vlEAnG%2BVvSnDlqCqg%2Bu3fETdIo8ML26cwZIMLdg7iIIATnsCxfQpPvojZRoTphzZlQBgRu5V%2BTeBEOneg96WmpdBXyyO0NiykVZychnr0ZZWPXldHG93C%2BsiD1I8dJeCCFzQxBv3PBT033l73lzHXWa3SRo9srGVbeJc6rtBXqptxD%2F4ycZBB0P1uSDUvMJu6ToSGgMluXxRUBEmOuKtifip5ly750aEX9rw9smeLqv2iE5BlpAKRa22yxqAM9g5GfXcDUjmfRd3YSHIhSA1GWCZU5gOqlSLtOf5wiVDLj3h%2BOTcHpMLXQusgGOqUBAKB6IskusBLa4qMYrgxvz%2FdJMtGMUYWN2RcTfFnzpbLgazPXNK1pcttoGnmn34O7mkgcTLb4BLQIGFCG3%2FQe332A0iWjd8bycWSiZzcB4QOedC88Td2GfR0CtZbJkMHN%2BzV%2FGvVnI4mQBGpPC2mLM56wsiiO8t%2Bov9HgU2J5xY5IrHdMyGbng0SUcgyYl59Vf50NYVF67H%2FEFyB%2FXgCGo7ylq5Xk&X-Amz-Signature=7e61c049580893749be4f8dfc53efc921822597461080f69a1650ed683352139&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6SBP2GO%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAVEBqgtetAlMVN26pnToRSeAa4yyOCNFLP2Eq9H9H1LAiEAqNrzgvbPs%2BwMw1taXRl3BDs9XnQv9CRwCAqp7oCOhC0qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrhJAfOUUhFB5dNzCrcA8bomFYLvU4csxOutCega9TzJ9NXt0ZT5OZcPJghVc9oVjxEw6W1ezXGZlh2uCnZUE2bGLxSfZOyvEdegO5jynTIfALoUwHAIW0u0fZlTH9i4OFr3ECwjBpSey8BPvon69uIYTAqInNCsiNVn5SfzR%2F0%2FHx5kTHWFo1d8VNwr9JYPwoKELXGkxWnE0K5AAhoGUlK63BM2ESV8Tzbf3kDs9rdK5GO5Px9YO4nEl40WdwrxSbeVQZHDzmMT1izKdEdkXqgkCjpaFgu9QIC4ntJYCK0sWYShgaW1tzZdOYqgYq26jFVcoSyI0x2OEzKRISeBShZXcF7n6vlEAnG%2BVvSnDlqCqg%2Bu3fETdIo8ML26cwZIMLdg7iIIATnsCxfQpPvojZRoTphzZlQBgRu5V%2BTeBEOneg96WmpdBXyyO0NiykVZychnr0ZZWPXldHG93C%2BsiD1I8dJeCCFzQxBv3PBT033l73lzHXWa3SRo9srGVbeJc6rtBXqptxD%2F4ycZBB0P1uSDUvMJu6ToSGgMluXxRUBEmOuKtifip5ly750aEX9rw9smeLqv2iE5BlpAKRa22yxqAM9g5GfXcDUjmfRd3YSHIhSA1GWCZU5gOqlSLtOf5wiVDLj3h%2BOTcHpMLXQusgGOqUBAKB6IskusBLa4qMYrgxvz%2FdJMtGMUYWN2RcTfFnzpbLgazPXNK1pcttoGnmn34O7mkgcTLb4BLQIGFCG3%2FQe332A0iWjd8bycWSiZzcB4QOedC88Td2GfR0CtZbJkMHN%2BzV%2FGvVnI4mQBGpPC2mLM56wsiiO8t%2Bov9HgU2J5xY5IrHdMyGbng0SUcgyYl59Vf50NYVF67H%2FEFyB%2FXgCGo7ylq5Xk&X-Amz-Signature=d80603acbe02de226b9a64fbd08518c2336e033bb23c06b30204f4956c621bc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









