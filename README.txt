Welcome to the Currency Converter!
----------------------------------

This program uses Python to accept an input file indicating an amount, the currency
it is currently expressed as, and the currency the user wishes the amount to 
be expressed as. The base currency for the program is US dollars and the exchange
rates are based on Google data collected in December 2020. 

To convert an amount, the input file should be expressed in the following format:
<current currency>
<amount to be converted>
<desired currency>

Each piece of data should be separated in a new line as the program will input the
formatted file and create a list from the lines on the file. 

Once the list has been created, it is used to determine the current currency of the
amount, the amount itself, and the currency the amount is to be converted into. 
This program can convert a US dollar amount to pounds, euros, yuan, or rubles and 
vice versa. 

The program uses if-else statements to determine the exchange rate to apply and
then creates an object, using the class exchangeRates, to convert the value.

Once, the amount is converted, the program then prints out the newly converted 
amount into an output file, named by the user. 


Example Run: 
-------------

- Input File Example - 
gdp
100
usd


Please enter the name of the file: example.txt
Please enter the name of the output file: output.txt

- Output File Example - 
134.0