# Copyright 2016 Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test fixtures."""


DDL = """\
CREATE TABLE contacts (
    contact_id INT64,
    first_name STRING(1024),
    last_name STRING(1024),
    email STRING(1024) )
    PRIMARY KEY (contact_id);
CREATE TABLE contact_phones (
    contact_id INT64,
    phone_type STRING(1024),
    phone_number STRING(1024) )
    PRIMARY KEY (contact_id, phone_type),
    INTERLEAVE IN PARENT contacts ON DELETE CASCADE;
CREATE TABLE all_types (
    pkey INT64 NOT NULL,
    int_value INT64,
    int_array ARRAY<INT64>,
    bool_value BOOL,
    bool_array ARRAY<BOOL>,
    bytes_value BYTES(16),
    bytes_array ARRAY<BYTES(16)>,
    date_value DATE,
    date_array ARRAY<DATE>,
    float_value FLOAT64,
    float_array ARRAY<FLOAT64>,
    string_value STRING(16),
    string_array ARRAY<STRING(16)>,
    timestamp_value TIMESTAMP,
    timestamp_array ARRAY<TIMESTAMP>,
    numeric_value NUMERIC,
    numeric_array ARRAY<NUMERIC>,
    json_value JSON,
    json_array ARRAY<JSON>,
    )
    PRIMARY KEY (pkey);
CREATE TABLE counters (
    name STRING(1024),
    value INT64 )
    PRIMARY KEY (name);
CREATE TABLE string_plus_array_of_string (
    id INT64,
    name STRING(16),
    tags ARRAY<STRING(16)> )
    PRIMARY KEY (id);
CREATE INDEX name ON contacts(first_name, last_name);
CREATE TABLE users_history (
     id INT64 NOT NULL,
     commit_ts TIMESTAMP NOT NULL OPTIONS
        (allow_commit_timestamp=true),
     name STRING(MAX) NOT NULL,
     email STRING(MAX),
     deleted BOOL NOT NULL )
     PRIMARY KEY(id, commit_ts DESC);
CREATE PROTO BUNDLE (
    spanner.examples.music.SingerInfo,
    spanner.examples.music.Genre,
    );
CREATE TABLE Types (
    RowID		INT64 NOT NULL,
    Int64a		INT64,
    Bytes		BYTES(MAX),
    Int64Array	ARRAY<INT64>,
    BytesArray	ARRAY<BYTES(MAX)>,
    ProtoMessage    spanner.examples.music.SingerInfo,
    ProtoEnum   spanner.examples.music.Genre,
    ProtoMessageArray   ARRAY<spanner.examples.music.SingerInfo>,
    ProtoEnumArray  ARRAY<spanner.examples.music.Genre>, ) 
    PRIMARY KEY (RowID);
CREATE TABLE Singers (
     SingerId   INT64 NOT NULL,
     FirstName  STRING(1024),
     LastName   STRING(1024),
     SingerInfo spanner.examples.music.SingerInfo,
     SingerGenre spanner.examples.music.Genre, )
     PRIMARY KEY (SingerId);
CREATE INDEX SingerByGenre ON Singers(SingerGenre) STORING (FirstName, LastName);
"""

EMULATOR_DDL = """\
CREATE TABLE contacts (
    contact_id INT64,
    first_name STRING(1024),
    last_name STRING(1024),
    email STRING(1024) )
    PRIMARY KEY (contact_id);
CREATE TABLE contact_phones (
    contact_id INT64,
    phone_type STRING(1024),
    phone_number STRING(1024) )
    PRIMARY KEY (contact_id, phone_type),
    INTERLEAVE IN PARENT contacts ON DELETE CASCADE;
CREATE TABLE all_types (
    pkey INT64 NOT NULL,
    int_value INT64,
    int_array ARRAY<INT64>,
    bool_value BOOL,
    bool_array ARRAY<BOOL>,
    bytes_value BYTES(16),
    bytes_array ARRAY<BYTES(16)>,
    date_value DATE,
    date_array ARRAY<DATE>,
    float_value FLOAT64,
    float_array ARRAY<FLOAT64>,
    string_value STRING(16),
    string_array ARRAY<STRING(16)>,
    timestamp_value TIMESTAMP,
    timestamp_array ARRAY<TIMESTAMP>)
    PRIMARY KEY (pkey);
CREATE TABLE counters (
    name STRING(1024),
    value INT64 )
    PRIMARY KEY (name);
CREATE TABLE string_plus_array_of_string (
    id INT64,
    name STRING(16),
    tags ARRAY<STRING(16)> )
    PRIMARY KEY (id);
CREATE INDEX name ON contacts(first_name, last_name);
CREATE TABLE users_history (
     id INT64 NOT NULL,
     commit_ts TIMESTAMP NOT NULL OPTIONS
        (allow_commit_timestamp=true),
     name STRING(MAX) NOT NULL,
     email STRING(MAX),
     deleted BOOL NOT NULL )
     PRIMARY KEY(id, commit_ts DESC);
"""

PG_DDL = """\
CREATE TABLE contacts (
    contact_id BIGINT,
    first_name VARCHAR(1024),
    last_name VARCHAR(1024),
    email VARCHAR(1024),
    PRIMARY KEY (contact_id) );
CREATE TABLE all_types (
    pkey BIGINT NOT NULL,
    int_value INT,
    int_array INT[],
    bool_value BOOL,
    bool_array BOOL[],
    bytes_value BYTEA,
    bytes_array BYTEA[],
    float_value DOUBLE PRECISION,
    float_array DOUBLE PRECISION[],
    string_value VARCHAR(16),
    string_array VARCHAR(16)[],
    date_value DATE,
    date_array DATE[],
    timestamp_value TIMESTAMPTZ,
    timestamp_array TIMESTAMPTZ[],
    numeric_value NUMERIC,
    numeric_array NUMERIC[],
    jsonb_value JSONB,
    jsonb_array JSONB[],
    PRIMARY KEY (pkey) );
CREATE TABLE counters (
    name VARCHAR(1024),
    value BIGINT,
    PRIMARY KEY (name));
CREATE TABLE string_plus_array_of_string (
    id BIGINT,
    name VARCHAR(16),
    PRIMARY KEY (id));
CREATE INDEX name ON contacts(first_name, last_name);
"""

PROTO_COLUMNS_DDL = """\
CREATE PROTO BUNDLE (
    spanner.examples.music.SingerInfo,
    spanner.examples.music.Genre,
    );
CREATE TABLE Singers (
     SingerId   INT64 NOT NULL,
     FirstName  STRING(1024),
     LastName   STRING(1024),
     SingerInfo spanner.examples.music.SingerInfo,
     SingerGenre spanner.examples.music.Genre, )
     PRIMARY KEY (SingerId);
"""

DDL_STATEMENTS = [stmt.strip() for stmt in DDL.split(";") if stmt.strip()]
EMULATOR_DDL_STATEMENTS = [
    stmt.strip() for stmt in EMULATOR_DDL.split(";") if stmt.strip()
]
PG_DDL_STATEMENTS = [stmt.strip() for stmt in PG_DDL.split(";") if stmt.strip()]
PROTO_COLUMNS_DDL_STATEMENTS = [
    stmt.strip() for stmt in PROTO_COLUMNS_DDL.split(";") if stmt.strip()
]
