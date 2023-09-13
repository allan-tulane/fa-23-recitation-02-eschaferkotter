from main import *

def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(50, 2, 2) == 276
  assert simple_work_calc(30, 2, 2) == 128
  assert simple_work_calc(75, 4, 2) == 8255
  
def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(8,2,2,lambda n:n) == 32