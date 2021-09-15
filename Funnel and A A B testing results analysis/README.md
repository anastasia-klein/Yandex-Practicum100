### Event funnel analysis and analysis of A/A/B testing results

There is an application for the sale of food products.

We have logs with data on pageviews including the experiment ID, one of which is changing fonts for the entire app.

__The purpose of the study__: to investigate user behavior for the company's app, study the sales funnel, analyze the results of the A/A/B test and determine whether the font affects user behavior.

__Description of the data__

The dataset contains the following fields:

* `EventName` — event name
* `DeviceIDHash` — unique user identifier
* `EventTimestamp` — event time
* `ExpId` — experiment number: 246 and 247 are the control groups, 248 is the test group

See __the research results__ in [9 Funnel and A A B testing results analysis.ipynb](https://github.com/anastasia-klein/Yandex-Practicum100/blob/main/Funnel%20and%20A%20A%20B%20testing%20results%20analysis/9%20Funnel%20and%20A%20A%20B%20testing%20results%20analysis.ipynb)
