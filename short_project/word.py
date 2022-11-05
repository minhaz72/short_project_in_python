import countryinfo 
from countryinfo import Countryinfo 

country=  str(input('enter your County Name : '))
coun= Countryinfo(country)

print(f'the capital is {coun.capital()}')
print(f'the population of {coun} is {coun.population} ')
print(f'the currency of the country is {coun.currencies }')
print( f'the mother toungh of this country is {coun.languages} ')

