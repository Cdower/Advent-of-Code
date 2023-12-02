import aoc_lube

LINES = aoc_lube.fetch(year=2023, day=2).splitlines()

TEST_LINES = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines()

def parse_line(line):
  id, sets = line.split(":")
  sets = sets.split(";")
  for i in range(len(sets)):
    set_list = sets[i].split(",")
    set_map = {}
    for cubes in set_list:
      count, color = cubes.strip().split(" ")
      set_map[color] = int(count)
    sets[i] = set_map
  ret = {
    "id": int(id.split(" ")[1]),
    "sets": sets,
  }
  return ret

def parse_lines(lines):
  ret = []
  for line in lines:
    game = parse_line(line)
    ret.append(game)
  return ret

def part_one(data=LINES):
  sum = 0
  bag = { "red": 12, "green": 13, "blue": 14}
  games = parse_lines(data)
  for game in games:
    invalid = False
    for set in game["sets"]:
      for color, count in set.items():
        if count > bag[color]:
          invalid = True
          break
      if invalid:
        break
    if not invalid:
      # print(f"Game {game["id"]}: valid" )
      sum += game["id"]
    # else:
    #   print(f"Game {game["id"]}: invalid. {count} {color} > {bag[color]} {color} in bag.")
    #   print(f"\t{game["sets"]}")
  return sum

def part_two(data=LINES):
  sum = 0
  games = parse_lines(data)
  for game in games:
    min_set = {}
    for set in game["sets"]:
      for color in set.keys():
        if color not in min_set:
          min_set[color] = set[color]
        else:
          min_set[color] = max(min_set[color], set[color])
    power = 1
    for color, count in min_set.items():
      power *= count
    sum += power
  return sum

p1_test = part_one(TEST_LINES)
p2_test = part_two(TEST_LINES)
p1 = part_one()
p2 = part_two()
assert p1_test == 8
assert p2_test == 2286
assert p1 == 2685
assert p2 == 83707

print(f"Part One Solution: {p1}")
print(f"Part Two Solution: {p2}")

# aoc_lube.submit(year=2023, day=2, part=1, solution=part_one)
# aoc_lube.submit(year=2023, day=2, part=2, solution=part_two)
