from car import Car
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


def create_calliope(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
    car_calliope = Calliope(last_service_date, current_mileage, last_service_mileage)
    return car_calliope

def create_glissade(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
    car_glissade = Glissade(last_service_date, current_mileage, last_service_mileage)
    return car_glissade

def create_palindrome(current_date, last_service_date, warning_light_on: bool):
    car_palindrome = Palindrome(last_service_date, warning_light_on)
    return car_palindrome

def create_rorschach(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
    car_rorschach = Rorschach(last_service_date, current_mileage, last_service_mileage)
    return car_rorschach

def create_thovex(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
    car_thovex = Thovex(last_service_date, current_mileage, last_service_mileage)
    return car_thovex