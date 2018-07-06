# Let's check that the Front Panel Python API works correctly
# we follow the manual her on page 34: http://assets00.opalkelly.com/library/FrontPanel-UM.pdf

import ok # import the API

dev = ok.okCFrontPanel()
pll = ok.okCPLL22150()

# check that we have some objects from the ok. namespace
print(dev) 
print(pll)
