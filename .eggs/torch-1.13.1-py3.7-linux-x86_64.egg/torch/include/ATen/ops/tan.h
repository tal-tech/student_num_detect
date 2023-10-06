#pragma once

// @generated by torchgen/gen.py from Function.h

#include <ATen/Context.h>
#include <ATen/DeviceGuard.h>
#include <ATen/TensorUtils.h>
#include <ATen/TracerMode.h>
#include <ATen/core/Generator.h>
#include <ATen/core/Reduction.h>
#include <ATen/core/Tensor.h>
#include <c10/core/Scalar.h>
#include <c10/core/Storage.h>
#include <c10/core/TensorOptions.h>
#include <c10/util/Deprecated.h>
#include <c10/util/Optional.h>



#include <ATen/ops/tan_ops.h>

namespace at {


// aten::tan(Tensor self) -> Tensor
inline at::Tensor tan(const at::Tensor & self) {
    return at::_ops::tan::call(self);
}

// aten::tan_(Tensor(a!) self) -> Tensor(a!)
inline at::Tensor & tan_(at::Tensor & self) {
    return at::_ops::tan_::call(self);
}

// aten::tan.out(Tensor self, *, Tensor(a!) out) -> Tensor(a!)
inline at::Tensor & tan_out(at::Tensor & out, const at::Tensor & self) {
    return at::_ops::tan_out::call(self, out);
}

// aten::tan.out(Tensor self, *, Tensor(a!) out) -> Tensor(a!)
inline at::Tensor & tan_outf(const at::Tensor & self, at::Tensor & out) {
    return at::_ops::tan_out::call(self, out);
}

}
