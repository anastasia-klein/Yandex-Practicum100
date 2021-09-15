### Final Project: Analysis of Non-optimal Use of Tariff Plans of the Virtual Telephony Service

There is the virtual telephony service that provides a communication network for organizations and distributes incoming calls among their operators, connects them to each other, and allows outgoing calls as well.

Statistics on the use of the service by operators of the clients are available: what tariff plan they use, how many calls they make, duration of calls, type of calls (internal or not, incoming or outgoing), information about missed calls.

__The purposes of the study are to:__

* find clients with non-optimal plans and those who need bigger calling plans, reveal their characteristics
* estimate the reduction in revenue if all users switch to plans that are more beneficial to them

__Description of the data__

The dataset `telecom_dataset_us.csv` contains the following columns:

- `user_id` — client account ID
- `date` — date the statistics were retrieved
- `direction` — call direction (`out` for outgoing, `in` for incoming)
- `internal` — whether the call was internal (between a client's operators)
- `operator_id` — operator identifier
- `is_missed_call` — whether the call was missed
- `calls_count` — number of calls
- `call_duration` — call duration (excluding waiting time)
- `total_call_duration` — call duration (including waiting time)

The dataset `telecom_clients_us.csv` has the following columns:

- `user_id`
- `tariff_plan` — client's current plan
- `date_start` — client's registration date

See the research results in [13 Final Project (Non-optimal Use of Telecom Tariff Plans).ipynb](https://github.com/anastasia-klein/Yandex-Practicum100/tree/main/Final%20Project#:~:text=13%20Final%20Project%20(Non-optimal%20Use%20of%20Telecom%20Tariff%20Plans).ipynb)

See a link to the dashboard on Tableau Public's server in [Dashboard Link.md](https://github.com/anastasia-klein/Yandex-Practicum100/blob/main/Final%20Project/Dashboard%20Link.md)

See a presentation of the research results in [20210705_final_project.pdf](https://github.com/anastasia-klein/Yandex-Practicum100/blob/main/Final%20Project/20210705_final_project.pdf)
