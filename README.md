# dbhasher

Generates checksums for database tables and queries


# Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .


# Usage

To use it:

    $ dbhash --help



# requirements for testing

- postgresql 9.3 or higher
- create a user named 'dbhashuser' with superuser rights
- create the world database template:
    - create database named 'world_template' (any ownner)
    - import the world database into the template database, e.g.
        ```psql postgres dbhashuser < tests/resources/world.sql```

# Todo

- script for creating dbhashuser that has rights to create schema
