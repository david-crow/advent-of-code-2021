# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import re

answer = sum(int(n) for n in re.findall(r"-?[\d]+", data))
# print(nums)

# import json

# data = json.loads(data)

# def eval(item):
#     if type(item) == int:
#         return item
#     if type(item) == list:
#         return sum([eval(i) for i in item])
#     if type(item) == dict:



# submission

print(answer)
submit(answer, part=part, day=day, year=year)
