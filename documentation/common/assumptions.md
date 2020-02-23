# Assumptions 

We split our assumptions by group member but you can consider this file to be the union of all our assumptions.

### James' assumptions

* Some assumptions about tokens:   
    * The user will not always give a valid token, and it should be validated  
* Some assumptions about errors within the program:  
    * When exceptions are rasied by our functions, we are assuming that they will be handled by the driving function accordingly and give the user a response that suits the error raised.  
    * We will not have to account for any other errors to raise other then the ones given to us to raise by the program  
* Assumptions about messages:  
    * Messages are sent in the order they are sent, unless specified otherwise with a function such as send later  
    * When two people use the function send later at the same time and designate the same sending time and channel, the order they arrive in doesn't matter  
    * When editing text, the edits will be based off the passed message to the function, and will hence not be based off the original message  
    * Any user can react to messages that they are authorized in the channel of  
    * Each message can have any number of different reactions, but each message can only have any reaction a maximum of once from any user  
    * Only admins can "pin" and "unpin" messages  
    * Any user can remove their own message, admins can remove any message  
    * Only a user can edit their own message, admins cannot edit other peoples messages  
    * If a user cannot edit a message, an access error should be raised  
    * When a message is edited, the new message cannot exceed the limit of 1000 characters  
    * When a message is sent during a standup, it will go to the standup queue  
    * If a message is sent to an incorrect channel id, we will return a value error
    
### Mitchell's assumptions

* Some assumptions about channel_* modules:
    * Authorized member is stored by reference with the token.
    * We control every aspect of the token, channel id assignment and storage etc.
* Some assumptions about channel_invite function:
    * The user is added regardless of access setting.
* Some assumptions about channel_join function:
    * The user can only 'join' public channels
* Some assumptions about channel_addowner function:
    * There can be an indefinite number of owner:
* Some assumptions about channels_listall function:
    * Lists both public and private channels
* Some assumptions about channels_list, channels_listall function:
    * Returns same details as described in channel_details

### Miranda's assumptions
* Overall assumptions:
    * Indefinite number of users can register/login, provided the emails are always different


* Assumptions for auth_login:
    * The validity of the email will be determined by a helper function, specifications about what make it valid hopefully to be released in iteration 2
    * The correct password is known when given a valid email, will then be compared to the entered password
    * When email is entered, it is searched up in a database -- if email is not in database, then no user is linked to the email

* Assumptions for auth_logout:
    * auth_login will always return a valid token
    * The token to logout will be different to the token returned by auth_login
    * Currently auth_logout does not return anything, I've assumed that in later iterations it might return the changed token (may make testing this function easier)

* Assumptions for auth_register:
    * When auth_register is implemented, the details entered by user will be stored onto a database so that when it is called again, it will search the database for matching emails to check if it has already been used
    * Validity of password will be determined by a helper function, specifications about what make it valid hopefully to be released in iteration 2

* Assumptions for auth_password_request:
    * Invalid email also emcompasses an email not linked with a user

* Assumptions for auth_passwordreset_reset:
    * 1234567890 is an invalid code
    * Code is valid when it matches the one sent by email to user when auth_register function is implemented
    * auth_register function will provide a code

* Assumptions for standup_start:
    * Any user who has created the channel can create a standup
    * Any user who has joined, or been invited to the channel can create a standup

* Assumptions for standup_send:
    * Any user who has created the channel can send a message during the standup
    * Any user who has join, or been invited to the channel can send a message during the standup