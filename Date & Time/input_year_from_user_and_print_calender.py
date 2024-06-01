import calendar;
import string;
import time;
value=False;
def main():
     global value;
     while not value:
          try:
               year=int(input(f"Enter the year which calender you wanna see="));
               if year<=0:
                    print('Please Enter the positive year');
                    continue;     
               value=True;
          except:
               print('Error!!please Enter the year again....');
               continue;
     print(f'The calender for the year {year} is......');
     print(calendar.prcal(year));
main();