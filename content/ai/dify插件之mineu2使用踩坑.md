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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCLLXXYO%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEPJQIcGJXHeYvuha3ifIpEn1PERPd8mxnlGNncfQ6BoAiEAnJ6bVbVPUKAZOlXuuQH0LeQfEDe7UvHOHyWA6AmXYjQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIfo8p4RhluhnHF4KSrcA4X7uX8jSvJeI8Wg3YwAtoh83nllGFctJp%2Bqi22Mbf6T9DljIn9UDBqW0H0n1NJnIHlCN%2B0pq0GiwpJX8%2FszrmXtqtwF%2F%2Ffip8nKo%2FZvDQzZzD10k0JPMCYQzOnF50uUUAMB0Ekm4pKswhBHbBoCoYzY643mfwyY%2BkGO6x8lfCRuNvFSOsfriz1GqBhwQ8N%2FKZkwOjg4sC7SyB05vX96kt8y1LrGEwjEa3sx8gSpiodQAiys0AcwHCwjEFCd6BlTEkaG0wlEtosZHoZeeGsUD%2BF39f5YHFXLz%2BKpb5Rkwq%2BK7SxaTu46b2OaCvHjLs6Z5iujYRd5DcHwQCK10jRe1C2a5c3F69uyPhNKEXdcUzIaTksQMLLwnR0fOr02NzNyHCSr7BQnaVTztEW6%2FCZ6m6aMa79eoj3yHUPGrswLifhvJOqIVgUmFMgrBbmPV74VpmViyb24aUET42Il0wvwimkjTZXwrMuMd7axgZlSwzVd8YMKf1gOSlF2hLURlg2oUplE6j47b3lfKyCBnjAZM17MCpGkPuuaXRbhGOr9Ov%2BNQH0BxZnL8GGfVIjzJY%2Bag78HI%2BsAit76QyRw9Ps84BwxP%2Fi7V6e%2BOfEpk9Y0E4rFnE6biQnAvwTIVN5BMJD90skGOqUBI41%2FeVxRgCYXaWoyImlPV9gTImDmWS%2FAuoZSpH2eDENQiEjW7bh4rjzq0RyMlWAG9MQ1KlIGTNX%2FaDk8krG8NsCotGVXYhYPEfZL321mK283aARGMLixsiugeTOufdOCjABew7SYrrcRh2VNwUDwTifycCe95POFdsRi4x42f1U23No1F6oh8jT5xEBA77yCh8wtTGOQ0iO2UGircdQtSHpXTV7x&X-Amz-Signature=8fc711046049548add17e0e6edfd54152835aec04df36c3881b0a3adabce9680&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCLLXXYO%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEPJQIcGJXHeYvuha3ifIpEn1PERPd8mxnlGNncfQ6BoAiEAnJ6bVbVPUKAZOlXuuQH0LeQfEDe7UvHOHyWA6AmXYjQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIfo8p4RhluhnHF4KSrcA4X7uX8jSvJeI8Wg3YwAtoh83nllGFctJp%2Bqi22Mbf6T9DljIn9UDBqW0H0n1NJnIHlCN%2B0pq0GiwpJX8%2FszrmXtqtwF%2F%2Ffip8nKo%2FZvDQzZzD10k0JPMCYQzOnF50uUUAMB0Ekm4pKswhBHbBoCoYzY643mfwyY%2BkGO6x8lfCRuNvFSOsfriz1GqBhwQ8N%2FKZkwOjg4sC7SyB05vX96kt8y1LrGEwjEa3sx8gSpiodQAiys0AcwHCwjEFCd6BlTEkaG0wlEtosZHoZeeGsUD%2BF39f5YHFXLz%2BKpb5Rkwq%2BK7SxaTu46b2OaCvHjLs6Z5iujYRd5DcHwQCK10jRe1C2a5c3F69uyPhNKEXdcUzIaTksQMLLwnR0fOr02NzNyHCSr7BQnaVTztEW6%2FCZ6m6aMa79eoj3yHUPGrswLifhvJOqIVgUmFMgrBbmPV74VpmViyb24aUET42Il0wvwimkjTZXwrMuMd7axgZlSwzVd8YMKf1gOSlF2hLURlg2oUplE6j47b3lfKyCBnjAZM17MCpGkPuuaXRbhGOr9Ov%2BNQH0BxZnL8GGfVIjzJY%2Bag78HI%2BsAit76QyRw9Ps84BwxP%2Fi7V6e%2BOfEpk9Y0E4rFnE6biQnAvwTIVN5BMJD90skGOqUBI41%2FeVxRgCYXaWoyImlPV9gTImDmWS%2FAuoZSpH2eDENQiEjW7bh4rjzq0RyMlWAG9MQ1KlIGTNX%2FaDk8krG8NsCotGVXYhYPEfZL321mK283aARGMLixsiugeTOufdOCjABew7SYrrcRh2VNwUDwTifycCe95POFdsRi4x42f1U23No1F6oh8jT5xEBA77yCh8wtTGOQ0iO2UGircdQtSHpXTV7x&X-Amz-Signature=058c941b90ee97e596dc7d3e8c9dc56426912956f7ef36e187035fb891f2db8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



