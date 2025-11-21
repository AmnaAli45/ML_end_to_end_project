import os,sys
from src.logger import logging

def error_message_detailed(error,error_detailed:sys):
    _,_,exc_tb = error_detailed.exc_info()
    # exc_tb tells: 
    # kis line prr error hua
    # kis file mein error hua
    # kon sa code run ho rha tha
    file_name = exc_tb.tb_frame.f_code.co_filename
    # tb_frame = wo frame (code block) jahan error hua.

    #exc_tb.tb_frame.f_code:
    # f_code = us code block ka code object
    # Iske andar details hoti hain jaise:
    # code kis file mein likha hai,function ka naam kya hai,line numbers, etc.

    # co_filename wo file ka naam deta hai jahan error hua.

    error_message = "Error occured in script {0} line no {1} error message {2}".format(
        file_name,exc_tb.tb_lineno, str(error)
    ) # here 0, 1 and 2 are the placeholders that hold the value according to given format.
    return error_message

class CustomException(Exception): # Ye Python ki built-in Exception class ko inherit kar raha hai.
    def __init__(self, error_message,error_detailed:sys):
        super().__init__(error_message) # ye parent class (Exception) ka constructor run karta hai.
        self.error_message = error_message_detailed(error_message,error_detailed=error_detailed)

    def __str__(self): # Jab bhi aap error ko print karo ya log karo, ye method call hota hai.
        return self.error_message

# ---------------------to run code in same file ---------------

# if __name__ == '__main__':
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Division by zero")
#         raise CustomException(e,sys)

# we can run it in app.py file also (best practice)    
