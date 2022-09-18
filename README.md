# Holo Schedule API
A Web API to get hololive's schedule.

## Getting Started
(Only supports local use for now, but it is planned to be deployed somewhere...)
- Install requirements and run `flask run`.
- `http://127.0.0.1:5000/schedules` to get all schedules, default is jp members.
- To get en, id members, specify in the url: `/en/schedules`.
- To get today's schedules: `/schedules/today`

## Notes
This program scrapes [this page](https://schedule.hololive.tv/lives/hololive)
and will update every 5 minutes. However the source page updates every 15
minutes, therefore, there will be at most 20 minutes of delay to the actual
stream schedule.
