# Plan (M18A-anything | James, John, Miranda, Mitchell)
Our plan is split into several stages, being mainly comprised of:
* General overview of project of our approach
* Our approach to testing.
* Dot point coverage of iteration 2 requirements
* Timeline for iteration 2 and the some of the rest of the project

### General overview

So far we have split up the project into logical segments, that we will create as modules, for instance an 'auth' module for all of the functions relating to 'auth'. The actual design of these modules has been split into almost equal parts across our team, ensuring that any one module has one person associated with it at least, the implementation of any module is up to the implementor.

Furthermore, we have anticipated some implementation problems and seek to solve them before we begin implementing:

##### 1. A filesystem is the best database right?

* Since integrating an actual database is probably out of the scope of the project we seek to have a simple universal solution. A solution that has stood out to us is to simply use the filesystem to our advantage and store the state of the database at any one time in a file. To follow our approach in modularization of our project we may simply store its related database information in a series of files in its directoy; Since different modules can access information via the interface the module provides it is up to the descrtion of the module designer in how they wish to design this (however we will probably follow a standard that develops as we begin implementing).
* For instance: Serialize the state of tokens, added channels etc. in a file and append/pop as needed. We can unserialize it into a list to be modified when required.

##### 2. Python does not 'limit' is users!

* Sharing common modules may be helpful and speed up the development in iteration 2. For instance: Modules for automatically handling serializing of information to files. However since python does not have a import system that utilizes file structrure we will have to search for a solution that will either comprise of
    * Flattening the directory structure
    * A neat way to have include modules such as appending to the 'os.path' a common folder relative to any module.

##### 3. There is no I in team but there is an M and a E.

* our plan to sdeperatly implement various sections may fail at the interfaces of our modules. Since these modules must be integrated we sought a way to prevent mismatch interfaces and expectations. Our solution is to duplicate the directory structure of the modules in a /docs folder which instead of implemented code contains doc files explaining the expected inputs and outputs and also and particular 'quirks' of said module/function (like a mini-man but distributed across several files).

### Testing

* Testing is a central part of our project and the order of implementation of our modules is an outcome of this.
* Throughout the design of our individual code we will most likely rely on automatic testing and analysis of code coverage to ensure validate our modules (and branch coverage in more complex or convoluted areas/algorithms).
* After several modules have been developed to the point of integration we will begin integration testing, relying on our mini-man documents as described above to understand the interfaces between our modules to verify them.
* Several tools will be used in this section to assist our team in production of code:
    * Obviously 'pytest' will be used to automate the testing process. View our current tests for examples.
    * For coverage 'coverage.py' will be used since it was explained in the lectures and most familiar to everybody.
    * While not directly associated with tests, seeing it is also a CASE tool 'pylint' will be included here to recognise our descion to follow a design standard.

### Timeline of Implementation

We will have to follow a logical order for all the functions we implement to ensure that any functions we want to test will actually be "testable" by pytest or some other driver program. This in the most basic form means that any functions related to the creation of a channel will have to be the first functions we implement [since we can just use a dummy token]. We can also simultaniously work on authorisation [aka any auth_* functions], since a strong understanding of how it will work will be cruical for all future functions where tokens will be passed.

After we have a channel that is working, we can then get onto "using" the channel, and development opens up quite a bit. Once we have a channel, we can implement and test any functions relating to the operation of the channel - such as channel_invite, channel_details, channel_join, channel_leave and channel_add/remove_owner [and admin_userpermission_change once we have multiple user options]. Furthermore, now that we have the ability to create multiple channels, we will be able also test functions such as channels_list/listall. Within these channels we will also be able to start the creation of message functions, starting with message_send, then moving onto message_edit/remove. As stated, we would want to at least have a strong basis in our tokenization method before we move onto these functions however.

Once these message functions are developed we can further test some other features of our code such as channel_message before moving onto the remaining message functions [which clearly for functions such as message_pin/unpin and message_react/unreact will need to have the function that adds the reaction completed before we can test the one that removes it]. We will also be able to implement other functions such as our standup_start/send functions and the search function.

Last but not least it the user functions: which has nothing preventing them being developed in tandem with all the other functions, however they are also non-vital to server operation - only user experience. Hence these have a lower priority then other functions that are fundamental to the server working. The same goes for a lot of the quality of life functions [such as pin, react, standup and search] and hence explain their priority in the above plan [alongside the fact it requires other functions to be complete before we can start them].

#### Diagramatic
See 'diagramatic-plan.pdf'
