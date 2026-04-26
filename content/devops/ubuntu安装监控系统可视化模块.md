---
title: Ubuntu安装监控系统可视化模块
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-20T03:10:00.000Z'
draft: false
tags:
- Linux
- Ubuntu
categories:
- DevOps
---

Prometheus是一个开放性的监控解决方案，用户可以非常方便的安装和使用Prometheus并且能够非常方便的对其进行扩展。为了能够更加直观的了解Prometheus Server，接下来我们将在本地部署并运行一个Prometheus Server实例，通过Node Exporter采集当前主机的系统资源使用情况。 并通过Grafana创建一个简单的可视化仪表盘。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAIWX4NZ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHfpzJhQnpZ8gWyAncMWNzlY8%2B9EJScVaj63KXjEnRgIhAMsYLwkYr2V048f0A%2Bkge%2FgKf%2BMBTfAyi5A0Hkw7D2rhKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfhFqs%2FiQO2wOFDEIq3ANIzGK6YpZ6Zpf2dM4GxVWaDU3wMGFTSf9raVRgDn0EF%2B2CeCkrXStV9IjJMic3Q292aZ18%2F8o7tRAMsu4%2Fdu%2B0Dl4TOb8gu6eLwW3Wh1Uww1K7YEkcXl3poPDFRTq0Vrp0T4AhELmkjV%2BiTjZ5Bdr6BdTqtQ%2BRDMbVJCcQQ3rckZX7McfAE1%2BEZWqYcSuRB7QYBSHkLut3tip3YVLjurp44%2FfqBw1SN7A3yz0zEKQ5nAIe3rqqFH6OOpHzRgVRLEK7U40Tz6MRPRH1JNu06ksX2D00jhYmRamEveXLTUdKZZiV0K%2FBm6kXWHhaD7mZurqDZ%2BJxc6CbMDRGS4pIas6DpjCDXsmo47dWZptlSPI0P2i%2FU6uNE1lP0uMsIdX4sQ9t3MFeKAO1OymZlI%2FtbBPC1sFVP%2BLru9HfqIeIjMv6ncnNxqizDyw5rYzvtLj%2BFalVqqZYaxptNVXnEZjtC8gHwNhhMHN7QxgxVp86BtIWSxb6C9Wi6%2BiC9hkOeS6ueBjkeCSoOAyKQ34aiuUIaDNin8P9GpsTq3XhYoYt8tqtqX%2FgQyOwKcfr17Rc2vie3dFGIrjSfEBW4HAouO1r2QsZxXN7KT3KBD%2FwowP1kWfBlZwsugf98%2FLLjQWW7zD3jrbPBjqkAWWJt1ooD0SLl%2FQdrVUTvQwpcPoMUvXaLBO8tMn47EZ3PRe%2FeqI7N%2B8vrR3SMbu0VgwwnXBQfGOFECSKsZMJWf%2BMo9TQ%2BcYi5vkwcckFnnl5iI5AOmg0WNa4EA8gEi80Fz20czRUzGJ2HYvWQV8AwB9xClUoVHkrZ%2BaWasqrfXDJh%2FRAijYtvdI7d9wCk5hN1DULxXz2HDGrZTRxKgd%2Bm8AB45Q5&X-Amz-Signature=1874ad3010011fc0814f4a00cd6aaab2f74815a1bdcc53ec5b2ca45f02012e50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> Prometheus是什么？

### 下载Prometheus

- 下载链接
### 安装Prometheus

- 解压
### 修改Prometheus配置

- 进入文件目标, 并修改配置
- 将以下内容放置在配置文件内
- 启动服务
### 在web浏览器查看

- localhost:9090
---

> Monitoring Linux host metrics with the Node Exporter

### 下载Node Exporter

- 下载地址
### 安装 & RUN

```shell
tar xvfz node_exporter-*.*-amd64.tar.gz
cd node_exporter-*.*-amd64
./node_exporter
```

### 在web浏览器查看

- http://localhost:9100/
---

> What is Grafana

### 安装Grafana

### Ubuntu安装流程

```shell
# 更新apt-getsudo apt-get install -y adduser libfontconfig1 musl
# 下载软件wget https://dl.grafana.com/enterprise/release/grafana-enterprise_10.0.0_amd64.deb
# 安装sudo dpkg -i grafana-enterprise_10.0.0_amd64.deb
```

