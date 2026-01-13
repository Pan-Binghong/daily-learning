---
title: 基于Nvidia驱动日志(Events.log)统计网络震荡次数
date: '2024-11-18T08:08:00.000Z'
lastmod: '2024-11-20T03:24:00.000Z'
draft: false
tags:
- Python
categories:
- 后端
---

> 💡 刚来这边公司，第一个任务让统计LinkDown，手动统计太呆了。索性自己写了一个工具出来。统计 Link Down 的次数，并显示服务名称和计算机名称。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4a1dfbc0-1f3e-46b0-94b1-512eb1ec7156/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662TFQDQQ%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCiiby5ewCAk0Ziah4kBW%2FkQ0kCJLO6lSio8rtU%2BuPCvQIhAILoMAUuFbC6sk5zZSrJ6SBNap3yYlKQGcGirLuQT7hwKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxlMDGdeP7YD4LOPz0q3AM68p12VAuRivgS%2FiU29HX051HjWrZ4fOh%2FsgKrq38pEtBIZLOmMM7jp4BfGIw5fINIW8buuUzs2d2XJjZPzAsekVIZwH7r%2BKTImSaEvYcsbABrw7hXximkWqoS1GjLRjDMhMT879Pz4WOIjXqi3FdL2Jd%2BE0b8aTmE25adoj%2FaebSHm2g8UheYIhD%2BLaNOpHzZIgF%2FVQiMLFHUmUUw%2BIzXIiY%2FCWOd8f80Vo01KMpve4rubI%2BTq4IS0sMXN6t%2F8jwrVUopWzbOwJ4LR0pKHFsgrtD49ZfjTSbeIk%2BFhD107k5cGr1qUXE3vGuu9tZTohOfnj26i8lk4Sx0In5Wd495CooivtgYasD1G1xbJr%2BUu5pQKg4QlPCSRplHXH0vf1cza7sG1wcP9jgLX8FVsdv%2FgOZKVAJVvCwP8YCHnMI7fiDaLZkm%2F9AVmnguJbdVlYWH5YLDm5B8Z6wWDE8fRDVg1dOmie1lNfPpZhvtk%2BS618xYOXoCI27NVCjlDXOciSSRedPY0CtCGYi%2F%2Bv4VhInXv8sjc%2FR1F1gvpnAJ4L04UWFrADTBk%2BdFjKzv1aSCXWPaCB60buI4F4apuAoUeYgGhrVxg%2FJCEgtNrpu9sac9dEBh5RBudmlD7DyDLDDq5pbLBjqkAZebirGxjRkq3vu%2BNA79PcogFgQpFQKgelu3MfCnIw0p349ABHPWHaa5gmC0t66IkMSLZUtpofeE3CNtxeYCEoK32B%2B%2BHSvebQ7CFDkfZg%2FnZNQJ%2BoN4orccsEaufTpFSyvMpoXYWcbUnbEoqeofQpX8Xa4fpf0tjebSXPDZBr97h7hHJbsYkWTBEZqBCo6WRpFC%2FvIFza3EKua%2FuTLWisFUnZKP&X-Amz-Signature=d1453c497f9ca2707831b3bd9b3a3261f6be54636202184084df06383f802879&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Souce Code

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   count_dict-v3.py
@Time    :   2024/05/13 09:19:02
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   统计Link Down的次数，并显示服务名称和计算机名称
'''

import pandas as pd
import json
import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def load_csv_and_process():
    file_path = filedialog.askopenfilename(filetypes=[('CSV文件', '*.csv')])

    if file_path:
        df = pd.read_csv(file_path)
        df_warning = df[(df['Severity'] == 'Warning') & (df['Event Name'] == 'Link is Down')]
        pattern1 = re.compile(r'Source\s+([a-fA-F0-9]+)')
        mac_list = []
        for source in df_warning['Source']:
            match1 = pattern1.search(source)
            if match1:
                mac_list.append(match1.group(1))
        time0 = df_warning['Date/Time'].iloc[-1]
        time1 = df_warning['Date/Time'].iloc[0]
        df_result = find_service_names_and_counts(mac_list, mac_dict, time_list=[time0, time1])
        df_result_computer = find_computer_names_and_counts(df_warning['Description'], time_list=[time0, time1])

        # 清除之前的表格内容（如果有的话）
        for widget in frame.winfo_children():
            widget.destroy()

        notebook = ttk.Notebook(frame)
        notebook.pack(fill='both', expand=True)

        # 第一页：服务名称统计
        service_frame = ttk.Frame(notebook)
        notebook.add(service_frame, text='Service Name')
        show_dataframe_in_gui(df_result, service_frame)

        # 第二页：计算机名称统计
        computer_frame = ttk.Frame(notebook)
        notebook.add(computer_frame, text='Computer Name')
        show_dataframe_in_gui(df_result_computer, computer_frame)

def find_computer_names_and_counts(descriptions, time_list):  
    start_time, end_time = time_list  
    # 创建一个字典来记录每个计算机名称的linkdown次数  
    computer_counts = {}  
    sum_counts = 0  
    pattern2 = re.compile(r'\(Computer:([^)]+)\)')  

    for desc in descriptions:  
        match2 = pattern2.search(desc)  
        if match2:  
            computer_name = match2.group(1)  
            computer_counts[computer_name] = computer_counts.get(computer_name, 0) + 1  
            sum_counts += 1  

    # 创建不包含时间信息的DataFrame  
    df_result_computer = pd.DataFrame.from_dict(computer_counts, orient='index', columns=['Count of Link is Down']).reset_index()  
    df_result_computer.columns = ['Computer Name', 'Count of Link is Down']  

    # 创建一个新行来保存时间信息  
    time_info_row = pd.Series(['Start Time: ' + start_time, 'End Time: ' + end_time], index=['Computer Name', 'Count of Link is Down'])  
    time_info_df = pd.DataFrame([time_info_row])  # 将Series转换为DataFrame  

    # 将时间信息DataFrame放在原始DataFrame的开始位置  
    df_result_computer = pd.concat([time_info_df, df_result_computer]).reset_index(drop=True)  

    # 在DataFrame的末尾添加一行总次数  
    total_row = pd.DataFrame({'Computer Name': ['Total'], 'Count of Link is Down': [sum_counts]}, index=[len(df_result_computer)])  
    df_result_computer = pd.concat([df_result_computer.iloc[:-1], total_row]).reset_index(drop=True)  

    return df_result_computer 

def find_service_names_and_counts(mac_list, mac_dict, time_list):  
    # 假设time_list有两个元素: [开始时间, 结束时间]  
    start_time, end_time = time_list  

    # 创建一个字典来记录每个服务名称的linkdown次数  
    service_counts = {}  
    sum_counts = 0  
    # 遍历mac_list中的每个MAC地址  
    for mac in mac_list:  
        # 查找MAC地址在哪个服务名称的列表中  
        for service_name, macs in mac_dict.items():  
            if mac in macs:  
                # 如果找到，增加该服务名称的计数  
                service_counts[service_name] = service_counts.get(service_name, 0) + 1  
                sum_counts += 1  
                break  # 跳出内部循环，因为每个MAC地址只应对应一个服务名称  

    # 创建DataFrame  
    df_result = pd.DataFrame.from_dict(service_counts, orient='index', columns=['Count of Link is Down']).reset_index()  
    df_result.columns = ['Service Name', 'Count of Link is Down']  

    time_info_row = pd.Series(['Start Time: ' + start_time, 'End Time: ' + end_time], index=['Service Name', 'Count of Link is Down'])  
    time_info_df = pd.DataFrame([time_info_row])  # 将Series转换为DataFrame  

    # 将时间信息DataFrame放在原始DataFrame的开始位置  
    df_result = pd.concat([time_info_df, df_result]).reset_index(drop=True) 

    # 在DataFrame的末尾添加一行总次数  
    total_row = pd.DataFrame({'Service Name': ['Total'], 'Count of Link is Down': [sum_counts]}, index=[len(df_result)-1])  
    df_result = pd.concat([df_result.iloc[:-1], total_row]).reset_index(drop=True)  # 重置索引，不包括最后一行（因为我们将在其后添加总次数）  

    return df_result   

def show_dataframe_in_gui(df, frame_widget):  
    # 清除之前的表格内容（如果有的话）  
    for widget in frame_widget.winfo_children():  
        widget.destroy()  

    # 注意这里：将df.columns转换为列表  
    column_names = list(df.columns)  

    # 创建一个Treeview组件来显示数据  
    tree = ttk.Treeview(frame_widget, columns=column_names, show='headings')  

    # 设置列标题  
    for col in column_names:  
        tree.heading(col, text=col)  

    # 插入数据到Treeview  
    for index, row in df.iterrows():  
        tree.insert('', 'end', values=row.tolist())  

    # 将Treeview添加到frame中（如果它之前没有被添加到frame中，这一步是必要的）  
    tree.pack(fill='both', expand=True)

def main():
    root = tk.Tk()
    root.geometry('400x500')
    root.title('Link Down Count')

    # 创建一个Frame来放置Treeview  
    global frame
    frame = tk.Frame(root)  
    frame.pack(fill='both', expand=True) 

    load_button = tk.Button(root, text='选择CSV文件', command=load_csv_and_process)
    load_button.pack()
        with open('mac_dict.json', 'r') as f:
            global mac_dict
            mac_dict = json.load(f)

        root.mainloop()

if __name__ == '__main__':
    main()

```

---

### 打包EXE

```python
pyinstaller --onefile --icon=./icon/dog.ico --noconsole cld.py
```

---

### 前置文件

```json
/*  提前准备 json 文件，格式为: */
 {
    "H800-1": [
        "a088cxxx",
        "a088cxxx",
        "a088cxxx",
        "a088cxxx"
    ],
    "H800-2": [
        "a088cxxx",
        "a088cxxx",
        "a088cxxx",
        "a088cxxx"
    ],
}

```

> 键为机器的名称

---

### 本工具下载地址

https://sharrr.com/s#daf91fe3-7832-4eca-8e82-7d2c4fede1f7/ojLQ34JnluGXvyDoq5cqvA%3D%3D/18uNVBJpd6IrmHTg9WXTHLlGF9hbB2iCiMwTBmoHX_I





