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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IOG5LWK%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFtiaQGs83xP3tkVduBmJWqySU1sbvfXu5qwnMaTzC8AiEAm2xaYV15d2wCsSgqs7Avg86Ry%2FVXIOnyUFGJKiF3bNkq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDAS7euPNWcF%2FObolnCrcA66seK1vY70l0805GnsXnw64lwNaIEfR%2FFm%2F6%2FQMPEaEIfynzCiTGnZEGzPbdjQovLw5PboiDAWNeouY01TibFvALT1d4UNySRl6dvqaEh3Cvz8d466Gw1QVe8kwMgo7KkToSVC%2BpsX4Iyk93qJg2xxPGRSq%2FuW1P%2Fzo%2F7LjICTV%2BAeiVplvVeLi1%2BhykOGeg5ALfAV5kWeuFiePctkrAgOh%2BpSZKobHPHzP8lRFDmbPBuxplMtPyVywGQIbwTmWCkgz7qiQaREoRFcNSp9e6tMN5cD4gSh3nev6bwpxGqqCOriVyY%2FA%2BhTSpbkPAhLE8w6dsIKxy9Ee6dsuKjxRp0Yn1%2Frl%2F%2FQT%2F8YUTEtRoz8mTEWER6nZBJgqbh5C9yR2S9hIqmwZfCGR6ZiMHVP8s7EqEnQYkCYsEKu48PfxIey4NPpDXFoKI9gT%2FT8xSz1QrQUjHzlqpoCbI%2BTyq7rTb7ANpJn8SWHuC8aUiKK37VWwjHTqcUz1qM66gdMs06yZyeWoEMnIOzogvdgpfRgI5%2B5aohK2Gf%2F6uHUQFi3XieWVy3TWqD6PluLt7pZtSmVzr2aDiaZCs8AA3DTXPswurR90kxObhA6AJsz%2Fi1m6FvnuHU24AotEjjP4W4XvMJuwmckGOqUB73k2A3igRWOTEP%2F%2FSS7haemcdBJH%2FcGqtih5c94Nag%2Bt1nsuf763eiPfW8m3656roHY4kU1PbY6fheXRCoKJOEkBsWH3uI5AfjLzsq0qW%2Ftn7R%2FTQ%2FA%2BQC8Pibh%2FettDNm3IU6OEobpXUM0j7cXCB9n8iE0ZWDgON4JwFG985ZOMUyRu%2FhgOtxM6nLfKXZedL0mSG0gMjnmbqYPKKQs%2Fj8fYiLmz&X-Amz-Signature=08ad28b930821a0157a9f4da9dd541467689ac6eca9b896d173fa6b3f5cf6bf8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IOG5LWK%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFtiaQGs83xP3tkVduBmJWqySU1sbvfXu5qwnMaTzC8AiEAm2xaYV15d2wCsSgqs7Avg86Ry%2FVXIOnyUFGJKiF3bNkq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDAS7euPNWcF%2FObolnCrcA66seK1vY70l0805GnsXnw64lwNaIEfR%2FFm%2F6%2FQMPEaEIfynzCiTGnZEGzPbdjQovLw5PboiDAWNeouY01TibFvALT1d4UNySRl6dvqaEh3Cvz8d466Gw1QVe8kwMgo7KkToSVC%2BpsX4Iyk93qJg2xxPGRSq%2FuW1P%2Fzo%2F7LjICTV%2BAeiVplvVeLi1%2BhykOGeg5ALfAV5kWeuFiePctkrAgOh%2BpSZKobHPHzP8lRFDmbPBuxplMtPyVywGQIbwTmWCkgz7qiQaREoRFcNSp9e6tMN5cD4gSh3nev6bwpxGqqCOriVyY%2FA%2BhTSpbkPAhLE8w6dsIKxy9Ee6dsuKjxRp0Yn1%2Frl%2F%2FQT%2F8YUTEtRoz8mTEWER6nZBJgqbh5C9yR2S9hIqmwZfCGR6ZiMHVP8s7EqEnQYkCYsEKu48PfxIey4NPpDXFoKI9gT%2FT8xSz1QrQUjHzlqpoCbI%2BTyq7rTb7ANpJn8SWHuC8aUiKK37VWwjHTqcUz1qM66gdMs06yZyeWoEMnIOzogvdgpfRgI5%2B5aohK2Gf%2F6uHUQFi3XieWVy3TWqD6PluLt7pZtSmVzr2aDiaZCs8AA3DTXPswurR90kxObhA6AJsz%2Fi1m6FvnuHU24AotEjjP4W4XvMJuwmckGOqUB73k2A3igRWOTEP%2F%2FSS7haemcdBJH%2FcGqtih5c94Nag%2Bt1nsuf763eiPfW8m3656roHY4kU1PbY6fheXRCoKJOEkBsWH3uI5AfjLzsq0qW%2Ftn7R%2FTQ%2FA%2BQC8Pibh%2FettDNm3IU6OEobpXUM0j7cXCB9n8iE0ZWDgON4JwFG985ZOMUyRu%2FhgOtxM6nLfKXZedL0mSG0gMjnmbqYPKKQs%2Fj8fYiLmz&X-Amz-Signature=2b3ec3e2e4feab8fc7d998cf5ed349263fb636affdb437bbc71e8c4c77e19cee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



