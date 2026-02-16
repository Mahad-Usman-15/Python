def statuscode(statuscode):
    match statuscode:
        case 404:
            print("Not Found")
        case 200:
            print("Success")
        case 500:
            print("Internal Server Error")
        case 503:
            print("Service Not Available")    
statuscode(200)             