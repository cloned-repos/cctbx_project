#include <cctbx/boost_python/flex_fwd.h>

#include <boost/python/module.hpp>
#include <boost/python/class.hpp>
#include <boost/python/def.hpp>
#include <boost/python/dict.hpp>
#include <boost/python/list.hpp>
#include <scitbx/array_family/flex_types.h>
#include <scitbx/array_family/shared.h>
#include <scitbx/math/mean_and_variance.h>
#include <scitbx/array_family/boost_python/shared_wrapper.h>
#include <scitbx/examples/bevington/prototype_core.h>
#include <Eigen/Sparse>
#include <boost/python/return_internal_reference.hpp>
#include <boost/math/tools/precision.hpp>

using namespace boost::python;
namespace scitbx{
namespace example{
namespace boost_python { namespace {

  void
  scaling_init_module() {
    using namespace boost::python;

    typedef return_value_policy<return_by_value> rbv;
    typedef default_call_policies dcp;

    class_<linear_ls_eigen_wrapper>("linear_ls_eigen_wrapper", no_init)
      .def(init<int>(arg("n_parameters")))
      .def("n_parameters", &linear_ls_eigen_wrapper::n_parameters)
      .def("reset", &linear_ls_eigen_wrapper::reset)
      .def("right_hand_side", &linear_ls_eigen_wrapper::right_hand_side)
      .def("solve", &linear_ls_eigen_wrapper::solve)
      .def("solved", &linear_ls_eigen_wrapper::solved)
      .def("solution", &linear_ls_eigen_wrapper::solution)
    ;

    typedef non_linear_ls_eigen_wrapper nllsew;
    boost::python::return_internal_reference<> rir;
    class_<nllsew,
           bases<scitbx::lstbx::normal_equations::non_linear_ls<double> > >(
           "non_linear_ls_eigen_wrapper", no_init)
      .def(init<int const&>(arg("n_parameters")))
      .def("reset", &nllsew::reset)
      .def("step_equations",&nllsew::step_equations, rir)
      .def("add_constant_to_diagonal",&nllsew::add_constant_to_diagonal)
      .def("get_normal_matrix_diagonal",&nllsew::get_normal_matrix_diagonal)
      .def("solve_returning_error_mat_diagonal", &nllsew::solve_returning_error_mat_diagonal)
    ;

    typedef bevington_base_class bev;
    class_<bev,bases<nllsew> >( "bevington_base_class", no_init)
      .def(init<int>(arg("n_parameters")))
      .def("set_cpp_data",&bev::set_cpp_data)
      .def("fvec_callable", &bev::fvec_callable)
      .def("access_cpp_build_up_directly_eigen_eqn", &bev::access_cpp_build_up_directly_eigen_eqn,
        (arg("objective_only"),arg("current_values")))
    ;
  }

}
}}} // namespace xfel::boost_python::<anonymous>

BOOST_PYTHON_MODULE(scitbx_examples_bevington_ext)
{
  scitbx::example::boost_python::scaling_init_module();

}
