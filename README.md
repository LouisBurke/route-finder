# Boxever Code Challenge Submission

## Approach

The approach I took was to take the routes and their connections, as provided in the challenge
and load them into a simple graph. The graph neatly fits into a python dictionary that takes the following
form.

```python
{
    'TEST': [('TEST1', 4)], 
    'OTH': [('OTH1', 6)], 'BOS': [], 'OTH1': [('BOS', 7)], 
    'TEST2': [('BOS', 6)], 
    'TEST1': [('TEST2', 5)], 
    'DUB': [('TEST', 3), ('OTH', 5), ('BOS', 1)]
}
```

Each airport has a key in the dictionary and list of connections and cost in terms of hours to get to each one.

## Usage

The solution is written in Python 3.9 and has one dependency, namely Click.

`pip install click`

An example of how to run:

`python route_finder.py --source 'DUB' --destination 'BOS' --routes 'times.csv'`

In the above example `--routes` needs to be a csv with the following format:

```csv
DUB,LHR,1
DUB,CDG,2
CDG,BOS,6
CDG,BKK,9
ORD,LAS,2
LHR,NYC,5
NYC,LAS,3
BOS,LAX,4
LHR,BKK,9
BKK,SYD,11
LAX,LAS,2
DUB,ORD,6
LAX,SYD,13
LAS,SYD,14
DUB,TEST,3
```

## Tests

There are two main functions for which I've added unit tests. To execute the tests run the following in the same location
as `route_finder.py`

`python test_route_finder.py`
