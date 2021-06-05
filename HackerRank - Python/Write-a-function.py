
def is_leap(year):
  return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
year = int(input())

# ****************** OR ****************************************

def is_leap(year):
    leap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return leap
        else:
            return True
    else:
        return leap

year = int(input())
print(is_leap(year))
  

  
