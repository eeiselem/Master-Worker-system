 distributed master-worker paradigm for distributed execution of tasks and answering queries

  one or more client programs (hereafter "client") communicate with a "master" process and pass their queries to the master. The query here refers to a client asking about an individual person by their name and other attributes. In that, the system stores information about an individual's name, residence location, and year of residence in a "data table"

  The query can be either by name or by location or year, in which the master responds with all data items that satisfy the query.

In finer details, the master receives a query from the client but does not actually respond to the query itself, instead, it passes the query to one of the two workers (call them worker 1 and worker 2). To balance the load across the workers, the master splits the workload equally: if the query contains a name that starts with a letter from a to m (all names are in lowercase), it is forwarded to worker 1; otherwise, it is forwarded to worker 2. That means worker 1 handles a-m and worker 2 handles n-z. When the results are returned from the respective worker, the master combines them and returns them as a list to the client.

use RPC as the mode of communication across client, master, and worker and the data format across processes will be JSON

for handling queries with location and year, the query goes to both the workers

Two separate JSON data files (data-am.json and data-nz.json) are given that will be loaded by the respective worker to store in their data table. The master process will not contain any data. 

The client program is rather simple. It makes a set of RPC calls to the master asking for individual persons by name, by name, and by year. A sample client program (client.py) is given to test your code

Also handles error cases and failure cases
