air_temp=float(input('Enter The Air Temperature (Degre F)\t'))
air_speed=float(input('Enter The Air Speed (MPH)\t'))


wct_index = 35.74 + 0.6215 * air_temp \
- 35.75 * air_speed ** 0.16 \
+ 0.4275 * air_temp * air_speed ** 0.16
print ('wind chill temperature index ' ,wct_index )