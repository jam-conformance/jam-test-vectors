from bin_to_json import StfTestVector
from jam_types import (
    Null,
    OpaqueHash,
    Struct,
    PreimagesXt,
    Enum,
    TimeSlot,
    ServiceId,
    U32,
    ByteSequence,
    Errno,
    ServicesStatistics,
    Vec
)
from jam_types import class_name as n

class PreimagesBlobsMapEntry(Struct):
    type_mapping = [
        ('hash', n(OpaqueHash)),
        ('blob', n(ByteSequence)),
    ]

class PreimagesRequestsMapKey(Struct):
    type_mapping = [
        ('hash', n(OpaqueHash)),
        ('length', n(U32)),
    ]

class PreimagesRequestsMapEntry(Struct):
    type_mapping = [
        ('key', n(PreimagesRequestsMapKey)),
        ('value', 'Vec<TimeSlot>'),
    ]

class PreimagesServiceAccount(Struct):
    type_mapping = [
        ('preimage_blobs', 'Vec<PreimagesBlobsMapEntry>'),
        ('preimage_requests', 'Vec<PreimagesRequestsMapEntry>'),
    ]

class PreimagesServiceAccountMapEntry(Struct):
    type_mapping = [
        ('id', n(ServiceId)),
        ('data', n(PreimagesServiceAccount))
    ]    

class PreimagesServiceAccountMap(Vec):
    sub_type = n(PreimagesServiceAccountMapEntry)

class PreimagesState(Struct):
    type_mapping = [
        ('accounts', n(PreimagesServiceAccountMap)),
        ('statistics', n(ServicesStatistics)),
    ]

class PreimagesInput(Struct):
    type_mapping = [
        ('preimages', n(PreimagesXt)),
        ('slot', n(TimeSlot)),
    ]

class PreimagesOutput(Enum):
    type_mapping = {
        0: ('ok', n(Null)),
        1: ('err', n(Errno))
    }

class PreimagesTestVector(StfTestVector):
    state_class = n(PreimagesState)
    input_class = n(PreimagesInput)
    output_class = n(PreimagesOutput)
    errno_map = {
        0: "preimage_unneeded",
        1: "preimages_not_sorted_unique",
        2: "preimages_too_big",
    }
