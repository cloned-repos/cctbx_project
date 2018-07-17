from __future__ import division, print_function
import time
import mmtbx.model
import iotbx.pdb
from libtbx.utils import null_out

neutral_atoms_list = ['Ru', 'Re', 'Ra', 'Rb', 'Rn', 'Rh', 'Be', 'Ba', 'Bi',
  'Bk', 'Br', 'H', 'P', 'Os', 'Ge', 'Gd', 'Ga', 'Pr', 'Pt', 'Pu', 'C', 'Pb',
  'Pa', 'Pd', 'Xe', 'Po', 'Pm', 'Ho', 'Hf', 'Hg', 'He', 'Mg', 'K', 'Mn', 'O',
  'S', 'W', 'Zn', 'Eu', 'Zr', 'Er', 'Ni', 'Na', 'Nb', 'Nd', 'Ne', 'Np', 'Fr',
  'Fe', 'B', 'F', 'Sr', 'N', 'Kr', 'Si', 'Sn', 'Sm', 'V', 'Sc', 'Sb', 'Se',
  'Co', 'Cm', 'Cl', 'Ca', 'Cf', 'Ce', 'Cd', 'Tm', 'Cs', 'Cr', 'Cu', 'La',
  'Li', 'Tl', 'Lu', 'Th', 'Ti', 'Te', 'Tb', 'Tc', 'Ta', 'Yb', 'Dy', 'I', 'U',
  'Y', 'Ac', 'Ag', 'Ir', 'Am', 'Al', 'As', 'Ar', 'Au', 'At', 'In', 'Mo']

def run():
  # Check if scatterers in xrs are neutral after calling function
  pdb_inp = iotbx.pdb.input(source_info=None, lines=pdb_str)
  model = mmtbx.model.manager(
      model_input       = pdb_inp,
      log = null_out())
  model.neutralize_scatterers()
  xrs = model.get_xray_structure()
  for scatterer in xrs.scatterers():
    assert (scatterer.scattering_type  in neutral_atoms_list)

  # Check if pdb_hierarchy has neutral atoms as well
  pdb_str_neutralized = model.model_as_pdb()
  pdb_inp_neutralized = iotbx.pdb.input(
    source_info=None,
    lines=pdb_str_neutralized)
  model_neutralized = mmtbx.model.manager(
      model_input       = pdb_inp_neutralized,
      log = null_out())
  xrs_neutralized = model_neutralized.get_xray_structure()
  for scatterer in xrs_neutralized.scatterers():
    assert (scatterer.scattering_type  in neutral_atoms_list)

