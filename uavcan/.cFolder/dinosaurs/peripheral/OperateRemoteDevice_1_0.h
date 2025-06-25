// This is an AUTO-GENERATED Cyphal DSDL data type implementation. Curious? See https://opencyphal.org.
// You shouldn't attempt to edit this file.
//
// Checking this file under version control is not recommended unless it is used as part of a high-SIL
// safety-critical codebase. The typical usage scenario is to generate it as part of the build process.
//
// To avoid conflicts with definitions given in the source DSDL file, all entities created by the code generator
// are named with an underscore at the end, like foo_bar_().
//
// Generator:     nunavut-2.3.1 (serialization was enabled)
// Source file:   /home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/peripheral/OperateRemoteDevice.1.0.uavcan
// Generated at:  2025-06-26 11:12:32.631112 UTC
// Is deprecated: no
// Fixed port-ID: None
// Full name:     dinosaurs.peripheral.OperateRemoteDevice
// Version:       1.0
//
// Platform
//     python_implementation:  CPython
//     python_version:  3.10.12
//     python_release_level:  final
//     python_build:  ('main', 'May 27 2025 17:12:29')
//     python_compiler:  GCC 11.4.0
//     python_revision:
//     python_xoptions:  {}
//     runtime_platform:  Linux-6.8.0-60-generic-x86_64-with-glibc2.35
//
// Language Options
//     target_endianness:  any
//     omit_float_serialization_support:  False
//     enable_serialization_asserts:  False
//     enable_override_variable_array_capacity:  False
//     cast_format:  (({type}) {value})

#ifndef DINOSAURS_PERIPHERAL_OPERATE_REMOTE_DEVICE_1_0_INCLUDED_
#define DINOSAURS_PERIPHERAL_OPERATE_REMOTE_DEVICE_1_0_INCLUDED_

#include <nunavut/support/serialization.h>
#include <stdint.h>
#include <stdlib.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 1693710260,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/peripheral/OperateRemoteDevice.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/peripheral/OperateRemoteDevice.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/peripheral/OperateRemoteDevice.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/peripheral/OperateRemoteDevice.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/peripheral/OperateRemoteDevice.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

