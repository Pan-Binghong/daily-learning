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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623UVO4JP%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T030022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEul1%2FJhu9ULgHpFvpV6yXenoavqT%2B37pdcn70TyP234AiEA3hBCCqRCA%2FCdzONWlzMIRDUOVOJimY8JPVMJQHIfT3QqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhdJ%2BsuAaJlOS%2F3tyrcA00b6cvYQvmsw0JaaN18fEQ1Ttwur%2BHjPI3bzJW7PgZwzyW7rT7uJX8bXR%2BXJAa7mMNPuSSwvCMfvP%2B3UfKpY57GndVakh19zHgL2nBuzaZqJNwY1iHA693E%2F9WiGb1H9wJFgsxTJjrChdq%2FoYCqfp5SHaruEA%2BX5Ad6GNvns9EYYnENWHq%2Fuy13ZUy93aOFIddKk3d%2BM89wWChjYgkUqS1XLUoe%2FVwuTDyRskNIKi0%2BWQ7%2F%2BmYQ6sLX0Tx8OvCUiayQUPWG5%2F7U7hpcSw%2FB20H5pDbtvQMSb%2F1Ert6VapukkAOs8dNjYlSw6YnJukKG8x%2FoIqjjQHdqEnaZ28Lf9rXqK2out9K61KHQaDGmAEHnKFgnUtyufdpobaFBtEmxwXODf2qFdknNE4pokb4P68fYlvPo5MR56g50zlyNcWnRU8jAwEcAPO4M7aFZ6tL5%2FYsjcLVADPWj7uMBswQtRKMUuzmHHEv3k7u%2F%2BFh9o7kjETJ9QRx301qUSITqn3J1FQS8c6dl5smkB9pxLKHzNHla7xuRv0tFWON8r2VDrzHTDEYGfxeRQ%2Bs1YXhTwS6YAHdpof3WO6ZN%2Byv0cmEHmPH4TRIG3j5zzanKyN3UaucWRZOc7ogfyxnDnCs6MIuq%2FMoGOqUBeb65qvkvDO4SVIdbt7KcrPLixPnFG3mSpcCLMg7ARQ%2FXfW0QsYURStPDeM%2BN%2FBBi3XObJ15ZTJdCGHNUAcvGM5vohUR%2FnphYO56x6Waddz0yh0Z3jRrkCjL09bCZaEZ1CF0RpQP4fWc0rnlVhGySD%2FG4%2Fa6A7kA%2BzFrpbU8V2AQrrOfJsa0QjNivfz3Rh%2FEuqFFjMEfdxKcpoHmxypvUhL6NhVnW&X-Amz-Signature=b5d25bc21ae63ebb6c47d9a71d78b9c48320fcb43a5831854ee9904467c4a728&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623UVO4JP%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T030022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEul1%2FJhu9ULgHpFvpV6yXenoavqT%2B37pdcn70TyP234AiEA3hBCCqRCA%2FCdzONWlzMIRDUOVOJimY8JPVMJQHIfT3QqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhdJ%2BsuAaJlOS%2F3tyrcA00b6cvYQvmsw0JaaN18fEQ1Ttwur%2BHjPI3bzJW7PgZwzyW7rT7uJX8bXR%2BXJAa7mMNPuSSwvCMfvP%2B3UfKpY57GndVakh19zHgL2nBuzaZqJNwY1iHA693E%2F9WiGb1H9wJFgsxTJjrChdq%2FoYCqfp5SHaruEA%2BX5Ad6GNvns9EYYnENWHq%2Fuy13ZUy93aOFIddKk3d%2BM89wWChjYgkUqS1XLUoe%2FVwuTDyRskNIKi0%2BWQ7%2F%2BmYQ6sLX0Tx8OvCUiayQUPWG5%2F7U7hpcSw%2FB20H5pDbtvQMSb%2F1Ert6VapukkAOs8dNjYlSw6YnJukKG8x%2FoIqjjQHdqEnaZ28Lf9rXqK2out9K61KHQaDGmAEHnKFgnUtyufdpobaFBtEmxwXODf2qFdknNE4pokb4P68fYlvPo5MR56g50zlyNcWnRU8jAwEcAPO4M7aFZ6tL5%2FYsjcLVADPWj7uMBswQtRKMUuzmHHEv3k7u%2F%2BFh9o7kjETJ9QRx301qUSITqn3J1FQS8c6dl5smkB9pxLKHzNHla7xuRv0tFWON8r2VDrzHTDEYGfxeRQ%2Bs1YXhTwS6YAHdpof3WO6ZN%2Byv0cmEHmPH4TRIG3j5zzanKyN3UaucWRZOc7ogfyxnDnCs6MIuq%2FMoGOqUBeb65qvkvDO4SVIdbt7KcrPLixPnFG3mSpcCLMg7ARQ%2FXfW0QsYURStPDeM%2BN%2FBBi3XObJ15ZTJdCGHNUAcvGM5vohUR%2FnphYO56x6Waddz0yh0Z3jRrkCjL09bCZaEZ1CF0RpQP4fWc0rnlVhGySD%2FG4%2Fa6A7kA%2BzFrpbU8V2AQrrOfJsa0QjNivfz3Rh%2FEuqFFjMEfdxKcpoHmxypvUhL6NhVnW&X-Amz-Signature=111559f5fbd38af17eedc197767e0cdc9c7a00c26b700a2a5a9f7f4e757b0f18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









