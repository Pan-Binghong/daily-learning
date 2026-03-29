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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5A5KQXH%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIGzknFBGjz6VYjZPb3G0pOkVcr89cx2jsQSjseoGhsK6AiASKw4yuHrC8l4nlmMExyiD6DuF8iYk82iTxQvDbt2zsir%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMebGvVCKjulx0kyxGKtwDh0r%2Bvz1qS1aZqPxwTKfQNIJ4qcH%2BgUClzNB6jhRiukMcWnwZHpKDiWS4CA8W0sU6UVGcHl6Uwo68YZM3fIPvsO11b8J4MsvKr8RkwyNHBItCL4c95d1nvRFa9v6Xz6XOFJ6hsTyezPz5mcQrr4QZfrCes%2FTND3mlD117DRz2As0t%2FvuqTrhUzctGxOobbIgmXqEQwWx7S4DmKJTa2zPSQb7%2BL2mYUbxm9rq1%2FVLDPvwrt4tFakf%2BlkJFaKf%2BvZ477j%2FyIUq%2Bg5av%2FzpyGEjnu4GPjDvQiNppnS7H7%2F3IvKMSkwPCaUfhz4lFtHLtBlCxCVpeU%2FwTKJQeJI3UG8U6RulGkl4H09gOWB3H3Ldfx4RomU8iV8R7%2FGMUGvSDilqntwyqFa9XZIpFXPgvp3K6gwt5AF5ifluUHxL1iTxequthiK0hpO2LjWLs9roMbHOg5G3tcbOkAWmYjJvV5UodNQdod%2F5LK5RT9Cb6%2Bc6NdeKoSvmDYt3B4uz%2Fzz%2FgSzjigpkL6akIhs1O9W%2FzRDcrRv1xwPHsvLOTt110%2BKr8ai2Stcv%2F%2BqFfGvybcReUyDxJsgjoaGHN4J24y2qmr%2B%2FL5xF4Vz3Muj6vS6SVUFryX4jVKD6Bxz5DQdLfqyIwg76izgY6pgE5sWO1wsT0kytjKDX2YkHla4ZjeT2lveD8g%2BqOOb48Jkz4cHK%2BMhXEOL%2FXXlXN5zGZqoTlTB30E6hVP5uVA4buJUB9vfv4W2kYdxpnFFHAEK7hjeULmLAGE7XdFrukbHuesYn4UadCU%2BP5SM4DE1NGRk2SdDK%2B2rfopFJIRRWON5hKtKrDl0rQnvHVlwoxqZKx0RXxyllsEJQQkF8CyXSFBsY4HV3c&X-Amz-Signature=bdccce082cce9024927b4cdfabc00575ca706cb4c4d6b565cf046cf1d0ae2323&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

