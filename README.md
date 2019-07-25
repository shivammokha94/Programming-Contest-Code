# Programming-Contest-Python-Code

This code is built for stage 2 of the contest which needs a use of a live message communication service via Twilio and ngrok to tunnel localhost.

The code consists of the following modules:

1.	utility.py which contains all necessary data creation functions.
2.	main_func.py (Run this file) which contains all the function calls.
3.	smsauth.py contains a simple chatbot which sends an SMS to the user for verification and follow up sequence. Note: The module requires twilio library installed.
4.	microservice.py – Flask application (Run simultaneously, before running main_func.py) is a microservice which is required to get messages from the user texts. Note: The module requires twilio and flask libraries installed.

The code can perform the following tasks,
1.	Create a username and form.
2.	If a username exists, ability to edit form details.
3.	Option to opt in to the message service.
4.	Verify the phone number for the user.
5.	Send and receive text message on user phone.
6.	Create a follow up sequence (1, 2 or 3) and send it to the user phone. Follow up sequence is currently assigned randomly.
7.	Ability to opt out of message service.
8.	Create a final dataset with category variables and save it in code directory.

  	How to run:

1.	Firstly, to run SMS service, i.e. send and receive SMS, we would require a Twilio account to access its API services.  . 
2.	After registering with Twilio, API key and AUTH_TOKEN is provided to us, which would be used in smsauth.py. 
3.	Once the authentication key and token are set (already set for the demo), we run the microservice.py file and keep it running in the background. When a phone number send out a message back to our Twilio phone number (automated phone number), it sends out an http response to a mentioned URL. Thus, this file is needed to run before running the main code. 
4.	Once the file is running, to proxy my localhost as a live website and in order to receive text messages, we need to run ngrok application (https://ngrok.com/). Save the ngrok application to the folder where the code lives and run the ngrok code.
Since our localhost would be running on port 5000, we use 5000 as tunnel proxy.
5.	Use this forwarding DNS address and set this up in your Twilio account.
6.	Once this is done, microservice.py is ready to be run.
7.	Once the program is running, it created a CSV in the code directory as ‘auth.csv’. This is needed to verify the number.


Program execution:

Running main_func.py provides the following option:
When the user selects option 1, he is prompted to enter username. If the username does not exist, he is prompted to fill up the form.

The program has the ability to handle invalid values. Once, the details are filled, they are loaded to user.csv and data.csv files. He is then returned back to the main menu. User has the ability to change the details and these are reflected back to the data.csv file in real time.
Once the user selects the option to opt in to message service, he is sent a text message with a verification code, prompted on the screed. The message id ensures the message is sent to the user. Once the user sends the verification response back, the response data is stored in auth.csv file.The user is also prompted to press Enter on screen once he sends the code, in order to check the auth.csv for the code. If the user responses with a wrong message, he is prompted to re-send the code. 
The code also has the ability to consider only the two latest verification codes for each number. Once the user responds with the right verification code and after he continues to the next screen, he is sent a follow up sequence code which is currently generated randomly. This sequence is stored in data.csv file.If the user wishes to opt out, he can do on the edit screen and the opt_in and follow up details are reset. Finally, to get all category variables, the final dataset can be saved.

To exit program, use option 3 from the main menu.

 
