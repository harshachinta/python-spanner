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
from google.spanner.executor import gapic_version as package_version

__version__ = package_version.__version__


from google.spanner.executor_v1.services.spanner_executor_proxy.client import (
    SpannerExecutorProxyClient,
)
from google.spanner.executor_v1.services.spanner_executor_proxy.async_client import (
    SpannerExecutorProxyAsyncClient,
)

from google.spanner.executor_v1.types.cloud_executor import AdminAction
from google.spanner.executor_v1.types.cloud_executor import AdminResult
from google.spanner.executor_v1.types.cloud_executor import BatchDmlAction
from google.spanner.executor_v1.types.cloud_executor import BatchPartition
from google.spanner.executor_v1.types.cloud_executor import CancelOperationAction
from google.spanner.executor_v1.types.cloud_executor import ChangeStreamRecord
from google.spanner.executor_v1.types.cloud_executor import ChildPartitionsRecord
from google.spanner.executor_v1.types.cloud_executor import CloseBatchTransactionAction
from google.spanner.executor_v1.types.cloud_executor import CloudBackupResponse
from google.spanner.executor_v1.types.cloud_executor import CloudDatabaseResponse
from google.spanner.executor_v1.types.cloud_executor import CloudInstanceConfigResponse
from google.spanner.executor_v1.types.cloud_executor import CloudInstanceResponse
from google.spanner.executor_v1.types.cloud_executor import ColumnMetadata
from google.spanner.executor_v1.types.cloud_executor import Concurrency
from google.spanner.executor_v1.types.cloud_executor import CopyCloudBackupAction
from google.spanner.executor_v1.types.cloud_executor import CreateCloudBackupAction
from google.spanner.executor_v1.types.cloud_executor import CreateCloudDatabaseAction
from google.spanner.executor_v1.types.cloud_executor import CreateCloudInstanceAction
from google.spanner.executor_v1.types.cloud_executor import (
    CreateUserInstanceConfigAction,
)
from google.spanner.executor_v1.types.cloud_executor import DataChangeRecord
from google.spanner.executor_v1.types.cloud_executor import DeleteCloudBackupAction
from google.spanner.executor_v1.types.cloud_executor import DeleteCloudInstanceAction
from google.spanner.executor_v1.types.cloud_executor import (
    DeleteUserInstanceConfigAction,
)
from google.spanner.executor_v1.types.cloud_executor import DmlAction
from google.spanner.executor_v1.types.cloud_executor import DropCloudDatabaseAction
from google.spanner.executor_v1.types.cloud_executor import ExecuteChangeStreamQuery
from google.spanner.executor_v1.types.cloud_executor import ExecutePartitionAction
from google.spanner.executor_v1.types.cloud_executor import FinishTransactionAction
from google.spanner.executor_v1.types.cloud_executor import (
    GenerateDbPartitionsForQueryAction,
)
from google.spanner.executor_v1.types.cloud_executor import (
    GenerateDbPartitionsForReadAction,
)
from google.spanner.executor_v1.types.cloud_executor import GetCloudBackupAction
from google.spanner.executor_v1.types.cloud_executor import GetCloudDatabaseAction
from google.spanner.executor_v1.types.cloud_executor import GetCloudInstanceAction
from google.spanner.executor_v1.types.cloud_executor import GetCloudInstanceConfigAction
from google.spanner.executor_v1.types.cloud_executor import GetOperationAction
from google.spanner.executor_v1.types.cloud_executor import HeartbeatRecord
from google.spanner.executor_v1.types.cloud_executor import KeyRange
from google.spanner.executor_v1.types.cloud_executor import KeySet
from google.spanner.executor_v1.types.cloud_executor import (
    ListCloudBackupOperationsAction,
)
from google.spanner.executor_v1.types.cloud_executor import ListCloudBackupsAction
from google.spanner.executor_v1.types.cloud_executor import (
    ListCloudDatabaseOperationsAction,
)
from google.spanner.executor_v1.types.cloud_executor import ListCloudDatabasesAction
from google.spanner.executor_v1.types.cloud_executor import (
    ListCloudInstanceConfigsAction,
)
from google.spanner.executor_v1.types.cloud_executor import ListCloudInstancesAction
from google.spanner.executor_v1.types.cloud_executor import MutationAction
from google.spanner.executor_v1.types.cloud_executor import OperationResponse
from google.spanner.executor_v1.types.cloud_executor import PartitionedUpdateAction
from google.spanner.executor_v1.types.cloud_executor import QueryAction
from google.spanner.executor_v1.types.cloud_executor import QueryResult
from google.spanner.executor_v1.types.cloud_executor import ReadAction
from google.spanner.executor_v1.types.cloud_executor import ReadResult
from google.spanner.executor_v1.types.cloud_executor import (
    ReconfigureCloudDatabaseAction,
)
from google.spanner.executor_v1.types.cloud_executor import RestoreCloudDatabaseAction
from google.spanner.executor_v1.types.cloud_executor import SpannerAction
from google.spanner.executor_v1.types.cloud_executor import SpannerActionOutcome
from google.spanner.executor_v1.types.cloud_executor import SpannerAsyncActionRequest
from google.spanner.executor_v1.types.cloud_executor import SpannerAsyncActionResponse
from google.spanner.executor_v1.types.cloud_executor import StartBatchTransactionAction
from google.spanner.executor_v1.types.cloud_executor import StartTransactionAction
from google.spanner.executor_v1.types.cloud_executor import TableMetadata
from google.spanner.executor_v1.types.cloud_executor import TransactionExecutionOptions
from google.spanner.executor_v1.types.cloud_executor import UpdateCloudBackupAction
from google.spanner.executor_v1.types.cloud_executor import UpdateCloudDatabaseAction
from google.spanner.executor_v1.types.cloud_executor import UpdateCloudDatabaseDdlAction
from google.spanner.executor_v1.types.cloud_executor import UpdateCloudInstanceAction
from google.spanner.executor_v1.types.cloud_executor import (
    UpdateUserInstanceConfigAction,
)
from google.spanner.executor_v1.types.cloud_executor import Value
from google.spanner.executor_v1.types.cloud_executor import ValueList
from google.spanner.executor_v1.types.cloud_executor import WriteMutationsAction

