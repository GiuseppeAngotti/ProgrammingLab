if i==0:
                subtracting=elements[1]
                i+=1
            else:
                try:
                    variation=elements[1]-subtracting
                    subtracting=elements[1]
                except Exception:
                    continue
        i=0
        elif s_year == date[0]:
            if i==0:
                subtracting=elements[1]
                i+=1
            else:
                try:
                    variation=elements[1]-subtracting
                    subtracting=elements[1]
                except Exception:
                    continue       