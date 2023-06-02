from bpp3d_dataset import hello

def test_hello():
    name = "your name"
    assert hello(name) == f"hello {name}" 