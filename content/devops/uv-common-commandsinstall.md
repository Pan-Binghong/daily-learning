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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBHZRTVX%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD8uqYk2eCU8W3vVE7QU%2BLwAFL7IPH4MqHO8cJkd%2B3a4gIhAJqe0ZHRWeSbfEujRlv7nhsMs%2FWVCgV7ovDUTX3N5EEcKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRz3UOmRZETeiBEEcq3AOd48A%2B4XlOhLo2WK6xAuAmkffkI%2Bg7e6cWnXEiJLQaR8pCHMW%2B1mZolNMxvSEjMb1fUOZIlz2p8%2BqbzmjRwZtKRw19FPVcnswyUZfCYUIAq0noqIkNkPiR%2Bf8qaegpyZG7izM6iYphPljc413PMQ56BOCVZpeoFb8hiQrg1amk%2Fm8GFOE1CnpSytIV9zLHCEqV%2FkqMkjAKCgkKO7d9k52BudTi36D3jLURz8hRuO6SkaU18MXxU1dzm4ALZBKj6JzAcAP22yjKjzo2svKqDojleHKrpc262sHDqLjL%2F2qsviVDCXzojTxSwjJUafydCxVffJVBugIQ4rX%2FgiRlyE1m1DTaQB2kNEmSIKzXdpkdemwNx4CNOChd%2FiD6ekgQRO%2F2%2F%2Fr8xC51wNTxrHmMmDse4z4MTke8IfZNsb%2Fv5eJrb1EncNucxtIODxSwwrTHmhU%2FnqNM3L8DVUavtgLa6SQKwsYF6C0V6EliCsLC6g2qtXz%2Fv47g0iBGDGiBwExwIRmDmxmfIujIQzbcfCFQCIA2cs1uO5fRGu0PxUW2YRgjbsr3ipCw3rnU3fnFi1SlEUHr4uZbwcZLTT1Nh5rtL5m475CwLo4n6PqBjvs4MsZxYP1mH2tAqrR8znH27TCRuL%2FIBjqkAR8%2BkqnO5dPpTmZoXg65haQGLUi2aAAcyCYxE0wLbIGvSIOetBwNr8uzp4fgMn1otKYzjCg0cvLiC5UvLUQ0CwG2NOucHtjwtznE%2BayUrMHIFxpXaIQ23le6IurGSuSKxEUy597FOCYQk2vPU%2BLjEgQUL16L6zx1WokBOH8citpId5yiVjLLM9OAgoLjnIo59m2LqQeluuHJButK2PPstkJwLslw&X-Amz-Signature=3fa2138f8bf71c5dec60432adfab970f9684bc1d9644cf1c6c24f87cb94af01c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBHZRTVX%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD8uqYk2eCU8W3vVE7QU%2BLwAFL7IPH4MqHO8cJkd%2B3a4gIhAJqe0ZHRWeSbfEujRlv7nhsMs%2FWVCgV7ovDUTX3N5EEcKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRz3UOmRZETeiBEEcq3AOd48A%2B4XlOhLo2WK6xAuAmkffkI%2Bg7e6cWnXEiJLQaR8pCHMW%2B1mZolNMxvSEjMb1fUOZIlz2p8%2BqbzmjRwZtKRw19FPVcnswyUZfCYUIAq0noqIkNkPiR%2Bf8qaegpyZG7izM6iYphPljc413PMQ56BOCVZpeoFb8hiQrg1amk%2Fm8GFOE1CnpSytIV9zLHCEqV%2FkqMkjAKCgkKO7d9k52BudTi36D3jLURz8hRuO6SkaU18MXxU1dzm4ALZBKj6JzAcAP22yjKjzo2svKqDojleHKrpc262sHDqLjL%2F2qsviVDCXzojTxSwjJUafydCxVffJVBugIQ4rX%2FgiRlyE1m1DTaQB2kNEmSIKzXdpkdemwNx4CNOChd%2FiD6ekgQRO%2F2%2F%2Fr8xC51wNTxrHmMmDse4z4MTke8IfZNsb%2Fv5eJrb1EncNucxtIODxSwwrTHmhU%2FnqNM3L8DVUavtgLa6SQKwsYF6C0V6EliCsLC6g2qtXz%2Fv47g0iBGDGiBwExwIRmDmxmfIujIQzbcfCFQCIA2cs1uO5fRGu0PxUW2YRgjbsr3ipCw3rnU3fnFi1SlEUHr4uZbwcZLTT1Nh5rtL5m475CwLo4n6PqBjvs4MsZxYP1mH2tAqrR8znH27TCRuL%2FIBjqkAR8%2BkqnO5dPpTmZoXg65haQGLUi2aAAcyCYxE0wLbIGvSIOetBwNr8uzp4fgMn1otKYzjCg0cvLiC5UvLUQ0CwG2NOucHtjwtznE%2BayUrMHIFxpXaIQ23le6IurGSuSKxEUy597FOCYQk2vPU%2BLjEgQUL16L6zx1WokBOH8citpId5yiVjLLM9OAgoLjnIo59m2LqQeluuHJButK2PPstkJwLslw&X-Amz-Signature=246c5162e326664508e06664f9f127bd4ab3640f98f5fbde7c553bd94f72e850&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBHZRTVX%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD8uqYk2eCU8W3vVE7QU%2BLwAFL7IPH4MqHO8cJkd%2B3a4gIhAJqe0ZHRWeSbfEujRlv7nhsMs%2FWVCgV7ovDUTX3N5EEcKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRz3UOmRZETeiBEEcq3AOd48A%2B4XlOhLo2WK6xAuAmkffkI%2Bg7e6cWnXEiJLQaR8pCHMW%2B1mZolNMxvSEjMb1fUOZIlz2p8%2BqbzmjRwZtKRw19FPVcnswyUZfCYUIAq0noqIkNkPiR%2Bf8qaegpyZG7izM6iYphPljc413PMQ56BOCVZpeoFb8hiQrg1amk%2Fm8GFOE1CnpSytIV9zLHCEqV%2FkqMkjAKCgkKO7d9k52BudTi36D3jLURz8hRuO6SkaU18MXxU1dzm4ALZBKj6JzAcAP22yjKjzo2svKqDojleHKrpc262sHDqLjL%2F2qsviVDCXzojTxSwjJUafydCxVffJVBugIQ4rX%2FgiRlyE1m1DTaQB2kNEmSIKzXdpkdemwNx4CNOChd%2FiD6ekgQRO%2F2%2F%2Fr8xC51wNTxrHmMmDse4z4MTke8IfZNsb%2Fv5eJrb1EncNucxtIODxSwwrTHmhU%2FnqNM3L8DVUavtgLa6SQKwsYF6C0V6EliCsLC6g2qtXz%2Fv47g0iBGDGiBwExwIRmDmxmfIujIQzbcfCFQCIA2cs1uO5fRGu0PxUW2YRgjbsr3ipCw3rnU3fnFi1SlEUHr4uZbwcZLTT1Nh5rtL5m475CwLo4n6PqBjvs4MsZxYP1mH2tAqrR8znH27TCRuL%2FIBjqkAR8%2BkqnO5dPpTmZoXg65haQGLUi2aAAcyCYxE0wLbIGvSIOetBwNr8uzp4fgMn1otKYzjCg0cvLiC5UvLUQ0CwG2NOucHtjwtznE%2BayUrMHIFxpXaIQ23le6IurGSuSKxEUy597FOCYQk2vPU%2BLjEgQUL16L6zx1WokBOH8citpId5yiVjLLM9OAgoLjnIo59m2LqQeluuHJButK2PPstkJwLslw&X-Amz-Signature=b9f4ed4161d03395397222ad1d8cb267cf65a27fd6aa77a23cc3ecdaea521965&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

