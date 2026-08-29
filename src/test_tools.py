from src.tools.knowledge_retrieval import (
    search_knowledge_base,
)


results = search_knowledge_base(
    "Can employees go abroad for work?"
)

for result in results:
    print(result)
    print("---")