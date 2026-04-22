---
title: Excel VBA 专业水印系统完整解析
date: '2026-04-21T05:04:00.000Z'
lastmod: '2026-04-21T05:08:00.000Z'
draft: false
tags:
- VBA
- Excel
- 办公自动化
categories:
- 知识
---

# 一、概述

本模块实现了一套完整的 Excel 工作表水印系统，支持：

- 密码保护的水印添加与移除
- 将多行斜体文字渲染为 PNG 图片作为背景水印
- 同时设置打印页眉水印（PageSetup）
- 通过 ChartObject 导出矢量排版为位图
> 💡 水印文字均已脱敏，原始内容以「机密」代替。

---

# 二、模块结构

整个系统由 3 个过程 + 1 组配置常量构成：

![](https://images.pexels.com/photos/20062955/pexels-photo-20062955.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200)

---

# 三、配置常量

```basic
Option Explicit

' ============================================================
'  水印配置常量
' ============================================================
Public Const WM_TEXT_L1   As String  = "机密"       ' 第一行（已脱敏）
Public Const WM_TEXT_L2   As String  = "机密"       ' 第二行（已脱敏）
Public Const WM_COLOR     As Long    = 13816530     ' 浅灰紫（BGR: D2/CF/52）
Public Const WM_FONT_SIZE As Integer = 28
Public g_WM_Password      As String
```

> 💡 颜色说明：13816530（十六进制 0xD2CF52），在 VBA 中颜色为 BGR 顺序，实际显示为低饱和度的金黄偏灰色调，视觉上与白色背景形成柔和对比，不喧宾夺主。

---

# 四、AddProfessionalWatermark() — 主入口

```basic
Sub AddProfessionalWatermark()
    Dim ws      As Worksheet
    Dim pwd     As String
    Dim imgPath As String

    Set ws = ActiveSheet

    ' 1. 弹窗要求用户设置密码
    pwd = InputBox("请设置水印保护密码：", "专业水印系统", "")
    If pwd = "" Then
        MsgBox "已取消操作。", vbInformation
        Exit Sub
    End If
    g_WM_Password = pwd

    ' 2. 如果工作表已受保护，先解除
    If ws.ProtectContents Or ws.ProtectDrawingObjects Then
        On Error Resume Next
        ws.Unprotect Password:=pwd
        If Err.Number <> 0 Then
            MsgBox "密码错误，无法解除保护！", vbCritical
            Exit Sub
        End If
        On Error GoTo 0
    End If

    Application.ScreenUpdating = False
    Application.DisplayAlerts = False

    ' 3. 生成水印图片
    imgPath = BuildWatermarkImage()
    If imgPath = "" Then
        Application.ScreenUpdating = True
        Application.DisplayAlerts = True
        MsgBox "水印图片生成失败！", vbCritical
        Exit Sub
    End If

    ' 4. 设置工作表背景（显示用）
    ws.SetBackgroundPicture imgPath

    ' 5. 设置打印页眉（打印/导出 PDF 用）
    On Error Resume Next
    With ws.PageSetup
        .CenterHeader = "&G"
        .CenterHeaderPicture.Filename = imgPath
        .CenterHeaderPicture.Width    = 500
        .CenterHeaderPicture.Height   = 350
    End With
    On Error GoTo 0

    ' 6. 重新保护工作表
    ws.Protect Password:=pwd, _
              DrawingObjects:=True, _
              Contents:=False, _         ' 不保护单元格内容，允许编辑
              UserInterfaceOnly:=True    ' 宏可以绕过保护

    Application.ScreenUpdating = True
    Application.DisplayAlerts = True

    MsgBox "水印添加成功！", vbInformation
End Sub
```

## 关键设计点

- Contents:=False + UserInterfaceOnly:=True：允许用户正常编辑单元格，但禁止通过界面拖动/删除图形对象，同时 VBA 代码本身不受保护限制。
- 双重水印策略：.SetBackgroundPicture 用于屏幕显示，PageSetup.CenterHeaderPicture 用于打印输出，两者共用同一张 PNG。
---

# 五、BuildWatermarkImage() — 核心图片生成

这是整个系统最复杂的函数，使用了一个巧妙的「借道 Chart 导出 PNG」技巧。

```basic
Function BuildWatermarkImage() As String
    ...
    imgPath = Environ("TEMP") & "\ce_wm_" & Format(Now, "yyyymmddhhmmss") & ".png"
```

## 5.1 临时工作表

```basic
    Set tmpWs = ThisWorkbook.Worksheets.Add(...)
    tmpWs.Name = "TMP_WM_" & Format(Now, "hhmmss")
```

在当前工作簿末尾插入一个临时工作表，名称带时间戳避免冲突，函数结束时会自动删除。

## 5.2 3×3 网格文本框排列

```basic
    cols = 3 : rows_n = 3
    boxW = 320 : boxH = 200
    totalW = cols * boxW + boxW * 0.5
    totalH = rows_n * boxH
```

水印由 9 个文本框（3列×3行）组成，奇数行向右偏移半个盒子宽度（boxW * 0.5），形成砖墙式错排布局：

```plain text
[机密][机密][机密]
  [机密][机密][机密]
[机密][机密][机密]
```

## 5.3 文本框样式

```basic
    With shp
        .Name     = "CE_TmpWM_" & n
        .Rotation = 330             ' 逆时针 30°（= 顺时针 -30°）
        .Fill.Visible = msoFalse    ' 无填充
        .Line.Visible = msoFalse    ' 无边框
    End With

    With shp.TextFrame
        .Characters.Text = WM_TEXT_L1 & vbLf & WM_TEXT_L2

        ' 第一行：28pt Arial 粗体斜体
        With .Characters(1, Len(WM_TEXT_L1)).Font
            .Name = "Arial" : .Size = WM_FONT_SIZE
            .Bold = True : .Italic = True : .Color = WM_COLOR
        End With

        ' 第二行：22pt（28-6）Arial 粗体斜体
        With .Characters(startPos, Len(WM_TEXT_L2)).Font
            .Name = "Arial" : .Size = WM_FONT_SIZE - 6
            .Bold = True : .Italic = True : .Color = WM_COLOR
        End With
    End With
```

两行文字共用同一颜色，但第二行字号缩小 6pt（22pt），形成主副标题的层次感。

![](https://images.pexels.com/photos/6579275/pexels-photo-6579275.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200)

## 5.4 通过 ChartObject 导出 PNG

> 💡 Excel 没有直接将任意区域导出为 PNG 的 API，但 Chart 有 .Export 方法。这是 VBA 中将 Shape 渲染为图片文件的经典变通方案。

```basic
    ' 1. 全选所有文本框
    tmpWs.Shapes(tmpNames(1)).Select
    For k = 2 To n
        tmpWs.Shapes(tmpNames(k)).Select False  ' False = 追加选择
    Next k
    Selection.Copy

    ' 2. 创建空白图表并粘贴
    Set chtObj = tmpWs.ChartObjects.Add(0, 0, totalW, totalH)
    With chtObj.Chart
        .ChartArea.Format.Fill.ForeColor.RGB = RGB(255, 255, 255)  ' 白底
        .ChartArea.Border.LineStyle = xlNone
        .Paste           ' 将形状粘贴到图表区
        .Export imgPath, "PNG"
    End With
    chtObj.Delete
```

导出流程：

- 全选所有水印文本框 → 复制到剪贴板
- 创建一个与水印等大的 ChartObject，白色背景
- 将剪贴板内容粘贴进 Chart
- 调用 Chart.Export 导出为 PNG
- 删除临时图表
## 5.5 清理

```basic
Cleanup:
    On Error Resume Next
    Application.DisplayAlerts = False
    If Not tmpWs Is Nothing Then tmpWs.Delete
    Application.DisplayAlerts = True
    On Error GoTo 0
```

无论成功或失败（通过 ErrHandle 标签跳转），都会删除临时工作表，避免工作簿中残留垃圾 Sheet。

---

# 六、RemoveProfessionalWatermark() — 移除水印

```basic
Sub RemoveProfessionalWatermark()
    ' 1. 密码验证
    ' ...

    ' 2. 清除背景图片
    ws.SetBackgroundPicture ""

    ' 3. 清除页眉
    With ws.PageSetup
        .CenterHeader = ""
        .LeftHeader   = ""
        .RightHeader  = ""
    End With

    ' 4. 删除残留形状（名称前缀匹配）
    For s = ws.Shapes.Count To 1 Step -1
        Set shp = ws.Shapes(s)
        If Left(shp.Name, 5) = "CE_WM" Or _
           Left(shp.Name, 10) = "CE_TmpWM_" Then
            shp.Delete
        End If
    Next s
End Sub
```

> 💡 逆序遍历：For s = ws.Shapes.Count To 1 Step -1 是删除集合元素的标准写法，避免正序遍历时因索引偏移而跳过元素。

> 💡 命名约定：所有水印相关形状以 CE_WM 或 CE_TmpWM_ 开头，移除时按前缀批量识别。

---

# 七、整体流程图

```plain text
AddProfessionalWatermark()
  │
  ├─ InputBox 密码输入
  ├─ 解除工作表保护
  ├─► BuildWatermarkImage()
  │     ├─ 创建临时 Sheet
  │     ├─ 生成 9 个错排文本框
  │     ├─ 全选 → Copy
  │     ├─ ChartObject.Paste → Export PNG
  │     └─ 删除临时 Sheet
  │
  ├─ SetBackgroundPicture（显示）
  ├─ PageSetup.CenterHeaderPicture（打印）
  └─ 重新 Protect 工作表

RemoveProfessionalWatermark()
  ├─ 密码验证 → Unprotect
  ├─ SetBackgroundPicture ""
  ├─ 清空 PageSetup 页眉
  └─ 逆序删除 CE_WM* 形状
```

![](https://images.pexels.com/photos/28380284/pexels-photo-28380284.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200)

---

# 八、技术亮点总结

---

# 九、潜在改进方向

- 临时 PNG 清理：当前代码未删除生成在 %TEMP% 下的 PNG 文件，长期运行会堆积。可在 RemoveProfessionalWatermark 中加入清理逻辑。
- 密码安全性：g_WM_Password 以明文全局变量存储，进程内可被其他宏读取，可考虑散列存储或仅在需要时临时持有。
- 多 Sheet 支持：当前仅操作 ActiveSheet，可扩展为对所有 Sheet 批量添加水印。
- 水印透明度：VBA TextBox 不支持透明度，若需半透明效果，需改用 Format.Transparency 属性（仅图形填充支持）。
> 💡 本文所有水印文字内容已脱敏处理，原始业务标识已替换为「机密」。

---

# 参考文献

---

[https://learn.microsoft.com/zh-cn/office/vba/api/excel.worksheet.setbackgroundpicture](https://learn.microsoft.com/zh-cn/office/vba/api/excel.worksheet.setbackgroundpicture)

[https://learn.microsoft.com/zh-cn/office/vba/api/excel.worksheet.protect](https://learn.microsoft.com/zh-cn/office/vba/api/excel.worksheet.protect)

[https://learn.microsoft.com/zh-cn/office/vba/api/excel.chart.export](https://learn.microsoft.com/zh-cn/office/vba/api/excel.chart.export)

[https://learn.microsoft.com/zh-cn/office/vba/api/excel.pagesetup](https://learn.microsoft.com/zh-cn/office/vba/api/excel.pagesetup)

