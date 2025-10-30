4-Day Macropad Journal
---------------------------------------------
Day 1: Idea
I always have to go through many tiny menues at the corner of my screen manually adjusting my monitor's brightness and system volume. I use these functions constantly, and it always takes up too much time. I thought, there must be a better way.

I've been wanting to design something simple but useful with a Raspberry Pi Pico , and this seemed like the perfect project. I want a macropad that gives me control over sound and brightness.

The basic functions I need are:

Volume Up/Down: A satisfying turn of a knob.

Mute/Unmute: Pressing the knob.

Brightness Up/Down: A second knob for this.

Third Programmable function for macros.


Day 2: Components

I decided to make choose some of my components today

Microcontroller: The Raspberry Pi Pico, has plenty of GPIO pins, and is easy to program

Input Controls: I'm going with two Rotary Encoder Buttons. These are perfect as they provide the rotational input for adjustment and the click functionality for muting or resetting.

Visual Feedback: I definitely want a clean, minimalist look, but I need visual feedback. I’ve decided on NeoPixels (SK6812MINI-E LEDs). Crucially, I'm going to use reverse-mounted NeoPixels This will allow the light to act as an indicator of the sound, volume and any other macro.

Day 3: Schematic

nothing much to write about but it took a while had to make sure i had the right resistors and had to find some of the symbols and footprints.

Day 4: PCB creation

I made the pcb today to size and it took a while because kicad doesnt have an easy way to align stuff in an array if its directly from the schematic it took a couple hours but i got it there. I did all the wiring, and then realized i put the neopixels on the wrong side so I had to redo all that work and rewire it but i finally got it to 0 errors.
