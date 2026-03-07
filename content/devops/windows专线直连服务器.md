---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UABZSZB%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIG6CbxGuJkCK4jvlm%2F7UzT2ZVIS%2B9Jih3UNW6VQdJRqQAiARLBOAyv9mQ6Mkj2JhIk9F16nUi7OPfUPX8mYFwxK33iqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMg7kEBCLKvfzY11TaKtwD6DIZq%2FVpyr5uTqCaRYrGj3wRJj75J2iOjOD%2FY2jcYTlMLu9b%2BIXyS5NrfM0NTjcJPh4ZZ3arEExIllIewRHIUTidbmB%2FRdn2b%2BVZ%2FmXQWq7kHWhMPezBMITzPZ6PvOWvxJZi1EGJBWDd1ctDKCj9E1sifihu6ARO0lnjEjPEG3J%2B%2BkuiaUB2O1tKntWbfyCkpZouBm8FEEJ8lbupX2j9Uf4AdR0%2BCjV8dTUmUPmMpq1C8q598xma7p2EHOnHv4gkbqO66SiMUaUeQU8m%2BevB4a6GNzTdNWhRS%2B%2BjsUUxtpd%2BsDKKcH6xJcgMWcArWsSBQDAvL0dH1q7mZji2rWlL8TlggA7l%2BkX%2FZh5lUtheEhHSM6xkXDcn%2B4rT6Ey02JwG7O9AGS8BHuvs4S%2FevBLRojkSrHRNMKoCo6oG1AtzbNyyCpThfevZsm2B6hWQAuYFl3xKQYns9ZdNkLedGNwrarLXdqEG5l9Jx0yGBY7SmGJteyoVQLCwxxBlNgc8RP5jYIUwxM5Orx9DiAqLBiPT0PMPFuz2usylCkYcu6BcatRUeHoYHvyVQIAwclN0Z7zftSHhmFMIeE5wcFnf5iWYL1j6hJ%2FyZDR6GgWqqYKCwTRehR27%2FfGbd3QHg5YwupSuzQY6pgH0RXo%2FlW98QUTzEdiskYWV0qnEYwyS75tRs2ZP16Hwq0%2FekB1%2FcV3kD18utz2uQ2zaI0lI3Ht0TolsKSzOhK5krArlm96siBFSLss6csxONoidXkisG1A3obOaaApflx6oqhcV4qmenjzmRxu5Rzg4HaLypCY1vpt3%2FFdIGHFR8orx74oWkR5scySIs5%2FdnYsKvo%2F8BOYWSC%2B576z71cun4UB80SZW&X-Amz-Signature=3cdcb8c8a5ac5127896505d5110e969a9a78089d767b7597a4497c1db8ddcc89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

