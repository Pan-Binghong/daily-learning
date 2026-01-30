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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWMEPJ4W%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtE6TuX9Mjq7ujqy4bCh7wTJj%2BLClp4Ytfz1%2FvgoQKnQIgH4%2BhWmmSbBekiy8wRQ9cwH9wwkYdAh0lc97FE%2FybP4QqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCL89yt6PcIftaB78SrcA5W7ifqdgx15AbHDZj3wP0v6nq5cdsA0e6RQn%2FKma70Dy%2FMal6ffa5jb47m0VrEnwNMO1wZ4Xla2eHOAVRkOcD5eRcJjrt3nOtsckL%2FeXMrfcM2wRu3jB7F85oY05z5UNh3hbe5orVzf8MZZsYkg9A6S%2BLtf%2FVqB59qN%2FdJMHadVBkrhbAAz1Ecp%2BcunK6UeM%2BCpiZ%2B1Wczr4V2op3wfzT748IJnhHYWr1%2Fk5Ysc8K%2B20v0IFmRyy7GbrN%2B%2B34kWZzqt5vGRF1ZgBblANSwsZ9s3YzPHo0yfb1%2B6ov9yJCtiPjblrqqbk7yFWkxW9qPGs6cGNs4fibDWHEFgAQWQOcX30Zuuxzv26cLohHbIdgZu2RjDn9Xyl2NEuAafDNkcBXSK5EuEBi0byxk%2FKQrJH1545WI%2F%2BUPIWHXTlzz43FZXnbq2ECqnh7nKxML66PBNyJ7mZNj%2F2p7lPwntCy%2BNgeGySA7nzubhsOrK2t01ediPIMWjgN5n28xPBUQjFz5wQ%2FLgfsUWFG%2BXhD8m1w9hsnVpFOIOirT%2BWlRI0kfVa%2F5A6322Nr2WLnviFsezHVU0J%2B%2FyRPutOM%2BpADeCPY0R%2FbxyVP32MKrnjcD0OQrJv3Coxa%2FEORsN6WMSq%2BHVMNTI8MsGOqUBaPZiRure%2F2Tpgrbe78DrypEKb%2FUNwcSSvpgrK%2B2HiKonebTEFV4%2FnEbmG%2BdpoQ7P15ukgTyeSnXkrbK8KkhJpOhlEsTD9NYEHIDXmD%2F8DS7bGNJO1ADxaJZKvf9O0U8FX%2FtYfRDYziothHNXIYt7CAj9lg5Qm7g1BQ3Oww3f6MLC2g1P3UqQ2bFp%2F%2FG1JMYz97jAbMf%2Bn3xYm7MNGFExGeNuiEP9&X-Amz-Signature=cbb8eaea67c1127045613c5f4fd35ac9e62ab91eac6e7c4505053752f6cdf178&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWMEPJ4W%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtE6TuX9Mjq7ujqy4bCh7wTJj%2BLClp4Ytfz1%2FvgoQKnQIgH4%2BhWmmSbBekiy8wRQ9cwH9wwkYdAh0lc97FE%2FybP4QqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCL89yt6PcIftaB78SrcA5W7ifqdgx15AbHDZj3wP0v6nq5cdsA0e6RQn%2FKma70Dy%2FMal6ffa5jb47m0VrEnwNMO1wZ4Xla2eHOAVRkOcD5eRcJjrt3nOtsckL%2FeXMrfcM2wRu3jB7F85oY05z5UNh3hbe5orVzf8MZZsYkg9A6S%2BLtf%2FVqB59qN%2FdJMHadVBkrhbAAz1Ecp%2BcunK6UeM%2BCpiZ%2B1Wczr4V2op3wfzT748IJnhHYWr1%2Fk5Ysc8K%2B20v0IFmRyy7GbrN%2B%2B34kWZzqt5vGRF1ZgBblANSwsZ9s3YzPHo0yfb1%2B6ov9yJCtiPjblrqqbk7yFWkxW9qPGs6cGNs4fibDWHEFgAQWQOcX30Zuuxzv26cLohHbIdgZu2RjDn9Xyl2NEuAafDNkcBXSK5EuEBi0byxk%2FKQrJH1545WI%2F%2BUPIWHXTlzz43FZXnbq2ECqnh7nKxML66PBNyJ7mZNj%2F2p7lPwntCy%2BNgeGySA7nzubhsOrK2t01ediPIMWjgN5n28xPBUQjFz5wQ%2FLgfsUWFG%2BXhD8m1w9hsnVpFOIOirT%2BWlRI0kfVa%2F5A6322Nr2WLnviFsezHVU0J%2B%2FyRPutOM%2BpADeCPY0R%2FbxyVP32MKrnjcD0OQrJv3Coxa%2FEORsN6WMSq%2BHVMNTI8MsGOqUBaPZiRure%2F2Tpgrbe78DrypEKb%2FUNwcSSvpgrK%2B2HiKonebTEFV4%2FnEbmG%2BdpoQ7P15ukgTyeSnXkrbK8KkhJpOhlEsTD9NYEHIDXmD%2F8DS7bGNJO1ADxaJZKvf9O0U8FX%2FtYfRDYziothHNXIYt7CAj9lg5Qm7g1BQ3Oww3f6MLC2g1P3UqQ2bFp%2F%2FG1JMYz97jAbMf%2Bn3xYm7MNGFExGeNuiEP9&X-Amz-Signature=daf46045b002f7a57644ff966c2c5a063767a913faea2a375a5ddc0106f45b90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

