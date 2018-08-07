# TigTRIM
A tool to trim contig ID's to 20 character or less, based on input filenames.

## Quick start
    tigtrim.py -i /path/to/directory/with/fastas -o /path/to/output/processed/fastas

## Usage

    usage: tigtrim.py [-h] -i INPUT -o OUTPUT [-r]

    A tool trim contig ID's to 20 characters or less using input filenames.

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            Path to directory containing .fasta files.
      -o OUTPUT, --output OUTPUT
                            Path to output destination.
      -r, --replace         Edits fasta in place, overwriting the file.
  
### What?
Replaces all contig headers (defined by ">") with the filename, followed by a sequential number. If your filename (excluding .fasta extension) is longer than 17 characters, it will be trimmed. 
  
### Why?
If you try to annotate the output of SPAdes/Velvet with PROKKA, you'll get an error. The tbl2asn module that PROKKA uses to parse the .gbk output requires contigs headers to be shorter than 20 characters. There are ways around this within PROKKA, but I found this to be a neater solution for my needs.

#### Writing in place
I've tried to stop any accidental overwriting of input files - it will ask you to continue if you accidentally provide the same input and output directory. To bypass this prompt, use the -r flag. 
