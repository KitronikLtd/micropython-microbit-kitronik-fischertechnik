# micropython-microbit-kitronik-fischertechnik
Example code for use with the Kitronik Interface for Fischertechnik board ( www.kitronik.co.uk/5656 )

## Operation

This package contains a function to drive motors:
```blocks
    kiff.motorOn(kiff, "Motor1", "forward", 100)
```

This package contains a function to stop drive:
```blocks
    kiff.motorOff(kiff, "Motor1")
```

This package contains a function to read NTC resistor:
```blocks
    display.show(kiff.ntc(kiff,"P0"))
```

This package contains a function to read phototransistor voltage:
```blocks
    display.show(kiff.phototransistor(kiff,"P0"))
```

This package contains a function to turn on LED:
```blocks
    display.show(kiff.led(kiff,"P0", "on"))
```

## License

MIT

## Supported Targets

BBC micro:bit