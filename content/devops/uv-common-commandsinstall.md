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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKP7H3W4%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHjXXVLlCFJHa2N4pSI8ZfuAEy8gRvcqMobFN%2FZoWknjAiEA1rctnoZItW01Ey5cHhuDFYy4jJVMLpIeeso2kf2itZAqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGm9yrsTquqIamfgLyrcA9%2BRJH4IOXmuh%2FBLiG%2FG5v%2BiI54%2F24JOhOLkCwoGahn0c55WjYsgFVc6LN6e7Imi1WnL7PJ%2FUyIgChPD64qYlzsPHsB6Xy7QCh1rQW4qb%2BWb2kJ69hTMa4PUxzpWmHAsTQDgmFw915I17ylQAgLhYoSlryL54NYcneEs5Od4D%2FTZuSHD1tvuKvrHSpH6v5Hi878Ju1Ef5Iirky%2BkQvBN3EdM5eI8VjhWQJG23%2FDlEwm3UKHpTdVIoej7dHNMBxiPtciNBJshibkjeXwNzvOC2c67bPa5Qqk8k5dhukm0ncgvGrvWF3KODKjkau%2BCHoj7fnkTetNez5vjIVvEB3JqX%2BlgxoNKf1nlfiewKMQnMsvyIwruJhaVWxufEc2s9ruinRnT0oaSDGuEyjZh6OLxH0P3ANj7L%2BbiQbQUP%2B1jk5SFt2AUS1T7fVjDIWSzc4TPd90Gv0mUoKrwBoQT13UnKeiE2QBWJUNzprmI9SDycSAVOC0gwpNKis%2BEdqEMuGP7vbc35cesuFyXvXJ5d87Rx1cooG%2BSfKjuWM2iSgRJsHh7aRARuE%2Bsun12m4F39PoF%2B0xPbNjDpeH2616zZ7ZHeAqSf%2BpGyld2acew0vV2QPAzG4A9AsMDrJcrjmkzMKa8hs8GOqUBIJ7QBdKvYK7KRR6rFIB9Gt5qX9aG54NcGKs5fxYWScvQvSyt7G7QJam2fNzZMcuutkPRjPT3q5DeN4VjnxPtK9GPjdC7LiaK5KUTVkis5viTKZMbetpFPcqVDZ2jAULJpxHxplyZyLVge%2FM4XuqiXmC4V%2FKd%2FDS6Jsys%2FRwwNpacLbKDLnfFVVZyjo1jP62Wb%2FSOfxPH9n2yavCvUhEetp7fIUXr&X-Amz-Signature=71d55aae83ecb0c55f5ebc0d87caa4431c3c16d35c0da1dcbd03f6f19fa19191&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKP7H3W4%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHjXXVLlCFJHa2N4pSI8ZfuAEy8gRvcqMobFN%2FZoWknjAiEA1rctnoZItW01Ey5cHhuDFYy4jJVMLpIeeso2kf2itZAqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGm9yrsTquqIamfgLyrcA9%2BRJH4IOXmuh%2FBLiG%2FG5v%2BiI54%2F24JOhOLkCwoGahn0c55WjYsgFVc6LN6e7Imi1WnL7PJ%2FUyIgChPD64qYlzsPHsB6Xy7QCh1rQW4qb%2BWb2kJ69hTMa4PUxzpWmHAsTQDgmFw915I17ylQAgLhYoSlryL54NYcneEs5Od4D%2FTZuSHD1tvuKvrHSpH6v5Hi878Ju1Ef5Iirky%2BkQvBN3EdM5eI8VjhWQJG23%2FDlEwm3UKHpTdVIoej7dHNMBxiPtciNBJshibkjeXwNzvOC2c67bPa5Qqk8k5dhukm0ncgvGrvWF3KODKjkau%2BCHoj7fnkTetNez5vjIVvEB3JqX%2BlgxoNKf1nlfiewKMQnMsvyIwruJhaVWxufEc2s9ruinRnT0oaSDGuEyjZh6OLxH0P3ANj7L%2BbiQbQUP%2B1jk5SFt2AUS1T7fVjDIWSzc4TPd90Gv0mUoKrwBoQT13UnKeiE2QBWJUNzprmI9SDycSAVOC0gwpNKis%2BEdqEMuGP7vbc35cesuFyXvXJ5d87Rx1cooG%2BSfKjuWM2iSgRJsHh7aRARuE%2Bsun12m4F39PoF%2B0xPbNjDpeH2616zZ7ZHeAqSf%2BpGyld2acew0vV2QPAzG4A9AsMDrJcrjmkzMKa8hs8GOqUBIJ7QBdKvYK7KRR6rFIB9Gt5qX9aG54NcGKs5fxYWScvQvSyt7G7QJam2fNzZMcuutkPRjPT3q5DeN4VjnxPtK9GPjdC7LiaK5KUTVkis5viTKZMbetpFPcqVDZ2jAULJpxHxplyZyLVge%2FM4XuqiXmC4V%2FKd%2FDS6Jsys%2FRwwNpacLbKDLnfFVVZyjo1jP62Wb%2FSOfxPH9n2yavCvUhEetp7fIUXr&X-Amz-Signature=4061761e37f23887f80523ae52e0bfd0bc5a8f6c00a97f6d1f50949dd08b6c13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKP7H3W4%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHjXXVLlCFJHa2N4pSI8ZfuAEy8gRvcqMobFN%2FZoWknjAiEA1rctnoZItW01Ey5cHhuDFYy4jJVMLpIeeso2kf2itZAqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGm9yrsTquqIamfgLyrcA9%2BRJH4IOXmuh%2FBLiG%2FG5v%2BiI54%2F24JOhOLkCwoGahn0c55WjYsgFVc6LN6e7Imi1WnL7PJ%2FUyIgChPD64qYlzsPHsB6Xy7QCh1rQW4qb%2BWb2kJ69hTMa4PUxzpWmHAsTQDgmFw915I17ylQAgLhYoSlryL54NYcneEs5Od4D%2FTZuSHD1tvuKvrHSpH6v5Hi878Ju1Ef5Iirky%2BkQvBN3EdM5eI8VjhWQJG23%2FDlEwm3UKHpTdVIoej7dHNMBxiPtciNBJshibkjeXwNzvOC2c67bPa5Qqk8k5dhukm0ncgvGrvWF3KODKjkau%2BCHoj7fnkTetNez5vjIVvEB3JqX%2BlgxoNKf1nlfiewKMQnMsvyIwruJhaVWxufEc2s9ruinRnT0oaSDGuEyjZh6OLxH0P3ANj7L%2BbiQbQUP%2B1jk5SFt2AUS1T7fVjDIWSzc4TPd90Gv0mUoKrwBoQT13UnKeiE2QBWJUNzprmI9SDycSAVOC0gwpNKis%2BEdqEMuGP7vbc35cesuFyXvXJ5d87Rx1cooG%2BSfKjuWM2iSgRJsHh7aRARuE%2Bsun12m4F39PoF%2B0xPbNjDpeH2616zZ7ZHeAqSf%2BpGyld2acew0vV2QPAzG4A9AsMDrJcrjmkzMKa8hs8GOqUBIJ7QBdKvYK7KRR6rFIB9Gt5qX9aG54NcGKs5fxYWScvQvSyt7G7QJam2fNzZMcuutkPRjPT3q5DeN4VjnxPtK9GPjdC7LiaK5KUTVkis5viTKZMbetpFPcqVDZ2jAULJpxHxplyZyLVge%2FM4XuqiXmC4V%2FKd%2FDS6Jsys%2FRwwNpacLbKDLnfFVVZyjo1jP62Wb%2FSOfxPH9n2yavCvUhEetp7fIUXr&X-Amz-Signature=294253674fbb0e6e46ce1497d1204c845c55f2f4fd0d2f211ea936048118d755&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

