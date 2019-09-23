# Subtitle-Shifter
You have slightly unsynchronized subtitles issue? This may fix your problem.
This is a VERY simple .srt subtitle shifter.


## Usage:

```
$terminal> python3 subshifter Subtitles.srt [delta in millisseconds] [encoding (optional)]
```

## Examples:

Shifting backwards 1 second:

```
$terminal> python3 subshifter BeingJohnMalkovich.srt -1000
```

Shifting forward 2 seconds:

```
$terminal> python3 subshifter TheDarjeelingLimited.srt 2000
```