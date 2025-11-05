---
title: Nginx安装 | Nginx详解
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-20T03:10:00.000Z'
draft: false
标签:
- Linux
categories:
- DevOps
---

## 什么是Nginx

> 💡 Nginx (pronounced "engine x") 是一个高性能的HTTP和反向代理服务器，也是一个MAP/POP3/SMTP邮件代理服务器。主要目的是处理静态内容（如 HTML、CSS、JavaScript、图像等），也可以作为负载均衡器和反向代理服务器来处理动态内容。

## Nginx背景科普

## 应用场景

假如说我们公司产品刚上线的时候并发量特别小, 访问的用户的话比较少, 一个jar包就完全够用了, 然后内部tomcat返回内容给用户, 那客户端来访问, 我们Tomcat给它返回出去。那压力不大的情况下还是比较快的。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f8a7bd3f-5cae-45ea-b64b-f2fe864dd020/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB6RI6EV%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs4FzgpW6BbvSIylMKi0B8fVtCoWyglbCUGgqM6P9w8QIhANgAnylG%2BAm2zV8zKEIDInoJsrejrAYin%2Bb0zgJiXTOWKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzrHLbX3QNiJzK59%2BMq3AOP5iijKX0DvnA%2FoOqyLEGowUjD6I4BAbLCuTwl5pEEAcuZ0Mb1VYhOEwvfBwUI7hSK%2FfHBzoH%2Bdahq6z6wtU7A2IZpmF90tV5dKTp8KRVTNOfpbm%2FtEP5Go4b8ymYIovTaUeKdpmBJWXw%2BrgCxdVDJRQpXF3Tbu142Wlx4O%2FWN4p0CuOkryzU7pAfuC7ABwBRXmoJb0eMZgXV8eUeZgDICzwl91lE5ucn8ievwuA%2BmghhEprHfx367z0U2NkAcxu3VgxIPracS3RNZITrbC%2BvKN526UrCMc6rVhUqZs2JnCanxwJeR8nnCy0gSu%2FvxBkUodKuTP03Hfa%2BCBd704BsxvO5z9N8t5jsLF328vDnaAj2gmUankOsGJa6AFS0nfca5L7%2F7GhBOF39%2FMCy41KMe7c8dCF0Z1pmfcwWb78xcGVet3gw3JCwm%2F4PUOrD6S%2FOsRqyUQui2imPUbXlKGsufj50x2LPacvYGkM7fQ2zqSNYfuiF8hLXI6MLOyHBAsSysPcpTIvW1wgeAxUVV%2FDAVUxtisrCuktkmJnUJSXoXj488CQIFkFD9xCMt18G6nN32zSdlylHhO%2Bkh5cNCcBKN2rxkqhvNIo13pvqe4BA5bQf7ssYgGLPcRMXu6DDLoqzIBjqkAS98mf0uLSIakm3erf0DrhjdxQuGHiNC7PsDaf6iOhWxqbve%2B%2BFHNc1RP4QUL39rGbABlgoqFrRj%2FKZrqqTzBWpMgVk0JI1e4BWRFTy9ZLJXMQNkLGLrDEaz5vemBSIJhLiy3ebSAetuaniPSAUy8E7zoUkWptKMu52JTJGbv2anRCj39ew%2FoX0AgOinbUWkpM5eJm%2BVKyfxkwY0zv4JqlMrxuiz&X-Amz-Signature=6f1c02e7d027184ea32aa0b8aaa9150664688dd3074fd84098e457f662e99948&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



