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
// Source file:   /home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/sensor/rfid/RfidQuery.1.0.uavcan
// Generated at:  2025-06-26 11:12:32.527569 UTC
// Is deprecated: no
// Fixed port-ID: None
// Full name:     dinosaurs.sensor.rfid.RfidQuery
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

#ifndef DINOSAURS_SENSOR_RFID_RFID_QUERY_1_0_INCLUDED_
#define DINOSAURS_SENSOR_RFID_RFID_QUERY_1_0_INCLUDED_

#include <nunavut/support/serialization.h>
#include <stdint.h>
#include <stdlib.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 1693710260,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/sensor/rfid/RfidQuery.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/sensor/rfid/RfidQuery.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/sensor/rfid/RfidQuery.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/sensor/rfid/RfidQuery.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/sensor/rfid/RfidQuery.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

/// This type does not have a fixed port-ID. See https://forum.opencyphal.org/t/choosing-message-and-service-ids/889
#define dinosaurs_sensor_rfid_RfidQuery_1_0_HAS_FIXED_PORT_ID_ false

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.sensor.rfid.RfidQuery.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_sensor_rfid_RfidQuery_1_0_FULL_NAME_             "dinosaurs.sensor.rfid.RfidQuery"
#define dinosaurs_sensor_rfid_RfidQuery_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.sensor.rfid.RfidQuery.1.0"

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.sensor.rfid.RfidQuery.Request.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_sensor_rfid_RfidQuery_Request_1_0_FULL_NAME_             "dinosaurs.sensor.rfid.RfidQuery.Request"
#define dinosaurs_sensor_rfid_RfidQuery_Request_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.sensor.rfid.RfidQuery.Request.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define dinosaurs_sensor_rfid_RfidQuery_Request_1_0_EXTENT_BYTES_                    1UL
#define dinosaurs_sensor_rfid_RfidQuery_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 1UL
static_assert(dinosaurs_sensor_rfid_RfidQuery_Request_1_0_EXTENT_BYTES_ >= dinosaurs_sensor_rfid_RfidQuery_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

typedef struct
{
    /// saturated uint8 rfid_id
    uint8_t rfid_id;
} dinosaurs_sensor_rfid_RfidQuery_Request_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see dinosaurs_sensor_rfid_RfidQuery_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_sensor_rfid_RfidQuery_Request_1_0_serialize_(
    const dinosaurs_sensor_rfid_RfidQuery_Request_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 8UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // saturated uint8 rfid_id
        // Saturation code not emitted -- native representation matches the serialized representation.
        buffer[offset_bits / 8U] = (uint8_t)(obj->rfid_id);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad0_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err0_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad0_);  // Optimize?
        if (_err0_ < 0)
        {
            return _err0_;
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
static inline int8_t dinosaurs_sensor_rfid_RfidQuery_Request_1_0_deserialize_(
    dinosaurs_sensor_rfid_RfidQuery_Request_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // saturated uint8 rfid_id
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->rfid_id = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->rfid_id = 0U;
    }
    offset_bits += 8U;
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void dinosaurs_sensor_rfid_RfidQuery_Request_1_0_initialize_(dinosaurs_sensor_rfid_RfidQuery_Request_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = dinosaurs_sensor_rfid_RfidQuery_Request_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.sensor.rfid.RfidQuery.Response.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_FULL_NAME_             "dinosaurs.sensor.rfid.RfidQuery.Response"
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.sensor.rfid.RfidQuery.Response.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_EXTENT_BYTES_                    292UL
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 292UL
static_assert(dinosaurs_sensor_rfid_RfidQuery_Response_1_0_EXTENT_BYTES_ >= dinosaurs_sensor_rfid_RfidQuery_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// saturated int32 STATUS_OK = 0
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_STATUS_OK (0L)

/// saturated uint8 MODE_DISABLE_RFID = 0
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_MODE_DISABLE_RFID (0U)

/// saturated uint8 MODE_ENABLE_RFID = 1
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_MODE_ENABLE_RFID (1U)

/// saturated uint8 MODE_MULTI_TAG_READ = 2
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_MODE_MULTI_TAG_READ (2U)

/// saturated uint8 MODE_SINGLE_TAG_READ = 3
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_MODE_SINGLE_TAG_READ (3U)

/// saturated uint8 FRE_NORTH_AMERICA = 1
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_FRE_NORTH_AMERICA (1U)

/// saturated uint8 FRE_CHINA_1 = 6
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_FRE_CHINA_1 (6U)

/// saturated uint8 FRE_EUROPE = 8
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_FRE_EUROPE (8U)

/// saturated uint8 FRE_CHINA_2 = 10
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_FRE_CHINA_2 (10U)

/// saturated uint8 FRE_FULL = 255
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_FRE_FULL (255U)

/// Array metadata for: saturated uint8[<=15] bootloader_version
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_bootloader_version_ARRAY_CAPACITY_           15U
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_bootloader_version_ARRAY_IS_VARIABLE_LENGTH_ true

/// Array metadata for: saturated uint8[<=15] hardware_version
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_hardware_version_ARRAY_CAPACITY_           15U
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_hardware_version_ARRAY_IS_VARIABLE_LENGTH_ true

/// Array metadata for: saturated uint8[<=15] firmware_version
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_firmware_version_ARRAY_CAPACITY_           15U
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_firmware_version_ARRAY_IS_VARIABLE_LENGTH_ true

/// Array metadata for: saturated uint8[<=30] serial_number
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_serial_number_ARRAY_CAPACITY_           30U
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_serial_number_ARRAY_IS_VARIABLE_LENGTH_ true

/// Array metadata for: saturated uint32[<=50] channel_list
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_channel_list_ARRAY_CAPACITY_           50U
#define dinosaurs_sensor_rfid_RfidQuery_Response_1_0_channel_list_ARRAY_IS_VARIABLE_LENGTH_ true

typedef struct
{
    /// saturated int32 status
    int32_t status;

    /// saturated uint8[<=15] bootloader_version
    struct  /// Array address equivalence guarantee: &elements[0] == &bootloader_version
    {
        uint8_t elements[dinosaurs_sensor_rfid_RfidQuery_Response_1_0_bootloader_version_ARRAY_CAPACITY_];
        size_t count;
    } bootloader_version;

    /// saturated uint8[<=15] hardware_version
    struct  /// Array address equivalence guarantee: &elements[0] == &hardware_version
    {
        uint8_t elements[dinosaurs_sensor_rfid_RfidQuery_Response_1_0_hardware_version_ARRAY_CAPACITY_];
        size_t count;
    } hardware_version;

    /// saturated uint8[<=15] firmware_version
    struct  /// Array address equivalence guarantee: &elements[0] == &firmware_version
    {
        uint8_t elements[dinosaurs_sensor_rfid_RfidQuery_Response_1_0_firmware_version_ARRAY_CAPACITY_];
        size_t count;
    } firmware_version;

    /// saturated uint8[<=30] serial_number
    struct  /// Array address equivalence guarantee: &elements[0] == &serial_number
    {
        uint8_t elements[dinosaurs_sensor_rfid_RfidQuery_Response_1_0_serial_number_ARRAY_CAPACITY_];
        size_t count;
    } serial_number;

    /// saturated uint8 mode
    uint8_t mode;

    /// saturated uint16 transmit_power
    uint16_t transmit_power;

    /// saturated uint16 min_transmit_power
    uint16_t min_transmit_power;

    /// saturated uint16 max_transmit_power
    uint16_t max_transmit_power;

    /// saturated uint8 frequency_band
    uint8_t frequency_band;

    /// saturated uint32[<=50] channel_list
    struct  /// Array address equivalence guarantee: &elements[0] == &channel_list
    {
        uint32_t elements[dinosaurs_sensor_rfid_RfidQuery_Response_1_0_channel_list_ARRAY_CAPACITY_];
        size_t count;
    } channel_list;
} dinosaurs_sensor_rfid_RfidQuery_Response_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see dinosaurs_sensor_rfid_RfidQuery_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_sensor_rfid_RfidQuery_Response_1_0_serialize_(
    const dinosaurs_sensor_rfid_RfidQuery_Response_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 2336UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // saturated int32 status
        // Saturation code not emitted -- native representation matches the serialized representation.
        const int8_t _err1_ = nunavutSetIxx(&buffer[0], capacity_bytes, offset_bits, obj->status, 32U);
        if (_err1_ < 0)
        {
            return _err1_;
        }
        offset_bits += 32U;
    }
    {   // saturated uint8[<=15] bootloader_version
        if (obj->bootloader_version.count > 15)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->bootloader_version.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index0_ = 0U; _index0_ < obj->bootloader_version.count; ++_index0_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->bootloader_version.elements[_index0_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
    }
    {   // saturated uint8[<=15] hardware_version
        if (obj->hardware_version.count > 15)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->hardware_version.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index1_ = 0U; _index1_ < obj->hardware_version.count; ++_index1_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->hardware_version.elements[_index1_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
    }
    {   // saturated uint8[<=15] firmware_version
        if (obj->firmware_version.count > 15)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->firmware_version.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index2_ = 0U; _index2_ < obj->firmware_version.count; ++_index2_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->firmware_version.elements[_index2_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
    }
    {   // saturated uint8[<=30] serial_number
        if (obj->serial_number.count > 30)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->serial_number.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index3_ = 0U; _index3_ < obj->serial_number.count; ++_index3_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->serial_number.elements[_index3_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
    }
    {   // saturated uint8 mode
        // Saturation code not emitted -- native representation matches the serialized representation.
        buffer[offset_bits / 8U] = (uint8_t)(obj->mode);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
    }
    {   // saturated uint16 transmit_power
        // Saturation code not emitted -- native representation matches the serialized representation.
        const int8_t _err2_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, obj->transmit_power, 16U);
        if (_err2_ < 0)
        {
            return _err2_;
        }
        offset_bits += 16U;
    }
    {   // saturated uint16 min_transmit_power
        // Saturation code not emitted -- native representation matches the serialized representation.
        const int8_t _err3_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, obj->min_transmit_power, 16U);
        if (_err3_ < 0)
        {
            return _err3_;
        }
        offset_bits += 16U;
    }
    {   // saturated uint16 max_transmit_power
        // Saturation code not emitted -- native representation matches the serialized representation.
        const int8_t _err4_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, obj->max_transmit_power, 16U);
        if (_err4_ < 0)
        {
            return _err4_;
        }
        offset_bits += 16U;
    }
    {   // saturated uint8 frequency_band
        // Saturation code not emitted -- native representation matches the serialized representation.
        buffer[offset_bits / 8U] = (uint8_t)(obj->frequency_band);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
    }
    {   // saturated uint32[<=50] channel_list
        if (obj->channel_list.count > 50)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->channel_list.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index4_ = 0U; _index4_ < obj->channel_list.count; ++_index4_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            const int8_t _err5_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, obj->channel_list.elements[_index4_], 32U);
            if (_err5_ < 0)
            {
                return _err5_;
            }
            offset_bits += 32U;
        }
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad1_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err6_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad1_);  // Optimize?
        if (_err6_ < 0)
        {
            return _err6_;
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
static inline int8_t dinosaurs_sensor_rfid_RfidQuery_Response_1_0_deserialize_(
    dinosaurs_sensor_rfid_RfidQuery_Response_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // saturated uint8[<=15] bootloader_version
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->bootloader_version.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->bootloader_version.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->bootloader_version.count > 15U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index5_ = 0U; _index5_ < out_obj->bootloader_version.count; ++_index5_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->bootloader_version.elements[_index5_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->bootloader_version.elements[_index5_] = 0U;
        }
        offset_bits += 8U;
    }
    // saturated uint8[<=15] hardware_version
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->hardware_version.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->hardware_version.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->hardware_version.count > 15U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index6_ = 0U; _index6_ < out_obj->hardware_version.count; ++_index6_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->hardware_version.elements[_index6_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->hardware_version.elements[_index6_] = 0U;
        }
        offset_bits += 8U;
    }
    // saturated uint8[<=15] firmware_version
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->firmware_version.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->firmware_version.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->firmware_version.count > 15U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index7_ = 0U; _index7_ < out_obj->firmware_version.count; ++_index7_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->firmware_version.elements[_index7_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->firmware_version.elements[_index7_] = 0U;
        }
        offset_bits += 8U;
    }
    // saturated uint8[<=30] serial_number
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->serial_number.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->serial_number.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->serial_number.count > 30U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index8_ = 0U; _index8_ < out_obj->serial_number.count; ++_index8_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->serial_number.elements[_index8_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->serial_number.elements[_index8_] = 0U;
        }
        offset_bits += 8U;
    }
    // saturated uint8 mode
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->mode = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->mode = 0U;
    }
    offset_bits += 8U;
    // saturated uint16 transmit_power
    out_obj->transmit_power = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;
    // saturated uint16 min_transmit_power
    out_obj->min_transmit_power = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;
    // saturated uint16 max_transmit_power
    out_obj->max_transmit_power = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;
    // saturated uint8 frequency_band
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->frequency_band = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->frequency_band = 0U;
    }
    offset_bits += 8U;
    // saturated uint32[<=50] channel_list
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->channel_list.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->channel_list.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->channel_list.count > 50U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index9_ = 0U; _index9_ < out_obj->channel_list.count; ++_index9_)
    {
        out_obj->channel_list.elements[_index9_] = nunavutGetU32(&buffer[0], capacity_bytes, offset_bits, 32);
        offset_bits += 32U;
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void dinosaurs_sensor_rfid_RfidQuery_Response_1_0_initialize_(dinosaurs_sensor_rfid_RfidQuery_Response_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = dinosaurs_sensor_rfid_RfidQuery_Response_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // DINOSAURS_SENSOR_RFID_RFID_QUERY_1_0_INCLUDED_
