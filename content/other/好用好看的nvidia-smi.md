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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSIUB2GI%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FsU%2BRzLFTuhE36mrjHDrXSqQVYVO6wsWE%2F5LwxE4MEgIhAImQ0B3oC1Sld8OTHfMVanRH9K%2BCXEZsalTFhLH8L05iKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9722My8jaqho9CSsq3ANBe1mPrYTqjKb5uT79sYkgLOyT3WJpW9ZR6VuXD6p1UoOsV%2FP73UPn%2FU2oRzhFqgt0ybrSExFpOnEc1mmBkR7ZNK4YUybzJVH5%2BAuncemBvV65XHbadCI8dcoZ%2FFbM4xNgstQSWv83LAo8ucp7Z7fFqQyIvokWtzSMtX7TR0DjqN8N5%2B5ahbgx8zKtJI2w2nEGHdtlnyB6tgE87SZ4euyipXqNX%2BxD%2FIq4wZ74LVNp69Ifdp5MXT5usBy1vPIzcwLMonmnQ045tNsor%2Bkodhdk8fgSa2fvtpvWFrVBsthEk0rui7zuV0WIhMVO6T3nm1nzbGychszB6WDRxrnInyWy%2F2TED8emyHb2FtjP8JFR%2FIBj0eY6ll1PMGzxqstoEZ%2BEiv9dm8zPWWn2C29CWZEEeXu2%2FdSCRmoz9dY1Sy2wIDXOD%2Fz6BmyHw5mY6z484JsHGl5FuymnIjeWo9KQ4T3swhYVNBuGqd4%2FdBGzdcUOAg5U7QYvFSGm5eIdADqzrbVL6e2icElsdFKUEe78Qt6UvPGgwP0vL2eptoYNFtFYsfYieFkxdqr9DuUi1XBtjUwTQg%2FhE3iNc5l6yHbbg10ct5S3yxwZCD0cq71pr1t4ABi0ZexCy1PxTodt9jDvyZLOBjqkATpRnPC3jqe4%2BW00TI88rxSDDtW7ZLWvVxfvwB0h%2FBR5n5cdGXTHpdf1iA8ftXuqWr4BTlmn7PDB2xZf4RhWQ0PquoewS5dOTHoAoyje9Pm0E3b5tHKR6gIlFGxgiJakJn1DecrMgPY64a9li8mLZ5Rmw%2FGosMWVG1SwhrZPCMVY50tcFQefypafzyXJs5R%2F7A93%2BrQJvGFjwENx3tFyaXw6jzRH&X-Amz-Signature=9506180123f22074e4a608bd153b96558ada59789cb33e534116c5592feb3926&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSIUB2GI%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FsU%2BRzLFTuhE36mrjHDrXSqQVYVO6wsWE%2F5LwxE4MEgIhAImQ0B3oC1Sld8OTHfMVanRH9K%2BCXEZsalTFhLH8L05iKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9722My8jaqho9CSsq3ANBe1mPrYTqjKb5uT79sYkgLOyT3WJpW9ZR6VuXD6p1UoOsV%2FP73UPn%2FU2oRzhFqgt0ybrSExFpOnEc1mmBkR7ZNK4YUybzJVH5%2BAuncemBvV65XHbadCI8dcoZ%2FFbM4xNgstQSWv83LAo8ucp7Z7fFqQyIvokWtzSMtX7TR0DjqN8N5%2B5ahbgx8zKtJI2w2nEGHdtlnyB6tgE87SZ4euyipXqNX%2BxD%2FIq4wZ74LVNp69Ifdp5MXT5usBy1vPIzcwLMonmnQ045tNsor%2Bkodhdk8fgSa2fvtpvWFrVBsthEk0rui7zuV0WIhMVO6T3nm1nzbGychszB6WDRxrnInyWy%2F2TED8emyHb2FtjP8JFR%2FIBj0eY6ll1PMGzxqstoEZ%2BEiv9dm8zPWWn2C29CWZEEeXu2%2FdSCRmoz9dY1Sy2wIDXOD%2Fz6BmyHw5mY6z484JsHGl5FuymnIjeWo9KQ4T3swhYVNBuGqd4%2FdBGzdcUOAg5U7QYvFSGm5eIdADqzrbVL6e2icElsdFKUEe78Qt6UvPGgwP0vL2eptoYNFtFYsfYieFkxdqr9DuUi1XBtjUwTQg%2FhE3iNc5l6yHbbg10ct5S3yxwZCD0cq71pr1t4ABi0ZexCy1PxTodt9jDvyZLOBjqkATpRnPC3jqe4%2BW00TI88rxSDDtW7ZLWvVxfvwB0h%2FBR5n5cdGXTHpdf1iA8ftXuqWr4BTlmn7PDB2xZf4RhWQ0PquoewS5dOTHoAoyje9Pm0E3b5tHKR6gIlFGxgiJakJn1DecrMgPY64a9li8mLZ5Rmw%2FGosMWVG1SwhrZPCMVY50tcFQefypafzyXJs5R%2F7A93%2BrQJvGFjwENx3tFyaXw6jzRH&X-Amz-Signature=572960e405ee2e49e681d19daa567cfeb7d6c2484e4e07d2bda6a121272415ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









