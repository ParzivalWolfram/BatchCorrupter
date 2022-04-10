# BatchCorrupter
This is a script originally made when I was like... 14? I've recently found it and i'm just poking at it,
adding new features or cleaning up some code or making sure the script still works on everything from Python 2.5 to 3.10.
The original purpose of this was to be able to do ROM corruption across an entire folder of ROMs instead of individually, 
so it's not really of much use to anyone but little old me. If you can find one, I'd love to know about it!

This code is bad, but hey, I was 14. Don't get me wrong, my new code is still awful, but i'm very, very slowly improving.


There are switches for this, for various things:

`--log`: Enable logging. This will either create a log at `../corrupter.log` or, alternatively, you can set a specific location via `--log=<path>`. Everything the program normally prints will be mirrored in the log. Log is not overwritten if already present.

`--debug`: Enables basic debug stats, useful for a few things. Also invokable with `-v` and `--verbose`.

`--superdebug`: Enables super verbose debug stats. This probably isn't useful for you unless you're helping me fix the program, and if logging is enabled, it may fill your drive very, very fast. Does not imply `--debug` on its own when called as `--superdebug`, but `-vv` will enable both debug levels, if you REALLY want to have both...

`--ignore-errors`: This will ignore file access errors. Not useful to anyone but me, unless you know EXACTLY what you're doing. Also invokable as `--ignore`.
