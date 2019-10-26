# Raspberry Pi powered LED Ouija Board

This is a raspberry pi based project to display messages on a Ouija board using LEDs.

(Construction Instructions Coming Soon)

REQUIRED TOOLS:

   - Electric Drill
   - 4mm or 5/32in Drill Bit

REQUIRED MATERIALS:

   - [Raspberry Pi](https://www.amazon.com/CanaKit-Raspberry-Basic-Starter-Official/dp/B07TTPK42Z/)
   - [Ouija Board](https://www.amazon.com/gp/product/B00EFDXAB4/)
   - [Micro SD Card](https://www.amazon.com/gp/product/B073K14CVB/)
   - [Raspberry Pi GPIO Breakout Module](https://www.amazon.com/CanaKit-Raspberry-Breakout-40-Pin-T-Shaped/dp/B011CZ2LEY/)
   - [Solderless Breadboard](https://www.amazon.com/EL-CP-003-Breadboard-Solderless-Distribution-Connecting/dp/B01EV6LJ7G/)
   - [Male to Female Jumpers](https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD1D64V/)
   - [Yellow LEDs](https://www.amazon.com/gp/product/B01GDZVTFA/)
   - [3mm LED Holders](https://www.amazon.com/gp/product/B01E3FY6ZC/)
   - [Heatshrink Tubing](https://www.amazon.com/560PCS-Heat-Shrink-Tubing-Eventronic/dp/B072PCQ2LW/)
   - [Ethernet Cable](https://www.amazon.com/AmazonBasics-RJ45-Cat-6-Ethernet-Patch-Cable-5-Feet-1-5-Meters/dp/B00N2VILDM/ref=sxin_2_pb?keywords=ethernet+cable&pd_rd_i=B00N2VILDM&pd_rd_r=1f8cd961-c503-4cf3-9ec1-84dd14edf8c8&pd_rd_w=cSP3p&pd_rd_wg=Drr1H&pf_rd_p=50bbfd25-5ef7-41a2-86d6-74d854b30e30&pf_rd_r=1NGEKVWB7MHDXKG3T8QV&qid=1572124690)

RESOURCES:

   - [Raspbian Images](https://www.raspberrypi.org/downloads/raspbian/)
   - [Raspberry Pi GPIO Pinout Diagram](https://www.raspberrypi.org/documentation/usage/gpio/)

PREREQUISITES:

1. Installed Raspbian image on the MicroSD Card (See Resources for Image)

   - [Instructions for installing an image](https://www.raspberrypi.org/documentation/installation/installing-images/)

2. SSH enabled on the clean image

   - [Instructions for enabling SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)
     
     -Follow the guide on Option 3
   

CONSTRUCTION:


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













