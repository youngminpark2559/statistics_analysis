xkbcommon: ERROR: failed to add default include path 
Qt: Failed to create XKB context!
Use QT_XKB_CONFIG_ROOT environmental variable to provide an additional search path, add ':' as separator to provide several search paths and/or make sure that XKB configuration data directory contains recent enough contents, to update please see http://cgit.freedesktop.org/xkeyboard-config/ .
Traceback (most recent call last):
  File "main.py", line 141, in <module>
    plt.xticks("afaf")
  File "/home/young/anaconda3/envs/py36gputorch100/lib/python3.6/site-packages/matplotlib/pyplot.py", line 1549, in xticks
    locs = ax.set_xticks(ticks)
  File "/home/young/anaconda3/envs/py36gputorch100/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 3337, in set_xticks
    ret = self.xaxis.set_ticks(ticks, minor=minor)
  File "/home/young/anaconda3/envs/py36gputorch100/lib/python3.6/site-packages/matplotlib/axis.py", line 1704, in set_ticks
    ticks = self.convert_units(ticks)
  File "/home/young/anaconda3/envs/py36gputorch100/lib/python3.6/site-packages/matplotlib/axis.py", line 1530, in convert_units
    ret = self.converter.convert(x, self.units, self)
  File "/home/young/anaconda3/envs/py36gputorch100/lib/python3.6/site-packages/matplotlib/category.py", line 53, in convert
    unit.update(values)
AttributeError: 'NoneType' object has no attribute 'update'
