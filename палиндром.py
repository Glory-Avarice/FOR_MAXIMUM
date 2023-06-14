def palindrom(slovo):
    if slovo == slovo[::-1]:
        print('True')
    else:
        print('False')

palindrom('лепсспел')

palindrom('helloworld')