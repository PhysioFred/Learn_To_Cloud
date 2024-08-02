# #functions with tuple and dictionary parameters

def student_information(sex, *classes, **details):
    print(f'Gender = {sex}')
    print(classes)
    print(details)

student_information("female", "Biology", "English", name='Jason', height='180cm', blood_type="O+")

print("-------------------------")


def student_information(*classes, **details):

    print(classes) #prints tuple
    print(details) #prints dictionary

sex = 'Gender = female'
course = ('Biology', 'English')
info = {'name': 'Jason', 'height': '180cm', 'blood_type': 'O+'}

student_information(sex, *course, **info)