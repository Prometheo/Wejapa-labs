#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
#find 10% of the rainfall

tencent = (rainfall*10)/100
rainfall -= tencent


# add the rainfall variable to the reservoir_volume variable

reservoir_volume += rainfall


# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm

fivecent = (reservoir_volume*5)/100
reservoir_volume += fivecent


# decrease reservoir_volume by 5% to account for evaporation

new_fivecent = (reservoir_volume*5)/100
reservoir_volume -= new_fivecent


# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.

reservoir_volume -= 2.5e5



# print the new value of the reservoir_volume variable
print(reservoir_volume)