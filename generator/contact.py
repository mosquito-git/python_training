from model.contact import Contact
import random
import string
import os
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# def clear(s):
#     return re.sub("[()\\ -'`]", "", s)


def rand_tel():
    return '+' + str(random.choice(string.digits)) + '(' + "".join(
        random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)) + ')' + "".join(
        random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(
            string.digits)
        + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits))


def rand_year():
    return "".join(
        random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(
            string.digits))


def rand_month():
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
    return random.choice(month_list)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    # return clear(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home="", mobile="", work="", fax="", email="", email2="",
                    email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-",
                    ayear="", address2="", phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
                       lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                       title=random_string("title", 20), company=random_string("company", 20),
                       address=random_string("address", 20), home=random.randrange(1, 9),
                       mobile=rand_tel(), work=rand_tel(),
                       fax=random.randrange(1, 99999), email=random_string("email", 5),
                       email2=random_string("email2", 5), email3=random_string("email3", 5),
                       homepage=random_string("homepage", 20),
                       bday=str(random.randrange(1, 32)),
                       bmonth=rand_month(),
                       byear=rand_year(),
                       aday=str(random.randrange(1, 32)),
                       amonth=rand_month(),
                       ayear=rand_year(),
                       address2=random_string("address2", 20), phone2=random_string("phone2", 20),
                       notes=random_string("notes", 20))
               for i in range(5)
           ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",  f)
# print(file)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))