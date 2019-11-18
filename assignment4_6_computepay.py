def computepay(h,r):
  if h <= 40 :
    return(pay)
  else:
    ovrhrs = (h-40)
    regular = (r*40)
    othrs = ovrhrs * (r *1.5)
    ovrpay = (regular + othrs)
    return(ovrpay)

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
pay = (h * r)
print(computepay(h,r))