"""
Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Philip Cipollina (pjc272) Luke Marcinkiewicz (lam365)
September 14th, 2017
"""
import cornell
import a1


def testA():
     "Test procedure for Part A"
     
     s='this is fun' #has multiple spaces
     A=a1.before_space(s)
     cornell.assert_equals('this',A)
     A=a1.after_space(s)
     cornell.assert_equals('is fun',A)
   
     s=' CS is fun' #begins with a space
     A=a1.before_space(s)
     cornell.assert_equals('',A)
     A=a1.after_space(s)
     cornell.assert_equals('CS is fun',A)
   
     s='Hello World' #Has only 1 space
     
     A=a1.before_space(s)
     cornell.assert_equals('Hello',A)
     
     A=a1.after_space(s)
     cornell.assert_equals('World',A)
   
     s='1 2 3' #Uses numbers instead of letters
     
     A=a1.before_space(s)
     cornell.assert_equals('1',A)
     
     A=a1.after_space(s)
     cornell.assert_equals('2 3',A)
   
     s='Test Case 5 ' #Ends with a space
     A=a1.before_space(s)
     cornell.assert_equals('Test',A)
     
     A=a1.after_space(s)
     cornell.assert_equals('Case 5 ',A)

     s='Double-Space  Test' #Has multiple spaces in a row
     A=a1.before_space(s)
     cornell.assert_equals('Double-Space',A)
     
     A=a1.after_space(s)
     cornell.assert_equals(' Test',A)
     
     s='Hello '
     A=a1.after_space(s)
     cornell.assert_equals('',A)     
def testB():
     "Test procedure for Part B"
     
     #Tests quotations
     B=a1.first_inside_quotes('I said "Hello" to him')
     cornell.assert_equals('Hello',B)
     
     #Tests multiple sets of quotes
     B=a1.first_inside_quotes('The "dog" said "hello" to him.') 
     cornell.assert_equals('dog',B)

     #Tests sentence beginning with quotes
     B=a1.first_inside_quotes('"This is a quote"- Phil') 
     cornell.assert_equals('This is a quote',B)
     
     #tests sentence ending in quotes
     B=a1.first_inside_quotes('He said "how are you"')
     cornell.assert_equals('how are you',B)
     
     #tests empty string return
     B=a1.first_inside_quotes('""')
     cornell.assert_equals('',B)
     
     #tests entirety within quotes
     B=a1.first_inside_quotes('"All Inside"')
     cornell.assert_equals('All Inside',B)
     
     #Tests lhs
     B=a1.get_lhs('{ "success" : true, "lhs" : "2.5 United States Dollars",'+
                  '"rhs" : "2.0952375 Euros", "error" : "" }')
     cornell.assert_equals('2.5 United States Dollars',B)
     
     #tests rhs
     B=a1.get_rhs('{ "success" : true, "lhs" : "2.5 United States Dollars",' +
                  ' "rhs" : "2.0952375 Euros", "error" : "" }')
     cornell.assert_equals('2.0952375 Euros',B)
     
     #checks for error
     B=a1.has_error('{ "success" : true, "lhs" : "2.5 United States Dollars",' +
                    '"rhs" : "2.0952375 Euros", "error" : "" }')
     cornell.assert_equals(False,B)
     
     #four digit number and same currency on both sides
     B=a1.get_lhs('{ "success" : true, "lhs" : "1000 United States Dollars", ' +
                  '"rhs" : "1000 United States Dollars", "error" : "" }')
     cornell.assert_equals('1000 United States Dollars',B)
     
     B=a1.get_rhs('{ "success" : true, "lhs" : "1000 United States Dollars",' +
                  '"rhs" : "1000 United States Dollars", "error" : "" }')
     cornell.assert_equals('1000 United States Dollars',B)
     
     B=a1.has_error('{ "success" : true, "lhs" : "1000 United States Dollars",'
                   + '"rhs" : "1000 United States Dollars", "error" : "" }')
     cornell.assert_equals(False,B)
     
     #checks that function works with 0
     B=a1.get_lhs('{ "success" : true, "lhs" : "0 Bosnia-Herzegovina ' +
                  'Convertible Marks", "rhs" : "0 Macanese Patacas", "error" :'+ 
                  '  "" }')
     cornell.assert_equals('0 Bosnia-Herzegovina Convertible Marks',B)
     
     B=a1.get_rhs('{ "success" : true, "lhs" : "0 Bosnia-Herzegovina '+        
                    'Convertible Marks", "rhs" : "0 Macanese Patacas", "error"'+
                   ' : "" }')
     cornell.assert_equals('0 Macanese Patacas',B)
     
     B=a1.has_error('{ "success" : true, "lhs" : "0 Bosnia-Herzegovina '+        
                    'Convertible Marks", "rhs" : "0 Macanese Patacas", "error"'+
                   ' : "" }')
     cornell.assert_equals(False,B)
     
     #Checks when there is an error
     B=a1.has_error('{ "success" : false, "lhs" : "", "rhs" : "", "error" : '+
     '"Source currency code is invalid." }')
     cornell.assert_equals(True,B)
     
     B=a1.get_lhs('{ "success" : false, "lhs" : "", "rhs" : "", "error" : '+
     '"Source currency code is invalid." }')
     cornell.assert_equals('',B)
     
     B=a1.get_rhs('{ "success" : false, "lhs" : "", "rhs" : "", "error" : '+
     '"Source currency code is invalid." }')
     cornell.assert_equals('',B)
     
     #Checks negatives
     B=a1.get_lhs('{ "success" : true, "lhs" : "-5 United States Dollars", '+
     '"rhs" : "-4.190475 Euros", "error" : "" }')
     cornell.assert_equals('-5 United States Dollars',B)
     
     B=a1.get_rhs('{ "success" : true, "lhs" : "-5 United States Dollars", '+
     '"rhs" : "-4.190475 Euros", "error" : "" }')
     cornell.assert_equals('-4.190475 Euros',B)

     #Checks 1 digit number left side
     B=a1.get_lhs('{ "success" : true, "lhs" : ".5 United States Dollars", '+
     '"rhs" : ".5 Cuban Converible Peso", "error" : "" }')
     cornell.assert_equals('.5 United States Dollars',B)
     
     #Checks 1 digit number right side
     B=a1.get_rhs('{ "success" : true, "lhs" : ".5 United States Dollars", '+
     '"rhs" : ".5 Cuban Convertible Peso", "error" : "" }')
     cornell.assert_equals('.5 Cuban Convertible Peso',B)
     
     #checks exponents
     B=a1.get_rhs('{ "success" : true, "lhs" : "0.5 Japanese Yen", "rhs" : '+
                  '"3.4292199622937E-6 Troy Ounces of Gold", "error" : "" }')
     cornell.assert_equals('3.4292199622937E-6 Troy Ounces of Gold', B)
     
     B=a1.get_lhs('{ "success" : true, "lhs" : "1.049E+101 Troy Ounces of Gold'+
                  '", "rhs" : "1.5295023526259E+106 Japanese Yen", "error" : '+
                  '"" }')
     cornell.assert_equals('1.049E+101 Troy Ounces of Gold', B)

