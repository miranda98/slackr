# Teamwork

So far our teamwork has run smoothly leading up to the submission of iteration two. We had determined much of what is listed below in iteration one.

##### How often you met, and why you met that often
Overall we had three standups across the the period of iteration two. Our first standup was more focused on:
 * Progress reports,
 * Planning workloads,
 * Setting deadlines, and
 * Understanding key concepts

Our second standup was more focused on the how we would store our data:
 * Discussing the ER diagram as part of lab06
 * Consistent storage of data (creating data, appending/adding data, removing data)

Our third standup was more focus on integration:
 * Integrating modules,
 * Ensuring tests had branch coverage, and
 * Correct use of modulularised components (shared modules)

Minutes were recorded for standups 1 and 3 as they occured through online calls, and are uploaded in the repository. The 2nd standup was face-to-face during the lab time, and notes were taken individually, so no minutes were taken for this standup.

##### What methods you used to ensure that meetings were successful
During both standups we had a member of our team take minutes and prior to each standup each member wrote several points they wanted to talk about in a group chat to ensure we addressed all necessary points.  
  * Utilizing the taskboard to identify talking points and large areas in need of addressing.
  * Code reviews (primarily shared modules or examples of how to acomplish tasks such as validating tokens).
  * Constant communcation, keeping a log of changes and workflow in our group chat to ensure everyone is on the same page.

##### What steps you took when things did not go to plan during iteration two
Refer to the taskboard to determine priority in assigning and implementing. Post to the group chat to engage in communal discussion of issues affecting the entire team, or simply to ask for assistance.  
Iteration two was a lot of small things conjoined, issues we had were:
 * Meeting deadlines on more complicated backend implementation. Regular standups mitigated this issue.
 * Writing succint tests to check for features added since iteration one. 

##### Details on how you had multiple people working on the same code
Many issues can arise when multiple people are working on the same code; such as conflicting variable names, function names and incorrect storage of data to name a few. To avoid any issues we created shared modules of code that handled our 'standardisation' of things like JWT secrets, data storage and errors. We strived to ensure each member could develop their code without much consideration of other peoples work. However exceptions to this rule included:
  * Naming conventions of data storage:
    * For instance the names of variables and dictionary keys (although we stick to the specifications primarily).
  * Return types:
    * Our blueprint's require in certain cases to return an empty dictionary.
  * Paired Programming:
    * By having multiple people working together on the same code at the same time, we were able to mitigate any possible conflict issues with our data and minimise chances of errors.


##### Our steps inherited from iteration one
Anticipating complication intersections between modules we agreed upon documenting to a communal folder under a directory structure resembling the package path. 
* If any modules has specific 'quirks' or defined behaviours, it is recorded here to allow people using this module to use it breezily.
* Communication is paramount and so we have created a Facebook Messenger group chat from which each participate in asynchronous stand ups, sharing any progress on our own modules or shared files (e.g. assumptions.md, plan.md ...).
	* Also participate in more synchronous stand ups during labs.
* Engaging in pair programming in order to assist team members with less experience. Most pair programming was conducted over Facebook Messenger call due to difficulties with physically meeting up and was highly effective in resolving program inconsistency issues and teaching members better programming practices (eg. use of ternary expressions, importing modules from other directories).

###### Conclusion
We aim to continue splitting the work as we have it now. We worked all of this out in the last iteration, gave certain people certain modules and are implementing them in an appropriate order. As we go into iteration 3 we will analyze the remaining functions and continue to assist each other in their development
