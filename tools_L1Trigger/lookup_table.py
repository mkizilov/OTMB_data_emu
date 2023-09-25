import os

def create_txt_file(path, file_name, content):
    # Get the CMSSW_BASE environment variable
    cmssw_base = os.getenv('CMSSW_BASE')
    
    # Construct the full path to the src directory
    src_dir = os.path.join(cmssw_base, path)
    
    # Create the file path for the new text file
    file_path = os.path.join(src_dir, file_name)
    
    # Check if the file already exists and remove it if it does
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Write the content to the file
    with open(file_path, 'w') as file:
        file.write(content)

def files_content_generator():
    content = ""
    for i in range(1, 100):
        content+= f"{i} 20\n"
    return content



if __name__ == "__main__":
    # Replace these values with the desired file name and content

    path = 'src/L1Trigger/CSCTriggerPrimitives/data/GEMCSC/AlignmentCorrection'
    file_header = """# dPhi=rechit local phi - prophit local phi [created in units of mRad]. dPhi corrected calculation takes the firmware long and short superchambers orientation into account on +/- endcaps, i.e.
#       R+1      R-1
# Even  -1       +1
# Odd   +1       -1
# Shift [strip(8)] is calculated by the following conversion rule: 0.37 [mRad] = 1 [strip(8)]
# cuts: 30GeV<muon_pt<200GeV, has_fidcut, n_ME11_segment=1, |RdPhi_Corrected|<2cm, |dPhi_Corrected|<4mRad, has_TightID, endcap, station, superchamber, eta
# [filename for TA's notekeeping]: ntuple: Run2022D_ZMu_PromptReco_RAWRECO_globalMu_pfisotight_idealGEMonCSC_v1.root]
# =================================================================================================================
# Superchamber_Eta | Shift [strip(8)]
"""

    files_info= [
        {"file": "GEMCSCLUT_align_corr_es_ME11_negative_endcap.txt", "content": file_header + files_content_generator()},
        {"file": "GEMCSCLUT_align_corr_es_ME11_positive_endcap.txt", "content": file_header + files_content_generator()},
        {"file": "GEMCSCLUT_align_corr_es_ME21_negative_endcap.txt", "content": file_header + files_content_generator()},
        {"file": "GEMCSCLUT_align_corr_es_ME21_positive_endcap.txt", "content": file_header + files_content_generator()}
    ]

    for file_info in files_info:
        create_txt_file(path, file_info["file"], file_info["content"])
        print(f"File {path + file_info['file']} has been created")
    
