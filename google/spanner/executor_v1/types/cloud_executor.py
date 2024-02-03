# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore
from google.spanner.admin.database.v1 import backup_pb2  # type: ignore
from google.spanner.admin.database.v1 import common_pb2  # type: ignore
from google.spanner.admin.database.v1 import spanner_database_admin_pb2  # type: ignore
from google.spanner.admin.instance.v1 import spanner_instance_admin_pb2  # type: ignore
from google.spanner.v1 import spanner_pb2  # type: ignore
from google.spanner.v1 import type_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.spanner.executor.v1",
    manifest={
        "SpannerAsyncActionRequest",
        "SpannerAsyncActionResponse",
        "SpannerAction",
        "ReadAction",
        "QueryAction",
        "DmlAction",
        "BatchDmlAction",
        "Value",
        "KeyRange",
        "KeySet",
        "ValueList",
        "MutationAction",
        "WriteMutationsAction",
        "PartitionedUpdateAction",
        "StartTransactionAction",
        "Concurrency",
        "TableMetadata",
        "ColumnMetadata",
        "TransactionExecutionOptions",
        "FinishTransactionAction",
        "AdminAction",
        "CreateUserInstanceConfigAction",
        "UpdateUserInstanceConfigAction",
        "GetCloudInstanceConfigAction",
        "DeleteUserInstanceConfigAction",
        "ListCloudInstanceConfigsAction",
        "CreateCloudInstanceAction",
        "UpdateCloudInstanceAction",
        "DeleteCloudInstanceAction",
        "CreateCloudDatabaseAction",
        "UpdateCloudDatabaseDdlAction",
        "UpdateCloudDatabaseAction",
        "DropCloudDatabaseAction",
        "ReconfigureCloudDatabaseAction",
        "ListCloudDatabasesAction",
        "ListCloudInstancesAction",
        "GetCloudInstanceAction",
        "ListCloudDatabaseOperationsAction",
        "RestoreCloudDatabaseAction",
        "GetCloudDatabaseAction",
        "CreateCloudBackupAction",
        "CopyCloudBackupAction",
        "GetCloudBackupAction",
        "UpdateCloudBackupAction",
        "DeleteCloudBackupAction",
        "ListCloudBackupsAction",
        "ListCloudBackupOperationsAction",
        "GetOperationAction",
        "CancelOperationAction",
        "StartBatchTransactionAction",
        "CloseBatchTransactionAction",
        "GenerateDbPartitionsForReadAction",
        "GenerateDbPartitionsForQueryAction",
        "BatchPartition",
        "ExecutePartitionAction",
        "ExecuteChangeStreamQuery",
        "SpannerActionOutcome",
        "AdminResult",
        "CloudBackupResponse",
        "OperationResponse",
        "CloudInstanceResponse",
        "CloudInstanceConfigResponse",
        "CloudDatabaseResponse",
        "ReadResult",
        "QueryResult",
        "ChangeStreamRecord",
        "DataChangeRecord",
        "ChildPartitionsRecord",
        "HeartbeatRecord",
    },
)


class SpannerAsyncActionRequest(proto.Message):
    r"""Request to executor service that start a new Spanner action.

    Attributes:
        action_id (int):
            Action id to uniquely identify this action
            request.
        action (google.spanner.executor_v1.types.SpannerAction):
            The actual SpannerAction to perform.
    """

    action_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    action: "SpannerAction" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SpannerAction",
    )


class SpannerAsyncActionResponse(proto.Message):
    r"""Response from executor service.

    Attributes:
        action_id (int):
            Action id corresponds to the request.
        outcome (google.spanner.executor_v1.types.SpannerActionOutcome):
            If action results are split into multiple
            responses, only the last response can and should
            contain status.
    """

    action_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    outcome: "SpannerActionOutcome" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SpannerActionOutcome",
    )


class SpannerAction(proto.Message):
    r"""SpannerAction defines a primitive action that can be
    performed against Spanner, such as begin or commit a
    transaction, or perform a read or mutation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        database_path (str):
            Database against which to perform action.
            In a context where a series of actions take
            place, an action may omit database path if it
            applies to the same database as the previous
            action.
        start (google.spanner.executor_v1.types.StartTransactionAction):
            Action to start a transaction.

            This field is a member of `oneof`_ ``action``.
        finish (google.spanner.executor_v1.types.FinishTransactionAction):
            Action to finish a transaction.

            This field is a member of `oneof`_ ``action``.
        read (google.spanner.executor_v1.types.ReadAction):
            Action to do a normal read.

            This field is a member of `oneof`_ ``action``.
        query (google.spanner.executor_v1.types.QueryAction):
            Action to do a query.

            This field is a member of `oneof`_ ``action``.
        mutation (google.spanner.executor_v1.types.MutationAction):
            Action to buffer a mutation.

            This field is a member of `oneof`_ ``action``.
        dml (google.spanner.executor_v1.types.DmlAction):
            Action to a DML.

            This field is a member of `oneof`_ ``action``.
        batch_dml (google.spanner.executor_v1.types.BatchDmlAction):
            Action to a batch DML.

            This field is a member of `oneof`_ ``action``.
        write (google.spanner.executor_v1.types.WriteMutationsAction):
            Action to write a mutation.

            This field is a member of `oneof`_ ``action``.
        partitioned_update (google.spanner.executor_v1.types.PartitionedUpdateAction):
            Action to a partitioned update.

            This field is a member of `oneof`_ ``action``.
        admin (google.spanner.executor_v1.types.AdminAction):
            Action that contains any administrative
            operation, like database, instance manipulation.

            This field is a member of `oneof`_ ``action``.
        start_batch_txn (google.spanner.executor_v1.types.StartBatchTransactionAction):
            Action to start a batch transaction.

            This field is a member of `oneof`_ ``action``.
        close_batch_txn (google.spanner.executor_v1.types.CloseBatchTransactionAction):
            Action to close a batch transaction.

            This field is a member of `oneof`_ ``action``.
        generate_db_partitions_read (google.spanner.executor_v1.types.GenerateDbPartitionsForReadAction):
            Action to generate database partitions for
            batch read.

            This field is a member of `oneof`_ ``action``.
        generate_db_partitions_query (google.spanner.executor_v1.types.GenerateDbPartitionsForQueryAction):
            Action to generate database partitions for
            batch query.

            This field is a member of `oneof`_ ``action``.
        execute_partition (google.spanner.executor_v1.types.ExecutePartitionAction):
            Action to execute batch actions on generated
            partitions.

            This field is a member of `oneof`_ ``action``.
        execute_change_stream_query (google.spanner.executor_v1.types.ExecuteChangeStreamQuery):
            Action to execute change stream query.

            This field is a member of `oneof`_ ``action``.
    """

    database_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    start: "StartTransactionAction" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="action",
        message="StartTransactionAction",
    )
    finish: "FinishTransactionAction" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="action",
        message="FinishTransactionAction",
    )
    read: "ReadAction" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="action",
        message="ReadAction",
    )
    query: "QueryAction" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="action",
        message="QueryAction",
    )
    mutation: "MutationAction" = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="action",
        message="MutationAction",
    )
    dml: "DmlAction" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="action",
        message="DmlAction",
    )
    batch_dml: "BatchDmlAction" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="action",
        message="BatchDmlAction",
    )
    write: "WriteMutationsAction" = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="action",
        message="WriteMutationsAction",
    )
    partitioned_update: "PartitionedUpdateAction" = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="action",
        message="PartitionedUpdateAction",
    )
    admin: "AdminAction" = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="action",
        message="AdminAction",
    )
    start_batch_txn: "StartBatchTransactionAction" = proto.Field(
        proto.MESSAGE,
        number=40,
        oneof="action",
        message="StartBatchTransactionAction",
    )
    close_batch_txn: "CloseBatchTransactionAction" = proto.Field(
        proto.MESSAGE,
        number=41,
        oneof="action",
        message="CloseBatchTransactionAction",
    )
    generate_db_partitions_read: "GenerateDbPartitionsForReadAction" = proto.Field(
        proto.MESSAGE,
        number=42,
        oneof="action",
        message="GenerateDbPartitionsForReadAction",
    )
    generate_db_partitions_query: "GenerateDbPartitionsForQueryAction" = proto.Field(
        proto.MESSAGE,
        number=43,
        oneof="action",
        message="GenerateDbPartitionsForQueryAction",
    )
    execute_partition: "ExecutePartitionAction" = proto.Field(
        proto.MESSAGE,
        number=44,
        oneof="action",
        message="ExecutePartitionAction",
    )
    execute_change_stream_query: "ExecuteChangeStreamQuery" = proto.Field(
        proto.MESSAGE,
        number=50,
        oneof="action",
        message="ExecuteChangeStreamQuery",
    )


