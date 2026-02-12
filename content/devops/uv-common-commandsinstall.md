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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQDL2FJS%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIBeOphBq0rn05pJ4xmuoBC726MOMt7%2FItAzrFKr5nQEBAiAEKVAKFWEMgq9oPspWY%2F6WI7%2BN6MNqtTJyQwdRlhEFPyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVxrwzsajnJViISW0KtwD31bgwqEnauXACTxtWO1IoXzbxBjIONLxLQAHdnf%2BkeZiQ0k5Qqn%2BTknJpFvN2aLntmEWEQY7CrVybwv4UxLB2KIUBAtI1BrQOegP7N8%2BmIRZb8Ye%2BQgqO8zFybbIcAHK8CuCTlcix%2FYcU7SIEZVp5WdiDakbWsM9Z1x6xFtOssGt8Mreu82oH%2BnVUasNOHeK3ZeFTyEo7bQ8K9%2BQbb8xSFehs6%2FTILH216bHwtg0du%2BH1eo38XShrdymqLLm34Q3qfXG2%2BZRLwdHa9Hd5ajrsZKp94z2c%2B7f5xHGoWBoPz%2FW2Dpmy5H1RxqZr8NMrbM9fI%2B1VymAAeeYsMfZUn34TiOAV6OjnsUvl5IMmx1QacmFs0bykMiifhLcuYM7zVvzWTnbh7K537JUmCg1dm%2FoVOEp0TZLJg0XJo7hO11JiPSaN1L%2BwkEKN6IBPWr%2Fun1rKTOYpruQcJrpxtJzirYW%2FJJwPgniQ%2BDy5AU8%2FoPHxxJBivVkrJzbQuX7Rqkxv876CtzGa6XpS5wzTxQRsf2rEp900%2Bg2LEfpA7L6q89moOtOimJX%2B7NyC%2Bw1eSI3AntHl8uOiPxPuyixAzQjcx%2F6lj2%2FAu0QheZEINDb5vt3TxwYlZ%2FUq4teReDjV%2Fow0ZG1zAY6pgGm8Vbac5r%2Fi4FKKAKcLPZlMFYQjBZHas0IyOtaAWBFmNsgD5rEJ62ABdPvvn%2FHoBjbQaXOoOhdqas9wP6NR7IEPLB%2Fc91ElIb4%2BNcXaSSiZCh%2Bl4M5QnRyKLASvAi5rpGMmOoPRtGiYQTH80A4a8boob2QXdgXbyY0BypnBNTw9RzgDj%2FH27vl%2BJ35AhDaw3CEhmzzqmbLLfRj4sDQ7JfVh%2B%2BLPwfZ&X-Amz-Signature=678988e468e71166d3521f3b852a996807a0d139c1d6ed598629ef40e75a79c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQDL2FJS%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIBeOphBq0rn05pJ4xmuoBC726MOMt7%2FItAzrFKr5nQEBAiAEKVAKFWEMgq9oPspWY%2F6WI7%2BN6MNqtTJyQwdRlhEFPyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVxrwzsajnJViISW0KtwD31bgwqEnauXACTxtWO1IoXzbxBjIONLxLQAHdnf%2BkeZiQ0k5Qqn%2BTknJpFvN2aLntmEWEQY7CrVybwv4UxLB2KIUBAtI1BrQOegP7N8%2BmIRZb8Ye%2BQgqO8zFybbIcAHK8CuCTlcix%2FYcU7SIEZVp5WdiDakbWsM9Z1x6xFtOssGt8Mreu82oH%2BnVUasNOHeK3ZeFTyEo7bQ8K9%2BQbb8xSFehs6%2FTILH216bHwtg0du%2BH1eo38XShrdymqLLm34Q3qfXG2%2BZRLwdHa9Hd5ajrsZKp94z2c%2B7f5xHGoWBoPz%2FW2Dpmy5H1RxqZr8NMrbM9fI%2B1VymAAeeYsMfZUn34TiOAV6OjnsUvl5IMmx1QacmFs0bykMiifhLcuYM7zVvzWTnbh7K537JUmCg1dm%2FoVOEp0TZLJg0XJo7hO11JiPSaN1L%2BwkEKN6IBPWr%2Fun1rKTOYpruQcJrpxtJzirYW%2FJJwPgniQ%2BDy5AU8%2FoPHxxJBivVkrJzbQuX7Rqkxv876CtzGa6XpS5wzTxQRsf2rEp900%2Bg2LEfpA7L6q89moOtOimJX%2B7NyC%2Bw1eSI3AntHl8uOiPxPuyixAzQjcx%2F6lj2%2FAu0QheZEINDb5vt3TxwYlZ%2FUq4teReDjV%2Fow0ZG1zAY6pgGm8Vbac5r%2Fi4FKKAKcLPZlMFYQjBZHas0IyOtaAWBFmNsgD5rEJ62ABdPvvn%2FHoBjbQaXOoOhdqas9wP6NR7IEPLB%2Fc91ElIb4%2BNcXaSSiZCh%2Bl4M5QnRyKLASvAi5rpGMmOoPRtGiYQTH80A4a8boob2QXdgXbyY0BypnBNTw9RzgDj%2FH27vl%2BJ35AhDaw3CEhmzzqmbLLfRj4sDQ7JfVh%2B%2BLPwfZ&X-Amz-Signature=7df86958ccd5a60becfd49b7d5dd24fd8aba0d6faf517e6f14794061e38682fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQDL2FJS%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIBeOphBq0rn05pJ4xmuoBC726MOMt7%2FItAzrFKr5nQEBAiAEKVAKFWEMgq9oPspWY%2F6WI7%2BN6MNqtTJyQwdRlhEFPyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVxrwzsajnJViISW0KtwD31bgwqEnauXACTxtWO1IoXzbxBjIONLxLQAHdnf%2BkeZiQ0k5Qqn%2BTknJpFvN2aLntmEWEQY7CrVybwv4UxLB2KIUBAtI1BrQOegP7N8%2BmIRZb8Ye%2BQgqO8zFybbIcAHK8CuCTlcix%2FYcU7SIEZVp5WdiDakbWsM9Z1x6xFtOssGt8Mreu82oH%2BnVUasNOHeK3ZeFTyEo7bQ8K9%2BQbb8xSFehs6%2FTILH216bHwtg0du%2BH1eo38XShrdymqLLm34Q3qfXG2%2BZRLwdHa9Hd5ajrsZKp94z2c%2B7f5xHGoWBoPz%2FW2Dpmy5H1RxqZr8NMrbM9fI%2B1VymAAeeYsMfZUn34TiOAV6OjnsUvl5IMmx1QacmFs0bykMiifhLcuYM7zVvzWTnbh7K537JUmCg1dm%2FoVOEp0TZLJg0XJo7hO11JiPSaN1L%2BwkEKN6IBPWr%2Fun1rKTOYpruQcJrpxtJzirYW%2FJJwPgniQ%2BDy5AU8%2FoPHxxJBivVkrJzbQuX7Rqkxv876CtzGa6XpS5wzTxQRsf2rEp900%2Bg2LEfpA7L6q89moOtOimJX%2B7NyC%2Bw1eSI3AntHl8uOiPxPuyixAzQjcx%2F6lj2%2FAu0QheZEINDb5vt3TxwYlZ%2FUq4teReDjV%2Fow0ZG1zAY6pgGm8Vbac5r%2Fi4FKKAKcLPZlMFYQjBZHas0IyOtaAWBFmNsgD5rEJ62ABdPvvn%2FHoBjbQaXOoOhdqas9wP6NR7IEPLB%2Fc91ElIb4%2BNcXaSSiZCh%2Bl4M5QnRyKLASvAi5rpGMmOoPRtGiYQTH80A4a8boob2QXdgXbyY0BypnBNTw9RzgDj%2FH27vl%2BJ35AhDaw3CEhmzzqmbLLfRj4sDQ7JfVh%2B%2BLPwfZ&X-Amz-Signature=5d45244a261bef009109874c841f96eaa80a126fe50986d672b5f68add223646&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

