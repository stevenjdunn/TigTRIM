#!/usr/bin/env python
import os
import argparse
import sys
import glob

# Version
_verion_= "0.1"

# Argparse Setup
parser = argparse.ArgumentParser(description="A tool trim contig ID's to 20 characters or less using input filenames.")
parser.add_argument("-i", "--input", required=True, help="Path to directory containing .fasta files.")
parser.add_argument("-o", "--output", required=True, help="Path to output destination.")
parser.add_argument("-r", "--replace", action='store_true', help="Edits fasta in place, overwriting the file.")
args = parser.parse_args()

# Orientation + Directory Creation
print('###################')
print('Welcome to TigTRIM!')
print('###################', '\n', '\n')

def farewell():
	print('\n','\n')
	print('Author: www.github.com/stevenjdunn','\n','\n')
	print('#########')
	print('Finished!')
	print('#########')

invoked_from = os.getcwd()
if not os.path.exists(args.output):
	try:
		os.makedirs(args.output)
		print('Output directory created.','\n')
	except Exception:
		print('Could not create output directory.','\n','\n', 'Please check whether you have the required permissions.')
		sys.exit(1)
os.chdir(args.output)
output_directory = os.getcwd()
os.chdir(invoked_from)
os.chdir(args.input)
input_directory = os.getcwd()
os.chdir(invoked_from)


# Fasta discovery
fasta_in = list(glob.glob(os.path.join(input_directory,'*.fasta')))
file_names = [x.replace(input_directory,'').replace('/','').replace('.fasta','') for x in fasta_in]


# Overwrite Warning
if input_directory == output_directory and not args.replace:
	print('')
	print('Input and output directory are the same.')
	print('')
	print('Files will be overwritten.')
	print('')
	print('')
	prompt = input('Do you want to continue? (Y/N):')
	prompt = prompt.upper()
	choices = ['Y','YE','YES','YEET']
	if prompt not in choices:
		print('')
		print('Exiting...')
		farewell()
		sys.exit(0)
	if prompt in choices:
		print('')
		print('To avoid this message in the future, use the -r/--replace flag.')

# Replace setup
if not args.replace:
	fasta_out = [x.replace(input_directory,output_directory) for x in fasta_in]
else:
	fasta_out = fasta_in

# Filename length check
for x in file_names:
	if len(x) >= 17:
		print('Filename ', x, ' is too long and will be shortened to: ', x[:17])
		file_names[:] = (item[:17] for item in file_names)

# Parse file and write to output.
print('')
print('Processing fasta files...')
print('')
for fin,fout,fnam in zip(fasta_in, fasta_out, file_names):
	x = open(fin)
	y = open(fout, 'w')
	contig_num = 1
	for line in x.readlines():
			if line.startswith('>'):
				new_header = '>' + fnam + '_' + str(contig_num) + '\n'
				y.write(new_header)
				contig_num += 1
			else:
				y.write(line)
	y.close()
	x.close()

# Farewell
print('')
print('')
print('Done!','\n')
print('Output files located in:', output_directory,'\n','\n')
farewell()
