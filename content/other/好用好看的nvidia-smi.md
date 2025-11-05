---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
标签:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S3AY7ET%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEnVmyRS%2FlWwqmB9HIBcq8%2BuEw1WSiMpA98U2RsooR1KAiEAkBF9sBRO91LOvaJPzrr%2BBb5j53P38NVDnsNbW5zTaVwqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGz4uvsYnIWiFtxG%2FSrcAzErWc4sbiR22wrTwzrInYb2nNO6JkjzmB%2Fs3G%2B%2FMwBNz3Vab2egh4S3mndpKOhnd7maD7SpdHoKbB305%2B6HpkhbkzC0lhBMngIdB8y%2F%2B0igNwkBsWB4LC24iN7QPlEpIEtXVEG%2B%2FAVUVMug9Rgs9eUU2HN6dbcEV85cQVuJ3weAsEFX5KI3rhmqCP9PHx1qM%2BMQP6sHrBV%2BJyxhJrpknseS%2FsE46JDGtMdgF7SCUxM7dPDi6vaTECXcq97tPEfr6qJgwsMP%2Bs%2FFPO8zE8rxSSKCMUKyeyNaXgwhquJt6Ulpt3SmeZBxc0dcH2dyV%2FTUC5FSJ6U9bwpJvYo6KWcsRA4QpwMLe65%2FHf2YQWUSEr%2F%2FMZ5AOOTa72qF%2Bz0DCOMT5szpJYnLRTzM%2BrCJvsN1%2Bjc9vjzOcZ6gZOnInn7%2BWBerb%2BuCS5Si4OYGvt54IvJL5y6Sh60%2Fr0zQ8aWpPq3DNS0oci9P8Bt8xSXd2ini4uiztmztPqTVOPtmwyrjcyGa16GpBE79wX0iSKOIRRDQ0wsYf0m9banw8G4JoD8C7pEEooD7Yv3jwtBwylLeG7cpwWQtrZZ%2F12u4HM5on9R5c66GWnYJaxAEOLE4MQBl%2ByR34npfoN3RHnS9lMQ8MLqjrMgGOqUBTwLADgG1fUFDlYTl8rZv1cAkVvAymqXPuaJyIZBFixekv61SMOm2Gk5u9ftYQhbgQ3PeMmhhT%2BtEwJsOY7zNem4iKwjVwGe3rdYVG6DDTyP1v5O%2BnAxi4d%2Bv174BD6q8mp%2BExRjFeuJ6wROHwqssDR52U%2FROPT7wCpK55LzErXRS1u2fzfqXaIn3PR%2BZ%2Bnxh2OVgIX4huxqoeTNZDZjIP%2FV9f4g3&X-Amz-Signature=602d5ef3efed9351e97929b9d43472ea1301000d66195065311b68dda464b1cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S3AY7ET%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEnVmyRS%2FlWwqmB9HIBcq8%2BuEw1WSiMpA98U2RsooR1KAiEAkBF9sBRO91LOvaJPzrr%2BBb5j53P38NVDnsNbW5zTaVwqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGz4uvsYnIWiFtxG%2FSrcAzErWc4sbiR22wrTwzrInYb2nNO6JkjzmB%2Fs3G%2B%2FMwBNz3Vab2egh4S3mndpKOhnd7maD7SpdHoKbB305%2B6HpkhbkzC0lhBMngIdB8y%2F%2B0igNwkBsWB4LC24iN7QPlEpIEtXVEG%2B%2FAVUVMug9Rgs9eUU2HN6dbcEV85cQVuJ3weAsEFX5KI3rhmqCP9PHx1qM%2BMQP6sHrBV%2BJyxhJrpknseS%2FsE46JDGtMdgF7SCUxM7dPDi6vaTECXcq97tPEfr6qJgwsMP%2Bs%2FFPO8zE8rxSSKCMUKyeyNaXgwhquJt6Ulpt3SmeZBxc0dcH2dyV%2FTUC5FSJ6U9bwpJvYo6KWcsRA4QpwMLe65%2FHf2YQWUSEr%2F%2FMZ5AOOTa72qF%2Bz0DCOMT5szpJYnLRTzM%2BrCJvsN1%2Bjc9vjzOcZ6gZOnInn7%2BWBerb%2BuCS5Si4OYGvt54IvJL5y6Sh60%2Fr0zQ8aWpPq3DNS0oci9P8Bt8xSXd2ini4uiztmztPqTVOPtmwyrjcyGa16GpBE79wX0iSKOIRRDQ0wsYf0m9banw8G4JoD8C7pEEooD7Yv3jwtBwylLeG7cpwWQtrZZ%2F12u4HM5on9R5c66GWnYJaxAEOLE4MQBl%2ByR34npfoN3RHnS9lMQ8MLqjrMgGOqUBTwLADgG1fUFDlYTl8rZv1cAkVvAymqXPuaJyIZBFixekv61SMOm2Gk5u9ftYQhbgQ3PeMmhhT%2BtEwJsOY7zNem4iKwjVwGe3rdYVG6DDTyP1v5O%2BnAxi4d%2Bv174BD6q8mp%2BExRjFeuJ6wROHwqssDR52U%2FROPT7wCpK55LzErXRS1u2fzfqXaIn3PR%2BZ%2Bnxh2OVgIX4huxqoeTNZDZjIP%2FV9f4g3&X-Amz-Signature=6187e5397968d2c474f5112afd906b0bd7324c8946e22f928a66796aa6530ed3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









