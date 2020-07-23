#Quiz: Calculate
#In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

#1. How many tiles are needed?
#2. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?




# Fill this in with an expression that calculates how many tiles are needed.
first_part = 9 * 7
second_part = 5 * 7
tiles_needed = first_part+second_part

print("{} tiles are needed".format(tiles_needed))

# Fill this in with an expression that calculates how many tiles will be left over.
left_over = (17*6)-tiles_needed
print("if we buy 17 packages of tiles, there will be {} tiles left over".format(left_over))
