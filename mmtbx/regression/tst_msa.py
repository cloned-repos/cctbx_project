
import mmtbx.msa
import libtbx.load_env
from cStringIO import StringIO

def exercise () :
  if (not libtbx.env.has_module(name="muscle")) :
    print "Skipping MUSCLE tests: muscle module not available."
    return
  fasta_sequences = """\
>1MRU_A
GSHMTTPSHLSDRYELGEILGFGGMSEVHLARDLRLHRDVAVKVLRADLARDPSFYLRFRREAQNAAALNHPAIVAVYDT
GEAETPAGPLPYIVMEYVDGVTLRDIVHTEGPMTPKRAIEVIADACQALNFSHQNGIIHRDVKPANIMISATNAVKVMDF
GIARAIADSGNSVTQTAAVIGTAQYLSPEQARGDSVDARSDVYSLGCVLYEVLTGEPPFTGDSPVSVAYQHVREDPIPPS
ARHEGLSADLDAVVLKALAKNPENRYQTAAEMRADLVRVHNGEPPEAPKVLTDAERTSLLSSAAGNLSGPR
>1L3R_E
GNAAAAKKGSEQESVKEFLAKAKEDFLKKWETPSQNTAQLDQFDRIKTLGTGSFGRVMLVKHKESGNHYAMKILDKQKVV
KLKQIEHTLNEKRILQAVNFPFLVKLEFSFKDNSNLYMVMEYVAGGEMFSHLRRIGRFSEPHARFYAAQIVLTFEYLHSL
DLIYRDLKPENLLIDQQGYIQVTDFGFAKRVKGRTWTLCGTPEYLAPEIILSKGYNKAVDWWALGVLIYEMAAGYPPFFA
DQPIQIYEKIVSGKVRFPSHFSSDLKDLLRNLLQVDLTKRFGNLKNGVNDIKNHKWFATTDWIAIYQRKVEAPFIPKFKG
PGDTSNFDDYEEEEIRVSINEKCGKEFTEF
>2A19_B
GAHTVDKRFGMDFKEIELIGSGGFGQVFKAKHRIDGKTYVIKRVKYNNEKAEREVKALAKLDHVNIVHYNGCWDGFDYDP
ETSSKNSSRSKTKCLFIQMEFCDKGTLEQWIEKRRGEKLDKVLALELFEQITKGVDYIHSKKLINRDLKPSNIFLVDTKQ
VKIGDFGLVTSLKNDGKRTRSKGTLRYMSPEQISSQDYGKEVDLYALGLILAELLHVCDTAFETSKFFTDLRDGIISDIF
DKKEKTLLQKLLSKKPEDRPNTSEILRTLTVWKKSPEKNERHTA"""
  clustal_aln = mmtbx.msa.get_muscle_alignment(fasta_sequences)
  assert (clustal_aln.names == ['1MRU_A', '2A19_B', '1L3R_E'])
  assert (len(clustal_aln.alignments[0]) == 371)
  pdb_sequences = [
    "XXATKGQNEPKKHFMVILSTCYGWSDD",
    "VTKGNDPKRHYIVLLTGAGSCFGWSDDARY",
    "GSHXXATKGQNDPKRHYMILSCYGWDDRY",
  ]
  pdb_names = ["pdb1","pdb2","pdb3"]
  pdb_offsets = [0, 0, 3]
  reference_sequence = "MIATKGQNEPKKHFMVILSTCYGWSDDAKFGG"
  for arg in [False, True] :
    m = mmtbx.msa.align_pdb_residues(
      pdb_sequences=pdb_sequences,
      pdb_names=pdb_names,
      pdb_offsets=pdb_offsets,
      reference_sequence=reference_sequence,
      substitute_names=arg)
    assert (m.convert_residue_number("pdb3", -2) is None)
    assert (m.convert_residue_number("pdb1", 10) == 10)
    assert (m.convert_residue_number("pdb2", 5) == 8)
    assert (m.convert_residue_number("pdb2", 16) == 19)
    assert (m.convert_residue_number("pdb2", 18) is None)
    assert (m.convert_residue_number("pdb1", 27) == 27)
    assert (m.convert_residue_number("pdb2", 30) == 30)
  pdb_str = """\
ATOM      2  CA  GLY A   3      -9.052   4.207   4.651  1.00 16.57           C
ATOM      6  CA  ASN A   4      -6.522   2.038   2.831  1.00 14.10           C
ATOM     14  CA  ASN A   5      -3.193   1.904   4.589  1.00 11.74           C
ATOM     22  CA  GLN A   6       0.384   1.888   3.199  1.00 10.53           C
ATOM     22  CA  ALA A   6A      0.384   1.888   3.199  1.00 10.53           C
ATOM     22  CA  GLY A   6B      0.384   1.888   3.199  1.00 10.53           C
ATOM     31  CA  GLN A   7       3.270   2.361   5.640  1.00 11.39           C
ATOM     40  CA  ASN A   8       6.831   2.310   4.318  1.00 12.30           C
ATOM     48  CA  TYR A   9       9.159   2.144   7.299  1.00 15.18           C
TER
ATOM     50  O   HOH     1       0.000   0.000   0.000  1.0  20.0            O
END
"""
  open("tmp1.pdb", "w").write(pdb_str)
  open("tmp2.fa", "w").write(">tmp2\nAVGNNQQNY")
  open("tmp3.fa", "w").write(">tmp3\nNNQQNY")
  open("tmp4.dat", "w").write("AVNNQQNF")
  params = mmtbx.msa.master_phil.fetch().extract()
  params.muscle.seq_file.extend(["tmp1.pdb", "tmp2.fa", "tmp3.fa", "tmp4.dat"])
  (aln_file, alignment) = mmtbx.msa.run(params=params, out=StringIO())
  assert (alignment ==
    "MUSCLE (3.8) multiple sequence alignment\n\n\n"+
    "tmp4            AV-NNQ--QNF\n"
    "tmp1_A          XXGNNQAGQNY\n"
    "tmp2            AVGNNQ--QNY\n"
    "tmp3            ---NNQ--QNY\n"
    "                   ***  **:")
  print "OK"

if __name__ == "__main__" :
  exercise()
