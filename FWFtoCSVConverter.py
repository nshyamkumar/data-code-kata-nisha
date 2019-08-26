#############################################################################
#===========================================================================#
#To generate a fixed width file as per the config given in a spec.json file,#
#then parse the generated fwf file  and write it to a delimited file        #
#============ Author- Nisha Shyamkumar =====================================#
#===========================================================================#
#############################################################################

#################################################################
#######################Import Packages###########################
#################################################################
import json
from itertools import accumulate
from operator import itemgetter

#################################################################
#############           Declare variables        ################
#################################################################
FWFFILE = 'fixedwidthfile.txt'
CONFIGFILE = 'spec.json'
OPCSVFILE = 'csvoutput.txt'
ENDOFL = '\n'
DELIMITER_CSV = '|'
line_list = ['Mike VanmooreVIC8433WilliamsAvenue  svert4562   0109hndcjk   Herellllbnm56677   7788998899000',
            'Kate Johnas PLC8438ParkinsStreet 67894562   Wise0109hndcjk7892345fghjk12345678910234ab']
			
#################################################################
######         Read config from spec.json              ##########
#################################################################
def readSpec(CONFIGFILE):
    with open(CONFIGFILE, 'r') as fconfig:
        config_dict = json.load(fconfig)
        fconfig.close()
        return config_dict

#################################################################
######         Build header line for the fwf file        ########
#################################################################
def buildHeaderForFWF(config_dict):
    headerfwf = ''
    for idx,columnname in enumerate(config_dict['ColumnNames']):
        headerfield = columnname.ljust(int(config_dict['Offsets'][idx]),' ')
        headerfwf = headerfwf+headerfield
    return headerfwf
	
########################################################################################
###### Build each fwf record and return as a list of records for the fwf file    ########
########################################################################################
def buildFwfRec(config_dict, line_list): 
    line_listfwf=[]
    for line in line_list:
        position = 0
        line_fwf=''
        for idx,columnname in enumerate(config_dict['ColumnNames']):
            field = line[position:position+int(config_dict['Offsets'][idx])].ljust(int(config_dict['Offsets'][idx]),' ')
            position = position+int(config_dict['Offsets'][idx])
            line_fwf = line_fwf+field
        line_listfwf.append(line_fwf)
    return line_listfwf

####################################################################################
######         Write to fwf file                          ##########################
######Uses 'windows-1252'(as in spec.json) encoding while writing to fwf file#######
#####  Header will be written only if 'IncludeHeader' is True          #############
####################################################################################
def writeFwfFile(OPFWFFILE,config_dict,headerfwf,rec_listfwf):   
    with open(OPFWFFILE,'w',encoding=config_dict['FixedWidthEncoding']) as ffwf:
        if config_dict['IncludeHeader'] == 'True':
            ffwf.write(headerfwf+ENDOFL)
        for rec_fwf in rec_listfwf:
            ffwf.write(rec_fwf+ENDOFL)
    ffwf.close()
    return

#######################################################################################
##Converts string offsets from spec file to integers for easiness while parsing fwf ###
#######################################################################################
def convertOffsetsToInt(field_widths):
    fieldwidths = []
    for width in field_widths:
        fieldwidths.append(int(width))
    return fieldwidths

#################################################################
######      Function to parse a fwf record               ########
#################################################################

def fwfParser(fWidths):
    sum_arg = tuple(accumulate(abs(width) for width in fWidths))
    cuts = tuple(index for index,width in enumerate(fWidths) if width < 0)
    # Get slice args
    ig_args = tuple(item for index, item in enumerate(zip((0,)+sum_arg,sum_arg)) if index not in cuts)
    # Generate `operator.itemgetter` object
    oprtObj =itemgetter(*[slice(s,e) for s,e in ig_args])
    return oprtObj

######################################################################################################
###### Function to parse the fwf file and write to a csv output file #################################
###### Uses 'windows-1252' encoding ( as in spec.json) while reading fwf file#########################
###### Uses 'utf-8' encoding ( as in spec.json) while writing to csv file#############################
#####Header will be written only if 'IncludeHeader' is set to 'True'  in  spec.json ##################
######################################################################################################
def fwfToCSVWriter(FWFFILE,OPCSVFILE,fieldwidths,fwf_encoding,delimited_encoding,include_header):
    with open(FWFFILE,"r",encoding = fwf_encoding) as ffwf,open(OPCSVFILE,'w',encoding = delimited_encoding) as fcsv:
        count = 0
        for row in ffwf:
            #skip header if needed
            if count==0 and include_header != 'True':
                count = count+1
                continue
            parse = fwfParser(fieldwidths)
            fields = parse(row)
            line = DELIMITER_CSV.join(fields)
            fcsv.write(line+ENDOFL)
    ffwf.close()
    fcsv.close()
    return

#################################################################
###### Main function                                     ########
#################################################################

if __name__ == "__main__":
    config_dict = readSpec(CONFIGFILE)
    header_fwf = buildHeaderForFWF(config_dict)
    rec_listfwf = buildFwfRec(config_dict,line_list)
    writeFwfFile(FWFFILE,config_dict,header_fwf,rec_listfwf)
    field_int_widths = convertOffsetsToInt(config_dict['Offsets'])
    fwfToCSVWriter(FWFFILE,OPCSVFILE,field_int_widths,config_dict['FixedWidthEncoding'],config_dict['DelimitedEncoding'],config_dict['IncludeHeader'])
  