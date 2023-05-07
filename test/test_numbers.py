from my_utils import add_number
from dir2 import sub_number

class Tester():
    def test_add(self):
        assert add_number(1,2) == 3
    
    def test_sub(self):
        assert sub_number(1,2) == -1

if __name__=="__main__":
    t = Tester()
    t.test_add()
    t.test_sub()