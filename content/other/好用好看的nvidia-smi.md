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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDXLQXWG%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQCgD67FZT6U2ZRhGCjHaZx0DCG6y4V89ib6xEdCYxZzGAIhAKopRHzuo0SUQl1Zxsx%2FhW%2BRFvFlL0h5LlvUwinW3f4oKv8DCBEQABoMNjM3NDIzMTgzODA1IgywA1MHTQ9ywEArctcq3AMcGvo2n589xFvQpLdz5LEhRKt8K20Sad2J5Y%2FT%2F4qPhZWuB3x6cEEOFuA%2Fv0VGgQInAOhaYkjIEmIFqnOuy2BsYt3Eo8MEUIcrxaluOXn95v%2BLVstMSaRrG60JEAr0ETprC4WlKb9WqUeCz00nzJ4aIRytqnQ5zn%2B7cpErhR%2FNVxT%2FYpaam6IaeMjwZod5hySvmo1E1mmVG4%2BlFHYbFqqiMsDEq35xjlZGOmnMscvpDYEHhxvvuEI5NfQvnswVfKjECFF%2FgnEYXEU%2FrBHjfNu2yawz7dg%2BQ86wzfqPqdipJJpCEGPAsPgAJmipxDFYusdmFTQs%2FMiIDMMKAJySxedET%2FGJB2qTt3Q6DB9IZ4kyBz5MwnEthBpbqxJlEUo2%2FSR6Dbi%2FKo4FHU6875pMZs%2B6sp27xKZewAoRNOV1iHHqRr%2Bu%2FjuJ8EuWB9q2RkKJnEg2unBY0q1OQcWsdJY2y8vcAsxDg28Plk1J3z3GFEBb%2F%2BaMg%2BCSzrrjZUA%2F5Hqt73T34Zm%2BKNGZVxe9ryB2GzlhsoqC%2FY%2BXSkYGOO%2Bz8qdrBes2tGFPABTCo3M53hBxGqH9%2FSofv3CxI0SDfofyizI6BAgQUYkXQRD08S7Y24PcAlkDszl2wCAkWaE88DCYnsTMBjqkASL9uL%2Foy8PPPp2m1gGnBSEqZYZzW5vnJF5A1ubnaqvLCmJ6JYRP4gw8%2FRQPfybg2NQqDDoC7wqI10Jo68bfgTm9MIcUxRbm3e8U5cvn3TvP53M3oB3j5NE1OHGZITksxx6ahFUeq4euzluBkbr4%2FwgT%2BGAVOuimeRuPd4Ec0F%2FIJ%2BRYATxTCmR8av%2FUn%2BCaBVnGyh0WCPY49dwWUCsUBuH5Lfpe&X-Amz-Signature=ea91f968e54462897497e27bd4264350166d30c94544f0a8c45407c8eb968e51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDXLQXWG%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQCgD67FZT6U2ZRhGCjHaZx0DCG6y4V89ib6xEdCYxZzGAIhAKopRHzuo0SUQl1Zxsx%2FhW%2BRFvFlL0h5LlvUwinW3f4oKv8DCBEQABoMNjM3NDIzMTgzODA1IgywA1MHTQ9ywEArctcq3AMcGvo2n589xFvQpLdz5LEhRKt8K20Sad2J5Y%2FT%2F4qPhZWuB3x6cEEOFuA%2Fv0VGgQInAOhaYkjIEmIFqnOuy2BsYt3Eo8MEUIcrxaluOXn95v%2BLVstMSaRrG60JEAr0ETprC4WlKb9WqUeCz00nzJ4aIRytqnQ5zn%2B7cpErhR%2FNVxT%2FYpaam6IaeMjwZod5hySvmo1E1mmVG4%2BlFHYbFqqiMsDEq35xjlZGOmnMscvpDYEHhxvvuEI5NfQvnswVfKjECFF%2FgnEYXEU%2FrBHjfNu2yawz7dg%2BQ86wzfqPqdipJJpCEGPAsPgAJmipxDFYusdmFTQs%2FMiIDMMKAJySxedET%2FGJB2qTt3Q6DB9IZ4kyBz5MwnEthBpbqxJlEUo2%2FSR6Dbi%2FKo4FHU6875pMZs%2B6sp27xKZewAoRNOV1iHHqRr%2Bu%2FjuJ8EuWB9q2RkKJnEg2unBY0q1OQcWsdJY2y8vcAsxDg28Plk1J3z3GFEBb%2F%2BaMg%2BCSzrrjZUA%2F5Hqt73T34Zm%2BKNGZVxe9ryB2GzlhsoqC%2FY%2BXSkYGOO%2Bz8qdrBes2tGFPABTCo3M53hBxGqH9%2FSofv3CxI0SDfofyizI6BAgQUYkXQRD08S7Y24PcAlkDszl2wCAkWaE88DCYnsTMBjqkASL9uL%2Foy8PPPp2m1gGnBSEqZYZzW5vnJF5A1ubnaqvLCmJ6JYRP4gw8%2FRQPfybg2NQqDDoC7wqI10Jo68bfgTm9MIcUxRbm3e8U5cvn3TvP53M3oB3j5NE1OHGZITksxx6ahFUeq4euzluBkbr4%2FwgT%2BGAVOuimeRuPd4Ec0F%2FIJ%2BRYATxTCmR8av%2FUn%2BCaBVnGyh0WCPY49dwWUCsUBuH5Lfpe&X-Amz-Signature=37ba7cc108ab66cc79dc64610afd7bab863c4ba064e82ede90b81f272aa1d4e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