class ReadAction(proto.Message):
    r"""A single read request.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        table (str):
            The table to read at.
        index (str):
            The index to read at if it's an index read.

            This field is a member of `oneof`_ ``_index``.
        column (MutableSequence[str]):
            List of columns must begin with the key
            columns used for the read.
        keys (google.spanner.executor_v1.types.KeySet):
            Keys for performing this read.
        limit (int):
            Limit on number of rows to read. If set, must
            be positive.
    """

    table: str = proto.Field(
        proto.STRING,
        number=1,
    )
    index: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    column: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    keys: "KeySet" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="KeySet",
    )
    limit: int = proto.Field(
        proto.INT32,
        number=5,
    )


class QueryAction(proto.Message):
    r"""A SQL query request.

    Attributes:
        sql (str):
            The SQL string.
        params (MutableSequence[google.spanner.executor_v1.types.QueryAction.Parameter]):
            Parameters for the SQL string.
    """

    class Parameter(proto.Message):
        r"""Parameter that bind to placeholders in the SQL string

        Attributes:
            name (str):
                Name of the parameter (with no leading @).
            type_ (google.spanner.v1.type_pb2.Type):
                Type of the parameter.
            value (google.spanner.executor_v1.types.Value):
                Value of the parameter.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: type_pb2.Type = proto.Field(
            proto.MESSAGE,
            number=2,
            message=type_pb2.Type,
        )
        value: "Value" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Value",
        )

    sql: str = proto.Field(
        proto.STRING,
        number=1,
    )
    params: MutableSequence[Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Parameter,
    )


class DmlAction(proto.Message):
    r"""A single DML statement.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        update (google.spanner.executor_v1.types.QueryAction):
            DML statement.
        autocommit_if_supported (bool):
            Whether to autocommit the transaction after
            executing the DML statement, if the Executor
            supports autocommit.

            This field is a member of `oneof`_ ``_autocommit_if_supported``.
    """

    update: "QueryAction" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="QueryAction",
    )
    autocommit_if_supported: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class BatchDmlAction(proto.Message):
    r"""Batch of DML statements invoked using batched execution.

    Attributes:
        updates (MutableSequence[google.spanner.executor_v1.types.QueryAction]):
            DML statements.
    """

    updates: MutableSequence["QueryAction"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="QueryAction",
    )


class Value(proto.Message):
    r"""Value represents a single value that can be read or written
    to/from Spanner.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        is_null (bool):
            If is_null is set, then this value is null.

            This field is a member of `oneof`_ ``value_type``.
        int_value (int):
            Int type value. It's used for all integer
            number types, like int32 and int64.

            This field is a member of `oneof`_ ``value_type``.
        bool_value (bool):
            Bool type value.

            This field is a member of `oneof`_ ``value_type``.
        double_value (float):
            Double type value. It's used for all float
            point types, like float and double.

            This field is a member of `oneof`_ ``value_type``.
        bytes_value (bytes):
            Bytes type value, stored in CORD. It's also
            used for PROTO type value.

            This field is a member of `oneof`_ ``value_type``.
        string_value (str):
            String type value, stored in CORD.

            This field is a member of `oneof`_ ``value_type``.
        struct_value (google.spanner.executor_v1.types.ValueList):
            Struct type value. It contains a ValueList
            representing the values in this struct.

            This field is a member of `oneof`_ ``value_type``.
        timestamp_value (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp type value.

            This field is a member of `oneof`_ ``value_type``.
        date_days_value (int):
            Date type value. Date is specified as a
            number of days since Unix epoch.

            This field is a member of `oneof`_ ``value_type``.
        is_commit_timestamp (bool):
            If set, holds the sentinel value for the
            transaction CommitTimestamp.

            This field is a member of `oneof`_ ``value_type``.
        array_value (google.spanner.executor_v1.types.ValueList):
            Array type value. The underlying Valuelist
            should have values that have the same type.

            This field is a member of `oneof`_ ``value_type``.
        array_type (google.spanner.v1.type_pb2.Type):
            Type of array element. Only set if value is
            an array.

            This field is a member of `oneof`_ ``_array_type``.
    """

    is_null: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="value_type",
    )
    int_value: int = proto.Field(
        proto.INT64,
        number=2,
        oneof="value_type",
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=3,
        oneof="value_type",
    )
    double_value: float = proto.Field(
        proto.DOUBLE,
        number=4,
        oneof="value_type",
    )
    bytes_value: bytes = proto.Field(
        proto.BYTES,
        number=5,
        oneof="value_type",
    )
    string_value: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="value_type",
    )
    struct_value: "ValueList" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="value_type",
        message="ValueList",
    )
    timestamp_value: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="value_type",
        message=timestamp_pb2.Timestamp,
    )
    date_days_value: int = proto.Field(
        proto.INT32,
        number=9,
        oneof="value_type",
    )
    is_commit_timestamp: bool = proto.Field(
        proto.BOOL,
        number=10,
        oneof="value_type",
    )
    array_value: "ValueList" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="value_type",
        message="ValueList",
    )
    array_type: type_pb2.Type = proto.Field(
        proto.MESSAGE,
        number=12,
        optional=True,
        message=type_pb2.Type,
    )


class KeyRange(proto.Message):
    r"""KeyRange represents a range of rows in a table or index.

    A range has a start key and an end key. These keys can be open
    or closed, indicating if the range includes rows with that key.

    Keys are represented by "ValueList", where the ith value in the
    list corresponds to the ith component of the table or index
    primary key.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start (google.spanner.executor_v1.types.ValueList):
            "start" and "limit" must have the same number
            of key parts, though they may name only a prefix
            of the table or index key. The start key of this
            KeyRange.
        limit (google.spanner.executor_v1.types.ValueList):
            The end key of this KeyRange.
        type_ (google.spanner.executor_v1.types.KeyRange.Type):
            "start" and "limit" type for this KeyRange.

            This field is a member of `oneof`_ ``_type``.
    """

    class Type(proto.Enum):
        r"""Type controls whether "start" and "limit" are open or closed.
        By default, "start" is closed, and "limit" is open.

        Values:
            TYPE_UNSPECIFIED (0):
                "TYPE_UNSPECIFIED" is equivalent to "CLOSED_OPEN".
            CLOSED_CLOSED (1):
                [start,limit]
            CLOSED_OPEN (2):
                [start,limit)
            OPEN_CLOSED (3):
                (start,limit]
            OPEN_OPEN (4):
                (start,limit)
        """
        TYPE_UNSPECIFIED = 0
        CLOSED_CLOSED = 1
        CLOSED_OPEN = 2
        OPEN_CLOSED = 3
        OPEN_OPEN = 4

    start: "ValueList" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ValueList",
    )
    limit: "ValueList" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ValueList",
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=Type,
    )


class KeySet(proto.Message):
    r"""KeySet defines a collection of Spanner keys and/or key
    ranges. All the keys are expected to be in the same table. The
    keys need not be sorted in any particular way.

    Attributes:
        point (MutableSequence[google.spanner.executor_v1.types.ValueList]):
            A list of specific keys. Entries in "keys"
            should have exactly as many elements as there
            are columns in the primary or index key with
            which this "KeySet" is used.
        range_ (MutableSequence[google.spanner.executor_v1.types.KeyRange]):
            A list of key ranges.
        all_ (bool):
            For convenience "all" can be set to "true" to
            indicate that this "KeySet" matches all keys in
            the table or index. Note that any keys specified
            in "keys" or "ranges" are only yielded once.
    """

    point: MutableSequence["ValueList"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ValueList",
    )
    range_: MutableSequence["KeyRange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="KeyRange",
    )
    all_: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ValueList(proto.Message):
    r"""List of values.

    Attributes:
        value (MutableSequence[google.spanner.executor_v1.types.Value]):
            Values contained in this ValueList.
    """

    value: MutableSequence["Value"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Value",
    )


class MutationAction(proto.Message):
    r"""A single mutation request.

    Attributes:
        mod (MutableSequence[google.spanner.executor_v1.types.MutationAction.Mod]):
            Mods that contained in this mutation.
    """

    class InsertArgs(proto.Message):
        r"""Arguments to Insert, InsertOrUpdate, and Replace operations.

        Attributes:
            column (MutableSequence[str]):
                The names of the columns to be written.
            type_ (MutableSequence[google.spanner.v1.type_pb2.Type]):
                Type information for the "values" entries
                below.
            values (MutableSequence[google.spanner.executor_v1.types.ValueList]):
                The values to be written.
        """

        column: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        type_: MutableSequence[type_pb2.Type] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=type_pb2.Type,
        )
        values: MutableSequence["ValueList"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="ValueList",
        )

    class UpdateArgs(proto.Message):
        r"""Arguments to Update.

        Attributes:
            column (MutableSequence[str]):
                The columns to be updated. Identical to
                InsertArgs.column.
            type_ (MutableSequence[google.spanner.v1.type_pb2.Type]):
                Type information for "values". Identical to
                InsertArgs.type.
            values (MutableSequence[google.spanner.executor_v1.types.ValueList]):
                The values to be updated. Identical to
                InsertArgs.values.
        """

        column: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        type_: MutableSequence[type_pb2.Type] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=type_pb2.Type,
        )
        values: MutableSequence["ValueList"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="ValueList",
        )

    class Mod(proto.Message):
        r"""Mod represents the write action that will be perform to a table.
        Each mod will specify exactly one action, from insert, update,
        insert_or_update, replace and delete.

        Attributes:
            table (str):
                The table to write.
            insert (google.spanner.executor_v1.types.MutationAction.InsertArgs):
                Exactly one of the remaining elements may be
                present. Insert new rows into "table".
            update (google.spanner.executor_v1.types.MutationAction.UpdateArgs):
                Update columns stored in existing rows of
                "table".
            insert_or_update (google.spanner.executor_v1.types.MutationAction.InsertArgs):
                Insert or update existing rows of "table".
            replace (google.spanner.executor_v1.types.MutationAction.InsertArgs):
                Replace existing rows of "table".
            delete_keys (google.spanner.executor_v1.types.KeySet):
                Delete rows from "table".
        """

        table: str = proto.Field(
            proto.STRING,
            number=1,
        )
        insert: "MutationAction.InsertArgs" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="MutationAction.InsertArgs",
        )
        update: "MutationAction.UpdateArgs" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="MutationAction.UpdateArgs",
        )
        insert_or_update: "MutationAction.InsertArgs" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="MutationAction.InsertArgs",
        )
        replace: "MutationAction.InsertArgs" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="MutationAction.InsertArgs",
        )
        delete_keys: "KeySet" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="KeySet",
        )

    mod: MutableSequence[Mod] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Mod,
    )


class WriteMutationsAction(proto.Message):
    r"""WriteMutationAction defines an action of flushing the
    mutation so they are visible to subsequent operations in the
    transaction.

    Attributes:
        mutation (google.spanner.executor_v1.types.MutationAction):
            The mutation to write.
    """

    mutation: "MutationAction" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MutationAction",
    )


class PartitionedUpdateAction(proto.Message):
    r"""PartitionedUpdateAction defines an action to execute a
    partitioned DML which runs different partitions in parallel.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        options (google.spanner.executor_v1.types.PartitionedUpdateAction.ExecutePartitionedUpdateOptions):
            Options for partitioned update.

            This field is a member of `oneof`_ ``_options``.
        update (google.spanner.executor_v1.types.QueryAction):
            Partitioned dml query.
    """

    class ExecutePartitionedUpdateOptions(proto.Message):
        r"""

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            rpc_priority (google.spanner.v1.spanner_pb2.Priority):
                RPC Priority

                This field is a member of `oneof`_ ``_rpc_priority``.
            tag (str):
                Transaction tag

                This field is a member of `oneof`_ ``_tag``.
        """

        rpc_priority: spanner_pb2.RequestOptions.Priority = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=spanner_pb2.RequestOptions.Priority,
        )
        tag: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )

    options: ExecutePartitionedUpdateOptions = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message=ExecutePartitionedUpdateOptions,
    )
    update: "QueryAction" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QueryAction",
    )


class StartTransactionAction(proto.Message):
    r"""StartTransactionAction defines an action of initializing a
    transaction.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        concurrency (google.spanner.executor_v1.types.Concurrency):
            Concurrency is for read-only transactions and
            must be omitted for read-write transactions.

            This field is a member of `oneof`_ ``_concurrency``.
        table (MutableSequence[google.spanner.executor_v1.types.TableMetadata]):
            Metadata about tables and columns that will
            be involved in this transaction. It is to
            convert values of key parts correctly.
        transaction_seed (str):
            Transaction_seed contains workid and op pair for this
            transaction, used for testing.
        execution_options (google.spanner.executor_v1.types.TransactionExecutionOptions):
            Execution options (e.g., whether transaction
            is opaque, optimistic).

            This field is a member of `oneof`_ ``_execution_options``.
    """

    concurrency: "Concurrency" = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message="Concurrency",
    )
    table: MutableSequence["TableMetadata"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="TableMetadata",
    )
    transaction_seed: str = proto.Field(
        proto.STRING,
        number=3,
    )
    execution_options: "TransactionExecutionOptions" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="TransactionExecutionOptions",
    )


class Concurrency(proto.Message):
    r"""Concurrency for read-only transactions.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        staleness_seconds (float):
            Indicates a read at a consistent timestamp
            that is specified relative to now. That is, if
            the caller has specified an exact staleness of s
            seconds, we will read at now - s.

            This field is a member of `oneof`_ ``concurrency_mode``.
        min_read_timestamp_micros (int):
            Indicates a boundedly stale read that reads
            at a timestamp >= T.

            This field is a member of `oneof`_ ``concurrency_mode``.
        max_staleness_seconds (float):
            Indicates a boundedly stale read that is at
            most N seconds stale.

            This field is a member of `oneof`_ ``concurrency_mode``.
        exact_timestamp_micros (int):
            Indicates a read at a consistent timestamp.

            This field is a member of `oneof`_ ``concurrency_mode``.
        strong (bool):
            Indicates a strong read, must only be set to
            true, or unset.

            This field is a member of `oneof`_ ``concurrency_mode``.
        batch (bool):
            Indicates a batch read, must only be set to
            true, or unset.

            This field is a member of `oneof`_ ``concurrency_mode``.
        snapshot_epoch_read (bool):
            True if exact_timestamp_micros is set, and the chosen
            timestamp is that of a snapshot epoch.
        snapshot_epoch_root_table (str):
            If set, this is a snapshot epoch read
            constrained to read only the specified log scope
            root table, and its children. Will not be set
            for full database epochs.
        batch_read_timestamp_micros (int):
            Set only when batch is true.
    """

    staleness_seconds: float = proto.Field(
        proto.DOUBLE,
        number=1,
        oneof="concurrency_mode",
    )
    min_read_timestamp_micros: int = proto.Field(
        proto.INT64,
        number=2,
        oneof="concurrency_mode",
    )
    max_staleness_seconds: float = proto.Field(
        proto.DOUBLE,
        number=3,
        oneof="concurrency_mode",
    )
    exact_timestamp_micros: int = proto.Field(
        proto.INT64,
        number=4,
        oneof="concurrency_mode",
    )
    strong: bool = proto.Field(
        proto.BOOL,
        number=5,
        oneof="concurrency_mode",
    )
    batch: bool = proto.Field(
        proto.BOOL,
        number=6,
        oneof="concurrency_mode",
    )
    snapshot_epoch_read: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    snapshot_epoch_root_table: str = proto.Field(
        proto.STRING,
        number=8,
    )
    batch_read_timestamp_micros: int = proto.Field(
        proto.INT64,
        number=9,
    )


class TableMetadata(proto.Message):
    r"""TableMetadata contains metadata of a single table.

    Attributes:
        name (str):
            Table name.
        column (MutableSequence[google.spanner.executor_v1.types.ColumnMetadata]):
            Columns, in the same order as in the schema.
        key_column (MutableSequence[google.spanner.executor_v1.types.ColumnMetadata]):
            Keys, in order. Column name is currently not
            populated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    column: MutableSequence["ColumnMetadata"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ColumnMetadata",
    )
    key_column: MutableSequence["ColumnMetadata"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ColumnMetadata",
    )


class ColumnMetadata(proto.Message):
    r"""ColumnMetadata represents metadata of a single column.

    Attributes:
        name (str):
            Column name.
        type_ (google.spanner.v1.type_pb2.Type):
            Column type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: type_pb2.Type = proto.Field(
        proto.MESSAGE,
        number=2,
        message=type_pb2.Type,
    )


class TransactionExecutionOptions(proto.Message):
    r"""Options for executing the transaction.

    Attributes:
        optimistic (bool):
            Whether optimistic concurrency should be used
            to execute this transaction.
    """

    optimistic: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class FinishTransactionAction(proto.Message):
    r"""FinishTransactionAction defines an action of finishing a
    transaction.

    Attributes:
        mode (google.spanner.executor_v1.types.FinishTransactionAction.Mode):
            Defines how exactly the transaction should be
            completed, e.g. with commit or abortion.
    """

    class Mode(proto.Enum):
        r"""Mode indicates how the transaction should be finished.

        Values:
            MODE_UNSPECIFIED (0):
                "MODE_UNSPECIFIED" is equivalent to "COMMIT".
            COMMIT (1):
                Commit the transaction.
            ABANDON (2):
                Drop the transaction without committing it.
        """
        MODE_UNSPECIFIED = 0
        COMMIT = 1
        ABANDON = 2

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )


class AdminAction(proto.Message):
    r"""AdminAction defines all the cloud spanner admin actions,
    including instance/database admin ops, backup ops and operation
    actions.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        create_user_instance_config (google.spanner.executor_v1.types.CreateUserInstanceConfigAction):
            Action that creates a user instance config.

            This field is a member of `oneof`_ ``action``.
        update_user_instance_config (google.spanner.executor_v1.types.UpdateUserInstanceConfigAction):
            Action that updates a user instance config.

            This field is a member of `oneof`_ ``action``.
        delete_user_instance_config (google.spanner.executor_v1.types.DeleteUserInstanceConfigAction):
            Action that deletes a user instance config.

            This field is a member of `oneof`_ ``action``.
        get_cloud_instance_config (google.spanner.executor_v1.types.GetCloudInstanceConfigAction):
            Action that gets a user instance config.

            This field is a member of `oneof`_ ``action``.
        list_instance_configs (google.spanner.executor_v1.types.ListCloudInstanceConfigsAction):
            Action that lists user instance configs.

            This field is a member of `oneof`_ ``action``.
        create_cloud_instance (google.spanner.executor_v1.types.CreateCloudInstanceAction):
            Action that creates a Cloud Spanner instance.

            This field is a member of `oneof`_ ``action``.
        update_cloud_instance (google.spanner.executor_v1.types.UpdateCloudInstanceAction):
            Action that updates a Cloud Spanner instance.

            This field is a member of `oneof`_ ``action``.
        delete_cloud_instance (google.spanner.executor_v1.types.DeleteCloudInstanceAction):
            Action that deletes a Cloud Spanner instance.

            This field is a member of `oneof`_ ``action``.
        list_cloud_instances (google.spanner.executor_v1.types.ListCloudInstancesAction):
            Action that lists Cloud Spanner instances.

            This field is a member of `oneof`_ ``action``.
        get_cloud_instance (google.spanner.executor_v1.types.GetCloudInstanceAction):
            Action that retrieves a Cloud Spanner
            instance.

            This field is a member of `oneof`_ ``action``.
        create_cloud_database (google.spanner.executor_v1.types.CreateCloudDatabaseAction):
            Action that creates a Cloud Spanner database.

            This field is a member of `oneof`_ ``action``.
        update_cloud_database_ddl (google.spanner.executor_v1.types.UpdateCloudDatabaseDdlAction):
            Action that updates the schema of a Cloud
            Spanner database.

            This field is a member of `oneof`_ ``action``.
        update_cloud_database (google.spanner.executor_v1.types.UpdateCloudDatabaseAction):
            Action that updates the schema of a Cloud
            Spanner database.

            This field is a member of `oneof`_ ``action``.
        drop_cloud_database (google.spanner.executor_v1.types.DropCloudDatabaseAction):
            Action that drops a Cloud Spanner database.

            This field is a member of `oneof`_ ``action``.
        list_cloud_databases (google.spanner.executor_v1.types.ListCloudDatabasesAction):
            Action that lists Cloud Spanner databases.

            This field is a member of `oneof`_ ``action``.
        list_cloud_database_operations (google.spanner.executor_v1.types.ListCloudDatabaseOperationsAction):
            Action that lists Cloud Spanner database
            operations.

            This field is a member of `oneof`_ ``action``.
        restore_cloud_database (google.spanner.executor_v1.types.RestoreCloudDatabaseAction):
            Action that restores a Cloud Spanner database
            from a backup.

            This field is a member of `oneof`_ ``action``.
        get_cloud_database (google.spanner.executor_v1.types.GetCloudDatabaseAction):
            Action that gets a Cloud Spanner database.

            This field is a member of `oneof`_ ``action``.
        create_cloud_backup (google.spanner.executor_v1.types.CreateCloudBackupAction):
            Action that creates a Cloud Spanner database
            backup.

            This field is a member of `oneof`_ ``action``.
        copy_cloud_backup (google.spanner.executor_v1.types.CopyCloudBackupAction):
            Action that copies a Cloud Spanner database
            backup.

            This field is a member of `oneof`_ ``action``.
        get_cloud_backup (google.spanner.executor_v1.types.GetCloudBackupAction):
            Action that gets a Cloud Spanner database
            backup.

            This field is a member of `oneof`_ ``action``.
        update_cloud_backup (google.spanner.executor_v1.types.UpdateCloudBackupAction):
            Action that updates a Cloud Spanner database
            backup.

            This field is a member of `oneof`_ ``action``.
        delete_cloud_backup (google.spanner.executor_v1.types.DeleteCloudBackupAction):
            Action that deletes a Cloud Spanner database
            backup.

            This field is a member of `oneof`_ ``action``.
        list_cloud_backups (google.spanner.executor_v1.types.ListCloudBackupsAction):
            Action that lists Cloud Spanner database
            backups.

            This field is a member of `oneof`_ ``action``.
        list_cloud_backup_operations (google.spanner.executor_v1.types.ListCloudBackupOperationsAction):
            Action that lists Cloud Spanner database
            backup operations.

            This field is a member of `oneof`_ ``action``.
        get_operation (google.spanner.executor_v1.types.GetOperationAction):
            Action that gets an operation.

            This field is a member of `oneof`_ ``action``.
        cancel_operation (google.spanner.executor_v1.types.CancelOperationAction):
            Action that cancels an operation.

            This field is a member of `oneof`_ ``action``.
        reconfigure_cloud_database (google.spanner.executor_v1.types.ReconfigureCloudDatabaseAction):
            Action that reconfigures a Cloud Spanner
            database.

            This field is a member of `oneof`_ ``action``.
    """

    create_user_instance_config: "CreateUserInstanceConfigAction" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="action",
        message="CreateUserInstanceConfigAction",
    )
    update_user_instance_config: "UpdateUserInstanceConfigAction" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action",
        message="UpdateUserInstanceConfigAction",
    )
    delete_user_instance_config: "DeleteUserInstanceConfigAction" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="action",
        message="DeleteUserInstanceConfigAction",
    )
    get_cloud_instance_config: "GetCloudInstanceConfigAction" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="action",
        message="GetCloudInstanceConfigAction",
    )
    list_instance_configs: "ListCloudInstanceConfigsAction" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="action",
        message="ListCloudInstanceConfigsAction",
    )
    create_cloud_instance: "CreateCloudInstanceAction" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="action",
        message="CreateCloudInstanceAction",
    )
    update_cloud_instance: "UpdateCloudInstanceAction" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="action",
        message="UpdateCloudInstanceAction",
    )
    delete_cloud_instance: "DeleteCloudInstanceAction" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="action",
        message="DeleteCloudInstanceAction",
    )
    list_cloud_instances: "ListCloudInstancesAction" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="action",
        message="ListCloudInstancesAction",
    )
    get_cloud_instance: "GetCloudInstanceAction" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="action",
        message="GetCloudInstanceAction",
    )
    create_cloud_database: "CreateCloudDatabaseAction" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="action",
        message="CreateCloudDatabaseAction",
    )
    update_cloud_database_ddl: "UpdateCloudDatabaseDdlAction" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="action",
        message="UpdateCloudDatabaseDdlAction",
    )
    update_cloud_database: "UpdateCloudDatabaseAction" = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="action",
        message="UpdateCloudDatabaseAction",
    )
    drop_cloud_database: "DropCloudDatabaseAction" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="action",
        message="DropCloudDatabaseAction",
    )
    list_cloud_databases: "ListCloudDatabasesAction" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="action",
        message="ListCloudDatabasesAction",
    )
    list_cloud_database_operations: "ListCloudDatabaseOperationsAction" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="action",
        message="ListCloudDatabaseOperationsAction",
    )
    restore_cloud_database: "RestoreCloudDatabaseAction" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="action",
        message="RestoreCloudDatabaseAction",
    )
    get_cloud_database: "GetCloudDatabaseAction" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="action",
        message="GetCloudDatabaseAction",
    )
    create_cloud_backup: "CreateCloudBackupAction" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="action",
        message="CreateCloudBackupAction",
    )
    copy_cloud_backup: "CopyCloudBackupAction" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="action",
        message="CopyCloudBackupAction",
    )
    get_cloud_backup: "GetCloudBackupAction" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="action",
        message="GetCloudBackupAction",
    )
    update_cloud_backup: "UpdateCloudBackupAction" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="action",
        message="UpdateCloudBackupAction",
    )
    delete_cloud_backup: "DeleteCloudBackupAction" = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="action",
        message="DeleteCloudBackupAction",
    )
    list_cloud_backups: "ListCloudBackupsAction" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="action",
        message="ListCloudBackupsAction",
    )
    list_cloud_backup_operations: "ListCloudBackupOperationsAction" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="action",
        message="ListCloudBackupOperationsAction",
    )
    get_operation: "GetOperationAction" = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="action",
        message="GetOperationAction",
    )
    cancel_operation: "CancelOperationAction" = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="action",
        message="CancelOperationAction",
    )
    reconfigure_cloud_database: "ReconfigureCloudDatabaseAction" = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="action",
        message="ReconfigureCloudDatabaseAction",
    )


class CreateUserInstanceConfigAction(proto.Message):
    r"""Action that creates a user instance config.

    Attributes:
        user_config_id (str):
            User instance config ID (not path), e.g.
            "custom-config".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        base_config_id (str):
            Base config ID, e.g. "test-config".
        replicas (MutableSequence[google.spanner.admin.instance.v1.spanner_instance_admin_pb2.ReplicaInfo]):
            Replicas that should be included in the user
            config.
    """

    user_config_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    base_config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    replicas: MutableSequence[
        spanner_instance_admin_pb2.ReplicaInfo
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=spanner_instance_admin_pb2.ReplicaInfo,
    )


class UpdateUserInstanceConfigAction(proto.Message):
    r"""Action that updates a user instance config.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_config_id (str):
            User instance config ID (not path), e.g.
            "custom-config".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        display_name (str):
            The descriptive name for this instance config
            as it appears in UIs.

            This field is a member of `oneof`_ ``_display_name``.
        labels (MutableMapping[str, str]):
            labels.
    """

    user_config_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class GetCloudInstanceConfigAction(proto.Message):
    r"""Action that gets a user instance config.

    Attributes:
        instance_config_id (str):
            Instance config ID (not path), e.g.
            "custom-config".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
    """

    instance_config_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteUserInstanceConfigAction(proto.Message):
    r"""Action that deletes a user instance configs.

    Attributes:
        user_config_id (str):
            User instance config ID (not path), e.g.
            "custom-config".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
    """

    user_config_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListCloudInstanceConfigsAction(proto.Message):
    r"""Action that lists user instance configs.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        page_size (int):
            Number of instance configs to be returned in
            the response. If 0 or less, defaults to the
            server's maximum allowed page size.

            This field is a member of `oneof`_ ``_page_size``.
        page_token (str):
            If non-empty, "page_token" should contain a next_page_token
            from a previous ListInstanceConfigsResponse to the same
            "parent".

            This field is a member of `oneof`_ ``_page_token``.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class CreateCloudInstanceAction(proto.Message):
    r"""Action that creates a Cloud Spanner instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_config_id (str):
            Instance config ID, e.g. "test-config".
        node_count (int):
            Number of nodes (processing_units should not be set or set
            to 0 if used).

            This field is a member of `oneof`_ ``_node_count``.
        processing_units (int):
            Number of processing units (node_count should be set to 0 if
            used).

            This field is a member of `oneof`_ ``_processing_units``.
        autoscaling_config (google.spanner.admin.instance.v1.spanner_instance_admin_pb2.AutoscalingConfig):
            The autoscaling config for this instance. If non-empty, an
            autoscaling instance will be created (processing_units and
            node_count should be set to 0 if used).

            This field is a member of `oneof`_ ``_autoscaling_config``.
        labels (MutableMapping[str, str]):
            labels.
    """

    instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    processing_units: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    autoscaling_config: spanner_instance_admin_pb2.AutoscalingConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=spanner_instance_admin_pb2.AutoscalingConfig,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )


