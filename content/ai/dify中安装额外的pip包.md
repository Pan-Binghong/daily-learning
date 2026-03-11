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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6ZC3D6H%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFd7z0%2BDyCP7VCwcebTvl6TTs2OJlU0%2Bv7cdMy0WdgP%2FAiAO3D6%2B30xcMpHQlooHI8J3tbSuEiTu5EQuebjX8iiKPCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMGqQUP3IsWdFQfHhgKtwDPNjI0LDtvMZDL6Q%2BlVCsBME%2BBQtf9wx7FN9%2FbcN%2FdksQ61tB5TyttvD4q9D4jyLI5%2Fd7nYyEkOQh7vY42Inw6HUyLApUg02KX55hXolpFfavSAsE7TnNmQ989f%2FvM31fnKEi1%2FyLF%2FqH46JNUORPF4ustGF8KGhnRKoUiUwT7sNlctpuWAns9RGEXN6Gb9Hpq42iRBvOFZ1hAt6GCLKiKswKqMIIMH36M9voJChiisuDFdKaYVhMg6e0AO5gV3RBmD8QdsLvZf6ToeaCMzSbCLlSKt%2BlEbTkY7B%2FuXvizCaclALF7sSRt0O2uDppSwvBDlq9RsY3y8RLVG0hD0ihSA1rw2LdEtxlZ4f2E8jLiX1J2XXE0Vhyy5ANM2joNGBqsnuBfCWN%2B9tTn8DhywCWKyIcevXIOPOYUuAQhsSgcKUcWOjnZzFpeFqHKr6ARvwIFUp0KRNGGQ3JZqtcQFd9r1YZbAOCMeQti8WwzdNX3vr9iAcl4tAN5pCL8ttwKHELIdAv8q98C34pqOJ1kq2fm83iD9M%2FlolYLeP5ZvCk6H0daC0fGtsPF1os8DPDGJhB%2FEXSVooIMQGDCs22F6Zbjh1QDw%2Bf7R7ta4TZvQayi0Opv2gsGB35yNk5%2FFgwqMDDzQY6pgF%2BUrLUouJ%2FlGewDGG%2BhBejwOsfD%2Bo%2B6%2BlI4oQIqfT84QdZ3SeuQvC%2F%2B8h8X6Vq5htwsgk9YdcyguEm%2BMfYfT%2FmZQI1s%2BLWnogLkPf4IGUJbJjalDzokmFFI1xi09M5w3oPdZntwXEJmvAAT61MehVnGs5ewW3%2FxybdCeL6MpWAfQM6PQFjEQelA0mk%2FZS2HIlLbEjEJQem6707p2Iwb4vWFLaxs6Xq&X-Amz-Signature=5134c028176eb65dfdd2746e402c80100cc3515507d6bd176df4c0e0d16b5a3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

