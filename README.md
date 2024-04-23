# gippo
Gippo is a python tool that uses the API of `iplocation.net` to retrieve information about a given IP address such as originating country, country code and ISP.
The returned information is stored in a table for easy readibility.

```sh
$ python3 main.py -i 8.8.8.8

    dBBBBb  dBP dBBBBBb dBBBBBb  dBBBBP
                    dB'     dB' dBP.BP 
  dBBBB   dBP   dBBBP'  dBBBP' dBP.BP  
 dB' BB  dBP   dBP     dBP    dBP.BP   
dBBBBBB dBP   dBP     dBP    dBBBBP     @Kr0ff
   
gippo - Retrieve information about a given IP address from "iplocation.net"
    
+------------+-----------------+---------+--------------------------+--------------+------------+--------------------+-------------------+
| IP Address | IP Number (Int) | IP Type |         Country          | Country Code |    ISP     | HTTP Response Code | HTTP Response Msg |
+------------+-----------------+---------+--------------------------+--------------+------------+--------------------+-------------------+
|  8.8.8.8   |    134744072    |    4    | United States of America |      US      | Google LLC |        200         |         OK        |
+------------+-----------------+---------+--------------------------+--------------+------------+--------------------+-------------------+
```

# Dependencies
- argparse
- prettytable
- requests

```sh
python3 -m pip install argparse prettytable requests
```
