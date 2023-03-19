let lydtyrke = 0
let strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
basic.forever(function () {
    basic.showIcon(IconNames.Happy)
    lydtyrke = smarthome.ReadNoise(AnalogPin.P1)
    if (lydtyrke > 120) {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
    } else if (lydtyrke > 110) {
        strip.showColor(neopixel.colors(NeoPixelColors.Orange))
    } else if (lydtyrke > 100) {
        strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
    } else if (lydtyrke > 90) {
        strip.showColor(neopixel.colors(NeoPixelColors.Purple))
    } else if (lydtyrke > 80) {
        strip.showColor(neopixel.colors(NeoPixelColors.Violet))
    } else if (lydtyrke > 70) {
        strip.showColor(neopixel.colors(NeoPixelColors.Indigo))
    } else if (lydtyrke > 60) {
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (lydtyrke > 50) {
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
    } else if (lydtyrke > 40) {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
    } else {
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
    }
})
