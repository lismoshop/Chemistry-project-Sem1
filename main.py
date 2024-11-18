import arrr
from pyscript import document
# import scipy.integrate as integrate
# import scipy.special as special
# from scipy.integrate import quad
# from numpy import sqrt, sin, cos, pi

# def translate_english(event):
#     input_text = document.querySelector("#english")
#     english = input_text.value
#     output_div = document.querySelector("#output")
#     output_div.innerText = arrr.translate(english)

def waveoutput(event):
    uiinput = document.querySelector("#uiwavefunctioninp")
    a = document.querySelector("uiwavefunctionlower")
    b = document.querySelector("uiwavefunctionupper")
    # result = integrate.quad(lambda x: special.jv(2.5,x), a, b)







    uioutput = document.querySelector("#uiwavefunctionoutp")
    # uioutput.innerText = arrr.translate(result)

