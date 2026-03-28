---
title: LibreOffice-Docker部署问题记录
date: '2026-03-27T06:56:00.000Z'
lastmod: '2026-03-27T06:57:00.000Z'
draft: false
categories:
- 其他
---

# LibreOffice Docker 部署问题记录

## 背景

项目使用 LibreOffice 将 xlsx 文件转换为 PDF。
Windows 本地测试正常，部署到 Linux Docker 容器后出现一系列问题。

---

## 问题一：PDF 文件大小不一致

### 现象

同一份数据，Windows 本地生成的 PDF 比服务器生成的小约 25–35%。

### 原因

两端 LibreOffice 版本不同：

不同版本的 PDF 导出引擎在压缩算法和字体嵌入上有差异，导致文件大小不同。

### 解决方法

在 Dockerfile 中从 TDF 官网下载指定版本，而不是用 apt-get install libreoffice（apt 源版本无法控制）：

```docker
RUN wget -q "https://download.documentfoundation.org/libreoffice/stable/26.2.2/deb/x86_64/LibreOffice_26.2.2_Linux_x86-64_deb.tar.gz" -O /tmp/lo.tar.gz \
    && tar -xzf /tmp/lo.tar.gz -C /tmp/ \
    && apt-get update \
    && dpkg -i /tmp/LibreOffice_26*/DEBS/*.deb || apt-get install -f -y --no-install-recommends \
    && ln -sf /opt/libreoffice26.2/program/soffice /usr/bin/soffice \
    && rm -rf /tmp/lo.tar.gz /tmp/LibreOffice_26* \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
```

> TDF 版本下载地址规律：https://download.documentfoundation.org/libreoffice/stable/{版本号}/deb/x86_64/

---

## 问题二：容器内找不到 LibreOffice（未找到 soffice）

### 现象

```plain text
[警告] 未找到 LibreOffice，跳过 PDF 转换（发票）
```

### 原因

1. TDF 方式安装后，可执行文件路径为 /opt/libreoffice26.2/program/soffice，不在 PATH 中
1. 代码中的候选路径列表只有 Windows 路径，没有 Linux TDF 路径
### 解决方法

① Dockerfile 中手动创建软链接：

```docker
RUN ln -sf /opt/libreoffice26.2/program/soffice /usr/bin/soffice
```

② 代码中补充 Linux 候选路径（pdf_export.py）：

```python
_SOFFICE_CANDIDATES = [
    'soffice',
    r'C:\Program Files\LibreOffice\program\soffice.exe',
    '/usr/bin/soffice',
    '/usr/lib/libreoffice/program/soffice',
    '/opt/libreoffice26.2/program/soffice',
    '/opt/libreoffice25.2/program/soffice',
]
```

---

## 问题三：缺少系统动态库（连续报 cannot open shared object file）

### 现象

依次出现以下错误（每次构建解决一个，下次又出现新的）：

```plain text
libXinerama.so.1: cannot open shared object file: No such file or directory
libssl3.so: cannot open shared object file: No such file or directory
libX11-xcb.so.1: cannot open shared object file: No such file or directory
```

### 原因

使用了 python:3.13-slim 作为基础镜像。slim 版本裁掉了大量系统库，而 LibreOffice 运行时依赖几十个 X11/系统库，导致缺库问题反复出现。

### 诊断方法

进入容器后用 ldd 一次性找出所有缺失库，避免逐个排查：

```bash
docker exec -it <容器ID> bash
ldd /opt/libreoffice26.2/program/soffice.bin | grep "not found"
```

### 解决方法

根治方案：将基础镜像从 python:3.13-slim 改为 python:3.13（完整版），并在 apt-get 中补全所有已知依赖：

```docker
FROM python:3.13

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    fonts-noto-cjk \
    fonts-dejavu-core \
    fonts-liberation \
    fontconfig \
    libssl3 \
    libxinerama1 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libxrandr2 \
    libxext6 \
    libx11-6 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxcb1 \
    libdbus-1-3 \
    libcups2 \
    libglib2.0-0 \
    libfreetype6 \
    libfontconfig1 \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libnspr4 \
    libnss3 \
    libxslt1.1 \
    libxml2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
```

> slim 镜像虽然更小，但对于 LibreOffice 这类重依赖的应用不适合，用完整镜像多约 100MB 但可以一次到位。

---

## 额外：profile_url 格式错误导致 bootstrap.ini 报损坏

### 现象

手动能打开 LibreOffice，但命令行调用时报：

```plain text
配置文件 [C:\Program Files\LibreOffice\program\bootstrap.ini] 已经损坏。
```

### 原因

代码中构造 LibreOffice 临时 profile 的 URI 格式错误：

```python
# 错误：双斜杠 + Windows 反斜杠
profile_url = f'file://{profile_dir}'
# 结果：file://C:\Users\...\Temp\lo_profile_xxxx
```

LibreOffice 要求 URI 格式为三斜杠 + 正斜杠：

```plain text
file:///C:/Users/.../Temp/lo_profile_xxxx
```

格式错误导致 LibreOffice 忽略临时 profile，回退到默认安装目录下的 profile，而该 profile 已损坏。

### 解决方法

```python
# 正确：三斜杠 + 正斜杠
profile_url = 'file:///' + profile_dir.replace('\\', '/')
```

---

## 经验总结

