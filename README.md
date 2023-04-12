# Word-Replacement-Algorithms

Implementations of two Word Replacement Algorithms to test speed and efficiencey when processing large data.

# Contributors
1. [Aminbhavi Suyash](https://github.com/SleepyPotato06)
2. [Mishra Satanshu](https://github.com/SatanshuMishra)
3. [Ramos Jason](https://github.com/JasonR24)

# Problem Statement

Keyword replacement in a corpus: In text analytics, often it is required that a set of keywords are replaced with a given set for the documents in hand. For example, on Twitter, people write a lot of abbreviations. When one requires to analyze the tweets, (s)he should find all the abbreviations in a given list of abbreviations (e.g. ASAP, won’t) and replace all these brief terms in the tweets with its proper phrase/keywords (e.g. ASAP -> As soon as possible, or won’t -> will not). Your job is to design an algorithm that finds all of the keywords that are in the abbreviation list in each tweet, and then replace them with the appropriate given keyword/phrase. The number of tweets can be millions and the list of keywords can be hundreds. A naïve approach is that for each tweet, your algorithm checks for all of the elements in the abbreviated list and replaces them. Other than the naïve approach, design a better algorithm and apply the required four steps explained in the first page.

# Abstract

This repository explores & compares the implementation of the search-and-replace algorithms utilising **Hashmap** and **Trie tree**.

The resulting graphs and prior analysis verify that the algorithms have a time complexity of **O(n)**. In addition to the implementation, the team completed some data processing, environment preparations, and implementation optimizations to address several difficulties including insufficient dataset size or inconsistent time complexities.

# Data & Results

![](https://lh5.googleusercontent.com/F5_X10QaJeHdSDLigE_xX9OaxF0tRU3l_kx-u7qBAD3k24oQNZkbDrr5rGfDhwk9OyHyCHHSNuJguKNxTRBhYKRfDSI4lmYt1X-QY6xPDR8jmZEJvnqbFvOOKDCwLp_FhlSOZVjkoPdQsIlDlA3U7SY)
>_Figure 1: Hash map algorithm tested against 100,000 to 1,000,000 character inputs_

![](https://lh5.googleusercontent.com/F5_X10QaJeHdSDLigE_xX9OaxF0tRU3l_kx-u7qBAD3k24oQNZkbDrr5rGfDhwk9OyHyCHHSNuJguKNxTRBhYKRfDSI4lmYt1X-QY6xPDR8jmZEJvnqbFvOOKDCwLp_FhlSOZVjkoPdQsIlDlA3U7SY)
>_Figure 2: Trie tree algorithm tested against 100,000 to 1,000,000 character inputs_
