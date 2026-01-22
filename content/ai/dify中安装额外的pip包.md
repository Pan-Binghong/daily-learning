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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP3BRSGC%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIBjYP3QVdJHpzE092qwyNN8fb1%2BPfydSkCn5QiVjhA%2BMAiBQAQshdVktzNRAArqaL%2FvZ1qRzUt4KogOkwPN1zXHTDyqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMP6m1XZrg%2B9%2BAJJ47KtwDU3txmL6zDG%2FWJ%2BJsKg%2BFYE%2Bv6V%2F%2Bju8devX6bOabWXIW2XIkMMPP7ndt0QCHnW2n6QlnCftzmDgBPM8aleXue44U9rHZza6Wd8utaLn0rs7IEov7ops%2B23qIgp%2FmFk4aVzbhbfQTdupjXtVrmb0aqE2tz0LOMEDkI2pWSVu8IeqHjzMT2dSPiUeYf6NK8%2FsnO5zy5yE5LwJW1oDuG%2BnjIp0zQMfUD3TmrhukkT5fq7hMp6MEl8YSS3yAqAud%2FlBF1u9WNu5Uo3zHvcj5T5pU80ik3trdfv6895a1xy9e%2F9RD2IMNqP1Bp%2BE27mtX4V9PmB2%2FFbI%2BwMQaHjMvmYSw6poamj08xgaG%2BBuKaNAdCaOiU1NlTZwnbKj8Y4fJqtYU8sqiKyl%2F6m0mwGjALybkaJM1m8u2zMq%2FkODgij2RrlQ5xS0mDETOLLgF25HMmf1W61XxoCHa7oKVFMWRezM3rjWMA4Ec0WYYNUxffxeni0498CElVfzBlQ1npZvhQ4Gs7dEiOFe5O%2FvMibQXCE20KlEpiZOWNTmnTCosxfpWSHRX60wPyz%2F70czL5mGcIzMEV0OrzcGcSSlgH9%2B3Fe3xFFN2JdqDpa5Ztry1a66ZExHEjIJd2GCkI1FWJCcwlILGywY6pgF7b%2BF0YMyaYE4e7RzP3v9DEEf0fq3Bpe2YFOP5LB82EjmiMC4YBjQFAxzEilWLbEVoOujWpWWGZJDNXdTd9mq%2B953LilfwzcAJlMGL6zbTFB4bvBklR2l70pYAq4OhhhXzuRmNpo3pTDldlJIJdpPz%2BQsUiH2oRtsxPAqPoI%2BzPHtUH6KkrGZ1vi0jyQQDh6sRDbAlEOZHaOoKFiqzccglqGxiuJuF&X-Amz-Signature=1391eff91c8235527f707c0c8f89866d1b1f627dd029ca5f1512d712c9eb6398&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

