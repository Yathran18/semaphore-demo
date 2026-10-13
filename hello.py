def greet():
    return "Hello Semaphore!"

def test_greet():
    assert greet() == "Hello Semaphore!"

if __name__ == "__main__":
    test_greet()
    print("Test passed!")