pdb_str = """
CRYST1   36.960  124.370   41.010  90.00 116.55  90.00 P 1 21 1
SCALE1      0.027056  0.000000  0.013519        0.00000
SCALE2      0.000000  0.008041  0.000000        0.00000
SCALE3      0.000000  0.000000  0.027259        0.00000
HETATM 6628  O   HOH A5000       6.345   4.777  15.778  1.00  7.19           H1-
HETATM 6629  O   HOH A5001       0.898 -11.608   9.059  1.00  4.52          He
HETATM 6630  O   HOH A5002      -9.341  15.181  18.207  1.00  4.40          Li
HETATM 6631  O   HOH A5003      -8.813  -4.503  15.152  1.00  4.49          Li1+
HETATM 6632  O   HOH A5004      -9.819   4.216  22.563  1.00  3.89          Be
HETATM 6633  O   HOH A5005       7.293  18.903  22.780  1.00  6.69          Be2+
HETATM 6634  O   HOH A5006       0.173   6.286  15.367  1.00  4.17           B
HETATM 6635  O   HOH A5007      -0.383   1.594  13.039  1.00  4.58           C
HETATM 6636  O   HOH A5008      -2.356   2.761  28.626  1.00  4.48           N
HETATM 6637  O   HOH A5009      -1.579  -5.998  16.103  1.00  4.95           O
HETATM 6638  O   HOH A5010     -13.313  18.722  16.219  1.00  7.64           O1-
HETATM 6639  O   HOH A5011       4.042 -17.542  13.901  1.00  5.04           O2-
HETATM 6640  O   HOH A5012       1.813 -15.513   8.453  1.00  4.89           F
HETATM 6641  O   HOH A5013      -3.818  15.582  34.975  1.00  6.70           F1-
HETATM 6642  O   HOH A5014       0.310 -17.405   7.121  1.00  5.09          Ne
HETATM 6643  O   HOH A5015     -15.880 -13.960  21.123  1.00  5.49          Na
HETATM 6644  O   HOH A5016       3.948 -16.112  11.472  1.00  5.30          Na1+
HETATM 6645  O   HOH A5017      -5.457  -5.035  27.632  1.00  5.33          Mg
HETATM 6646  O   HOH A5018      -1.033 -20.162  14.712  1.00  5.86          Mg2+
HETATM 6647  O   HOH A5019      -4.100  13.292   7.498  1.00  5.86          Al
HETATM 6648  O   HOH A5020      -9.492 -26.443  15.424  1.00  6.73          Al3+
HETATM 6649  O   HOH A5021     -17.549 -17.302   8.636  1.00  6.46          Si
HETATM 6650  O   HOH A5022       4.404  -7.020  14.825  1.00  6.87          Si4+
HETATM 6651  O   HOH A5023     -10.836   7.859  11.832  1.00  5.89           P
HETATM 6652  O   HOH A5024       0.998   3.980  13.754  1.00  5.70           S
HETATM 6653  O   HOH A5025      -5.365  12.486   5.272  1.00  6.33          Cl
HETATM 6654  O   HOH A5026     -15.556 -14.292  17.362  1.00  5.92          Cl1-
HETATM 6655  O   HOH A5027       3.867 -15.378  22.380  1.00  7.31          Ar
HETATM 6656  O   HOH A5028      -7.693   6.919  26.782  1.00  5.96           K
HETATM 6657  O   HOH A5029      -6.978  30.897  25.968  0.80  5.32           K1+
HETATM 6658  O   HOH A5030      -6.322 -25.130   8.738  1.00  5.59          Ca
HETATM 6659  O   HOH A5031       6.962   7.229  16.925  1.00  6.08          Ca2+
HETATM 6660  O   HOH A5032     -16.532  19.553  26.386  1.00  5.96          Sc
HETATM 6661  O   HOH A5033       2.846 -13.052   7.763  1.00  5.81          Sc3+
HETATM 6662  O   HOH A5034       1.784   0.090  -2.170  1.00  7.02          Ti
HETATM 6663  O   HOH A5035       2.605 -14.287   0.491  1.00  6.70          Ti2+
HETATM 6664  O   HOH A5036     -20.529  -8.793  13.734  1.00  6.46          Ti3+
HETATM 6665  O   HOH A5037      -1.062  -0.582  14.744  1.00  6.45          Ti4+
HETATM 6666  O   HOH A5038     -14.665   0.020  25.868  0.80  5.37           V
HETATM 6667  O   HOH A5039      -1.000   3.064  31.898  1.00  6.58           V2+
HETATM 6668  O   HOH A5040      -3.011  18.109  34.071  1.00  6.71           V3+
HETATM 6669  O   HOH A5041      -8.717  31.117  28.097  1.00  8.45           V5+
HETATM 6670  O   HOH A5042     -19.474  -9.238  17.375  1.00  7.04          Cr
HETATM 6671  O   HOH A5043       2.577  12.013  31.099  1.00  7.46          Cr2+
HETATM 6672  O   HOH A5044      -1.803  18.594  31.768  1.00  9.12          Cr3+
HETATM 6673  O   HOH A5045      -5.340 -10.857  -4.897  1.00  9.22          Mn
HETATM 6674  O   HOH A5046      -8.923   4.751  25.261  1.00  6.53          Mn2+
HETATM 6675  O   HOH A5047     -14.493  -4.667   4.322  1.00  5.71          Mn3+
HETATM 6676  O   HOH A5048      -7.935  12.827   4.276  1.00  7.36          Mn4+
HETATM 6677  O   HOH A5049     -16.603 -15.963  22.859  1.00  6.52          Fe
HETATM 6678  O   HOH A5050       5.273 -15.598  15.395  1.00  6.29          Fe2+
HETATM 6679  O   HOH A5051       3.235   9.285  30.877  1.00  6.67          Fe3+
HETATM 6680  O   HOH A5052       3.025 -18.039  22.544  1.00  6.99          Co
HETATM 6681  O   HOH A5053      -0.542 -15.322  -4.060  1.00  7.59          Co2+
HETATM 6682  O   HOH A5054     -15.891  10.115  10.580  1.00  8.16          Co3+
HETATM 6683  O   HOH A5055     -18.117   2.800  31.652  1.00  8.25          Ni
HETATM 6684  O   HOH A5056       4.325  -0.300  22.401  1.00  8.80          Ni2+
HETATM 6685  O   HOH A5057     -10.666  -4.255   5.624  1.00  7.56          Ni3+
HETATM 6686  O   HOH A5058       7.586  19.226  29.730  1.00  9.19          Cu
HETATM 6687  O   HOH A5059      -8.448  26.719  21.195  1.00  8.94          Cu1+
HETATM 6688  O   HOH A5060       1.615 -22.177   9.005  0.70  6.61          Cu2+
HETATM 6689  O   HOH A5061     -17.611  31.917  21.108  1.00  7.51          Zn
HETATM 6690  O   HOH A5062      -9.590  -3.484  29.577  1.00  6.73          Zn2+
HETATM 6691  O   HOH A5063      -9.010 -23.725  17.437  1.00  6.62          Ga
HETATM 6692  O   HOH A5064     -11.495  -2.227   4.073  0.79  5.34          Ga3+
HETATM 6693  O   HOH A5065      -5.323 -27.884   9.135  1.00  7.29          Ge
HETATM 6694  O   HOH A5066     -11.995 -24.557  19.436  1.00  7.76          Ge4+
HETATM 6695  O   HOH A5067       8.866  12.749  23.235  1.00  9.38          As
HETATM 6696  O   HOH A5068     -20.992  -5.261   6.751  1.00 10.30          Se
HETATM 6697  O   HOH A5069     -11.955  16.592  37.039  1.00 10.09          Br
HETATM 6698  O   HOH A5070      -4.929 -13.595  -5.436  1.00  9.30          Br1-
HETATM 6699  O   HOH A5071      -5.562 -22.177   1.544  1.00  7.55          Kr
HETATM 6700  O   HOH A5072      -1.071   2.859  -0.759  0.80  6.86          Rb
HETATM 6701  O   HOH A5073     -16.938 -10.770  -0.110  1.00  9.09          Rb1+
HETATM 6702  O   HOH A5074      -7.582 -21.920  19.111  0.70  5.55          Sr
HETATM 6703  O   HOH A5075       6.197  12.147  11.582  1.00  7.42          Sr2+
HETATM 6704  O   HOH A5076     -23.796  -1.956   8.962  0.70 19.49           Y
HETATM 6705  O   HOH A5077       9.894   4.496  22.239  1.00  9.32           Y3+
HETATM 6706  O   HOH A5078     -21.108 -13.726  13.696  1.00  8.40          Zr
HETATM 6707  O   HOH A5079       5.444  -2.244  -0.988  1.00 10.26          Zr4+
HETATM 6708  O   HOH A5080       1.428 -32.632  10.473  1.00  7.70          Nb
HETATM 6709  O   HOH A5081     -11.489  22.783  34.873  1.00  9.91          Nb3+
HETATM 6710  O   HOH A5082      -5.022   8.426  -0.521  1.00  9.46          Nb5+
HETATM 6711  O   HOH A5083       4.245 -26.322  18.944  1.00  9.17          Mo
HETATM 6712  O   HOH A5084     -21.686  31.635  22.531  1.00  8.64          Mo3+
HETATM 6713  O   HOH A5085       5.619   0.799   8.811  1.00  9.02          Mo5+
HETATM 6714  O   HOH A5086     -20.860  -2.905   5.430  1.00 10.43          Mo6+
HETATM 6715  O   HOH A5087      10.698  16.257  24.585  1.00  8.87          Tc
HETATM 6716  O   HOH A5088     -13.683 -23.315  21.718  0.80  8.64          Ru
HETATM 6717  O   HOH A5089     -15.661  11.589   8.016  1.00  8.65          Ru3+
HETATM 6718  O   HOH A5090     -12.698   2.182  34.354  1.00  8.53          Ru4+
HETATM 6719  O   HOH A5091     -17.937 -14.404   3.222  1.00 11.95          Rh
HETATM 6720  O   HOH A5092       9.630   8.424   8.317  1.00  9.93          Rh3+
HETATM 6721  O   HOH A5093       4.321 -24.967  11.322  1.00 10.50          Rh4+
HETATM 6722  O   HOH A5094       2.854  22.947  17.184  1.00  9.90          Pd
HETATM 6723  O   HOH A5095     -18.873  15.498  20.461  1.00  9.71          Pd2+
HETATM 6724  O   HOH A5096       5.173 -14.697   1.413  1.00  8.92          Pd4+
HETATM 6725  O   HOH A5097      13.750   8.522  14.089  0.90  8.83          Ag
HETATM 6726  O   HOH A5098       3.960 -14.391  24.920  1.00 10.92          Ag1+
HETATM 6727  O   HOH A5099     -17.719  14.157  22.605  1.00  8.67          Ag2+
HETATM 6728  O   HOH A5100     -13.886  -0.324  33.947  1.00  8.25          Cd
HETATM 6729  O   HOH A5101      -0.211  -8.780  26.524  1.00  7.97          Cd2+
HETATM 6730  O   HOH A5102       7.556 -13.249   0.737  0.70  6.51          In
HETATM 6731  O   HOH A5103     -21.951 -11.151  14.274  1.00  8.87          In3+
HETATM 6732  O   HOH A5104     -14.061  -1.934  27.862  0.80  5.90          Sn
HETATM 6733  O   HOH A5105     -14.045  20.753  14.529  1.00 10.10          Sn2+
HETATM 6734  O   HOH A5106      -8.571 -21.026  26.684  1.00  8.59          Sn4+
HETATM 6735  O   HOH A5107      -3.422 -29.610  15.693  1.00  8.74          Sb
HETATM 6736  O   HOH A5108     -17.171   8.243   8.941  0.80  8.41          Sb3+
HETATM 6737  O   HOH A5109      -1.387  18.424  36.218  1.00 10.11          Sb5+
HETATM 6738  O   HOH A5110     -18.238   8.843  16.853  1.00  8.90          Te
HETATM 6739  O   HOH A5111     -12.911 -10.114  -3.539  1.00 10.15           I
HETATM 6740  O   HOH A5112     -14.718   0.056  29.622  0.80  6.93           I1-
HETATM 6741  O   HOH A5113       3.198  24.539  23.772  1.00 10.25          Xe
HETATM 6742  O   HOH A5114      -9.544  -5.654  -3.780  1.00 12.88          Cs
HETATM 6743  O   HOH A5115     -14.304  29.432  17.958  1.00 10.60          Cs1+
HETATM 6744  O   HOH A5116       0.027 -31.416  18.068  1.00 11.49          Ba
HETATM 6745  O   HOH A5117       2.957 -22.353  -4.387  0.70  8.04          Ba2+
HETATM 6746  O   HOH A5118       5.044   8.538  33.082  1.00 12.08          La
HETATM 6747  O   HOH A5119     -18.925 -19.092   7.000  1.00 14.18          La3+
HETATM 6748  O   HOH A5120       3.686 -31.641  11.616  1.00 12.00          Ce
HETATM 6749  O   HOH A5121       4.314 -21.047   4.935  1.00 13.08          Ce3+
HETATM 6750  O   HOH A5122     -12.952 -11.779  -1.393  1.00 10.99          Ce4+
HETATM 6751  O   HOH A5123     -22.006  -1.983  17.485  1.00 10.26          Pr
HETATM 6752  O   HOH A5124      -3.968  -5.120  30.009  1.00  8.71          Pr3+
HETATM 6753  O   HOH A5125     -16.808 -13.442  32.754  1.00 10.21          Pr4+
HETATM 6754  O   HOH A5126     -18.522 -19.217  21.909  1.00 11.45          Nd
HETATM 6755  O   HOH A5127       7.389 -14.736  13.689  0.79  9.38          Nd3+
HETATM 6756  O   HOH A5128      -6.170   0.637  -4.572  1.00 11.33          Pm
HETATM 6757  O   HOH A5129     -14.747   4.266  34.323  0.70  7.31          Pm3+
HETATM 6758  O   HOH A5130      10.579  11.382  21.519  1.00  8.24          Sm
HETATM 6759  O   HOH A5131     -19.700 -16.238  30.105  1.00  9.42          Sm3+
HETATM 6760  O   HOH A5132     -22.579 -14.695  17.219  1.00  9.41          Eu
HETATM 6761  O   HOH A5133       0.431  22.503  15.354  1.00 10.83          Eu2+
HETATM 6762  O   HOH A5134       3.775  -0.454   4.787  1.00 10.46          Eu3+
HETATM 6763  O   HOH A5135       8.736 -13.435   3.171  0.70  7.33          Gd
HETATM 6764  O   HOH A5136       0.738  -6.147  26.648  0.60  5.75          Gd3+
HETATM 6765  O   HOH A5137       1.394 -23.570  -0.951  0.70  9.59          Tb
HETATM 6766  O   HOH A5138     -19.678   6.552  16.380  1.00  9.94          Tb3+
HETATM 6767  O   HOH A5139      -2.871 -28.584  20.001  1.00  9.75          Dy
HETATM 6768  O   HOH A5140     -13.866  27.937  31.785  1.00 11.94          Dy3+
HETATM 6769  O   HOH A5141       3.567  -2.449   6.680  1.00 10.18          Ho
HETATM 6770  O   HOH A5142      -9.008 -27.341   6.794  1.00 12.93          Ho3+
HETATM 6771  O   HOH A5143     -23.728  12.240  13.099  0.60  8.45          Er
HETATM 6772  O   HOH A5144     -11.400 -26.489   5.781  1.00 10.82          Er3+
HETATM 6773  O   HOH A5145       0.539   8.340   4.707  1.00 11.51          Tm
HETATM 6774  O   HOH A5146      -4.464 -31.333   4.295  1.00 14.23          Tm3+
HETATM 6775  O   HOH A5147       1.679 -13.251  26.060  1.00 10.97          Yb
HETATM 6776  O   HOH A5148      16.068   6.165   7.249  1.00  9.59          Yb2+
HETATM 6777  O   HOH A5149     -12.354  -3.161  29.667  1.00 10.37          Yb3+
HETATM 6778  O   HOH A5150      -3.325  -9.756  -6.517  1.00 13.33          Lu
HETATM 6779  O   HOH A5151      -0.150  -0.784  -3.769  1.00 11.21          Lu3+
HETATM 6780  O   HOH A5152       0.864 -27.670  20.944  1.00 13.15          Hf
HETATM 6781  O   HOH A5153       5.277  14.822   9.726  0.80  8.80          Hf4+
HETATM 6782  O   HOH A5154      -0.920  25.709  32.136  1.00 12.95          Ta
HETATM 6783  O   HOH A5155      -7.440  14.897  39.637  1.00 13.70          Ta5+
HETATM 6784  O   HOH A5156      -1.897  16.311   9.508  0.30  8.01           W
HETATM 6785  O   HOH A5157       9.876  -7.712  22.676  0.70 12.19           W6+
HETATM 6786  O   HOH A5158       7.075  23.333  22.508  1.00 10.79          Re
HETATM 6787  O   HOH A5159      -3.347  13.709   3.688  0.80 12.93          Os
HETATM 6788  O   HOH A5160       4.584  25.908  28.447  0.70 11.73          Os4+
HETATM 6789  O   HOH A5161     -10.135  14.821  39.519  1.00 12.17          Ir
HETATM 6790  O   HOH A5162       7.822  15.920  12.630  0.80 11.10          Ir3+
HETATM 6791  O   HOH A5163     -15.533  -9.718  -4.075  1.00 13.25          Ir4+
HETATM 6792  O   HOH A5164     -21.586  15.788  20.362  1.00 12.26          Pt
HETATM 6793  O   HOH A5165       1.617 -10.551  25.406  0.60  6.76          Pt2+
HETATM 6794  O   HOH A5166       2.331  15.845  10.907  1.00 12.82          Pt4+
HETATM 6795  O   HOH A5167     -20.388  24.283  25.576  0.80 10.02          Au
HETATM 6796  O   HOH A5168     -16.045 -22.074  21.225  0.80  9.72          Au1+
HETATM 6797  O   HOH A5169       0.061  -9.313  -3.705  1.00 11.60          Au3+
HETATM 6798  O   HOH A5170       7.492 -17.244  12.425  1.00 13.30          Hg
HETATM 6799  O   HOH A5171     -19.752   9.771  34.130  0.60  7.87          Hg1+
HETATM 6800  O   HOH A5172       8.647 -12.463  12.618  0.76  9.72          Hg2+
HETATM 6801  O   HOH A5173       3.978   9.179  37.165  1.00 13.43          Tl
HETATM 6802  O   HOH A5174     -17.402  22.538  31.902  1.00 14.63          Tl1+
HETATM 6803  O   HOH A5175       6.354  18.018  31.924  1.00 10.88          Tl3+
HETATM 6804  O   HOH A5176       1.089  19.502  35.743  0.80  9.96          Pb
HETATM 6805  O   HOH A5177      -0.157  11.746  38.584  1.00 11.69          Pb2+
HETATM 6806  O   HOH A5178      -2.909   7.593  -2.014  1.00 11.66          Pb4+
HETATM 6807  O   HOH A5179       8.977  13.583  13.488  0.86  7.85          Bi
HETATM 6808  O   HOH A5180       6.665 -23.693  10.766  1.00 12.76          Bi3+
HETATM 6809  O   HOH A5181     -11.604   1.117  -0.345  1.00 12.54          Bi5+
HETATM 6810  O   HOH A5182     -17.302   0.369  30.581  1.00 10.82          Po
HETATM 6811  O   HOH A5183     -19.659 -11.610  29.687  1.00 11.09          At
HETATM 6812  O   HOH A5184      -3.968   1.929  -3.764  1.00 12.35          Rn
HETATM 6813  O   HOH A5185      11.407 -18.267  17.735  1.00 12.98          Fr
HETATM 6814  O   HOH A5186       5.397  25.468  22.317  1.00 12.46          Ra
HETATM 6815  O   HOH A5187      -4.717   4.208  -2.299  0.60 11.91          Ra2+
HETATM 6816  O   HOH A5188     -24.859  13.594  20.904  0.80 10.07          Ac
HETATM 6817  O   HOH A5189      -0.525 -29.946  20.292  1.00 11.70          Ac3+
HETATM 6818  O   HOH A5190     -24.085 -10.808  12.682  0.80  9.23          Th
HETATM 6819  O   HOH A5191       2.450  17.612  37.060  1.00 14.59          Th4+
HETATM 6820  O   HOH A5192      -8.704  -4.915  31.699  0.90  9.67          Pa
HETATM 6821  O   HOH A5193      -4.418 -30.056  18.178  0.60  5.84           U
HETATM 6822  O   HOH A5194      -2.425  -5.196  -4.808  1.00 14.11           U3+
HETATM 6823  O   HOH A5195     -16.770  28.630  18.033  1.00 13.65           U4+
HETATM 6824  O   HOH A5196     -17.157  23.223  16.403  0.70 11.62           U6+
HETATM 6825  O   HOH A5197     -17.100 -11.582  -2.706  1.00 14.26          Np
HETATM 6826  O   HOH A5198       4.790   5.726  -0.392  0.50 14.83          Np3+
HETATM 6827  O   HOH A5199       0.569  27.671  27.800  1.00 16.07          Np4+
HETATM 6828  O   HOH A5200       5.999  -4.767  -2.338  0.60  8.51          Np6+
HETATM 6829  O   HOH A5201     -15.871  26.197  30.725  1.00 15.27          Pu
HETATM 6830  O   HOH A5202       6.613  -0.513  20.819  1.00 14.76          Pu3+
HETATM 6831  O   HOH A5203     -15.579  -3.630  26.346  0.70  7.25          Pu4+
HETATM 6832  O   HOH A5204      -2.469   7.614  37.998  1.00 15.95          Pu6+
HETATM 6833  O   HOH A5205     -23.621  -8.303  15.805  0.80  9.45          Am
HETATM 6834  O   HOH A5206     -19.652  -9.388  23.334  0.80 16.78          Cm
HETATM 6835  O   HOH A5207     -21.063 -13.891  29.633  0.69  9.58          Bk
HETATM 6836  O   HOH A5208       6.155 -19.205   4.041  1.00 13.10          Cf
"""

if (__name__ == "__main__"):
  t0 = time.time()
  run()
  print("OK. Time:", round(time.time()-t0, 2))
