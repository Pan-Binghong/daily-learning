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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MBS3JKJ%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQDg%2FV0CDLtusSFY7cCuXjXVA%2FvC55bkZZ6EV2CmklNBuwIgE%2BdnaMPmKfPh8ahRciBjfm%2Bgx28x4yz7nthdyCLkxXsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDExx8OeuO6OosUzhDyrcA0AJjXotHoUiSEGVSeQ5DfAqmoMfDujKNLamB3Ph%2FU6BpNrC7SIw%2BDnbO01hKFxcFpNcX39qfuYKp06g6uiTecsfq4F8NYZHdYCcAANdi383wjCo2vEILQOt2QdeG5hEvMKncPsw%2Bygvu1oGN9Ao4LgT0COkLEYqZTK0N8573ybdYyBk9PEdtt80jbvUuNvTIvBuqZwZCpZEhsUuiXOOpn8A0qQ%2FFpOzGuYqVcLcIIB%2BAWl%2Bf4NepqAG0ldxtv47LE0Ynbjf8PY0%2B8D8J2MqVCJkNankPEiozfb%2FgEJAYs2r%2Fs0qE9W7DBeQKwQfl%2BzsTew3cmIGMi1JZT47oxK8pTGOYrLpyQoUY7VkkzswS82CW1fqEPdoIcCHHGN2ENxN2NQl7JHQUYkJLdHdmVSvMMsWsZfLgyMvwnw89sS8ELv0Zs1PoSJpDBZsvrA7DBIp55lfrNTmBsj%2BC8d7Hby7ZGgfKrjz31ROA6wDI%2B4Se4vhD%2FZgvBB3KqhXz3R7HvS1pT65Q6sUwX%2BAbR4%2FDy0GoJCbTFjXjICTWGjiNB9zYR%2FsO8pPDCOm%2FgHulHus8YwmnZmCxsqrW2VOGekk4riqR1x7IYVosaLoyh%2FxAUN0uXohopD3YDMAKNBaRo%2BYMNTcrckGOqUB9dt41AK8U7VkO53G%2ByoAco4GfnpmV5NEISY2Qv3RWXc5cNgLbaF5N%2Fi64LYNmTr2cBIz%2Fn2jC672wzwaEVNqmaI7MQ0ok07LvPEetPsE4jG9H%2B%2FSdlqFbdGk9LIAJEINgIVr8587EuKBChM6SXnUwJpnRp%2Bs0OmxZTKHy0tpLxa3isGVQFHZK1P8YSwffBkaPFSPEsp5Wti1cu0SuvqZxC9Hjx8T&X-Amz-Signature=bb3166870da4abf1b40d5618e5710b364657471b5729bf90144f812f20460366&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MBS3JKJ%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQDg%2FV0CDLtusSFY7cCuXjXVA%2FvC55bkZZ6EV2CmklNBuwIgE%2BdnaMPmKfPh8ahRciBjfm%2Bgx28x4yz7nthdyCLkxXsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDExx8OeuO6OosUzhDyrcA0AJjXotHoUiSEGVSeQ5DfAqmoMfDujKNLamB3Ph%2FU6BpNrC7SIw%2BDnbO01hKFxcFpNcX39qfuYKp06g6uiTecsfq4F8NYZHdYCcAANdi383wjCo2vEILQOt2QdeG5hEvMKncPsw%2Bygvu1oGN9Ao4LgT0COkLEYqZTK0N8573ybdYyBk9PEdtt80jbvUuNvTIvBuqZwZCpZEhsUuiXOOpn8A0qQ%2FFpOzGuYqVcLcIIB%2BAWl%2Bf4NepqAG0ldxtv47LE0Ynbjf8PY0%2B8D8J2MqVCJkNankPEiozfb%2FgEJAYs2r%2Fs0qE9W7DBeQKwQfl%2BzsTew3cmIGMi1JZT47oxK8pTGOYrLpyQoUY7VkkzswS82CW1fqEPdoIcCHHGN2ENxN2NQl7JHQUYkJLdHdmVSvMMsWsZfLgyMvwnw89sS8ELv0Zs1PoSJpDBZsvrA7DBIp55lfrNTmBsj%2BC8d7Hby7ZGgfKrjz31ROA6wDI%2B4Se4vhD%2FZgvBB3KqhXz3R7HvS1pT65Q6sUwX%2BAbR4%2FDy0GoJCbTFjXjICTWGjiNB9zYR%2FsO8pPDCOm%2FgHulHus8YwmnZmCxsqrW2VOGekk4riqR1x7IYVosaLoyh%2FxAUN0uXohopD3YDMAKNBaRo%2BYMNTcrckGOqUB9dt41AK8U7VkO53G%2ByoAco4GfnpmV5NEISY2Qv3RWXc5cNgLbaF5N%2Fi64LYNmTr2cBIz%2Fn2jC672wzwaEVNqmaI7MQ0ok07LvPEetPsE4jG9H%2B%2FSdlqFbdGk9LIAJEINgIVr8587EuKBChM6SXnUwJpnRp%2Bs0OmxZTKHy0tpLxa3isGVQFHZK1P8YSwffBkaPFSPEsp5Wti1cu0SuvqZxC9Hjx8T&X-Amz-Signature=5c0ab8dbe1067d37fb9ec35f4a9a58ffa2f747a9e97ce75930076b2d49baad59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



