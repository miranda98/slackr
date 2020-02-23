## Software Engineering Principles: Code Refactoring

During iteration 3, our team was tasked with refactoring our code from iteration 2 while integrating new aspects of the backend that were added in iteration 3. During this iteration, the team refactored code by *addressing one type of code smell at a time* and made appropriate edits to improve maintainability in our code. Taking this approach allowed the team to:  
* Work effectively and productively by encouraging a goal-orientated mindset
* Be confident that all possible design smells were addressed and taken care of
* Achieve consistency in code as the team collectively decided how/to what extent each design smell would be resolved  

When addressing each design smell, the edits made to the code were guided by fundamental design principles, such as abstraction, DRY and KISS. This is elaborated in detail in the sections below.


### Rigidity/Fragility
Rigidity arose as a design smell during iteration 3 when additional updates were made to the project specification.  
* Mainly resolved using abstraction: more layers of abstraction = one change can fix problems everywhere else
* Hard coded parts were removed and replaced with more flexible methods, and very common problems were replaced with middleware-esque wrapper decorators.
* Design of our datastore using nested dictionaries and lists to create scalable structure for our data
* Scalability also means that when new code is added, it can be integrated seamlessly with the pre-existing code. This was the case for adding the reactions under the *messages* section of the code.
    * See backend/standup/standup\_send + backend/standup/standup\_start
    * See backend/utility/\*

### Immobility
While not a major part of the project, the code took immovability and adapting the code to new contexts as part of the design of the code. A major part of the refactoring that took place was the abstraction and fragmentation of code blocks into distinct modules.  
* Abstraction - easily editable to accommodate for new contexts (we spotted this a mile of in iteration 1 and planned for it, however we have added more modules in iteration 3).
    * See backend/utility/\*

### Viscocity
* Modularised format of the code meant that there were code sections that formed a template for new functions. Because the code was abstracted in this way, these functions could be reused when having to add new functions and add new functionality to old ones.
    * See backend/message/edit

### Opacity
* Comments were added to densely packed pieces of code
* Consistency across functions and modules ? variable names, format of functions
    * When integrating our sections of code together?
        * See backend/standup/standup\_send and backend/standup/standup\_start

### Needless Complexity
Some simple additions into the datastore got rid of some unnecessarily complex logic in some of our functions. We recognised that often functions gave tokens as the only method of identifying a user resulting in functions having to loop through lists to backwards-search for user data, such as user IDs. Rather than this, we replaced this search loop with the logically simpler task of accessing a dictionary entry from a ```token_to_<variable>``` dictionary, providing a simpler solution to the same task in accordance to the KISS principle. This method was also applied for other pieces of data such as ```email_to_uid```. Other than this, most of the code logic had been maintained and monitored during the implementation stage of iteration 2, keeping the code complexity to a minimum.  
* See literally everything cause everything used this (/backend/auth/passwordreset\_request)

### Needless Repetition
Many functions required the user to be authenticated using a token, but this procedure proved to be same piece of code for all functions. Using the DRY principle, the team realised that this needless repetition could be removed by defining a new wrapper function, ```@Secured```, for these functions.  
* See backend/message/edit

### Coupling
It was observed that there was some degree of coupling between different code modules within our code. This arose from the abstraction of some of the helper functions into separated modules which required them to be coupled to most main functions. However, this interdependence between main functions and helper functions was decided to be more beneficial than detrimental to the overall design of the code. It ensured that repetition was reduced in the code and that code was modularised, which complemented how work on functions was divided amongst team members.  
* Originally, standup functions required to make changes to the channel functions. But instead of reworking channels, we simply added a table that identifies a channels standup status, similar to the needless complexity things above.
* See backend/standup/standup\_send and backend/standup/standup_start
