## Teamwork: Agile practices
### Table of contents
- [Introduction](#introduction)
- [How often we met](#how-often-we-met-and-why-we-met-that-often)  
- [Ensuring successful meetings](#what-methods-we-used-to-ensure-that-meetings-were-successful)
- [Dealing with failure](#what-steps-we-took-when-things-did-not-go-to-plan-during-iteration-three)
- [Working together](#details-on-how-we-had-multiple-people-working-on-the-same-code)
- [Looking to the past](#our-steps-inherited-from-iteration-two)
- [Looking to the future](#improvements-in-future-projects)
- [Conclusion](#conclusion)  

<br>

##### Introduction
Following from iteration 2, the lead up to the submission of iteration 3 has run smoothly. We had determined much of what is listed below in iteration one, and have since extrapolated and adjusted as the project has progressed.  

<br>

##### How often we met, and why we met that often
Overall we had two standups across the the period of iteration three. Any done during labs were more generally about integration with frontend, whilst the others were done using messenger and having a group call with everyone who was available. Any that were done over messenger had their minutes recorded and saved in our repo.  

Our first standup was more focused on:
* Updates on what work was left to be done  
* Planning workloads and re-delegation of tasks  
* Analysis of specification update  
* Setting deadlines  
* Discussing questions and feedback from iteration 2  

Our second standup, which took part during the lab time of week 8 focused on:
* Reviewing the work that needed to be completed, as much of the tasks that were set from the previous standup were near completed  
* Getting emails to work with the password reset functionality.  
* Serving static content on the frontend/backend.  
* Re-delegating tasks (again), this time including the markdowns and ER diagram as well as the code  
* Ensuring that the functions that were still to be completed after iteration 2 were working with the front-end  
* Threading aspects of the project.  

<br>

##### What methods we used to ensure that meetings were successful  
Successful meetings are key to agile development, so to ensure our meetings were successful we used the following methods:  
* During the first standup, minutes were taken (uploaded in our repository), so that all team members could review what points they missed. This was particularly important as one team member was absent, so they were able to view the minutes and clarify with the rest of the team over messenger about what work was to be expected for the following weeks. Somewhat identical to our other iterations, we are getting quite good at this.  
* Utilizing the taskboard to identify talking points and large areas in need of addressing.  
* Code reviews (primarily more difficult things like emails and threading).  
* Constant communication, keeping a log of changes and workflow in our group chat to ensure everyone is on the same page.  

<br>

##### What steps we took when things did not go to plan during iteration three
We had very few problems in iteration three, due to the processes listed below that prevented any issues: 
* Meeting deadlines - We were sure to have ALL CODE (including tests and refactoring) done well before the due date, leaving us time to focus on documentation.  
* Taskboard - Referring to the taskboard to determine priority in assigning and implementing  
* Updates - Post to the group chat to engage in communal discussion of issues affecting the entire team, or simply to ask for assistance.  

<br>

##### Details on how we had multiple people working on the same code
Many issues can arise when multiple people are working on the same code; such as conflicting variable names, function names and incorrect storage of data to name a few. To avoid any issues we created shared modules of code that handled our 'standardisation' of things like JWT secrets, data storage and errors.  

Some agile practices we used to ensure this included:  
* Pair programming:  
    * We engaged in pair programming for several features:  
        * Sending emails for resetting the password, discussing in our standups and then working from home, pushing and pulling each others amendments.  
        * Upload photo, discussing in our standups and then working it out in the lab together. 
    * The use of pair programming allowed us to work together on difficult segments/functions so one person could focus on code generation whilst another could focus on code logic - allowing for faster development of code overall.
* Peer/code review:  
    * We engaged in peer/code review for several features:  
        * Threading, for message sendlater and standup_start. 
        * Reviewing each others code, suggesting improvements to avoid code smells (See seprinciples.md)
    * Some of the reasons we completed peer/code reviews:  
        * Refactoring correctly - since a lot of our code was modularised, everyone's code was peer reviewed to make sure they all cleaned up their code and utilised the 'modules' correctly, and also to make sure everyone's code was consistent so it was easy for all team members to understand.  
        * Engineering principles - By reviewing our peers code, we could improve our own code implementations to better follow the DRY KISS principles and prevent code smells in both the code we are reviewing and our own future code.  

<br>

##### Our steps inherited from iteration two  
Due to the nature of the project, we must have inherited a few steps from prior iterations. Most notably:  
* Anticipating complication intersections between modules we agreed upon documenting to a communal folder under a directory structure resembling the package path.
    * If any modules has specific 'quirks' or defined behaviours, it is recorded within our repo to allow people using this module to use it with ease.  
    * These modules follow the same directory structure as the rest of the repo to ensure ease of use
* Communication is paramount and so we have created a Facebook Messenger group chat from which each participate in asynchronous stand ups, sharing any progress on our own modules or shared files (e.g. seprinciples.md, teamwork.md ...).
	* Also participate in more synchronous stand ups during labs and over voice call online
* Engaging in pair programming in order to assist team members with less experience. 
    * Most pair programming was conducted over Facebook Messenger call due to difficulties with physically meeting up
    * Was highly effective in resolving program inconsistency issues and teaching members better programming practices (eg. use of ternary expressions, importing modules from other directories).  

<br>

##### Improvements in future projects  
Whilst overall we worked well as a team, we believe there were a few areas for improvement if we were to do such a project again. This includes(but is not limited to):  
* Personal skills - Whilst its great to have one member on our team who is very proficient in code development and the associated processes; in future projects it would be good for us to all understand the process, something this project has helped the less experienced of us to understand.  
* Delivery layout - Whilst we had completed all our work to a high standard, we did still lose a number of "marks" in iteration 2 due to our documentation not being presented in an expected layout to the markers. This, in a project outside of uni/working with a larger team, would cause confusion and possible major delays - so we have all learnt from this experience how important documentation is, especially in its expected layout.  
* Deadlines and work allocation - We have all learnt the importance of maintatining deadlines and allocating work evenly among team members through this project. We noticed that workflow became much smoother when work was delegated with each members' strengths into consideration. While there was the equal workload requirement set by the course, this is something that will be useful in all future group tasks.
* Software engineering principles - Through this project, we have learnt the value in principles such as DRY, DIE, SOLID and KISS for software development that will allow us to implement better code in the future. It highlighted the importance of well designed code as being equal to a fully functioning product which became good foundations for us for future software projects.

<br>

##### Conclusion
We had excellent teamwork through iteration three and the project more generally. It went quite smoothly with a few hitches here and there but overall everything was smoothed out. By use of planning and agile practices we were able to design a solution that both fulfilled all criteria and delivered a finished product. By following good software engineering practices we have allowed any future teams who take over/use this code a simple task of modifying it to their purposes.

<br>