- 操作系统不是Ubuntu则查看上面的链接, 根据自身系统进行安装
### RUN Grafana

- 运行Grafana可视化服务
```shell
sudo /bin/systemctl start grafana-server
```

### 在web浏览器查看

- http://localhost:3000/
- 设置流程如下:
step-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAIWX4NZ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHfpzJhQnpZ8gWyAncMWNzlY8%2B9EJScVaj63KXjEnRgIhAMsYLwkYr2V048f0A%2Bkge%2FgKf%2BMBTfAyi5A0Hkw7D2rhKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfhFqs%2FiQO2wOFDEIq3ANIzGK6YpZ6Zpf2dM4GxVWaDU3wMGFTSf9raVRgDn0EF%2B2CeCkrXStV9IjJMic3Q292aZ18%2F8o7tRAMsu4%2Fdu%2B0Dl4TOb8gu6eLwW3Wh1Uww1K7YEkcXl3poPDFRTq0Vrp0T4AhELmkjV%2BiTjZ5Bdr6BdTqtQ%2BRDMbVJCcQQ3rckZX7McfAE1%2BEZWqYcSuRB7QYBSHkLut3tip3YVLjurp44%2FfqBw1SN7A3yz0zEKQ5nAIe3rqqFH6OOpHzRgVRLEK7U40Tz6MRPRH1JNu06ksX2D00jhYmRamEveXLTUdKZZiV0K%2FBm6kXWHhaD7mZurqDZ%2BJxc6CbMDRGS4pIas6DpjCDXsmo47dWZptlSPI0P2i%2FU6uNE1lP0uMsIdX4sQ9t3MFeKAO1OymZlI%2FtbBPC1sFVP%2BLru9HfqIeIjMv6ncnNxqizDyw5rYzvtLj%2BFalVqqZYaxptNVXnEZjtC8gHwNhhMHN7QxgxVp86BtIWSxb6C9Wi6%2BiC9hkOeS6ueBjkeCSoOAyKQ34aiuUIaDNin8P9GpsTq3XhYoYt8tqtqX%2FgQyOwKcfr17Rc2vie3dFGIrjSfEBW4HAouO1r2QsZxXN7KT3KBD%2FwowP1kWfBlZwsugf98%2FLLjQWW7zD3jrbPBjqkAWWJt1ooD0SLl%2FQdrVUTvQwpcPoMUvXaLBO8tMn47EZ3PRe%2FeqI7N%2B8vrR3SMbu0VgwwnXBQfGOFECSKsZMJWf%2BMo9TQ%2BcYi5vkwcckFnnl5iI5AOmg0WNa4EA8gEi80Fz20czRUzGJ2HYvWQV8AwB9xClUoVHkrZ%2BaWasqrfXDJh%2FRAijYtvdI7d9wCk5hN1DULxXz2HDGrZTRxKgd%2Bm8AB45Q5&X-Amz-Signature=0fb713f07cb3d7f54f960058e340fb9d881ebe08a44fda31dfb2e6626fdc9d31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAIWX4NZ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHfpzJhQnpZ8gWyAncMWNzlY8%2B9EJScVaj63KXjEnRgIhAMsYLwkYr2V048f0A%2Bkge%2FgKf%2BMBTfAyi5A0Hkw7D2rhKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfhFqs%2FiQO2wOFDEIq3ANIzGK6YpZ6Zpf2dM4GxVWaDU3wMGFTSf9raVRgDn0EF%2B2CeCkrXStV9IjJMic3Q292aZ18%2F8o7tRAMsu4%2Fdu%2B0Dl4TOb8gu6eLwW3Wh1Uww1K7YEkcXl3poPDFRTq0Vrp0T4AhELmkjV%2BiTjZ5Bdr6BdTqtQ%2BRDMbVJCcQQ3rckZX7McfAE1%2BEZWqYcSuRB7QYBSHkLut3tip3YVLjurp44%2FfqBw1SN7A3yz0zEKQ5nAIe3rqqFH6OOpHzRgVRLEK7U40Tz6MRPRH1JNu06ksX2D00jhYmRamEveXLTUdKZZiV0K%2FBm6kXWHhaD7mZurqDZ%2BJxc6CbMDRGS4pIas6DpjCDXsmo47dWZptlSPI0P2i%2FU6uNE1lP0uMsIdX4sQ9t3MFeKAO1OymZlI%2FtbBPC1sFVP%2BLru9HfqIeIjMv6ncnNxqizDyw5rYzvtLj%2BFalVqqZYaxptNVXnEZjtC8gHwNhhMHN7QxgxVp86BtIWSxb6C9Wi6%2BiC9hkOeS6ueBjkeCSoOAyKQ34aiuUIaDNin8P9GpsTq3XhYoYt8tqtqX%2FgQyOwKcfr17Rc2vie3dFGIrjSfEBW4HAouO1r2QsZxXN7KT3KBD%2FwowP1kWfBlZwsugf98%2FLLjQWW7zD3jrbPBjqkAWWJt1ooD0SLl%2FQdrVUTvQwpcPoMUvXaLBO8tMn47EZ3PRe%2FeqI7N%2B8vrR3SMbu0VgwwnXBQfGOFECSKsZMJWf%2BMo9TQ%2BcYi5vkwcckFnnl5iI5AOmg0WNa4EA8gEi80Fz20czRUzGJ2HYvWQV8AwB9xClUoVHkrZ%2BaWasqrfXDJh%2FRAijYtvdI7d9wCk5hN1DULxXz2HDGrZTRxKgd%2Bm8AB45Q5&X-Amz-Signature=0e3009efb825137d74ee852ceb2355e74e7e65359c967b1d5490916e40375986&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAIWX4NZ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHfpzJhQnpZ8gWyAncMWNzlY8%2B9EJScVaj63KXjEnRgIhAMsYLwkYr2V048f0A%2Bkge%2FgKf%2BMBTfAyi5A0Hkw7D2rhKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfhFqs%2FiQO2wOFDEIq3ANIzGK6YpZ6Zpf2dM4GxVWaDU3wMGFTSf9raVRgDn0EF%2B2CeCkrXStV9IjJMic3Q292aZ18%2F8o7tRAMsu4%2Fdu%2B0Dl4TOb8gu6eLwW3Wh1Uww1K7YEkcXl3poPDFRTq0Vrp0T4AhELmkjV%2BiTjZ5Bdr6BdTqtQ%2BRDMbVJCcQQ3rckZX7McfAE1%2BEZWqYcSuRB7QYBSHkLut3tip3YVLjurp44%2FfqBw1SN7A3yz0zEKQ5nAIe3rqqFH6OOpHzRgVRLEK7U40Tz6MRPRH1JNu06ksX2D00jhYmRamEveXLTUdKZZiV0K%2FBm6kXWHhaD7mZurqDZ%2BJxc6CbMDRGS4pIas6DpjCDXsmo47dWZptlSPI0P2i%2FU6uNE1lP0uMsIdX4sQ9t3MFeKAO1OymZlI%2FtbBPC1sFVP%2BLru9HfqIeIjMv6ncnNxqizDyw5rYzvtLj%2BFalVqqZYaxptNVXnEZjtC8gHwNhhMHN7QxgxVp86BtIWSxb6C9Wi6%2BiC9hkOeS6ueBjkeCSoOAyKQ34aiuUIaDNin8P9GpsTq3XhYoYt8tqtqX%2FgQyOwKcfr17Rc2vie3dFGIrjSfEBW4HAouO1r2QsZxXN7KT3KBD%2FwowP1kWfBlZwsugf98%2FLLjQWW7zD3jrbPBjqkAWWJt1ooD0SLl%2FQdrVUTvQwpcPoMUvXaLBO8tMn47EZ3PRe%2FeqI7N%2B8vrR3SMbu0VgwwnXBQfGOFECSKsZMJWf%2BMo9TQ%2BcYi5vkwcckFnnl5iI5AOmg0WNa4EA8gEi80Fz20czRUzGJ2HYvWQV8AwB9xClUoVHkrZ%2BaWasqrfXDJh%2FRAijYtvdI7d9wCk5hN1DULxXz2HDGrZTRxKgd%2Bm8AB45Q5&X-Amz-Signature=ebffc3527efccdc6b3d2594012f857916bbf0aeebca44e1448bf234ddf1395ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAIWX4NZ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHfpzJhQnpZ8gWyAncMWNzlY8%2B9EJScVaj63KXjEnRgIhAMsYLwkYr2V048f0A%2Bkge%2FgKf%2BMBTfAyi5A0Hkw7D2rhKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfhFqs%2FiQO2wOFDEIq3ANIzGK6YpZ6Zpf2dM4GxVWaDU3wMGFTSf9raVRgDn0EF%2B2CeCkrXStV9IjJMic3Q292aZ18%2F8o7tRAMsu4%2Fdu%2B0Dl4TOb8gu6eLwW3Wh1Uww1K7YEkcXl3poPDFRTq0Vrp0T4AhELmkjV%2BiTjZ5Bdr6BdTqtQ%2BRDMbVJCcQQ3rckZX7McfAE1%2BEZWqYcSuRB7QYBSHkLut3tip3YVLjurp44%2FfqBw1SN7A3yz0zEKQ5nAIe3rqqFH6OOpHzRgVRLEK7U40Tz6MRPRH1JNu06ksX2D00jhYmRamEveXLTUdKZZiV0K%2FBm6kXWHhaD7mZurqDZ%2BJxc6CbMDRGS4pIas6DpjCDXsmo47dWZptlSPI0P2i%2FU6uNE1lP0uMsIdX4sQ9t3MFeKAO1OymZlI%2FtbBPC1sFVP%2BLru9HfqIeIjMv6ncnNxqizDyw5rYzvtLj%2BFalVqqZYaxptNVXnEZjtC8gHwNhhMHN7QxgxVp86BtIWSxb6C9Wi6%2BiC9hkOeS6ueBjkeCSoOAyKQ34aiuUIaDNin8P9GpsTq3XhYoYt8tqtqX%2FgQyOwKcfr17Rc2vie3dFGIrjSfEBW4HAouO1r2QsZxXN7KT3KBD%2FwowP1kWfBlZwsugf98%2FLLjQWW7zD3jrbPBjqkAWWJt1ooD0SLl%2FQdrVUTvQwpcPoMUvXaLBO8tMn47EZ3PRe%2FeqI7N%2B8vrR3SMbu0VgwwnXBQfGOFECSKsZMJWf%2BMo9TQ%2BcYi5vkwcckFnnl5iI5AOmg0WNa4EA8gEi80Fz20czRUzGJ2HYvWQV8AwB9xClUoVHkrZ%2BaWasqrfXDJh%2FRAijYtvdI7d9wCk5hN1DULxXz2HDGrZTRxKgd%2Bm8AB45Q5&X-Amz-Signature=c566e39a92d1f3504bbf5a0823c98fb94fa153cb2eaf2ef4563cf321d22cb40b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAIWX4NZ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHfpzJhQnpZ8gWyAncMWNzlY8%2B9EJScVaj63KXjEnRgIhAMsYLwkYr2V048f0A%2Bkge%2FgKf%2BMBTfAyi5A0Hkw7D2rhKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfhFqs%2FiQO2wOFDEIq3ANIzGK6YpZ6Zpf2dM4GxVWaDU3wMGFTSf9raVRgDn0EF%2B2CeCkrXStV9IjJMic3Q292aZ18%2F8o7tRAMsu4%2Fdu%2B0Dl4TOb8gu6eLwW3Wh1Uww1K7YEkcXl3poPDFRTq0Vrp0T4AhELmkjV%2BiTjZ5Bdr6BdTqtQ%2BRDMbVJCcQQ3rckZX7McfAE1%2BEZWqYcSuRB7QYBSHkLut3tip3YVLjurp44%2FfqBw1SN7A3yz0zEKQ5nAIe3rqqFH6OOpHzRgVRLEK7U40Tz6MRPRH1JNu06ksX2D00jhYmRamEveXLTUdKZZiV0K%2FBm6kXWHhaD7mZurqDZ%2BJxc6CbMDRGS4pIas6DpjCDXsmo47dWZptlSPI0P2i%2FU6uNE1lP0uMsIdX4sQ9t3MFeKAO1OymZlI%2FtbBPC1sFVP%2BLru9HfqIeIjMv6ncnNxqizDyw5rYzvtLj%2BFalVqqZYaxptNVXnEZjtC8gHwNhhMHN7QxgxVp86BtIWSxb6C9Wi6%2BiC9hkOeS6ueBjkeCSoOAyKQ34aiuUIaDNin8P9GpsTq3XhYoYt8tqtqX%2FgQyOwKcfr17Rc2vie3dFGIrjSfEBW4HAouO1r2QsZxXN7KT3KBD%2FwowP1kWfBlZwsugf98%2FLLjQWW7zD3jrbPBjqkAWWJt1ooD0SLl%2FQdrVUTvQwpcPoMUvXaLBO8tMn47EZ3PRe%2FeqI7N%2B8vrR3SMbu0VgwwnXBQfGOFECSKsZMJWf%2BMo9TQ%2BcYi5vkwcckFnnl5iI5AOmg0WNa4EA8gEi80Fz20czRUzGJ2HYvWQV8AwB9xClUoVHkrZ%2BaWasqrfXDJh%2FRAijYtvdI7d9wCk5hN1DULxXz2HDGrZTRxKgd%2Bm8AB45Q5&X-Amz-Signature=0421e1606adba065951583336b470ab269292b8e13e6edb76db18a060b70d2b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAIWX4NZ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHfpzJhQnpZ8gWyAncMWNzlY8%2B9EJScVaj63KXjEnRgIhAMsYLwkYr2V048f0A%2Bkge%2FgKf%2BMBTfAyi5A0Hkw7D2rhKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfhFqs%2FiQO2wOFDEIq3ANIzGK6YpZ6Zpf2dM4GxVWaDU3wMGFTSf9raVRgDn0EF%2B2CeCkrXStV9IjJMic3Q292aZ18%2F8o7tRAMsu4%2Fdu%2B0Dl4TOb8gu6eLwW3Wh1Uww1K7YEkcXl3poPDFRTq0Vrp0T4AhELmkjV%2BiTjZ5Bdr6BdTqtQ%2BRDMbVJCcQQ3rckZX7McfAE1%2BEZWqYcSuRB7QYBSHkLut3tip3YVLjurp44%2FfqBw1SN7A3yz0zEKQ5nAIe3rqqFH6OOpHzRgVRLEK7U40Tz6MRPRH1JNu06ksX2D00jhYmRamEveXLTUdKZZiV0K%2FBm6kXWHhaD7mZurqDZ%2BJxc6CbMDRGS4pIas6DpjCDXsmo47dWZptlSPI0P2i%2FU6uNE1lP0uMsIdX4sQ9t3MFeKAO1OymZlI%2FtbBPC1sFVP%2BLru9HfqIeIjMv6ncnNxqizDyw5rYzvtLj%2BFalVqqZYaxptNVXnEZjtC8gHwNhhMHN7QxgxVp86BtIWSxb6C9Wi6%2BiC9hkOeS6ueBjkeCSoOAyKQ34aiuUIaDNin8P9GpsTq3XhYoYt8tqtqX%2FgQyOwKcfr17Rc2vie3dFGIrjSfEBW4HAouO1r2QsZxXN7KT3KBD%2FwowP1kWfBlZwsugf98%2FLLjQWW7zD3jrbPBjqkAWWJt1ooD0SLl%2FQdrVUTvQwpcPoMUvXaLBO8tMn47EZ3PRe%2FeqI7N%2B8vrR3SMbu0VgwwnXBQfGOFECSKsZMJWf%2BMo9TQ%2BcYi5vkwcckFnnl5iI5AOmg0WNa4EA8gEi80Fz20czRUzGJ2HYvWQV8AwB9xClUoVHkrZ%2BaWasqrfXDJh%2FRAijYtvdI7d9wCk5hN1DULxXz2HDGrZTRxKgd%2Bm8AB45Q5&X-Amz-Signature=1899dcfa25c0ff754e781a2cdb1e26cc6ac9540adf6d5b678c0bb5ee88482e1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> 参考链接

### 拓展代码

- 安装Prometheus
```shell
# 下载export VERSION=2.13.0
curl -LO  https://github.com/prometheus/prometheus/releases/download/v$VERSION/prometheus-$VERSION.darwin-amd64.tar.gz
# 解压tar -xzf prometheus-${VERSION}.darwin-amd64.tar.gz
cd prometheus-${VERSION}.darwin-amd64
# 配置promethes.ymlvim promethes.yml
# 运行./prometheus
```

- 安装Node Exporter
```shell
# 下载curl -OL https://github.com/prometheus/node_exporter/releases/download/v0.17.0/node_exporter-0.17.0.linux-amd64.tar.gz
# 解压tar -xzf node_exporter-0.17.0.linux-amd64.tar.gz
# 将 node_exporter 工具安装到系统中，使其可以被全局访问和使用。cd node_exporter-0.17.0.linux-amd64/
mv node_exporter /usr/local/bin/
# 运行service node_exporter start
```