class UpdateCloudInstanceAction(proto.Message):
    r"""Action that updates a Cloud Spanner instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        display_name (str):
            The descriptive name for this instance as it
            appears in UIs. Must be unique per project and
            between 4 and 30 characters in length.

            This field is a member of `oneof`_ ``_display_name``.
        node_count (int):
            The number of nodes allocated to this instance. At most one
            of either node_count or processing_units should be present
            in the message.

            This field is a member of `oneof`_ ``_node_count``.
        processing_units (int):
            The number of processing units allocated to this instance.
            At most one of processing_units or node_count should be
            present in the message.

            This field is a member of `oneof`_ ``_processing_units``.
        autoscaling_config (google.spanner.admin.instance.v1.spanner_instance_admin_pb2.AutoscalingConfig):
            The autoscaling config for this instance. If non-empty, this
            instance is using autoscaling (processing_units and
            node_count should be set to 0 if used).

            This field is a member of `oneof`_ ``_autoscaling_config``.
        labels (MutableMapping[str, str]):
            labels.
    """

    instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    processing_units: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    autoscaling_config: spanner_instance_admin_pb2.AutoscalingConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=spanner_instance_admin_pb2.AutoscalingConfig,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )


class DeleteCloudInstanceAction(proto.Message):
    r"""Action that deletes a Cloud Spanner instance.

    Attributes:
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
    """

    instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateCloudDatabaseAction(proto.Message):
    r"""Action that creates a Cloud Spanner database.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        database_id (str):
            Cloud database ID (not full path), e.g.
            "db0".
        sdl_statement (MutableSequence[str]):
            SDL statements to apply to the new database.
        encryption_config (google.spanner.admin.database.v1.common_pb2.EncryptionConfig):
            The KMS key used to encrypt the database to
            be created if the database should be CMEK
            protected.
        dialect (str):
            Optional SQL dialect (GOOGLESQL or
            POSTGRESQL).  Default: GOOGLESQL.

            This field is a member of `oneof`_ ``_dialect``.
        proto_descriptors (bytes):

            This field is a member of `oneof`_ ``_proto_descriptors``.
    """

    instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    sdl_statement: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    encryption_config: common_pb2.EncryptionConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=common_pb2.EncryptionConfig,
    )
    dialect: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    proto_descriptors: bytes = proto.Field(
        proto.BYTES,
        number=7,
        optional=True,
    )


