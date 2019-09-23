# Subtitle-Shifter

#### A VERY simple .srt subtitle shifter.

You have slightly unsynchronized subtitles? This script may fix your problem!

It was made to easily shift subtitles over time, so it won't disturb your experience while watching movies or series

## Usage:

```
$terminal> python3 subshifter.py Subtitles.srt [delta in millisseconds] [encoding (optional)]
```

## Examples:

Shifting backwards by 1 second:

```
$terminal> python3 subshifter.py BeingJohnMalkovich.srt -1000
```

Shifting forward by 2 seconds:

```
$terminal> python3 subshifter.py TheDarjeelingLimited.srt 2000
```