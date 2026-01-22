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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WY7MDOGF%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIFxmNqy8F35HhWedzUOaE6A%2BhOR5hl%2Fwq3usOxczMJ1VAiEAxhXmwv7i8EaRvU2t%2FrGK6sjAggT%2F5wst%2BVguxgt4xEkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF5moQTxPYysnnlIZyrcA%2BePEN0ZkOG3TL1YGxv2HReBd4LxAPnLY8Z2A2WXqr2%2BTr1dFvacTQz%2BsTt2CTTs4Qhx9s1wMS9%2BtDAtoVeijISSMqqMmyWHata12SAytj06uKJrbqPBzDEtW%2FCYx%2Fv92%2BXo7dTn88v2R%2FFxeNr%2BNo%2F6HIjen9UyqwRsk8KeuC%2Bw5UIJkHw6Po955ELIBDljIslNwtpG1lHNOIui2%2Bgx6ynKTAiEsABMpcGhay%2BsWMF%2FnMgavnwbkb6Fi%2BcHNAjal69Qk8il1uI8QD6GxePWdurFiCHHKofeew1bekrAWH4M%2B6q3szSMUeFCW0Lp6wHOhkH71dogB1sDyERNyrmyT9cUcrR7nQbahimnRM2eogrL%2BhepSAg1stImkfzex5yM8%2FXT44XSUP6UI9HDa2j0eJRfubqtb53hbPdM%2BVhLSjbjKelBFwxLKyLA%2BF0%2Fl22gMGqJAk%2FoYwRzvfX1RBmz0eUbvFipw10yDDwqJpP6drSl8t8dpQtcfrFX1O6LxQnPquT0DlCxmpEhpOLjZLgMWYTXmoXYccYb2MyqtVwoqjbyIDum%2BTf%2BaiQ4vNdHv%2BEVLF5ceb6uGcwAnysodIJ31nOYPNjOQo2CHGOIt7nLVwJOd%2Fcf3JkKVlk1jAwBMP3XxcsGOqUBNGDYGuWb4Hk22hbigO09ciOgsu4Z9Ga7SquwbNQ3kVGvywRcUphqAZtIcCTYK03oWx%2Fl6gbuk2bzl%2BLBgS3e2Vany%2FIYehYbsOYLdNJzghcpvljkr9FgCklG0edIt8FodoDtXyd0V2u8jRulSMvbkhCqtsTkXZ5vfY6XMAYNY2rRI1oHKizhTu0oF%2FCdJCLSB7Arj4Y7McKYAjyfe3Zkp0%2FM5%2FSq&X-Amz-Signature=e1216d5912803253153fffd5000a77e98a4b35a44f6f73e8f8700c1882c10db9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WY7MDOGF%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIFxmNqy8F35HhWedzUOaE6A%2BhOR5hl%2Fwq3usOxczMJ1VAiEAxhXmwv7i8EaRvU2t%2FrGK6sjAggT%2F5wst%2BVguxgt4xEkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF5moQTxPYysnnlIZyrcA%2BePEN0ZkOG3TL1YGxv2HReBd4LxAPnLY8Z2A2WXqr2%2BTr1dFvacTQz%2BsTt2CTTs4Qhx9s1wMS9%2BtDAtoVeijISSMqqMmyWHata12SAytj06uKJrbqPBzDEtW%2FCYx%2Fv92%2BXo7dTn88v2R%2FFxeNr%2BNo%2F6HIjen9UyqwRsk8KeuC%2Bw5UIJkHw6Po955ELIBDljIslNwtpG1lHNOIui2%2Bgx6ynKTAiEsABMpcGhay%2BsWMF%2FnMgavnwbkb6Fi%2BcHNAjal69Qk8il1uI8QD6GxePWdurFiCHHKofeew1bekrAWH4M%2B6q3szSMUeFCW0Lp6wHOhkH71dogB1sDyERNyrmyT9cUcrR7nQbahimnRM2eogrL%2BhepSAg1stImkfzex5yM8%2FXT44XSUP6UI9HDa2j0eJRfubqtb53hbPdM%2BVhLSjbjKelBFwxLKyLA%2BF0%2Fl22gMGqJAk%2FoYwRzvfX1RBmz0eUbvFipw10yDDwqJpP6drSl8t8dpQtcfrFX1O6LxQnPquT0DlCxmpEhpOLjZLgMWYTXmoXYccYb2MyqtVwoqjbyIDum%2BTf%2BaiQ4vNdHv%2BEVLF5ceb6uGcwAnysodIJ31nOYPNjOQo2CHGOIt7nLVwJOd%2Fcf3JkKVlk1jAwBMP3XxcsGOqUBNGDYGuWb4Hk22hbigO09ciOgsu4Z9Ga7SquwbNQ3kVGvywRcUphqAZtIcCTYK03oWx%2Fl6gbuk2bzl%2BLBgS3e2Vany%2FIYehYbsOYLdNJzghcpvljkr9FgCklG0edIt8FodoDtXyd0V2u8jRulSMvbkhCqtsTkXZ5vfY6XMAYNY2rRI1oHKizhTu0oF%2FCdJCLSB7Arj4Y7McKYAjyfe3Zkp0%2FM5%2FSq&X-Amz-Signature=04f2ef912d1d29fad7c5c4baf11742269a2d943e81cc5e0a07393276d9daf7e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



