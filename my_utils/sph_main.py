def add_number(a, b):
    """ simpe add function

    説明の追加は日本語でもいける？
    なんかいろいろ書いてもよさそう
    Todo:
        Todo.これとか同じ感じで入る？
    
    Args:
        a (int): first number...
        b (int): second number

    Returns:
        int: sum of a and b

    Notes: 
        これはノートです
    
    Note:
        これもノートです

    Warnings: 
        これはワーニングです

    Raises:
        ValueError: aとbはintである必要があります

    Examples:
        >>> add_number(1,2)

    Tip:
        https://www.sphinx-doc.org/ja/master/usage/extensions/napoleon.html
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a and b must be int")
    return a + b