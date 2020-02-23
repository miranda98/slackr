# Assurance

Our assurance is largely based on the verification of our implementation (backed by our testing) and validation of our approach via system testing and acceptance testing/criteria. Such assurance is necessary to ensure the correctness of our implementation both in a more formal algorithmic sense and also a more informal descriptive sense.

##### Verification

During iteration one we designed a testing suite and during iteration two we expanded upon that iteration suite in order to achieve code coverage in the form of lines and branch coverage.
 * Most major critical modules have 100% branch coverage and line coverage (possibly all depending on how much time requirements).
 * Modules are short and attempt to minimise the need for branch coverage by having low cyclomatic complexity (more functional).
 
Tools we used to acomplish this verification include:
  * Pytest: for the testing of modules.
  * Pycoverage: for the testing of branch and line coverage (note. uses Pytest).
  * Pylint: for cleaning up our syntax (note. Pylint complains about our modularization files \__init__.py).
    * For Pylint, we decided to neglect most modules for things like variable naming and docstrings due to time constraints, but we did follow structual complaints to avoid anti-patterns. 
    * While we understand that variable/function naming and docstrings greatly improve the maintainability of a module and project at large, we assumed that all of this code will never see the light of day and we were restricted on time due to other engagements: _something something trimesters something something_.

##### Validation

Our validation comes from assuring that features described and required by user stories have been implemented and acceptance criteria that provides a less technical and more explicit detail of what a user expects as apposed to wants or needs. Our acceptance criteria includes but is not limited too:
  * Given that I am not logged in, if I login, I expect to be able to access any functionality requiring authorization.
  * Given that I am logged in, if I logout, I expect to be unable to access any functionality requiring authorization.
  * Given that I have logged in on one browser/device, if I log in on other devices/browsers, I expect to stay be logged in on all platforms.
  * Given that I have logged out
  * Given that I am unregistered, if I register correctly, I expect to be logged in immediately.
  * Given that I have registered, if I change my password, I expect the next time I login I require my new password.
  * Given that I am a member of a channel, if I invite someone to a channel, I expect them to be able to access said channel immediately.
  * Given that I have joined a channel, if I view the channel's messages, I expect to see the latest messages.
  * Given that I have joined a channel, if I leave the channel, I expect to not see it in my channels list.
  * Given that I have joined a channel, if I send, remove or edit a message, I expect to see said modifications occur to the message in said channel immediately.
  * Given that I have joined a channel, if I pin a particular message, I expect other members to be able to identify the pinned message.
  * Given that I have joined a channel, if I react to a message, I expect the reaction to be noticeable by other users.
  * Given that I registered, if I change any component of my profile, I expect all displayed information to reflect this change i.e. invalidate cache if any.
  * Given that I have joined a channel, if I start a standup, I expect other members to recieve a message indicating an event has occured.
