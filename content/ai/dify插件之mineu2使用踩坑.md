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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SEP3ZNO%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2%2Fi5KRpkZGuFqIy1dZJIGGSGdBnrgHSeNY3cQdUz9pAiEAwkQV%2Blo6h0UgPjheswul1xjcDkCgpQZ5thMk3f7NL5sqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD6vgwQkPNFUpzrsyircA%2F8O7u0clHTxBqkeiqCQ9ML%2FOdpcp2LEMmskqd3ySb4THnqKRJd0QVAM8cyQui6fcD5vBj2P5ECKtOWDG3iMLSq%2BjU02U9oFHyWhv8fzooP0g9xKZxJNaa600hbAyensftoRHCG4edfqgOTnDwuNd3XtJ17%2Fr8UpRq996EDsYhYyGbZeY1W3C4uMTG7pVyZQSlUuqTTerLlM%2FiWaU2Y2dgwbPW%2BR9JAcCfYpl4DSBswpqJlkk6y3j4yqFSGUlM%2BqMytNeYvIZAQD8VgzokEI5Mtrom%2FVdLIWqihy42MFTDG8s9btVoUmFmXEOWz%2FpP4pSV2GyZuPRvx%2BgdWLCMeUmkCd4Z17gYYCHExi9KCWsgdYrobBqYrl5hVRjRcRHJ5ygdMxP4bbpMxdmZtV84OYQkmczloNdulgQQXpsYOvbWVjbGGq%2BzxT590uZYvMTqJK1FCBIXzk%2FTffXDN9OqmbaZvZjISyFRjoM2Wvm7mm5Fv8PuxjWvhJDhqGuy7kenOPTRfjrhEbGmF4iyVanNHWxfqdT%2B2o5IT1PEsdMXr2%2FVw0DsxM%2FXqdGhZgkNbZre%2BdwtdIBEHuuuIMe2Wbw8XByFVn%2FXPCb7TNjiS7aewfFKmqSWtW0dDEPWoGUiNwMKj0h84GOqUB0ay6iBRWq%2BZPjV675rdV24V8S0WAqNTZRGvbZpLEtzNn0B8J3i%2BClTylDk9U6ZI5r%2FbGMNnthRjjCeu2WX%2Bo4zLI84SIhS4UyKlGWus7QKqq96ay5lZqTh4iguWfCiemBBzwZXjZ%2B3m5yG4X0Oq%2FsVWAZaxzSmygtVByyUB6ipXQOpI9%2BRu7i2Vva9QWe9wQGs484wCuMZYRaWnG509pkNx9W4aV&X-Amz-Signature=0daa3aabfe405ac2d39528302c473569759c3ba89e1d0ad2dcec7c4fa833d2c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SEP3ZNO%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2%2Fi5KRpkZGuFqIy1dZJIGGSGdBnrgHSeNY3cQdUz9pAiEAwkQV%2Blo6h0UgPjheswul1xjcDkCgpQZ5thMk3f7NL5sqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD6vgwQkPNFUpzrsyircA%2F8O7u0clHTxBqkeiqCQ9ML%2FOdpcp2LEMmskqd3ySb4THnqKRJd0QVAM8cyQui6fcD5vBj2P5ECKtOWDG3iMLSq%2BjU02U9oFHyWhv8fzooP0g9xKZxJNaa600hbAyensftoRHCG4edfqgOTnDwuNd3XtJ17%2Fr8UpRq996EDsYhYyGbZeY1W3C4uMTG7pVyZQSlUuqTTerLlM%2FiWaU2Y2dgwbPW%2BR9JAcCfYpl4DSBswpqJlkk6y3j4yqFSGUlM%2BqMytNeYvIZAQD8VgzokEI5Mtrom%2FVdLIWqihy42MFTDG8s9btVoUmFmXEOWz%2FpP4pSV2GyZuPRvx%2BgdWLCMeUmkCd4Z17gYYCHExi9KCWsgdYrobBqYrl5hVRjRcRHJ5ygdMxP4bbpMxdmZtV84OYQkmczloNdulgQQXpsYOvbWVjbGGq%2BzxT590uZYvMTqJK1FCBIXzk%2FTffXDN9OqmbaZvZjISyFRjoM2Wvm7mm5Fv8PuxjWvhJDhqGuy7kenOPTRfjrhEbGmF4iyVanNHWxfqdT%2B2o5IT1PEsdMXr2%2FVw0DsxM%2FXqdGhZgkNbZre%2BdwtdIBEHuuuIMe2Wbw8XByFVn%2FXPCb7TNjiS7aewfFKmqSWtW0dDEPWoGUiNwMKj0h84GOqUB0ay6iBRWq%2BZPjV675rdV24V8S0WAqNTZRGvbZpLEtzNn0B8J3i%2BClTylDk9U6ZI5r%2FbGMNnthRjjCeu2WX%2Bo4zLI84SIhS4UyKlGWus7QKqq96ay5lZqTh4iguWfCiemBBzwZXjZ%2B3m5yG4X0Oq%2FsVWAZaxzSmygtVByyUB6ipXQOpI9%2BRu7i2Vva9QWe9wQGs484wCuMZYRaWnG509pkNx9W4aV&X-Amz-Signature=221ea029ab7db4337fb2cd37bf1ede1190ac2e066936c71fb9825d91287a86b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



