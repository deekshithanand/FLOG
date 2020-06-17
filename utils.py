def validateForm(formData):
    flag = False
    message = ""
    keys = ['uname', 'fname', 'lname', 'pwd', 'email', 'cpwd']
    for key in keys:
        if not formData[key]:
            flag = True
            message = "Some fields are missing!"
            return flag,message

    if(formData['cpwd'] != formData['pwd']):
        flag = True
        message = "Passwords dont match!!!"
    return flag, message
