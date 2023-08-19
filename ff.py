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
from expencion import rasxodnye_materialy
from expencion import akcii_dict
# from name import list_name
from expencion import list_img
import json

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
        cursor.execute("SELECT id, create_date from salon")
        salon_data = cursor.fetchall()
        list_id_from_salon = []
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