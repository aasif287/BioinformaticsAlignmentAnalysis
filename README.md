# Needleman-Wunsch Algorithm with Fixed Gap Costs

This Python script, `NW_GE.py`, implements the Needleman-Wunsch algorithm to perform pairwise sequence alignment for DNA sequences. The algorithm uses fixed gap costs with the following parameters:

- **Match Score:** 1
- **Mismatch Score:** -1
- **Gap Open:** -2
- **Gap Extend (for extra credit):** -0.5
  
## Notes

- **Alignability Assumption:** This implementation assumes that the input sequences are alignable.
  
- **Alignment Matrix and Error Handling:** The script does not provide the alignment matrix and error handling is not implemented, as the input is assumed to be valid.

- **Single Alignment Output:** The output file will provide Only one correct alignment.

- **Tool Usage and Dependencies:** Existing tools, Python packages, calls to outside programs, and code found on the internet are not used in this implementation.
  
-  **File Reference:** Note that in the script, `open(sys.argv[1])` refers to `seq_file.fna` when the script was run on Amarel, a computing system offered at Rutgers Univeristy.
  
## Usage

To run the script, use the following command:

```bash
python NW_GE.py some_file_name.fasta

