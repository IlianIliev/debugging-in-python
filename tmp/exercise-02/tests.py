from main import create_element


def test():
    element = create_element("paragraph", [])
    assert element == {"type": "paragraph", "blocks": []}

