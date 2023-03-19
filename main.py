def on_button_pressed_a():
    if smarthome.read_noise(AnalogPin.P1) > 30:
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        if smarthome.read_noise(AnalogPin.P1) > 40:
            strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
            if smarthome.read_noise(AnalogPin.P1) > 50:
                strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
                if smarthome.read_noise(AnalogPin.P1) > 60:
                    strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
                    if smarthome.read_noise(AnalogPin.P1) > 70:
                        strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
                        if smarthome.read_noise(AnalogPin.P1) > 80:
                            strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
                            if smarthome.read_noise(AnalogPin.P1) > 90:
                                strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
                                if smarthome.read_noise(AnalogPin.P1) > 100:
                                    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
                                    if smarthome.read_noise(AnalogPin.P1) > 110:
                                        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
                                        if smarthome.read_noise(AnalogPin.P1) > 120:
                                            strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
input.on_button_pressed(Button.A, on_button_pressed_a)

lydtyrke = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)

def on_forever():
    global lydtyrke
    basic.show_icon(IconNames.HAPPY)
    lydtyrke = smarthome.read_noise(AnalogPin.P1)
    if lydtyrke > 120:
        strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    elif lydtyrke > 110:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif lydtyrke > 100:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif lydtyrke > 90:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        pass
    elif lydtyrke > 80:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        pass
    elif lydtyrke > 70:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        pass
    elif lydtyrke > 60:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        pass
    elif lydtyrke > 50:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        pass
    elif lydtyrke > 40:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        pass
    else:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        pass
basic.forever(on_forever)
