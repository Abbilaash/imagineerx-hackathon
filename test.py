import pickle
def register_func():
    data = {
            'USERNAME':'abbi',
            'NAME':'Abbilaash A T',
            'PASSWORD':'abbi',
            'AADHAAR':'123456789011',
            'PHONE':'8667093591',
            'GMAIL':"abbilaashat@gmail.com",
            'ACCNO':'CB00975GH46'
    }
    with open("src/auth.bin", "wb") as file:
        pickle.dump(data, file)
    
register_func()
    