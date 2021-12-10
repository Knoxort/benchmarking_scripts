from copy import deepcopy
import numpy as np
import math

def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
def square (a):
    return (a*a)
def cube (a):
    return (a*a*a)
def ln(a):
    return (np.log(a))
def exp(a):
    return (math.exp(a))


#aabcfn_nft = ("add(mul(mul(add(div(1.0, add(mul(square(add(mul(size, 0.984389464024), 0.611576472456)), 1.00000091351), -0.00145783162768)), mul(add(mul(size, 2.16153080235e-06), -0.000102086535598), size)), add(mul(square(mul(cube(add(mul(square(add(mul(size, 0.999999366907), 1.65096305966e-05)), 0.997106286111), 0.27061336757)), 1.00000000013)), 2.35014648952e-15), -0.047996134208)), 2.18024879476e-06), 3.92282079185e-06)")

aabcfn_nft = ("add(mul(cube(add(add(mul(ln(add(mul(div(add(mul(square(add(mul(size, 4.43349955561), -133.398813815)), 1.00000000032), -6.57500571721e-07), add(mul(size, -25644.2057259), 455803137.882)), 6543892.86191), 17.4083372601)), 1.00284171734), -0.010210794622), add(add(mul(ln(add(add(mul(size, 0.636941593958), -9.55412434521), add(mul(div(add(mul(cube(size), 0.595807979601), 1364.08839403), add(mul(size, 0.999999859765), 1.72087716948)), 5.92658401946e-09), -4.3058461308e-07))), 1.03979393372), -0.125729303345), add(mul(size, 1.0335144459), 0.046280480941)))), 4.68681143019e-11), 2.44037772749e-07)")

aabcfn_ft = ("add(mul(mul(add(add(add(mul(size, 1.00493293798), 1.19396323052), add(mul(size, -1.94357933085), 2.19476194084)), add(mul(size, 1.93861391747), -0.765191285305)), add(mul(ln(add(mul(mul(add(mul(square(add(mul(size, 0.26006594007), -9.78767918425)), 1.0), -5.5891527765e-14), add(mul(square(add(mul(size, 0.260070801294), -9.78779727318)), 5.2156426279e-08), 0.74908151607)), 1.00000000006), 0.13457675858)), 0.999999981682), 6.08941173004e-09)), -5.79642931111e-08), 4.78328868069e-06)")

ampfe_nft = ("add(mul(mul(add(add(mul(ln(add(mul(size, 1.00347807085), -0.0923938307393)), 0.999999999214), 2.64584053808e-09), add(mul(mul(add(mul(size, 10.7830330952), -293.166928913), add(mul(size, 3.70663317202), add(mul(ln(add(mul(size, 1.00000295901), 1.23066060684e-06)), 1.42036624104e-05), -80.1455742027))), 8.94977649728e-05), -0.0804710254183)), add(add(mul(ln(add(mul(ln(add(mul(size, 1.52801423307), -7.24792087226)), 1.00000000001), -2.97856756663e-11)), -283.464021941), 329.555965141), add(mul(square(add(mul(size, 24.1400984448), -235.57142399)), 1.0), -3.744207185e-12))), 3.7571162568e-09), 0.000115059034464)")

ampfe_ft = ("add(mul(mul(add(mul(square(add(mul(mul(add(mul(mul(add(mul(cube(add(mul(size, 3.6828192811), -28.258728457)), 1.0), 7.03559552992e-09), add(mul(size, 0.000110067050703), -0.000626221408583)), 0.00331547941671), 24.2609260665), add(add(mul(size, 7.36538292762e-05), 1.63922272608e-13), add(mul(ln(add(mul(cube(add(mul(size, 0.99999999964), 3.60396788046e-09)), 1.03949109508), -1039.36864964)), -1.91926413294e-09), -0.000389344379156))), 0.999999999999), 3.85743008567e-15)), 1.00004405581), -1.56232076928e-07), add(mul(square(add(mul(mul(add(mul(size, 0.0992504372586), -3.20639130708), add(mul(size, 0.977780822155), 0.736984705949)), 0.708364324658), 2.54296588227)), -4.79300179e-06), 1.00273938593)), 1.00026377561), -1.26045179344e-05)")

for size in range(1,100,1):
  print(str(size) + ',' + str(eval(aabcfn_nft)) + ',' + str(eval(aabcfn_ft)) + ',' + str(eval(ampfe_nft)) + ',' + str(eval(ampfe_ft)) )
  #print (eval(e1))
  #print(str(size) + ',' + eval(aabcfn_nft) + ',' + eval(abbcf_ft))
