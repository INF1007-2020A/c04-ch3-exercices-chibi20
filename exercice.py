#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    b = math.sqrt(a)
    return b


def square(a: float) -> float:
    b = a**2
    return b


def average(a: float, b: float, c: float) -> float:
    moyenne = (a+b+c)/3
    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    décimal = angle_degs+(angle_mins+angle_secs/60)/60
    rad = décimal*math.pi/180
    return rad


def to_degrees(angle_rads: float) -> tuple:
    angle = angle_rads*(180/math.pi)
    angle_degré = angle%60
    angle_minute = (angle-angle_degré)%60
    angle_seconde = (angle_degré-angle_minute
    return angle_degré, 0.0, 0.0


def to_celsius(temperature: float) -> float:
    temperature_C = (temperature-32)/1.8
    return temperature_C


def to_farenheit(temperature: float) -> float:
    temperature_F = temperature*1.8+32
    return temperature_F


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
