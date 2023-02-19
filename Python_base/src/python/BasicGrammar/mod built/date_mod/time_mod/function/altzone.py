from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
time.altzone()：返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
"""

print("time.altzone %d " % time.altzone)
