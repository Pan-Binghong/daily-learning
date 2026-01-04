---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNTILK5D%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIHievAL4K6unobq3ITL4oK3YtB8K%2BLnuR13tco%2BgV4fmAiEAh8YVqZzh6m95vbgiphrKH7t4SxpurGMfTKFvcw8xJzcq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBrgdoINyadeHzzlHircA2MXgRjO7wwwilCQqiUkOn0PhPGp%2BD%2FGCyNTZv2isM4PdzPGVGPDuZwrBe44FY%2FE8xClH5WZK%2BqEUxFQfIETa5T5ZIubzjaG60dQCtFI2Zn6vjchVtyTHOCN2URtqRcoPzJ0UsX6xZ%2BAdPMoiNTdHRp%2FYwcEg0IQTVr2mWNlAgTzCzoGvL1wjkeDS6ESICaxO5lARdeGtlKp4JzSl3dbwqMGknITjYxt2hI8o6Cm%2Fis%2BPZZWtMNA8W40b0zm%2FIWxyQIp4z%2F6PRiJOjpwyumX2TINeKzzi5CZDIrS1TVvsvi0AJ6SZ5eA8oCcZ4z7m%2By8JYddDpcEMjuxmWk3SxHrDlqHA3UTVqQiqFeAprZY07b2v1cIWNxFrJhI5TQOhPc77eELwwSLQ%2FU4SfKpixm9cLROToQ6hl2GtjOGr%2Bob9tQip%2BwuL2CNKvoAvJWAcjdHiAbRm3Jxx7Jwfl5zmqrfgMknw4bhxSG7lTGcFdWdV0fuZgCHDZonQb6U8VhqXvdpUKhpLU%2FtdZxVgClFl84lejb9Yhegzb9wvL1%2Fp8%2BZn0tkCGfCVmJ3UO2iUXqfIT%2BWYLI2wrBJmuI3pc9q9tUIgRvSdNRad%2Bz7wLOKdu%2BQJkADdKelPw27BomPVwzQMMmh58oGOqUBoyks4yaSMfvs2kACvBxqgREd4n1tQtVeh%2FaNs%2FZLv2a%2BfpC3TzHQalure1ff2ZtxURfLc8Pc8PPvLWb7ciSC8cR6E49hb2eLk23kptotuNjxtqTptrJ9%2B8w4IoOcfLnPV0XSTGIGEBt6SoLUySrNDYHPPh%2FYY0dcT2ybDD9F%2BY9Jeu0LvjEiS%2BxYkaThfCm7YmdJTI3zPnv40HIrkQEyHKy14j6x&X-Amz-Signature=733937fc04a3b9ec0db1841b4fa4e09e81f59fe941080fbb5cc2f94cf18c0753&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNTILK5D%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIHievAL4K6unobq3ITL4oK3YtB8K%2BLnuR13tco%2BgV4fmAiEAh8YVqZzh6m95vbgiphrKH7t4SxpurGMfTKFvcw8xJzcq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBrgdoINyadeHzzlHircA2MXgRjO7wwwilCQqiUkOn0PhPGp%2BD%2FGCyNTZv2isM4PdzPGVGPDuZwrBe44FY%2FE8xClH5WZK%2BqEUxFQfIETa5T5ZIubzjaG60dQCtFI2Zn6vjchVtyTHOCN2URtqRcoPzJ0UsX6xZ%2BAdPMoiNTdHRp%2FYwcEg0IQTVr2mWNlAgTzCzoGvL1wjkeDS6ESICaxO5lARdeGtlKp4JzSl3dbwqMGknITjYxt2hI8o6Cm%2Fis%2BPZZWtMNA8W40b0zm%2FIWxyQIp4z%2F6PRiJOjpwyumX2TINeKzzi5CZDIrS1TVvsvi0AJ6SZ5eA8oCcZ4z7m%2By8JYddDpcEMjuxmWk3SxHrDlqHA3UTVqQiqFeAprZY07b2v1cIWNxFrJhI5TQOhPc77eELwwSLQ%2FU4SfKpixm9cLROToQ6hl2GtjOGr%2Bob9tQip%2BwuL2CNKvoAvJWAcjdHiAbRm3Jxx7Jwfl5zmqrfgMknw4bhxSG7lTGcFdWdV0fuZgCHDZonQb6U8VhqXvdpUKhpLU%2FtdZxVgClFl84lejb9Yhegzb9wvL1%2Fp8%2BZn0tkCGfCVmJ3UO2iUXqfIT%2BWYLI2wrBJmuI3pc9q9tUIgRvSdNRad%2Bz7wLOKdu%2BQJkADdKelPw27BomPVwzQMMmh58oGOqUBoyks4yaSMfvs2kACvBxqgREd4n1tQtVeh%2FaNs%2FZLv2a%2BfpC3TzHQalure1ff2ZtxURfLc8Pc8PPvLWb7ciSC8cR6E49hb2eLk23kptotuNjxtqTptrJ9%2B8w4IoOcfLnPV0XSTGIGEBt6SoLUySrNDYHPPh%2FYY0dcT2ybDD9F%2BY9Jeu0LvjEiS%2BxYkaThfCm7YmdJTI3zPnv40HIrkQEyHKy14j6x&X-Amz-Signature=137de79ba70685305a7fad53ab23518ae3fd3ab875ad0545a62f49a5291af0f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNTILK5D%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIHievAL4K6unobq3ITL4oK3YtB8K%2BLnuR13tco%2BgV4fmAiEAh8YVqZzh6m95vbgiphrKH7t4SxpurGMfTKFvcw8xJzcq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBrgdoINyadeHzzlHircA2MXgRjO7wwwilCQqiUkOn0PhPGp%2BD%2FGCyNTZv2isM4PdzPGVGPDuZwrBe44FY%2FE8xClH5WZK%2BqEUxFQfIETa5T5ZIubzjaG60dQCtFI2Zn6vjchVtyTHOCN2URtqRcoPzJ0UsX6xZ%2BAdPMoiNTdHRp%2FYwcEg0IQTVr2mWNlAgTzCzoGvL1wjkeDS6ESICaxO5lARdeGtlKp4JzSl3dbwqMGknITjYxt2hI8o6Cm%2Fis%2BPZZWtMNA8W40b0zm%2FIWxyQIp4z%2F6PRiJOjpwyumX2TINeKzzi5CZDIrS1TVvsvi0AJ6SZ5eA8oCcZ4z7m%2By8JYddDpcEMjuxmWk3SxHrDlqHA3UTVqQiqFeAprZY07b2v1cIWNxFrJhI5TQOhPc77eELwwSLQ%2FU4SfKpixm9cLROToQ6hl2GtjOGr%2Bob9tQip%2BwuL2CNKvoAvJWAcjdHiAbRm3Jxx7Jwfl5zmqrfgMknw4bhxSG7lTGcFdWdV0fuZgCHDZonQb6U8VhqXvdpUKhpLU%2FtdZxVgClFl84lejb9Yhegzb9wvL1%2Fp8%2BZn0tkCGfCVmJ3UO2iUXqfIT%2BWYLI2wrBJmuI3pc9q9tUIgRvSdNRad%2Bz7wLOKdu%2BQJkADdKelPw27BomPVwzQMMmh58oGOqUBoyks4yaSMfvs2kACvBxqgREd4n1tQtVeh%2FaNs%2FZLv2a%2BfpC3TzHQalure1ff2ZtxURfLc8Pc8PPvLWb7ciSC8cR6E49hb2eLk23kptotuNjxtqTptrJ9%2B8w4IoOcfLnPV0XSTGIGEBt6SoLUySrNDYHPPh%2FYY0dcT2ybDD9F%2BY9Jeu0LvjEiS%2BxYkaThfCm7YmdJTI3zPnv40HIrkQEyHKy14j6x&X-Amz-Signature=f36797e57c67d911a35bff05f8ceb7f850edc02e01e569f757466fa6844bfcb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

