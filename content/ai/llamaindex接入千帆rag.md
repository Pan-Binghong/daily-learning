---
title: LlamaIndex接入千帆RAG
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- RAG
categories:
- AI
---

记录从使用Llama-index框架, 基于在线文心千帆大模型ERNIE-4.0, 构建实现本地知识检索.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7OQH3F%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2NChsMLWCW%2BzrBZxg34bol3%2FIW0fwNqJw23Gy56QI%2BAiEAohcDzeOtSHMRTbGlB%2BDdODdih6z%2FsWWXFoFgwz61rEQq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDCCdPL15XwE%2BSbS31ircA0%2F58EQruY0dlA61R344xtT0E0%2BKIrmSYXcScMGlq00LsmXoX8fgC%2BndTEiJ84W%2Fbo0W4RyONKAWHcTYCz%2FTG8i6%2FvjgCbiHA9NHmox%2Fkb6y7EVx8CuhLg07C5gGjE1pRES2X0SjmMVMjL1uOokKD%2Bu483OzDOG5ST2Hr3duJgaSmpi7GipHZ2oSRITeXlJz77cFq7hk1%2Fsi6jctrGhX4KNquFlnEM7320FKUTAYM55wweN%2BeIrBVBn2IMEsfr7Z10epoVHKgwaD5gn1D5arCkt9%2B%2F2%2BpJBPrRiV7ap%2BuzeokOlUYdvC%2FqVmT6Pd57jYNtAVGgg07HAf4sf5luaY7qiCfyjiBWQR%2BFfhmTnIocYujFvAbCIvrx3FLfR6xNfnxBMzT84%2B4t3TBp70PqWkuMTNSBxx1ARG90Sb8222kHMbE6e7xjtbfVT2l07FmgjrSOXRtspecy9zWq%2F%2BOyCuNF4sNjONrDSK%2BO8C%2BTHfhyHOx94xZjQPSBe90nvXTZP0CDDODiUb%2BRQk7kdyl3SqOgxSnAmLfTGiSM2dkZac61VY5D%2BIS%2F%2FCicL8USF8GMFjv7eKhd9XTL9zeL3tnfyBl8mDjcyZKa98sYNHBWv8w9IgHREGjmEgs2i7er35ML%2BW5csGOqUBKB%2B1KAadNQzA8qPV0HiQh2IYT0jBTmLlgEJAy628EwJf5YIsvV93rqcV%2F0qn76%2FagrMJTO0AfKZ9%2FXWlq99W5xf9iop1mbpWYGnBE6MEkSGFyoWlIB1MTieO8K%2F4jTrVgCyN9ruhmXXatJy0UXnMoMxljTppkVvZOwiQwjjyPbCGjMAfwgolGsQXDkZsBHB9X%2FqDMVsVhMFP3RjA5GT%2BZmX8SCRY&X-Amz-Signature=cf52cad3ca38ffa8443183db6f498a0d37fcd5ca23b27281b142bb20f5a8d127&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7OQH3F%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2NChsMLWCW%2BzrBZxg34bol3%2FIW0fwNqJw23Gy56QI%2BAiEAohcDzeOtSHMRTbGlB%2BDdODdih6z%2FsWWXFoFgwz61rEQq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDCCdPL15XwE%2BSbS31ircA0%2F58EQruY0dlA61R344xtT0E0%2BKIrmSYXcScMGlq00LsmXoX8fgC%2BndTEiJ84W%2Fbo0W4RyONKAWHcTYCz%2FTG8i6%2FvjgCbiHA9NHmox%2Fkb6y7EVx8CuhLg07C5gGjE1pRES2X0SjmMVMjL1uOokKD%2Bu483OzDOG5ST2Hr3duJgaSmpi7GipHZ2oSRITeXlJz77cFq7hk1%2Fsi6jctrGhX4KNquFlnEM7320FKUTAYM55wweN%2BeIrBVBn2IMEsfr7Z10epoVHKgwaD5gn1D5arCkt9%2B%2F2%2BpJBPrRiV7ap%2BuzeokOlUYdvC%2FqVmT6Pd57jYNtAVGgg07HAf4sf5luaY7qiCfyjiBWQR%2BFfhmTnIocYujFvAbCIvrx3FLfR6xNfnxBMzT84%2B4t3TBp70PqWkuMTNSBxx1ARG90Sb8222kHMbE6e7xjtbfVT2l07FmgjrSOXRtspecy9zWq%2F%2BOyCuNF4sNjONrDSK%2BO8C%2BTHfhyHOx94xZjQPSBe90nvXTZP0CDDODiUb%2BRQk7kdyl3SqOgxSnAmLfTGiSM2dkZac61VY5D%2BIS%2F%2FCicL8USF8GMFjv7eKhd9XTL9zeL3tnfyBl8mDjcyZKa98sYNHBWv8w9IgHREGjmEgs2i7er35ML%2BW5csGOqUBKB%2B1KAadNQzA8qPV0HiQh2IYT0jBTmLlgEJAy628EwJf5YIsvV93rqcV%2F0qn76%2FagrMJTO0AfKZ9%2FXWlq99W5xf9iop1mbpWYGnBE6MEkSGFyoWlIB1MTieO8K%2F4jTrVgCyN9ruhmXXatJy0UXnMoMxljTppkVvZOwiQwjjyPbCGjMAfwgolGsQXDkZsBHB9X%2FqDMVsVhMFP3RjA5GT%2BZmX8SCRY&X-Amz-Signature=d48a91ace0e9fe087199e8b22ef2203834130c96b841348807b607fafaee9b82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 导入本地Embedding

