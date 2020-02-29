# WoltApi
An api to return restaurants nearby in 3km with search key

## How to run
Create venv 
```bash
python3 -m venv venv
```

Run venv
```bash
source venv/bin/activate
```

Install packages
```bash
pip install -r requirements.txt
```

Run Flask
```bash
python searchNearbyAPI.py 
```

Get search by curl or URL in your browser
```bash
curl -X GET  "http://127.0.0.1:5000/search-nearby?q=burger&lat=24.9400752782822&lon=60.2001494897883"
```
## Learning outcome
-Making API fast with Flask  
-Writing tests  
-Making basic stupid mistake: not use lowercase to compare strings