class UpdateCloudDatabaseDdlAction(proto.Message):
    r"""Action that updates the schema of a Cloud Spanner database.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        database_id (str):
            Cloud database ID (not full path), e.g.
            "db0".
        sdl_statement (MutableSequence[str]):
            SDL statements to apply to the database.
        operation_id (str):
            Op ID can be used to track progress of the
            update. If set, it must be unique per database.
            If not set, Cloud Spanner will generate
            operation ID automatically.
        proto_descriptors (bytes):

            This field is a member of `oneof`_ ``_proto_descriptors``.
    """

    instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    sdl_statement: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    operation_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    proto_descriptors: bytes = proto.Field(
        proto.BYTES,
        number=6,
        optional=True,
    )


class UpdateCloudDatabaseAction(proto.Message):
    r"""Action that updates a Cloud Spanner database.

    Attributes:
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        database_name (str):
            Cloud database name (not full path), e.g.
            "db0".
        enable_drop_protection (bool):
            Updated value of enable_drop_protection, this is the only
            field that has supported to be updated.
    """

    instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    enable_drop_protection: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class DropCloudDatabaseAction(proto.Message):
    r"""Action that drops a Cloud Spanner database.

    Attributes:
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        database_id (str):
            Cloud database ID (not full path), e.g.
            "db0".
    """

    instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReconfigureCloudDatabaseAction(proto.Message):
    r"""Action that reconfigures a Cloud Spanner database.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        database_uri (str):
            The fully qualified uri of the database to be
            reconfigured.

            This field is a member of `oneof`_ ``_database_uri``.
        serving_locations (MutableSequence[str]):
            The locations of the serving regions, e.g.
            "asia-south1".
    """

    database_uri: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    serving_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ListCloudDatabasesAction(proto.Message):
    r"""Action that lists Cloud Spanner databases.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path) to list
            databases from, e.g. "test-instance".
        page_size (int):
            Number of databases to be returned in the
            response. If 0 or less, defaults to the server's
            maximum allowed page size.
        page_token (str):
            If non-empty, "page_token" should contain a next_page_token
            from a previous ListDatabasesResponse to the same "parent"
            and with the same "filter".
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListCloudInstancesAction(proto.Message):
    r"""Action that lists Cloud Spanner databases.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        filter (str):
            A filter expression that filters what operations are
            returned in the response. The expression must specify the
            field name, a comparison operator, and the value that you
            want to use for filtering. Refer
            spanner_instance_admin.proto.ListInstancesRequest for
            detail.

            This field is a member of `oneof`_ ``_filter``.
        page_size (int):
            Number of instances to be returned in the
            response. If 0 or less, defaults to the server's
            maximum allowed page size.

            This field is a member of `oneof`_ ``_page_size``.
        page_token (str):
            If non-empty, "page_token" should contain a next_page_token
            from a previous ListInstancesResponse to the same "parent"
            and with the same "filter".

            This field is a member of `oneof`_ ``_page_token``.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class GetCloudInstanceAction(proto.Message):
    r"""Action that retrieves a Cloud Spanner instance.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path) to retrieve the
            instance from, e.g. "test-instance".
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListCloudDatabaseOperationsAction(proto.Message):
    r"""Action that lists Cloud Spanner database operations.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path) to list database
            operations from, e.g. "test-instance".
        filter (str):
            A filter expression that filters what operations are
            returned in the response. The expression must specify the
            field name, a comparison operator, and the value that you
            want to use for filtering. Refer
            spanner_database_admin.proto.ListDatabaseOperationsRequest
            for detail.
        page_size (int):
            Number of databases to be returned in the
            response. If 0 or less, defaults to the server's
            maximum allowed page size.
        page_token (str):
            If non-empty, "page_token" should contain a next_page_token
            from a previous ListDatabaseOperationsResponse to the same
            "parent" and with the same "filter".
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class RestoreCloudDatabaseAction(proto.Message):
    r"""Action that restores a Cloud Spanner database from a backup.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        backup_instance_id (str):
            Cloud instance ID (not path) containing the
            backup, e.g. "backup-instance".
        backup_id (str):
            The id of the backup from which to restore,
            e.g. "test-backup".
        database_instance_id (str):
            Cloud instance ID (not path) containing the
            database, e.g. "database-instance".
        database_id (str):
            The id of the database to create and restore
            to, e.g. "db0". Note that this database must not
            already exist.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database_instance_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetCloudDatabaseAction(proto.Message):
    r"""Action that gets a Cloud Spanner database.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        database_id (str):
            The id of the database to get, e.g. "db0".
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateCloudBackupAction(proto.Message):
    r"""Action that creates a Cloud Spanner database backup.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        backup_id (str):
            The id of the backup to be created, e.g.
            "test-backup".
        database_id (str):
            The id of the database from which this backup
            was created, e.g. "db0". Note that this needs to
            be in the same instance as the backup.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The expiration time of the
            backup, which must be at least 6 hours and at
            most 366 days from the time the request is
            received.
        version_time (google.protobuf.timestamp_pb2.Timestamp):
            The version time of the backup, which must be within the
            time range of [earliest_version_time, NOW], where
            earliest_version_time is retrieved by cloud spanner frontend
            API (See details: go/cs-pitr-lite-design).

            This field is a member of `oneof`_ ``_version_time``.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    version_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )


class CopyCloudBackupAction(proto.Message):
    r"""Action that copies a Cloud Spanner database backup.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        backup_id (str):
            The id of the backup to be created, e.g.
            "test-backup".
        source_backup (str):
            The fully qualified uri of the source backup from which this
            backup was copied. eg.
            "projects/<project_id>/instances/<instance_id>/backups/<backup_id>".
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The expiration time of the
            backup, which must be at least 6 hours and at
            most 366 days from the time the request is
            received.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    source_backup: str = proto.Field(
        proto.STRING,
        number=4,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class GetCloudBackupAction(proto.Message):
    r"""Action that gets a Cloud Spanner database backup.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        backup_id (str):
            The id of the backup to get, e.g.
            "test-backup".
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateCloudBackupAction(proto.Message):
    r"""Action that updates a Cloud Spanner database backup.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        backup_id (str):
            The id of the backup to update, e.g.
            "test-backup".
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Updated value of expire_time, this is the only
            field that supported to be updated.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class DeleteCloudBackupAction(proto.Message):
    r"""Action that deletes a Cloud Spanner database backup.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path), e.g.
            "test-instance".
        backup_id (str):
            The id of the backup to delete, e.g.
            "test-backup".
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListCloudBackupsAction(proto.Message):
    r"""Action that lists Cloud Spanner database backups.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path) to list backups
            from, e.g. "test-instance".
        filter (str):
            A filter expression that filters backups
            listed in the response. The expression must
            specify the field name, a comparison operator,
            and the value that you want to use for
            filtering. Refer backup.proto.ListBackupsRequest
            for detail.
        page_size (int):
            Number of backups to be returned in the
            response. If 0 or less, defaults to the server's
            maximum allowed page size.
        page_token (str):
            If non-empty, "page_token" should contain a next_page_token
            from a previous ListBackupsResponse to the same "parent" and
            with the same "filter".
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCloudBackupOperationsAction(proto.Message):
    r"""Action that lists Cloud Spanner database backup operations.

    Attributes:
        project_id (str):
            Cloud project ID, e.g.
            "spanner-cloud-systest".
        instance_id (str):
            Cloud instance ID (not path) to list backup
            operations from, e.g. "test-instance".
        filter (str):
            A filter expression that filters what
            operations are returned in the response.
            The expression must specify the field name, a
            comparison operator, and the value that you want
            to use for filtering. Refer
            backup.proto.ListBackupOperationsRequest for
            detail.
        page_size (int):
            Number of backups to be returned in the
            response. If 0 or less, defaults to the server's
            maximum allowed page size.
        page_token (str):
            If non-empty, "page_token" should contain a next_page_token
            from a previous ListBackupOperationsResponse to the same
            "parent" and with the same "filter".
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetOperationAction(proto.Message):
    r"""Action that gets an operation.

    Attributes:
        operation (str):
            The name of the operation resource.
    """

    operation: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelOperationAction(proto.Message):
    r"""Action that cancels an operation.

    Attributes:
        operation (str):
            The name of the operation resource to be
            cancelled.
    """

    operation: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartBatchTransactionAction(proto.Message):
    r"""Starts a batch read-only transaction in executor. Successful
    outcomes of this action will contain batch_txn_id--the identificator
    that can be used to start the same transaction in other Executors to
    parallelize partition processing.

    Example of a batch read flow:

    1. Start batch transaction with a timestamp
       (StartBatchTransactionAction)
    2. Generate database partitions for a read or query
       (GenerateDbPartitionsForReadAction/GenerateDbPartitionsForQueryAction)
    3. Call ExecutePartitionAction for some or all partitions, process
       rows
    4. Clean up the transaction (CloseBatchTransactionAction).

    More sophisticated example, with parallel processing:

    1. Start batch transaction with a timestamp
       (StartBatchTransactionAction), note the returned
       BatchTransactionId
    2. Generate database partitions for a read or query
       (GenerateDbPartitionsForReadAction/GenerateDbPartitionsForQueryAction)
    3. Distribute the partitions over a pool of workers, along with the
       transaction ID.

    In each worker: 4-1. StartBatchTransactionAction with the given
    transaction ID 4-2. ExecutePartitionAction for each partition it
    got, process read results 4-3. Close (not cleanup) the transaction
    (CloseBatchTransactionAction).

    When all workers are done: 5. Cleanup the transaction
    (CloseBatchTransactionAction). This can be done either by the last
    worker to finish the job, or by the main Executor that initialized
    this transaction in the first place. It is also possible to clean it
    up with a brand new Executor -- just execute
    StartBatchTransactionAction with the ID, then clean it up right
    away.

    Cleaning up is optional, but recommended.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        batch_txn_time (google.protobuf.timestamp_pb2.Timestamp):
            The exact timestamp to start the batch
            transaction.

            This field is a member of `oneof`_ ``param``.
        tid (bytes):
            ID of a batch read-only transaction. It can
            be used to start the same batch transaction on
            multiple executors and parallelize partition
            processing.

            This field is a member of `oneof`_ ``param``.
        cloud_database_role (str):
            Database role to assume while performing this action.
            Setting the database_role will enforce additional role-based
            access checks on this action.
    """

    batch_txn_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="param",
        message=timestamp_pb2.Timestamp,
    )
    tid: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="param",
    )
    cloud_database_role: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CloseBatchTransactionAction(proto.Message):
    r"""Closes or cleans up the currently opened batch read-only
    transaction.
    Once a transaction is closed, the Executor can be disposed of or
    used to start start another transaction. Closing a batch
    transaction in one Executor doesn't affect the transaction's
    state in other Executors that also read from it.

    When a transaction is cleaned up, it becomes globally invalid.
    Cleaning up is optional, but recommended.

    Attributes:
        cleanup (bool):
            Indicates whether the transaction needs to be
            cleaned up.
    """

    cleanup: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class GenerateDbPartitionsForReadAction(proto.Message):
    r"""Generate database partitions for the given read. Successful outcomes
    will contain database partitions in the db_partition field.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        read (google.spanner.executor_v1.types.ReadAction):
            Read to generate partitions for.
        table (MutableSequence[google.spanner.executor_v1.types.TableMetadata]):
            Metadata related to the tables involved in
            the read.
        desired_bytes_per_partition (int):
            Desired size of data in each partition.
            Spanner doesn't guarantee to respect this value.

            This field is a member of `oneof`_ ``_desired_bytes_per_partition``.
        max_partition_count (int):
            If set, the desired max number of partitions.
            Spanner doesn't guarantee to respect this value.

            This field is a member of `oneof`_ ``_max_partition_count``.
    """

    read: "ReadAction" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ReadAction",
    )
    table: MutableSequence["TableMetadata"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="TableMetadata",
    )
    desired_bytes_per_partition: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    max_partition_count: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )


class GenerateDbPartitionsForQueryAction(proto.Message):
    r"""Generate database partitions for the given query. Successful
    outcomes will contain database partitions in the db_partition field.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query (google.spanner.executor_v1.types.QueryAction):
            Query to generate partitions for.
        desired_bytes_per_partition (int):
            Desired size of data in each partition.
            Spanner doesn't guarantee to respect this value.

            This field is a member of `oneof`_ ``_desired_bytes_per_partition``.
    """

    query: "QueryAction" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="QueryAction",
    )
    desired_bytes_per_partition: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


class BatchPartition(proto.Message):
    r"""Identifies a database partition generated for a particular
    read or query. To read rows from the partition, use
    ExecutePartitionAction.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        partition (bytes):
            Serialized Partition instance.
        partition_token (bytes):
            The partition token decrypted from partition.
        table (str):
            Table name is set iff the partition was
            generated for a read (as opposed to a query).

            This field is a member of `oneof`_ ``_table``.
        index (str):
            Index name if the partition was generated for
            an index read.

            This field is a member of `oneof`_ ``_index``.
    """

    partition: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    partition_token: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    table: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    index: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class ExecutePartitionAction(proto.Message):
    r"""Performs a read or query for the given partitions. This
    action must be executed in the context of the same transaction
    that was used to generate given partitions.

    Attributes:
        partition (google.spanner.executor_v1.types.BatchPartition):
            Batch partition to execute on.
    """

    partition: "BatchPartition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BatchPartition",
    )


class ExecuteChangeStreamQuery(proto.Message):
    r"""Execute a change stream TVF query.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Name for this change stream.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Specifies that records with commit_timestamp greater than or
            equal to start_time should be returned.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Specifies that records with commit_timestamp less than or
            equal to end_time should be returned.

            This field is a member of `oneof`_ ``_end_time``.
        partition_token (str):
            Specifies which change stream partition to
            query, based on the content of child partitions
            records.

            This field is a member of `oneof`_ ``_partition_token``.
        read_options (MutableSequence[str]):
            Read options for this change stream query.
        heartbeat_milliseconds (int):
            Determines how frequently a heartbeat
            ChangeRecord will be returned in case there are
            no transactions committed in this partition, in
            milliseconds.

            This field is a member of `oneof`_ ``_heartbeat_milliseconds``.
        deadline_seconds (int):
            Deadline for this change stream query, in
            seconds.

            This field is a member of `oneof`_ ``_deadline_seconds``.
        cloud_database_role (str):
            Database role to assume while performing this
            action. This should only be set for cloud
            requests. Setting the database role will enforce
            additional role-based access checks on this
            action.

            This field is a member of `oneof`_ ``_cloud_database_role``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    partition_token: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    read_options: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    heartbeat_milliseconds: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    deadline_seconds: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    cloud_database_role: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )


