## Digital Clock Reflections

This repo contains some code that will generate all of the times on a 24 hour, 7 segment display, digital clock that are also reflectable valid times.

Example:

When 00:05 is reflected, the digits are reversed and flipped. This means the '5' turns into a '2' and the resulting time is 20:00.

Note: Although a '1' is the same when flipped it would appear on the wrong side of the segment display for that digit, hence not resulting in a valid time display.

> ! The valid times and their reflections are as follows:  
> 00:00 -> 00:00  
> 00:05 -> 20:00  
> 00:20 -> 05:00  
> 00:50 -> 02:00  
> 00:55 -> 22:00  
> 02:00 -> 00:50  
> 02:05 -> 20:50  
> 02:20 -> 05:50  
> 02:50 -> 02:50  
> 02:55 -> 22:50  
> 05:00 -> 00:20  
> 05:05 -> 20:20  
> 05:20 -> 05:20  
> 05:50 -> 02:20  
> 05:55 -> 22:20  
> 20:00 -> 00:05  
> 20:05 -> 20:05  
> 20:20 -> 05:05  
> 20:50 -> 02:05  
> 20:55 -> 22:05  
> 22:00 -> 00:55  
> 22:05 -> 20:55  
> 22:20 -> 05:55  
> 22:50 -> 02:55  
> 22:55 -> 22:55
