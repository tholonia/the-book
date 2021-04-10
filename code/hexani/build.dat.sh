status=pending
rating=TBD
psn=0
# ┌───────────────────────────────────────────────────
# │ 🟠 **** 🟠 KEEP  NUMBEWR ARE CRAZY (redo)
# └───────────────────────────────────────────────────
delay=60

a01="--name        ${name}"
a02="--series      ${series}"

a03"--ncount      6"
a04="--SES         0,361,1"
a05="--angle       60" 		# necessary??
a06="--length      40"

a07="--lenDev      0:0"
a08="--angDev      0:0"		#<pct>:<random> <0-1>:<0-1> <pct> is percent, but as decimal, 0.3 = 30%. <random> 1=only use HIGHEST value, 0=randomely chosese btn LOWEST and HIGHEST
a09="--usecolor    default" # (see 'palletes' below)
a10="--use_alt_color default"
a11="--style       11,9,7,5,3,1" #
a12="--flowersize  12"		# remember to adjust 'length'... length + flowersize <= 70
a13="--outline     no"		# <no", or <color name> | <color code> | "reverse",  pensize can be optionally defined as ...  black:4, if using codes, '#!A467ED:3', it MUST be quoted
a14="--growflower  0"		  # 0 = off/NO, 1 = on/YES
a15="--syncpoints  0"		  # 0 = off (only valid if there is angular or length randomness)
a16="--cores       1"			# 1 or 2
a17="--randclr     0"     # 1 = yes, 0 = no

a18="--desc_only   0"
a19=""
a20=""

# pallets
# ---------
# 'random' ,'darkgrays' ,'lightgrays' ,'default' ,'medical_gray','medical_gray_3' ,'aura_red' ,'pi' ,'progressive3' ,'progressive4','SinSinSin' ,'
# SinSinSinFast' ,'SinCosSin' ,'SinCosDelta' ,'SinCosDeltaFast','prog_A' ,'prog_B' ,'prog_C': ,'prog_C_fast'
# greens
# browns

