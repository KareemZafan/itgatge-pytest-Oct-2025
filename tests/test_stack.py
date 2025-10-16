from src.stack import Stack 


class TestStack:

    def test_push(self):
        stc = Stack()
        assert stc.is_empty() == True

        stc.push("Ahmed")
        stc.push("Mahmoud")
        stc.push("Ali")

        assert stc.get_peek() == "Ali"
        assert stc.get_stack_size() == 3
        assert stc.get_stack_elements() == ["Ahmed","Mahmoud","Ali"]

    def test_pop(self):
        stc = Stack()
        assert stc.is_empty() == True

        stc.push("Ahmed")
        stc.push("Mahmoud")
        stc.push("Ali")
        stc.push("Ahmed2")
        stc.push("Mahmoud2")
        stc.push("Alaa")

        assert stc.get_peek() == "Alaa"
        assert stc.get_stack_size() == 6
        assert stc.get_stack_elements() == ["Ahmed","Mahmoud","Ali","Ahmed2","Mahmoud2","Alaa"]
        

        res = stc.pop()
        assert res == "Alaa"
        assert stc.get_peek() == "Mahmoud2"
        assert stc.get_stack_size() == 5
        assert stc.get_stack_elements() == ["Ahmed","Mahmoud","Ali","Ahmed2","Mahmoud2"]


