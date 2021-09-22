"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Philip Cipollina (pjc272) Luke Marcinkiewicz (lam365)
September 14th, 2017
"""


def before_space(s):
    """
    Returns: Substring of s; up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    #find the space
    a=s.index(' ')
    #slice from beginning to the space
    result=s[:a]
    return result


def after_space(s):
    """
    Returns: Substring of s after the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    #find first space
    b=s.index(' ')
    #slice from 1 character after space to end
    result2=s[b+1:]
    return result2


def first_inside_quotes(s):
    """
    Returns: The first substring of s between two (double) quote characters
    A quote character is one that is inside a string, not one that delimits it.
    We typically use single quotes (') to delimit a string if want to use a
    double quote character (") inside of it.
       
    Example:  If s is 'A "B C" D', this function returns 'B C'
    Example:  If s is 'A "B C" D "E F" G', this function still returns 'B C'
    because it only picks the first such substring.
       
    Parameter s: a string to search
    Precondition: s a string with at least two (double) quote characters.
    """
    #find beginning quotes
    start=s.index('"')
    #store portion of text after it
    tail=s[start+1:]
    #find end quotes
    end=tail.index('"')
    result3=tail[:end]
    return result3


def get_lhs(json):
    """
    Returns: The the LHS value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "lhs". For example, if
    the JSON is
    '{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros",
    "error":""}'
    then this function returns '2 United States Dollars' (not '"2 United States
    Dollars"'). It returns the empty string if the JSON is the result of an
    invalid query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    #find string lhs
    left=json.index('"lhs"')
    #get value inside quotes after lhs
    val=json[left+5:]
    result4=first_inside_quotes(val)
    return result4


def get_rhs(json):
    """
    Returns: The RHS value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "rhs". For example, if
    the JSON is
    '{"success":true, "lhs":"2 United States Dollars", "rhs": "1.825936 Euros",
    "error":""}'
    then this function returns '1.825936 Euros' (not '"1.825936 Euros"'). It
    returns the empty string if the JSON is the result of on invalid query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    #find the string rhs
    right=json.index('"rhs"')
    #find value inside quotes following rhs
    valr=json[right+5:]
    result5=first_inside_quotes(valr)
    return result5


def has_error(json):
    """
    Returns: True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the opposite of
    the value following the keyword "success". For example, if the JSON is
    '{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is
    invalid."}'
    then the query is not valid, so this function returns True (It does NOT
    return the message 'Source currency code is invalid').
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    #find the beginning and end of segment where error value will appear 
    w=json.index(':')
    x=json.index(',')
    #slice the substring
    y=json[w+2:x]
    #compare to string 'false'
    z=bool(y=='false')
    return z


def currency_response(currency_from, currency_to, amount_from):
    """
    Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
        '{"success":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "error":""}'
    
    where the values old-amount and new-amount contain the value and name for
    the original and new currencies. If the query is invalid, both old-amount
    and new-amount will be empty, while "success" will be followed by the value
    false.
    
    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    import cornell
    #set url variable
    url='http://cs1110.cs.cornell.edu/2017fa/a1server.php?src='
    #add proper values to variable url
    url=url+currency_from + '&dst='+ currency_to +'&amt='+str(amount_from)
    result=cornell.urlread(url)
    return result


def iscurrency(currency):
    """
    Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string.
    """
    #input string to webserver
    input=currency_response('USD', currency, 1.0)
    #determine if there is an error using has_error
    err=has_error(input)
    result=bool(err==False)
    return result


def exchange(currency_from, currency_to, amount_from):
    """
    Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in currency 
    currency_from to the currency currency_to. The value returned represents the 
    amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    #get json string using currency response
    str=currency_response(currency_from, currency_to, amount_from)
    #find the returned (right side) value
    rhs=get_rhs(str)
    #strip to find only numerical value
    num=before_space(rhs)
    #convert string into float
    result=float(num)
    return result