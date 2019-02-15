#Math functions

import math

end='\n\n';
signal_power=10;
noise_power=5;

ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels, end=end);

radians = 0.7
height = math.sin(radians)
print(height, end=end)

sqrt4 = math.sqrt(4)
print(sqrt4)
