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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V2DOUU7%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEi%2B9op2rDooIcFodI%2BV7CYH7ndCtaPopOTzov%2FAbwrQAiEArkBFQrT1XUc3UP1qKd2hJI8FOCX40LnSrGB6PfkAgBoqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF8liXisr3gtNOdQqircAxhEtjrTkyGsWI17a%2Fq5tu%2FFfT9D2zbfpzlUpO0MZ0Y48Yo1%2FN%2BQQbB72Nssz470rUI1WBNpbdqAP1XzBOy8l3LLEIYdGyx%2Fz2RlW1OB%2FKB2%2BLxk9RzwqTK8tf1MUCrF3JJ2j%2FzrJzQ8HNdZAafDtVS7TaDjuniE1E318cNMEa7IaI6QmtaNrnuXfouUdTMNJykl2mlj4TlNoBasSHtm5yx%2BaVSApsOelZSzojA5acA3wiLl1u8y0Xgx9pVybCe2h8DPCPmwKlMlnjBWRf6VvKX9grcEJaV4o1TzVafCJfjtC4mbDaHeqFesV6tnK5vDJCGCP2oUHn1c%2F8T8jZZILCl7%2F%2FyufDJieRAJLhn3g%2Fo3ECdbZlkL9giVjBOLl7RrfFlHOsGoX6umGsCk7aK4uVpE4eq1aBgYeuoCRSX5THMiD10oyzMIq7Aj417s6nvMk8rQ98vGdILqtSZBWLrFYcE%2BUq%2B1zGOPf0ADZ%2B7OeLqtSJDOLkIOEnp%2BMXbEUO7qDwRNE3Ea6so6UZnn8%2FvJziebyJw4pJ%2Bq6Ynl4Dfxs9YIR2Ma7jBeUenCurPp%2BlmLurJF9IUb82RfcNw5BA6xmF4%2BfQK8fqf7d8TM7oR4z%2BwA7eLC0Js8hcVpDyztMJuYqckGOqUBhGbwebUzYHfgga%2Fgrwee0zOb39nhSqB16WAvnlpHpgW5noKbVjYffADZ6%2BADqwlNlxe879Qjc5QS6NaHgmQhL6gq8%2Flh7sgwkFFi29IsxIpsowaFbTfavHst9WE0dv0vXNxRJdTvTnrLxWSYyfATm69Br0WjkSezW%2B7%2BzTzwVSQQSEiKGKSEJDuNWgsG8ZLMDGDMFp3vLMDx6A7DHe%2BIFwYbjVKc&X-Amz-Signature=7d9bc842bf8a73e04d0fa1ffe81bcbfa7dfd9d7c121a335bbdd07739f0c6ad7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

