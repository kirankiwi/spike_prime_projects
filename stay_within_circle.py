from hub import light_matrix
import color
import color_sensor
import runloop
import motor
from hub import port

mat_colour = color.WHITE
motor_velocity = 660
motor_degrees = 5

async def main():
    while True:
        if color_sensor.color(port.C) == mat_colour:
            motor.run_for_degrees(port.A,-motor_degrees,motor_velocity)
            motor.run_for_degrees(port.B, motor_degrees,motor_velocity)
        else:
            motor.run_for_degrees(port.A,180,360)
            await motor.run_for_degrees(port.B,-180,360)
            motor.run_for_degrees(port.A,180,360)
            await motor.run_for_degrees(port.B,180,360)
runloop.run(main())
