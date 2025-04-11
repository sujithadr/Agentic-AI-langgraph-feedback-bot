from typing_extensions import TypedDict, Annotated
from project.operators import merge_dicts

class State(TypedDict):
    """
    LangGraph State structure that flows between nodes.
    Annotated fields specify how values should be combined.
    """
    text: str
    tag: str
    answer: Annotated[dict, merge_dicts]
    payload: dict[str, list]
