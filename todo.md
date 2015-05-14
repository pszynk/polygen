
#### TODO: python random data generator (with tokens)

##### Input:

* FILE OUTPUT OPTIONS
    * file count (files to generate)      | 1
    * minimal file length                 | 200 bytes
    * maximal file length                 | 200
    * file name                           | type\_nr.dat
    * overrite files?                     | no

* payload type                        | must be set (can have additional parameters?)
* random data generation method       | /dev/urandom (can have additional parameters?)
    * urandom
    * seeded random
    * cuts from files + random

* helper options
    * logging (verbose, debug, file?)     | none
    * special fromfile_prefix_chars       | @
    * save arguments to file (new lines!) | no default

##### Output:

File with header and binary data. Format:

Date: (data)
Type: (data type)
Version: (version of this data type)
Tokens: (list of tokens) ? format with binary (\x##, or \x## if not human readable)
Content: (how data is generated)
Random\_method: how random data was generated

\_\_BINARY\_DATA\_\_ <- after this starts binary data


##### Project:

classes: 
* Header -> all the metadata
* RandomGenerator(sth) -> method generate(length) of random data
* TypeGenerator(RandomGenrator, sth) -> generator for each class
  * takes random generator
  * returns flow of that type of length N
  * should set metadata (pr. should have static params, but not date, and random method)?
* function parsing input
* type generator can parse own input
* random generator can parse own input
* function writing random generated flows to files
