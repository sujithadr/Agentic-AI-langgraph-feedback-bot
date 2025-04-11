def merge_dicts(dict1, dict2):
    """
    Custom dictionary merge function used in LangGraph's Annotated state handling.
    Combines values from multiple nodes.
    """
    return {**dict1, **dict2} # Merge dict2 into dict1, overwriting keys in dict1 with dict2's values

