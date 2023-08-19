import psycopg2
from config import host, user, password, db_name, port
from psycopg2 import Error
from datetime import datetime, timedelta
import random
from datetime import time

from expencion import list_address
from expencion import generate_random_phone_number
from expencion import generate_random_date
from expencion import list_job_tittle
from expencion import generate_random_email
from expencion import list_img
from expencion import rasxodnye_materialy
from expencion import akcii_dict
from name import list_name
import json


list_create_date_salon = []
min_salary = 30000
max_salary = 80000
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        for _ in range(5):
            insert_query = """ INSERT INTO salon(create_date, address, phone)
                                     VALUES (%s, %s, %s)"""
            lower_date_boundary = generate_random_date(datetime(2016, 12, 14))
            random_address = random.choice(list_address)
            random_phone_number = generate_random_phone_number()
            item_tuple = (lower_date_boundary, random_address, random_phone_number)
            cursor.execute(insert_query, item_tuple)

            for x in range(2):
                insert_masters_query = """INSERT INTO masters(create_date, date_of_birth, name, phone, email, job_title, salon_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                random_number = random.randint(1, 5)
                random_date_of_birth = generate_random_date(
                    lower_date_boundary)
                random_name = random.choice(list_name[0].split('\n'))
                random_email = generate_random_email()
                random_phone_number = generate_random_phone_number()
                cursor.execute(insert_masters_query, (
                    generate_random_date(random_date_of_birth), random_date_of_birth, random_name, random_phone_number,
                    random_email,
                    random.choice(list_job_tittle), random_number))

        cursor.execute("SELECT id, create_date from masters")
        masters_data = cursor.fetchall()
        list_masters_id = []
        list_create_date_clients = []

        for x in range(2):
            for item in masters_data:
                masters_id = item[0]
                list_masters_id.append(masters_id)
                create_date = item[1]

                random_hour = random.randint(9, 21)
                random_minute = random.randint(0, 59)
                create_datetime = datetime.combine(create_date, time(random_hour, random_minute))

                insert_clients_query = """INSERT INTO clients(create_date, name, phone, email, masters_id)
                                                        VALUES (%s, %s, %s, %s, %s)"""
                random_email = generate_random_email()
                random_phone_number = generate_random_phone_number()
                random_name = random.choice(list_name[0].split('\n'))
                cursor.execute(insert_clients_query,
                               (create_datetime, random_name,
                                random_phone_number, random_email, random.choice(list_masters_id)))

        cursor.execute("SELECT masters_id, create_date from clients")
        clients_data = cursor.fetchall()
        list_masters_from_clients_id = []

        for item in clients_data:
            masters_id_from_clients = item[0]
            list_masters_from_clients_id.append(masters_id_from_clients)
            create_date = item[1]

        insert_shedule_query = """INSERT INTO shedule(day, hours_worked, masters_id)
                                                                VALUES (%s, %s, %s)"""
        random_hour_work = random.randint(3, 12)
        cursor.execute(insert_shedule_query,
                       (create_date, random_hour_work, random.choice(list_masters_from_clients_id)))

        for item in masters_data:
            masters_id_for_portfolio = item[0]
            create_date = item[1]

            insert_portfolio_query = """INSERT INTO masters_portfolio(create_date, url, masters)
                                    VALUES (%s, %s, %s)"""
            cursor.execute(insert_portfolio_query,
                           (create_date, random.randint(min_salary, max_salary), masters_id_for_portfolio))

        cursor.execute("SELECT create_date from salon")
        salon_data1 = cursor.fetchall()

        with open("servises.txt", "r", encoding="utf-8") as file:
            data = file.read()

            data_dict = json.loads(data)

            for item, price in data_dict.items():
                insert_services_query = """INSERT INTO services(create_date, name, price)
                                                VALUES (%s, %s, %s)"""
                cursor.execute(insert_services_query,
                               (random.choice(salon_data1), item, price))


        cursor.execute("SELECT id, create_date from salon")
        salon_data = cursor.fetchall()
        list_id_from_salon = []

        for item in salon_data:
            for material in rasxodnye_materialy:
                salon_id_from_salon = item[0]
                list_id_from_salon.append(salon_id_from_salon)
                create_date = item[1]

                insert_shedule_query = """INSERT INTO finances(create_date, name, count, salon_id)
                                                                                VALUES (%s, %s, %s, %s)"""
                cursor.execute(insert_shedule_query,
                               (create_date, random.choice(rasxodnye_materialy), random.randint(1, 1000),
                                random.choice(list_id_from_salon)))

        for item in salon_data:
            for name, descr in akcii_dict.items():
                salon_id_from_salon = item[0]
                list_id_from_salon.append(salon_id_from_salon)
                d = generate_random_date(datetime(2016, 12, 14))
                insert_shedule_query = """INSERT INTO promotion(create_date, delete_date, name, description, salon_id)
                                        VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(insert_shedule_query,
                               (d, generate_random_date(d), name, descr,
                                random.choice(list_id_from_salon)))



except (Exception, Error) as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")