### Analyzing the business metrics of Yandex.Afisha

There is a service that helps users find out about events like movie showings, exhibitions, gigs, etc. and buy tickets.

The following data are available:

* Server logs with data on Yandex.Afisha visits from June 2017 through May 2018
* Dump file with all orders for the period
* Marketing expenses statistics

__The purpose of the study is to explore:__

* How people use the product
* When they start to buy
* How much money each customer brings
* When they pay off

__Description of the data__

The `visits` table (server logs with data on website visits):
* Uid — user's unique identifier
* Device — user's device
* Start Ts — session start date and time
* End Ts — session end date and time
* Source Id — identifier of the ad source the user came from

The `orders` table (data on orders):
* Uid — unique identifier of the user making an order
* Buy Ts — order date and time
* Revenue — Yandex.Afisha's revenue from the order

The `costs` table (data on marketing expenses):
* source_id — ad source identifier
* dt — date
* costs — expenses on this ad source on this day

See the research results in [Yandex Afisha business metrics analysis](https://github.com/anastasia-klein/Yandex-Practicum100/tree/main/Yandex%20Afisha%20business%20metrics%20analysis)
