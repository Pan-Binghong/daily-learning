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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THYYJRSQ%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDGRluH8QhPaoHp0sUxMEX8xqwmCoiMHVSLpZCFLHY%2BxgIhAJtBtRxWPZ0IvIHec9RBfD9q9rTGNP3l20j%2BwldOP5tYKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLWS2a8cAuIipDuC8q3APtRvizX6rbrpOusJ%2F02gVa1ucvCPSYdLwEOOTFexWWAtNbUmkHpUQ72HJyp76OO7sJbHcHDSCfa6ysN9lV4fMT6UXZzLqbb1D7KCnqCTIovm8TLY3oUIczTcShkDU6MhRBMoc22AD0%2F%2BaLuHlw3EGLmnTaqR9DIKYnsOQc9HQHD3yKGVGM%2B%2FX7phwUavE6HKTpJSD%2FUQSQ%2BZ053KC%2FgwsfW8uu9Y591zWCV2bNA0%2FjrZB0rxnx%2Fz12%2FvB9qjprl6arXM35%2F4S2CIb493jxezm9cNE%2FMo%2BFtNYR171o74GgaxSa6y8d%2BcruWjQirUkg%2FVzGlSVAPioC3xBg%2FlwTT6stxQyeuSURG%2BuCM7bZQ8nu76iMNyz0kVGRRn2gsj8nx3U019gO2oOILt4Mx%2Bh5SAp2yw2164d17AC1w8WacBv30Q9j8QdX2TYLiWMr9ewEdpSYj%2BJ8PGvsMWELS2EnJqMTKJX11EzL8B2Sw4yyJn7%2BTMwJqTmNdpllxnxNjO9sXfyP%2BfezSQ03qi80CvI1hxw%2FaKTkX3RzgM7XF7WVgkveRv8%2BuHC0eMCKRaDuMobVyfw%2Fqx4fmBfiT2RGwFnd5OvnxQev%2BoUFlusoUEYj0QfqRDhhWwNZDNa18x8WiDDupujNBjqkAcRZx4IYjvvbEtuEC2mrkkpU8fl9A2RbMeLkQ57E8p%2FL5XGneB%2FWC4e67mWMWbmCUBXxh15JBe0M8zzwhwzdEc90ud0tMaSjEFpBXxPFSWf%2FQO5EmaPzAKoi6iuSW8DuzMzhj%2FKuJNftssCLZiInguSyK%2FZPwWJtoR9yKHtluDHZiBy0wJ%2BreSro0%2FSsfgSd4b6whQkFveKv%2B3d9IeV810bQQxcm&X-Amz-Signature=e0ab3591aa88766809dbd355ca86691df48643eb92d2e434c969269d541a741d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THYYJRSQ%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDGRluH8QhPaoHp0sUxMEX8xqwmCoiMHVSLpZCFLHY%2BxgIhAJtBtRxWPZ0IvIHec9RBfD9q9rTGNP3l20j%2BwldOP5tYKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLWS2a8cAuIipDuC8q3APtRvizX6rbrpOusJ%2F02gVa1ucvCPSYdLwEOOTFexWWAtNbUmkHpUQ72HJyp76OO7sJbHcHDSCfa6ysN9lV4fMT6UXZzLqbb1D7KCnqCTIovm8TLY3oUIczTcShkDU6MhRBMoc22AD0%2F%2BaLuHlw3EGLmnTaqR9DIKYnsOQc9HQHD3yKGVGM%2B%2FX7phwUavE6HKTpJSD%2FUQSQ%2BZ053KC%2FgwsfW8uu9Y591zWCV2bNA0%2FjrZB0rxnx%2Fz12%2FvB9qjprl6arXM35%2F4S2CIb493jxezm9cNE%2FMo%2BFtNYR171o74GgaxSa6y8d%2BcruWjQirUkg%2FVzGlSVAPioC3xBg%2FlwTT6stxQyeuSURG%2BuCM7bZQ8nu76iMNyz0kVGRRn2gsj8nx3U019gO2oOILt4Mx%2Bh5SAp2yw2164d17AC1w8WacBv30Q9j8QdX2TYLiWMr9ewEdpSYj%2BJ8PGvsMWELS2EnJqMTKJX11EzL8B2Sw4yyJn7%2BTMwJqTmNdpllxnxNjO9sXfyP%2BfezSQ03qi80CvI1hxw%2FaKTkX3RzgM7XF7WVgkveRv8%2BuHC0eMCKRaDuMobVyfw%2Fqx4fmBfiT2RGwFnd5OvnxQev%2BoUFlusoUEYj0QfqRDhhWwNZDNa18x8WiDDupujNBjqkAcRZx4IYjvvbEtuEC2mrkkpU8fl9A2RbMeLkQ57E8p%2FL5XGneB%2FWC4e67mWMWbmCUBXxh15JBe0M8zzwhwzdEc90ud0tMaSjEFpBXxPFSWf%2FQO5EmaPzAKoi6iuSW8DuzMzhj%2FKuJNftssCLZiInguSyK%2FZPwWJtoR9yKHtluDHZiBy0wJ%2BreSro0%2FSsfgSd4b6whQkFveKv%2B3d9IeV810bQQxcm&X-Amz-Signature=cfaec5f996c8b44fd6f2c860d9222f6bcb49bef9f8c8977c4b27595df38f01d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