class SpannerActionOutcome(proto.Message):
    r"""SpannerActionOutcome defines a result of execution of a
    single SpannerAction.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        status (google.rpc.status_pb2.Status):
            If an outcome is split into multiple parts,
            status will be set only in the last part.

            This field is a member of `oneof`_ ``_status``.
        commit_time (google.protobuf.timestamp_pb2.Timestamp):
            Transaction timestamp. It must be set for
            successful committed actions.

            This field is a member of `oneof`_ ``_commit_time``.
        read_result (google.spanner.executor_v1.types.ReadResult):
            Result of a ReadAction. This field must be
            set for ReadActions even if no rows were read.

            This field is a member of `oneof`_ ``_read_result``.
        query_result (google.spanner.executor_v1.types.QueryResult):
            Result of a Query. This field must be set for
            Queries even if no rows were read.

            This field is a member of `oneof`_ ``_query_result``.
        transaction_restarted (bool):
            This bit indicates that Spanner has restarted
            the current transaction. It means that the
            client should replay all the reads and writes.
            Setting it to true is only valid in the context
            of a read-write transaction, as an outcome of a
            committing FinishTransactionAction.

            This field is a member of `oneof`_ ``_transaction_restarted``.
        batch_txn_id (bytes):
            In successful StartBatchTransactionAction
            outcomes, this contains the ID of the
            transaction.

            This field is a member of `oneof`_ ``_batch_txn_id``.
        db_partition (MutableSequence[google.spanner.executor_v1.types.BatchPartition]):
            Generated database partitions (result of a
            GenetageDbPartitionsForReadAction/GenerateDbPartitionsForQueryAction).
        admin_result (google.spanner.executor_v1.types.AdminResult):
            Result of admin related actions.

            This field is a member of `oneof`_ ``_admin_result``.
        dml_rows_modified (MutableSequence[int]):
            Stores rows modified by query in single DML
            or batch DML action. In case of batch DML
            action, stores 0 as row count of errored DML
            query.
        change_stream_records (MutableSequence[google.spanner.executor_v1.types.ChangeStreamRecord]):
            Change stream records returned by a change
            stream query.
    """

    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message=status_pb2.Status,
    )
    commit_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    read_result: "ReadResult" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="ReadResult",
    )
    query_result: "QueryResult" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="QueryResult",
    )
    transaction_restarted: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    batch_txn_id: bytes = proto.Field(
        proto.BYTES,
        number=6,
        optional=True,
    )
    db_partition: MutableSequence["BatchPartition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="BatchPartition",
    )
    admin_result: "AdminResult" = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message="AdminResult",
    )
    dml_rows_modified: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=9,
    )
    change_stream_records: MutableSequence["ChangeStreamRecord"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="ChangeStreamRecord",
    )


