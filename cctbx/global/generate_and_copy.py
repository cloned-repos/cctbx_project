import os, shutil
import generate_carray_bpl
import generate_vector_algebra
import generate_vector_algebra_traits
import generate_vector_algebra_operators
import generate_operator_traits_builtin
import generate_af_algebras
import generate_flagged_value_algebra
generate_carray_bpl.run()
generate_vector_algebra.run()
generate_vector_algebra_traits.run()
generate_vector_algebra_operators.run()
generate_operator_traits_builtin.run()
generate_af_algebras.run()
generate_flagged_value_algebra.run()
for file, dir in (
  ("carray_bpl.h", "../cctbx/"),
  ("algebra.h", "../cctbx/vector/"),
  ("algebra_traits.h", "../cctbx/vector/"),
  ("algebra_operators.h", "../cctbx/vector/"),
  ("operator_traits_builtin.h", "../cctbx/array_family/"),
  ("flagged_value_algebra.h", "../cctbx/array_family/"),
  ("ref_algebra.h", "../cctbx/array_family/"),
  ("tiny_algebra.h", "../cctbx/array_family/"),
  ("small_algebra.h", "../cctbx/array_family/"),
  ("shared_algebra.h", "../cctbx/array_family/"),
  ("versa_algebra.h", "../cctbx/array_family/"),
):
  print "Copying " + dir + file
  shutil.copy(file, dir + file)
  os.unlink(file)
