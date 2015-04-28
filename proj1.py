#Python3 compaitable code 
#Energy Content in earthquake
richter_scale=float(input("Enter The Value of richter_scale \t"))
E=10**(1.5*richter_scale+4.8)
print ("Energy Content in it ",E,'Joules')
print ("TNT Content Equivalent in tons ",E/(4.184 * 10**9),'Tones')