但是随着我们的项目逐渐成熟用的人也越来越多，并发量慢慢增大了，这时候一台服务器满足不了我们的需求了，如果还坚持用Tomcat的方法就会导致我们的服务器超出承载范围导致服务器崩溃，会给公司造成一定的经济损失。



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e18d0097-d421-45d6-9b57-fa533675b872/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB6RI6EV%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs4FzgpW6BbvSIylMKi0B8fVtCoWyglbCUGgqM6P9w8QIhANgAnylG%2BAm2zV8zKEIDInoJsrejrAYin%2Bb0zgJiXTOWKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzrHLbX3QNiJzK59%2BMq3AOP5iijKX0DvnA%2FoOqyLEGowUjD6I4BAbLCuTwl5pEEAcuZ0Mb1VYhOEwvfBwUI7hSK%2FfHBzoH%2Bdahq6z6wtU7A2IZpmF90tV5dKTp8KRVTNOfpbm%2FtEP5Go4b8ymYIovTaUeKdpmBJWXw%2BrgCxdVDJRQpXF3Tbu142Wlx4O%2FWN4p0CuOkryzU7pAfuC7ABwBRXmoJb0eMZgXV8eUeZgDICzwl91lE5ucn8ievwuA%2BmghhEprHfx367z0U2NkAcxu3VgxIPracS3RNZITrbC%2BvKN526UrCMc6rVhUqZs2JnCanxwJeR8nnCy0gSu%2FvxBkUodKuTP03Hfa%2BCBd704BsxvO5z9N8t5jsLF328vDnaAj2gmUankOsGJa6AFS0nfca5L7%2F7GhBOF39%2FMCy41KMe7c8dCF0Z1pmfcwWb78xcGVet3gw3JCwm%2F4PUOrD6S%2FOsRqyUQui2imPUbXlKGsufj50x2LPacvYGkM7fQ2zqSNYfuiF8hLXI6MLOyHBAsSysPcpTIvW1wgeAxUVV%2FDAVUxtisrCuktkmJnUJSXoXj488CQIFkFD9xCMt18G6nN32zSdlylHhO%2Bkh5cNCcBKN2rxkqhvNIo13pvqe4BA5bQf7ssYgGLPcRMXu6DDLoqzIBjqkAS98mf0uLSIakm3erf0DrhjdxQuGHiNC7PsDaf6iOhWxqbve%2B%2BFHNc1RP4QUL39rGbABlgoqFrRj%2FKZrqqTzBWpMgVk0JI1e4BWRFTy9ZLJXMQNkLGLrDEaz5vemBSIJhLiy3ebSAetuaniPSAUy8E7zoUkWptKMu52JTJGbv2anRCj39ew%2FoX0AgOinbUWkpM5eJm%2BVKyfxkwY0zv4JqlMrxuiz&X-Amz-Signature=be53fac02ebc0dd7b31e0d1687ffb52898e05ee979c9857b7a579ce60e8a3753&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



如果遇到这种问题最笨的方法是直接去横向扩展服务器就好了，比如说我们加了一台, 加了两台, 加了三台。那加了三台服务器之后呢, 我们的Tomcat就跑到了多台服务器上，但是跑在多个服务器上，我们的用户访问方式是一个一个去访问的，那肯定就乱套了，因为Session的话, 它是不共享的，这个时候几个项目启动在不同的服务器上，用户要访问，就需要增加一个代理服务器了，通过代理服务器来帮我们转发和处理请求，我们希望这个代理服务器可以帮助我们接收用户的请求，然后将用户的请求按照规则帮我们转发到不同的服务器节点之上。这个过程用户是无感知的，用户并不知道是哪个服务器返回的结果，我们还希望他可以按照服务器的性能提供不同的权重选择。保证最佳体验！所以我们使用了Nginx！



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ecd4eda1-0259-405a-b4b8-0ee8d108dbb5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB6RI6EV%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs4FzgpW6BbvSIylMKi0B8fVtCoWyglbCUGgqM6P9w8QIhANgAnylG%2BAm2zV8zKEIDInoJsrejrAYin%2Bb0zgJiXTOWKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzrHLbX3QNiJzK59%2BMq3AOP5iijKX0DvnA%2FoOqyLEGowUjD6I4BAbLCuTwl5pEEAcuZ0Mb1VYhOEwvfBwUI7hSK%2FfHBzoH%2Bdahq6z6wtU7A2IZpmF90tV5dKTp8KRVTNOfpbm%2FtEP5Go4b8ymYIovTaUeKdpmBJWXw%2BrgCxdVDJRQpXF3Tbu142Wlx4O%2FWN4p0CuOkryzU7pAfuC7ABwBRXmoJb0eMZgXV8eUeZgDICzwl91lE5ucn8ievwuA%2BmghhEprHfx367z0U2NkAcxu3VgxIPracS3RNZITrbC%2BvKN526UrCMc6rVhUqZs2JnCanxwJeR8nnCy0gSu%2FvxBkUodKuTP03Hfa%2BCBd704BsxvO5z9N8t5jsLF328vDnaAj2gmUankOsGJa6AFS0nfca5L7%2F7GhBOF39%2FMCy41KMe7c8dCF0Z1pmfcwWb78xcGVet3gw3JCwm%2F4PUOrD6S%2FOsRqyUQui2imPUbXlKGsufj50x2LPacvYGkM7fQ2zqSNYfuiF8hLXI6MLOyHBAsSysPcpTIvW1wgeAxUVV%2FDAVUxtisrCuktkmJnUJSXoXj488CQIFkFD9xCMt18G6nN32zSdlylHhO%2Bkh5cNCcBKN2rxkqhvNIo13pvqe4BA5bQf7ssYgGLPcRMXu6DDLoqzIBjqkAS98mf0uLSIakm3erf0DrhjdxQuGHiNC7PsDaf6iOhWxqbve%2B%2BFHNc1RP4QUL39rGbABlgoqFrRj%2FKZrqqTzBWpMgVk0JI1e4BWRFTy9ZLJXMQNkLGLrDEaz5vemBSIJhLiy3ebSAetuaniPSAUy8E7zoUkWptKMu52JTJGbv2anRCj39ew%2FoX0AgOinbUWkpM5eJm%2BVKyfxkwY0zv4JqlMrxuiz&X-Amz-Signature=843e0dea04d88ce8c5f18f9b7fb89c5045095e0994be2b0e4f4a750103455fbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



