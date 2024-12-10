import random


def speedometer(low_bound: int = 0, high_bound: int = 40):
    return random.randrange(low_bound, high_bound)


def vehicle_speed():
    speed = speedometer()
    if speed <= 30:
        return 'lowspeed'
    elif speed <= 60:
        return 'normal'
    elif speed <= 90:
        return 'overspeed'
    return "towed"
