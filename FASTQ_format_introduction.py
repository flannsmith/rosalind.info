# Given: FASTQ file

# Return: Corresponding FASTA records

from sys import argv
from Bio import SeqIO
from io import StringIO


def main():
    out_handle = StringIO("")
    SeqIO.convert(argv[1], "fastq", out_handle, "fasta")
    print (out_handle.getvalue().strip())


if __name__ == "__main__":
    main()