---

# Nginx主要实现的三个功能

### 反向代理

- 正向代理是代理我们的客户端的，而反向代理是代理我们的服务器端的，让客户无感知的游览我们一些服务器资源。
### 负载均衡

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4c052bfc-ce0a-47ca-adc7-4939f2ac9280/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB6RI6EV%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs4FzgpW6BbvSIylMKi0B8fVtCoWyglbCUGgqM6P9w8QIhANgAnylG%2BAm2zV8zKEIDInoJsrejrAYin%2Bb0zgJiXTOWKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzrHLbX3QNiJzK59%2BMq3AOP5iijKX0DvnA%2FoOqyLEGowUjD6I4BAbLCuTwl5pEEAcuZ0Mb1VYhOEwvfBwUI7hSK%2FfHBzoH%2Bdahq6z6wtU7A2IZpmF90tV5dKTp8KRVTNOfpbm%2FtEP5Go4b8ymYIovTaUeKdpmBJWXw%2BrgCxdVDJRQpXF3Tbu142Wlx4O%2FWN4p0CuOkryzU7pAfuC7ABwBRXmoJb0eMZgXV8eUeZgDICzwl91lE5ucn8ievwuA%2BmghhEprHfx367z0U2NkAcxu3VgxIPracS3RNZITrbC%2BvKN526UrCMc6rVhUqZs2JnCanxwJeR8nnCy0gSu%2FvxBkUodKuTP03Hfa%2BCBd704BsxvO5z9N8t5jsLF328vDnaAj2gmUankOsGJa6AFS0nfca5L7%2F7GhBOF39%2FMCy41KMe7c8dCF0Z1pmfcwWb78xcGVet3gw3JCwm%2F4PUOrD6S%2FOsRqyUQui2imPUbXlKGsufj50x2LPacvYGkM7fQ2zqSNYfuiF8hLXI6MLOyHBAsSysPcpTIvW1wgeAxUVV%2FDAVUxtisrCuktkmJnUJSXoXj488CQIFkFD9xCMt18G6nN32zSdlylHhO%2Bkh5cNCcBKN2rxkqhvNIo13pvqe4BA5bQf7ssYgGLPcRMXu6DDLoqzIBjqkAS98mf0uLSIakm3erf0DrhjdxQuGHiNC7PsDaf6iOhWxqbve%2B%2BFHNc1RP4QUL39rGbABlgoqFrRj%2FKZrqqTzBWpMgVk0JI1e4BWRFTy9ZLJXMQNkLGLrDEaz5vemBSIJhLiy3ebSAetuaniPSAUy8E7zoUkWptKMu52JTJGbv2anRCj39ew%2FoX0AgOinbUWkpM5eJm%2BVKyfxkwY0zv4JqlMrxuiz&X-Amz-Signature=918137cb3019a94becff4eb157728c9797d356d6b5060d9ecad84c9c080b7cc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

比如说我们这个地方有64G, 16G, 8G的服务器, 我们希望更多的请求能够达到咱们64G的服务器，更少的请求达到16G和8G的服务器, 那Nginx也具备咱们负载均衡的功能, 它有一些类似的策略, 比如说轮循跟加强轮重, 比如说我们这个64G的服务器比较牛, 所以说它的权重就更高。那如果有很多请求达进来的话, 那大量的请求都会走到64G的服务器里, 那可能只有一部分请求能进入咱们一些权重比较小的服务器, 这样的话来保证我们服务器的性能最大化, 哪怕我们有台很小的服务器也可以上线去使用, 可以节约成本。



### 动静分离

动静分离，在我们的软件开发中，有些请求是需要后台处理的，有些请求是不需要经过后台处理的（如：css、html、jpg、js等等文件），这些不需要经过后台处理的文件称为静态文件。让动态网站里的动态网页根据一定规则把不变的资源和经常变的资源区分开来，动静资源做好了拆分以后，我们就可以根据静态资源的特点将其做缓存操作。提高资源响应的速度



那这就是咱们Nginx三个主要的功能的一个介绍。第一个是咱们的反向代理。第二个是一个负载均衡。第三个是一个静态分离。在我们正常的工作开发中, 这些三个请求是经常可以使用到的

---

## Nginx安装

### windows上安装Nginx

进入黑窗口后输入nginx.exe

它是没输出日志的，那怎么样子判断它启动成功了呢？

我们可以在游览器上来访问一下咱们本地的localhost80端口

只要出现Welcome to nginx!就说明安装成功了

这是就是一个windows安装的教程

### Linux上安装Nginx

### 坑

## Nginx常用命令

```javascript
1. `cd /usr/local/nginx/sbin/`
2. `./nginx 启动`
3. `./nginx -s stop 停止`
4. `./nginx -s quit 安全退出`
5. `./nginx -s reload 重新加载配置文件`
6. `ps aux|grep nginx 查看nginx进程`
```

> Reference







