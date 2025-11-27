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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IFDXRUV%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGDKxyuLb8t42urfWm%2BG5SknHieL1%2Bk%2BtrNRyXjJJy%2BwIhAIDTSywilQUFpgpa%2BADWkr%2FEU8cx%2BNGLysXfxn2Q5%2BWEKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWTd5Gf0b27jlp95Yq3AM6xQlZut%2Bkecjjer0VVeXobA%2BSYJw%2FgN0C1md3A1uxVOCXDeBaJbdCb%2BPvhrBvUQSxQzf7BUPRhsmpi9t888WqlbRTTHawhxuRnn0XrRZ4GaCZB3y6iFJQrk%2B2VQtO4B6G3Tjsd5jQsXYHaRvC6vluIO2jjZoYU45aCa6OO2Lf1cl0dCeKAX15arTl5R%2FEpUBpNM2jgTxMGqyrFH4fuSyC46yuc7Wr05Rz8AQCJ0xpEityI0zySbp%2BqpDVD8V6rlpnBq9cRgI2haXD%2FN3h%2BGdlVXPb3LQ65%2BtIQgfayTpYmQhwmWQB1gjoaLOwrZ9FEnkd1aYOSc4NruCedmr1ZQbCIlT8IQppYMJcwrXRzs5ZYqgllJcYxeY7NIkr70mO3ykmPr%2FEIkXD09wRid%2Fl5gBv2rvZuvywiLAsPgGfTPNv1xR9CEuQuJt7kVXbD6hcGLlDERiuBUXqEVyZxvDtEmmO%2FHXPl02g0E%2BAfaOxIqG7fwk81hpoNjmwqpj7V9ESmJ4DbME5UIi6kKGa%2BIBYhOSaRC5YwPWSWFlNi6BGJfSHPIPVsABfa8m4i8%2FC7TmXev%2FtFTdJwl6Q%2FWqoWUBrasJ7D6pYEagKClpFxqcyZYD78kvzCzYYaaiiZjgzrjCq5J7JBjqkAbyJ33HrPoTRDHG33lYy41m5cqW9sgNiW02P56kvtQD0NofgsSqlm%2FKKE9DqXvkfclzPGZ14403lAO%2BYPGvY49IWtHpBWut6%2Bq1%2FR9jMR7OT8phlWq2bBBdg4KKlDx9tWOWlttpTUIq7phZGpkPlqCOrkDBgVkn%2BeBc418Hxx1E36S4L8883v5oX%2BIEN0Pt3e42DTwjIefNv8DBfOrMYK6TBb%2BxA&X-Amz-Signature=224bd73baf5162afeffb28e4f4f5a59b3403e7b12c9a56321b816b03bb865faa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

