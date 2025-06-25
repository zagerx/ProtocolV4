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
// Source file:   /home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/motion_controller/ControllerParameter.1.0.uavcan
// Generated at:  2025-06-26 11:12:32.341448 UTC
// Is deprecated: no
// Fixed port-ID: None
// Full name:     dinosaurs.actuator.motion_controller.ControllerParameter
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

#ifndef DINOSAURS_ACTUATOR_MOTION_CONTROLLER_CONTROLLER_PARAMETER_1_0_INCLUDED_
#define DINOSAURS_ACTUATOR_MOTION_CONTROLLER_CONTROLLER_PARAMETER_1_0_INCLUDED_

#include <dinosaurs/actuator/motion_controller/Result_1_0.h>
#include <nunavut/support/serialization.h>
#include <stdint.h>
#include <stdlib.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 1693710260,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/motion_controller/ControllerParameter.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/motion_controller/ControllerParameter.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/motion_controller/ControllerParameter.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/motion_controller/ControllerParameter.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/zhangge/worknote/ProtocolV4/uavcan/custom_data_types/dinosaurs/actuator/motion_controller/ControllerParameter.1.0.uavcan is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

/// This type does not have a fixed port-ID. See https://forum.opencyphal.org/t/choosing-message-and-service-ids/889
#define dinosaurs_actuator_motion_controller_ControllerParameter_1_0_HAS_FIXED_PORT_ID_ false

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.actuator.motion_controller.ControllerParameter.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_actuator_motion_controller_ControllerParameter_1_0_FULL_NAME_             "dinosaurs.actuator.motion_controller.ControllerParameter"
#define dinosaurs_actuator_motion_controller_ControllerParameter_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.actuator.motion_controller.ControllerParameter.1.0"

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.actuator.motion_controller.ControllerParameter.Request.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_FULL_NAME_             "dinosaurs.actuator.motion_controller.ControllerParameter.Request"
#define dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.actuator.motion_controller.ControllerParameter.Request.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_EXTENT_BYTES_                    107UL
#define dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 107UL
static_assert(dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_EXTENT_BYTES_ >= dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// saturated uint8 TWO_WHEEL_DIFFERENTIAL = 0
#define dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_TWO_WHEEL_DIFFERENTIAL (0U)

/// saturated uint8 WHEEL_LINE_SPEED = 0
#define dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_WHEEL_LINE_SPEED (0U)

/// saturated uint8 WHEEL_RPM = 1
#define dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_WHEEL_RPM (1U)

/// saturated uint8 IMU_AND_ODOMETRY = 0
#define dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_IMU_AND_ODOMETRY (0U)

typedef struct
{
    /// saturated uint8 robot_chassis_type
    uint8_t robot_chassis_type;

    /// saturated uint8 robot_motion_actuator_command_type
    uint8_t robot_motion_actuator_command_type;

    /// saturated uint8 robot_motion_sensor_data_type
    uint8_t robot_motion_sensor_data_type;

    /// saturated float32 velocity_p
    float velocity_p;

    /// saturated float32 velocity_i
    float velocity_i;

    /// saturated float32 velocity_d
    float velocity_d;

    /// saturated float32 velocity_integral_max
    float velocity_integral_max;

    /// saturated float32 velocity_integral_min
    float velocity_integral_min;

    /// saturated float32 velocity_output_max
    float velocity_output_max;

    /// saturated float32 velocity_output_min
    float velocity_output_min;

    /// saturated float32 angular_velocity_p
    float angular_velocity_p;

    /// saturated float32 angular_velocity_i
    float angular_velocity_i;

    /// saturated float32 angular_velocity_d
    float angular_velocity_d;

    /// saturated float32 angular_velocity_integral_max
    float angular_velocity_integral_max;

    /// saturated float32 angular_velocity_integral_min
    float angular_velocity_integral_min;

    /// saturated float32 angular_velocity_output_max
    float angular_velocity_output_max;

    /// saturated float32 angular_velocity_output_min
    float angular_velocity_output_min;

    /// saturated float32 abs_p
    float abs_p;

    /// saturated float32 abs_i
    float abs_i;

    /// saturated float32 abs_d
    float abs_d;

    /// saturated float32 abs_integral_max
    float abs_integral_max;

    /// saturated float32 abs_integral_min
    float abs_integral_min;

    /// saturated float32 abs_output_max
    float abs_output_max;

    /// saturated float32 abs_output_min
    float abs_output_min;

    /// saturated float32 abs_enter_threshold
    float abs_enter_threshold;

    /// saturated float32 abs_v_coefficient
    float abs_v_coefficient;

    /// saturated float32 abs_tilt_coefficient
    float abs_tilt_coefficient;

    /// saturated float32 abs_slide_coefficient
    float abs_slide_coefficient;

    /// saturated uint16 disconnect_protect_time
    uint16_t disconnect_protect_time;

    /// saturated uint16 command_interval
    uint16_t command_interval;
} dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_serialize_(
    const dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 856UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // saturated uint8 robot_chassis_type
        // Saturation code not emitted -- native representation matches the serialized representation.
        buffer[offset_bits / 8U] = (uint8_t)(obj->robot_chassis_type);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
    }
    {   // saturated uint8 robot_motion_actuator_command_type
        // Saturation code not emitted -- native representation matches the serialized representation.
        buffer[offset_bits / 8U] = (uint8_t)(obj->robot_motion_actuator_command_type);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
    }
    {   // saturated uint8 robot_motion_sensor_data_type
        // Saturation code not emitted -- native representation matches the serialized representation.
        buffer[offset_bits / 8U] = (uint8_t)(obj->robot_motion_sensor_data_type);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
    }
    {   // saturated float32 velocity_p
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err0_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->velocity_p);
        if (_err0_ < 0)
        {
            return _err0_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 velocity_i
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err1_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->velocity_i);
        if (_err1_ < 0)
        {
            return _err1_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 velocity_d
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err2_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->velocity_d);
        if (_err2_ < 0)
        {
            return _err2_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 velocity_integral_max
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err3_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->velocity_integral_max);
        if (_err3_ < 0)
        {
            return _err3_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 velocity_integral_min
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err4_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->velocity_integral_min);
        if (_err4_ < 0)
        {
            return _err4_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 velocity_output_max
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err5_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->velocity_output_max);
        if (_err5_ < 0)
        {
            return _err5_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 velocity_output_min
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err6_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->velocity_output_min);
        if (_err6_ < 0)
        {
            return _err6_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 angular_velocity_p
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err7_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->angular_velocity_p);
        if (_err7_ < 0)
        {
            return _err7_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 angular_velocity_i
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err8_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->angular_velocity_i);
        if (_err8_ < 0)
        {
            return _err8_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 angular_velocity_d
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err9_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->angular_velocity_d);
        if (_err9_ < 0)
        {
            return _err9_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 angular_velocity_integral_max
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err10_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->angular_velocity_integral_max);
        if (_err10_ < 0)
        {
            return _err10_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 angular_velocity_integral_min
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err11_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->angular_velocity_integral_min);
        if (_err11_ < 0)
        {
            return _err11_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 angular_velocity_output_max
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err12_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->angular_velocity_output_max);
        if (_err12_ < 0)
        {
            return _err12_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 angular_velocity_output_min
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err13_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->angular_velocity_output_min);
        if (_err13_ < 0)
        {
            return _err13_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_p
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err14_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_p);
        if (_err14_ < 0)
        {
            return _err14_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_i
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err15_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_i);
        if (_err15_ < 0)
        {
            return _err15_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_d
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err16_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_d);
        if (_err16_ < 0)
        {
            return _err16_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_integral_max
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err17_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_integral_max);
        if (_err17_ < 0)
        {
            return _err17_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_integral_min
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err18_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_integral_min);
        if (_err18_ < 0)
        {
            return _err18_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_output_max
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err19_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_output_max);
        if (_err19_ < 0)
        {
            return _err19_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_output_min
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err20_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_output_min);
        if (_err20_ < 0)
        {
            return _err20_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_enter_threshold
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err21_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_enter_threshold);
        if (_err21_ < 0)
        {
            return _err21_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_v_coefficient
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err22_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_v_coefficient);
        if (_err22_ < 0)
        {
            return _err22_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_tilt_coefficient
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err23_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_tilt_coefficient);
        if (_err23_ < 0)
        {
            return _err23_;
        }
        offset_bits += 32U;
    }
    {   // saturated float32 abs_slide_coefficient
        // Saturation code not emitted -- assume the native representation of float32 is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        const int8_t _err24_ = nunavutSetF32(&buffer[0], capacity_bytes, offset_bits, obj->abs_slide_coefficient);
        if (_err24_ < 0)
        {
            return _err24_;
        }
        offset_bits += 32U;
    }
    {   // saturated uint16 disconnect_protect_time
        // Saturation code not emitted -- native representation matches the serialized representation.
        const int8_t _err25_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, obj->disconnect_protect_time, 16U);
        if (_err25_ < 0)
        {
            return _err25_;
        }
        offset_bits += 16U;
    }
    {   // saturated uint16 command_interval
        // Saturation code not emitted -- native representation matches the serialized representation.
        const int8_t _err26_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, obj->command_interval, 16U);
        if (_err26_ < 0)
        {
            return _err26_;
        }
        offset_bits += 16U;
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad0_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err27_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad0_);  // Optimize?
        if (_err27_ < 0)
        {
            return _err27_;
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
static inline int8_t dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_deserialize_(
    dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // saturated uint8 robot_chassis_type
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->robot_chassis_type = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->robot_chassis_type = 0U;
    }
    offset_bits += 8U;
    // saturated uint8 robot_motion_actuator_command_type
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->robot_motion_actuator_command_type = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->robot_motion_actuator_command_type = 0U;
    }
    offset_bits += 8U;
    // saturated uint8 robot_motion_sensor_data_type
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->robot_motion_sensor_data_type = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->robot_motion_sensor_data_type = 0U;
    }
    offset_bits += 8U;
    // saturated float32 velocity_p
    out_obj->velocity_p = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 velocity_i
    out_obj->velocity_i = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 velocity_d
    out_obj->velocity_d = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 velocity_integral_max
    out_obj->velocity_integral_max = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 velocity_integral_min
    out_obj->velocity_integral_min = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 velocity_output_max
    out_obj->velocity_output_max = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 velocity_output_min
    out_obj->velocity_output_min = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 angular_velocity_p
    out_obj->angular_velocity_p = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 angular_velocity_i
    out_obj->angular_velocity_i = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 angular_velocity_d
    out_obj->angular_velocity_d = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 angular_velocity_integral_max
    out_obj->angular_velocity_integral_max = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 angular_velocity_integral_min
    out_obj->angular_velocity_integral_min = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 angular_velocity_output_max
    out_obj->angular_velocity_output_max = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 angular_velocity_output_min
    out_obj->angular_velocity_output_min = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_p
    out_obj->abs_p = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_i
    out_obj->abs_i = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_d
    out_obj->abs_d = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_integral_max
    out_obj->abs_integral_max = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_integral_min
    out_obj->abs_integral_min = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_output_max
    out_obj->abs_output_max = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_output_min
    out_obj->abs_output_min = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_enter_threshold
    out_obj->abs_enter_threshold = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_v_coefficient
    out_obj->abs_v_coefficient = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_tilt_coefficient
    out_obj->abs_tilt_coefficient = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated float32 abs_slide_coefficient
    out_obj->abs_slide_coefficient = nunavutGetF32(&buffer[0], capacity_bytes, offset_bits);
    offset_bits += 32U;
    // saturated uint16 disconnect_protect_time
    out_obj->disconnect_protect_time = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;
    // saturated uint16 command_interval
    out_obj->command_interval = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_initialize_(dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = dinosaurs_actuator_motion_controller_ControllerParameter_Request_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

// +-------------------------------------------------------------------------------------------------------------------+
// | dinosaurs.actuator.motion_controller.ControllerParameter.Response.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_FULL_NAME_             "dinosaurs.actuator.motion_controller.ControllerParameter.Response"
#define dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_FULL_NAME_AND_VERSION_ "dinosaurs.actuator.motion_controller.ControllerParameter.Response.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_EXTENT_BYTES_                    1UL
#define dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 1UL
static_assert(dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_EXTENT_BYTES_ >= dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

typedef struct
{
    /// dinosaurs.actuator.motion_controller.Result.1.0 result
    dinosaurs_actuator_motion_controller_Result_1_0 result;
} dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_serialize_(
    const dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
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
    {   // dinosaurs.actuator.motion_controller.Result.1.0 result
        size_t _size_bytes0_ = 1UL;  // Nested object (max) size, in bytes.
        int8_t _err28_ = dinosaurs_actuator_motion_controller_Result_1_0_serialize_(
            &obj->result, &buffer[offset_bits / 8U], &_size_bytes0_);
        if (_err28_ < 0)
        {
            return _err28_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes0_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad1_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err29_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad1_);  // Optimize?
        if (_err29_ < 0)
        {
            return _err29_;
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
static inline int8_t dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_deserialize_(
    dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // dinosaurs.actuator.motion_controller.Result.1.0 result
    {
        size_t _size_bytes1_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err30_ = dinosaurs_actuator_motion_controller_Result_1_0_deserialize_(
            &out_obj->result, &buffer[offset_bits / 8U], &_size_bytes1_);
        if (_err30_ < 0)
        {
            return _err30_;
        }
        offset_bits += _size_bytes1_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_initialize_(dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = dinosaurs_actuator_motion_controller_ControllerParameter_Response_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // DINOSAURS_ACTUATOR_MOTION_CONTROLLER_CONTROLLER_PARAMETER_1_0_INCLUDED_