class AdminResult(proto.Message):
    r"""AdminResult contains admin action results, for
    database/backup/operation.

    Attributes:
        backup_response (google.spanner.executor_v1.types.CloudBackupResponse):
            Results of cloud backup related actions.
        operation_response (google.spanner.executor_v1.types.OperationResponse):
            Results of operation related actions.
        database_response (google.spanner.executor_v1.types.CloudDatabaseResponse):
            Results of database related actions.
        instance_response (google.spanner.executor_v1.types.CloudInstanceResponse):
            Results of instance related actions.
        instance_config_response (google.spanner.executor_v1.types.CloudInstanceConfigResponse):
            Results of instance config related actions.
    """

    backup_response: "CloudBackupResponse" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CloudBackupResponse",
    )
    operation_response: "OperationResponse" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OperationResponse",
    )
    database_response: "CloudDatabaseResponse" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CloudDatabaseResponse",
    )
    instance_response: "CloudInstanceResponse" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CloudInstanceResponse",
    )
    instance_config_response: "CloudInstanceConfigResponse" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="CloudInstanceConfigResponse",
    )


class CloudBackupResponse(proto.Message):
    r"""CloudBackupResponse contains results returned by cloud backup
    related actions.

    Attributes:
        listed_backups (MutableSequence[google.spanner.admin.database.v1.backup_pb2.Backup]):
            List of backups returned by
            ListCloudBackupsAction.
        listed_backup_operations (MutableSequence[google.longrunning.operations_pb2.Operation]):
            List of operations returned by
            ListCloudBackupOperationsAction.
        next_page_token (str):
            "next_page_token" can be sent in a subsequent list action to
            fetch more of the matching data.
        backup (google.spanner.admin.database.v1.backup_pb2.Backup):
            Backup returned by
            GetCloudBackupAction/UpdateCloudBackupAction.
    """

    @property
    def raw_page(self):
        return self

    listed_backups: MutableSequence[backup_pb2.Backup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=backup_pb2.Backup,
    )
    listed_backup_operations: MutableSequence[
        operations_pb2.Operation
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=operations_pb2.Operation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    backup: backup_pb2.Backup = proto.Field(
        proto.MESSAGE,
        number=4,
        message=backup_pb2.Backup,
    )


class OperationResponse(proto.Message):
    r"""OperationResponse contains results returned by operation
    related actions.

    Attributes:
        listed_operations (MutableSequence[google.longrunning.operations_pb2.Operation]):
            List of operations returned by
            ListOperationsAction.
        next_page_token (str):
            "next_page_token" can be sent in a subsequent list action to
            fetch more of the matching data.
        operation (google.longrunning.operations_pb2.Operation):
            Operation returned by GetOperationAction.
    """

    @property
    def raw_page(self):
        return self

    listed_operations: MutableSequence[operations_pb2.Operation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=operations_pb2.Operation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    operation: operations_pb2.Operation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=operations_pb2.Operation,
    )


class CloudInstanceResponse(proto.Message):
    r"""CloudInstanceResponse contains results returned by cloud
    instance related actions.

    Attributes:
        listed_instances (MutableSequence[google.spanner.admin.instance.v1.spanner_instance_admin_pb2.Instance]):
            List of instances returned by
            ListCloudInstancesAction.
        next_page_token (str):
            "next_page_token" can be sent in a subsequent list action to
            fetch more of the matching data.
        instance (google.spanner.admin.instance.v1.spanner_instance_admin_pb2.Instance):
            Instance returned by GetCloudInstanceAction
    """

    @property
    def raw_page(self):
        return self

    listed_instances: MutableSequence[
        spanner_instance_admin_pb2.Instance
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=spanner_instance_admin_pb2.Instance,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: spanner_instance_admin_pb2.Instance = proto.Field(
        proto.MESSAGE,
        number=3,
        message=spanner_instance_admin_pb2.Instance,
    )


class CloudInstanceConfigResponse(proto.Message):
    r"""CloudInstanceConfigResponse contains results returned by
    cloud instance config related actions.

    Attributes:
        listed_instance_configs (MutableSequence[google.spanner.admin.instance.v1.spanner_instance_admin_pb2.InstanceConfig]):
            List of instance configs returned by
            ListCloudInstanceConfigsAction.
        next_page_token (str):
            "next_page_token" can be sent in a subsequent list action to
            fetch more of the matching data.
        instance_config (google.spanner.admin.instance.v1.spanner_instance_admin_pb2.InstanceConfig):
            Instance config returned by
            GetCloudInstanceConfigAction.
    """

    @property
    def raw_page(self):
        return self

    listed_instance_configs: MutableSequence[
        spanner_instance_admin_pb2.InstanceConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=spanner_instance_admin_pb2.InstanceConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_config: spanner_instance_admin_pb2.InstanceConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=spanner_instance_admin_pb2.InstanceConfig,
    )


class CloudDatabaseResponse(proto.Message):
    r"""CloudDatabaseResponse contains results returned by cloud
    database related actions.

    Attributes:
        listed_databases (MutableSequence[google.spanner.admin.database.v1.spanner_database_admin_pb2.Database]):
            List of databases returned by
            ListCloudDatabasesAction.
        listed_database_operations (MutableSequence[google.longrunning.operations_pb2.Operation]):
            List of operations returned by
            ListCloudDatabaseOperationsAction.
        next_page_token (str):
            "next_page_token" can be sent in a subsequent list action to
            fetch more of the matching data.
        database (google.spanner.admin.database.v1.spanner_database_admin_pb2.Database):
            Database returned by GetCloudDatabaseAction
    """

    @property
    def raw_page(self):
        return self

    listed_databases: MutableSequence[
        spanner_database_admin_pb2.Database
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=spanner_database_admin_pb2.Database,
    )
    listed_database_operations: MutableSequence[
        operations_pb2.Operation
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=operations_pb2.Operation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database: spanner_database_admin_pb2.Database = proto.Field(
        proto.MESSAGE,
        number=4,
        message=spanner_database_admin_pb2.Database,
    )


class ReadResult(proto.Message):
    r"""ReadResult contains rows read.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        table (str):
            Table name.
        index (str):
            Index name, if read from an index.

            This field is a member of `oneof`_ ``_index``.
        request_index (int):
            Request index (multiread only).

            This field is a member of `oneof`_ ``_request_index``.
        row (MutableSequence[google.spanner.executor_v1.types.ValueList]):
            Rows read. Each row is a struct with multiple
            fields, one for each column in read result. All
            rows have the same type.
        row_type (google.spanner.v1.type_pb2.StructType):
            The type of rows read. It must be set if at
            least one row was read.

            This field is a member of `oneof`_ ``_row_type``.
    """

    table: str = proto.Field(
        proto.STRING,
        number=1,
    )
    index: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    request_index: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    row: MutableSequence["ValueList"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="ValueList",
    )
    row_type: type_pb2.StructType = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=type_pb2.StructType,
    )


class QueryResult(proto.Message):
    r"""QueryResult contains result of a Query.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        row (MutableSequence[google.spanner.executor_v1.types.ValueList]):
            Rows read. Each row is a struct with multiple
            fields, one for each column in read result. All
            rows have the same type.
        row_type (google.spanner.v1.type_pb2.StructType):
            The type of rows read. It must be set if at
            least one row was read.

            This field is a member of `oneof`_ ``_row_type``.
    """

    row: MutableSequence["ValueList"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ValueList",
    )
    row_type: type_pb2.StructType = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=type_pb2.StructType,
    )


class ChangeStreamRecord(proto.Message):
    r"""Raw ChangeStream records.
    Encodes one of: DataChangeRecord, HeartbeatRecord,
    ChildPartitionsRecord returned from the ChangeStream API.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_change (google.spanner.executor_v1.types.DataChangeRecord):
            Data change record.

            This field is a member of `oneof`_ ``record``.
        child_partition (google.spanner.executor_v1.types.ChildPartitionsRecord):
            Child partitions record.

            This field is a member of `oneof`_ ``record``.
        heartbeat (google.spanner.executor_v1.types.HeartbeatRecord):
            Heartbeat record.

            This field is a member of `oneof`_ ``record``.
    """

    data_change: "DataChangeRecord" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="record",
        message="DataChangeRecord",
    )
    child_partition: "ChildPartitionsRecord" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="record",
        message="ChildPartitionsRecord",
    )
    heartbeat: "HeartbeatRecord" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="record",
        message="HeartbeatRecord",
    )


