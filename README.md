# BNT162b2-vaccine
The point of this challenge is to create an algorithm to figure out the mRNA sequence of the BNT162b2-vaccine by replacing the last amnio acid in each codon. This is the easy part, it seems like RNA folding needs to get integrated somehow for better optimazation (not an easy task in Python) as brought up in this [PR](https://github.com/berthubert/bnt162b2/pull/3).

Came across:
- [Reverse Engineering the source code of the BioNTech/Pfizer SARS-CoV-2 Vaccine](https://berthub.eu/articles/posts/reverse-engineering-source-code-of-the-biontech-pfizer-vaccine/) 
- [Reverse Engineering Source Code of the Biontech Pfizer Vaccine: Part 2](https://berthub.eu/articles/posts/part-2-reverse-engineering-source-code-of-the-biontech-pfizer-vaccine/)

All the data and information can be found through both posts, pretty fun challenge so far. Currently have the algorithm at `79.4%` match for Codons.
