# Holo Schedule API
A Web API to get hololive's schedule.

## Getting Started
(Only supports local use for now, but it is planned to be deployed somewhere...)
- Install requirements and run `flask run`.
- `http://127.0.0.1:5000/schedules`
- To use twitter api search functions, keys are required to be specified in `credentials/credentials.yaml`.  

## Contribute
All suggestions are welcomed,
The source code uses yapf formatter.

## Notes
This program scrapes [this page](https://schedule.hololive.tv/lives/hololive) and will update every 5 minutes. However the source page updates every 15 minutes, therefore, there will be at most 20 minutes of delay to the actual stream schedule.