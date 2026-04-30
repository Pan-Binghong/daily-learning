<<<<<<< HEAD
---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png)

---

## 2. 重启docker

```javascript
docker compose restart
```

=======
---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644BD73JV%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDBIq10PG3h5N3b5H4iHnPFhkUmW%2FDsSNMyK486dhicVQIhAOUUPfWNypwhBLOOWTYIPdEf5DqJqGYhwNdp3s0ELrmbKv8DCAkQABoMNjM3NDIzMTgzODA1IgwmUwh16BUueyjZAMsq3APhrhNpccQYgsGqSQWKD3a0aoNbuqITggYNRHa2rztG%2ByZfoHx1CuIB6qKvk%2Bp90e6yJkvFpRtqXfOM%2BSH44yjzcJqwSAxhP7O3mVyvHQkJhWhq%2FBYstd%2BtcrylaAkbq%2FVBsf6QJ1hak6kmKqH80UdyAyJvzLJVhhi%2FCo0yoE%2FqNKbn6QVvj%2BMtorijFeAB5tVovP53jJnpwFi7m%2BXi54nSUAKgrz%2BQsbd4JTWG0oGuIvr6btqNZNKaqCDnbH2dnKadddjMN7XVIp2N8ttD2HXtcZ4yscdA6CgfSXtC2cwdekKYqNg2Pz%2F6m2EnHh7zWviZPowX7iu3tXpLVuY4ZOTpAuzwylZnhaD%2FD6o7%2B2nd0prytSmNT7CNUj5jZBb79U2BFQPl7Ty6XdG%2FS3S4h0MXFbw%2Bbp0pXAofOWEZSPx46y0W%2B6I3NG93kQ4jLsiNWmOWYA6JXYaK7j7KFD%2F%2FTu9gxz2RtDTwgICq5G6hWLvoDmdcbCc6Kvdt3gUaSXhDLX9Vs85do4hB1YRB2vfmXNWUqVQUa5kyePsmAhaOcH8GcwPOT3YqjwIvhminTqrklnsU8XHxpiT3tRZPDD6NMqAx06IllJaS5Uc%2BLizBdDY%2FE37XHBlEuNGCTbY7HjC0nczPBjqkAQtFOsBSd%2B8d8GkS2cKk23xxxl2D2fcq0N0qrdZnbmOSiEQderznxmXr25bZ0S4grv4dzHOM0W6UU214VchrxwuwwPPdT20Dbx%2FY5aARu51axW7MUTeKJAuTSphhRYdi1%2F1iGwBs5ymXO58k4%2FrDSw63oiozlmKXDyukyJ58vsv0pKknkiYA1%2BpkTyUsN%2FeGRqfKT77hFLn4GCi2gAcFMKnM4kKY&X-Amz-Signature=af0ec11ad82b90f0c1609359f4771b38a5fcaa9c09e566f802445e9221a77009&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176
