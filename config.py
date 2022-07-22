import board


## Driver 0
# # Pin for Stepper Drive Pulses
PUL_pin0 = board.IO3
# Pin for Controller Direction Bit
DIR_pin0 = board.IO4
# Pin for Controller Enable Bit
ENA_pin0 = board.IO5

# This is actualy a delay between PUL pulses
# effectively sets the motor rotation speed.
delay0 = 0.0000001

# pause due to a possible change direction
pause0 = .5
##

## Driver 1
# Pin for Stepper Drive Pulses
PUL_pin1 = board.IO39
# Pin for Controller Direction Bit
DIR_pin1 = board.IO40
# Pin for Controller Enable Bit
ENA_pin1 = board.IO41

# This is actualy a delay between PUL pulses
# effectively sets the motor rotation speed.
delay1 = 0.0000001

# pause due to a possible change direction
pause1 = .5
##

# Used for test(). Delete the following if test() not used.
# This is the number of steps that the motor is spinning. 
# Used for forward direction.
stepsFwd = 6400*4
# This is the number of steps that the motor is spinning. 
# Used for reverse direction.
stepsBwd = 6400
# This is the number of cycles to be run once program is started.
cycles = 1000
# This is the iteration of cycles to be run once program is started.
cyclecount = 0


def print_config(pin):
    if pin == 0:
        print('PUL = GPIO {}'.format(PUL_pin0).replace('board.', ''))
        print('DIR = GPIO {}'.format(DIR_pin0).replace('board.', ''))
        print('ENA = GPIO {}'.format(ENA_pin0).replace('board.', ''))
        print('Speed set to ' + str(delay0))
        print('Pause due to a possible change direction set to ' + str(pause0))

        # Used for test(). Delete the following if test() not used.
        print('Duration Fwd set to ' + str(stepsFwd))
        print('Duration Bwd set to ' + str(stepsBwd))
        print('number of Cycles to Run set to ' + str(cycles))
    else:
        print('PUL = GPIO {}'.format(PUL_pin1).replace('board.', ''))
        print('DIR = GPIO {}'.format(DIR_pin1).replace('board.', ''))
        print('ENA = GPIO {}'.format(ENA_pin1).replace('board.', ''))
        print('Speed set to ' + str(delay1))
        print('Pause due to a possible change direction set to ' + str(pause1))

        # Used for test(). Delete the following if test() not used.
        print('Duration Fwd set to ' + str(stepsFwd))
        print('Duration Bwd set to ' + str(stepsBwd))
        print('number of Cycles to Run set to ' + str(cycles))
        
