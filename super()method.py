a = int(input("Enter the price : ₹"))
if 50<a<300 :
    a1 = a*(15/100)+a
    print("#Total Tip             : ₹",a*(15/100))
    print("#Total Tip without Tip : ₹",a)
    print("#Total Tip with Tip    : ₹",a1)
else :
    a2 = a*(20/100)+a
    print("#Total Tip             : ₹",a*(20/100))
    print("#Total Tip without Tip : ₹",a)
    print("#Total Tip with Tip    : ₹",a2)


