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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBLSFZSV%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDl24aTHgbMzijmi%2BEvOhvOC%2B5vTgGjQ0v5In6ZVWTbGAIgSEVMLhoq%2FY2tFf%2F%2B6tpLRg0fGxizBJfBrWlarJvOwpkqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtNWEuMqXvnkav9pCrcA9rAUfPTrbeHM9nZPiArWSso6m4iot60czw%2F8Fd%2Fx3OP9ros7%2F5R4tVDQ4kdXTMxEmXfnQHReG113cSy1ytStdscMJQPCEkrnGvEex2qzNeVS8Ya%2FC6k0vR0vpZeWEEWsgKW6245KH5JL0k8NfcUDtJ8D4JWXMdqq7wFQb%2B348QjnUfY7Xgt8DwXcPxar4u7b7YjFkGOhI714DF44mXntrsNTKp%2FYwn4J7FKcaiY9qVNWbLLHjD1mHDR%2BUrRe9m%2BNmeGsGlhwlI7ZlzWUccvie%2BNqrK9yMtWz6Nl0Se8LvBPE7qVMzsxHu98%2BVBn%2B%2FtQQmHNfRfcV0b%2B%2Fk9KqCeLIji2ee0JkDHmYGJplAZkx2oS%2BPp4gokGkuzJAGMTPIhCSEXKT5asjviolHG4Atx8oPRoU%2BT%2BzWnQ3eRm6r31lUjObLtrE4E6cgTMmJIATlBzTVrzXdTlUZratUeq%2BCuXVndvTiiVlv3x8lbvWWh7teTqMCE2i45i3NcyoKiLJ5Es7cCOV4xW4icNgv77XZWV5DUEx5V33iIXf%2FZSazw%2F2egTXmIOcXg1vAtkOdSov7mGInwqmf2f334EUxW83zrXuza1VQirA4aqcFopdUdJm475SnaKtY3DkgPT7z6lMLe2gc8GOqUBJnrcYrC%2Fk5Y7%2BwJRqLxo4KjBOw6uCHf32K97Em7PXQFN9QEmeJ9QneeBeEIo0er%2BdohbkPdOIg6WmjLCLp9acFCnlGRMoGhpPDmwfwVX29qzP9wkCU3wTvDGRTP1ZEdKQietHLmePGyHCFsVUB5W2eL5nE%2FAGTDrvGI6rm1joO0GCbeYTWyJBHIp6I1vxeFF8DWaokWc1IoQVv%2FtaH77v2UIQ%2BX1&X-Amz-Signature=f0886ec211d9b35716c5fbf3db6fff608fc16243e1f1ec2ad40f819da936402b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBLSFZSV%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDl24aTHgbMzijmi%2BEvOhvOC%2B5vTgGjQ0v5In6ZVWTbGAIgSEVMLhoq%2FY2tFf%2F%2B6tpLRg0fGxizBJfBrWlarJvOwpkqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtNWEuMqXvnkav9pCrcA9rAUfPTrbeHM9nZPiArWSso6m4iot60czw%2F8Fd%2Fx3OP9ros7%2F5R4tVDQ4kdXTMxEmXfnQHReG113cSy1ytStdscMJQPCEkrnGvEex2qzNeVS8Ya%2FC6k0vR0vpZeWEEWsgKW6245KH5JL0k8NfcUDtJ8D4JWXMdqq7wFQb%2B348QjnUfY7Xgt8DwXcPxar4u7b7YjFkGOhI714DF44mXntrsNTKp%2FYwn4J7FKcaiY9qVNWbLLHjD1mHDR%2BUrRe9m%2BNmeGsGlhwlI7ZlzWUccvie%2BNqrK9yMtWz6Nl0Se8LvBPE7qVMzsxHu98%2BVBn%2B%2FtQQmHNfRfcV0b%2B%2Fk9KqCeLIji2ee0JkDHmYGJplAZkx2oS%2BPp4gokGkuzJAGMTPIhCSEXKT5asjviolHG4Atx8oPRoU%2BT%2BzWnQ3eRm6r31lUjObLtrE4E6cgTMmJIATlBzTVrzXdTlUZratUeq%2BCuXVndvTiiVlv3x8lbvWWh7teTqMCE2i45i3NcyoKiLJ5Es7cCOV4xW4icNgv77XZWV5DUEx5V33iIXf%2FZSazw%2F2egTXmIOcXg1vAtkOdSov7mGInwqmf2f334EUxW83zrXuza1VQirA4aqcFopdUdJm475SnaKtY3DkgPT7z6lMLe2gc8GOqUBJnrcYrC%2Fk5Y7%2BwJRqLxo4KjBOw6uCHf32K97Em7PXQFN9QEmeJ9QneeBeEIo0er%2BdohbkPdOIg6WmjLCLp9acFCnlGRMoGhpPDmwfwVX29qzP9wkCU3wTvDGRTP1ZEdKQietHLmePGyHCFsVUB5W2eL5nE%2FAGTDrvGI6rm1joO0GCbeYTWyJBHIp6I1vxeFF8DWaokWc1IoQVv%2FtaH77v2UIQ%2BX1&X-Amz-Signature=769f30c31b08c5eb0810e09d6e0eb6695065fcdd10ba342d278e1fd06ee6dabd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









