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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WA4URA3%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQCqSsAzNbtGYPPwiBHCT%2F2ta1iM74UnTVrV%2FxeJl4DRIAIgBtjjhnhdnsQSwyh32YC%2F6YVt5T7VF1vOzVMfMyOEpTkqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNckJIyrfAFa%2FiVB5yrcA6TtILSdS9iOKKVFpzPBt2Pt8mEMvilMnU4aQ5mhDg42swYXBwKCjWjgvkHXoc3C8GU5ToO6cZBbDey87QjssyHdsyY24rHhG7uhzV%2BMBNLpS0AGNEoE7Ocmi56SopXsaLXcWEKyCzWVtzQsOhwHgh2PtjAMond1QH%2BTSi9QR6OGEN0BnXeSp0azgJSRKk%2BIxr426Z3qStYimIG8C14xCFUqCmq8bwknBYTaM1qF1l%2Bep8NI6aT08kpji1aPmW7ilyyLUw9BmShshvJT81iPYs7MwelaWzXLcQCwCKY%2BVurCdLygycwgjHSVJaiqyKsaY9%2Bi7DlD6iOY0a2wMALStZXhyHEQ8aWID6NTpRRpyfTWWkk%2B6dFNNSq3NcAPWdKXBl%2B%2Fsqk1qNAVEgb7Xvb4m%2B5Bkzfm%2FWIyflnXtnpuarYGjMuZ7hO4tbcu0eTvOdOVKrWHQFHyfiABx4a8%2BzksdAPa3pVWa8V1gPIcZLK7U43brFeeldm222TskAIHhI9SRl0yozFWBqx%2F%2FPN7LB0yjbwU3WpKIAcHPl7pB7%2B01IISDSlMMNdcaNBzg0RXlzwrTaRPYEYzFu4EeF%2BYtGGpk7%2FpEdh2ps7CYHmksxqhOayyyB3a6WGmOxq%2B%2FyjvMIvJ9MgGOqUBEHnYP%2BQUuZo5eC7DX4uWttSw0KyiaQON1%2F89CbgJtd%2FP7YN3eIzv4EJI4g0i1V0ZxN6sUBtC015oL8equve2fz9ORsPMbX6wnlcP%2B4oYMZLvcStG9C7C6QsiyEbJ3Zhz2K1RsVD3bIg7bW%2BSeq6l2eQrTW9hpf1us9MDGpJPWju%2BP9YIYeRD4gC%2Br16b13UqV3TzUzrqNjYiaHlDlkzEYucCbk2%2B&X-Amz-Signature=3c34b2e515d0458c061d56666850da06d68733dd3e19808fb1d4f9c69737d150&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

