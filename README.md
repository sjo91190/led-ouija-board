# Raspberry Pi powered LED Ouija Board

This is a raspberry pi based project to display messages on a Ouija board using LEDs.

(Construction Instructions Coming Soon)

REQUIRED TOOLS:

   - Electric Drill
   - 4mm or 5/32in Drill Bit
   - Lighter
   - Double-sided foam tape

REQUIRED MATERIALS:

   - [Raspberry Pi](https://www.amazon.com/CanaKit-Raspberry-Basic-Starter-Official/dp/B07TTPK42Z/)
   - [Ouija Board](https://www.amazon.com/gp/product/B00EFDXAB4/)
   - [Micro SD Card](https://www.amazon.com/gp/product/B073K14CVB/)
   - [Raspberry Pi GPIO Breakout Module](https://www.amazon.com/CanaKit-Raspberry-Breakout-40-Pin-T-Shaped/dp/B011CZ2LEY/)
   - [Solderless Breadboard](https://www.amazon.com/EL-CP-003-Breadboard-Solderless-Distribution-Connecting/dp/B01EV6LJ7G/)
   - [Male to Female Jumpers](https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD1D64V/)
   - [470 Ohm Resistors](https://www.amazon.com/EDGELEC-Resistor-Tolerance-Multiple-Resistance/dp/B07QG1V4BH/)
   - [Yellow LEDs](https://www.amazon.com/gp/product/B01GDZVTFA/)
   - [3mm LED Holders](https://www.amazon.com/gp/product/B01E3FY6ZC/)
   - [Heatshrink Tubing](https://www.amazon.com/560PCS-Heat-Shrink-Tubing-Eventronic/dp/B072PCQ2LW/)
   - [Ethernet Cable](https://www.amazon.com/AmazonBasics-RJ45-Cat-6-Ethernet-Patch-Cable-5-Feet-1-5-Meters/dp/B00N2VILDM/ref=sxin_2_pb?keywords=ethernet+cable&pd_rd_i=B00N2VILDM&pd_rd_r=1f8cd961-c503-4cf3-9ec1-84dd14edf8c8&pd_rd_w=cSP3p&pd_rd_wg=Drr1H&pf_rd_p=50bbfd25-5ef7-41a2-86d6-74d854b30e30&pf_rd_r=1NGEKVWB7MHDXKG3T8QV&qid=1572124690)

RESOURCES:

   - [Raspbian Images](https://www.raspberrypi.org/downloads/raspbian/)
   - [Raspberry Pi GPIO Pinout Diagram](https://www.raspberrypi.org/documentation/usage/gpio/)
   - [LED Anode/Cathode Diagram](https://www.build-electronic-circuits.com/wp-content/uploads/2014/05/LED-anatomy-1024x455.png)

PREREQUISITES:

1. Installed Raspbian image on the MicroSD Card (See Resources for Image)

   - [Instructions for installing an image](https://www.raspberrypi.org/documentation/installation/installing-images/)

2. SSH enabled on the clean image

   - [Instructions for enabling SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)
     
     - Follow the guide on Option 3
   

CONSTRUCTION:
1. Drill holes through the middle of letters. The back may peel apart at drill sites so be careful. 
If it does peel a little bit, it is not a big deal.
2. Wire up the LEDs

   - Be familiar with anode/cathode (+/-) on the LED. See LED Diagram in Resources section
   - Use warm color jumper wires when connecting to the anode (+) and dull colors when connecting to the cathode (-) 
   so you don't get them mixed up.
   - When the jumper cables are connected to the LED, slip a piece of heat shrink tubing over each of the 
   jumper leads up to the connection to the LED. Use a size that is nice and snug.
   - Apply a heat source (lighter is OK) briefly to the heat shrink tubing until it is tight against the leads
   - Slip a piece of heat shrink tubing over both of the jumper leads (Use appropriate size), all the way up to the LED 
   (but not covering the LED, obviously).
   - Apply heat source to the heat shrink tubing until it is tight and holding both leads together
   - Repeat 26 times, one for each letter - Or extra if you think you will need them.
3. Pop the LED holders into the Ouija board from the front
4. Push the LEDs into the LED holders from the inside
5. Mount the breadboard and the Raspberry Pi and make connections between the two
   - Mount the breadboard to the bottom of the Ouija board. Breadboard has adhesive on the back.
   - Connect the Raspberry Pi GPIO breakout board to the breadboard and to the Raspberry Pi.
   - Once you have an idea of where to place the Raspberry Pi, mount the bottom of the case to the Ouija board using the 
   double-sided foam tape and insert the Raspberry Pi into the case.
   - Be sure to leave space for ease of access to the power connection on the Raspberry Pi.
6. Begin wiring the project. [Wiring Diagram](https://github.com/sjo91190/led-ouija-board/blob/master/OuijaBoardWiring.pdf)
    - Insert the 470 ohm resistors down the middle of the breadboard, starting at one side
    - Begin wiring the GPIO pins from the GPIO breakout board to one side of the resistors
    - Begin wiring the LEDs to the other side of the resistors
7. Find a nice shadow box to contain the project!
   
SETUP INSTRUCTIONS:

1. Insert the MicroSD Card into the Raspberry Pi

2. Power on the Raspberry Pi and connect it to a LAN port on a wireless router via Ethernet cable

3. Connect to the Raspberry Pi via SSH from a computer

   - `ssh pi@raspberrypi`
   - You will likely get a warning saying the host isn't recognized, just type yes to continue
   - This command will only work on Mac and Linux. For Windows you will need to download an SSH client.
      - PuTTY is recommended for Windows
   - Default Password: `raspberry`
4. (Optional, but recommended) Use command `passwd` to change the default password
5. (Optional) Change the network hostname to `ouijaboard` via `raspi-config`

   - Run command: `sudo raspi-config`
   - Use arrows to navigate to option 2: `Network Options` and select
   - Select option N1 and follow the instructions to change the hostname
   - You will be prompted to reboot, accept the reboot
   - When logging in now, you will need to run: `ssh pi@ouijaboard`
   
6. Connect the Raspberry Pi to your wifi network

   - Run command `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
   - At the bottom of the file, add:
      ```
      network={
           ssid="YourWifiSSID"
           psk="YourWifiPASSWORD"
      }
      ```
2. Clone the project to your RPi:

   `git clone https://github.com/sjo91190/led-ouija-board.git`

3. Edit /etc/rc.local on the RPi to configure the GPIO ports:

    `sudo nano /etc/rc.local`
   
      Should look something like this:

      ```
   _IP=$(hostname -I) || true
      if [ "$_IP" ]; then
        printf "My IP address is %s\n" "$_IP"
      fi

      exit 0 
      ```
      Add in the line `sudo /usr/bin/python3 /home/pi/led-ouija-board/gpioSET.py &` between `fi` and `exit 0`
      
      ```
   _IP=$(hostname -I) || true
     if [ "$_IP" ]; then
       printf "My IP address is %s\n" "$_IP"
     fi
      
     sudo /usr/bin/python3 /home/pi/led-ouija-board/gpioSET.py &
      
     exit 0 
     ```    
   
   `ctrl+o` to save and `ctrl-x` to exit the file
   
3. Create a cronjob to auto-run at reboot

   `sudo crontab -e`
   
   If this is your first time using cron on the RPi, you will be asked to configure cron. Simply choose the recommended option when you're prompted
   
   Once you are in the crontab file, insert below the #'s:
   
   `@reboot sudo /usr/bin/python3 /home/pi/led-ouija-board/ouija.py`
   
   `ctrl+o` to save and `ctrl+x` to exit the crontab

4. Reboot the RPi

   `sudo reboot now`
   
   When the RPi boots, you should see all the letters cycle and flash twice
   
5. After the Pi boots, reconnect via SSH. Once connected, enter the command

   `python3 /home/pi/led-ouija-board/ouijaBoard.py`
   
   You will be prompted to `Enter Phrase: `
   
   Type in your message and hit enter, and you will begin to see the Ouija board spell out your message
   
   Note that only upper and lower case letters will show. Else, you will have a 1 second delay before the letters after the non-letter characters display
   
   The space character will also count as a 1 second delay
   

Self hosted local web-server and web gui coming soon













