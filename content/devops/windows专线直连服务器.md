---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6N7EBAA%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkW9hFHJY1oOSzkKDULaFUquVA%2BinAk0IK23OOZeLryAiAry8TFdvXfpl2qFC42DDLoYo9O3PhNH1%2F5Lt0WO%2BHq3yqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0CuEnqwSt0mJErdGKtwDggc%2BWJkFiuxvMkUT%2FuAHOSPfT0gqVE9ko0kXSvorXOo7iLIJERKWm%2FY00hEM9O7C5LgL3ZTQHcZX9A9QTbKIvdIoo0R%2BRwq8KQv5Ih%2BjOMrLQarx9SOOy4IQJACqKd0CTEOBQKpSeYyzMfilwr2ddAYildOZ2hFGx79%2FFyhH6ZG1f9ChlJ6r2v4p6B01uQxC5EMSZTsGr%2BiUh8%2FZs7d2Z2i8Xr5QeDy8dZfQhSQz9aB3dtZfur9fA9IRz2tZugpAsv7yu8WymU04YtnROQEPMnFLy2fHEQFlafv%2F8K3yFhAwLQM4kGiGgRAp525myJLj2VqLN2gcQDfX5e9WCBu%2BOoiXldbP64exUKU0%2FfBqbxzmWTwkwMRCYO2zptcga2YbjwFMofDy5jmreIXietVYsbnyWd6nvlgnnZwXr2QeidqCfiG5rtA3cfxSJiAtPLg3lz9uRxI36fIg1d6%2FM%2Bzzzr2B%2FxvpS%2FEnanuM2irdyHIjw4nxA2ObgEelrsoXEfVY1RO2zCk4xYehyZSVYIYB5K6KzE6z6okJVLFewiAr9jjG7oBpHAWJUAAgM3xc1zf8WH24Fp3lCEhIIfbgJplKsc5V9uu6U4QjIz1juyzeQN6yODnQ%2FJIyqXBlv0gw5JDYzQY6pgHVpfNucBN%2BHRyYvbIgGg2lSB0A1QuZeq9ZoTvS9VzN7XH%2FbkoEqQTvtRgbKq2rkatmMnJx1k%2FkyWNjZ5lL1Ajqmvcp48swembQtZb8IikCMIzfZbGVLTkBopxPlf2hw8ysweXQRV%2Bzx%2FzeiWb5OLl5WLt7grR0EpN0gqFOezuGSaEfNjhbkNVCuT5XpDQ0Y6yEcUDXi%2Bi%2B2ijOmfj5MKATMsFhN%2Bfc&X-Amz-Signature=875d1674600cd469188dc4719affb31ddf089f03c446406fc4626c77a2319549&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

