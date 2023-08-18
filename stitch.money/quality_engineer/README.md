 # Quality Engineer Assessment

My solution to [Stitch.Money](https://stitch.money/)'s Quality Engineer Assessment.

I have created dedicated folders for each of the 'coding' tasks:

1) [Automated tests for UI](./ui_testing)
2) [Performance tests](./perf_testing)
3) [API tests (backend)](./api_testing)

See the [BUGS.md](./BUGS.md) file for bugs I've found in the applications, and [TESTPLAN.md](./TESTPLAN.md) for the test plan.

### Things I wanted to do but didn't manage to (time wasn't on my side 😞)

- Build a CI/CD pipeline to run the automated tests, i.e. [GitLab CI](https://docs.gitlab.com/ee/ci/) or [GitHub Actions](https://github.com/features/actions) 😆
- Using headless browser to speed up UI Automated tests, e.g. [puppeteer](https://github.com/puppeteer/puppeteer).
- Write the UI/API automated tests in Elixir (or Ruby), use [vegeta](https://github.com/tsenart/vegeta) for HTTP load testing.
- Explore [Visual Testing With Visual AI](https://applitools.com/). 

Mea culpa 🙏🏽

#### Tools:

Tools you will probably require:

- [git](https://git-scm.com/)
- [Kotlin](https://kotlinlang.org/)
- [Python](https://www.python.org/)
- [Gradle](https://gradle.org/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

Each 'coding' task has a (dedicated) **README**, e.g. you can use [this guide](./perf_testing/README.md) for the performance testing task, for example. 
Please, follow instructions in the **README** to run tests. 
