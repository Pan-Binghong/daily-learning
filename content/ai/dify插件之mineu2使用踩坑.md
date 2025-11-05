---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
标签:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632Q56EEE%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNmLv0i66WouR2szAKrwzeEpSYoA8aAASrQYGPUML5wQIhAL4ldASndBFSqjF9f9FZLdVoIirsNqhEAU95CJXJZhsDKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzK6plRN7Vqi8VgNu0q3AOpK6LQm8vlBMgCekmP5CqOjCpTBnIZIT6MaIOv5FLQyIWBibkKtK%2Bp2jPmKDRYKTVIeZLP%2BnOiLsZQnQEv9ilgTanvOEKN5g%2BpnCnvVPig7GJYJktm6RxoYPP7hu4FrO%2BSuqOqWjwqYuk9XyaCP4B4ZwsE8PvsPLMwXZh25M9oM0GP8QVenihClkqO%2BYC0Uw7pPz%2FXK1jnRD4cseo104A%2F1CGAriO7A64fxW9s87v%2BNZF9E7%2Bo5W0LuXWPdu7ML2ZUhwgDvAq2wmqpZDwAJm3bhSfL3YhXArCGRJ1ID67pZYnNvP8k6xnIzIv8FiQpv4bxAMK1INBNcyG0HaXcOwinPugKYRHPLAw8TxHeBSjXECHayd6BT5xXlpxRAHzgRXCHhNNw%2Fj4nmP1OMdAxmhK%2Fl27u9AqWSOTjyVcZNAN0p%2F0ESJy99OrdexwdaZqIcDtdihi1466nbNnXFRLH00IV%2BUah8I5TMCdSasEtKqo%2F4CMOENhOxLtFdVZ31Wn9tcmTfDL3XE4U6YQiQ%2BKEE00fmN%2BX0h%2BJKgKQYZFc0ruECluRUz7tGbTRZ22R8GsbrpKN8r2Cq4CCLE0zmW0aHHwESvy2lJYsv7qkcH7nBoQ4wb%2B5cwuFlaPja5HBLTCro6zIBjqkATLu35H7ORcopGogdgCh1A7nttYIqd0kvjubTxbWFFpiRfFvbYgG%2BvA3uD4UKA%2B6oEiNRAre4OIo2K%2B40QCy7bWd43yT39f14gyUog%2F1prBCD0Hm2AK06z%2B7rcI8t17zUFm204vZvvrH3gs%2Bj0c74lZQBubnzM%2Bd8KAsyo9p8132VOTvtgENz6ag4QsH67vrGchBmfbohcvQGVoLyQwsAw%2BrU2CG&X-Amz-Signature=fa83dab614de26b4729a48b0fc9337da1f7050ad391eec7f6690d4f47b4288ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632Q56EEE%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNmLv0i66WouR2szAKrwzeEpSYoA8aAASrQYGPUML5wQIhAL4ldASndBFSqjF9f9FZLdVoIirsNqhEAU95CJXJZhsDKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzK6plRN7Vqi8VgNu0q3AOpK6LQm8vlBMgCekmP5CqOjCpTBnIZIT6MaIOv5FLQyIWBibkKtK%2Bp2jPmKDRYKTVIeZLP%2BnOiLsZQnQEv9ilgTanvOEKN5g%2BpnCnvVPig7GJYJktm6RxoYPP7hu4FrO%2BSuqOqWjwqYuk9XyaCP4B4ZwsE8PvsPLMwXZh25M9oM0GP8QVenihClkqO%2BYC0Uw7pPz%2FXK1jnRD4cseo104A%2F1CGAriO7A64fxW9s87v%2BNZF9E7%2Bo5W0LuXWPdu7ML2ZUhwgDvAq2wmqpZDwAJm3bhSfL3YhXArCGRJ1ID67pZYnNvP8k6xnIzIv8FiQpv4bxAMK1INBNcyG0HaXcOwinPugKYRHPLAw8TxHeBSjXECHayd6BT5xXlpxRAHzgRXCHhNNw%2Fj4nmP1OMdAxmhK%2Fl27u9AqWSOTjyVcZNAN0p%2F0ESJy99OrdexwdaZqIcDtdihi1466nbNnXFRLH00IV%2BUah8I5TMCdSasEtKqo%2F4CMOENhOxLtFdVZ31Wn9tcmTfDL3XE4U6YQiQ%2BKEE00fmN%2BX0h%2BJKgKQYZFc0ruECluRUz7tGbTRZ22R8GsbrpKN8r2Cq4CCLE0zmW0aHHwESvy2lJYsv7qkcH7nBoQ4wb%2B5cwuFlaPja5HBLTCro6zIBjqkATLu35H7ORcopGogdgCh1A7nttYIqd0kvjubTxbWFFpiRfFvbYgG%2BvA3uD4UKA%2B6oEiNRAre4OIo2K%2B40QCy7bWd43yT39f14gyUog%2F1prBCD0Hm2AK06z%2B7rcI8t17zUFm204vZvvrH3gs%2Bj0c74lZQBubnzM%2Bd8KAsyo9p8132VOTvtgENz6ag4QsH67vrGchBmfbohcvQGVoLyQwsAw%2BrU2CG&X-Amz-Signature=ff17745dfad6ecde3c47ca8b8dc34075511e3b17d7642fbe048ccf0cb0361d9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



