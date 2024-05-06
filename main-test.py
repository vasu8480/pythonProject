from main import Add

def TestAdd():
    assert Add(2,3) == 5
    assert Add(2,3) == 2
    print("Add Function works correctly")
    print("from vasu")

if __name__ == '__main__':
    TestAdd()