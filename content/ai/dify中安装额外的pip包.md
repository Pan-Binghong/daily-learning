---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPP4QUIX%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDSWVDleAPxmFllfBZKi6RvwPz7F1Pukg5nRYY7%2B4kFIwIgDNPJeNWaLAvWFYBT%2BxiZHLEmZgEJQ1H9PKcUA3zScsUq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDI5Bz3v86vfjroKsfircA3INqCunVdnbe9kDoeUAVYX1V0EqgC04IONbbL0JOlMoXFhXV9SLvrHOXqcvhdQu5FMWohkpkiEkURcLpC6B3zw5c7BmEDugzny0dEFBR8c1V0gLHSnkdl5vfLb2%2BSy1fA1%2FMhviTKZi3DLrDlWp23WHsLZMLz6w9Nz4uUYlZ0y%2FtX9caJNLm3kYcP9Zvii3lryojit0HC99DSlDa2jrlLP1IzxLcas0vdTzhmphedUxqB2H%2FgiIdIEGstHw%2F206Lv0mDJzPz0JHSSl%2FUqOS1PYW%2B6wmWmiHpOd4eFhcspqLQAnvW0gUjcep3znNUg1Me3zUmaBCy7EvpJXHYUrOJbigEWAHa8rIEBcB5teDJFvoE85Pso9RheBLmlZ%2FRhIxjZ2Eq%2BueY19nIBLG8Qty5jUpFc2SkNyXQtU4a8sDxFR1xWLl8BQ4x%2BQyTFJ%2BAAeE%2Fl9E%2BKcrCaBdktbfWE%2FaxhdRH7z%2FnowlaM40FVlH1anHmemN1dczi3enKYqc3%2F5SmjRuuqrUTzGYKCy6iMqGuLothjQvu0NruxGhWZT0V964HtY3p8ytsisjqRLUNpnlU1mmjEZ99w92bkD3uAyr4ALwWoVnTkQpGwqLtfr0jDrmfQCW5OaVcTxHir%2FOMNHoiswGOqUBSCPlQH2pYX7m7sF0kmrnSWjkakMNp3UjoR1OTk0HM0OSxxTjtmZrnzYGJQ4nWEVsOc4nSjCqxYGr2w4DiMyqUV1EWDejUzPm8K5I4w2AvRSKlsiVcsvOksa%2FCqsbz2iY4ljZJoGg623jUnLEFnkSzfj3mF8y%2BbD75pMby3%2BphSouXDAUdelByc0pPDhY2WPtOTBJlGecSZ92YmdsbkywUVWB%2BLl9&X-Amz-Signature=2e42cc1c7bd224296185c1aaaa970a7f357ae45d4305907d999a648304aabe89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

