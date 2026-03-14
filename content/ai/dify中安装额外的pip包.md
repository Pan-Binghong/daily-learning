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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CR3GWLZ%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9uxvRlsmrpkUpkXfilkGRhTgtI9GjxVgumN1u5m%2BiJgIgIbpeJ8htQk9JS8D98B69hkyY9Gjl7b0je9k1sw9kugUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIwgCkBH2gV0FBL7HyrcA5FbUXb7QZndl0koBvsVOTKCPTQENoGzUdtLpvOECaNIp1GBNoV%2FwuGPjsigJe9zuybUsFN9HSjFFJFUHaHYLhetB5KHrWxReEyT%2BE4obJVbLKtz9mBS2ti3%2FHS3iEAyQ0yxQhzygb2KoukxJQGmGP5TORc2MSwyBgCQsCixTTn0AeSb6ccUmdb8nTerPPykBGu1yx9uNZiczloD%2B1%2BEXrJudEGtmukSy6m6rWPt%2BRXVaqB0F2VNtjRPDIfl79omZtRKYu7Z4uJXGhhMrBRQxa5Rhq7167WzAby4WxtQUKL4ougo7MqRX5nNTmZJv1UxgXEkRjieAupHU%2FGUus%2BZc%2FnJ%2B%2Bgg%2BSRdtXa1Uu%2FZxR%2FnFUdrkFAfZkC8H%2FABR4jArXJgO4y1tzop5kFnlhBFXCHMM17aswOqXDuBgbuH4TamfZfdPabRG9ySsorlmhh5JsbZq7%2FhYdOX97XCX%2BKr4iZVAAWruB4chouc4NrDzCdGfWLA7FzRYv0KfCzT7C0YB2lHRz1n5Hr4Pree6g0OUWfJVf0GhPHKe1mZHnhAuI7fienOeNgdNWvVzWdCz7Pf1hmkP1acQzE1ioCR7jwO%2FgxgSCt5qhTxFraww4yle3mAZHjotE38O5QboXwYMPSC080GOqUB2BXbq3qm66%2BqKmfU9qa2ladsOWeRcmAXu5XT%2Fr4jGpIey4%2B47WDOHOFhAH9oNgaS%2BFCWeezqcTO2mpFFcYQMYZaUPQZVJfkVIQAjZ4rFEgOV6anQCbJsBRvj49Lkm4Z2MXsTFdcpXIxU%2FTc5AUunVxQV%2BUFjyBRTstngUyw8W59SqoN43%2B8uz3eXHhyqtKdH2C7JDOBJSpEXTwEYSRv6gj2ZczBu&X-Amz-Signature=d8622c8a16bbdef2849d769ba79f6f0da3a6b4850cd08d95a87ed6c46bfa7bdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

