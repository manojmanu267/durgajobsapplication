# this script also execute in the environment of this project this script also in the scope of django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "durgajobs.settings")
# settings also available to this script also

import django

django.setup()  # you are conveying django please consider this script also part of this project
# first 4 lines if we write means this script is going to be consider under django

from testapp.models import PuneJobs
from faker import Faker
from random import *

fake = Faker()


def phonenumbergen():
    d1 = randint(6, 9)
    num = "" + str(d1)
    for i in range(9):
        num = num + str(randint(0, 9))
    return int(num)


def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.random_element(
            elements=(
                "Prodapt",
                "Amazon",
                "Atlassian",
                "Google",
                "Tcs",
                "Infosys",
                "Accenture",
                "Cognizant",
            )
        )
        ftitle = fake.random_element(
            elements=(
                "Project Manager",
                "Team Lead",
                "Data Scientist",
                "Data Engineer",
                "Test Engineer",
                "Data Analyst",
            )
        )
        feligibility = fake.random_element(
            elements=("B.Tech", "M.Tech", "MCA", "BBA", "P.H.D")
        )
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        Pune_jobs_record = PuneJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )


n = int(input("Enter Number Of Records"))
populate(n)
print(f"{n} records Inserted Successfully")