/// This type does not have a fixed port-ID. See https://forum.opencyphal.org/t/choosing-message-and-service-ids/889
#define dinosaurs_peripheral_OperateRemoteDevice_1_0_HAS_FIXED_PORT_ID_ false

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.peripheral.OperateRemoteDevice.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_peripheral_OperateRemoteDevice_1_0_FULL_NAME_             "dinosaurs.peripheral.OperateRemoteDevice"
#define dinosaurs_peripheral_OperateRemoteDevice_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.peripheral.OperateRemoteDevice.1.0"

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.peripheral.OperateRemoteDevice.Request.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_FULL_NAME_             "dinosaurs.peripheral.OperateRemoteDevice.Request"
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.peripheral.OperateRemoteDevice.Request.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_EXTENT_BYTES_                    340UL
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 340UL
static_assert(dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_EXTENT_BYTES_ >= dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// saturated uint8 OPEN = 0
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_OPEN (0U)

/// saturated uint8 CLOSE = 1
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_CLOSE (1U)

/// saturated uint8 ONE_SHOT = 2
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_ONE_SHOT (2U)

/// Array metadata for: saturated uint8[<=80] name
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_name_ARRAY_CAPACITY_           80U
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_name_ARRAY_IS_VARIABLE_LENGTH_ true

/// Array metadata for: saturated uint8[<=256] param
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_param_ARRAY_CAPACITY_           256U
#define dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_param_ARRAY_IS_VARIABLE_LENGTH_ true

typedef struct
{
    /// saturated uint8 method
    uint8_t method;

    /// saturated uint8[<=80] name
    struct  /// Array address equivalence guarantee: &elements[0] == &name
    {
        uint8_t elements[dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_name_ARRAY_CAPACITY_];
        size_t count;
    } name;

    /// saturated uint8[<=256] param
    struct  /// Array address equivalence guarantee: &elements[0] == &param
    {
        uint8_t elements[dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_param_ARRAY_CAPACITY_];
        size_t count;
    } param;
} dinosaurs_peripheral_OperateRemoteDevice_Request_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_serialize_(
    const dinosaurs_peripheral_OperateRemoteDevice_Request_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 2720UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // saturated uint8 method
        // Saturation code not emitted -- native representation matches the serialized representation.
        buffer[offset_bits / 8U] = (uint8_t)(obj->method);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
    }
    {   // saturated uint8[<=80] name
        if (obj->name.count > 80)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->name.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index0_ = 0U; _index0_ < obj->name.count; ++_index0_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->name.elements[_index0_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
    }
    {   // saturated uint8[<=256] param
        if (obj->param.count > 256)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint16
        const int8_t _err0_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, obj->param.count, 16U);
        if (_err0_ < 0)
        {
            return _err0_;
        }
        offset_bits += 16U;
        for (size_t _index1_ = 0U; _index1_ < obj->param.count; ++_index1_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->param.elements[_index1_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad0_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err1_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad0_);  // Optimize?
        if (_err1_ < 0)
        {
            return _err1_;
        }
        offset_bits += _pad0_;
    }
    // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
    *inout_buffer_size_bytes = (size_t) (offset_bits / 8U);
    return NUNAVUT_SUCCESS;
}

/// Deserialize an instance from the provided buffer.
/// The lifetime of the resulting object is independent of the original buffer.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original buffer where possible.
///
/// @param obj      The object to update from the provided serialized representation.
///
/// @param buffer   The source buffer containing the serialized representation. There are no alignment requirements.
///                 If the buffer is shorter or longer than expected, it will be implicitly zero-extended or truncated,
///                 respectively; see Specification for "implicit zero extension" and "implicit truncation" rules.
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the supplied serialized
///                                 representation, in bytes. Upon return this value will be updated with the
///                                 size of the consumed fragment of the serialized representation (in bytes),
///                                 which may be smaller due to the implicit truncation rule, but it is guaranteed
///                                 to never exceed the original buffer size even if the implicit zero extension rule
///                                 was activated. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_deserialize_(
    dinosaurs_peripheral_OperateRemoteDevice_Request_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
{
    if ((out_obj == NULL) || (inout_buffer_size_bytes == NULL) || ((buffer == NULL) && (0 != *inout_buffer_size_bytes)))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    if (buffer == NULL)
    {
        buffer = (const uint8_t*)"";
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    const size_t capacity_bits = capacity_bytes * (size_t) 8U;
    size_t offset_bits = 0U;
    // saturated uint8 method
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->method = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->method = 0U;
    }
    offset_bits += 8U;
    // saturated uint8[<=80] name
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->name.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->name.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->name.count > 80U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index2_ = 0U; _index2_ < out_obj->name.count; ++_index2_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->name.elements[_index2_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->name.elements[_index2_] = 0U;
        }
        offset_bits += 8U;
    }
    // saturated uint8[<=256] param
    // Array length prefix: truncated uint16
    out_obj->param.count = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;
    if (out_obj->param.count > 256U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index3_ = 0U; _index3_ < out_obj->param.count; ++_index3_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->param.elements[_index3_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->param.elements[_index3_] = 0U;
        }
        offset_bits += 8U;
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_initialize_(dinosaurs_peripheral_OperateRemoteDevice_Request_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = dinosaurs_peripheral_OperateRemoteDevice_Request_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.peripheral.OperateRemoteDevice.Response.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_FULL_NAME_             "dinosaurs.peripheral.OperateRemoteDevice.Response"
#define dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.peripheral.OperateRemoteDevice.Response.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_EXTENT_BYTES_                    259UL
#define dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 259UL
static_assert(dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_EXTENT_BYTES_ >= dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// saturated uint8 SUCESS = 0
#define dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_SUCESS (0U)

/// saturated uint8 EPERM = 1
#define dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_EPERM (1U)

/// saturated uint8 EINVAL = 22
#define dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_EINVAL (22U)

/// Array metadata for: saturated uint8[<=256] value
#define dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_value_ARRAY_CAPACITY_           256U
#define dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_value_ARRAY_IS_VARIABLE_LENGTH_ true

typedef struct
{
    /// saturated uint8 result
    uint8_t result;

    /// saturated uint8[<=256] value
    struct  /// Array address equivalence guarantee: &elements[0] == &value
    {
        uint8_t elements[dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_value_ARRAY_CAPACITY_];
        size_t count;
    } value;
} dinosaurs_peripheral_OperateRemoteDevice_Response_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_serialize_(
    const dinosaurs_peripheral_OperateRemoteDevice_Response_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 2072UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // saturated uint8 result
        // Saturation code not emitted -- native representation matches the serialized representation.
        buffer[offset_bits / 8U] = (uint8_t)(obj->result);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
    }
    {   // saturated uint8[<=256] value
        if (obj->value.count > 256)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint16
        const int8_t _err2_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, obj->value.count, 16U);
        if (_err2_ < 0)
        {
            return _err2_;
        }
        offset_bits += 16U;
        for (size_t _index4_ = 0U; _index4_ < obj->value.count; ++_index4_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->value.elements[_index4_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad1_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err3_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad1_);  // Optimize?
        if (_err3_ < 0)
        {
            return _err3_;
        }
        offset_bits += _pad1_;
    }
    // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
    *inout_buffer_size_bytes = (size_t) (offset_bits / 8U);
    return NUNAVUT_SUCCESS;
}

/// Deserialize an instance from the provided buffer.
/// The lifetime of the resulting object is independent of the original buffer.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original buffer where possible.
///
/// @param obj      The object to update from the provided serialized representation.
///
/// @param buffer   The source buffer containing the serialized representation. There are no alignment requirements.
///                 If the buffer is shorter or longer than expected, it will be implicitly zero-extended or truncated,
///                 respectively; see Specification for "implicit zero extension" and "implicit truncation" rules.
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the supplied serialized
///                                 representation, in bytes. Upon return this value will be updated with the
///                                 size of the consumed fragment of the serialized representation (in bytes),
///                                 which may be smaller due to the implicit truncation rule, but it is guaranteed
///                                 to never exceed the original buffer size even if the implicit zero extension rule
///                                 was activated. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_deserialize_(
    dinosaurs_peripheral_OperateRemoteDevice_Response_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
{
    if ((out_obj == NULL) || (inout_buffer_size_bytes == NULL) || ((buffer == NULL) && (0 != *inout_buffer_size_bytes)))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    if (buffer == NULL)
    {
        buffer = (const uint8_t*)"";
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    const size_t capacity_bits = capacity_bytes * (size_t) 8U;
    size_t offset_bits = 0U;
    // saturated uint8 result
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->result = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->result = 0U;
    }
    offset_bits += 8U;
    // saturated uint8[<=256] value
    // Array length prefix: truncated uint16
    out_obj->value.count = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;
    if (out_obj->value.count > 256U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index5_ = 0U; _index5_ < out_obj->value.count; ++_index5_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->value.elements[_index5_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->value.elements[_index5_] = 0U;
        }
        offset_bits += 8U;
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_initialize_(dinosaurs_peripheral_OperateRemoteDevice_Response_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = dinosaurs_peripheral_OperateRemoteDevice_Response_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // DINOSAURS_PERIPHERAL_OPERATE_REMOTE_DEVICE_1_0_INCLUDED_
