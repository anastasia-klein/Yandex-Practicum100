### Prioritizing hypotheses and the A/B test results analyzing

There are a list of hypotheses that may help boost revenue of a big online store. It's necessary to prioritize these hypotheses in order to cut expenses on experimentation and test only the most promising ideas.

There are the results of the A/B test of one of the the hypotheses. The purpose of the study: to analyze the results of the A/B test and make a business decision based on the findings of this analysis.

__Description of the data__

The dataset used to prioritize the hypothesis contains the following fields:

* `Hypotheses` — brief descriptions of the hypotheses
* `Reach` — user reach, on a scale of one to ten
* `Impact` — impact on users, on a scale of one to ten
* `Confidence` — confidence in the hypothesis, on a scale of one to ten
* `Effort` — the resources required to test a hypothesis, on a scale of one to ten. The higher the Effort value, the more resource-intensive the test.

The data containing the A/B test results coinsists of 2 tables:

* the table containing information about orders:
    * `transactionId` — order identifier
    * `visitorId` — identifier of the user who placed the order
    * `date` — of the order
    * `revenue` — from the order
    * `group` — the A/B test group that the user belongs to

* the table containing information about visits:
    * `date` — date
    * `group` — A/B test group
    * `visits` — the number of visits on the date specified in the A/B test group specified

See the research results in [7 AB Test Analysis.ipynb](https://github.com/anastasia-klein/Yandex-Practicum100/blob/main/AB%20Test%20Analysis/7%20AB%20Test%20Analysis.ipynb)




