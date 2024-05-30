from hub import light_matrix
import runloop
from hub import port, sound
import color
import color_sensor
import motor
async def main():
# The robot has to be on green when this program starts.
    while True:
        if color_sensor.color(port.C) == color.GREEN:
            await motor.run_for_degrees(port.B,50,720)
        else:
            if color_sensor.color(port.D) == color.GREEN:
                await motor.run_for_degrees(port.A,-50,720)
runloop.run(main())