# QGen

Generating questions happens in an unsupervised way:
1. A headline comes in and is processed for named entities (all named entities are logged in a NE table)
2. One of those named entities is chosen to be obscured (this is the "answer")
3. The NE type and embedding fingerprint are used to select n other named entities to act as the alternate answers

# Fingerprints
Every named entity has a fingerprint, which is a low-dimensional embedding that can be used to avoid fuzzy matches as answers for the same question (i.e. we doh't want "Donald Trump" and "Mr. Trump" to appear in the 
