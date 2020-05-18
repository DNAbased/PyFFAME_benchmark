### taken from https://github.com/hemberg-lab/MPRAnator/blob/master/downloadables/MpraSnps_script.py
### single hash: original comments ('#')
### triple hash: own comments ('###')
### modified to work with the creator's current website
### written for python2.x?
import sys
import requests

url = "http://genomegeek.com/MPRA/SNPs/Results/" ### not up to date in github repo (exact path and https)
fileToWriteResults = "mpranator_out.fa"
'''
# MPRA Sample Data change as appropriate.
sequenceS = ">sequence1chr1:42990-43041,testest\nACAGATTAGTCAGTACGGCTAGCTAGCTACGTCTATATTATAGCGATACGGG"
snpS = "1\t42991\trs43434\tT\tG\n1\t43030\trs121212\tA\tG" ### single space sufficient?
### that does not look right; does this pipeline not check for the correct ref base at the respective position?
'''
with open('./context_00100.fa', 'r') as f:
    sequenceS = f.read()
with open('./00100_dataset_split_reordered.vcf', 'r') as f:
    snpS = f.read()
### due to length restriction of 10 nt, 1 variant was removed from the 500 dataset
### due to length restriction of 10 nt, 3 variants were removed from the 1k dataset
### due to length restriction of 10 nt, 7 variants were removed from the 3k dataset
### due to length restriction of 10 nt, 8 variants were removed from the 5k dataset
### due to length restriction of 10 nt, 16 variants were removed from the 10k dataset (still leading to a 504 gateway timeout...)
### note: the competitiveness is difficult to judge as the computations are performed on a remote server

# ordering of output
barcodeOrder = "Barcode,"
backgroundOrder = "Background,"
restriction1Order = "restriction site 1,"
restriction2Order = "restriction site 2,"
adapter1Order = "adapter site 1,"
adapter2Order = "adapter site 2,"

# Change the ordering below as appropriate. Just move the variables in your 
# desired order.
ordering = barcodeOrder + backgroundOrder + restriction1Order + restriction2Order + adapter1Order + adapter2Order

# Data below is optional. Add the appropriate parameters. Default numbers are given below.
barCodeDistance = "1"
barCodeLength = "11"
minimumGCContent = "1"
maximumGCContent = "100"
numOfBarCodesPerSequence = "3"
restriction1 = ""
restriction2 = ""
adapter1 = ""
adapter2 = ""

# put data in a dictionary
data = {"sequenceS":sequenceS,
"SnpS":snpS,
"ordering":ordering,
"barCodeDistance":barCodeDistance,
"barCodeLength":barCodeLength,
"minimumGCContent":minimumGCContent,
"maximumGCContent":maximumGCContent,
"numOfBarCodesPerSequence":numOfBarCodesPerSequence,
"restriction1":restriction1,
"restriction2":restriction2,
"adapter1":adapter1,
"adapter2":adapter2,
"usingDownload":True,
}

# Posting the data.
result = requests.post(url = url, data = data)

# writing the results 
openfile = open(fileToWriteResults, "w")
openfile.write(str(result.content)) ### had to add str, because output was byte?!
openfile.close()
### output still contains '\n's?

### results
### replicate 1: 1.73 seconds
### replicate 2: 2.51 seconds
### replicate 3: 1.85 seconds
### replicate 4: 2.58 seconds
### replicate 5: 1.72 seconds
