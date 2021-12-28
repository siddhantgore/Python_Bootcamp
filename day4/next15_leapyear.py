
def find_leap_years(given_year):
    leap=[]
    while(len(leap)<15):
        if(given_year%4==0 and given_year%100==0 and given_year%400==0):
            leap.append(given_year)
        given_year=given_year+1

    return leap

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)