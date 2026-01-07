---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTW5MUO6%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICsg0FA%2FSkE1CC989213YXCy3YKChCfKgk1xtfclA7I5AiEAmC9jX4SfxmaNqj7iHjj%2Bs7TaJP8Qf8xY4dFqa1gLI%2FAq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDDwWvGDJJHbLB9Rq6ircAw9GW4%2FaYtdxKgy2HGRKwpSAQQjDr43bL4JZkR%2FW5tU8a38nY3XI66ThiZy3pyf%2B%2BQiis7cpdwiN%2B%2BTGXUSQrcJR5WihYwaGOQ9LI5SUAHW2%2Fs8h7yz5s62rHS3vATKU54W%2FR3hblvZ06AcuB180o5J9fke27bZwNj%2Bj3tYkYLE2x38EyugFHVUfcqdKM0qMTJa5RG0KouLS9u7q%2BpOwzah5DaHt5w0FVU6kkN%2F5EIlO%2Bv5YAxHzsGk%2BZtSmKrs7cdWofcRmgPabV%2FIL9h3WQktBmffQWe%2FXgodvqghwUGqlnxa9JmA0nIg9VksBM2hLuc2JrUO7AFBPjeTDsjpu%2Fg0Aq2g2h89N9meQmgBjiWDl2x5fPjj%2FinSZ0eGhqXGShiIA6DrczJ9B9w%2F2vz2jBoij64FLwabmultCNhV7ej5iOUviWSDe%2BSYu%2FKL9zzyfw5OBo7aPuoqf4PCEtOyZ2WxS1Eec633%2BkGYaubsPQ2yiJQQ9KentcOGzmrCr6VdypXzmwShxQFX%2B%2F9lv64BudVXh7hzfLvxz%2BpH3iYNEMlcbGWaTUsUWg2Lyd7bSbLMdOn%2BNvJ5rDRh924BeypHlNNsLmTm%2FdFRTVH6edg9qJkdllMPz0eXIqJfW%2BFJBMImP98oGOqUBcUwJRLjvuf8YcYuDWG0jtyJ%2FyFrovfYQNdiL6mUilOA2M6CAusE4yIV3coc5DDNcuMdXDFOuDBqsCj963VHVH9l%2FYFT08wqWt6wp7BEjLvT%2Fjn0rOs0IjtXljmAfMzovyDyJkF%2BRGg7BxWh5fek0ieiGhlH6lt4kFfI2e3e%2F0Gb5Klf3Sw6Hw2OSVL6sVxORlHyHls9jd5KuhjS9vHhFvgeBcsFk&X-Amz-Signature=ff300de218a6d9c4d808c52de9baf1f0f3b654ef15d1be3227990651d2164544&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTW5MUO6%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICsg0FA%2FSkE1CC989213YXCy3YKChCfKgk1xtfclA7I5AiEAmC9jX4SfxmaNqj7iHjj%2Bs7TaJP8Qf8xY4dFqa1gLI%2FAq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDDwWvGDJJHbLB9Rq6ircAw9GW4%2FaYtdxKgy2HGRKwpSAQQjDr43bL4JZkR%2FW5tU8a38nY3XI66ThiZy3pyf%2B%2BQiis7cpdwiN%2B%2BTGXUSQrcJR5WihYwaGOQ9LI5SUAHW2%2Fs8h7yz5s62rHS3vATKU54W%2FR3hblvZ06AcuB180o5J9fke27bZwNj%2Bj3tYkYLE2x38EyugFHVUfcqdKM0qMTJa5RG0KouLS9u7q%2BpOwzah5DaHt5w0FVU6kkN%2F5EIlO%2Bv5YAxHzsGk%2BZtSmKrs7cdWofcRmgPabV%2FIL9h3WQktBmffQWe%2FXgodvqghwUGqlnxa9JmA0nIg9VksBM2hLuc2JrUO7AFBPjeTDsjpu%2Fg0Aq2g2h89N9meQmgBjiWDl2x5fPjj%2FinSZ0eGhqXGShiIA6DrczJ9B9w%2F2vz2jBoij64FLwabmultCNhV7ej5iOUviWSDe%2BSYu%2FKL9zzyfw5OBo7aPuoqf4PCEtOyZ2WxS1Eec633%2BkGYaubsPQ2yiJQQ9KentcOGzmrCr6VdypXzmwShxQFX%2B%2F9lv64BudVXh7hzfLvxz%2BpH3iYNEMlcbGWaTUsUWg2Lyd7bSbLMdOn%2BNvJ5rDRh924BeypHlNNsLmTm%2FdFRTVH6edg9qJkdllMPz0eXIqJfW%2BFJBMImP98oGOqUBcUwJRLjvuf8YcYuDWG0jtyJ%2FyFrovfYQNdiL6mUilOA2M6CAusE4yIV3coc5DDNcuMdXDFOuDBqsCj963VHVH9l%2FYFT08wqWt6wp7BEjLvT%2Fjn0rOs0IjtXljmAfMzovyDyJkF%2BRGg7BxWh5fek0ieiGhlH6lt4kFfI2e3e%2F0Gb5Klf3Sw6Hw2OSVL6sVxORlHyHls9jd5KuhjS9vHhFvgeBcsFk&X-Amz-Signature=4097807ed7e341abc370ca816afab49dd61ca49ad1cab4510cd7ab421201bcb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

