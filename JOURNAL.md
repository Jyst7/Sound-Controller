4-Day Macropad Journal - 11h
---------------------------------------------
Day 1: Idea 1h
I always have to go through many tiny menues at the corner of my screen manually adjusting my monitor's brightness and system volume. I use these functions constantly, and it always takes up too much time. I thought, there must be a better way.

I've been wanting to design something simple but useful with a Raspberry Pi Pico , and this seemed like the perfect project. I want a macropad that gives me control over sound and brightness.

The basic functions I need are:

Volume Up/Down: A satisfying turn of a knob.

Mute/Unmute: Pressing the knob.

Brightness Up/Down: A second knob for this.

Third Programmable function for macros.


Day 2: Components 2h

I decided to make choose some of my components today

Microcontroller: The Raspberry Pi Pico, has plenty of GPIO pins, and is easy to program

Input Controls: I'm going with two Rotary Encoder Buttons. These are perfect as they provide the rotational input for adjustment and the click functionality for muting or resetting.

Visual Feedback: I definitely want a clean, minimalist look, but I need visual feedback. I’ve decided on NeoPixels (SK6812MINI-E LEDs). Crucially, I'm going to use reverse-mounted NeoPixels This will allow the light to act as an indicator of the sound, volume and any other macro.

Day 3: Schematic 4h

nothing much to write about but it took a while had to make sure i had the right resistors and had to find some of the symbols and footprints.

<img width="533" height="282" alt="Screenshot 2025-10-29 at 8 24 33 PM" src="https://github.com/user-attachments/assets/c8ff1ba7-8a63-4f7c-b03a-7c46904a8b7b" />

Day 4: PCB creation 4h

I made the pcb today to size and it took a while because kicad doesnt have an easy way to align stuff in an array if its directly from the schematic it took a couple hours but i got it there. I did all the wiring, and then realized i put the neopixels on the wrong side so I had to redo all that work and rewire it but i finally got it to 0 errors.

<img width="417" height="472" alt="Screenshot 2025-10-29 at 8 24 17 PM" src="https://github.com/user-attachments/assets/53566abb-29f8-4ac2-a004-59b52eda5902" />

<img width="534" height="619" alt="Screenshot 2025-10-29 at 8 22 21 PM" src="https://github.com/user-attachments/assets/2fa051d8-565a-411e-bdae-7fb6f01d5574" />
