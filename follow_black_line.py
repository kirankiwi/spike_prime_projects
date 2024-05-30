from hub import light_matrix
import runloop
import motor
from hub import port
import color
import color_sensor

async def main():
    while True:
        if color_sensor.color(port.C) == color.BLACK:
            motor.run_for_degrees(port.A,20,720)
        else:
            if color_sensor.color(port.D) == color.BLACK:
                motor.run_for_degrees(port.B,-20,720)
            else:
                motor.run_for_degrees(port.A,-5,720)
                motor.run_for_degrees(port.B,5,720)
runloop.run(main())