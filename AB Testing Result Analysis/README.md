### Analysis of A/B Testing Results

There is an international online store.

There are the results of the A/B tests launched from 2020-12-07 to 2021-01-01, and the technical specification of one of the tests.

Technical description

* Test name: recommender_system_test
* Groups: А (control), B (new payment funnel)
* Launch date: 2020-12-07
* Date when they stopped taking up new users: 2020-12-21
* End date: 2021-01-01
* Audience: 15% of the new users from the EU region
* Purpose of the test: testing changes related to the introduction of an improved recommendation system
* Expected result: within 14 days of signing up, users will show better conversion into product page views (the product_page event), instances of adding items to the shopping cart (product_cart), and purchases (purchase). At each stage of the funnel product_page → product_cart → purchase, there will be at least a 10% increase.
* Expected number of test participants: 6000

__The purpose of the study__: to check if the tests were carried out correctly and analyze the results of the A/B tests.

__Description of the data__

The following datasets are available:
* `ab_project_marketing_events_us.csv` — the calendar of marketing events for 2020
* `final_ab_new_users_upd_us.csv` — all users who signed up in the online store from December 7 to 21, 2020
* `final_ab_events_upd_us.csv` — all events of the new users within the period from December 7, 2020 through January 1, 2021
* `final_ab_participants_upd_us.csv` — table containing test participants

Structure of `ab_project__marketing_events_us.csv`:
* name — the name of the marketing event
* regions — regions where the ad campaign will be held
* start_dt — campaign start date
* finish_dt — campaign end date

Structure of `final_ab_new_users_upd_us.csv`:
* user_id
* first_date — sign-up date
* region
* device — device used to sign up

Structure of `final_ab_events_upd_us.csv`:
* user_id
* event_dt — event date and time
* event_name — event type name
* details — additional data on the event (for instance, the order total in USD for purchase events)

Structure of `final_ab_participants_upd_us.csv`:
* user_id
* ab_test — test name
* group — the test group the user belonged to

See the research results in [11 AB Testing Result Analysis.ipynb](https://github.com/anastasia-klein/Yandex-Practicum100/blob/main/AB%20Testing%20Result%20Analysis/11%20AB%20Testing%20Result%20Analysis.ipynb)
