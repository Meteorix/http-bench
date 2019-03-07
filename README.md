# http-bench

http server benchmark

* python wsgi (with rapidjson)
* python flask (with rapidjson)
* go gin

# benchmark tool

wrk: https://github.com/wg/wrk


```shell
./wrk -t2 -d10s -c200 http://127.0.0.1:5000/json
```

# env

```
SMP Debian 4.9.51-1 (2017-09-28) x86_64 GNU/Linux
cpu cores: 4
cpu MHz: 2397.222
MemTotal: 8GB
```

# cases:

* json response
* ...

# result

||Latency|Req/Sec|
|---|--|--|
|py_wsgi|1.61ms|117116|
|py_flask|9.89ms|20292|
|go_gin|3.37ms|81473|