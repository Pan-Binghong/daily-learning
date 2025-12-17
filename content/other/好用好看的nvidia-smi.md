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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QITA3BMH%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE2Of4tfBu1OT8mO3IPAfmGR%2FXgJ2yPIJg4DmoOHAmfQIhAKxgbm2SCNTGTtA%2FLVd%2BnT9MFy81JLHfWtP8OB5rJ85AKv8DCHQQABoMNjM3NDIzMTgzODA1IgyOSXUiL8Bny5YTrHUq3AOYlroNTznRlafu4pwKY5v5bg4dcOhR946yj6uoqNw5%2BUnEHOYa0kH78ZpMiFPLpm%2Bg%2FOQlwverqJai%2F4qH5N%2BwdHRcE9wTuEBlPLleO9H85CLcaDjKkY6cl%2BLFXwdUpWxHedT4mGD5nMeA41nydm3uqNze8g8jdxiFkJsio646Q5T8yy4Gu2eh0wig31FqzCLsRrCGacTVfrpc3NtpEs5bIo8ncrA9qdtMMFj9k6uxUh%2Bha8uoIAbztRourQym2n4rCPbt%2BFEFhJWK7VA1wfZXNall8TQ7OAI0nRTLbaBs4BY%2F2ygYinaW3X%2BpfSvGvE7IPhtw3TV2k%2BRAri6Op7UHJk0fGriNcdl4IWO4HPqiDHgb6qO1QO3oCxNLOYt%2F%2B%2FR6eFBYgbC0Y4Vmm4i2TqvnNcoaOcmxtguTtpA%2BY7qx2WOBzjZ%2Ff8oEJ5Xl74FxDcwX%2BmtMtjfSl0xgL0dJd5vC6yzogtMb%2BWjpzXFQtEL4Qq1ofn2BwY2Q%2FXK47LJ1HeZJ7nYWA6zsZ53jU%2F5TOcYDj0T8%2BRLKcZK17jC4TESYmQrW2POO3iEypvpwahLQbopBUwAti%2Fg0XMTNRvjsMqDISe2CPPE9VLBn%2FPB7Z1cLOvjs7tFNvzJ1JbN1GjC2sojKBjqkAc98jEusAJL5jmx8kdegPnm9rTJAwmzLkczqVR%2FQPR%2FkLswLjR39jnifH8hmkkzcvzJ2Bqa6VJ4KNGiPY%2FHJ%2F6NSma2UttoDOgp1wjqCHWzAOM8g4ZJADpKsgBbGtzI4wRBklKcKjJBhxT3VHEt5UgFlLqXwUDlu9l536NS5QNyTtCFBRMt0It4qYjWZolybB23h4GGxqP032a%2BmGIxQAcowBoMt&X-Amz-Signature=85d7b50ee9b29b821552bbaeb66fd49171a2975f27ad3a3539efa7ae8e6778d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QITA3BMH%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE2Of4tfBu1OT8mO3IPAfmGR%2FXgJ2yPIJg4DmoOHAmfQIhAKxgbm2SCNTGTtA%2FLVd%2BnT9MFy81JLHfWtP8OB5rJ85AKv8DCHQQABoMNjM3NDIzMTgzODA1IgyOSXUiL8Bny5YTrHUq3AOYlroNTznRlafu4pwKY5v5bg4dcOhR946yj6uoqNw5%2BUnEHOYa0kH78ZpMiFPLpm%2Bg%2FOQlwverqJai%2F4qH5N%2BwdHRcE9wTuEBlPLleO9H85CLcaDjKkY6cl%2BLFXwdUpWxHedT4mGD5nMeA41nydm3uqNze8g8jdxiFkJsio646Q5T8yy4Gu2eh0wig31FqzCLsRrCGacTVfrpc3NtpEs5bIo8ncrA9qdtMMFj9k6uxUh%2Bha8uoIAbztRourQym2n4rCPbt%2BFEFhJWK7VA1wfZXNall8TQ7OAI0nRTLbaBs4BY%2F2ygYinaW3X%2BpfSvGvE7IPhtw3TV2k%2BRAri6Op7UHJk0fGriNcdl4IWO4HPqiDHgb6qO1QO3oCxNLOYt%2F%2B%2FR6eFBYgbC0Y4Vmm4i2TqvnNcoaOcmxtguTtpA%2BY7qx2WOBzjZ%2Ff8oEJ5Xl74FxDcwX%2BmtMtjfSl0xgL0dJd5vC6yzogtMb%2BWjpzXFQtEL4Qq1ofn2BwY2Q%2FXK47LJ1HeZJ7nYWA6zsZ53jU%2F5TOcYDj0T8%2BRLKcZK17jC4TESYmQrW2POO3iEypvpwahLQbopBUwAti%2Fg0XMTNRvjsMqDISe2CPPE9VLBn%2FPB7Z1cLOvjs7tFNvzJ1JbN1GjC2sojKBjqkAc98jEusAJL5jmx8kdegPnm9rTJAwmzLkczqVR%2FQPR%2FkLswLjR39jnifH8hmkkzcvzJ2Bqa6VJ4KNGiPY%2FHJ%2F6NSma2UttoDOgp1wjqCHWzAOM8g4ZJADpKsgBbGtzI4wRBklKcKjJBhxT3VHEt5UgFlLqXwUDlu9l536NS5QNyTtCFBRMt0It4qYjWZolybB23h4GGxqP032a%2BmGIxQAcowBoMt&X-Amz-Signature=5f548575c8a84c6f5efc254ea537d57cb059b4a6e623d939c3b336e6134708ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









