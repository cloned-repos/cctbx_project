from cctbx import xray
from cctbx import eltbx
from cctbx import miller
from cctbx.array_family import flex
import iotbx.pdb
from scitbx.python_utils import easy_pickle
from scitbx.python_utils.misc import user_plus_sys_time
import sys

def show_scatterer_digest(structure):
  sd = structure.scattering_dict().dict()
  for key,val in sd.items():
    gn = str(val.gaussian.n_ab())
    if (val.gaussian.c() != 0):
      gn += "+c"
    print "%s:%s*%d" % (key, gn, val.member_indices.size()),
  print

def timings(structure, d_min):
  structure_5g = structure.deep_copy_scatterers()
  structure_4g = structure.deep_copy_scatterers()
  structure_2g = structure.deep_copy_scatterers()
  structure_5g.scattering_dict()
  structure_4g.scattering_dict(d_min=1, d_min_it1992=1)
  structure_2g.scattering_dict(
    custom_dict=eltbx.xray_scattering.two_gaussian_agarwal_isaacs)
  miller_set = miller.build_set(
    crystal_symmetry=structure,
    d_min=d_min,
    anomalous_flag=00000)
  miller_set.show_summary()
  print "d_min:", d_min
  timer = user_plus_sys_time()
  f_calc_simple = xray.structure_factors_simple(
    structure_5g.unit_cell(),
    structure_5g.space_group(),
    miller_set.indices(),
    structure_5g.scatterers(),
    structure_5g.scattering_dict()).f_calc()
  print "direct simple: %.2f seconds" % timer.elapsed()
  f_calc_simple = flex.abs(f_calc_simple)
  for structure in (structure_5g, structure_4g, structure_2g):
    show_scatterer_digest(structure)
    for calc_type,cos_sin_flag in (("direct cos+sin function:",00000),
                                   ("direct cos+sin table:",0001)):
      timer = user_plus_sys_time()
      f_calc = miller_set.structure_factors_from_scatterers(
        xray_structure=structure,
        algorithm="direct",
        cos_sin_table=cos_sin_flag).f_calc()
      print "  %-24s %.2f seconds," % (calc_type, timer.elapsed()),
      ls = xray.targets_least_squares_residual(
        f_calc_simple, f_calc.data(), 00000, 1)
      print "r-factor: %.6f" % ls.target()
    for calc_type,exp_table_one_over_step_size in (("fft exp function:",0),
                                                   ("fft exp table:",-100)):
      timer = user_plus_sys_time()
      f_calc = xray.structure_factors.from_scatterers(
        miller_set=miller_set,
        wing_cutoff=1.e-4,
        exp_table_one_over_step_size=exp_table_one_over_step_size)(
          xray_structure=structure,
          miller_set=miller_set,
          algorithm="fft").f_calc()
      print "  %-24s %.2f seconds," % (calc_type, timer.elapsed()),
      ls = xray.targets_least_squares_residual(
        f_calc_simple, f_calc.data(), 00000, 1)
      print "r-factor: %.6f" % ls.target()
  print

def read_structure(file_name):
  try: return easy_pickle.load(file_name)
  except: pass
  try: return iotbx.pdb.as_xray_structure(file_name)
  except: pass
  raise RuntimeError("Unknown file format: %s" % file_name)

def run(args):
  "usage: cctbx.structure_factor_timings coordinate_file [d-spacing ...]"
  if (len(args) == 0):
    print >> sys.stderr, run.__doc__
    return
  file_name = args[0]
  try:
    d_spacings = [float(arg) for arg in args[1:]]
  except:
    print >> sys.stderr, run.__doc__
    return
  if (d_spacings == []):
    d_spacings = [4,3,2,1]
  structure = read_structure(file_name)
  structure.show_summary()
  print
  for d_min in d_spacings:
    timings(structure, d_min)

if (__name__ == "__main__"):
  run(sys.argv[1:])
