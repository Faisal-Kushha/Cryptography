# Lab: 18 - Cryptography

## Tools Used

VS Code

Python

Poetry

nltk

black

## Feature Tasks and Requirements

[x] Create an encrypt function that takes in a plain text phrase and a numeric shift.

- [x] the phrase will then be shifted that many letters.

E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’

- [x] shifts that exceed 26 should wrap around

E.g. encrypt(‘abc’,27) would return ‘bcd’

- [x] shifts that push a letter out or range should wrap around

E.g. encrypt(‘zzz’,1) would return ‘aaa’

[x] Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

[x] create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

[x] Devise a method for the computer to determine if code was broken with minimal human guidance.

## Implementation Notes

[x] In order to accomplish a certain task you’ll need access to a corpus of English words.

- [x] A search on something like python list of english words should get you going.

## User Acceptance Tests

[x] encrypt a string with a given shift

[x] decrypt a previously encrypted string with the same shift

[x] encryption should handle upper and lower case letters

[x] encryption should allow non-alpha characters but ignore them, including white space

[x] decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.

[x] refer to supplied unit tests.

## Developer

Faisal Kushha

## Pull requests

https://github.com/Faisal-Kushha/Cryptography/pull/1
