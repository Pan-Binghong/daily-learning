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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS57FOIZ%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICziW%2F1xl8QJMxEmjEDtQJc5j1czXYposj5aNcVooKaHAiAmtFO%2F1NuP6JX9QEYiNVYSU2T18wQ85BIQfcGMgHWDsSqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF9pGoZtvA9ipf%2F9pKtwDHDA5Du4AORpA0%2BsK4MiybxUlrvK%2FoHoJYXMCO7G2nvu0xWnUay%2Foi2swVn4MZ1YTqf6KDCwijfnVPKA3lX375udcVs8H%2B%2BwAN9PRPbSdb7HY8d948o3Z63INeC859APFaWAJvmKXqILaGPaM8iJfMfCY7OyduD5Ygid3bpEwcnu%2BdCknyarsZkAvJpsw0WGQYEaNHRS%2BTfobtjy3Eik2gbvBH029TmMSNR%2BEBef6pR4%2FJ5vrJ7rPkeEpoH6hrjNwu1Xv%2BKDhMLcsvbQ2e66Nru1ZJVuPXtoXPcdGQp59QB%2FfUjeaQvWSSVLZ6JZW%2FFn%2F4dPq3A%2B603FEdCQ7gBRs5bC70v7LhPVFpULSZ4hHDJspMfBc1oRTmWkcsE8R5%2FQGOt2INr54yAwK7I2yJKQAQm8aiSYAjwiNKy7bLzQ6CRbvd%2FHFCyajoHDcaXWRf1XaVNKvc4kqOISe84%2BWEbyOJiBl7z3uq1Sat%2FB8S7%2BS3yRZjT0UtDZ%2B5GClwI%2F6kErNB79lY5R%2B%2FsSmvwxxiWLNWkSfmTdROvvpFlQVH4FP0EyYwVsuMSpQ6ywUD2mtcbunqBZRlzQhL0BM1ee%2F8nYGfVci%2Bd4Y2cg2nmjLuCENC1dzJBFXPEkYQOMA%2Bb4w3ojXzgY6pgGqs6m%2BZ2FU7ix0H%2F9BIEET%2FRX7o%2BgHln8nvo%2B9Qgo%2BZpjPZsC%2B2vB048zB%2BCmH0GHMw5YJ0RTy5r55WFSflTErd6ucRuI6kufkLFa27v02AZxQi0qwJlajz9bAWGdMbnCq6j1Ooh6%2BBFIm%2FTE4tSQZeqVSCmovb6do33WqSeqtupobtnIQli%2F3AqNsp8C0RzHBk1Snz3wGPbmWsze%2BEOfJaFz1RJbf&X-Amz-Signature=ff623029b8d4e3bb9d026eb68cfce8d48563289c9b2555520916296d68ea41cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

