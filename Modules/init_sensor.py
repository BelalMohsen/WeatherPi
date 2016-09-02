#!/usr/bin/python
# -*- coding: utf-8 -*-
from Modules.init_io import *
# from init_logging import *


# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0


def sensor_inside_init():

    try:

        sensor_temp_inside = aio_sensors.receive('sensortempinside')
        sensor_temp_inside = float(sensor_temp_inside.value)

        sensor_pressure_inside = aio_sensors.receive('sensorpressureoutside')
        sensor_pressure_inside = float(sensor_pressure_inside.value)

        sensor_humidity_inside = aio_sensors.receive('sensorhumidityoutside')
        sensor_humidity_inside = float(sensor_humidity_inside.value)

        log_string = 'Temperature Inside        :   {0:0.3f}°C / {1:0.3F}°F'.format(sensor_temp_inside,
                                                                               c_to_f(sensor_temp_inside))

        print(log_string)
        debug_logger.debug(log_string)

        log_string = 'Sensor Pressure Inside    :   {0:0.2f} hPa'.format(sensor_pressure_inside)

        print(log_string)
        debug_logger.debug(log_string)

        log_string = 'Sensor Humidity Inside    :   {0:0.2f} %'.format(sensor_humidity_inside)

        print(log_string)
        debug_logger.debug(log_string)

    except IOError:

        log_string = 'ERROR - sensor_inside_init'

        print(log_string)
        debug_logger.debug(log_string)


def sensor_outside_init():

    try:

        sensor_temp_outside = aio_sensors.receive('sensortempoutside')
        sensor_temp_outside = float(sensor_temp_outside.value)

        sensor_pressure_outside = aio_sensors.receive('sensorpressureoutside')
        sensor_pressure_outside = float(sensor_pressure_outside.value)

        sensor_humidity_outside = aio_sensors.receive('sensorhumidityoutside')
        sensor_humidity_outside = float(sensor_humidity_outside.value)

        log_string = 'Temperature Outside       :   {0:0.3f}°C / {1:0.3F}°F'.format(sensor_temp_outside, c_to_f(sensor_temp_outside))

        print(log_string)
        debug_logger.debug(log_string)

        log_string = 'Sensor Pressure Outside   :   {0:0.2f} hPa'.format(sensor_pressure_outside)

        print(log_string)
        debug_logger.debug(log_string)

        log_string = 'Sensor Humidity Outside   :   {0:0.2f} %'.format(sensor_humidity_outside)

        print(log_string)
        debug_logger.debug(log_string)

    except IOError:

        log_string = 'ERROR - sensor_outside_init'

        print(log_string)
        debug_logger.debug(log_string)

if __name__ == '__main__':

    try:

        sensor_inside_init()
        sensor_outside_init()

    except KeyboardInterrupt:
        from clear import *
        clear_all()
