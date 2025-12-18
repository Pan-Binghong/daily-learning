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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4VDSWND%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtXCEU%2BvcsEbSBTkU1Zge0B15COLAQuK6DdgdnpcQGcgIhAOEwl50TVWVOw7uT9Jfpyiaw1VUxEXW%2BIaE%2Btrm1eIOqKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyHhmVoK0PP9YnjUOoq3AMrYjwlbEv6mVhi6XY6rtgXFJQpn%2Bst%2B%2FEyET%2FNPR5morRNz%2BrudY12reVlUZZVJsX87RWumyL1AimL2jSQldP7F4JLwGVQ2zeqoHfUdl3hfKNwQ9meAE8Xpqm71UmIMREzK50rbwcr%2FqRywSGmSJBgfthYV7v6NKe%2F5d2T%2BkKHUKtEcNqJbpejSy6HY5W%2FCv4mbgAGLbw7FCd66qJbZeJkh%2BVTyFgEDn8QCZbX3EWIXCrwDkhT9uTH5jOso2j4EfaTL1SMSmwUThjLg4PkNyze2b0g3Ddbgr%2F4SGqzbgjH3TM8IUHhFwZTUoNR8WwtdiZ1UwUj0E%2FB4ylr8JK%2BfntW%2B9ygDirtXg3VnuHmWvv46eH6M1RM9kW21sYicj3DeWDsA3FsR2NhXmUigBa1xykseC%2FieiYx8DZs3KxBykiQAQPi1oDmKCDpOuu24DvFTFvE0iSZg0FetzSduMNc%2FJ0wmQ%2BTRoSBQQHqlJGPvhfewDxzl2%2FV0GHVc4LtQgXkovcVWMxvC1rxbW9QD4s9zJfX1HX4DuBtxaw4yTbY3s5MNrf9GwKiQq6TwxfcxbO%2BO1Rb7LbModPgnuwcgx7RHDiBRMEiUUyYMyDrifhuV804OrduGXPSsI9cqKK9sDD7yo3KBjqkAZ%2Bt70iXk4xbXlauCJ5v97jVb1jGMoQhxPdpyF4NTGfM%2Bwf8QmWsnaDmE0bqeRZ2NCZovkAA%2FJjaFC9A1Va27aAnY2VgLFOl4n%2BDXBgUQphf%2FQiqc1GpfyYyrNU%2BWiIdMtroW7yGkwg1OeP7awCe0QTOWmfTXl3Z6PWejfAlWUWGRSu2vuSQwblSi8Oea2f5YSrDOT81ampZ147sovN92gGi8XWg&X-Amz-Signature=f63cb6000e9d6276e71131686a97f3d9679aeaf128593a8365f7c67df90d1202&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4VDSWND%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtXCEU%2BvcsEbSBTkU1Zge0B15COLAQuK6DdgdnpcQGcgIhAOEwl50TVWVOw7uT9Jfpyiaw1VUxEXW%2BIaE%2Btrm1eIOqKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyHhmVoK0PP9YnjUOoq3AMrYjwlbEv6mVhi6XY6rtgXFJQpn%2Bst%2B%2FEyET%2FNPR5morRNz%2BrudY12reVlUZZVJsX87RWumyL1AimL2jSQldP7F4JLwGVQ2zeqoHfUdl3hfKNwQ9meAE8Xpqm71UmIMREzK50rbwcr%2FqRywSGmSJBgfthYV7v6NKe%2F5d2T%2BkKHUKtEcNqJbpejSy6HY5W%2FCv4mbgAGLbw7FCd66qJbZeJkh%2BVTyFgEDn8QCZbX3EWIXCrwDkhT9uTH5jOso2j4EfaTL1SMSmwUThjLg4PkNyze2b0g3Ddbgr%2F4SGqzbgjH3TM8IUHhFwZTUoNR8WwtdiZ1UwUj0E%2FB4ylr8JK%2BfntW%2B9ygDirtXg3VnuHmWvv46eH6M1RM9kW21sYicj3DeWDsA3FsR2NhXmUigBa1xykseC%2FieiYx8DZs3KxBykiQAQPi1oDmKCDpOuu24DvFTFvE0iSZg0FetzSduMNc%2FJ0wmQ%2BTRoSBQQHqlJGPvhfewDxzl2%2FV0GHVc4LtQgXkovcVWMxvC1rxbW9QD4s9zJfX1HX4DuBtxaw4yTbY3s5MNrf9GwKiQq6TwxfcxbO%2BO1Rb7LbModPgnuwcgx7RHDiBRMEiUUyYMyDrifhuV804OrduGXPSsI9cqKK9sDD7yo3KBjqkAZ%2Bt70iXk4xbXlauCJ5v97jVb1jGMoQhxPdpyF4NTGfM%2Bwf8QmWsnaDmE0bqeRZ2NCZovkAA%2FJjaFC9A1Va27aAnY2VgLFOl4n%2BDXBgUQphf%2FQiqc1GpfyYyrNU%2BWiIdMtroW7yGkwg1OeP7awCe0QTOWmfTXl3Z6PWejfAlWUWGRSu2vuSQwblSi8Oea2f5YSrDOT81ampZ147sovN92gGi8XWg&X-Amz-Signature=98339bbee032fc72f2e0bb04a08180fc637dadc651fc824be65128c92a30b9e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