class DataChangeRecord(proto.Message):
    r"""ChangeStream data change record.

    Attributes:
        commit_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp in which the change was
            committed.
        record_sequence (str):
            The sequence number for the record within the
            transaction.
        transaction_id (str):
            A globally unique string that represents the
            transaction in which the change was committed.
        is_last_record (bool):
            Indicates whether this is the last record for
            a transaction in the current partition.
        table (str):
            Name of the table affected by the change.
        column_types (MutableSequence[google.spanner.executor_v1.types.DataChangeRecord.ColumnType]):
            Column types defined in the schema.
        mods (MutableSequence[google.spanner.executor_v1.types.DataChangeRecord.Mod]):
            Changes made in the transaction.
        mod_type (str):
            Describes the type of change. One of INSERT,
            UPDATE or DELETE.
        value_capture_type (str):
            One of value capture type: NEW_VALUES, OLD_VALUES,
            OLD_AND_NEW_VALUES.
        record_count (int):
            Number of records in transactions.
        partition_count (int):
            Number of partitions in transactions.
        transaction_tag (str):
            Transaction tag info.
        is_system_transaction (bool):
            Whether the transaction is a system
            transactionn.
    """

    class ColumnType(proto.Message):
        r"""Column types.

        Attributes:
            name (str):
                Column name.
            type_ (str):
                Column type in JSON.
            is_primary_key (bool):
                Whether the column is a primary key column.
            ordinal_position (int):
                The position of the column as defined in the
                schema.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=2,
        )
        is_primary_key: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        ordinal_position: int = proto.Field(
            proto.INT64,
            number=4,
        )

    class Mod(proto.Message):
        r"""Describes the changes that were made.

        Attributes:
            keys (str):
                The primary key values in JSON.
            new_values (str):
                The new values of the changed columns in
                JSON. Only contain the non-key columns.
            old_values (str):
                The old values of the changed columns in
                JSON. Only contain the non-key columns.
        """

        keys: str = proto.Field(
            proto.STRING,
            number=1,
        )
        new_values: str = proto.Field(
            proto.STRING,
            number=2,
        )
        old_values: str = proto.Field(
            proto.STRING,
            number=3,
        )

    commit_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    record_sequence: str = proto.Field(
        proto.STRING,
        number=2,
    )
    transaction_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    is_last_record: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    table: str = proto.Field(
        proto.STRING,
        number=5,
    )
    column_types: MutableSequence[ColumnType] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=ColumnType,
    )
    mods: MutableSequence[Mod] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=Mod,
    )
    mod_type: str = proto.Field(
        proto.STRING,
        number=8,
    )
    value_capture_type: str = proto.Field(
        proto.STRING,
        number=9,
    )
    record_count: int = proto.Field(
        proto.INT64,
        number=10,
    )
    partition_count: int = proto.Field(
        proto.INT64,
        number=11,
    )
    transaction_tag: str = proto.Field(
        proto.STRING,
        number=12,
    )
    is_system_transaction: bool = proto.Field(
        proto.BOOL,
        number=13,
    )


class ChildPartitionsRecord(proto.Message):
    r"""ChangeStream child partition record.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Data change records returned from child partitions in this
            child partitions record will have a commit timestamp greater
            than or equal to start_time.
        record_sequence (str):
            A monotonically increasing sequence number that can be used
            to define the ordering of the child partitions record when
            there are multiple child partitions records returned with
            the same start_time in a particular partition.
        child_partitions (MutableSequence[google.spanner.executor_v1.types.ChildPartitionsRecord.ChildPartition]):
            A set of child partitions and their
            associated information.
    """

    class ChildPartition(proto.Message):
        r"""A single child partition.

        Attributes:
            token (str):
                Partition token string used to identify the
                child partition in queries.
            parent_partition_tokens (MutableSequence[str]):
                Parent partition tokens of this child
                partition.
        """

        token: str = proto.Field(
            proto.STRING,
            number=1,
        )
        parent_partition_tokens: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    record_sequence: str = proto.Field(
        proto.STRING,
        number=2,
    )
    child_partitions: MutableSequence[ChildPartition] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=ChildPartition,
    )


class HeartbeatRecord(proto.Message):
    r"""ChangeStream heartbeat record.

    Attributes:
        heartbeat_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp for this heartbeat check.
    """

    heartbeat_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
