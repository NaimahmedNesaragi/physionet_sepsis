head -n 1 p000001.psv > merged.psv 
for f in *.psv; do tail -n +2 -q "$f"; done >> merged.psv