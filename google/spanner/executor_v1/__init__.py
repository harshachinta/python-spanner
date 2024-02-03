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
from google.spanner.executor_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.spanner_executor_proxy import SpannerExecutorProxyClient
from .services.spanner_executor_proxy import SpannerExecutorProxyAsyncClient

from .types.cloud_executor import AdminAction
from .types.cloud_executor import AdminResult
from .types.cloud_executor import BatchDmlAction
from .types.cloud_executor import BatchPartition
from .types.cloud_executor import CancelOperationAction
from .types.cloud_executor import ChangeStreamRecord
from .types.cloud_executor import ChildPartitionsRecord
from .types.cloud_executor import CloseBatchTransactionAction
from .types.cloud_executor import CloudBackupResponse
from .types.cloud_executor import CloudDatabaseResponse
from .types.cloud_executor import CloudInstanceConfigResponse
from .types.cloud_executor import CloudInstanceResponse
from .types.cloud_executor import ColumnMetadata
from .types.cloud_executor import Concurrency
from .types.cloud_executor import CopyCloudBackupAction
from .types.cloud_executor import CreateCloudBackupAction
from .types.cloud_executor import CreateCloudDatabaseAction
from .types.cloud_executor import CreateCloudInstanceAction
from .types.cloud_executor import CreateUserInstanceConfigAction
from .types.cloud_executor import DataChangeRecord
from .types.cloud_executor import DeleteCloudBackupAction
from .types.cloud_executor import DeleteCloudInstanceAction
from .types.cloud_executor import DeleteUserInstanceConfigAction
from .types.cloud_executor import DmlAction
from .types.cloud_executor import DropCloudDatabaseAction
from .types.cloud_executor import ExecuteChangeStreamQuery
from .types.cloud_executor import ExecutePartitionAction
from .types.cloud_executor import FinishTransactionAction
from .types.cloud_executor import GenerateDbPartitionsForQueryAction
from .types.cloud_executor import GenerateDbPartitionsForReadAction
from .types.cloud_executor import GetCloudBackupAction
from .types.cloud_executor import GetCloudDatabaseAction
from .types.cloud_executor import GetCloudInstanceAction
from .types.cloud_executor import GetCloudInstanceConfigAction
from .types.cloud_executor import GetOperationAction
from .types.cloud_executor import HeartbeatRecord
from .types.cloud_executor import KeyRange
from .types.cloud_executor import KeySet
from .types.cloud_executor import ListCloudBackupOperationsAction
from .types.cloud_executor import ListCloudBackupsAction
from .types.cloud_executor import ListCloudDatabaseOperationsAction
from .types.cloud_executor import ListCloudDatabasesAction
from .types.cloud_executor import ListCloudInstanceConfigsAction
from .types.cloud_executor import ListCloudInstancesAction
from .types.cloud_executor import MutationAction
from .types.cloud_executor import OperationResponse
from .types.cloud_executor import PartitionedUpdateAction
from .types.cloud_executor import QueryAction
from .types.cloud_executor import QueryResult
from .types.cloud_executor import ReadAction
from .types.cloud_executor import ReadResult
from .types.cloud_executor import ReconfigureCloudDatabaseAction
from .types.cloud_executor import RestoreCloudDatabaseAction
from .types.cloud_executor import SpannerAction
from .types.cloud_executor import SpannerActionOutcome
from .types.cloud_executor import SpannerAsyncActionRequest
from .types.cloud_executor import SpannerAsyncActionResponse
from .types.cloud_executor import StartBatchTransactionAction
from .types.cloud_executor import StartTransactionAction
from .types.cloud_executor import TableMetadata
from .types.cloud_executor import TransactionExecutionOptions
from .types.cloud_executor import UpdateCloudBackupAction
from .types.cloud_executor import UpdateCloudDatabaseAction
from .types.cloud_executor import UpdateCloudDatabaseDdlAction
from .types.cloud_executor import UpdateCloudInstanceAction
from .types.cloud_executor import UpdateUserInstanceConfigAction
from .types.cloud_executor import Value
from .types.cloud_executor import ValueList
from .types.cloud_executor import WriteMutationsAction

__all__ = (
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
    "SpannerExecutorProxyClient",
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
