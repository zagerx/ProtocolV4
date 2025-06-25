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
// Source file:   /home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/bootstrap/updatee/UpdateeDescribe.1.0.uavcan
// Generated at:  2025-06-26 11:12:32.412673 UTC
// Is deprecated: no
// Fixed port-ID: None
// Full name:     dinosaurs.bootstrap.updatee.UpdateeDescribe
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

#ifndef DINOSAURS_BOOTSTRAP_UPDATEE_UPDATEE_DESCRIBE_1_0_INCLUDED_
#define DINOSAURS_BOOTSTRAP_UPDATEE_UPDATEE_DESCRIBE_1_0_INCLUDED_

#include <dinosaurs/bootstrap/updatee/Version_1_0.h>
#include <nunavut/support/serialization.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 1693710260,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/bootstrap/updatee/UpdateeDescribe.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/bootstrap/updatee/UpdateeDescribe.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/bootstrap/updatee/UpdateeDescribe.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/bootstrap/updatee/UpdateeDescribe.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/bootstrap/updatee/UpdateeDescribe.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

/// This type does not have a fixed port-ID. See https://forum.opencyphal.org/t/choosing-message-and-service-ids/889
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_HAS_FIXED_PORT_ID_ false

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.bootstrap.updatee.UpdateeDescribe.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_FULL_NAME_             "dinosaurs.bootstrap.updatee.UpdateeDescribe"
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.bootstrap.updatee.UpdateeDescribe.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_EXTENT_BYTES_                    400UL
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 312UL
static_assert(dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_EXTENT_BYTES_ >= dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// Array metadata for: saturated uint8[<=50] name
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_name_ARRAY_CAPACITY_           50U
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_name_ARRAY_IS_VARIABLE_LENGTH_ true

/// Array metadata for: saturated uint8[<=50] file_name
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_file_name_ARRAY_CAPACITY_           50U
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_file_name_ARRAY_IS_VARIABLE_LENGTH_ true

/// Array metadata for: saturated uint8[<=150] file_path
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_file_path_ARRAY_CAPACITY_           150U
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_file_path_ARRAY_IS_VARIABLE_LENGTH_ true

/// Array metadata for: saturated uint8[<=30] build_time
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_build_time_ARRAY_CAPACITY_           30U
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_build_time_ARRAY_IS_VARIABLE_LENGTH_ true

/// Array metadata for: saturated uint8[16] unique_id
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_unique_id_ARRAY_CAPACITY_           16U
#define dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_unique_id_ARRAY_IS_VARIABLE_LENGTH_ false

typedef struct
{
    /// saturated uint8[<=50] name
    struct  /// Array address equivalence guarantee: &elements[0] == &name
    {
        uint8_t elements[dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_name_ARRAY_CAPACITY_];
        size_t count;
    } name;

    /// saturated uint8[<=50] file_name
    struct  /// Array address equivalence guarantee: &elements[0] == &file_name
    {
        uint8_t elements[dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_file_name_ARRAY_CAPACITY_];
        size_t count;
    } file_name;

    /// saturated uint8[<=150] file_path
    struct  /// Array address equivalence guarantee: &elements[0] == &file_path
    {
        uint8_t elements[dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_file_path_ARRAY_CAPACITY_];
        size_t count;
    } file_path;

    /// saturated uint64 build_number
    uint64_t build_number;

    /// saturated uint8[<=30] build_time
    struct  /// Array address equivalence guarantee: &elements[0] == &build_time
    {
        uint8_t elements[dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_build_time_ARRAY_CAPACITY_];
        size_t count;
    } build_time;

    /// dinosaurs.bootstrap.updatee.Version.1.0 software_version
    dinosaurs_bootstrap_updatee_Version_1_0 software_version;

    /// saturated uint8[16] unique_id
    uint8_t unique_id[16];

    /// dinosaurs.bootstrap.updatee.Version.1.0 hardware_version
    dinosaurs_bootstrap_updatee_Version_1_0 hardware_version;
} dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_serialize_(
    const dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 2496UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // saturated uint8[<=50] name
        if (obj->name.count > 50)
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
    {   // saturated uint8[<=50] file_name
        if (obj->file_name.count > 50)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->file_name.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index1_ = 0U; _index1_ < obj->file_name.count; ++_index1_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->file_name.elements[_index1_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
    }
    {   // saturated uint8[<=150] file_path
        if (obj->file_path.count > 150)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->file_path.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index2_ = 0U; _index2_ < obj->file_path.count; ++_index2_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->file_path.elements[_index2_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
    }
    {   // saturated uint64 build_number
        // Saturation code not emitted -- native representation matches the serialized representation.
        const int8_t _err0_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, obj->build_number, 64U);
        if (_err0_ < 0)
        {
            return _err0_;
        }
        offset_bits += 64U;
    }
    {   // saturated uint8[<=30] build_time
        if (obj->build_time.count > 30)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->build_time.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        for (size_t _index3_ = 0U; _index3_ < obj->build_time.count; ++_index3_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->build_time.elements[_index3_]);  // C std, 6.3.1.3 Signed and unsigned integers
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
    {   // dinosaurs.bootstrap.updatee.Version.1.0 software_version
        size_t _size_bytes0_ = 2UL;  // Nested object (max) size, in bytes.
        int8_t _err2_ = dinosaurs_bootstrap_updatee_Version_1_0_serialize_(
            &obj->software_version, &buffer[offset_bits / 8U], &_size_bytes0_);
        if (_err2_ < 0)
        {
            return _err2_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes0_ * 8U;  // Advance by the size of the nested object.
    }
    {   // saturated uint8[16] unique_id
        const size_t _origin0_ = offset_bits;
        for (size_t _index4_ = 0U; _index4_ < 16UL; ++_index4_)
        {
            // Saturation code not emitted -- native representation matches the serialized representation.
            buffer[offset_bits / 8U] = (uint8_t)(obj->unique_id[_index4_]);  // C std, 6.3.1.3 Signed and unsigned integers
            offset_bits += 8U;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        (void) _origin0_;
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
    {   // dinosaurs.bootstrap.updatee.Version.1.0 hardware_version
        size_t _size_bytes1_ = 2UL;  // Nested object (max) size, in bytes.
        int8_t _err4_ = dinosaurs_bootstrap_updatee_Version_1_0_serialize_(
            &obj->hardware_version, &buffer[offset_bits / 8U], &_size_bytes1_);
        if (_err4_ < 0)
        {
            return _err4_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes1_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad2_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err5_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad2_);  // Optimize?
        if (_err5_ < 0)
        {
            return _err5_;
        }
        offset_bits += _pad2_;
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
static inline int8_t dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_deserialize_(
    dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // saturated uint8[<=50] name
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
    if (out_obj->name.count > 50U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index5_ = 0U; _index5_ < out_obj->name.count; ++_index5_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->name.elements[_index5_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->name.elements[_index5_] = 0U;
        }
        offset_bits += 8U;
    }
    // saturated uint8[<=50] file_name
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->file_name.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->file_name.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->file_name.count > 50U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index6_ = 0U; _index6_ < out_obj->file_name.count; ++_index6_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->file_name.elements[_index6_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->file_name.elements[_index6_] = 0U;
        }
        offset_bits += 8U;
    }
    // saturated uint8[<=150] file_path
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->file_path.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->file_path.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->file_path.count > 150U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index7_ = 0U; _index7_ < out_obj->file_path.count; ++_index7_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->file_path.elements[_index7_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->file_path.elements[_index7_] = 0U;
        }
        offset_bits += 8U;
    }
    // saturated uint64 build_number
    out_obj->build_number = nunavutGetU64(&buffer[0], capacity_bytes, offset_bits, 64);
    offset_bits += 64U;
    // saturated uint8[<=30] build_time
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->build_time.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->build_time.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->build_time.count > 30U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    for (size_t _index8_ = 0U; _index8_ < out_obj->build_time.count; ++_index8_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->build_time.elements[_index8_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->build_time.elements[_index8_] = 0U;
        }
        offset_bits += 8U;
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // dinosaurs.bootstrap.updatee.Version.1.0 software_version
    {
        size_t _size_bytes2_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err6_ = dinosaurs_bootstrap_updatee_Version_1_0_deserialize_(
            &out_obj->software_version, &buffer[offset_bits / 8U], &_size_bytes2_);
        if (_err6_ < 0)
        {
            return _err6_;
        }
        offset_bits += _size_bytes2_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    // saturated uint8[16] unique_id
    for (size_t _index9_ = 0U; _index9_ < 16UL; ++_index9_)
    {
        if ((offset_bits + 8U) <= capacity_bits)
        {
            out_obj->unique_id[_index9_] = buffer[offset_bits / 8U] & 255U;
        }
        else
        {
            out_obj->unique_id[_index9_] = 0U;
        }
        offset_bits += 8U;
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // dinosaurs.bootstrap.updatee.Version.1.0 hardware_version
    {
        size_t _size_bytes3_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err7_ = dinosaurs_bootstrap_updatee_Version_1_0_deserialize_(
            &out_obj->hardware_version, &buffer[offset_bits / 8U], &_size_bytes3_);
        if (_err7_ < 0)
        {
            return _err7_;
        }
        offset_bits += _size_bytes3_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_initialize_(dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = dinosaurs_bootstrap_updatee_UpdateeDescribe_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // DINOSAURS_BOOTSTRAP_UPDATEE_UPDATEE_DESCRIBE_1_0_INCLUDED_

