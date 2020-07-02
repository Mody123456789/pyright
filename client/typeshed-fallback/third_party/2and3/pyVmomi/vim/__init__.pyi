from datetime import datetime
from enum import Enum
from typing import Any, List

from ..vmodl.query import PropertyCollector
from . import event, fault, view
from .event import EventManager
from .option import OptionManager
from .view import ViewManager

class ManagedObject: ...

class ManagedEntity(ManagedObject):
    _moId: str
    obj: None
    name: str

class ServiceInstanceContent:
    setting: OptionManager
    propertyCollector: PropertyCollector
    rootFolder: Folder
    viewManager: ViewManager
    perfManager: PerformanceManager
    eventManager: EventManager

class ServiceInstance:
    content: ServiceInstanceContent
    def CurrentTime(self) -> Any: ...

class PerformanceManager:
    class MetricId:
        def __init__(self, counterId: Any, instance: Any): ...
    class PerfCounterInfo:
        key: int
        groupInfo: Any
        nameInfo: Any
        rollupType: Any
    class QuerySpec:
        entity: ManagedEntity
        metricId: List[PerformanceManager.MetricId]
        intervalId: int
        maxSample: int
        startTime: datetime
    class EntityMetricBase:
        value: Any
        entity: ManagedEntity
    def QueryPerfCounterByLevel(self, collection_level: int) -> List[PerformanceManager.PerfCounterInfo]: ...
    def QueryPerf(self, querySpec: List[PerformanceManager.QuerySpec]) -> List[PerformanceManager.EntityMetricBase]: ...

class ClusterComputeResource(ManagedEntity): ...
class ComputeResource(ManagedEntity): ...
class Datacenter(ManagedEntity): ...
class Datastore(ManagedEntity): ...
class Folder(ManagedEntity): ...
class HostSystem(ManagedEntity): ...
class VirtualMachine(ManagedEntity): ...

class VirtualMachinePowerState(Enum):
    poweredOff: int
    poweredOn: int
    suspended: int
