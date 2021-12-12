import re



def check_country_code(num):
    country_codes = {'India':'91', 'USA':'1', 'UAE':'971', 'UK':'44'}
    
    if(num[0:2] == country_codes['India']):
        return True
    elif(num[0:1] == country_codes['USA']):
        return True
    elif(num[0:3] == country_codes['UAE']):
        return True
    elif(num[0:2] == country_codes['UK']):
        return True
    else:
        return False
    
def check_phone(num):
    num1 = ""
    #removing special characters in the phone number
    for i in num:
        if(i.isdigit() == True):
            num1 = num1 + i
    print(num1)
    
    if((len(num1) > 10) and (len(num1) < 13)):
        if(check_country_code(num1)):
            return "+" + num1
        else:
            print("Invalid Country code")
            return None
    elif((len(num1) >= 13) or (len(num1) < 10)):
        print("Invalid Country code")
        return None
    else:
        return '+91' + num1


def check_email(email):
    email=email.strip()
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(email_regex, email)):
        return email
    else:
        return None

