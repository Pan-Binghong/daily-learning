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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQRUDIQA%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQiXzAzQOzk7fbWIlDIvZ7HXOrme8xvwIjKeU%2Bx87tlAiEAmUBWyiiHO%2Fc0y9eVNEo4IDpuOBcIuRaa21%2B0emzlPVoqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHwFrKg8sRyi6Vq%2BLCrcA4WoQCOInIQLDj3O6RvXy%2FFpzcA0uNg6e5UnyMZb4cAGVED68%2FRDW85ud%2B1OJxlds1yGoc%2BGaRxJTRC5kdn6G63G7peXJHeLRpcMP3QKYWhsX2pEjJ443KbtXYJukpyY6tiUAmOXLKbSsuqMLF6hML8WU1eeZCXyd6CkMmXIHUecWZcTM0fFO07bwGG1mPiGLd6Wx6%2BdAelmxraWaDSZPaxTeXUoGvHr%2BkR8DKkXCHXvlCXEDDqKo7Xy4Z%2BMrUJO6NqNDgF8GqKEAuxsi1Ld2zm0V1FVDT77gqZeZjmqsBSo6ztq7XozZG0Ze96mhZ%2BPSzGenV8aKWFFRUWkR%2B9G%2B%2BwZ%2FB9kKcrfLIUjuAYeoHOR%2FOBcn8keX49yKi9K0Zu67KLn0Z2W8sDGgx1NVk3Zr6ct3FndaYfLOoxZsPHLlHSTHH6VKKf2ZH2c1NU486Gf6a388awBdrpv2irfdqOspJSVkjUIk7qbL66OehCEG9sdI6uhcnKWKIHvQ9Hg7uxkWV%2BecgsbD9WVnXF4plyfHA5%2By9Oz9tfxyO8RUsBEMXEudtV3ZjcA0f1u0AOd0%2FXgkM8cWUNkdAbSGtXIF1MYUuUGGwryV8tDuaZ6G5PGXGgsGZkcjADvKGO7LjgMMMzeo80GOqUBMHkN%2BSl77tw2lioW8t1gyAnzJ2uw3xbFkyHQzdGHOMIctQfssAjyoa%2BAV2oXq9oifJqbIjGTlmzH2563LZtUM3%2FyOy%2Bhqnj4430Bm9N7mN3aStU5ZoqYkCChPbqIOXNFPs3OhubwFA7oJBXge%2B2LGfuuqItJx0eaOmAPnerbZuxdC5NXlREkQMu2skGxx5koIqlfTAlJAGV%2FV%2BIfwrz4lQhgb7zy&X-Amz-Signature=0fefc7f1dc66be6f59b0179f99c0375e07f24486428603a0c9f4c8bd5310e975&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQRUDIQA%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQiXzAzQOzk7fbWIlDIvZ7HXOrme8xvwIjKeU%2Bx87tlAiEAmUBWyiiHO%2Fc0y9eVNEo4IDpuOBcIuRaa21%2B0emzlPVoqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHwFrKg8sRyi6Vq%2BLCrcA4WoQCOInIQLDj3O6RvXy%2FFpzcA0uNg6e5UnyMZb4cAGVED68%2FRDW85ud%2B1OJxlds1yGoc%2BGaRxJTRC5kdn6G63G7peXJHeLRpcMP3QKYWhsX2pEjJ443KbtXYJukpyY6tiUAmOXLKbSsuqMLF6hML8WU1eeZCXyd6CkMmXIHUecWZcTM0fFO07bwGG1mPiGLd6Wx6%2BdAelmxraWaDSZPaxTeXUoGvHr%2BkR8DKkXCHXvlCXEDDqKo7Xy4Z%2BMrUJO6NqNDgF8GqKEAuxsi1Ld2zm0V1FVDT77gqZeZjmqsBSo6ztq7XozZG0Ze96mhZ%2BPSzGenV8aKWFFRUWkR%2B9G%2B%2BwZ%2FB9kKcrfLIUjuAYeoHOR%2FOBcn8keX49yKi9K0Zu67KLn0Z2W8sDGgx1NVk3Zr6ct3FndaYfLOoxZsPHLlHSTHH6VKKf2ZH2c1NU486Gf6a388awBdrpv2irfdqOspJSVkjUIk7qbL66OehCEG9sdI6uhcnKWKIHvQ9Hg7uxkWV%2BecgsbD9WVnXF4plyfHA5%2By9Oz9tfxyO8RUsBEMXEudtV3ZjcA0f1u0AOd0%2FXgkM8cWUNkdAbSGtXIF1MYUuUGGwryV8tDuaZ6G5PGXGgsGZkcjADvKGO7LjgMMMzeo80GOqUBMHkN%2BSl77tw2lioW8t1gyAnzJ2uw3xbFkyHQzdGHOMIctQfssAjyoa%2BAV2oXq9oifJqbIjGTlmzH2563LZtUM3%2FyOy%2Bhqnj4430Bm9N7mN3aStU5ZoqYkCChPbqIOXNFPs3OhubwFA7oJBXge%2B2LGfuuqItJx0eaOmAPnerbZuxdC5NXlREkQMu2skGxx5koIqlfTAlJAGV%2FV%2BIfwrz4lQhgb7zy&X-Amz-Signature=75d7069ce36871a1e9b13915611bf9f191e0a57bfaa69009621e27d070083fd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

