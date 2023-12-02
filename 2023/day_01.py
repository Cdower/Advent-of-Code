import aoc_lube

LINES = aoc_lube.fetch(year=2023, day=1).splitlines()

TEST_PART_ONE = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

TEST_PART_TWO = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def part_one(data=LINES) -> int:
  sum=0
  for line in data:
    i=0
    j=len(line)-1
    first, last = "", ""
    while i <= j:
      if line[i].isnumeric():
        first = line[i]
      else:
        i+=1
      if line[j].isnumeric():
        last = line[j]
      else:
        j-=1
      if first and last:
        break
    sum+=int(f"{first}{last}")
  return sum

def part_two(data=LINES) -> int:
  sum=0
  for line in data:
    lidx = len(line)
    ridx = 0
    l_key = ""
    r_key = ""
    for key in numbers:
      l = line.find(key)
      r = line.rfind(key)
      if l != -1:
        lidx = min(lidx, l)
      if r != -1:
        ridx = max(ridx, r)
      if l == lidx:
        l_key = key
      if r == ridx:
        r_key = key
    # if l_key:
    #   line = line.replace(l_key, str(numbers[l_key]))
    # if r_key:
    #   line = line.replace(r_key, str(numbers[r_key]))
    # line = line.replace(key, str(numbers[key]))
    i=0
    j=len(line)-1
    first, last = "", ""
    first_idx, last_idx = len(line), 0
    while i <= j:
      if line[i].isnumeric():
        first = line[i]
        first_idx = i
      else:
        i+=1
      if line[j].isnumeric():
        last = line[j]
        last_idx = j
      else:
        j-=1
      if first and last:
        break
    if ridx > last_idx:
      last = numbers[r_key]
    if lidx < first_idx:
      first = numbers[l_key]
    # print(f"{first}{last} {line}")
    sum+=int(f"{first}{last}")
  return sum

p1_test = part_one(TEST_PART_ONE)
p2_test = part_two(TEST_PART_TWO)
p1 = part_one()
p2 = part_two()
assert p1_test == 142
assert p2_test == 281
assert p1 == 54081
assert p2 == 54649
print(f"Part One Solution: {p1}")
print(f"Part Two Solution: {p2}")

# aoc_lube.submit(year=2023, day=1, part=1, solution=part_one)
# aoc_lube.submit(year=2023, day=1, part=2, solution=part_two)
