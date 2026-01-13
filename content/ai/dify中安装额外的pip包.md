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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMB43HFJ%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICPFkntH27NuPmpE0moUn8pZtF5G5B%2FSyLXT%2BnwjAaZTAiAyh%2F6dVf0ibKWd1MEwaMmU0RstBIbOa9FiFook3wNl%2FCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHNKWtrmHldjbewi%2FKtwDmpysceVuu2FKeCVrE6BM8Lw2GqTTiP6BFzz6MOZFG8BjDjx7LG4jdJ8kD9QDWjftYIIwjgxnnt4BW6ygKLvcD9gbxeV4rfrmTm8stnxDnouwhWnY87m30QPVLRy%2FBCy3P2Fz8xQmVndii7V%2Bs4VzpXjbchBtddOPfF4q5Wo0cavBVXI362pIvg8tTwi6y9DOoZzWMk%2ByC9SWXJaOACUZDE6QTCTry6eyr1avWOQkp1mW07FqRVNo57VMWgGXgBd45rs1NOLNwZNhQJ51HehUsuadGq1rVSeFjB6nxqaJszpMNEEM2E2dJIlE%2B86oSoa%2FuVN571%2FkApKMqroiG%2Bwcxc6n6o5EzYB7eS7TNJWsy4pA7folURaqKYCY7LjEwGHCPpIIC80o5PckqfY2S7GBeUAxp%2FYWD6UCVIanTGnALlbs2A8QxtTXY53nJPffD4XgKKwWksNyWRgl7IeI%2BPxJ9h8GIeu8lnFb9Ly%2BdPtUfgkOmMyZ0qaTbtWeLaJ2tuizvKQEUtN72xLJY7qcWsZibnmXCsYffQAGnj2jO3ZOzxhymhYGo1eke2R5%2BwNAdPaQdrQfop4wLR2VRYnYHI0GmTH7EzcBJSlKxxdcHMAupEbGvH3QsfhU1vsX10Ywl%2BeWywY6pgEMTpqIxEi1mOfRfJkoLHy%2BROti%2Blfd0SVvM0g5t896H6GzyGQyfNUb6bgZmy24mEBrOA%2F7TfoC03IJ9F9ej%2BXAIZAqmPXDvtxG0cEqG3OQH4X%2FckCkBrD6%2F1TvdJWNkEreTB%2FCNwSOJCczPqFpnzfeMSvkESkOeB0y6kCbPx8mLxVVQft0s09Y4acTHljeU3MIenggbquiAzg1HvffCJB52xKJKYH3&X-Amz-Signature=8d4738d7921ef36eb2297ec17014e60d9d62f9e61b832245039586f218e8845d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

