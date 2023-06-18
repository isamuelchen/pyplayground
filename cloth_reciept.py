price=quant=cost=cloth=hst=total=0
HST=.13
TAX=1.13
print("this program will help you calculate the costs of your clothing and give you a receipt")
print("what type of clothing do you want?")
cloth=input()
print("how much do ",cloth,"cost?")
price=int(input())
print ("how much ",cloth," do you want")
quant=int(input())
cost=price*quant
print("receipt")
print("-------------------------")
print("item","              ",cloth)
print ("cost","            ","$",price)
print("quantity","        ","$",quant,)
print("-------------------------")
hst=HST*cost
print("subtotal","        ","$",cost)
print("HST","             ","$",HST)
total=cost*TAX
print
print("total","           ","$","{total:.2f}".format(total= 2))
print("thanks for using this program!")





