def Easy158(n):
  assert type(n) == int and 0 <= n <= 9999
  left, right  = n / 100, n % 100
  unique_nums  = len(set([left / 10, left % 10, right / 10, right % 10])) == 4
  math_formula = n == (left+right) ** 2 
  return unique_nums and math_formula

print Easy158(3025)
print Easy158(0)
