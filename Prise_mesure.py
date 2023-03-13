
import nidaqmx as ni

## ai0 is the channel number that you want to use to acquire data. Make sure that this is the correct channel name.
## Dev1 is the name of the device connected to the computer.


with ni.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")  
    task.read()
