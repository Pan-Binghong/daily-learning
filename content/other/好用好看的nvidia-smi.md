---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KIGBXBM%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQDvG4xUErNo10S%2B2ljCsvFbab1UPeRV98R4NdneyvrmQQIgXrVCBWqvBBjN3WKVGbKy13Rq9DAObATHen5IfZyANo8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNXpgxN6CtCzX8yhqSrcA1GBUwy9WCljB2UXNqgIjrpAbm5Z14jYAs01jJWbUaL4Gbj81woZAwDoQGpwcrrwuQieRbwKZ5f4%2FoZxDM879Qz4d%2BIIs878ywDHLWpM3vlGPxfLlf%2FhJghScel2WbI3xApqht0HH7JRw3Y2aIy1961RwAsMzF%2FjvDLqy00fVbHZ1EapMZawcD8PW0JrbAzoICaqnM3OUR0NaReF9p4A2jSYcgOH0PB557VdOIr1VSd5zwsacwDLVxgMa5Hs%2Fhi2kfBaAaUIyywvsRH0z%2FMeTKzVV5UmAloS5kudP24RDxO6rmd%2FboEm7Pymgz4nuo4NMpfu581RZ91t%2B6muDkgWLC99cHjPxsZvAtr9LsEJCpWC13r4lSZZZf%2BJEOV84iOQtjpMpLJ%2F3UkRjYueVj1MPdgU9LCwQMIBcgs6%2Bi1R3sbmgv0ncol0GJyGSCXrnCSoywlmTSFYzPSHbTEJlZ7cdMWqBE9442DcnJLZSKsY2cvF%2FzNLLnaKuRCzdr95VAfeSNCGfxEtKypGh%2FhheA3P6r5K7jOTcQBdL2019MFV58LzuStk95EjTKQKwjBTrMYhnW9O%2B9K%2F3K9xWyHHurh5%2FA3SqyFuTzBFRxXxwy8u79et7aREA5qfFPdBYbSFMMu19MwGOqUBa204SXE2X17j2G%2FaH5wsRmzxG%2BD8nyvXYzIXpJRnEcXZxnqufQFZLEuLnZ%2Fi3ypSmA8A9Y1IuBciSBDjgCpZa%2BcjgCV9w%2Bs7rXpcaq57Cw%2F%2BktMrrwQ8H%2FPZ%2Bf4cA87Frxv27psF4jD4jXWjyeO%2FU9HXxWRKZPpWxK5DEWVhhNidbmOHSeyE767p4wC4crw81vdicG4gjPGMaVhdZFfFwGudN29x&X-Amz-Signature=b51d49989b143d4b8b7d3738348c95eb45ef1ef2cd3bc5e1b0ddee3a5c9e0a8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KIGBXBM%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQDvG4xUErNo10S%2B2ljCsvFbab1UPeRV98R4NdneyvrmQQIgXrVCBWqvBBjN3WKVGbKy13Rq9DAObATHen5IfZyANo8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNXpgxN6CtCzX8yhqSrcA1GBUwy9WCljB2UXNqgIjrpAbm5Z14jYAs01jJWbUaL4Gbj81woZAwDoQGpwcrrwuQieRbwKZ5f4%2FoZxDM879Qz4d%2BIIs878ywDHLWpM3vlGPxfLlf%2FhJghScel2WbI3xApqht0HH7JRw3Y2aIy1961RwAsMzF%2FjvDLqy00fVbHZ1EapMZawcD8PW0JrbAzoICaqnM3OUR0NaReF9p4A2jSYcgOH0PB557VdOIr1VSd5zwsacwDLVxgMa5Hs%2Fhi2kfBaAaUIyywvsRH0z%2FMeTKzVV5UmAloS5kudP24RDxO6rmd%2FboEm7Pymgz4nuo4NMpfu581RZ91t%2B6muDkgWLC99cHjPxsZvAtr9LsEJCpWC13r4lSZZZf%2BJEOV84iOQtjpMpLJ%2F3UkRjYueVj1MPdgU9LCwQMIBcgs6%2Bi1R3sbmgv0ncol0GJyGSCXrnCSoywlmTSFYzPSHbTEJlZ7cdMWqBE9442DcnJLZSKsY2cvF%2FzNLLnaKuRCzdr95VAfeSNCGfxEtKypGh%2FhheA3P6r5K7jOTcQBdL2019MFV58LzuStk95EjTKQKwjBTrMYhnW9O%2B9K%2F3K9xWyHHurh5%2FA3SqyFuTzBFRxXxwy8u79et7aREA5qfFPdBYbSFMMu19MwGOqUBa204SXE2X17j2G%2FaH5wsRmzxG%2BD8nyvXYzIXpJRnEcXZxnqufQFZLEuLnZ%2Fi3ypSmA8A9Y1IuBciSBDjgCpZa%2BcjgCV9w%2Bs7rXpcaq57Cw%2F%2BktMrrwQ8H%2FPZ%2Bf4cA87Frxv27psF4jD4jXWjyeO%2FU9HXxWRKZPpWxK5DEWVhhNidbmOHSeyE767p4wC4crw81vdicG4gjPGMaVhdZFfFwGudN29x&X-Amz-Signature=44595b7cf142e1db319c3c7ac1f1fe4060b58f08935748a570082b136046d742&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









