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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6VBMTP5%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIGssVwx882JSlvrVxq39m2Fdm8e%2FIrptpqpzuqNO4W%2FCAiAh41UBQ%2B502EEY04RNJVvlLLA8tJJrQZI1uY3O6MQDZCqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbu3F9fHVWHs6GZsQKtwD9pHrYqHUfoWuJj7I2lZsd3%2F0Ke5UH8Axddon9JLDuarv%2FizG8fjoex8%2Fe3skraGtHT%2FoVYwfEtAYgXDxr9ltUMp9gspIF0zA%2FN8o0qopMZWM1vs4HGcnwsf7TCg%2BF6MaH7qZlXH5V5BN%2BqBssR1AYPe8FRbcnxopqQLXV7ukg%2F2jtUOKzvddOxgDt8hWUxjtGqPeTCWCIoU9MSXc9nzCDNmH7PnUiCf8g0l6q%2B%2BFfPIT9GKB0Pcu7ilps1v%2FOr5i5ufr3mgu1EbviTaxKiB1PefcLpaf5OrYdbyQ9k0p3fbxsfJSZrE%2BOWezpgWoP8%2F%2Fa8BZ4JWpsHW%2FTzYd2B2zq%2FzFGgiDB4hhaSVBJ%2FOjRhFVcpZ3PCizJSXz%2FdRmgFJ7oOd5c33WTv9B7J09br4K3dBwU5IFHHiLqEgmk3MIrJVaVIgcDkmyQIFZCxeAn2ICqe1pOZn0g4yBwjO23Sy4QV2yKdBspNj%2FIRvDAYInSBqLsgdFzdcv8NqkV6Cv0l%2F8PZvkgv5p3EN4G6%2BIvpmHBzHq%2BNHjlUsYHD%2B%2FzV2g21J%2B5gcD0hgcfb2Wi9Wk7hvfSfewaXuN1Nc%2FY%2BLQFg4cOpwQMUuPtCe3ucmtC3156AG9Lzpkqhhg62gcCKgwjK2LzwY6pgHau6UKj4Uj%2FbAaV4Hsqta96pyO%2Fy%2BOF7sNbHPrVi%2FNETD9s4X14ZuO9QYjqgn5DK0GsHDMOO3ME7hqNzkaV4Q3YMTMb5LEGjc7EfUt8MlP5FWafSn0za%2FCR58y%2Fxzq%2Be%2B0r852CUdbdhJFAQ8DXm9Q1yM2S0GwLlje%2BZvuQaHAAg3p%2FFDL44tmwY29Su3PtUdqCXmPqHiKTFuzPcsU1xnDDBJES6GZ&X-Amz-Signature=fea822588b08e9003bb5f61c72a2aeef4e6cd9f65f1c695534bfddbeb86ec0b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6VBMTP5%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIGssVwx882JSlvrVxq39m2Fdm8e%2FIrptpqpzuqNO4W%2FCAiAh41UBQ%2B502EEY04RNJVvlLLA8tJJrQZI1uY3O6MQDZCqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbu3F9fHVWHs6GZsQKtwD9pHrYqHUfoWuJj7I2lZsd3%2F0Ke5UH8Axddon9JLDuarv%2FizG8fjoex8%2Fe3skraGtHT%2FoVYwfEtAYgXDxr9ltUMp9gspIF0zA%2FN8o0qopMZWM1vs4HGcnwsf7TCg%2BF6MaH7qZlXH5V5BN%2BqBssR1AYPe8FRbcnxopqQLXV7ukg%2F2jtUOKzvddOxgDt8hWUxjtGqPeTCWCIoU9MSXc9nzCDNmH7PnUiCf8g0l6q%2B%2BFfPIT9GKB0Pcu7ilps1v%2FOr5i5ufr3mgu1EbviTaxKiB1PefcLpaf5OrYdbyQ9k0p3fbxsfJSZrE%2BOWezpgWoP8%2F%2Fa8BZ4JWpsHW%2FTzYd2B2zq%2FzFGgiDB4hhaSVBJ%2FOjRhFVcpZ3PCizJSXz%2FdRmgFJ7oOd5c33WTv9B7J09br4K3dBwU5IFHHiLqEgmk3MIrJVaVIgcDkmyQIFZCxeAn2ICqe1pOZn0g4yBwjO23Sy4QV2yKdBspNj%2FIRvDAYInSBqLsgdFzdcv8NqkV6Cv0l%2F8PZvkgv5p3EN4G6%2BIvpmHBzHq%2BNHjlUsYHD%2B%2FzV2g21J%2B5gcD0hgcfb2Wi9Wk7hvfSfewaXuN1Nc%2FY%2BLQFg4cOpwQMUuPtCe3ucmtC3156AG9Lzpkqhhg62gcCKgwjK2LzwY6pgHau6UKj4Uj%2FbAaV4Hsqta96pyO%2Fy%2BOF7sNbHPrVi%2FNETD9s4X14ZuO9QYjqgn5DK0GsHDMOO3ME7hqNzkaV4Q3YMTMb5LEGjc7EfUt8MlP5FWafSn0za%2FCR58y%2Fxzq%2Be%2B0r852CUdbdhJFAQ8DXm9Q1yM2S0GwLlje%2BZvuQaHAAg3p%2FFDL44tmwY29Su3PtUdqCXmPqHiKTFuzPcsU1xnDDBJES6GZ&X-Amz-Signature=1532c053fc3eda83fa681f8579294eb50f6bd8414c5ecdbfdb466c16976ec4ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6VBMTP5%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIGssVwx882JSlvrVxq39m2Fdm8e%2FIrptpqpzuqNO4W%2FCAiAh41UBQ%2B502EEY04RNJVvlLLA8tJJrQZI1uY3O6MQDZCqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbu3F9fHVWHs6GZsQKtwD9pHrYqHUfoWuJj7I2lZsd3%2F0Ke5UH8Axddon9JLDuarv%2FizG8fjoex8%2Fe3skraGtHT%2FoVYwfEtAYgXDxr9ltUMp9gspIF0zA%2FN8o0qopMZWM1vs4HGcnwsf7TCg%2BF6MaH7qZlXH5V5BN%2BqBssR1AYPe8FRbcnxopqQLXV7ukg%2F2jtUOKzvddOxgDt8hWUxjtGqPeTCWCIoU9MSXc9nzCDNmH7PnUiCf8g0l6q%2B%2BFfPIT9GKB0Pcu7ilps1v%2FOr5i5ufr3mgu1EbviTaxKiB1PefcLpaf5OrYdbyQ9k0p3fbxsfJSZrE%2BOWezpgWoP8%2F%2Fa8BZ4JWpsHW%2FTzYd2B2zq%2FzFGgiDB4hhaSVBJ%2FOjRhFVcpZ3PCizJSXz%2FdRmgFJ7oOd5c33WTv9B7J09br4K3dBwU5IFHHiLqEgmk3MIrJVaVIgcDkmyQIFZCxeAn2ICqe1pOZn0g4yBwjO23Sy4QV2yKdBspNj%2FIRvDAYInSBqLsgdFzdcv8NqkV6Cv0l%2F8PZvkgv5p3EN4G6%2BIvpmHBzHq%2BNHjlUsYHD%2B%2FzV2g21J%2B5gcD0hgcfb2Wi9Wk7hvfSfewaXuN1Nc%2FY%2BLQFg4cOpwQMUuPtCe3ucmtC3156AG9Lzpkqhhg62gcCKgwjK2LzwY6pgHau6UKj4Uj%2FbAaV4Hsqta96pyO%2Fy%2BOF7sNbHPrVi%2FNETD9s4X14ZuO9QYjqgn5DK0GsHDMOO3ME7hqNzkaV4Q3YMTMb5LEGjc7EfUt8MlP5FWafSn0za%2FCR58y%2Fxzq%2Be%2B0r852CUdbdhJFAQ8DXm9Q1yM2S0GwLlje%2BZvuQaHAAg3p%2FFDL44tmwY29Su3PtUdqCXmPqHiKTFuzPcsU1xnDDBJES6GZ&X-Amz-Signature=9752fa6d9dfb23362c0fd0035aef0d59f6c1d55ac5f2908ddf4f8c3dfb64d3ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

