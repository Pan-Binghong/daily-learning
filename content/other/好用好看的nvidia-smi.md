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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CP254HX%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC03SO2lzNS7p1pfYNAerRBWol1d%2Bf1Q8aoyM8ulYrgVgIhAOZ6AFCfsgiyHyjeJyNxGsCOnctUOz3ymR2uKQr889bRKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFacSZhncQrM3HWckq3ANPOCdMAeXzTsMyT550uzr2paVoFBh%2FTGNh2y%2FD2Bdk6xxjHv0U6ayM%2FE%2F1R2orl58NriS1FrUUmaeDQ4L%2F5oMWUsQUVCG9f9MqfIguiH3qcIygL0BZjpJot2ZbxM7c5%2FnODuIVCHJ0qxXzmNkyPh102d4AMNEewF4Mm7vJbrZWseZS4pUJgAuK5i6gc3KQv6AHogih2Dy1y8h3c2QukRghXirB9TZaYndmcz0V4qC%2FvolZBaz8vdzn0ewq3Uve5yYLU5MVb0s3ogTCKXYKy%2F3piD8eUfpu70ld2Uasq9TmEtemHC6TTh1KlcKJpPHLqe%2BVpGxzIDgTm1I6CKg2h0OFqAYyFXes0JepgDZJoeViSXiowDcG2dcMsN%2BpUDvBGYgHYtYHQdNgNHx%2BsOA5TYEen48qkIfD5H0Bsbo%2Bc2fpbaeJkUbWVKaFRMOqzLf%2BOkTefKeOs1m15r4V68Dh9as5aue6uOh5NB%2Fd1aynv5yhV5roJaoF7jNQ4l9WYKMBMWYiVql1wyOvqkjdBnkbae4G8E5VTeEN2Y3HFlnjOTJ0BORupGefupCafJjiQaj5qvLOFTjouEobEJac65kLPmsEi5pb9K7IdCAVeFZ2nyZgigrY36Gy7GRWhhPjsjD484fOBjqkASdSPyIRwXrmBjT4XPfJ7vDGGTS%2BV3XNwDHjt2%2Fty4qd6pRmruA35yoI9nuVeiZ2MYvWoqE%2BVVm7sZ7rchwwd935o9RcHOwReIHwOlHInXbCfQHg5DIE7L7TpGQCr5m4ymKKUoES4DlFBUlTo4kw%2B4bzr%2B4IbRSUegBaSawA6jDYu%2B9NnRScbQuuLBLmAySpsGm179Q9MuQe4C%2BcpbklI4ib0JT3&X-Amz-Signature=8a987458547cd3f29b61417dbfb34c435c9b18dd7925c6dd6f7268f3c313693b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CP254HX%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC03SO2lzNS7p1pfYNAerRBWol1d%2Bf1Q8aoyM8ulYrgVgIhAOZ6AFCfsgiyHyjeJyNxGsCOnctUOz3ymR2uKQr889bRKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFacSZhncQrM3HWckq3ANPOCdMAeXzTsMyT550uzr2paVoFBh%2FTGNh2y%2FD2Bdk6xxjHv0U6ayM%2FE%2F1R2orl58NriS1FrUUmaeDQ4L%2F5oMWUsQUVCG9f9MqfIguiH3qcIygL0BZjpJot2ZbxM7c5%2FnODuIVCHJ0qxXzmNkyPh102d4AMNEewF4Mm7vJbrZWseZS4pUJgAuK5i6gc3KQv6AHogih2Dy1y8h3c2QukRghXirB9TZaYndmcz0V4qC%2FvolZBaz8vdzn0ewq3Uve5yYLU5MVb0s3ogTCKXYKy%2F3piD8eUfpu70ld2Uasq9TmEtemHC6TTh1KlcKJpPHLqe%2BVpGxzIDgTm1I6CKg2h0OFqAYyFXes0JepgDZJoeViSXiowDcG2dcMsN%2BpUDvBGYgHYtYHQdNgNHx%2BsOA5TYEen48qkIfD5H0Bsbo%2Bc2fpbaeJkUbWVKaFRMOqzLf%2BOkTefKeOs1m15r4V68Dh9as5aue6uOh5NB%2Fd1aynv5yhV5roJaoF7jNQ4l9WYKMBMWYiVql1wyOvqkjdBnkbae4G8E5VTeEN2Y3HFlnjOTJ0BORupGefupCafJjiQaj5qvLOFTjouEobEJac65kLPmsEi5pb9K7IdCAVeFZ2nyZgigrY36Gy7GRWhhPjsjD484fOBjqkASdSPyIRwXrmBjT4XPfJ7vDGGTS%2BV3XNwDHjt2%2Fty4qd6pRmruA35yoI9nuVeiZ2MYvWoqE%2BVVm7sZ7rchwwd935o9RcHOwReIHwOlHInXbCfQHg5DIE7L7TpGQCr5m4ymKKUoES4DlFBUlTo4kw%2B4bzr%2B4IbRSUegBaSawA6jDYu%2B9NnRScbQuuLBLmAySpsGm179Q9MuQe4C%2BcpbklI4ib0JT3&X-Amz-Signature=9c8ddacc2859107926ede4bab8f01116ce7557d1b8f8241d56e62a85967b2291&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









