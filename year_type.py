year=input('請輸入西元年')
year=int(year)

def is_leap():
    if year % 4 != 0:
        print('平年')
        return False
    elif year % 100 != 0:
        print('閏年')
        return False
    elif year % 400 != 0:
        print('平年')
        return False 
    elif year % 3200 != 0:
          print('潤年')
          return False
    else:
        print('平年')
        return True
    
is_leap()