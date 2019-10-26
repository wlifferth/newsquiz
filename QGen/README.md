# QGen

Generating questions happens in an unsupervised way:
1. A headline comes in and is processed for named entities (all named entities are logged in a NE table)
2. One of those named entities is chosen to be obscured (this is the "answer")
3. The NE type and embedding fingerprint are used to select n other named entities to act as the alternate answers

## Key Challenges
- Categorizing Named Entities
    - It would be helpful to be able to bucket named entities in some sensible taxonomy (i.e. Person > Politician), but there's a good amount of fuzziness with named entities. Is Elizabeth Warren a politician or an academic?
    - One obvious solution is to have a Named Entity collection then a separate taxonomy collection, where a single named entity can appear in many taxonomy categories.
- Choosing Alternate Answers
    - An ideal alternate answer (that is, alternate to the correct answer) has both properties of semantic similarity and distinct identity. If the correct answer is "Donald Trump", "Don J Trump" is a bad answer because it lacks a distinct identity, and "Antarctica" is a bad alternate answer because it lacks semantic similarity. ("Mitch McConnel" or "Emanuel Macron" would be better alternate answers because they are both distinct and semantically similar).
    - To ensure distinct identity we need a robust deduping mechanism. When a new Named Entity is found, it will need to be compared to some subset of all current named entities.
    - To ensure semantic similarity we can use some kind of taxonomy (see above), and only pull alternate answers from similar taxonomical groups.