def testC():
     "Test procedure for Part C"
     
     #Checks function
     C=a1.currency_response('USD','EUR',3.0)
     cornell.assert_equals('{ "success" : true, "lhs" : "3 United States ' +
                         'Dollars", "rhs" : "2.514285 Euros", "error" : "" }',C)
     
     #Checks 4 digits, non-zero after decimal
     C=a1.currency_response('CLF','CLP', 100.5)
     cornell.assert_equals('{ "success" : true, "lhs" : "100.5 Chilean ' +
     'Unidades de Fomento", "rhs" : "2703693.530939 Chilean Pesos", "error" '
     +': "" }',C)
     
     #Checks negatives
     C=a1.currency_response('NZD','OMR',-10.0)
     cornell.assert_equals('{ "success" : true, "lhs" : "-10 New Zealand '+
     'Dollars", "rhs" : "-2.7750571241161 Omani Rials", "error" : "" }',C)
     
     #Checks 0
     C=a1.currency_response('SRD','SAR',0.0)
     cornell.assert_equals('{ "success" : true, "lhs" : "0 Surinamese '+
                    'Dollars", "rhs" : "0 Saudi Riyals", "error" : "" }',C)
     
     #Checks invalid input
     C=a1.currency_response('ABC', 'USD', 40.0)
     cornell.assert_equals('{ "success" : false, "lhs" : "", "rhs" : "", '+
                           '"error" : "Source currency code is invalid." }',C)
      
      #Checks 1 digit input
     C=a1.currency_response('NZD','OMR',.1)
     cornell.assert_equals('{ "success" : true, "lhs" : "0.1 New Zealand '+
     'Dollars", "rhs" : "0.027750571241161 Omani Rials", "error" : "" }',C)
     
     #Checks exponents
     C=a1.currency_response('USD','USD',1.434525E10)
     cornell.assert_equals('{ "success" : true, "lhs" : "14345250000 United ' +
                           'States Dollars", "rhs" : "14345250000 United States'
                           +' Dollars", "error" : "" }',C)
          

def testD():
     "Test procedure for Part D"
     
     #Checks invalid
     D=a1.iscurrency('ABC')
     cornell.assert_equals(False,D)
    
    #Checks valid
     D=a1.iscurrency('EUR')
     cornell.assert_true(D)
     
     #Checks currency with no value from chart
     D=a1.iscurrency('MTL')
     cornell.assert_false(D)
     
     #Checks 1 letter
     D=a1.iscurrency('A')
     cornell.assert_false(D)
     
     #Checks 4 letters
     D=a1.iscurrency('ABCDE')
     cornell.assert_false(D)
     
     #Checks empty string
     D=a1.iscurrency('')
     cornell.assert_false(D)
     
     #Checks function
     D=a1.exchange('USD', 'AUD', 1.0)
     cornell.assert_floats_equal(1.25541,D)
     
     #Checks large numbers
     D=a1.exchange('BTC','ETB',10000.0)
     cornell.assert_floats_equal(1076784196.0124,D)
     
     #Checks 0
     D=a1.exchange('GBP','SVC',0.0)
     cornell.assert_floats_equal(0.0,D)
     
     #Checks negative
     D=a1.exchange('HKD','SOS',-154.8)
     cornell.assert_floats_equal(-11463.369846692,D)
     
     #checks single digit, exponential output
     D=a1.exchange('JPY','XAU',.5)
     cornell.assert_floats_equal(3.4292199622937E-6,D)
     
     #Checks exponential input
     D=a1.exchange('XAU','JPY',10.49E6)
     cornell.assert_floats_equal(1529502352625.9,D)

testA()
testB()
testC()
testD()
print("Module a1 passed all tests") 