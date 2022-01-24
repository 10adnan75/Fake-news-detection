### LIAR: A BENCHMARK DATASET FOR FAKE NEWS DETECTION

_William Yang Wang, "Liar, Liar Pants on Fire": A New Benchmark Dataset for Fake News Detection, to appear in Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (ACL 2017), short paper, Vancouver, BC, Canada, July 30-August 4, ACL._

---

> Note that the full-text verdict report is not available in this version of the dataset, but you can get the entire verdict report and links to the source documents by running the following command: ``` wget http://www.politifact.com//api/v/2/statement/[ID]/?format=json```

**The TSV format is described as follows:**

| Column | Content |
| --- | --- |
| 1 | `ID` |
| 2 | `label` |
| 3 | `statement` |
| 4 | `subject(s)` |
| 5 | `speaker` |
| 6 | `job title` |
| 7 | `state info` |
| 8 | `party affiliation` |
| 9 | `barely true counts` |
| 10 | `false counts` |
| 11 | `half true counts` |
| 12 | `mostly true counts` |
| 13 | `pants on fire counts` |
| 14 | `context` |

---

**_The data's copyright is retained by the original sources. There are no assurances with this data, and it is offered `as is`, although you are invited to report any faults with the preliminary version. This dataset is intended to be used for research purposes only. Kindly contact William Wang at william@cs.ucsb.edu if you have any further queries concerning the dataset._**
