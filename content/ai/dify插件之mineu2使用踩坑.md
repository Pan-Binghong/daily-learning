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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQC32RAR%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYJ6wGDBjG0QaVgr00cARghXj%2FBSbOwg8blX8lCxlW%2FwIhAIXA41Lbk3t4u2U3EfOAjKfdAuM9o%2FAXu0Mye2qnx5qoKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZMPwqy1EgsXpYcg0q3APPK6CUlG5yaebJ3QFvnJq1yDInOohKLvy0v5lckyF%2Fd8rJ9c0%2FogZTuc4T5idqtCSxwm1uVEwDNNt15lDNUFv80XJt2gzq7am2lyuCgAKlwA58y000HUxWiSefWVOHJelU2%2B8FCtzIUtHWBoqV9uEU19pg2Dqy2BHTIe%2FTwCMuqOOiHdjAtaoAu64C357%2BMS9t4bhXk%2FoDn3oqqDPDTxZ70Jlc7Le%2Bv7U%2FIzNI1ukkGvMHcZdypVwwNZlwy%2FogohiKi5gYxtgR96G%2BRsFM6qacRynrozYVWIEHDQo2Uci2JoAmassNJ0WduvPxrYddBf4f4zHgWDF9VdSpnDmhFIXm0FKnb1terJlwXI2e5bhCZaZbEYHKHu%2BQqta1ivqdATJ%2FNkZECVp9GVwVi9Gk5mN3EaA7t2%2BXPO466Ex2T2r9fPLOFk%2BTM%2Bqh6uEEkSbjw84LkZ5mRbY%2FVIW4gDrx76hb5Q2Z1hvwe4aYIh4cu1%2FeqjSGISjgs%2BFLPxe1GynFA5sFooE%2BFAEA%2FEROSiQ%2FGwO%2B82nXuRfLWuuY598PqsxPUn5s%2Bydh8VIaEtAo%2FtN2ET2LU5aCR3Mmzh6I8aByDx%2F9yvJtByk221dj9xOz3ey1Wy8nwEW%2BOa3%2BuJ%2B04zCuvOTMBjqkAX21LrMTUGziNQJklDHuOl0MWH%2FJGVfP56uTc8V6hC4S4TLnLpHqjwYBUOuXW%2FMoi2Mn2CcsjF89KhZ8jPlTiRIgZq0FSzEc365vSO3FIJVWYrNl6827v93n9w7XH%2B89yNxUZ5pASdyxp6hh7yw86iZITflGVEObasQCH1AUGmUYeamPUucWsuLIlqyJi8r%2BbPXxWyY9enM4B2oVw4zsHC%2FSavkJ&X-Amz-Signature=705360ff17769fbb9e7ce2629b10400204bd432a08bc43bf04ec252df10bc438&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQC32RAR%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYJ6wGDBjG0QaVgr00cARghXj%2FBSbOwg8blX8lCxlW%2FwIhAIXA41Lbk3t4u2U3EfOAjKfdAuM9o%2FAXu0Mye2qnx5qoKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZMPwqy1EgsXpYcg0q3APPK6CUlG5yaebJ3QFvnJq1yDInOohKLvy0v5lckyF%2Fd8rJ9c0%2FogZTuc4T5idqtCSxwm1uVEwDNNt15lDNUFv80XJt2gzq7am2lyuCgAKlwA58y000HUxWiSefWVOHJelU2%2B8FCtzIUtHWBoqV9uEU19pg2Dqy2BHTIe%2FTwCMuqOOiHdjAtaoAu64C357%2BMS9t4bhXk%2FoDn3oqqDPDTxZ70Jlc7Le%2Bv7U%2FIzNI1ukkGvMHcZdypVwwNZlwy%2FogohiKi5gYxtgR96G%2BRsFM6qacRynrozYVWIEHDQo2Uci2JoAmassNJ0WduvPxrYddBf4f4zHgWDF9VdSpnDmhFIXm0FKnb1terJlwXI2e5bhCZaZbEYHKHu%2BQqta1ivqdATJ%2FNkZECVp9GVwVi9Gk5mN3EaA7t2%2BXPO466Ex2T2r9fPLOFk%2BTM%2Bqh6uEEkSbjw84LkZ5mRbY%2FVIW4gDrx76hb5Q2Z1hvwe4aYIh4cu1%2FeqjSGISjgs%2BFLPxe1GynFA5sFooE%2BFAEA%2FEROSiQ%2FGwO%2B82nXuRfLWuuY598PqsxPUn5s%2Bydh8VIaEtAo%2FtN2ET2LU5aCR3Mmzh6I8aByDx%2F9yvJtByk221dj9xOz3ey1Wy8nwEW%2BOa3%2BuJ%2B04zCuvOTMBjqkAX21LrMTUGziNQJklDHuOl0MWH%2FJGVfP56uTc8V6hC4S4TLnLpHqjwYBUOuXW%2FMoi2Mn2CcsjF89KhZ8jPlTiRIgZq0FSzEc365vSO3FIJVWYrNl6827v93n9w7XH%2B89yNxUZ5pASdyxp6hh7yw86iZITflGVEObasQCH1AUGmUYeamPUucWsuLIlqyJi8r%2BbPXxWyY9enM4B2oVw4zsHC%2FSavkJ&X-Amz-Signature=2d739f6c3179b72064b561d8a13ff6473173905a18dd21ce31e81ed9384b6a99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



