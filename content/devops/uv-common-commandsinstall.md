---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRLZZOUL%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIG0RoWVHWBNa7Ve0%2BH%2FXfD4F8vXvJxEw6o5198RRsigJAiEAszjPhJXyqdNaoze%2BRfiUAV%2BdOi5n3Rw%2Bt0xQ9Eioq%2BwqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4RXF3qMdsRoSigKCrcA4EcDJ1xtVFPZQc2DtfdSqvcpcBBPv6DthoagRkBXq8suATaj3MqOhfLtnTbOgx9MQAayTtGGwPeZCE8HZLLxQ7kAXF5VTtBXHdvIRgNVe9gMhExCfIhiCWTuXYnV2NRPCkYVQh0bazM9wFz3DJkQH7aKErmqJG9WjQGTblYHm%2BInHfgsw52XKOShyexzbV930Bhp9CkUq7%2BQtFgVRylMv9LAUssWSBuFOjxu18NDzg2abkCoW1ycFhezDO3Ad6B8vYQw2X0KRjcpB7gyI1G7KuAseHsf4hOJptEVb%2Fzb3wA7HJv5Jzw8RnNETIrHLeaLWaFzMIxXR4f00jDDEe5j9Mt20k5U9rVLY8xvhr615HHv8%2Bv99q6JU0LzFgIcsqoSwtP6rXA2Qs3gcrZylM42Jh0bNN7Rmd%2FW8ctts%2FXp%2F7uyDFt9wWxcNlPMPA2HRfL826T2iRsVnLnW76ddMYo8Zmt599iOmE91g1yZExhnEtqLKeysS9toUCAWszhTvV1BvKhfRrWruCvMqRGKIafBcxKevSJ33vMU9bU6uHWUbdAxkfMtMXE9h3K6zEN9nJoIy1CkxIcma%2B0xkldwxzVBrae2%2Bfw2nn6e3sd%2FjmCMY5OJ5cz3IUueO3WMhlAMJPtxc8GOqUBidQ6uM2WfpsNPPgsVw43ybxeDn4wkiBAejdBKotvgVuegW19gFZgZpjupYD9SPmB%2Fm2ADJYyMrs1U%2FM9aYLEnDQJMDlB2aszJo%2FlU2rVfLYtbgAhiFQQLjMVE1Zk9zUPXx0s%2FjTIvwRJx%2BiUdK%2FOHzCTqzL%2FchURHlIzwwElAvIxWhB4DSkTQ%2BkHcShf2eu23hdEwljepguphNjzX%2BenBcYHLLaG&X-Amz-Signature=9512d652d7e0e9a0c0734a8350d729310f4a75a9d284b7a8dfcb9927c83cb808&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRLZZOUL%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIG0RoWVHWBNa7Ve0%2BH%2FXfD4F8vXvJxEw6o5198RRsigJAiEAszjPhJXyqdNaoze%2BRfiUAV%2BdOi5n3Rw%2Bt0xQ9Eioq%2BwqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4RXF3qMdsRoSigKCrcA4EcDJ1xtVFPZQc2DtfdSqvcpcBBPv6DthoagRkBXq8suATaj3MqOhfLtnTbOgx9MQAayTtGGwPeZCE8HZLLxQ7kAXF5VTtBXHdvIRgNVe9gMhExCfIhiCWTuXYnV2NRPCkYVQh0bazM9wFz3DJkQH7aKErmqJG9WjQGTblYHm%2BInHfgsw52XKOShyexzbV930Bhp9CkUq7%2BQtFgVRylMv9LAUssWSBuFOjxu18NDzg2abkCoW1ycFhezDO3Ad6B8vYQw2X0KRjcpB7gyI1G7KuAseHsf4hOJptEVb%2Fzb3wA7HJv5Jzw8RnNETIrHLeaLWaFzMIxXR4f00jDDEe5j9Mt20k5U9rVLY8xvhr615HHv8%2Bv99q6JU0LzFgIcsqoSwtP6rXA2Qs3gcrZylM42Jh0bNN7Rmd%2FW8ctts%2FXp%2F7uyDFt9wWxcNlPMPA2HRfL826T2iRsVnLnW76ddMYo8Zmt599iOmE91g1yZExhnEtqLKeysS9toUCAWszhTvV1BvKhfRrWruCvMqRGKIafBcxKevSJ33vMU9bU6uHWUbdAxkfMtMXE9h3K6zEN9nJoIy1CkxIcma%2B0xkldwxzVBrae2%2Bfw2nn6e3sd%2FjmCMY5OJ5cz3IUueO3WMhlAMJPtxc8GOqUBidQ6uM2WfpsNPPgsVw43ybxeDn4wkiBAejdBKotvgVuegW19gFZgZpjupYD9SPmB%2Fm2ADJYyMrs1U%2FM9aYLEnDQJMDlB2aszJo%2FlU2rVfLYtbgAhiFQQLjMVE1Zk9zUPXx0s%2FjTIvwRJx%2BiUdK%2FOHzCTqzL%2FchURHlIzwwElAvIxWhB4DSkTQ%2BkHcShf2eu23hdEwljepguphNjzX%2BenBcYHLLaG&X-Amz-Signature=7cb5be99fe508220daba02d339a30a062dc5ab554d7faab8480a2202f9a7abf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRLZZOUL%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIG0RoWVHWBNa7Ve0%2BH%2FXfD4F8vXvJxEw6o5198RRsigJAiEAszjPhJXyqdNaoze%2BRfiUAV%2BdOi5n3Rw%2Bt0xQ9Eioq%2BwqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4RXF3qMdsRoSigKCrcA4EcDJ1xtVFPZQc2DtfdSqvcpcBBPv6DthoagRkBXq8suATaj3MqOhfLtnTbOgx9MQAayTtGGwPeZCE8HZLLxQ7kAXF5VTtBXHdvIRgNVe9gMhExCfIhiCWTuXYnV2NRPCkYVQh0bazM9wFz3DJkQH7aKErmqJG9WjQGTblYHm%2BInHfgsw52XKOShyexzbV930Bhp9CkUq7%2BQtFgVRylMv9LAUssWSBuFOjxu18NDzg2abkCoW1ycFhezDO3Ad6B8vYQw2X0KRjcpB7gyI1G7KuAseHsf4hOJptEVb%2Fzb3wA7HJv5Jzw8RnNETIrHLeaLWaFzMIxXR4f00jDDEe5j9Mt20k5U9rVLY8xvhr615HHv8%2Bv99q6JU0LzFgIcsqoSwtP6rXA2Qs3gcrZylM42Jh0bNN7Rmd%2FW8ctts%2FXp%2F7uyDFt9wWxcNlPMPA2HRfL826T2iRsVnLnW76ddMYo8Zmt599iOmE91g1yZExhnEtqLKeysS9toUCAWszhTvV1BvKhfRrWruCvMqRGKIafBcxKevSJ33vMU9bU6uHWUbdAxkfMtMXE9h3K6zEN9nJoIy1CkxIcma%2B0xkldwxzVBrae2%2Bfw2nn6e3sd%2FjmCMY5OJ5cz3IUueO3WMhlAMJPtxc8GOqUBidQ6uM2WfpsNPPgsVw43ybxeDn4wkiBAejdBKotvgVuegW19gFZgZpjupYD9SPmB%2Fm2ADJYyMrs1U%2FM9aYLEnDQJMDlB2aszJo%2FlU2rVfLYtbgAhiFQQLjMVE1Zk9zUPXx0s%2FjTIvwRJx%2BiUdK%2FOHzCTqzL%2FchURHlIzwwElAvIxWhB4DSkTQ%2BkHcShf2eu23hdEwljepguphNjzX%2BenBcYHLLaG&X-Amz-Signature=b4260df6a3e8930a700169f4cdc6d57057a6303d50003c2b45ae85d85c1f57bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

