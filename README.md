# Subtitle-Shifter

#### A VERY simple .srt subtitle shifter.

You have slightly unsynchronized subtitles? This script may fix your problem!


## Usage:

```
$terminal> python3 subshifter Subtitles.srt [delta in millisseconds] [encoding (optional)]
```

## Examples:

Shifting backwards by 1 second:

```
$terminal> python3 subshifter BeingJohnMalkovich.srt -1000
```

Shifting forward by 2 seconds:

```
$terminal> python3 subshifter TheDarjeelingLimited.srt 2000
```