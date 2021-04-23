from Calculator import Calc


class TestCalc:
    def test_add(self):
        assert Calc.add(3, 4) == 7
        assert 10 == Calc.add(5, 5)
        assert 9 == Calc.add(5, 4)

    def test_sub(self):
        assert 1 == Calc.sub(3, 2)
        assert 1000 == Calc.sub(1001, 1)
