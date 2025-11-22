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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662Y6N7LO%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCepkNLwQ99%2BcmnrBJGQndnPFTyycx6H1Sypj6Jwl5LCAIhANiuY2pAk2JHchOmoCo2RIr0VHimtxA5U9MOnLVV7y6bKv8DCBwQABoMNjM3NDIzMTgzODA1Igyy2NTPZQDXgpPNnagq3AOCPfLWl%2FausPUVlE9kp4Fkz3vJl4R%2BZ09D%2B0Y8Mext9ubG017EE3F1tcmSs9EmOpgEQ%2BWGWiDiGUzKVvysRbjyIHZOH9G044xqMp2t4Oe0r2xn0jUAcL9gL91n5AI7FqqfHEh0WspUimwBoXAJM%2FSm%2F2ArKjRLuPtmCa%2BP4qPKLGhP%2Bn9NVRmotGz6B1ZNhjohhw9B2m4rVHAgwjdTNbytFjojQgCy8RnP%2BtOgV4Hedar4FyWyoUyyt07VY3%2BDmTOgib4vn7g2GGQBZsICvJ9LgJr7fJjTU9UwSbhK5j%2FB9z29cCOemkPUcEmonXPoaUTbjHqnxudQ8mfWe4Cn0IFy4zYKfcsYmXIcQriOFkjYEZzaYfUHV8bRGQ3qU2ZVV5GfL1tS95%2Ficy9b4fu9mEpsE9guetvyfej5XJEBzY1k80g27WQ3oyLO3CTPoQZy2PbZeBUOHp48QoRLaE119U3QMiqw6unco4%2Bt2EewjF4GiWYGGvtW%2BQ3HKLkKLywhvYAu0%2Bs%2Bhef7LiG2pqQWXQANV4tzKx%2FzyfI%2Bw5kPBCgM59Nfccmegt1dxUVI4c1zxigeN06ta%2Fmpf4yOB7B4%2FaiEPrbZQh%2FHZV%2BnguTjTYE%2FJLQpN4m4am6FCRoQYzDovoTJBjqkAZtKixtrEHXhH1O4GKzji0vaOsIYOqD6bFMROr9t1mBGwn3yS10orR%2ByyAPYBlnxNtT1PexIbVd4ZhRm4kSWCEuoZnBrvHhLHK0bhP7FnrKe1H3ShSz0V23MCwK%2BxSTYVsH%2Bnuk7JKvnmvnl%2FJslSC2h0OmXDjPdnWnyInpAMhpQigsZmolr9S9yy7HO6y%2FGkni80Um9n64TBw%2FfJTx9k1xCoqPA&X-Amz-Signature=e955907ce66cec324ffa9b8d5d0ce83d83346c0d2d426ea4a758fa46d46fd0c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662Y6N7LO%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCepkNLwQ99%2BcmnrBJGQndnPFTyycx6H1Sypj6Jwl5LCAIhANiuY2pAk2JHchOmoCo2RIr0VHimtxA5U9MOnLVV7y6bKv8DCBwQABoMNjM3NDIzMTgzODA1Igyy2NTPZQDXgpPNnagq3AOCPfLWl%2FausPUVlE9kp4Fkz3vJl4R%2BZ09D%2B0Y8Mext9ubG017EE3F1tcmSs9EmOpgEQ%2BWGWiDiGUzKVvysRbjyIHZOH9G044xqMp2t4Oe0r2xn0jUAcL9gL91n5AI7FqqfHEh0WspUimwBoXAJM%2FSm%2F2ArKjRLuPtmCa%2BP4qPKLGhP%2Bn9NVRmotGz6B1ZNhjohhw9B2m4rVHAgwjdTNbytFjojQgCy8RnP%2BtOgV4Hedar4FyWyoUyyt07VY3%2BDmTOgib4vn7g2GGQBZsICvJ9LgJr7fJjTU9UwSbhK5j%2FB9z29cCOemkPUcEmonXPoaUTbjHqnxudQ8mfWe4Cn0IFy4zYKfcsYmXIcQriOFkjYEZzaYfUHV8bRGQ3qU2ZVV5GfL1tS95%2Ficy9b4fu9mEpsE9guetvyfej5XJEBzY1k80g27WQ3oyLO3CTPoQZy2PbZeBUOHp48QoRLaE119U3QMiqw6unco4%2Bt2EewjF4GiWYGGvtW%2BQ3HKLkKLywhvYAu0%2Bs%2Bhef7LiG2pqQWXQANV4tzKx%2FzyfI%2Bw5kPBCgM59Nfccmegt1dxUVI4c1zxigeN06ta%2Fmpf4yOB7B4%2FaiEPrbZQh%2FHZV%2BnguTjTYE%2FJLQpN4m4am6FCRoQYzDovoTJBjqkAZtKixtrEHXhH1O4GKzji0vaOsIYOqD6bFMROr9t1mBGwn3yS10orR%2ByyAPYBlnxNtT1PexIbVd4ZhRm4kSWCEuoZnBrvHhLHK0bhP7FnrKe1H3ShSz0V23MCwK%2BxSTYVsH%2Bnuk7JKvnmvnl%2FJslSC2h0OmXDjPdnWnyInpAMhpQigsZmolr9S9yy7HO6y%2FGkni80Um9n64TBw%2FfJTx9k1xCoqPA&X-Amz-Signature=494c14c8a8ff29e3986f4274c9fc7bd6ce7779fdb7277e6f547480384a950a22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









