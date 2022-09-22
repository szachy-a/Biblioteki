from unittest import TestCase, main
from bittabl import BitTabl

class BitTablTestCase(TestCase):
    def testBitTablJedenInt(self):
        bt = BitTabl(10)
        bt[2] = 1
        bt[5] = 1
        self.assertEqual(1, bt[2])
        self.assertEqual(1, bt[5])
        self.assertEqual(0, bt[3])
        
    def testBitTablDwaInty(self):
        bt = BitTabl(70)
        bt[4] = 1
        bt[68] = 1
        self.assertEqual(1, bt[4])
        self.assertEqual(1, bt[68])
        self.assertEqual(0, bt[69])
        self.assertEqual(0, bt[1])
        
    def testBitTablDwaWIncie(self):
        bt = BitTabl(5)
        bt[1] = 1
        bt[3] = 1
        bt[2] = 1
        bt[2] = 0
        self.assertEqual(1, bt[1])
        self.assertEqual(1, bt[3])
        self.assertEqual(0, bt[2])

    def testBitTablNieprawidlowyIndeks(self):
        bt = BitTabl(5)
        with self.assertRaises(IndexError):
            bt[18] = 1
        with self.assertRaises(IndexError):
            q = bt[100]
        with self.assertRaises(IndexError):
            bt[-1] = 1
        with self.assertRaises(IndexError):
            q = bt[-1]

    def testBitTablNieprawidlowyBit(self):
        bt = BitTabl(10)
        with self.assertRaises(ValueError):
            bt[5] = 3

 

if __name__ == '__main__':
    main()
