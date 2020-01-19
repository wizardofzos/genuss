# genuss

USSTAB generator...


## Very short howto

1. Create your own "ASCII-art" for your logon. Make sure no more than say 18 lines high and 79 cols in width
1. Add colors via "!=B" (for blue) or "!=G" for green. (see rest of color codes in genuss.py)
1. Make sure genuss.py takes YOUR ascii-art as input
1. Run genuss.py and have it output to 'middle'
1. cat HEAD middle TAIL > my-uss-tab.asm
1. Compile that and add to your TN3270 config ;)

Should look like this when using the provided screen-zdevops.txt

![alt text](https://raw.githubusercontent.com/wizardofzos/genuss/master/zdevops-usstab.png)
