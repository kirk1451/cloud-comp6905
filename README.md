# cloud-comp6905
assignment 3

To generate request,  I have created 2 Vm's (A1)that produce more than 3000 request/ minute using the Sender.py script. This is equivalent to 360000+ requests pre hour.

Using a scaling VM with min 1 and max 4, starting at 1. The scaleset implements the shell script that downloads all the necessary extensions needed to run the python file Receiver.py.
If there was a double load, the scale set will increase to a maximum of 4 ( limit of azure trial) and continue clearing the queue as much as it can.

The cost of the scale set is equivelent to the cost of all the resources in the set. Which involves using premade resource groups used by the Receiver and Sender files.
4 X A1 (at max ) (including addons such as networking and load balcing) = $9.00/ month (approx)
storage = 1TB (queues and tables) = 71.68/month to  be increased accordingly. total (approx) $80.00/month

