#! /usr/bin/python3
import unittest
import auto
class TestJakis(unittest.TestCase):
    def test_f0(self):
        self.assertTrue(True)
    def test_f1__1(self):
        w = auto.f1(0)
        self.assertEqual(w,0)
    def test_f1_2(self):
        c = auto.f1(1)
        self.assertEqual(c,1)
    def test_f1_3(self):
        b = auto.f1(2)
        self.assertEqual(b,4)
    def test_f1_4(self):
        d = auto.f1(2,1)
        self.assertEqual(d,5)
    def test_f1_4(self):
        d = auto.f1(2,3)
        self.assertEqual(d,7)
    def test_f2_1(self):
        w = auto.f2('ala')
        self.assertEqual(w,'a')
    def test_f2_2(self):
        w = auto.f2([1,2,3])
        self.assertEqual(w,1)
    def test_f2_3(self):
        w = auto.f2([])
        self.assertEqual(w,'BUUM')
    def test_f3_1(self):
        w = auto.f3(1)
        self.assertEqual(w,'jeden')
    def test_f3_2(self):
        w = auto.f3(2)
        self.assertEqual(w,'dwa')
    def test_f3_3(self):
        w = auto.f3(3)
        self.assertEqual(w,'trzy')
    def test_f3_4(self):
        w = auto.f3(6)
        self.assertEqual(w,'other')
    def test_f4_1(self):
        w = auto.f4('ala')
        self.assertEqual(w,'ala ma kota')
    def test_f4_2(self):
        w = auto.f4('kot')
        self.assertEqual(w,'kot ma kota')
    def test_f4_3(self):
        w = auto.f4('kot', 'psa')
        self.assertEqual(w,'kot ma kota i psa')
    def test_f4_4(self):
        w = auto.f4('kot', 'mysz')
        self.assertEqual(w,'kot ma kota i mysz')
    def test_f5_1(self):
        w = auto.f5(0)
        self.assertEqual(w,[])
    def test_f5_2(self):
        w = auto.f5(1)
        self.assertEqual(w,[0])
    def test_f5_3(self):
        w = auto.f5(2)
        self.assertEqual(w,[0,1])
    def test_f5_4(self):
        w = auto.f5(7)
        self.assertEqual(w,[0,1,2,3,4,5,6])
    def test_f5_5(self):
        w = auto.f5(7,2)
        self.assertEqual(w,[0,2,4,6])
if __name__ == '__main__':
    unittest.main()
