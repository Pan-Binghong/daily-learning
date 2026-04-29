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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QOLYOT4%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQCTNoWGJLtptxS7SqXuJJ%2B0C0pHpnCsvyNfuaUSTTuT%2FQIgZYyg2rQTETW89Bu0d30j3KtNO3%2BHByYQfgIATkx5MbQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAdaNNk0SbY1glN4QyrcAxbTb2kqhl8qcz%2BKkejtEVzlZiRoHpU5kERrFLMwbuHyp%2FBNpHqw%2BVTboTuw5ZwRQHM7SM39F%2B4dnHgoWtgqLlo2aLHfyutC7VvXF3mgD2LZF0t2QSQRBLA9gW%2FRB2wvcg22NQrR3df6RFhxOJIxvklD9CgBiMSaYw7hpbCZ18W6LHogLDn4UTrPqJBthuzRKd1tTQnMFcRQM839lln8aJxfD6CrZ6fsXeKV0dRAPs6xJQ8hG1jocjYz3PEM5hQ8r5gIkLcPcNscfaFzy3nbobVa%2BBLn8AbSmqSEbXaeFZae4IF2RkeEjblBd8P5G6Bb53IKbuT2uuxGYjpjdhFaD9zBwIZbXGYEGNPV5DTL7Gdu0m2xmvGYtpPkdBS6%2Bs%2BrSTcyPTMfz%2F%2F2VHa7U5Wb38Qke08GKrzRsDoVVyGSxgb0RuBki5%2BYygQBe%2BD2WEzw%2F1jcLpBZQtfBNdIZcKNxf0UiIEwZVtDubDCj8sYwTs2iGwkzlu5AwF4ObmNdt%2FoqzqwY06Q%2BP1zN4bQP5WWmQmiUDskJeh5YBPZtwqZeRdrXtehOBN8jZrs1afmVyop0QySEqaT0aLN3aTG6zBbwKwQEd4ASYDqWjwIvCCfFr5FdvV40QqyB%2F7exFbsnMM76xc8GOqUBupqNg33mhpthSfK89bro59xHGwv9LC7H2M1O91jyLj7aTZohQfVYZH9FrX4q0R9Ib13ESX3yCXppFjmumK79RhnW%2BBw7Uie15HEkm1pAUgEmEcofisuHVIewG%2FspiwK7LEz2Nl3QeNNRuYAfbEUj5c6m%2FYzX1YUh5i%2BoWJhForV4bFT5xUvZrqmxutf%2BwhkVy1QqaAbcE%2FWGhJdJQef1yU2kZHVb&X-Amz-Signature=623afe94455928bb5338e5126a4f05dea08e4f303ddd0beb09d28fd5f856d7c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

