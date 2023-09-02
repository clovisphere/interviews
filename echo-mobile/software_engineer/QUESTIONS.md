# Software Engineer Assessment

Questions:

- You are given a string S composed of characters A to Z, formulate a function that transforms a given string by changing each letter as follows: ‘a’ becomes ‘z’, ‘b’ becomes ‘y’, ‘c’ becomes ‘x’, etc. See [solution](./pset1.py)

- You a given a string S of any length, formulate a function that splits the strings into substrings of a given length N and returns the substrings in a list. If the length of S is not evenly divisible by N, it is acceptable to have the last substring with a length less than N. See [solution](./pset2.py)

- Assume you have a sensor that reports temperature readings periodically. The readings are stored as 2 lists of equal length; List T composed of timestamps for each reading and list R composed of temperature readings for each of the matching timestamps. Your goal is to identify timestamps at which a certain threshold temperature Q was crossed. Formulate a function that takes lists T and R and a threshold temperature Q and returns a list of timestamps where Q was exceeded. Note that you should only return timestamps representing a datapoint that crosses the threshold, and ignore those that remain above the threshold. See [solution](./pset3.py)

- You are given a list P of average share prices for a particular stock for each day in a given year. Your goal is to buy 1 share and later sell it at maximum profit. Formulate a function that takes list P and returns the best day to buy (B) and the best day to sell (S). You have to buy the share before you can later sell it. See [solution](./pset4.py)
