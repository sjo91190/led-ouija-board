# Raspberry Pi powered LED Ouija Board

This is a raspberry pi based project to display messages on a Ouija board using LEDs.

(Construction and Pre-Requisite instructions coming soon)

SETUP INSTRUCTIONS:

1. Clone the project to your RPi:

   `git clone https://github.com/sjo91190/led-ouija-board.git`

2. Edit /etc/rc.local on the RPi to configure the GPIO ports:

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
   
   
   