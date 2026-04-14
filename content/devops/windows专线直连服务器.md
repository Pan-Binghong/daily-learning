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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGV6WPD6%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnvyDyigf8wc3gPyu74f60PQhaWhp6bkxwM9yLsxY8BQIhALssCH0N80DefljDiwEsbJOw2njjGOI%2F6ePdTY%2Fb36LhKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBKHHx9RuVcRQT1GAq3ANTKOC2x6mp%2BJh2DNpDzQOBHwYv3eeOIVFDR2kDe96I9ep7zUksJGvWUTvJSOyinKOfeJwNvs6agNArPowwqwPpQH3cjsn91jxM3uzV9mGyC27DXqHeT70fzQChaJoeST0N2tfUVBifWKL0xhi6rW%2B30av0kZ1zTv6fScCt4wvnM2VtugDfOtspJB99XPrXLw4sNlcsjYSzi4i29DW5tWjV%2BHd%2BfKK%2F2wgyapllqvuYR1hff1OI9e8vGy9EgWLDpwp19ecmoHsZwBSG6Uvn68lp4cOCyj67R4WTJT325PLpSmyafNmhrX6onRUXwPgy9h5c2i%2F2xH1sicLwUSWTjLvh6Nb%2FxtY1soV0MkFjCCqx%2F0tSkGFUOc7iWfmtTxa%2Be2BwLwA2zTGFLugkGmrGx8zfpgRe3fNGY1vEsI8ty%2Fb4xLix0doe7p6QXrPAUR8SJHeFdJI3%2FpQpp2kvkD5gM6TbSY8K2Bpis51g1Q01KgdoYy1bWyC9M9Dtf4DD6e9EGt%2F1BKdI6xPQlahWbMPWwijo%2F%2F0cgIr7NgqkcmhiXHOcaOchBAwEJQQ%2Bz0kkzrDQTHV6%2BdSsakCXxpkBCDMlXrf57ZyVhbcVXDIGg1KxLb9VBZDmTNIfxJvLrY%2FMFDCf3vbOBjqkAeAe6TtMSd29Q8svGXKfNN18x60MWy%2Bd2289J9fZGHNPM5jVZ5PHBnzsLj4GBzHTJ5rB8FMpJxwlYmh0bUKMNZK%2FNdzDeCdP8Bg4UCu%2BDoa7RlLgoA9CyGb2Qv0AIn610G2Qiv47WmXdXc8HES1D1H7Blx%2Bl6bMwbLW2p0aUnx%2B8EivVm%2Bfl3kgDWA9GtXrqZ3uSRHg8ZmBscE45dRk3Y1gFj336&X-Amz-Signature=6dd1a91e48d6369cdeb3d7d031cf3486f409ba8a56efcb23665c3bcc1e92a6bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

