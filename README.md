# flight-tracker

This program can be used with the command line using the origin code to be put in it will use the Tequila API to search for flights and their prices. It searched the origin to the destinations that are in the google sheet for the cheapest flights from tomorrow to 6 months away. The user can put in the minimum time at the destination and the max and it will return the cheapest flight somewhere within those parameters.

What is used:
- Sheety API (push to the google sheet)
- Google Sheets (store the data)
- Kiwi/Tequila API (for the flight data)
- Twilio (for the sms message)

**Highlights:**
Working with multiple APIs is really cool to see the functions come together and create one thing and something new. I also enjoyed working on OOP and getting the different parts to work without making a huge file. It was good to just try to create something with just the idea kind of flesh out but not the piece by piece tutorial.

**Struggles/Learned:**
I learned to check your spelling multiple times. I was trying to push data to the sheet and it kept giving me a bad request error and I couldn't figure out why. I took a break and came back and it was just missing a letter in the parameters for the sheety request, lol. I was so hurt and confused because I didn't want to max out my usage with one mistake but once I fixed that it was all good.