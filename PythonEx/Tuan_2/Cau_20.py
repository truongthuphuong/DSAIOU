str_input=input()
spend_account=0
while str_input:
    str_input=str_input.split(' ')
    if str_input[0] == 'D':
        spend_account += int(str_input[1])
    elif str_input[0] == 'W':
        spend_account -= int(str_input[1])
        if spend_account<0:
            spend_account=0
    
    str_input=input()
print(spend_account)