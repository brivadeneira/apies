# APIes

RESTful API which responds elasticsearch requests.

 ![](https://i.imgur.com/N0tRK7K.png)
 *Simplified APIes diagram*

# Table of contents
* [Features](#features)  
* [Installation](#installation)   
* [Python version](#python-version)   
* [Usage](#usage)   
    * [Run the APIes](#run-the-apies)   
    * [Current Checkpoints](#current-checkpoints)   
    * [Model requests](#model-requests)   
    * [Model responses](#model-responses)   
    * [Python requests](#python-requests)   
    * [curl](#curl)   
    * [Logs](#logs)   
* [Examples](#examples)   
* [Test](#test)   
* [Deployment Scenario](#deployment-scenario)   
* [TODO](#todo)   
* [License](#license)   
* [Comments](#comments)   
* [Authors](#authors)   


## Features

* Returns all monitor measurements (`<API-URL>/measurements/all`)
* Returns monitor measurements between two specified datetimes (`<API-URL>/measurements`)

## Installation

```shell script
git clone git@gitlab.com:infoxel/welo-api-es.git
cd welo-api-es
python3 -m venv apies
source apies/bin/activate
pip install -r requirements.txt
# create an empty logs file
touch app/resources/logs/apies.log
# edit .env file with elasticsearch host and indexes
mv app/.env.example app/.env
nano app/.env
```

```.env
ES_HOST=<welo-elasticsearch-host>
ES_MON_INDEX=<monitor-index>
# ES_TEXT_INDEX=<text-index>
``` 

## Python version
` 3.8.8`

## Usage

### Run the APIes

```shell script
python main.py --ip 127.0.0.1 --port 8080
```

### Current checkpoints

* **'<API-URL>/measurements/all'**: Returns all monitor measurements.
* **'<API-URL>/measurements**: Returns monitor measurements between two specified dates *(see requests)*.
* **'<API-URL>/text'**: Returns welo text between two specified dates *(see requests)*.

### Model requests

* **Measurements requests**:
```python
{"start_time": str, # "YYYY-MM-DDThh:mm:ss+00:00" 
 "stop_time": str} # "YYYY-MM-DDThh:mm:ss+00:00"
```

* **Text requests** *(in process)*:
```python
{
 "channel_id": str, # "welo-channel-to-search-in"
 "start_time": str, # "YYYY-MM-DDThh:mm:ss+00:00" 
 "stop_time": str, # "YYYY-MM-DDThh:mm:ss+00:00"
 "text": str, # text-to-search"
}
```

### Model responses
```python
{"code": int, #(HTTP status code(200 or 404)
 "description": str,
 "data": {"response": {"search_value": str,
                       "hits": [{
                                 "searched_timestamp": str, #timestamp (microseconds)
                                 "previuos": str, 
				                 "next": str
				                }],
					   "total_responses": int
					  }
         }
}
```

### python requests
```python
import requests

response = requests.get('<API-URL>/measurements/all')
response.json()


# post requests with required body
json_request = {
                "start_time": '<YYYY-MM-DDThh:mm:ss+00:00>', 
                "stop_time": '<YYYY-MM-DDThh:mm:ss+00:00>'
               }
response = requests.post('<API-URL>/measurements', json=json_request)         
```

### curl
```shell script
$ curl -X GET '<API-URL>/endpoint'
$ curl -X POST '<API-URL>/words' -d '{"channel_id": "<welo-channel-to-search-in>", "start_time": "<YYYY-MM-DDThh:mm:ss+00:00>", "stop_time": "<YYYY-MM-DDThh:mm:ss+00:00>", "text": "<text-to-search>"
}'

```

### Logs

Useful log messages will be written in `app/app/resources/logs/apies.log`

## Examples

```shell script
$ curl -X POST http://127.0.0.1:8000/measurements -d '{"start_time": "2021-03-15T00:59:27.021995+00:00", "stop_time": "2021-03-15T00:59:27.021995+00:00"}'
{"code":200,"description":"measurements found in range 2021-03-15T00:59:27.021995+00:00 to 2021-03-15T00:59:27.021995+00:00","data":{"took":0,"timed_out":false,"_shards":{"total":1,"successful":1,"skipped":0,"failed":0},"hits":{"total":{"value":1,"relation":"eq"},"max_score":1.0,"hits":[{"_index":"monitor","_type":"_doc","_id":"3JZlM3gBJpF2A6CGGbva","_score":1.0,"_source":{"measurement_time":"2021-03-15T00:59:27.021995+00:00","measurement_type":"memory_log","machine_name":"downloader_4","value":22.3}}]}}}%    
```

```python
import requests
time_range = {
              "start_time": "2021-03-15T00:59:27.021995+00:00", 
              "stop_time": "2021-03-15T00:59:27.296794+00:00"
            }
response = requests.post('http://127.0.0.1:8000/measurements/', json=time_range)
response.json()
```

```json
{"code": 200,
 "description": "measurements found in range 2021-03-15T00:59:27.021995+00:00 to 2021-03-15T00:59:27.296794+00:00",
 "data": {"took": 0,
  "timed_out": "False",
  "_shards": {"total": 1, "successful": 1, "skipped": 0, "failed": 0},
  "hits": {"total": {"value": 3, "relation": "eq"},
   "max_score": 1.0,
   "hits": [{"_index": "monitor",
     "_type": "_doc",
     "_id": "3JZlM3gBJpF2A6CGGbva",
     "_score": 1.0,
     "_source": {"measurement_time": "2021-03-15T00:59:27.021995+00:00",
      "measurement_type": "memory_log",
      "machine_name": "downloader_4",
      "value": 22.3}},
    {"_index": "monitor",
     "_type": "_doc",
     "_id": "3ZZlM3gBJpF2A6CGG7tW",
     "_score": 1.0,
     "_source": {"measurement_time": "2021-03-15T00:59:27.296794+00:00",
      "measurement_type": "memory_log",
      "machine_name": "downloader_2",
      "value": 21.7}},
    {"_index": "monitor",
     "_type": "_doc",
     "_id": "JpZtM3gBJpF2A6CG676R",
     "_score": 1.0,
     "_source": {"measurement_time": "2021-03-15T00:59:27.183978+00:00",
      "measurement_type": "memory_log",
      "machine_name": "rtmp_2",
      "value": 3.5}}]}}}
```

## Test

*TODO*

## Deployment scenario

A beta version of APIes is now running in `unstable test` GCloud machine.

* **ssh command**: `gcloud beta compute ssh --zone "us-central1-a" "unstable-test" --project "welo-app"`
* **logs path**: `/home/bibo/apies/app/resources/logs/apies.log`

## TODO

-[ ] tests  
-[ ] create elasticsearch text requests index  
-[ ] define processing text logic 

## License
[MIT](<https://choosealicense.com/licenses/mit/>)

## Comments

* Logs in `apies.log` would be interesting to recover and process statistics data like *the most searched text*.
* The curated info could be visualised with *grafana*

## Authors

Bibiana Rivadaneira