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
// Source file:   /home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/wheel_motor/SetVelocity.1.0.uavcan
// Generated at:  2025-06-26 11:12:32.331008 UTC
// Is deprecated: no
// Fixed port-ID: None
// Full name:     dinosaurs.actuator.wheel_motor.SetVelocity
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

#ifndef DINOSAURS_ACTUATOR_WHEEL_MOTOR_SET_VELOCITY_1_0_INCLUDED_
#define DINOSAURS_ACTUATOR_WHEEL_MOTOR_SET_VELOCITY_1_0_INCLUDED_

#include <nunavut/support/serialization.h>
#include <stdint.h>
#include <stdlib.h>
#include <uavcan/si/unit/velocity/Scalar_1_0.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 1693710260,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/wheel_motor/SetVelocity.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/wheel_motor/SetVelocity.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/wheel_motor/SetVelocity.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/wheel_motor/SetVelocity.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/wheel_motor/SetVelocity.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

/// This type does not have a fixed port-ID. See https://forum.opencyphal.org/t/choosing-message-and-service-ids/889
#define dinosaurs_actuator_wheel_motor_SetVelocity_1_0_HAS_FIXED_PORT_ID_ false

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.actuator.wheel_motor.SetVelocity.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_actuator_wheel_motor_SetVelocity_1_0_FULL_NAME_             "dinosaurs.actuator.wheel_motor.SetVelocity"
#define dinosaurs_actuator_wheel_motor_SetVelocity_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.actuator.wheel_motor.SetVelocity.1.0"

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.actuator.wheel_motor.SetVelocity.Request.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_FULL_NAME_             "dinosaurs.actuator.wheel_motor.SetVelocity.Request"
#define dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.actuator.wheel_motor.SetVelocity.Request.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_EXTENT_BYTES_                    65UL
#define dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 65UL
static_assert(dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_EXTENT_BYTES_ >= dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// Array metadata for: uavcan.si.unit.velocity.Scalar.1.0[<=16] velocity
#define dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_velocity_ARRAY_CAPACITY_           16U
#define dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_velocity_ARRAY_IS_VARIABLE_LENGTH_ true

typedef struct
{
    /// uavcan.si.unit.velocity.Scalar.1.0[<=16] velocity
    struct  /// Array address equivalence guarantee: &elements[0] == &velocity
    {
        uavcan_si_unit_velocity_Scalar_1_0 elements[dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_velocity_ARRAY_CAPACITY_];
        size_t count;
    } velocity;
} dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_serialize_(
    const dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 520UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // uavcan.si.unit.velocity.Scalar.1.0[<=16] velocity
        if (obj->velocity.count > 16)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->velocity.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index0_ = 0U; _index0_ < obj->velocity.count; ++_index0_)
        {
            size_t _size_bytes0_ = 4UL;  // Nested object (max) size, in bytes.
            int8_t _err0_ = uavcan_si_unit_velocity_Scalar_1_0_serialize_(
                &obj->velocity.elements[_index0_], &buffer[offset_bits / 8U], &_size_bytes0_);
            if (_err0_ < 0)
            {
                return _err0_;
            }
            // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
            offset_bits += _size_bytes0_ * 8U;  // Advance by the size of the nested object.
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
static inline int8_t dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_deserialize_(
    dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // uavcan.si.unit.velocity.Scalar.1.0[<=16] velocity
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->velocity.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->velocity.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->velocity.count > 16U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index1_ = 0U; _index1_ < out_obj->velocity.count; ++_index1_)
    {
        {
            size_t _size_bytes1_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
            const int8_t _err2_ = uavcan_si_unit_velocity_Scalar_1_0_deserialize_(
                &out_obj->velocity.elements[_index1_], &buffer[offset_bits / 8U], &_size_bytes1_);
            if (_err2_ < 0)
            {
                return _err2_;
            }
            offset_bits += _size_bytes1_ * 8U;  // Advance by the size of the nested serialized representation.
        }
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_initialize_(dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = dinosaurs_actuator_wheel_motor_SetVelocity_Request_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.actuator.wheel_motor.SetVelocity.Response.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_FULL_NAME_             "dinosaurs.actuator.wheel_motor.SetVelocity.Response"
#define dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.actuator.wheel_motor.SetVelocity.Response.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_EXTENT_BYTES_                    4UL
#define dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 4UL
static_assert(dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_EXTENT_BYTES_ >= dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// saturated int32 SET_SUCCESS = 0
#define dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_SET_SUCCESS (0L)

/// saturated int32 FAILED = 1
#define dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_FAILED (1L)

/// saturated int32 PARAMETER_NOT_INIT = 2
#define dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_PARAMETER_NOT_INIT (2L)

typedef struct
{
    /// saturated int32 status
    int32_t status;
} dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_serialize_(
    const dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 32UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // saturated int32 status
        // Saturation code not emitted -- native representation matches the serialized representation.
        const int8_t _err3_ = nunavutSetIxx(&buffer[0], capacity_bytes, offset_bits, obj->status, 32U);
        if (_err3_ < 0)
        {
            return _err3_;
        }
        offset_bits += 32U;
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad1_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err4_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad1_);  // Optimize?
        if (_err4_ < 0)
        {
            return _err4_;
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
static inline int8_t dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_deserialize_(
    dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // saturated int32 status
    out_obj->status = nunavutGetI32(&buffer[0], capacity_bytes, offset_bits, 32);
    offset_bits += 32U;
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_initialize_(dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = dinosaurs_actuator_wheel_motor_SetVelocity_Response_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // DINOSAURS_ACTUATOR_WHEEL_MOTOR_SET_VELOCITY_1_0_INCLUDED_
