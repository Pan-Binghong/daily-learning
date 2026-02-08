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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNS4T27Z%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B0KPldyd2usP8s%2FZSnV4elJuZmx0HlccLwOX38et3AAIgAxaDD5ncXjIetKLgptSDCpyEgU7OeAM4pGmSDkLU1ZEq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDI5Iw%2F2Sw6Fkr1IhVyrcA3AHN8d8%2BD%2BU0IAXtqnUeLZlhCHuzV9VKyMd8NymbXgNP%2F7%2BjcNgcV6%2FQh1lBoywE6Eloay5Ecz9ns1tXh9RxWKNuToiKvbCiqrfyslrAsI58Vaa3i%2BWzCj4L7ipLm58e0MwJ19KL1beGaHEoUtEDsi3F6491lKDtYxbRs1WHb273y1xqFnNsJp8XjIdu24d6sIM3FMHtUsiq7ibopfj0L8CBOZ7czqbngFRhurv%2FP0AEO2UwqByaFKWtRUseQtdr3nqhl0g2jAxinF8PSz90HMHpDA0TYViCZwwp4%2BLmb0HMh3Ks9uFSpw5hiKhHbAsPDjVesnz%2F%2FCY%2B96EA9vo8CDE8qKeRf9bnNtpw8A0atCyyJsdX%2BNpiZvW1TdfkJ7692Uaq6L9nzd5XtXwouMIeJTGxStoCYIkui9uxnqMMPvQRH7iPjmTneJa3ef%2Fj2DPOu5FO2kPkRyyXVNvvAxim%2BiRWWd2g%2Bxs5gZ4zA7%2FgLVr6Cy8VOubzQxYxF1gTHTDl1SxEW9cuTCdyPye%2Brk0eVE8g4wcFtdmaQbd230hC9v6pWFhRejG%2F8ppKIF2ydCC8iW6%2F5BFD5vVmtRSf8ucx4eGYqDczYEHeLf1zS%2FnZzohKc72nccZ4ShzaFG5MNWLoMwGOqUBQ4ngHjJyx%2BexNOGcRPLmhLjp8cNITuFoRsgxlZYC%2FwZFtb2mtJsA30g0KR9pTX5uM5J2PZO1LOkcySE1F9bWf1y8tOx2ZCkCc4JVnKS52H%2BwEcm1XFjXCBnv960L2Jz8HmpRo4qcNRaZUO%2B49ZwxXeEWjc8zGG8T28saaZVbmA2jqATBc%2FJLYIHoKfLO1hTMnQfMnFz0g1lFeUVPfJKFgmuEt2%2BD&X-Amz-Signature=238479170be6dff4635e60dd8b75e423ab1c0eccfd9901b48db293d864ddac5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNS4T27Z%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B0KPldyd2usP8s%2FZSnV4elJuZmx0HlccLwOX38et3AAIgAxaDD5ncXjIetKLgptSDCpyEgU7OeAM4pGmSDkLU1ZEq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDI5Iw%2F2Sw6Fkr1IhVyrcA3AHN8d8%2BD%2BU0IAXtqnUeLZlhCHuzV9VKyMd8NymbXgNP%2F7%2BjcNgcV6%2FQh1lBoywE6Eloay5Ecz9ns1tXh9RxWKNuToiKvbCiqrfyslrAsI58Vaa3i%2BWzCj4L7ipLm58e0MwJ19KL1beGaHEoUtEDsi3F6491lKDtYxbRs1WHb273y1xqFnNsJp8XjIdu24d6sIM3FMHtUsiq7ibopfj0L8CBOZ7czqbngFRhurv%2FP0AEO2UwqByaFKWtRUseQtdr3nqhl0g2jAxinF8PSz90HMHpDA0TYViCZwwp4%2BLmb0HMh3Ks9uFSpw5hiKhHbAsPDjVesnz%2F%2FCY%2B96EA9vo8CDE8qKeRf9bnNtpw8A0atCyyJsdX%2BNpiZvW1TdfkJ7692Uaq6L9nzd5XtXwouMIeJTGxStoCYIkui9uxnqMMPvQRH7iPjmTneJa3ef%2Fj2DPOu5FO2kPkRyyXVNvvAxim%2BiRWWd2g%2Bxs5gZ4zA7%2FgLVr6Cy8VOubzQxYxF1gTHTDl1SxEW9cuTCdyPye%2Brk0eVE8g4wcFtdmaQbd230hC9v6pWFhRejG%2F8ppKIF2ydCC8iW6%2F5BFD5vVmtRSf8ucx4eGYqDczYEHeLf1zS%2FnZzohKc72nccZ4ShzaFG5MNWLoMwGOqUBQ4ngHjJyx%2BexNOGcRPLmhLjp8cNITuFoRsgxlZYC%2FwZFtb2mtJsA30g0KR9pTX5uM5J2PZO1LOkcySE1F9bWf1y8tOx2ZCkCc4JVnKS52H%2BwEcm1XFjXCBnv960L2Jz8HmpRo4qcNRaZUO%2B49ZwxXeEWjc8zGG8T28saaZVbmA2jqATBc%2FJLYIHoKfLO1hTMnQfMnFz0g1lFeUVPfJKFgmuEt2%2BD&X-Amz-Signature=1a0abc782f06672245a97f87567f8724b85288a9ba485a0d683d163d2bec1665&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNS4T27Z%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B0KPldyd2usP8s%2FZSnV4elJuZmx0HlccLwOX38et3AAIgAxaDD5ncXjIetKLgptSDCpyEgU7OeAM4pGmSDkLU1ZEq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDI5Iw%2F2Sw6Fkr1IhVyrcA3AHN8d8%2BD%2BU0IAXtqnUeLZlhCHuzV9VKyMd8NymbXgNP%2F7%2BjcNgcV6%2FQh1lBoywE6Eloay5Ecz9ns1tXh9RxWKNuToiKvbCiqrfyslrAsI58Vaa3i%2BWzCj4L7ipLm58e0MwJ19KL1beGaHEoUtEDsi3F6491lKDtYxbRs1WHb273y1xqFnNsJp8XjIdu24d6sIM3FMHtUsiq7ibopfj0L8CBOZ7czqbngFRhurv%2FP0AEO2UwqByaFKWtRUseQtdr3nqhl0g2jAxinF8PSz90HMHpDA0TYViCZwwp4%2BLmb0HMh3Ks9uFSpw5hiKhHbAsPDjVesnz%2F%2FCY%2B96EA9vo8CDE8qKeRf9bnNtpw8A0atCyyJsdX%2BNpiZvW1TdfkJ7692Uaq6L9nzd5XtXwouMIeJTGxStoCYIkui9uxnqMMPvQRH7iPjmTneJa3ef%2Fj2DPOu5FO2kPkRyyXVNvvAxim%2BiRWWd2g%2Bxs5gZ4zA7%2FgLVr6Cy8VOubzQxYxF1gTHTDl1SxEW9cuTCdyPye%2Brk0eVE8g4wcFtdmaQbd230hC9v6pWFhRejG%2F8ppKIF2ydCC8iW6%2F5BFD5vVmtRSf8ucx4eGYqDczYEHeLf1zS%2FnZzohKc72nccZ4ShzaFG5MNWLoMwGOqUBQ4ngHjJyx%2BexNOGcRPLmhLjp8cNITuFoRsgxlZYC%2FwZFtb2mtJsA30g0KR9pTX5uM5J2PZO1LOkcySE1F9bWf1y8tOx2ZCkCc4JVnKS52H%2BwEcm1XFjXCBnv960L2Jz8HmpRo4qcNRaZUO%2B49ZwxXeEWjc8zGG8T28saaZVbmA2jqATBc%2FJLYIHoKfLO1hTMnQfMnFz0g1lFeUVPfJKFgmuEt2%2BD&X-Amz-Signature=cc44ee9455c0dd31aba986d86df9f7dc1b1eb5146bde72fb9a228649db4bebbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