__all__ = (
    "SpannerExecutorProxyClient",
    "SpannerExecutorProxyAsyncClient",
    "AdminAction",
    "AdminResult",
    "BatchDmlAction",
    "BatchPartition",
    "CancelOperationAction",
    "ChangeStreamRecord",
    "ChildPartitionsRecord",
    "CloseBatchTransactionAction",
    "CloudBackupResponse",
    "CloudDatabaseResponse",
    "CloudInstanceConfigResponse",
    "CloudInstanceResponse",
    "ColumnMetadata",
    "Concurrency",
    "CopyCloudBackupAction",
    "CreateCloudBackupAction",
    "CreateCloudDatabaseAction",
    "CreateCloudInstanceAction",
    "CreateUserInstanceConfigAction",
    "DataChangeRecord",
    "DeleteCloudBackupAction",
    "DeleteCloudInstanceAction",
    "DeleteUserInstanceConfigAction",
    "DmlAction",
    "DropCloudDatabaseAction",
    "ExecuteChangeStreamQuery",
    "ExecutePartitionAction",
    "FinishTransactionAction",
    "GenerateDbPartitionsForQueryAction",
    "GenerateDbPartitionsForReadAction",
    "GetCloudBackupAction",
    "GetCloudDatabaseAction",
    "GetCloudInstanceAction",
    "GetCloudInstanceConfigAction",
    "GetOperationAction",
    "HeartbeatRecord",
    "KeyRange",
    "KeySet",
    "ListCloudBackupOperationsAction",
    "ListCloudBackupsAction",
    "ListCloudDatabaseOperationsAction",
    "ListCloudDatabasesAction",
    "ListCloudInstanceConfigsAction",
    "ListCloudInstancesAction",
    "MutationAction",
    "OperationResponse",
    "PartitionedUpdateAction",
    "QueryAction",
    "QueryResult",
    "ReadAction",
    "ReadResult",
    "ReconfigureCloudDatabaseAction",
    "RestoreCloudDatabaseAction",
    "SpannerAction",
    "SpannerActionOutcome",
    "SpannerAsyncActionRequest",
    "SpannerAsyncActionResponse",
    "StartBatchTransactionAction",
    "StartTransactionAction",
    "TableMetadata",
    "TransactionExecutionOptions",
    "UpdateCloudBackupAction",
    "UpdateCloudDatabaseAction",
    "UpdateCloudDatabaseDdlAction",
    "UpdateCloudInstanceAction",
    "UpdateUserInstanceConfigAction",
    "Value",
    "ValueList",
    "WriteMutationsAction",
)
