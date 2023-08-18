# Test Plan

| Release | Product Name | Test Owner | Date | Comments 			   |
| ------- | ------------ | ---------- | ---- | ----------------------- |
| 1.0 | TODO List | Clovis Mugaruka | April 14th, 20222| Initial Draft |

## Product Description
An application that allows users to keep track of activities or tasks they need to do.

## Test Objective

> Evaluate the stability of the product, its functions and features.

## Documentation

1. [Frontend / UI](https://github.com/Stitch-Money/todo-front-end)
2. [Backend API](https://github.com/Stitch-Money/todo-front-end)
3. [UI Test Cases](https://gitlab.com/-/ide/project/clovis.mugaruka/interviews/edit/main/-/stitch.money/quality_engineer/ui_testing/README.md#L7)
4. [API Checklist](https://gitlab.com/-/ide/project/clovis.mugaruka/interviews/tree/main/-/stitch.money/quality_engineer/api_testing/README.md/#L7)

## Test Phases

| Phase   | Description 																				  				|
| ------- | ----------------------------------------------------------------------------------------------------------- |
| Prep    | Preparation for the tests, which include things such as setting up test environment, test case design, etc. |
| Test    | Test plan execution and agile delivery of test results													  	|
| Closure | Share test findings (report)																				|

## Schedule

| Day | Period  | Topics Activity 												   |
| --- | ------  | ---------------------------------------------------------------- |
| 1   | Prep    | Finalize test plan,team review, workspace setup, test case setup |
| 2   | Prep    | Test server setup + configuration, software installation         |
| 3   | Test    | UI                                                               |
| 4   | Test    | Backend API                                                      |
| 5   | Test    | Application Performance Testing                                  |
| 6-7 | Test    | Regresion, end to end test                                       |
| 8   | Closure | Reporting, analysis and presentation                             |


## Result Measurement

| Feedback Type | Objective 														|
| ----------- 	| ----------------------------------------------------------------- |
| Bug reports   | Test quality, real world performance 								|
| Suggestions   | Measure acceptance, prioritize backlog, generate new (test) ideas |


## Test Budget
N/A

## Miscellaneous

**Research**
- Read through all the TODO List code (both backend and frontend) to:
	- Identify possible point of failure
	- Identify all callbacks needed for mocking
	- Identify DB schema for data seeding
- Gather acceptance criteria for initial test case/ideas planning
- Research how to mock the api, as well as the in-memory cache
- Research needed for integration tests
- Check Spock framework

**Performance / Load Test**
- Simulate 100,000 - 1,000,000 users accessing the TODO List application and doing different action, e.g. create todo, edit tod, etc.
- What happens when the in memory cache/db has a lot of todos (1 million)? Does the performance degrade?
- Research other aread of the application we can load test.

**Security Testing**
Security wasn't a requirement for this 'initial' test, but it will come in handy before we go live. 
We may need to research tools we can use for OWASP validation and penetration (open source or paid software).

**Action items to come from research**
- Write JIRA ticket for all necessary work to be done.
- Create a JIRA Epoc for the TODO List application testing.
