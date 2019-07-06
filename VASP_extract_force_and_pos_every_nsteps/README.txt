
"pot_en" is obtained by typing "grep 'e_b>' REPORT  | awk '{print $3}'  > pot_en &" in linux system.
"posADforce" is obtained by typing "cat OUTCAR | sed -n '/POSITION/,/total drift:/{/total drift:/b;p}' > PosAndForce &" in linux system.