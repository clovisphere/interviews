# Backend API tests 📝
Solution to the [Stitch.Money](https://stitch.money/) Quality Engineer assessment - **API Testing**.

## What is the purpose of this project?
> The purpose of this project is to test the TODO List application (API).

### API Testing Checklist
1. Verify that the API is working as expected.
2. Verify that the API is returning the expected data.
3. Verify that the API is returning the expected error codes.
4. Verify that the API is returning the expected error messages.
5. Verify that the API is returning the expected HTTP status codes.
6. Verify that the API is returning the expected HTTP headers.
7. Verify that the API is returning the expected HTTP response bodies.
8. (optional) API security testing.
9. (optional) API performance testing.
10. (optional) API integration testing.

☝🏽 Test ideas guide my (exploratory) tests - not a big fan of "test cases" 
(I don't mind them but test ideas are much more fun 🤭).

**Key points**:
- This being a [RESTful API](https://www.redhat.com/en/topics/api/what-is-a-rest-api), does the API use the right HTTP [verbs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) and [status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)?
- Does the API return the expected headers and response bodies? (case in point, [RFC 4627](https://www.ietf.org/rfc/rfc4627.txt) for **JSON MIME media type**)
- Does the API handles duplicate requests?
- Does the API handles invalid requests?
- Does the API handles invalid data?
- Does the API implement oauth2 authentication?

**IMPORTANT** 〽️ ⚠️ 
- I have commented out section that verify that the expected
  [Header's Content-Type](./app/src/test/kotlin/com/clovisphere/interviews/stitch/APITest.kt#L35) is 
  returned by the API on each test because the API returns "_text/json; charset=utf-8_" by default.
- I purposefully made API calls using **PUT** and **DELETE** verbs. 
  Why? 'cause I'm a big fan of [RESTful API](https://www.redhat.com/en/topics/api/what-is-a-rest-api) 😆
  
On a more serious note, using good naming conventions and a pattern makes 
it easier to read and understand the code, see 👇🏽

E.g.
```bash
$ curl -X PUT -H "Content-Type: application/json" -d '{"status":"done"}' http://localhost:8080/todos/1
```
and
```bash
$ curl -X DELETE -H http://localhost:8080/todos/1
```
are much more readable than
```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "status":"done"}' http://localhost:8080/edit-todos
```
and
```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"id": 1}' http://localhost:8080/del-todos
```
(This could be part of the recommendation to the team in charge of the [Stitch.Money](https://stitch.money/) 
Quality Engineer assessment)


#### A note on the tooling used in this project
I chose to use [Rest-assured](https://rest-assured.io/) for API testing. 
[Postman](https://www.postman.com/) and [Insomnia](https://insomnia.rest/) are choices I considered, 
but I went with Rest-assured because I find it very flexible and easy to use... 
and it plays (really) well with [Kotlin](https://kotlinlang.org/) 🥳 🎊

#### Requirements
Before we run our tests, grab a copy of the [TODO List (API)](https://github.com/Stitch-Money/Todo-list-api.git) 
and run it (information on how to deploy the app locally is on 
the [README](https://github.com/Stitch-Money/Todo-list-api/blob/main/README.md))... 
I will assume that you have the [TODO List (API)](https://github.com/Stitch-Money/Todo-list-api.git) 
running on port 8080.

```console
Java:   >= 11
Kotlin: >= 1.6
Gradle: >= 7.4.2
```

**Note**: You can change the TODO app's url and port number in the 
[setup(...) function](./app/src/test/kotlin/com/clovisphere/interviews/stitch/BaseTest.kt#L20)

It is possible to run these tests on [IntelliJ](https://www.jetbrains.com/idea/) or 
any other IDE. But for the purpose of this assessment, we will use the command line and gradle.

###### How to run the tests?
```bash
$ git clone https://gitlab.com/clovis.mugaruka/interviews.git
$ cd interviews/stitch.money/quality_engineer/api_testing
$ ./gradlew clean test
```

Test Summary Report can be found [here](./app/build/reports/tests/test/index.html).


Build with 💘 🇨🇩
©️ 2022 Clovis Mugaruka
