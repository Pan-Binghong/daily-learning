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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W23O7PKX%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T042006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYlZClGdqKGKlfpIMsGXee%2FoPB1BH8j9eCYzl5yZkDPAIhAPq1oPSuIy2Lln8H9L0urXz4yGCRk%2BG3iuMPa6AfEymvKv8DCHQQABoMNjM3NDIzMTgzODA1IgyLoXCvKNUk%2BEHbsgwq3AO%2BPh4Svf9zN4PwAUz1NaFk7crfi6hICi4pKqHKsl%2FQpE%2BJNjLkCIXez8IgL%2FYrrh5IxkdNXrWqv3DPjfSFudWEj5SvMVeXwU%2Bt92GB%2F%2Fbd%2BEj%2FvRPqVXQ27s9dS9GSZfPRbNY1nyMbiiD8FqbFM%2BgcYR0do7LkMF8ZYiouXpvNRC0YsCCV0wYNYuizNiBAKAk64mGyr4RjOHEbk0DBydXDt9ANhUcsU%2BJ1tIZ947lGvLRp7B3Rv6jXuMZ3DePIjI%2BQ5JFLxl3o%2FDoqH8kfb2g%2Fob33xQ832M4YEGxboVEejOaMb6aDUb3q6oPoOYv5XwATJk2zVYRFxIdXMF5buCMDpDkz1NzxvROChfN7THII%2F%2B53%2FX%2BZGvatsHhO3UEU0rlW3A92Pl%2Bj%2F%2Ft2HJOhozMYEFBTbEZh3Qra9Qj2gJ39oTwVDYfU8FML5o1PQPviRJq6X3ol2sHDb9Lqv%2FTifvtoKcwbOZzVsy1Wkp56WxNoQR8eKUtpiT6CORtd3Xb6rSquvvrcXEECfkt0we8GAuXN260aXT%2F%2B5MF6wMoCxNMc50w8X9ZmBFhpcRkPBLhcwmPqhTNM38Z4TeLvG4G6JjmaCfhQ2qbpsCNZ%2FXiGoA%2FTW%2Be5hrQKDckD62eoCDCorKvPBjqkASmWrVitgpvIyxYrqGD340hLplTgnzvPLNrhy0RAQ5bv74bRZcVloIFv9koXhYUowHotQSBJPUgGh1gC52XXzCYuekgjguSpa39plZ41JHkeGD85Qgko4Una%2BkTAfrtbjIs7umzz%2F8YINvCBRPDmgx32DCg1TuByWgJdoO1DbdvezlL7pHdMvkMg6%2FlBKTAnienIB1QQeKXUHC7B2naOhPVVtL%2BC&X-Amz-Signature=8aeb1e7dd8271022467b2a8fe18dc793114af06a0ce60e41cf8485941f34d29b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W23O7PKX%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T042006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYlZClGdqKGKlfpIMsGXee%2FoPB1BH8j9eCYzl5yZkDPAIhAPq1oPSuIy2Lln8H9L0urXz4yGCRk%2BG3iuMPa6AfEymvKv8DCHQQABoMNjM3NDIzMTgzODA1IgyLoXCvKNUk%2BEHbsgwq3AO%2BPh4Svf9zN4PwAUz1NaFk7crfi6hICi4pKqHKsl%2FQpE%2BJNjLkCIXez8IgL%2FYrrh5IxkdNXrWqv3DPjfSFudWEj5SvMVeXwU%2Bt92GB%2F%2Fbd%2BEj%2FvRPqVXQ27s9dS9GSZfPRbNY1nyMbiiD8FqbFM%2BgcYR0do7LkMF8ZYiouXpvNRC0YsCCV0wYNYuizNiBAKAk64mGyr4RjOHEbk0DBydXDt9ANhUcsU%2BJ1tIZ947lGvLRp7B3Rv6jXuMZ3DePIjI%2BQ5JFLxl3o%2FDoqH8kfb2g%2Fob33xQ832M4YEGxboVEejOaMb6aDUb3q6oPoOYv5XwATJk2zVYRFxIdXMF5buCMDpDkz1NzxvROChfN7THII%2F%2B53%2FX%2BZGvatsHhO3UEU0rlW3A92Pl%2Bj%2F%2Ft2HJOhozMYEFBTbEZh3Qra9Qj2gJ39oTwVDYfU8FML5o1PQPviRJq6X3ol2sHDb9Lqv%2FTifvtoKcwbOZzVsy1Wkp56WxNoQR8eKUtpiT6CORtd3Xb6rSquvvrcXEECfkt0we8GAuXN260aXT%2F%2B5MF6wMoCxNMc50w8X9ZmBFhpcRkPBLhcwmPqhTNM38Z4TeLvG4G6JjmaCfhQ2qbpsCNZ%2FXiGoA%2FTW%2Be5hrQKDckD62eoCDCorKvPBjqkASmWrVitgpvIyxYrqGD340hLplTgnzvPLNrhy0RAQ5bv74bRZcVloIFv9koXhYUowHotQSBJPUgGh1gC52XXzCYuekgjguSpa39plZ41JHkeGD85Qgko4Una%2BkTAfrtbjIs7umzz%2F8YINvCBRPDmgx32DCg1TuByWgJdoO1DbdvezlL7pHdMvkMg6%2FlBKTAnienIB1QQeKXUHC7B2naOhPVVtL%2BC&X-Amz-Signature=16830b8509b58377c097ee0d713df7cd419c84b49befc706d350bc1c70130c84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W23O7PKX%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T042006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYlZClGdqKGKlfpIMsGXee%2FoPB1BH8j9eCYzl5yZkDPAIhAPq1oPSuIy2Lln8H9L0urXz4yGCRk%2BG3iuMPa6AfEymvKv8DCHQQABoMNjM3NDIzMTgzODA1IgyLoXCvKNUk%2BEHbsgwq3AO%2BPh4Svf9zN4PwAUz1NaFk7crfi6hICi4pKqHKsl%2FQpE%2BJNjLkCIXez8IgL%2FYrrh5IxkdNXrWqv3DPjfSFudWEj5SvMVeXwU%2Bt92GB%2F%2Fbd%2BEj%2FvRPqVXQ27s9dS9GSZfPRbNY1nyMbiiD8FqbFM%2BgcYR0do7LkMF8ZYiouXpvNRC0YsCCV0wYNYuizNiBAKAk64mGyr4RjOHEbk0DBydXDt9ANhUcsU%2BJ1tIZ947lGvLRp7B3Rv6jXuMZ3DePIjI%2BQ5JFLxl3o%2FDoqH8kfb2g%2Fob33xQ832M4YEGxboVEejOaMb6aDUb3q6oPoOYv5XwATJk2zVYRFxIdXMF5buCMDpDkz1NzxvROChfN7THII%2F%2B53%2FX%2BZGvatsHhO3UEU0rlW3A92Pl%2Bj%2F%2Ft2HJOhozMYEFBTbEZh3Qra9Qj2gJ39oTwVDYfU8FML5o1PQPviRJq6X3ol2sHDb9Lqv%2FTifvtoKcwbOZzVsy1Wkp56WxNoQR8eKUtpiT6CORtd3Xb6rSquvvrcXEECfkt0we8GAuXN260aXT%2F%2B5MF6wMoCxNMc50w8X9ZmBFhpcRkPBLhcwmPqhTNM38Z4TeLvG4G6JjmaCfhQ2qbpsCNZ%2FXiGoA%2FTW%2Be5hrQKDckD62eoCDCorKvPBjqkASmWrVitgpvIyxYrqGD340hLplTgnzvPLNrhy0RAQ5bv74bRZcVloIFv9koXhYUowHotQSBJPUgGh1gC52XXzCYuekgjguSpa39plZ41JHkeGD85Qgko4Una%2BkTAfrtbjIs7umzz%2F8YINvCBRPDmgx32DCg1TuByWgJdoO1DbdvezlL7pHdMvkMg6%2FlBKTAnienIB1QQeKXUHC7B2naOhPVVtL%2BC&X-Amz-Signature=7dab700076a4f91d71812666f6d2b14015c9b3fab1ee71a4bd10004e4344c767&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