- 下载Embedding模型
```python
from modelscope import snapshot_download
model_dir = snapshot_download('Xorbits/bge-m3', cache_dir='/data/LLMs')
```

- 加载本地Embedding模型
```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
cache_folder = r"embed_model/m3e-large"embed_model = HuggingFaceEmbedding(cache_folder=cache_folder)
```

---

### 构建本地知识库

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
directory = "/data/documents" #文档路径vector_index = VectorStoreIndex.from_documents(documents)
```

---

### 构建查询引擎

```python
query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
```

> similarity_top_k可根据经验自行调整, 推荐设置3, 5.

---

### 构建RAG Agent

- 构建工具
```python
import os
def get_tool(name, full_name, documents=None):
    if not os.path.exists(f"./data/{name}"):
        # build vector index        vector_index = VectorStoreIndex.from_documents(documents)
        vector_index.storage_context.persist(persist_dir=f"./data/{name}")
    else:
        vector_index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=f"./data/{name}"),
        )
    query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
    query_engine_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name=name,
            description=(
                "Provides information about Uber quarterly financials ending"                f" {full_name}"            ),
        ),
    )
    return query_engine_tool
```

- 设置Agent
```python
from llama_index.core.agent import AgentRunner, ReActAgent
agent = ReActAgent.from_tools(
    query_engine_tools, llm=agent_llm, verbose=True, max_iterations=20)
```

- 运行
```python
response = agent.chat("您的问题")
```

### 整体代码

```python
from llama_index.core import Settings
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.qianfan import Qianfan
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# 初始化Qianfan模型class Rag:
    def __init__(self):
        self.access_key = ""        self.secret_key = ""        self.model_name = "ERNIE-4.0-8K-Latest"        self.url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"        self.llm = Qianfan(self.access_key, self.secret_key, self.model_name, self.url, context_window=8192)
        self.cache_folder = r"embed_model/m3e-large"        self.directory = r"/data/documents"  # 数据目录路径    def get_tool(self, name, full_name, documents=None):
        embed_model = HuggingFaceEmbedding(cache_folder=self.cache_folder)
        Settings.embed_model = embed_model
        vector_index = VectorStoreIndex.from_documents(documents)
        persist_path = f"{self.directory}/{name}"        if not os.path.exists(persist_path):
            vector_index.storage_context.persist(persist_dir=persist_path)
        query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=self.llm)
        query_engine_tool = QueryEngineTool(query_engine=query_engine, metadata=ToolMetadata(name=name, description=f"Provides information from document {full_name}"))
        return query_engine_tool
    def parse_args(self):
        query_engine_tools = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.directory, filename)
                documents = SimpleDirectoryReader(input_files=[filepath]).load_data()
                tool_name = filename[:-4]  # 去除'.txt'得到工具名称                tool = self.get_tool(tool_name, tool_name, documents=documents)
                query_engine_tools.append(tool)
        return query_engine_tools
    def query_engine(self, query):
        from llama_index.core.agent import ReActAgent
        tools = self.parse_args()
        agent = ReActAgent.from_tools(tools, llm=self.llm, verbose=True, max_iterations=20)
        response = agent.chat(query)
        return response
# 创建 Rag 实例并执行查询if __name__ == "__main__":
    rag = Rag()
    print(rag.query_engine(query="问题"))
```

> 参考链接

